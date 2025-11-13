# Structure of dual BON-domain protein DolP identifies phospholipid binding as a new mechanism for protein localisation

## Authors

- Jack Alfred Bryant<sup>1</sup> ([ORCID: 0000-0002-7912-2144](https://orcid.org/0000-0002-7912-2144))
- Faye C Morris<sup>1</sup> ([ORCID: 0000-0002-9021-0452](https://orcid.org/0000-0002-9021-0452))
- Timothy J Knowles<sup>1</sup>
- Riyaz Maderbocus<sup>1</sup>
- Eva Heinz<sup>4</sup> ([ORCID: 0000-0003-4413-3756](https://orcid.org/0000-0003-4413-3756))
- Gabriela Boelter<sup>1</sup>
- Dema Alodaini<sup>1</sup>
- Adam Colyer<sup>1</sup>
- Peter J Wotherspoon<sup>1</sup>
- Kara A Staunton<sup>1</sup>
- Mark Jeeves<sup>3</sup>
- Douglas F Browning<sup>1</sup>
- Yanina R Sevastsyanovich<sup>1</sup>
- Timothy J Wells<sup>1</sup>
- Amanda E Rossiter<sup>1</sup>
- Vassiliy N Bavro<sup>1</sup>
- Pooja Sridhar<sup>2</sup>
- Douglas G Ward<sup>2</sup>
- Zhi-Soon Chong<sup>5</sup>
- Emily CA Goodall<sup>1</sup> ([ORCID: 0000-0003-4846-6566](https://orcid.org/0000-0003-4846-6566))
- Christopher Icke<sup>1</sup> ([ORCID: 0000-0002-7815-8591](https://orcid.org/0000-0002-7815-8591))
- Alvin CK Teo<sup>7</sup>
- Shu-Sin Chng<sup>5</sup> ([ORCID: 0000-0001-5466-7183](https://orcid.org/0000-0001-5466-7183))
- David I Roper<sup>7</sup>
- Trevor Lithgow<sup>4</sup>
- Adam F Cunningham<sup>1</sup>
- Manuel Banzhaf<sup>1</sup>
- Michael Overduin<sup>2</sup> †
- Ian R Henderson<sup>1</sup> ([ORCID: 0000-0002-9954-4977](https://orcid.org/0000-0002-9954-4977)) †

### Affiliations

1. Institute of Microbiology and Infection, University of Birmingham Edgbaston United Kingdom
2. School of Biosciences, University of Birmingham Edgbaston United Kingdom
3. Institute for Cancer and Genomic Sciences, University of Birmingham Edgbaston United Kingdom
4. Infection & Immunity Program, Biomedicine Discovery Institute and Department of Microbiology, Monash University Clayton Australia
5. Department of Chemistry, National University of Singapore Singapore Singapore
6. Institute for Molecular Bioscience, University of Queensland St. Lucia Australia
7. School of Life Sciences, The University of Warwick Coventry United Kingdom
8. Institute of Inflammation and Immunotherapy, University of Birmingham Edgbaston United Kingdom
9. Department of Biochemistry, University of Alberta Edmonton Canada

† Corresponding author

## Abstract

The Gram-negative outer-membrane envelops the bacterium and functions as a permeability barrier against antibiotics, detergents, and environmental stresses. Some virulence factors serve to maintain the integrity of the outer membrane, including DolP (formerly YraP) a protein of unresolved structure and function. Here, we reveal DolP is a lipoprotein functionally conserved amongst Gram-negative bacteria and that loss of DolP increases membrane fluidity. We present the NMR solution structure for Escherichia coli DolP, which is composed of two BON domains that form an interconnected opposing pair. The C-terminal BON domain binds anionic phospholipids through an extensive membrane:protein interface. This interaction is essential for DolP function and is required for sub-cellular localisation of the protein to the cell division site, providing evidence of subcellular localisation of these phospholipids within the outer membrane. The structure of DolP provides a new target for developing therapies that disrupt the integrity of the bacterial cell envelope.

## Introduction

Gram-negative bacteria are intrinsically resistant to many antibiotics and environmental insults, which is largely due to the presence of their hydrophobic outer membrane (OM). This asymmetric bilayer shields the periplasmic space, a thin layer of peptidoglycan and the inner membrane (IM). In the model bacterium Escherichia coli, the IM is a symmetrical phospholipid bilayer, whereas the OM has a more complex organisation with lipopolysaccharide (LPS) and phospholipids forming an asymmetric bilayer containing integral β-barrel proteins (May and Grabowicz, 2018; Konovalova et al., 2017). The OM is also decorated with lipoproteins (approximately 75 have been identified in E. coli), many of which, are functional orphans (Leyton et al., 2012; Babu et al., 2006). Biogenesis of the OM is completed by several proteinaceous systems, which must bypass the periplasmic, mesh-like peptidoglycan (Konovalova et al., 2017; Egan, 2018; Ekiert et al., 2017; Stubenrauch and Lithgow, 2019). The growth of all three envelope layers must be tightly coordinated in order to maintain membrane integrity. Improper coordination can lead to bacterial growth defects, sensitivity to antibiotics, and can cause cell lysis (Egan, 2018; Gray et al., 2015).

DolP (division and OM stress-associated lipid-binding protein; formerly YraP) is a nonessential protein found in E. coli and other Gram-negative bacteria (Goodall et al., 2018). Loss of DolP results in the disruption of OM integrity, induces increased susceptibility to detergents and antibiotics, and attenuates the virulence of Salmonella enterica (Morris et al., 2018). Importantly, DolP is a crucial component of the serogroup B meningococcal vaccine where it enhances the immunogenicity of other components by an unknown mechanism (Bos et al., 2014). Recently, the dolP gene was connected genetically to the activation of peptidoglycan amidases during E. coli cell division, however this activity has not been directly confirmed experimentally (Tsang et al., 2017). In contrast, protein interactome studies suggest DolP is a component of the β-barrel assembly machine (Bam) complex (Carlson et al., 2019; Babu et al., 2018). While these data suggest that DolP may be involved in outer-membrane protein (OMP) biogenesis and the regulation of peptidoglycan remodeling, its precise function in either of these processes remained unclear. Nonetheless, given its roles in these vital cell envelope processes, and its requirement for virulence and the maintenance of cell envelope integrity, DolP is a potential target for the development of therapeutics.

In this study, we demonstrate that DolP is an outer-membrane lipoprotein functionally conserved amongst Gram-negative bacteria, but with a function distinct from other BON (Bacterial OsmY and nodulation) domain-containing proteins. We solve the NMR solution structure of DolP revealing the first view of a dual BON-domain fold. Extensive structural and functional analyses define a membrane:protein interface that binds DolP to anionic phospholipids and provides the basis for a new mechanism for targeting proteins to the cell division site. We show that loss of dolP affects OM fluidity, which perturbs the BAM complex, suggesting an indirect role for DolP in OMP biogenesis. The insights provided here not only advance our understanding of how DolP functions but provide a basis for beginning to develop drugs to target it.

## Results

### DolP belongs to an extensive family of lipoproteins required for OM homeostasis

In E. coli, the dolP gene is located downstream of the genes encoding LpoA (an activator of PBP1A) (Typas et al., 2010), YraN (a putative Holiday-Junction resolvase), and DiaA (a regulator of chromosomal replication) (Ishida et al., 2004), and two σE-dependent promoters are found immediately upstream of the dolP gene (Dartigalongue et al., 2001; Figure 1A). Bioinformatic analyses predicted that dolP encodes a lipoprotein with two putative domains of unknown function, termed BON domains (Yeats and Bateman, 2003), as well as a Lol-dependent OM targeting signal sequence where acylation was predicted to occur on cysteine residue C19. To test the hypothesis that DolP is localised to the periplasmic face of the OM, we raised an antiserum to the protein to probe subcellular fractions. DolP was found in the Triton X-100 insoluble fraction of the E. coli cell envelope along with other OM proteins. As a control for the antiserum, DolP was absent from Triton X-100 insoluble fractions of cell envelopes harvested from E. coli ΔdolP (Figure 1—figure supplement 1A). Furthermore, expression of a C19A point mutant, preventing N-terminal acylation, effectively eliminated DolP from the OM fractions (Figure 1—figure supplement 1B). Unlike the lipoproteins BamC and Lpp, which can be surface localized (Cowles et al., 2011; Webb et al., 2012), DolP was not accessible to antibody or protease in intact E. coli cells. However, DolP could be labelled and degraded when OM integrity was compromised (Figure 1—figure supplement 1C,D), confirming that DolP is predominantly targeted to the inner leaflet of the OM, localizing it within the periplasmic space.

![Figure 1.](https://cdn.elifesciences.org/articles/62614/elife-62614-fig1-v2.jpg)

**Figure 1.:** (A) In E. coli, dolP is located downstream of diaA and encodes a lipoprotein with a signal sequence (orange) and two BON domains (red). The signal sequence is cleaved by LspA, the cysteine at position 19 acylated by Lgt and Lnt and finally the protein is targeted to the OM by the Lol system (Figure 1—figure supplement 1). E. coli contains three BON-domain proteins. DolP shares a similar domain organisation with OsmY, which encodes a periplasmic protein that possesses a signal sequence (green) which is recognised and cleaved by the signal peptidase LepB. Kbp is more divergent from DolP and OsmY, has no predictable signal sequence and is composed of BON and LysM domains (Figure 1—figure supplement 2). (B) DolP, OsmY and Kbp are widespread amongst proteobacteria, and cluster into three distinct groups based on the program CLANS (Frickey and Lupas, 2004) with connections shown for a P value cut-off of <10−2 (Table 4). (C) Growth phenotypes for mutant isolates lacking DolP (ΔdolP), wild-type strain (WT) or the complemented mutant (COMP). Strains were grown on LB agar containing vancomycin (100 μg/ml) or sodium dodecyl sulphate (SDS; 4.8%). (D) DolP from diverse proteobacterial species expressed in an E. coli ΔdolP strain restores growth in the presence of vancomycin as assessed by a serial dilution plate growth assay. Plasmids expressing OsmY do not complement the defect.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/62614/elife-62614-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) OM fractions of E. coli BW25113, an isogenic ∆dolP mutant and the complemented mutant were analysed by SDS-PAGE and Western immunoblotting with antibodies to DolP and the known OM lipoproteins BamC and BamE. DolP is not detected in the mutant but like BamC and BamE is found with the membrane fraction. (B) Western immunoblotting of OM fractions from E. coli ∆dolP complemented with a plasmid (pDolP-C19A) encoding DolP with a point mutation at position C19. (C) E. coli cells treated with protease in the presence (+) or absence (-) of polymyxin B, which permeablises the OM, allowing the protease access to the periplasm. Antibodies to the cytoplasmic RNA polymerase (RNAP) and the periplasmic chaperone SurA were used as controls. (D) Immunofluorescence photomicrographs of E. coli BW25113, an isogenic ∆dolP mutant and the complemented mutant. Cells were probed with anti-DolP before and after permeabilisation. Anti-SurA was used as a control.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/62614/elife-62614-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** The Pfam database was interrogated for the presence of proteins containing BON domains. BON domains are widely distributed in bacteria and eight major architectures are noted (Table 1). The predominant architecture is that observed for DolP and OsmY where the protein possesses a signal sequence and one or more BON domains. The second major architecture is that observed for Kbp, where proteins possess one or more BON domains and a LysM domain. The other major architectures include associations with Secretin (Pfam: PF00263), CBS (Pfam: PF00571), OmpA (Pfam: PF00691), MS_channel (Pfam: PF00924), FHA (Pfam: PF00498) or cytidylate kinase (Pfam: PF13189) domains. Due to their functions, many of these domains would place their associated BON domains in proximity to cell membranes.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/62614/elife-62614-fig1-figsupp3-v2.jpg)

**Figure 1—figure supplement 3.:** The precise functions of Kbp and OsmY are unknown, though both are induced during adaptation to hyperosmolarity (Yan et al., 2019; Yim and Villarejo, 1992; Weber et al., 2006; Ashraf et al., 2016; Lennon et al., 2015) (A) Investigation of osmY and kbp null mutants of E. coli revealed neither was sensitive to vancomycin or SDS. Growth phenotypes for mutant isolates lacking BON-domain proteins, wild-type strains (WT) or complemented mutants (COMP). Strains were grown on LB agar containing vancomycin (100 μg/ml) or sodium dodecyl sulphate (SDS; 4.8%). (B) A plasmid encoding a DolP-OsmY chimeric protein composed of the lipoprotein targeting sequence of DolP and the BON domains of OsmY failed to complement the OM defect associated with loss of dolP. (C) E. coli BW25113 ΔdolP is not more susceptible to osmotic stress induced by NaCl than the parent strain as assessed by a serial dilution plate assay. Interestingly, our investigations did not reveal a role for either kbp or osmY in survival of osmotic stress as the E. coli BW25113 parent strain and isogenic osmY::aph and kbp::aph mutants survived equally well.

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/62614/elife-62614-fig1-figsupp4-v2.jpg)

**Figure 1—figure supplement 4.:** (A) Mutants lacking dolP are sensitive to the anionic detergents cholate and deoxycholate (B) Mutants lacking dolP have growth rates that are indistinguishable from wild-type E. coli. (C) Scanning electron microscopy reveals parental and E. coli ∆dolP cells have no discernible differences in cellular morphology.

![Figure 1—figure supplement 5.](https://cdn.elifesciences.org/articles/62614/elife-62614-fig1-figsupp5-v2.jpg)

**Figure 1—figure supplement 5.:** The signal sequence and domain architecture of DolP are shown. The sequence changes to pET17b-dolPWT to create the construct targeting DolP to the IM (pET17b-dolPIM) are shown in red. The signal sequence of dolP was also swapped for that of pelB in order to create the construct pET17b-dolPpelB in order to target DolP to the periplasmic space with no modification. Fluorescence microscopy of ΔdolP cells expressing either DolPWT-mCherry or DolPIM-mCherry or DolPpelB-mCherry from the pET17b plasmid after growth to mid-exponential phase (OD600 ~0.4–0.8). Scale bars represent 2 μM and both phase contrast and the mCherry channel are shown in greyscale and red, respectively. The capacity of DolPWT, DolPIM, DolPWT-mCherry or DolPIM-mCherry to complement the ΔdolP mutant sensitivity phenotype was screened by dilution assay on 4.8% SDS. The expression of each construct was checked by Western blotting of total protein extracts with anti-DolP antiserum.

Further in silico analyses revealed the DolP lipoprotein was conserved across diverse species of Proteobacteria and is present even in organisms with highly-reduced genomes for example Buchnera spp (Table 1 and Supplementary file 1). The genome of E. coli contains three BON-domain-containing proteins: DolP, OsmY, and Kbp. DolP shares a dual BON-domain architecture and 29.5% sequence identity with OsmY, which is distinguished from DolP by a canonical Sec-dependent signal sequence. In contrast, Kbp consists of single BON and LysM domains and lacks a discernible signal sequence (Figure 1A). Our comprehensive analysis found seven predominant domains co-occurring with BON in different modular protein architectures across bacterial phyla, suggesting specialised roles for BON domains (Table 1 and Figure 1—figure supplement 2). Clustering analyses of sequences obtained by HMMER searches revealed DolP, OsmY and Kbp are distributed throughout the α, β, and γ-proteobacteria and form distinct clusters indicating that DolP has a role that is independent of OsmY and Kbp (Figure 1B). Our analyses demonstrated that OsmY and Kbp are not functionally redundant with DolP and isogenic mutants show distinct phenotypes, therefore confirming a distinct role for DolP in E. coli (Figure 1—figure supplement 3).

**Table 1.**
 Taxonomic distribution of BON family domain architectures.


<table>
  <thead>
    <tr>
      <th>Cluster number*</th>
      <th>UniRef100†</th>
      <th>Total number of proteins ‡</th>
      <th>Major domain architecture in cluster§</th>
      <th>α</th>
      <th>β</th>
      <th>γ</th>
      <th>δ</th>
      <th>ε</th>
      <th>ζ</th>
      <th>Aci††</th>
      <th>Act††</th>
      <th>Bac††</th>
      <th>Chl††</th>
      <th>Chl††</th>
      <th>Chl††</th>
      <th>Cya††</th>
      <th>Dei††</th>
      <th>Fib††</th>
      <th>Fir††</th>
      <th>Gem††</th>
      <th>Nit††</th>
      <th>Pla††</th>
      <th>Spi††</th>
      <th>Syn††</th>
      <th>The††</th>
      <th>The††</th>
      <th>The††</th>
      <th>Ver††</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>1280</td>
      <td>2723</td>
      <td>OsmY-like and 1 x BON</td>
      <td>41 (89)¶,**</td>
      <td>176 (533)</td>
      <td>1484 (1830)</td>
      <td>33 (56)</td>
      <td>12 (12)</td>
      <td>1 (1)</td>
      <td>6 (12)</td>
      <td>2 (3)</td>
      <td>5 (5)</td>
      <td>3 (11)</td>
      <td></td>
      <td>3 (4)</td>
      <td>43 (65)</td>
      <td>1 (1)</td>
      <td></td>
      <td>13 (13)</td>
      <td>1 (2)</td>
      <td>1 (1)</td>
      <td>14 (30)</td>
      <td>9 (9)</td>
      <td></td>
      <td>1 (1)</td>
      <td>1 (1)</td>
      <td></td>
      <td>7 (19)</td>
    </tr>
    <tr>
      <td>2</td>
      <td>833</td>
      <td>2395</td>
      <td>DolP-like</td>
      <td>97 (103)</td>
      <td>330 (335)</td>
      <td>1892 (1919)</td>
      <td>15 (17)</td>
      <td>2 (2)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>1 (1)</td>
      <td></td>
      <td></td>
      <td>1 (2)</td>
      <td></td>
      <td></td>
      <td>1 (1)</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>3</td>
      <td>579</td>
      <td>690</td>
      <td>three x BON + 1 x BON</td>
      <td>95 (187)</td>
      <td>108 (255)</td>
      <td>35 (36)</td>
      <td>18 (28)</td>
      <td></td>
      <td></td>
      <td>7 (23)</td>
      <td>14 (25)</td>
      <td>14 (30)</td>
      <td>2 (2)</td>
      <td></td>
      <td>3 (21)</td>
      <td>6 (10)</td>
      <td>5 (7)</td>
      <td>1 (1)</td>
      <td>32 (32)</td>
      <td>1 (2)</td>
      <td></td>
      <td>12 (27)</td>
      <td></td>
      <td></td>
      <td>1 (1)</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>4</td>
      <td>476</td>
      <td>537</td>
      <td>BON + secretin</td>
      <td>207 (276)</td>
      <td>77 (80)</td>
      <td>70 (117)</td>
      <td>32 (34)</td>
      <td></td>
      <td></td>
      <td>4 (4)</td>
      <td>1 (1)</td>
      <td></td>
      <td></td>
      <td>3 (3)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>10 (11)</td>
      <td></td>
      <td>1 (1)</td>
      <td>7 (7)</td>
      <td></td>
      <td>1 (1)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>5</td>
      <td>409</td>
      <td>1570</td>
      <td>Kbp-like</td>
      <td>66 (66)</td>
      <td>131 (132)</td>
      <td>1323 (1328)</td>
      <td>1 (1)</td>
      <td>1 (1)</td>
      <td></td>
      <td></td>
      <td></td>
      <td>31 (31)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>5 (5)</td>
      <td></td>
      <td>1 (1)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>1 (1)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>6</td>
      <td>282</td>
      <td>300</td>
      <td>CBS + CBS + BON</td>
      <td>82 (136)</td>
      <td>17 (29)</td>
      <td>4 (4)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>53 (127)</td>
      <td>4 (4)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>7</td>
      <td>220</td>
      <td>318</td>
      <td>BON + BON + OmpA</td>
      <td>157 (161)</td>
      <td>55 (57)</td>
      <td>9 (11)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>62 (64)</td>
      <td>1 (1)</td>
      <td></td>
      <td></td>
      <td></td>
      <td>19 (23)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>1 (1)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>8</td>
      <td>70</td>
      <td>75</td>
      <td>BON + Mschannel</td>
      <td>31 (32)</td>
      <td>1 (1)</td>
      <td>24 (25)</td>
      <td>2 (3)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>1 (1)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>8 (13)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9</td>
      <td>52</td>
      <td>52</td>
      <td>one x BON</td>
      <td></td>
      <td>1 (1)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>42 (51)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>10</td>
      <td>43</td>
      <td>80</td>
      <td>one x BON and 1 x DUF2204</td>
      <td></td>
      <td>1 (1)</td>
      <td>1 (1)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>77 (77)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>1 (1)</td>
    </tr>
    <tr>
      <td>11</td>
      <td>33</td>
      <td>87</td>
      <td>1–2 X Forkhead + BON</td>
      <td>2 (2)</td>
      <td>4 (4)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>2 (2)</td>
      <td>78 (79)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>12</td>
      <td>30</td>
      <td>33</td>
      <td>one x BON</td>
      <td></td>
      <td>26 (27)</td>
      <td></td>
      <td>3 (3)</td>
      <td></td>
      <td></td>
      <td></td>
      <td>1 (1)</td>
      <td></td>
      <td></td>
      <td></td>
      <td>1 (1)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>1 (1)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td colspan="3">smaller cluster/unclustered:</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>83</td>
      <td>109</td>
      <td></td>
      <td>22 (29)</td>
      <td>19 (19)</td>
      <td>25 (25)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>9 (9)</td>
      <td></td>
      <td></td>
      <td></td>
      <td>1 (1)</td>
      <td></td>
      <td></td>
      <td></td>
      <td>4 (12)</td>
      <td></td>
      <td></td>
      <td>2 (2)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>1 (1)</td>
      <td></td>
    </tr>
  </tbody>
</table>

_* The main twelve clusters were analysed, all proteins falling into smaller clusters were summarised into the single category ‘smaller cluster’.†, ‡, §, ¶ Shown are the number of UniRef100 used in the clustering approach†, the corresponding number of proteins derived from the HMMER search‡, the observed major domain architecture§ and the number of unique protein sequences (in brackets)¶ as well as the number of unique organisms mapped to the bacterial (Sub)Phyla**.†† Acidobacteria, Actinobacteria, Bacteroidetes, Chlamydiae, Chlorobi, Chloroflexi, Cyanobacteria, Deinococcus-Thermus, Fibrobacteres, Firmicutes, Gemmatimonadetes, Nitrospirae, Planctomycetes, Spirochaetes, Synergistetes, Thermobaculum, Thermodesulfobacteria, Thermotogae, Verrucomicrobia._

Previously, we demonstrated that loss of dolP in S. enterica conferred susceptibility to vancomycin and SDS, suggesting DolP plays an important role in maintaining the integrity of the OM (Morris et al., 2018). Further evidence of a role for DolP in maintaining OM integrity is shown by E. coli ΔdolP susceptibility to vancomycin, SDS, cholate, and deoxycholate (Figure 1C and Figure 1—figure supplement 4A). Resistance could be restored by supplying dolP in trans (Figure 1C). Despite evidence for disrupted OM integrity, the growth rate observed for the dolP mutant strain was identical to that of the parent, and scanning-electron microscopy revealed no obvious differences in cell size or shape (Figure 1—figure supplement 4B,C). To determine whether DolP is broadly required for OM homeostasis, plasmids expressing DolP homologues from S. enterica, Vibrio cholerae, Pasteurella multocida, Haemophilus influenza, and Neisseria meningitidis were shown to restore the OM barrier function of the E. coli ΔdolP mutant (Figure 1F). Finally, either replacement of the DolP signal sequence with that of PelB (Tsang et al., 2017), which targets the protein to the periplasmic space, or mutation of the signal sequence to avoid OM targeting via the Lol system, prevented complementation of the ΔdolP phenotype (Figure 1—figure supplement 5). Together these results support a conserved role for DolP in maintenance of OM integrity throughout Gram-negative bacteria and demonstrate that localisation of DolP to the inner leaflet of the OM is essential to mediate this function.

### The structure of DolP reveals a dual BON-domain lipoprotein

To gain further insight into the function of DolP, the structure of full-length mature E. coli DolP was determined by NMR spectroscopy. To promote native folding of DolP, the protein was over-expressed in the periplasm using a PelB signal sequence; the N-terminal cysteine was removed to prevent acylation and provide for rapid purification of the soluble protein. Purified DolP was processed, soluble and monomeric, as confirmed by analytical ultra-centrifugation and size exclusion chromatography (Figure 2—figure supplement 1). Using a standard Nuclear Overhauser Effect (NOE)-based approach, a convergent ensemble was calculated from the 20 lowest-energy solution structures, revealing two BON domains facing away from each other and offset by ~45° (Figure 2A and Figure 2—figure supplement 2). The individual BON1 (Residues 45–112) and BON2 (Residues 114–193) domains have C-alpha backbone root mean square deviations (RMSDs) of 0.3 and 0.3 Å, respectively, and an overall global RMSD of 0.5 Å (Table 2). Despite having low sequence identity (24.7%) each BON domain consists of a three-stranded mixed parallel/antiparallel β-sheet packed against two α-helices yielding an αββαβ topology. The two BON domains present high structural homology and superpose with an RMSD of 1.8 Å over C-alpha backbone (Figure 2—figure supplements 2 and 3). Notably, BON1 is embellished by an additional short α1* helix between BON1:α1 and BON1:β1 (Figure 2A and Figure 2—figure supplements 2 and 3). The N-terminal acylation site is connected through a 27 amino acid dynamic unstructured linker (Figure 2B). The molecular envelope of full-length DolP calculated by small-angle X-ray scattering (SAXS) accommodated the NMR-derived structure of DolP and supported the presence of a flexible N-terminal extension. The experimentally determined scattering curve fit the NMR-derived structure with a χ (Konovalova et al., 2017) of 1.263, confirming the accuracy of the NMR-derived structure and an exclusively monomeric state (Figure 2C and Figure 2—figure supplement 4).

![Figure 2.](https://cdn.elifesciences.org/articles/62614/elife-62614-fig2-v2.jpg)

**Figure 2.:** (A) Solution structure and topology of DolP, with α helices, β strands and termini labelled. (B) Backbone model of the 20 lowest-energy solution structures of DolP. The core folded domain is highlighted in red whilst the flexible N-terminal is shown in grey. The dynamic nature of the linker was demonstrated from S2 order parameter analysis calculated from chemical shift assignments using TALOS+. (C) Small-angle X-ray scattering curve of DolP with corresponding best fit of the solution structure of DolP. Best fit calculated based on the core DolP solution structure with flexibility accommodated in residues 20–46, 112–118, and 189–195. The corresponding ab-initio bead model is shown calculated using Dammif (Franke and Svergun, 2009) based solely on the scattering data. (D) Western blots of total protein extracts show plasmid-mediated expression of DolP in E. coli ΔdolP after site-directed mutation of conserved residues. The empty vector (EV) control is labelled and WT represents wild-type DolP. The presence of the OM lipoprotein BamB was used as a control. Colony growth assays by serial dilution of mutants on 4.8% SDS reveal which residues are critical for the maintenance of the OM barrier function. (E) Structure of DolP showing position of transposon-mediated insertions. Western blots of total protein extracts show plasmid-mediated expression of mutant versions of DolP in E. coli ΔdolP. The empty vector (EV) control is labelled and WT represents wild-type DolP. Colony growth assays by serial dilution of mutants on 4.8% SDS reveal which insertions abolish DolP function. Blue labels represent position of non-functional insertions. Orange labels represent position of tolerated insertions. The presence of the OM lipoprotein BamB was used as a control.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/62614/elife-62614-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) DolP, lacking the site of acylation, was purified and subject to analytical ultracentrifugation. DolP demonstrated a uniform sedimentation velocity consistent with a monomeric species. (B) Column chromatography of purified DolP revealed that it had an elution profile consistent with a single monomeric species.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/62614/elife-62614-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** (A) The ensemble of the 20 lowest-energy structures superimposed to DolP BON1 (N47-I111) and BON2 (G120-T185) domain backbones showing how well the domains superimpose as well as the respective degrees of freedom available to each domain. (B) Dalilite superposition of DolP BON domains 1 (Red; residues 46–114) and 2 (Blue; residues 117–189). The BON domains are similar except for the double turn extension of the BON2:α1 helix and the presence of the α1’ helix present in BON1 that is absent in BON2. The pairwise RMSD for backbone heavy atoms is 1.8 Å and dalilite Z-score is 8.4. (C) Superposition of DolP BON2 (Blue) on to the BON subdomain of Rv0899 (OmpATb) (Green; accession code – 2KSM; residues 136–196). For BON2 the pairwise RMSD for backbone heavy atoms was 2.7 Å and the dalilite Z-score was 4.9. Similarly, for BON1 the pairwise RMSD was 2.6 Å and the dalilite Z-score was 5.3.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/62614/elife-62614-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** (A) The amino acid sequences of the experimentally derived BON domains of DolP and OmpATb are aligned with the predicted amino acid sequences of the BON domains from Kbp and OsmY. The position of the experimentally derived secondary structure for DolP BON1 and BON2 and OmpATb are depicted below the sequence alignment. (B) Alignments of the amino acid sequences of DolP and OsmY from various Gram-negative bacteria. The positions of the experimentally-derived secondary structural elements of E. coli DolP are depicted below the sequence alignment. The signal sequence is depicted by the red box. The Lipobox associated with recognition by LspA and acylation is highlighted in purple. The conserved glycine residues are highlighted in blue and the tyrosine residue associated with interdomain interactions is highlighted in green. Residues showing CSPs are highlighted in pink.

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/62614/elife-62614-fig2-figsupp4-v2.jpg)

**Figure 2—figure supplement 4.:** (A) Zoom in of the low s region of the small-angle X-ray scattering curve of DolP shown in Figure 2 highlighting the closeness of fit to the DolP solution structure. (B) Residuals plot between the DolP solution structure and the small-angle X-ray scattering curve highlighting the closeness of fit.

![Figure 2—figure supplement 5.](https://cdn.elifesciences.org/articles/62614/elife-62614-fig2-figsupp5-v2.jpg)

**Figure 2—figure supplement 5.:** 38 interdomain NOEs were identified via Cyana (Table 3). Due to the ambiguity between chemically equivalent hydrogens within the same group, multiple NOEs are displayed to all equivalent hydrogens resulting in 83 NOEs being displayed.

![Figure 2—figure supplement 6.](https://cdn.elifesciences.org/articles/62614/elife-62614-fig2-figsupp6-v2.jpg)

**Figure 2—figure supplement 6.:** (A) The linear region of the Guinier plot measured from the raw SAXS data for DolP. Values for Rg and I(0) are shown calculated using AutoRG in program Primus. (B) Pair-wise distance distribution P(r), calculated from the scattering curve of DolP, calculated using gnom arbitrary units (a.u.).

**Table 2.**
 Structural statistics of the ensemble of 20 DolP solution structures.


<table>
  <thead>
    <tr>
      <th></th>
      <th>DolP</th>
    </tr>
    <tr>
      <th>Completeness of resonance assignments†</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Aromatic completeness</td>
      <td>74.14%</td>
    </tr>
    <tr>
      <td>Backbone completeness</td>
      <td>98.42%</td>
    </tr>
    <tr>
      <td>Sidechain completeness</td>
      <td>84.84%</td>
    </tr>
    <tr>
      <td>Unambiguous CH2 completeness</td>
      <td>100%</td>
    </tr>
    <tr>
      <td>Unambiguous CH3 completeness</td>
      <td>100%</td>
    </tr>
    <tr>
      <td>Unambiguous sidechain NH2 completeness</td>
      <td>100%</td>
    </tr>
    <tr>
      <td>Conformationally restricting restraints‡</td>
      <td></td>
    </tr>
    <tr>
      <td>Distance restraints</td>
      <td></td>
    </tr>
    <tr>
      <td>Total NOEs</td>
      <td>2930 (2762)</td>
    </tr>
    <tr>
      <td>Intra residue (i = j)</td>
      <td>408 (374)</td>
    </tr>
    <tr>
      <td>Sequential (| i – j |=1)</td>
      <td>869 (783)</td>
    </tr>
    <tr>
      <td>Medium range (1 &lt; | i - j |&lt;5)</td>
      <td>773 (741)</td>
    </tr>
    <tr>
      <td>Long range (| i – j |≥5)</td>
      <td>880 (866)</td>
    </tr>
    <tr>
      <td>Interdomain</td>
      <td>38</td>
    </tr>
    <tr>
      <td>Dihedral angle restraints</td>
      <td>258</td>
    </tr>
    <tr>
      <td>Hydrogen bond restraints</td>
      <td>128</td>
    </tr>
    <tr>
      <td>No. of restraints per residue</td>
      <td>16.6 (20.9)</td>
    </tr>
    <tr>
      <td>No. of long range restraints per residue</td>
      <td>5.0 (6.5)</td>
    </tr>
    <tr>
      <td>Residual restraint violations‡</td>
      <td></td>
    </tr>
    <tr>
      <td>Average No. of distance violations per structure</td>
      <td></td>
    </tr>
    <tr>
      <td>0.2 Å-0.5 Å</td>
      <td>3.55</td>
    </tr>
    <tr>
      <td>&gt;0.5 Å</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Average No. of dihedral angle violations per structure</td>
      <td></td>
    </tr>
    <tr>
      <td>&gt;5o</td>
      <td>0 (max 4.8)</td>
    </tr>
    <tr>
      <td>Model quality‡</td>
      <td></td>
    </tr>
    <tr>
      <td>Global (residues 46–190)</td>
      <td></td>
    </tr>
    <tr>
      <td>Rmsd backbone atoms (Å)§</td>
      <td>0.5</td>
    </tr>
    <tr>
      <td>Rmsd heavy atoms (Å)§</td>
      <td>0.9</td>
    </tr>
    <tr>
      <td>Domain 1 (Residues 46–112)</td>
      <td></td>
    </tr>
    <tr>
      <td>Rmsd backbone atoms (Å)</td>
      <td>0.3</td>
    </tr>
    <tr>
      <td>Rmsd heavy atoms (Å)</td>
      <td>0.7</td>
    </tr>
    <tr>
      <td>Domain 2 (Residues 118–190)</td>
      <td></td>
    </tr>
    <tr>
      <td>Rmsd backbone atoms (Å)</td>
      <td>0.3</td>
    </tr>
    <tr>
      <td>Rmsd heavy atoms (Å)</td>
      <td>0.8</td>
    </tr>
    <tr>
      <td>Rmsd bond lengths (Å)</td>
      <td>0.005</td>
    </tr>
    <tr>
      <td>Rmsd bond angles (o)</td>
      <td>0.6</td>
    </tr>
    <tr>
      <td>MolProbity Ramachandran statistics‡.§</td>
      <td></td>
    </tr>
    <tr>
      <td>Most favoured regions (%)</td>
      <td>95.1</td>
    </tr>
    <tr>
      <td>Allowed regions (%)</td>
      <td>4.3</td>
    </tr>
    <tr>
      <td>Disallowed regions (%)</td>
      <td>0.7</td>
    </tr>
    <tr>
      <td>Global quality scores (raw/Z score)‡</td>
      <td></td>
    </tr>
    <tr>
      <td>Verify 3D</td>
      <td>0.38 /- 1.28</td>
    </tr>
    <tr>
      <td>Prosall</td>
      <td>0.52 /- 0.54</td>
    </tr>
    <tr>
      <td>Procheck (phi-psi)d</td>
      <td>−0.28 /- 0.79</td>
    </tr>
    <tr>
      <td>Procheck (all)d</td>
      <td>−0.75 /- 4.44</td>
    </tr>
    <tr>
      <td>Molprobity clash score</td>
      <td>47.99 /- 6.71</td>
    </tr>
    <tr>
      <td>Model Contents</td>
      <td></td>
    </tr>
    <tr>
      <td>Ordered residue ranges§</td>
      <td>45–193</td>
    </tr>
    <tr>
      <td>Total number of residues</td>
      <td>178</td>
    </tr>
    <tr>
      <td>BMRB accession number</td>
      <td>19760</td>
    </tr>
    <tr>
      <td>PDB ID code</td>
      <td>7A2D</td>
    </tr>
  </tbody>
</table>

_* Structural statistics computed for the ensemble of 20 deposited structures.† Computed using AVS software (Moseley et al., 2004) from the expected number of resonances, excluding highly exchangeable protons (N-terminal, Lys, amino and Arg guanido groups, hydroxyls of Ser, Thr, and Tyr), carboxyls of Asp and Glu, non-protonated aromatic carbons, and the C-terminal His6 tag.‡ Calculated using PSVS version 1.5 (Bhattacharya et al., 2007). Average distance violations were calculated using the sum over r−6.§ Based on ordered residue ranges [S(φ) + S(ψ)>1.8].Values in (brackets) refer to the core structured region._

The two BON domains pack against each other via their β-sheets through contacts mediated directly by Y75 and V82 in BON1 and T150, G160, L161 and T188 in BON2 with a total of 38 interdomain NOEs (Figure 2D, Figure 2—figure supplement 5, Table 3). This interdomain orientation is consistent with SAXS analysis (Figure 2C) and appears to be essential for function as the mutation Y75A abolishes function (Figure 2D). Single point mutations (G83V and G160V) of the highly conserved glycine residues had less effect, however the double mutant was non-functional (Figure 2D and Figure 2—figure supplement 3). Since the latter protein was not detectable by Western immunoblotting this is likely due to structural instability (Figure 2D).

**Table 3.**
 Interdomain NOE restraints identified by Cyana during automated NOE assignment and structure calculation.


<table>
  <thead>
    <tr>
      <th>Proton pair</th>
      <th>Intensity</th>
      <th>Distance (Å)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>TYR 75 HD1 - THR 188 HA</td>
      <td>Weak</td>
      <td>5.5</td>
    </tr>
    <tr>
      <td>TYR 75 HE1 - GLY 160 HA2</td>
      <td>Weak</td>
      <td>5.4</td>
    </tr>
    <tr>
      <td>TYR 108 HE1 - ALA 186 HA</td>
      <td>Weak</td>
      <td>5.5</td>
    </tr>
    <tr>
      <td>TYR 108 HE2 - ALA 186 HA</td>
      <td>Weak</td>
      <td>5.5</td>
    </tr>
    <tr>
      <td>TYR 108 HE1 - ALA 186 HB</td>
      <td>Weak</td>
      <td>5.1</td>
    </tr>
    <tr>
      <td>TYR 75 HD1 - ALA 186 HB</td>
      <td>Weak</td>
      <td>5.2</td>
    </tr>
    <tr>
      <td>TYR 75 HE1 - LEU 161 HA</td>
      <td>Weak</td>
      <td>5.2</td>
    </tr>
    <tr>
      <td>TYR 75 HE1 - LEU 161 HB3</td>
      <td>Weak</td>
      <td>5.4</td>
    </tr>
    <tr>
      <td>TYR 75 HE1 - LEU 161 HG</td>
      <td>Weak</td>
      <td>5.5</td>
    </tr>
    <tr>
      <td>TYR 75 HE1 - LEU 161 HD1</td>
      <td>Weak</td>
      <td>4.9</td>
    </tr>
    <tr>
      <td>TYR 75 HE1 - LEU 161 HD2</td>
      <td>Weak</td>
      <td>4.9</td>
    </tr>
    <tr>
      <td>THR 73 HG2 - ALA 186 HB</td>
      <td>Weak</td>
      <td>5.5</td>
    </tr>
    <tr>
      <td>LYS 78 HD2 - PHE 187 hr</td>
      <td>Weak</td>
      <td>5.5</td>
    </tr>
    <tr>
      <td>LYS 78 HD3 - PHE 187 hr</td>
      <td>Weak</td>
      <td>5.5</td>
    </tr>
    <tr>
      <td>TYR 75 HD1 - HET 159 HA</td>
      <td>Weak</td>
      <td>5.5</td>
    </tr>
    <tr>
      <td>TYR 108 HD1 - ALA 186 HB</td>
      <td>Weak</td>
      <td>5.5</td>
    </tr>
    <tr>
      <td>GLN 76 HE22 - LEU 161 HB2</td>
      <td>Weak</td>
      <td>5.2</td>
    </tr>
    <tr>
      <td>GLN 76 HE22 - LEU 161 HG</td>
      <td>Weak</td>
      <td>5.1</td>
    </tr>
    <tr>
      <td>GLN 76 HE22 - LEU 161 HD1</td>
      <td>Weak</td>
      <td>4.5</td>
    </tr>
    <tr>
      <td>GLN 76 HE22 - LEU 161 HD2</td>
      <td>Weak</td>
      <td>4.5</td>
    </tr>
    <tr>
      <td>TYR 75 HD1 - THR 188 HG2</td>
      <td>Weak</td>
      <td>4.2</td>
    </tr>
    <tr>
      <td>TYR 75 HE1 - LEU 161 hr</td>
      <td>Weak</td>
      <td>4.3</td>
    </tr>
    <tr>
      <td>TYR 75 HE1 - VAL 162 hr</td>
      <td>Weak</td>
      <td>5.5</td>
    </tr>
    <tr>
      <td>TYR 75 HE1 - LEU 161 HB2</td>
      <td>Weak</td>
      <td>4.1</td>
    </tr>
    <tr>
      <td>TYR 75 HE1 - THR 188 HG2</td>
      <td>Weak</td>
      <td>4.1</td>
    </tr>
    <tr>
      <td>TYR 75 HE1 - THR 188 hr</td>
      <td>Weak</td>
      <td>5.5</td>
    </tr>
    <tr>
      <td>TYR 75 HE1 - GLY 160 hr</td>
      <td>Weak</td>
      <td>4.8</td>
    </tr>
    <tr>
      <td>TYR 75 HD1 - GLY 160 hr</td>
      <td>Weak</td>
      <td>4.7</td>
    </tr>
    <tr>
      <td>THR 73 HG2 - HET 159 HG</td>
      <td>Weak</td>
      <td>4.4</td>
    </tr>
    <tr>
      <td>TYR 75 HE1 - LEU 161 HD</td>
      <td>Weak</td>
      <td>4.0</td>
    </tr>
    <tr>
      <td>TYR 75 HE2 - LEU 161 HD</td>
      <td>Weak</td>
      <td>5.1</td>
    </tr>
    <tr>
      <td>GLN 76 HE21 - LEU 161 HD</td>
      <td>Medium</td>
      <td>3.7</td>
    </tr>
    <tr>
      <td>GLN 76 HE22 - LEU 161 HD</td>
      <td>Medium</td>
      <td>3.7</td>
    </tr>
    <tr>
      <td>LYS 78 HG - PHE 187 hr</td>
      <td>Weak</td>
      <td>4.9</td>
    </tr>
    <tr>
      <td>LYS 78 HD - ALA 186 HB</td>
      <td>Weak</td>
      <td>5.1</td>
    </tr>
    <tr>
      <td>LYS 78 HD - PHE 187 hr</td>
      <td>Weak</td>
      <td>4.7</td>
    </tr>
    <tr>
      <td>LYS 78 HE - PHE 187 hr</td>
      <td>Weak</td>
      <td>5.3</td>
    </tr>
    <tr>
      <td>ARG 112 HA - ARG 182 HB</td>
      <td>Weak</td>
      <td>5.3</td>
    </tr>
  </tbody>
</table>

The elements of DolP that are required for function were mapped using an unbiased linker-scanning mutagenesis screen. The resulting DolP derivatives, containing in-frame 5-amino-acid insertions, were tested for stability by Western immunoblotting. Functional viability was assessed by their capacity to restore growth of E. coli ΔdolP in the presence of SDS (Figure 2E). Seven mutants occurred in the signal sequence and the linker region and were not considered further. Eight insertions were identified in BON1, with insertions at positions L50 (BON1:α1) and V72 (BON1:β1) failing to complement the ΔdolP defect whereas the rest were well tolerated. Five insertions were found in BON2, with those at positions L136, L142, and G160 being well tolerated. The remaining insertions at positions D125 and W127 occurred in BON2:α1 but failed to complement the ΔdolP phenotype. None of these mutations abolished protein expression. These data indicate the importance of BON2:α1 in maintaining DolP function and OM integrity (Figure 2E).

### DolP binds specifically to anionic phospholipids via BON2

Given that OM permeability defects are often associated with the loss or modification of molecular partners, we sought to identify DolP ligands. Scrutiny of the literature revealed high-throughput protein:protein interaction data (Carlson et al., 2019; Babu et al., 2018) indicating that DolP co-located with components of the BAM complex in the OM. As the loss of multiple genes encoding different components of a single pathway can have additive phenotypes, such as decreased fitness, we investigated strains with dual mutations in dolP and genes coding the non-essential BAM complex components bamB or bamE. We observed that simultaneous deletion of dolP and bamB or bamE lead to negative genetic interactions and increased rates of cell lysis (Figure 3—figure supplement 1A,B), suggesting a potential interaction. However, despite these genetic interactions, in our hands no significant interaction could be detected between DolP and the BAM complex through immunoprecipitations (Figure 3—figure supplement 1C) and no significant change in overall OMP levels was observed (Supplementary file 2 and Figure 3—figure supplement 1D). Analyses of purified OM fractions revealed no apparent differences in LPS profiles (Figure 3—figure supplement 2A), or phospholipid content (Figure 3—figure supplement 2B) between the parent and the dolP mutant. No significant increase in hepta-acylated Lipid A was observed in the absence of DolP, indicating that the permeability defect is also not due to loss of OM lipid asymmetry (Figure 3—figure supplement 2C). In contrast, ΔdolP cells were found to have an increase in membrane fluidity (Figure 3—figure supplement 2D) as assessed by staining with the membrane intercalating dye pyrene-decanoic acid (PDA), which undergoes a fluorescence shift upon formation of the excimer, an event which is directly related to membrane fluidity (Storek et al., 2019). Considering that bamB mutants are sensitive to increased membrane fluidity (Storek et al., 2019), these data suggest that the genetic interaction between dolP and bamE or bamB, observed here, is facilitated indirectly through changes to membrane fluidity on the loss of DolP.

The dolP mutant has changed to membrane fluidity and that BON domains are suggested to bind phospholipids (Yeats and Bateman, 2003), therefore we sought to test whether DolP interacts with phospholipids. A set of potential ligands were screened by chemical shift perturbation (CSP) analysis, including E. coli OM lipids embedded in micelles. DolP bound specifically to micelles containing the anionic phospholipids phosphatidylglycerol (PG) and cardiolipin (CL) but not to micelles devoid of PG or CL, or those containing the zwitterionic phospholipid phosphatidylethanolamine (PE) (Figure 3A, Figure 3—figure supplement 3, Figure 4A). Significant CSPs were noted for A74, G120-I128, K131-R133, Q135-L137, V142-S145, I173, and S178-V180. The perturbed residues were mapped to the structure, revealing a single extensive binding site centred on BON2:α1 that was sufficiently large to contact several lipid molecules (Figure 3A). A dissociation constant (Kd) of ~100 mM (monomeric DHPG) was measured (Figure 3—figure supplement 4). No lipid interaction was seen for any BON1 domain residue, emphasising the specialised role of BON2, which not only differs from DolP BON1, but also from the BON domains of OsmY and Kbp (Figure 2—figure supplement 3). Analysis of the electrostatic surface reveals a large negative surface potential on BON1:α1, which is absent in BON2:α1 and may act to repel BON1 from PG, whilst BON2:α1 uniquely harbours an aromatic residue W127 in the observed PG- binding site (Figure 4—figure supplement 1).

![Figure 3.](https://cdn.elifesciences.org/articles/62614/elife-62614-fig3-v2.jpg)

**Figure 3.:** (A) DolP ribbon structure highlighting residues exhibiting substantial CSPs (Δδave) upon DHPG micelle interaction. The histogram shows the normalised perturbations induced in each residue’s amide signal when DHPG (40 mM) was added to DolP (300 µM). Examples of significant CSPs are shown. (B) Histogram showing intensity reductions of HN signals of DolP induced by adding 5-doxyl PC and DMPG into DPC/CHAPs micelles and the corresponding structure of a representative DolP-micelle complex calculated using CSPs and doxyl restraints using the program HADDOCK. Only the BON2:α1 helix is observed making contact with the micelle surface. No corresponding interaction of the BON1:α1 helix is observed. Zoom panels show burial of BON2:α1 into the micelle. The side chains of DolP residues that intercalate between the acyl chains (G120, S123, W127, T130, and S134) are coloured red. The side chains of residues that buttress the interface (E121, N124, T126, I128, K131, R133, and Q135) are coloured yellow. DolP is shown in blue and the phospholipid micelle is shown in tan.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/62614/elife-62614-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) dolP genetically interacts with the genes encoding the non-essential BAM complex accessory lipoproteins. Strains were arrayed on LB Lennox agar plates using a Biomatrix six replicator. Genetic interaction plates were incubated for 12 hr at 37°C and imaged. An example of a 384‐well plate is shown above the graph. Each plate contained a total of 384 colonies consisting of 96 wildtype, single, and double mutant clones. Fitness was measured by quantifying colony size and integral opacity, which represents colony density, using the image analysis software Iris (Kritikos et al., 2017). Bar plots show the averaged values 96 technical replicates. The error bars represent the 95% confidence interval. (B) Phase contrast microscopy of WT, ΔdolP, ΔbamB, ΔbamC, ΔbamE, ΔbamBΔdolP, ΔbamCΔdolP and ΔbamEΔdolP cells after growth to mid-exponential phase (OD600 ~0.4–0.8). Scale bars represent 2 μM. Phase light cells can be observed for the ΔbamBΔdolP and ΔbamEΔdolP cells.( C) DolP immunoprecipitation. Whole cell triton X-100 solubilised lysates of E. coli BW25113 pDolPpelB, pBamA-His, and ΔdolP, were purified by Ni-NTA affinity chromatography then detected by western blot using anti-DolP and BamA-E antibodies. (D) Purified OM samples from E. coli BW25113 parent (WT) or ΔdolP cells were separated by SDS-PAGE, with (d) and without (n) boiling before being visualised by staining with coomassie.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/62614/elife-62614-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** (A) SDS-PAGE gel showing separation of LPS preparations from E. coli BW25113 and E. coli BW25113 harbouring pET20b-wbbL which restores O-antigen expression on the bacterial cell surface. (B) Analysis of phospholipid profiles from purified ∆dolP cell envelopes. Phospholipids were extracted by the Bligh-Dyer method from E. coli IM or OM samples purified by sucrose density gradient centrifugation. Phospholipids were visualised by staining with phosphomolybdic acid and charring after being separated by thin-layer chromatography with the following mobile phase: Chloroform:methanol:acetic acid (65:25:10). Phospholipid profiles were also analysed by LC/MS-MS following separation on the Luna C8(2) column under a THF/MeOH/H2O gradient. Phospholipid compositions are shown as sum for each of the four major classes observed: lyso-phophatidylethanolamines (LysoPE), phosphatidylethanolamines (PE), phosphatidylglycerols (PG) and cardiolipins (CL). Each data set is from three biological replicates generated from three separately purified membranes. Error bars represent ±S.D. (C) PagP-mediated Lipid A palmitoylation assay. PagP transfers an acyl chain from surface exposed phospholipid to hexa-acylated Lipid A to form hepta-acylated Lipid A. [32P]-labelled Lipid A was purified from cells grown to mid-exponential phase in LB broth with aeration. An equal amount of radioactive material (cpm/lane) was loaded on each spot and separated by thin-layer chromatography before quantification. As a positive control, cells were exposed to 25 mM EDTA for 10 min prior to Lipid A extraction in order to chelate Mg2+ ions and destabilise the LPS layer, leading to high levels of Lipid A palmitoylation. Hepta-acylated and hexa-acylated lipid A was quantified and hepta-acylated Lipid A represented as a percentage of total. Triplicate experiments were utilised to calculate averages and standard deviations with students t-tests used to assess significance. Student’s t-tests: NS* p>0.1 compared with Parent EV. (D) E. coli BW25113 cells were grown overnight in LB (~16 hr) before being harvested by centrifugation and washed three times in PBS. Membrane fluidity was measured for each strain in triplicate and error bars represent standard deviation. Membrane fluidity is expressed as relative to E. coli BW25113 parent cells (WT).

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/62614/elife-62614-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** (A) 1H,15N HSQC spectra of 15N-DolP (300 μM) in the presence (red) and absence (black) of 40 mM 1,2-dihexanoyl-sn-glycero-3-phospho-(1'-rac-glycerol) (DHPG) highlighting the large chemical shift perturbations observed on DHPG binding. (B) Histograms showing the normalised CSP values observed in 15N-labelled DolP (300 μM) amide signals in the presence of 5 mM cardiolipin, 20 mM 1,2,-dihexanoyl-sn-glycero-3-phosphethanolamine and 20 and 40 mM 1,2-dihexanoyl-sn-glycero-3-phospho-(1'-rac-glycerol).

![Figure 3—figure supplement 4.](https://cdn.elifesciences.org/articles/62614/elife-62614-fig3-figsupp4-v2.jpg)

**Figure 3—figure supplement 4.:** Kd estimation was performed using the sum of the average chemical shift distance plotted against ligand concentration and fit using a standard ligand binding curve. Representative fits for G120, W127, and T138 are shown with corresponding estimations for Bmax, the maximum Δδppm, and Kd highlighted.

![Figure 4.](https://cdn.elifesciences.org/articles/62614/elife-62614-fig4-v2.jpg)

**Figure 4.:** (A) Histograms showing the normalised CSP values observed in 15N-labelled DolP (300 μM) amide signals in the presence of 20 mM 1,2,-dihexanoyl-sn-glycero-3-phosphethanolamine, 20 mM 1,2-dihexanoyl-sn-glycero-3-phospho-(1'-rac-glycerol) and 5 mM cardiolipin.( B) Mutagenesis of the BON2:α1 helix residues identified by CSPs. The positions of W127 and L137 are indicated as sticks. Western blots of total protein extracts show plasmid-mediated expression of DolP in E. coli ΔdolP after site-directed mutation of amino acid residues. The empty vector (EV) control is labelled and WT represents wild-type DolP. Colony growth assays of E. coli ΔdolP complemented with DolP mutants reveal which residues are critical for the maintenance of OM barrier function. The presence of the protein PqiB was used as a control. (C) Histograms showing the normalised CSP values observed in 15N-labelled DolPWT or DolPW127E mutant (300 μM) amide signals in the presence of 40 mM 1,2-dihexanoyl-sn-glycero-3-phospho-(1'-rac-glycerol).

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/62614/elife-62614-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A) Electrostatic surface map of DolP BON domains 1 and 2 calculated using DelPhi (Li et al., 2012) at a pH of 6 and 0.05M ionic strength (which approximates the experimental conditions). The −3kT/e surface is shown in red and the +3kT/e surface is shown in blue. A formal charge library was used, with a dielectric of 2 assigned to the protein interior and a dielectric of 80 assigned to the exterior. Cartoon representations of the BON structures are shown to the right of each surface to more clearly highlight the orientations of the protein. The BON1:α1 and BON2:α1 helices show clear differences, with BON1:α1 being predominantly neutral with an electronegative patch towards its N-terminus, whilst BON2:α2 shows no electronegatively at all, but rather has a large electropositive patch towards the centre of this helix presumably explaining its specificity for the electropositive surface of phosphatidylglycerol. (B) Hydrophobic surface map of DolP BON domains 1 and 2, hydrophobic residues (A, G, V, I, L, F, M) are shown in cyan, W127 (Red) is shown exposed on the surface of the BON2:α1 helix. Cartoon representations of the BON structures are shown to the right of each surface to more clearly highlight the orientations of the protein.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/62614/elife-62614-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** (A) E. coli BW25113 ∆dolP mutants were complemented with plasmids expressing a wild-type copy of DolP or a mutant version. Each strain was serially diluted and plated on LB-agar containing either vancomycin (100 μg/ml) or SDS (4.8% wt/vol), and growth was observed after overnight incubation. The W127E and L137E mutants failed to grow. (B) Western immunoblotting of whole cell lysates derived from overnight cultures of mutants highlighted in the top panel. Blots were probed with antibodies to the outer-membrane lipoprotein BamB and to DolP.

As the BON2 domain contained a particularly large PG-specific interaction site, we sought to resolve the micelle-complexed structure of mature DolP. Intermolecular structural restraints were obtained from paramagnetic relaxation enhancements (PRE) obtained by incorporating 5-doxyl spin-labelled phosphatidyl choline (PC) and 1,2-dimyristoyl-sn-glycero-3-phospho-(1’-rac-glycerol) (DMPG) into a n-dodecylphosphocholine (DPC) micelle and by measuring CSPs. The complexed structure was calculated using HADDOCK (Dominguez et al., 2003) with 18 PRE distance restraints and side chains of the 25 chemical shift perturbations, with final refinement in water (Figure 3B). The amino acids G120-T130 and V132-S139 were observed to insert into the micelle interior based on the PRE and CSP data. This reveals an unprecedented burial of the BON2:α1 helix, which spans the entirety of the L119-S139 sequence. The protein-micelle interface buries 1358 ± 316 Å2 and to our knowledge represents the most extensive structured surface of a membrane:protein interface resolved to date. The surface forms intimate contacts with at least six proximal phospholipid headgroups through an extensive network of highly populated hydrogen bonds and electrostatic interactions. Whilst the side chains of residues G120, S123, W127, T130, and S134 intercalate between the acyl chains, E121, N124, T126, I128, K131, R133, and Q135 buttress the interface (Figure 3B). This element was also functionally important based on our transposon screen (Figure 2E), and was further confirmed as being essential by directed mutagenesis. Mutations within the PG-binding BON2:α1 disrupt the function of DolP, the most critical of which are W127E and L137E; W127 is located in the centre of the binding site that penetrates deep into the core of the PG micelle, and L137 is located at the periphery of the helix (Figure 3B, Figure 4B and Figure 4—figure supplement 2). Not only does mutation of W127 lead to loss of function, but introduction of the W127E mutation was shown to abolish binding of DolP to PG micelles as observed by a loss of CSPs within BON2:α1 (Figure 4C). Notably, the BON2:α1 structure presents an extended α-helix when compared to BON1:α1 (Figure 2—figure supplements 2 and 3). The helical extension in BON2:α1 contains the W127 anionic phospholipid-binding determinant of DolP. This further implicates W127, which is absent in BON1 and OsmY, in specialisation of DolP BON2 for phospholipid binding.

### Phospholipid-binding guides DolP localisation to the cell division site

DolP binds anionic phospholipid, which demonstrates sub-cellular localisation to sites of higher membrane curvature including the cell poles and division site (Oliver et al., 2014; Renner and Weibel, 2011; Mileykovskaya and Dowhan, 2000). To determine if DolP also shows a preference for such sites, we constructed a plasmid expressing a DolP-mCherry fusion and utilising fluorescence microscopy we observed DolP localised specifically to the cell division site (Figure 5A). Considering that DolP is non-functional when targeted to the IM (Figure 1—figure supplement 5), we investigated if DolP could still localise to the site of cell division when it was mistargeted to the IM; no septal localisation was observed (Figure 1—figure supplement 5). Next, we tested whether the phospholipid-binding activity is also required for division site localisation of DolP. We found that introduction of the W127E mutation, which prevents interaction of DolP with PG/CL micelles, abolished division site localisation of DolP (Figure 5A). Considering that W127E not only abolished PG/CL binding, but also division site localisation, we concluded that division site localisation of DolP was dependent upon binding of DolP to anionic phospholipids, which have previously been shown to be enriched at the division site (Renner and Weibel, 2011; Mileykovskaya and Dowhan, 2000).

![Figure 5.](https://cdn.elifesciences.org/articles/62614/elife-62614-fig5-v2.jpg)

**Figure 5.:** (A) Fluorescence microscopy of ΔdolP cells expressing either DolPWT::mCherry or DolPW127E::mCherry from the pET17b plasmid after growth to mid-exponential phase (OD600 ~0.4–0.8). Scale bars represent 2 μM and both phase contrast and the mCherry channel are shown in greyscale and red respectively. White arrows highlight division site localisation of DolPWT-mCherry. Demographic representations of the DolPWT-mCherry or DolPW127E-mCherry fluorescence intensities measure along the medial axis of the cells. Images of >500 cells were analysed using the MicrobeJ software and sorted according to length where the y-axis represents relative cellular position with 0 being mid-cell and 3 or −3 being the cell poles (Ducret et al., 2016). (B) Thin layer chromatography of phospholipids extracted from either E. coli BW25113 (WT), ΔrcsFΔlpp, ΔrcsFΔlppΔpgsA (referred to as ΔpgsA) or ΔclsAΔclsBΔclsC (referred to as ΔclsABC) strains. The rcsF and lpp genes must be removed in order to prevent toxic build-up of Lpp on the IM in the pgsA mutant. Phospholipids were separated using chloroform:methanol:acetic acid (65:25:10) as the mobile phase before staining with phophomolybdic acid and charring.( C) Fluorescence microscopy of ΔpgsA or ΔclsABC cells expressing DolPWTmCherry from the pET17b plasmid after growth to mid-exponential phase (OD600 ~0.4–0.8). White arrows highlight DolP-mCherry mislocalisation.

To confirm this result we analysed DolP localisation in a strain that lacks all three cardiolipin synthases and is defective for cardiolipin synthesis, which was confirmed by phospholipid extraction and thin layer chromatography (Figure 5B). We observed that DolP localisation is perturbed in the CL- strain, with less dividing cells showing localisation of DolP to the septum (Figure 5C). These effects are further exacerbated in a strain that does not synthesise the major cell anionic phospholipids phosphatidylglycerol or cardiolipin, as confirmed by phospholipid extraction and thin layer chromatography (Figure 5B). Loss of both phosphatidylglycerol and cardiolipin synthesis worsened the severity of the localisation defect with less septal localisation and a significant proportion of cells showing mislocalisation of DolP to patches at the cell poles (Figure 5C). Taken together these data demonstrate that DolP localisation to the division site is dependent upon interaction with anionic phospholipid via BON2:α1, and that this interaction and the sub-cellular localisation are required for DolP function.

## Discussion

We have revealed the first structure of a dual-BON-domain protein, a protein architecture that is widely conserved amongst bacteria and therefore provides insight into a diverse range of proteins acting in different organisms. We also report the first evidence for direct binding of lipids by BON domains. We show that DolP BON2 demonstrates specificity for the anionic phospholipids PG and CL, which have previously been shown to localise to sites of higher membrane curvature including the cell poles and division site (Oliver et al., 2014; Renner and Weibel, 2011; Mileykovskaya and Dowhan, 2000). Interestingly, we detected no phospholipid binding for DolP BON1, which lacks the key W127 phospholipid interaction residue. This key residue is also lacking in the other periplasmic BON-domain-containing protein in E. coli, OsmY. Thus, we have demonstrated a specialised role for DolP in the cell and our data suggests BON domains are not generalist phospholipid-binding domains, as was suggested previously (Yeats and Bateman, 2003).

Here, we show for the first time that localisation of DolP to the cell division site is dependent upon recognition of anionic phospholipids by DolP BON2. To our knowledge, this is the only example of this mechanism of localisation to the bacterial division site (Laloux and Jacobs-Wagner, 2014). Considering anionic phospholipids also accumulate at the old pole, the question of how DolP specifically recognises the division site remains. We hypothesise that DolP prefers the site of higher positive (convex) curvature found only at the inner leaflet of the OM cell division site in vivo and in the PG micelles used in this study. Previous evidence has shown that inhibition of cell constriction, by the addition of cephalexin, also prevents DolP localisation to future division sites (Tsang et al., 2017). This indicates that DolP may require cell constriction for localisation to the division site, therefore lending support to the hypothesis that DolP may recognise membrane curvature. An alternative explanation is that the phospholipid-binding mode of DolP may trigger interaction with some as yet unidentified division site localised protein partner, but no obvious candidates are offered by published envelope interactome data (Carlson et al., 2019; Babu et al., 2018). Nevertheless, these data reveal that DolP function is dependent on localisation to the division site through phospholipid binding and localisation to the OM through its N-terminal lipid anchor. The model of DolP localisation to the cell division site proposed here also provides some evidence that anionic phospholipids localise to sites of high membrane curvature in the OM. While this has been shown for whole cells (Oliver et al., 2014; Mileykovskaya and Dowhan, 2000), and the IM through the use of spheroplasts (Renner and Weibel, 2011), to our knowledge, no such observation has yet been made for the OM directly. Considering that the OM is significantly different from the IM and is depleted of PG and CL by comparison (Lugtenberg and Peters, 1976; Figure 3—figure supplement 2B), the localisation of these lipids to sites of negative curvature could be further enhanced by the relative scarcity of these lipids in the OM and this warrants further study.

We have not found a direct mechanism through which DolP maintains OM integrity. No differences in LPS content or OM asymmetry were observed in a dolP mutant suggesting DolP does not influence the OM phospholipid recycling Mla pathway or LPS biogenesis. Previous protein:protein interaction studies captured DolP as a near neighbour of two components of the Bam complex, BamD and BamE (Carlson et al., 2019; Babu et al., 2018). Consistent with this, dolP shows synthetic lethality with the gene encoding the periplasmic chaperone SurA, leading to suggestions of a role for DolP in OMP biogenesis (Onufryk et al., 2005; Yan et al., 2019; Typas et al., 2008). However, we were unable to demonstrate a direct interaction between DolP and the BAM complex, and no such interaction has been seen in the extensive studies evaluating the subunit composition and multimeric states of the BAM complex (Wu et al., 2005; Hagan et al., 2010; Gunasinghe et al., 2018; Knowles et al., 2009) or in similar studies in N. meningitidis (Bos et al., 2014). However, while this is in agreement with the fact that DolP is localised to the division site, whereas the Bam complex is uniformly present across the cell surface (Gunasinghe et al., 2018), it does not rule out potential transient interactions. Previous observations revealed that the OM is a rigid structure (Rojas et al., 2018) that this membrane rigidity stabilises assembly precincts (Gunasinghe et al., 2018), and that the activity of the BAM complex is sensitive to increases in membrane fluidity (Storek et al., 2019). We suggest that the increased membrane fluidity of the dolP cells, demonstrated here, provides a challenging environment for assembly precincts to be maintained. We hypothesise that DolP, perhaps through interactions with peptidoglycan amidases (Tsang et al., 2017), might also modulate peptidoglycan remodeling in such a way as to minimise the clash between the periplasmic components of the assembly precinct and the cell wall, which might be exacerbated in regions of high membrane curvature.

In conclusion, this study reports for the first time the direct binding of lipid by BON domains and a new mechanism of protein division site localisation. The indirect link between DolP and the general machinery responsible for outer-membrane biogenesis adds to the recently described role of DolP in the regulation of cell wall amidases during division, therefore potentially placing DolP at the interface between envelope biogenesis processes (Tsang et al., 2017). The demonstration that loss of DolP increases sensitivity to antibiotics and membrane disrupting agents, in addition to the decrease in virulence in vivo, and an increase of the efficacy of the N. meningitidis vaccine, suggests DolP will provide a useful starting platform for antimicrobial design based on the disruption to regulation of multiple envelope biogenesis mechanisms (Morris et al., 2018; Giuliani et al., 2006; Pizza et al., 2000).

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
      <td>Strain, strain background (Escherichia coli)</td>
      <td>BL21(DE3)</td>
      <td>Invitrogen</td>
      <td></td>
      <td>T7 express, protein expression strain</td>
    </tr>
    <tr>
      <td>Strain, strain background (Escherichia coli)</td>
      <td>BW25113</td>
      <td>Datsenko and Wanner, 2000</td>
      <td></td>
      <td>rrnB3 ΔlacZ4787 ΔphoBR580 hsdR514 Δ(araBAD)567 Δ(rhaBAD)568 galU95 ΔendA9::FRT ΔuidA3::pir(wt) recA1 rph-1</td>
    </tr>
    <tr>
      <td>Strain, strain background (Escherichia coli)</td>
      <td>BW25113 △dolP</td>
      <td>This paper</td>
      <td></td>
      <td>BW25113 with dolP deleted</td>
    </tr>
    <tr>
      <td>Strain, strain background (Escherichia coli)</td>
      <td>BW25113 △lpp,△rcsF</td>
      <td>This paper</td>
      <td></td>
      <td>BW25113 with lpp and rcsF deleted</td>
    </tr>
    <tr>
      <td>Strain, strain background (Escherichia coli)</td>
      <td>BW25113 △lpp,△rcsF,△pgsA</td>
      <td>This paper</td>
      <td></td>
      <td>BW25113 with lpp, rcsF and pgsA genes deleted</td>
    </tr>
    <tr>
      <td>Strain, strain background (Escherichia coli)</td>
      <td>BW25113 △clsA,△clsB,△clsC</td>
      <td>This paper</td>
      <td></td>
      <td>BW25113 with clsA, clsB and clsC genes deleted</td>
    </tr>
    <tr>
      <td>genetic reagent (E. coli)</td>
      <td>KEIO library</td>
      <td>Datsenko and Wanner, 2000</td>
      <td></td>
      <td>Nonessential genes disrupted in E. coli BW25113</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pKD4</td>
      <td>Datsenko and Wanner, 2000</td>
      <td>Plasmid</td>
      <td>Template for the amplification of a kanamycin resistance cassette flanked by FRT sites.</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pKD46</td>
      <td>Datsenko and Wanner, 2000</td>
      <td>Plasmid</td>
      <td>Temperature sensitive, low copy number plasmid encoding the Lambda RED recombinase genes under the control of an arabinose inducible promoter</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pCP20</td>
      <td>Datsenko and Wanner, 2000</td>
      <td>Plasmid</td>
      <td>Temperature sensitive plasmid encoding the FLP recombinase gene</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pET17b</td>
      <td>Novagen</td>
      <td>Plasmid</td>
      <td>T7 expression vector, AmpR</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pET17b dolP</td>
      <td>This paper</td>
      <td>Plasmid</td>
      <td>pET17b with dolP cloned between NdeI and EcoRI</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pET17b dolP TM</td>
      <td>This paper</td>
      <td>Plasmid</td>
      <td>As described above with the dolP gene randomly disrupted by Transposon mutations</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pET17b dolP STm</td>
      <td>This paper</td>
      <td>Plasmid</td>
      <td>pET17b with the S. typhimurium dolP gene cloned between NdeI and HindIII</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pET17b dolP H.i</td>
      <td>This paper</td>
      <td>Plasmid</td>
      <td>pET17b encoding a codon optimised Haemophilus influenza dolP homolog</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pET17b dolP P.m</td>
      <td>This paper</td>
      <td>Plasmid</td>
      <td>pET17b encoding a codon optimised Pasteurella multocida dolP homolog</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pET17b dolP N.m</td>
      <td>This paper</td>
      <td>Plasmid</td>
      <td>pET17b encoding a codon optimised Neisseria meningitidis dolP homolog</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pET17b dolP V.c</td>
      <td>This paper</td>
      <td>Plasmid</td>
      <td>pET17b encoding a codon optimised Vibrio cholera dolP homolog</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pET17b osmY</td>
      <td>This paper</td>
      <td>Plasmid</td>
      <td>pET17b encoding a codon optimised E. coli K12 osmY</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>p(OM)OsmY</td>
      <td>This paper</td>
      <td>Plasmid</td>
      <td>pET17b encoding a codon optimised E. coli K12 osmY synthesised with the dolP signal sequence and acylation site in place of the osmY signal sequence</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pET20b</td>
      <td>Novagen</td>
      <td>Plasmid</td>
      <td>T7 expression vector, AmpR</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pET20b dolP</td>
      <td>This paper</td>
      <td>Plasmid</td>
      <td>pET20b with dolP cloned between NdeI and EcoRI</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pET20b dolP PM</td>
      <td>This paper</td>
      <td>Plasmid</td>
      <td>pET20b with dolP cloned between NdeI and EcoRI with site-directed point mutations at various sites</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pET20b wbbL</td>
      <td>This paper</td>
      <td>Plasmid</td>
      <td>pET20b with wbbL gene cloned between NdeI and HindIII</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pET20b dolP::mCherry</td>
      <td>This paper</td>
      <td>Plasmid</td>
      <td>pET20b encoding dolP fused to a codon optimised mCherry gene via a C-terminal 11-codon flexible linker (GGSSLVPSSDP)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pET26b dolPpelB::mCherry</td>
      <td>This paper</td>
      <td>Plasmid</td>
      <td>pET26b dolP::mCherry with the dolP signal sequence replaced with that of pelB</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pET20b dolPIM::mCherry</td>
      <td>This paper</td>
      <td>Plasmid</td>
      <td>pET20b dolP::mCherry with codon 20 and 22 of dolP each mutated to aspartic acid</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pET20b dolPW127E::mCherry</td>
      <td>This paper</td>
      <td>Plasmid</td>
      <td>pET20b dolP::mCherry with codon 127 mutated to glutamic acid</td>
    </tr>
  </tbody>
</table>

### Bioinformatic analyses

The BON-domain profile was obtained from Pfam http://pfam.sanger.ac.uk/ (Punta et al., 2012) and used as input for HMMER (hmmsearch version 3.1) (Finn et al., 2011) against the Uniprot database (http://www.uniprot.org, release 06032013) with an inclusion cutoff of E = 1 without heuristic filters. Sequence redundancy for clustering analysis was minimised using the UniRef100 resource of representative sequences; clustering was performed with the mclblastline program (Enright et al., 2002; Hunter et al., 2012) based on the e-value obtained by a BlastP run of all-against-all. Optimal settings for the mcl clustering were manually determined, clustering was performed at an e-value cutoff of 1E-2 and an inflation parameter of 1.2 using the scheme seven setting implemented in mcl. The resulting clusters were matched back to the proteins originally recovered by the HMMER search, and the number of proteins, as well as the number of matched organisms, are summarised for each phylum or subphylum in Table 1. UniProt accession numbers of all proteins according to their clusters are given in Supplementary file 1. The domain annotation was obtained from the InterPro database (Hunter et al., 2012). For cluster representation (Figure 1), the program CLANS (Frickey and Lupas, 2004) was used under the default settings. Clusterings with CLANS was based on a subset of OsmY-, DolP- and Kbp-like proteins identified as described above; the respective accession numbers are given in Table 4. Pairwise alignment similarity values were analysed at the Protein Information Resource site (PIR; http://pir.georgetown.edu/).

**Table 4.**
 Accession numbers for the sequences used for CLANS clustering shown in Figure 1.


<table>
  <thead>
    <tr>
      <th>Organism</th>
      <th>OsmY</th>
      <th>DolP</th>
      <th>Kbp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Escherichia coli K12</td>
      <td>P0AFH8</td>
      <td>P64596</td>
      <td>P0ADE6</td>
    </tr>
    <tr>
      <td>Klebsiella pneumoniae MGH 78578</td>
      <td>A6THZ1</td>
      <td>A6TEG9</td>
      <td>A6T985</td>
    </tr>
    <tr>
      <td>Enterobacter cloacae ENHKU01</td>
      <td>J7G7C8</td>
      <td>J7GHD1</td>
      <td>J7GFT3</td>
    </tr>
    <tr>
      <td>Salmonella enterica Typhimurium</td>
      <td>Q7CP68</td>
      <td>Q7CPQ6</td>
      <td>Q8ZML9</td>
    </tr>
    <tr>
      <td>Erwinia billingiae Eb661</td>
      <td>D8MMS8</td>
      <td>D8MME2</td>
      <td>D8MNV6</td>
    </tr>
    <tr>
      <td>Serratia proteamaculans 568</td>
      <td>A8G9G9</td>
      <td>A8GJZ3</td>
      <td>A8GFP7</td>
    </tr>
    <tr>
      <td>Cronobacter sakazakii ATCC BAA-894</td>
      <td>A7MGB6</td>
      <td>A7MIQ1</td>
      <td>A7MEA9</td>
    </tr>
    <tr>
      <td>Pantoea sp. Sc1</td>
      <td>H8DPK0</td>
      <td>H8DQ90</td>
      <td>H8DIH9</td>
    </tr>
    <tr>
      <td>Hafnia alvei ATCC 51873</td>
      <td>G9Y3J7</td>
      <td>G9Y4J4</td>
      <td>G9YAM4</td>
    </tr>
    <tr>
      <td>Citrobacter rodentium ICC168</td>
      <td>D2TRY4</td>
      <td>D2TQ24</td>
      <td>D2TM58</td>
    </tr>
    <tr>
      <td>Shigella flexneri 1235–66</td>
      <td>I6F1Q5</td>
      <td>I6GLP1</td>
      <td>I6HD15</td>
    </tr>
    <tr>
      <td>Yersinia enterocolitica 8081</td>
      <td>A1JJ93</td>
      <td>A1JR75</td>
      <td></td>
    </tr>
    <tr>
      <td>Yersinia pestis KIM10+</td>
      <td>Q7CG58</td>
      <td>Q8D1R6</td>
      <td></td>
    </tr>
    <tr>
      <td>Dickeya dadantii 3937</td>
      <td>E0SJX0</td>
      <td>E0SHF6</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Plasmids, bacterial strains, and culture conditions

Escherichia coli BW25113 was the parental strain used for most investigations. E. coli dolP::kan, osmY::kan and kbp::kan mutants were obtained from the KEIO library (Baba et al., 2006) and the mutations transduced into a clean parental strain. E. coli Δ dolP was created by resolving the KanR cassette, as previously described (Datsenko and Wanner, 2000). E. coli BW25113 ΔpgsA was constructed first by transfer of the rcsF::aph allele from the Keio library into E. coli BW25113 and removal of the kanR cassette. The lpp:aph allele was then introduced into the ΔrcsF strain, and the cassette removed by the λ-Red recombination method of Datsenko and Wanner, due to the presence of Lpp being toxic in the absence of phosphatidylglycerol (Datsenko and Wanner, 2000; Kikuchi et al., 2000; Suzuki et al., 2002). Finally, the same method was utilised to create the ΔpgsA strain (ΔrcsF,Δlpp,ΔpgsA) The genes encoding DolP and OsmY were amplified from E. coli BW25113 and cloned into pET17b to create pDolP and pOsmY. Orthologous sequences from S. enterica, V. cholera, N. meningitidis, H. influenza and P. multocida were synthesised and cloned into pET17b to create the plasmids pSe, pVc, pNm, pHi, and pPm, respectively. To create pDolPpelB, the gene encoding DolP was synthesised but with nucleotides encoding the PelB signal sequence in place of the native signal sequence and without Cys19 to relieve the possibility of acylation; this plasmid was constructed in pET26b+ such that the protein had a C-terminal His-tag. In addition, to create p(OM)OsmY the gene encoding OsmY was synthesised but with nucleotides encoding the native DolP signal sequence and Cys19 N-terminal acylation site in place of the native OsmY signal sequence. The latter plasmid was constructed in pET17b. The pET17b-dolP::mCherry plasmid was constructed to contain an 11 amino acid flexible linker and a codon optimised mCherry gene at the 3’ end of the dolP gene. Gene synthesis was performed by Genscript. The pet20b+-wbbL plasmid for restoring O-antigen synthesis in E. coli K-12 was previously described (Browning et al., 2013a). Single point mutations were generated by using Quickchange II according to manufacturer’s instructions. All constructs were confirmed by DNA sequencing. Strains were routinely cultured on LB agar and LB broth. Linker scanning mutagenesis was performed with an Ez-Tn5 kit (Epicentre) as previously described (Browning et al., 2013b).

### Analysis of membrane lipid content

Cell envelopes of E. coli were separated by defined sucrose density gradient separation, precisely as described previously following cell disruption by 3 passes of the C3 emulsiflex (Avestin) (Isom et al., 2017; Dalebroux et al., 2015). Samples were generated in biological triplicate from three separate 2 L batches of cells grown to an OD6000.6–0.8, with the final volumes for washed membranes being 1 ml, which were stored at −80 °C until analysis. Lipids were extracted by the Bligh-Dyer method (Bligh and Dyer, 1959) from purified membranes as described previously (Isom et al., 2017). Methanol and chloroform were added to the samples to extract the metabolites using a modified Bligh-Dyer procedure (Wu et al., 2008) with a final methanol/chloroform/water ratio of 2:2:1.8. The non-polar layer was extracted and dried under nitrogen before being stored at −80 °C until analysis. Samples were re-dissolved in 200 μl chloroform before being separated by thin layer chromatography on silica gel 60 plates with the mobile phase as chloroform:methanol:water at the following ratio: 65:25:10. Lipids were visualised by staining with phosphomolybdic acid. Analysis of lipid samples by mass spectrometry was completed as described previously (Teo et al., 2019). The differences were as follows: lipid extracts were diluted 10x or 20x into starting LC solvent the LC-MS/MS run directly. Normalisation was completed by taking the ion intensity of each phospholipid relative to the total ion count.

### Biochemical analyses

Cellular fractions were prepared as described previously (Parham et al., 2004). Cellular fractions and purified proteins were electrophoresed on 12 or 15% SDS-PAGE gels and stained with Coomassie blue or transferred to a polyvinylidene difluoride (PVDF) membrane for Western immunoblotting as previously described (Leyton et al., 2011). Loading consistency was confirmed by immuno-blotting with anti-BamB or anti-PqiB antiserum where possible. Protease shaving assays were described previously (Selkrig et al., 2012). Proteins were localised by immunofluorescence as described previously (Leyton et al., 2011). Analytical ultracentrifugation was performed as described previously (Knowles et al., 2011). For proteomic analysis of OM protein content, OM fractions purified by defined sucrose gradient centrifugation in biological triplicate and were digested with trypsin using the FASP method (Wiśniewski et al., 2009). Primary amines in the peptides were then dimethylated using hydrogenated or deuterated formaldehyde and sodium cyanoborohydride. Labelled peptides were mixed, separated into 15 fractions by mixed-mode reverse-phase/anion exchange chromatography, the fractions lyophilised and each analysed with a 90 min LC-MS/MS run using a Bruker Impact Q-TOF mass spectrometer. Data was searched against forward and randomised E. coli sequence databases using MASCOT and filtered at 1% FDR. Quantitation was based on the extracted ion chromatograms of light/heavy peptide pairs. DolP was investigated for binding partners using immunoprecipitation assays as described previously. Briefly, E. coli ΔdolP, and isogenic strains containing pDolPpelB or plasmid containing a His-Tagged version of BamA were grown in LB media to an OD600 of ~0.6 and harvested by centrifugation. Cells were resuspended in PBS with Triton X-100 supplemented with lysozyme and Benzonase nuclease. Cells were lysed and clarified by centrifugation. The lysate was incubated with Ni-NTA agarose (Qiagen) or appropriate antibodies. Precipitated proteins were analysed by Western immunoblotting.

### NMR spectroscopy

Experiments were carried out at 298 K on a Varian Inova 800 MHz spectrometer equipped with a triple-resonance cryogenic probe and z-axis pulse-field gradients. Isotope labelled DolP (15N 13C) with its N-terminal cysteine replaced was used at a concentration of 1.5 mM in 50 mM sodium phosphate (pH 6), 50 mM NaCl and 0.02% NaN3 in 90% H2O/10% D2O. Spin system and sequential assignments were made from CBCA(CO)NH, HNCACB, HNCA, HN(CO)CA, HNCO, HN(CA)CO, H(C)CH TOCSY and (H)CCH TOCSY experiments (Muhandiram and Kay, 1994). Spectra were processed with NMRPipe (Delaglio et al., 1995) and analysed with SPARKY (Goddard and Kneller, 2008).

### Structure calculations

Interproton distance restraints were obtained from 15N- and 13C-edited NOESY-HSQC spectra (τmix=100 ms). PRE restraints were obtained by adding 10 mM DPC/3.33 mM CHAPS micelles spiked with 1 mM DMPG and 0.185 mM 5-doxyl 1-palmitoyl-2-steroyl-sn-glycero-phosphocholine (Avanti, Polar Lipids, Alabaster, AL, USA) to 15N-labelled DolP (300 µM) and by standardising amide resonance intensities to those induced by spiking instead with unlabelled dipalmitoyl phosphocholine (Avanti Polar Lipids). Backbone dihedral angle restraints (ϕ and ψ) were obtained using TALOS from the backbone chemical shifts (Cornilescu et al., 1999). Slowly exchanging amides were deduced from the 1H 15N SOFAST-HSQC (Schanda et al., 2005) spectra of protein dissolved in 99.96% D2O. The structure was calculated iteratively using CANDID/CYANA, with automated NOE cross-peak assignment and torsion angle dynamics implemented (Güntert, 2004). A total of 20 conformers with the lowest CYANA target function were produced that satisfied all measured restraints. Aria1.2 was used to perform the final water minimisation (Linge et al., 2001). Structures were analysed using PROCHECK-NMR (Laskowski et al., 1993) and MOLMOL (Koradi et al., 1996). Structural statistics are summarised in Table 2.

### Lipid interactions

Ligand binding to 300 μM 15N- DolP in 50 mM sodium phosphate (pH 6), 50 mM NaCl and 0.02% NaN3 in 90% H2O/10% D2O was monitored by 1H15N-HSQCs at concentrations of 0–40 mM of either DHPG or DHPE (c.m.c.,~7 mM). The DPC-DMPG: DolP complex was calculated by HADDOCK (Dominguez et al., 2003; Dancea et al., 2008). A total of 18 paramagnetic relaxation enhancements restrained the distances between the micelle centre and the respective NH groups to 0–20 Å, with CSPs defining the flexible zone. The top 200 models were ranked according to their experimental energies and statistics derived from the 20 lowest-energy conformers were reported (Table 5).

**Table 5.**
 HADDOCK docking statistics for ensemble 20 lowest-energy DolP-DPC micelle solution structures calculated.


<table>
  <thead>
    <tr>
      <th>Experimental parameters*</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Ambiguous distance restraints</td>
      <td>19 including NH of I20, G120-T130, V132-Q135, T138, S139, and NHε of W127</td>
    </tr>
    <tr>
      <td>Number of flexible residues†</td>
      <td>50 (I20-V45 (flexible linker as ascertained by NMR), A74, G120-I128, K131-R133, Q135-L137, V142-S145, I173,S178-V180)</td>
    </tr>
    <tr>
      <td>Atomic pairwise RMSD (Å)</td>
      <td></td>
    </tr>
    <tr>
      <td>All backbone</td>
      <td></td>
    </tr>
    <tr>
      <td>Flexible interface backbone</td>
      <td></td>
    </tr>
    <tr>
      <td>Intermolecular energies (kcal.mol−1)</td>
      <td></td>
    </tr>
    <tr>
      <td>Evdw</td>
      <td>−100.81 ± 7.74</td>
    </tr>
    <tr>
      <td>Eelec</td>
      <td>−231.67 ± 64.14</td>
    </tr>
    <tr>
      <td>Erestraints</td>
      <td>22.30 ± 4.29</td>
    </tr>
    <tr>
      <td>Buried surface area (Å2)</td>
      <td>2186.78 ± 133.277</td>
    </tr>
  </tbody>
</table>

_* deduced from intensity reductions observed in presence of 5-doxl derivative.† according to their surface accessibility and the chemical shift perturbation in presence of DPC/CHAPS._

### Small-angle X-ray scattering

Synchrotron SAXS data of DolP were collected at the EMBL X33 beamline (DESY, Hamburg) using a robotic sample changer. DolP concentrations between 1 and 10 mg/ml were run in 50 mM sodium phosphate (pH 6), 50 mM NaCl and 0.02% NaN3. Data were recorded on a PILATUS 1M pixel detector (DECTRIS, Baden, Switzerland) at a sample-detector distance of 2.7 m and a wavelength of 1.5 Å, covering a range of momentum transfer of 0.012 < s < 0.6 Å−1 (s = 4πsin(θ)/γ, where 2θ is the scattering angle) and processed by PRIMUS (Konarev et al., 2003). The forward scattering I(0) and the radius of gyration (Rg) were calculated using the Guinier approximation (Guinier, 1939; Figure 2—figure supplement 6). The pair-distance distribution function pR, from which the maximum particle dimension (Dmax) is estimated, was computed using GNOM (Svergun, 1992; Figure 2—figure supplement 6). Low resolution shape analysis of the solute was performed using DAMMIF (Franke and Svergun, 2009). Several independent simulated annealing runs were performed and the results were analysed using DAMAVER (Volkov and Svergun, 2003). Back comparison of the DolP solution structure with the SAXS data was performed using the ensemble optimisation method (Bernadó et al., 2008) accounting for flexibility between residues 20–46, 112–118 and 189–195. All programs used for analysis of the SAXS data belong to the ATSAS package (Petoukhov and Svergun, 2005).

### Accession codes

Coordinates and NMR assignments have been deposited with accession codes 7A2D (PDB) and 19760 (BMRB), respectively.

### Cell imaging

Cultures were grown at 37°C to OD6000.4–0.5. Cells were harvested by centrifugation at 7000 x g for 1 min before being applied to agarose pads, which were prepared with 1.5% agarose in PBS and set in Gene Frames (Thermo Scientific). Cells were immediately imaged using a Zeiss AxioObserver equipped with a Plan-Apochromat 100x/Oil Ph3 objective and illumination from HXP 120V for phase contrast images. Fluorescence images were captured using the Zeiss filter set 45, with excitation at 560/40 nm and emission recorded with a bandpass filter at 630/75 nm. For localisation analysis and generation of demographs, the MicrobeJ plugin for Fiji was used and >500 cells were used as input for analysis (Ducret et al., 2016).

### Membrane fluidity assay

Membrane fluidity was measured by use of the membrane fluidity assay kit (Abcam: ab189819) as was described previously except with minor modifications (Storek et al., 2019). Specific bacterial strains were grown to stationary phase overnight (~16 hr) after which cells were harvested by centrifugation, washed with PBS three times and finally labelled with labelling mix (10 μM pyrenedecanoic acid and 0.08% pluronic F-127 in PBS) for 20 min in the dark at 25°C with shaking. Cells were washed twice with PBS before fluorescence was recorded with excitation at 350 nm and emission at either 400 nm or 470 nm to detect emission of the monomer or excimer respectively. Unlabelled cells were used as a control to confirm labelling and the E. coli BW25113 ΔwaaD strain was used as a positive control for increased membrane fluidity. Following subtraction of fluorescence from the blanks, averages from triplicate experiments were used to calculate the ratio of excimer to monomer fluorescence. These ratios were then expressed as relative to the parent E. coli BW25113 strain.

### Genetic interaction analysis

Genetic interaction assay was performed as described in Banzhaf et al., 2020. For each probed strain, a single source plate was generated and transferred to the genetic interaction plate using a pinning robot (Biomatrix 6). On each genetic interaction assay plate, the parental strain, the single deletion A, the single deletion B and the double deletion AB were arrayed, each in 96 copies per plate. Genetic interaction plates were incubated at 37°C for 12 hr and imaged under controlled lighting conditions (spImager S and P Robotics) using an 18-megapixel Canon Rebel T3i (Canon). Colony integral opacity as fitness readout was quantified using the image analysis software Iris (Kritikos et al., 2017). Fitness ratios were calculated for all mutants by dividing their fitness values by the respective WT fitness value. The product of single mutant fitness ratios (expected) was compared to the double mutant fitness ratio (observed) across replicates. The probability that the two means (expected and observed) are equal across replicates is obtained by a Student's two‐sample t‐test.

### Lipid A palmitoylation assay

Labelling of LPS, Lipid A purification, TLC analysis, and quantification were done exactly as described previously (Chong et al., 2015). The positive control was exposed to 25 mM EDTA for 10 min prior to harvest of cells by centrifugation in order to induce PagP mediated palmitoylation of Lipid A (Chong et al., 2015). Experiments were completed in triplicate and the data generated was analysed as described previously.
