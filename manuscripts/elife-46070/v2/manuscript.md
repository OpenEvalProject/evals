# Large protein organelles form a new iron sequestration system with high storage capacity

## Authors

- Tobias W Giessen<sup>1</sup> ([ORCID: 0000-0001-6328-2031](https://orcid.org/0000-0001-6328-2031)) †
- Benjamin J Orlando<sup>4</sup>
- Andrew A Verdegaal<sup>1</sup> ([ORCID: 0000-0002-4517-6961](https://orcid.org/0000-0002-4517-6961))
- Melissa G Chambers<sup>4</sup> ([ORCID: 0000-0001-5111-7194](https://orcid.org/0000-0001-5111-7194))
- Jules Gardener<sup>5</sup>
- David C Bell<sup>5</sup>
- Gabriel Birrane<sup>7</sup> ([ORCID: 0000-0002-1759-5499](https://orcid.org/0000-0002-1759-5499))
- Maofu Liao<sup>2</sup> †
- Pamela A Silver<sup>1</sup> †

### Affiliations

1. Department of Systems Biology Harvard Medical School Boston United States
2. Wyss Institute for Biologically Inspired Engineering Harvard University Boston United States
3. Department of Biomedical Engineering University of Michigan Ann Arbor United States
4. Department of Cell Biology Harvard Medical School Boston United States
5. Center for Nanoscale Systems Harvard University Cambridge United States
6. School of Engineering and Applied Sciences Harvard University Cambridge United States
7. Department of Medicine Beth Israel Deaconess Medical Center, Harvard Medical School Boston United States

† Corresponding author

## Abstract

Iron storage proteins are essential for cellular iron homeostasis and redox balance. Ferritin proteins are the major storage units for bioavailable forms of iron. Some organisms lack ferritins, and it is not known how they store iron. Encapsulins, a class of protein-based organelles, have recently been implicated in microbial iron and redox metabolism. Here, we report the structural and mechanistic characterization of a 42 nm two-component encapsulin-based iron storage compartment from Quasibacillus thermotolerans. Using cryo-electron microscopy and x-ray crystallography, we reveal the assembly principles of a thermostable T = 4 shell topology and its catalytic ferroxidase cargo and show interactions underlying cargo-shell co-assembly. This compartment has an exceptionally large iron storage capacity storing over 23,000 iron atoms. Our results reveal a new approach for survival in diverse habitats with limited or fluctuating iron availability via an iron storage system able to store 10 to 20 times more iron than ferritin.

## Introduction

Iron is essential to virtually all organisms on earth. It is needed for a wide variety of catalytic and redox processes ranging from cellular energy production via oxidative phosphorylation to oxygen transport by hemoglobin (Sánchez et al., 2017). However, the same properties that make iron useful for cellular metabolism can result in toxicity under aerobic conditions (Sánchez et al., 2017). Ferrous iron (Fe2+) is easily oxidized to insoluble ferric iron (Fe3+) resulting in the formation of harmful precipitates and reactive oxygen species (ROS) via Fenton chemistry (Dixon and Stockwell, 2014). Cells have evolved to cope with these problems by strictly controlling the intracellular concentration and reactivity of free iron (Crichton, 2002). Ferritin proteins are used as the main iron storage system by animals, plants and most microbes (Arosio et al., 2017). The main ferritin-like proteins involved in iron storage are ferritin (Ftn), bacterioferritin (Bfr) and DNA-binding proteins from starved cells (Dps) all able to oxidize Fe2+ to Fe3+ via a ferroxidase activity (Andrews, 2010). While Ftn and Bfr are primarily used as a dynamic iron storage (Honarmand Ebrahimi et al., 2015), the main function of Dps proteins is to counteract oxidative stress (Chiancone et al., 2004). Ferritins (Ftn and Bfr) assemble into 24 subunit protein compartments up to 12 nm in diameter able to store 2000 to 4,000 Fe atoms in their interior (Andrews, 1998; Harrison and Arosio, 1996). However, some organisms do not encode ferritin genes in their genomes and their iron storage systems have remained elusive.

A newly discovered class of protein organelles called encapsulin nanocompartments have been shown to be involved in microbial iron storage and redox metabolism (Giessen and Silver, 2017; He et al., 2016; McHugh et al., 2014; Sutter et al., 2008). Previously reported encapsulins share an HK97 phage-like fold and self-assemble from a single capsid protein into icosahedral compartments between 24 and 32 nm in diameter with triangulation numbers of T = 1 (60 subunits) and T = 3 (180 subunits), respectively (Akita et al., 2007; McHugh et al., 2014; Sutter et al., 2008). Their key feature is the ability to specifically encapsulate cargo proteins (Figure 1a). Encapsulation is mediated by short C-terminal sequences referred to as targeting peptides (TPs) (Sutter et al., 2008; Tamura et al., 2015). Genes encoding encapsulin shell proteins and dedicated cargo proteins are organized in co-regulated operons (Giessen and Silver, 2017; Sutter et al., 2008). So far, operons involved in hydrogen peroxide and nitric oxide detoxification as well as iron mineralization have been reported (Nichols et al., 2017). The main cargo protein-types described to date are DyP-type peroxidases, hemerythrins and different classes of ferritin-like proteins (Contreras et al., 2014; Giessen and Silver, 2017; McHugh et al., 2014; Rahmanpour and Bugg, 2013). We have identified a novel type of encapsulin operon involved in iron metabolism in a range of Firmicutes we term the Iron-Mineralizing Encapsulin-Associated Firmicute (IMEF)-system (Giessen and Silver, 2017).

![Figure 1.](https://cdn.elifesciences.org/articles/46070/elife-46070-fig1-v2.jpg)

**Figure 1.:** (a) Schematic diagram of a core encapsulin operon and targeting peptide (TP)-dependent cargo encapsulation. (b) Surface view of the cryo-EM map of the Qs T = 4 encapsulin shell (top) and inside view of cargo-loaded encapsulin (bottom). 5-, 3- and 2-fold symmetry axes are indicated by red symbols. The overall icosahedral symmetry is highlighted by black lines representing icosahedral facets. Cargo-densities are shown in orange while the shell is radially colored. To depict the complete cargo-loaded compartment, a 10 Å filtered map highlighting the cargo was combined with the 3.85 Å map of the shell. (c) Asymmetric unit of the T4 encapsulin shell and structural alignment of the four unique T4 shell monomers with one another and with the T. maritima (Tm) T = 1 monomer (3DKT), the P. furiosus (Pf) T = 3 monomer (2E0Z) and the HK97 bacteriophage Head II T = 7 monomer (2FT1).

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/46070/elife-46070-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (a) The Qs operon is highlighted in red. The nearest-neighbor phylogenetic tree is based on a ClustalO alignment of IMEF cargo proteins. IMEF cargo accessions are shown in Supplementary Table 1. Evolutionary distances were estimated as the number of amino acid substitutions per site. The scale bar represents 0.09 expected amino acid residue substitutions per site. b, Shown are negative stain (uranyl formate) TEM micrographs of purified compartments (right) and a representative SDS-PAGE gel (left). The SDS-PAGE gel shows that the IMEF cargo protein (22.6 kDa) co-purifies with the encapsulin capsid protein (32.2 kDa). The SDS-PAGE gel is the same as shown for comparison in Fig. 3e of the main text. Scale bars in micrographs correspond to 100 nm.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/46070/elife-46070-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** (a) FSC curves calculated from independent half-maps (black line) and a comparison of the atomic model of the IMEF encapsulin versus the experimental map (red line). The green dashed line represents an FSC cutoff of 0.5 and the blue dashed line represents an FSC cutoff of 0.143. (b) Annotated monomer alignment of the IMEF capsid protein monomers with local cryo-EM maps. The different structural elements of the T = 4 encapsulin monomer are shown. Representative density maps (mesh) and atomic models (model B of the asymmetric unit) illustrating side chain features and overall fit of the atomic model with the cryo-EM map are shown. (c) T = 4 IMEF encapsulin capsid with highlighted asymmetric unit (right) and annotation (left) defining the 4 capsid monomers of the asymmetric unit and the hexameric and pentameric capsomers. (d) Central slice of cargo-loaded IMEF encapsulin capsid. Less defined lower resolution density can clearly be seen in the interior (red dotted lines). (e) Top: Drawings illustrating the icosahedral symmetry and tiling of capsids with different triangulation numbers. Bottom: Capsid models of T = 1, T = 3 and the newly discovered T = 4 encapsulin shells including maximum external diameter and subunit number.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/46070/elife-46070-fig1-figsupp3-v2.jpg)

**Figure 1—figure supplement 3.:** (a) Model of a hexameric unit with cargo colored blue, encapsulin shell colored gray and targeting peptide colored magenta. A simulated map of the model low-pass filtered to 60 Å was used for signal subtraction and classification. (b) View of the low-pass filtered mask encompassing a hexameric unit of the encapsulin shell and associated symmetry averaged cargo density. (c) Data processing scheme to expand icosahedral symmetry and perform focused classification on a hexameric nit with associated cargo proteins. (d) Examples of low-resolution features showing a connection between cargo density and general areas of the targeting peptide in the encapsulin shell. Targeting peptides are shown as red spheres, encapsulin shell is shown as blue ribbon. Areas circled in purple dashed lines indicate densities for a flexible tether between the targeting peptide and cargo.

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/46070/elife-46070-fig1-figsupp4-v2.jpg)

**Figure 1—figure supplement 4.:** Top: central slices through the T = 4 shell. Middle: Comparison of shell and internal cargo resolution. Bottom: Focus on shell resolution. The lowest resolution parts of the T = 4 shell are highlighted and include 5- and 3-fold pore residues corresponding to A-domain loops and E-loops, respectively, and A-domain loops forming the closed ‘pore’ at the 2-fold symmetryaxis.

Here, we report the structural and mechanistic characterization of the IMEF-system found in Quasibacillus thermotolerans (Qs), an organism that does not encode any ferritins in its genome. We show that this encapsulin-based system self-assembles into a thermostable 42 nm 9.6 MDa protein compartment with a novel T = 4 topology able to mineralize and store an exceptionally large quantity of iron.

## Results and discussion

### Discovery and computational analysis of IMEF operons

IMEF-systems are found in Firmicute genomes and their operon organization indicates a function in dynamic iron storage. To investigate the distribution of IMEF-systems in microbes, we carried out BLASTp searches using IMEF cargo proteins as queries and identified 71 operons in a range of Firmicutes including Qs (Figure 1—figure supplement 1a). The core operon consists of the encapsulin capsid protein and the IMEF cargo protein with 70% of operons also encoding a 2Fe-2S ferredoxin homologous to bacterioferritin-associated ferredoxins (Bfd). Bfd proteins are involved in the mobilization of iron under iron-limited conditions (Yao et al., 2012). In addition, 31% of operons are associated with proteins similar to ferrochelatases involved in catalyzing the insertion of ferrous iron into protoporphyrins (Dailey et al., 2000). The majority of IMEF-encoding genomes do not contain any ferritin or bacterioferritin genes (Supplementary file 1). Most IMEF genomes do however contain Dps-encoding genes. Overall, the operon organization of IMEF-systems and the lack of other known primary iron storage proteins indicate a function for IMEF-systems in dynamic iron storage similar to that of Ftn and Bfr.

### Overall structure of the cargo-loaded IMEF encapsulin

Using a recombinant system for the expression of the two-gene IMEF operon containing the IMEF cargo protein gene and the encapsulin capsid protein gene, we produced homogeneous IMEF cargo-loaded encapsulins (Figure 1—figure supplement 1b). Through single-particle cryo-EM analysis, we determined the structure of the Qs IMEF encapsulin shell at an overall resolution of 3.85 Å (Figure 1—figure supplement 2a and Supplementary file 2). The IMEF encapsulin self-assembles into a 240-subunit icosahedral compartment with a diameter of 42 nm (Figure 1b and Figure 1—figure supplement 2a–d). The IMEF compartment is substantially larger than previously reported encapsulins and possesses a triangulation number of T = 4 instead of T = 1 (60 subunits, 24 nm) or T = 3 (180 subunits, 32 nm) and represents the largest encapsulin compartment reported to date (Figure 1—figure supplement 2e). The shell is composed of 12 pentameric and 30 hexameric capsomers occupying icosahedral vertices and faces, respectively. In contrast, T = 1 encapsulins consist of only 12 pentameric capsomers while the T = 3 encapsulin shell is made up of 12 pentameric and 20 hexameric capsomers. The T = 4 IMEF-system consequently possesses an internal volume 530% and 220% larger than that of T = 1 and T = 3 encapsulins, respectively. The 5-fold symmetry axes are located at the pentameric vertices while 3-fold symmetry axes are present at all interfaces where three hexameric capsomers meet. The center of each hexameric capsomer corresponds to an icosahedral edge possessing 2-fold symmetry. The icosahedral asymmetric unit consists of one pentameric and three hexameric monomers (Figure 1b and Figure 1—figure supplement 2c). Symmetrically arranged lower resolution density (ca. 10 Å) representing the IMEF cargo is visible in the compartment interior (Figure 1b and Figure 1—figure supplement 2d). 42 distinct densities, one for each capsomer of the T = 4 structure, can be observed. No connection of cargo and shell density is visible, likely due to averaging or the flexibility of a 37 amino acid linker preceding the IMEF targeting peptide that directs and anchors the IMEF cargo to the shell interior. Averaging and linker flexibility likely also contribute to the lower resolution observed for the interior IMEF densities. The distance between the shell and cargo densities is 4.5 nm which can be bridged by the 37 amino acid linker. To further investigate and better resolve the cargo densities, we applied an approach combining symmetry expansion and focused classification with residual signal subtraction (Figure 1—figure supplement 3). This approach was able to separate cargo densities bound at slightly different locations indicating that the symmetry observed for the cargo densities (Figure 1b) is a result of averaging. The observed non-symmetrical densities are still weak compared to the shell density. At low threshold values possible connections between cargo densities and the shell are visible, potentially representing the linker connecting the cargo with the bound TP (Figure 1—figure supplement 3).

The four capsid proteins of the asymmetric unit adopt different conformations with significant differences found in the E-loop and A-domain (Figure 1c). E-loops are located at capsomer interfaces and their relative orientation plays a key role in determining the overall topology and triangulation number of encapsulin compartments as evidenced by comparison of the IMEF T = 4 monomer with T = 1 (Thermotoga maritima), T = 3 (Pyrococcus furiosus) and T = 7 (HK97 phage) capsid proteins (Figure 1c). A-domain loops form compartment pores and are likely adapted to optimize the particular function of a given encapsulin, for example ROS detoxification or iron mineralization. In addition, local resolution maps indicate that E-loops and A-domain loops represent the most flexible parts of the shell which suggests a certain structural flexibility of the pores formed by A-domain loops (Figure 1—figure supplement 4).

### Pores in the IMEF encapsulin shell

The IMEF encapsulin shell contains negatively charged pores at the 3- and 5-fold symmetry axes. The surface view of the intact shell (Figure 2—figure supplement 1a) shows a tight packing with pores at the 3- and 5-fold symmetry axes and at the interface between two hexameric and one pentameric capsomer (pseudo 3-fold) representing the only conduits to the interior. Similarly, pores at the symmetry axes were also reported for T = 1 and T = 3 encapsulin systems. All pores in the IMEF-system are negatively charged on both the exterior and interior surface due to the presence of conserved aspartate, glutamate and asparagine residues (Figure 2a,b, Figure 2—figure supplement 1b and Figure 2—figure supplement 2). This is similar to the negatively charged pores in ferritin systems that guide positively charged iron to the ferritin interior (Arosio et al., 2017). In no other encapsulin system are all pores negatively charged indicating that pores in the IMEF-system are optimized for attracting and channeling positively charged ions. The 2-fold pores observed at the interface of two capsomers in T = 1 and T = 3 encapsulins are not present in the IMEF-system (Nichols et al., 2017). The 3-fold pore forms the largest channel to the IMEF compartment interior and is 7.2 Å wide at its narrowest point, substantially larger than previously reported encapsulin pores. Extra cryo-EM density is observed at the center of both the 3-fold and 5-fold pores. This could be a result of averaging accentuating noise on symmetry axes or potentially represent bound ions (e.g. Fe2+/3+) or even water molecules. The 2-fold symmetry axes at the center of hexameric capsomers also represent potential channels, as observed in T = 3 systems (Nichols et al., 2017), but the conformation of two asparagine side chains prevents the formation of a 2-fold opening in the T = 4 shell leading to a closed pore (Figure 2c). This observation combined with the flexibility observed for loops around the 2- and 5-fold symmetry axes in local resolution maps (Figure 1—figure supplement 4) could indicate the presence of gated pores in encapsulins that may regulate ion flux to the compartment interior, similar to some ferritins (Theil et al., 2008).

![Figure 2.](https://cdn.elifesciences.org/articles/46070/elife-46070-fig2-v2.jpg)

**Figure 2.:** (a, b and c) Electrostatic surface representation of the 5-fold (d) and 3-fold (e) T = 4 shell pores and the 2-fold symmetry axis (f). Outside views showing negatively charged pores (top) with no pore opening observed at the two-fold symmetry axis, cutaway side view highlighting the narrowest point of the pores (middle) and cryo-EM maps with fitted monomer models in ribbon representation (bottom). Additional cryo-EM density is observed at the center of both pores in interaction distance with the side chains of pore residues (5-fold: Asn200, 3-fold: Asp9, Asp71, Glu251 and Glu252, shown in stick representation). (d) Chainmail network mediated by E-loop and P-domain interactions. Only E-loops and P-domains are shown. E-loops and P-domains of the outlined ring belonging to the same monomer are located next to one another and are shown in light and dark blue, respectively. (e) Extended E-loop interactions interlock neighboring capsid monomers at the two unique three-fold interfaces. Each E-loop interacts with two P-domains. (f) Representative thermal unfolding curves for Qs T = 4 encapsulin components determined via differential scanning fluorimetry. Tm: midpoint of the thermal unfolding curve.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/46070/elife-46070-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (a) Left: View down the 5-fold symmetry axis highlighting the 5-fold and pseudo 3-fold pores. Right: View down the 2-fold symmetry axis highlighting the 3-fold pores and the closed 2-fold ‘pore’. This surface representation indicates tight packing of monomers resulting in the 5- and (pseudo) 3-fold pores being the only conduits to the internal space created by the encapsulin shell. Pseudo 3-fold pores are defined as pores at the interface of 2 hexameric and one pentameric capsomer that in contrast to actual 3-fold pores (the interface of 3 hexameric capsomers) do not coincide with an icosahedral 3-fold symmetry axis. (b) Electrostatic surface representations of both the inside and outside views are shown. 5- and (pseudo) 3-fold pores are clearly negatively charged on both sides and all the way through the pore itself. The potential pore at the 2-fold symmetry axis is positively charged (outside) right at the pore entrance due to the presence of two asparagine residues closing off the pore while the inside of the 2-fold ‘pore’ is strongly negatively charged similar to the other pores. TP binding sites around the 5- and 2-fold symmetry axes are indicated with yellow circles and large negatively charged surface patches close to TP binding sites are outlined by black dotted lines. These patches might be involved in increasing cargo affinity for the interior encapsulin shell close to the binding site due to ionic interactions with positively charged residues of the long IMEF cargo linker. (c) Electrostatic surface models of P-domains and E-loops (outlines on the left and surface on the right) highlighting complementary electrostatic interactions around 3-fold pores. d, Specific interactions observed at the interface of 3 capsid monomers. Strong cryo-EM density observed connecting subunits are outlined with red dotted lines. This density suggests aromatic interactions for Phe135 and Phe66 and potential anion-π interactions for Phe70 and Glu252. The interactions between the G-loop, E-loop and P-domain of 3 different subunits are likely one of the factors responsible for the observed thermal stability of this system. It is of note that the proposed Phe70-Glu252 interaction in the T = 4 IMEF encapsulin is located at the same location as the isopeptide bond observed in the HK97 bacteriophage capsid.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/46070/elife-46070-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** Annotated secondary structural elements, the consensus sequence and a sequence logo are shown above the sequences. Organisms and protein sequences used are shown below the alignment. Residues important for TP interaction (purple), formation of the 3- and 5-fold pores (red) and in forming the overall TP binding site (blue) are indicated with asterisks.

### Non-covalent chainmail and thermal stability of the IMEF-system

The IMEF compartment possesses a non-covalent chainmail topology and is highly thermostable. E-loops and P-domains of neighboring capsid monomers arrange head to tail to form interlocking concatenated rings resulting in a non-covalent chainmail topology (Figure 2d) (Zhang et al., 2013). This architecture has only been observed in a number of viral capsids including the HK97 bacteriophage but not in a bacterial system. In contrast to HK97 where an isopeptide bond covalently links E-loops and P-domains (Duda, 1998), the IMEF encapsulin uses non-covalent interactions. At each 3-fold pore, E-loops connect with two neighboring P-domains including the G-loop conserved in T = 4 encapsulins and their interfaces contain complementary electrostatic as well as aromatic and potential anion-π interactions (Figure 2e and Figure 2—figure supplement 1c,d) (Philip et al., 2011). The IMEF cargo protein shows a linear unfolding curve starting at ca. 40°C and extending to ca. 75°C followed by a hyperbolic increase leading to a midpoint of the thermal unfolding curve of 80.6°C. The shell protein is highly thermostable with a melting temperature of 86.6°C, respectively (Figure 2f). A stabilizing effect is observed for the cargo-loaded compartment (88.9°C). Compartments isolated from high iron conditions show even greater thermal stability (91.8°C) likely due to the internal cavity being stabilized by mineralized material.

### Structure and analysis of the IMEF cargo protein

Sequence and x-ray structure analysis show that the IMEF cargo represents a distinct class of ferritin-like protein (Flp) with an unusual ferroxidase center. Phylogenetic analysis revealed that the IMEF cargo protein is a member of the Flp superfamily and is most closely related to Dps proteins (Figure 3a and Supplementary file 3) but no known ferroxidase motifs could be detected based on the primary sequence alone (Andrews, 2010). IMEF proteins form a separate clade distinct from other Flp proteins associated with encapsulin systems. All IMEF proteins share a conserved C-terminal TP (Figure 3b). We determined the x-ray crystal structure of the IMEF cargo to a final resolution of 1.72 Å (Figure 3c and Supplementary file 4). The cargo adopts a four-helix bundle fold characteristic of other members of the Flp superfamily and forms a dimer with two Fe atoms bound at the subunit interface creating a ferroxidase site based on an alternative ferroxidase sequence motif (Figure 3d, Figure 3—figure supplement 1a,b). This leads to a combined molecular weight of the fully cargo-loaded IMEF compartment of 9.6 MDa (42 × cargo dimer [22.6 kDa]+240 × capsid protein, [32.2 kDa]). Through structure and sequence analysis, we identified a set of conserved residues involved in the formation of the dinuclear ferroxidase center. This IMEF ferroxidase motif differs from known examples and represents an alternative way of forming an inter-subunit ferroxidase center (Figure 3d). Due to flexibility, the C-terminal linker and TP are not resolved in the cargo x-ray structure in accordance with observations from our cryo-EM analysis. Removal of the 13 C-terminal residues results in empty encapsulin shells confirming that the IMEF TP is necessary for cargo encapsulation (Figure 3e).

![Figure 3.](https://cdn.elifesciences.org/articles/46070/elife-46070-fig3-v2.jpg)

**Figure 3.:** (a) Neighbor-joining phylogeny (cladogram) of protein classes involved in iron metabolism that are part of the Flp superfamily. Scale bar: amino acid substitutions per site. EncFlp: Flps found within encapsulin operons containing TPs, noEncFlp: Flps found outside encapsulin operons not containing TPs, Rr: rubrerythrins, Mam-Ftn: mammalian ferritins, Bac-Ftn: bacterial ferritins. (b) TP sequence of the Qs IMEF cargo protein and TP sequence logo highlighting strong sequence conservation. (c) X-ray crystal structure of the Qs IMEF cargo. (d) Di-iron ferroxidase active site of the IMEF cargo. The iron-coordinating residues are shown in stick representation. (e) SDS-PAGE gels of purified encapsulins showing that co-purification is dependent on the presence of the TP. (f) Cryo-EM map interior view of the 2-fold symmetry axis with TP density shown in cyan. (g) Close-up of additional cryo-EM density observed around the 2-fold symmetry axis. (h) Electrostatic surface representation of the TP binding site without (top) and with (bottom) TP. The 7 C-terminal IMEF residues are shown as a surface mesh.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/46070/elife-46070-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (a) Left: Chromatogram indicating that His-tagged IMEF exists as a mixture of dimer and monomer in solution (in the absence of encapsulin). Right: Calibration curve used to estimate molecular weights and oligomerization state. (b) Top: X-ray structure of the dimeric IMEF cargo. Middle: Cargo density observed above hexameric capsomers (2-fold symmetry axis). Bottom: Cargo density observed above pentameric capsomers (5-fold symmetry axis). The symmetry of cryo-EM cargo densities indicates averaging during cryo-EM reconstruction. The sizes of the densities observed in combination with x-ray and gel filtration experiments suggests that the IMEF cargo is present in a dimeric form when encapsulated. Due to steric hinderance it is very unlikely that on average more than one dimer per hexameric or pentameric capsomer is present in a fully loaded IMEF encapsulin. This means that when fully loaded 42 IMEF dimers are present per T = 4 IMEF encapsulin. (c) TP densities observed around the 5-fold symmetry axis. The densities are weaker than densities observed around 2-fold symmetry axes (Figure 3f). (d) Top: 2- and 5-fold TP binding sites. A mesh model of the modeled TP is shown in cyan. Yellow dotted lines highlight large negative surface patches. Conformational changes lead to a less pronounced surface groove for the 5-fold binding site (black arrow). Overall the 2- and 5-fold binding sites are different due to the different conformations of capsid monomers when present in hexameric vs. pentameric capsomers, explaining the different binding affinities and observed differing TP density strengths. Bottom: Sequence logo and consensus sequence of the flexible linker and TP of all identified IMEF cargo proteins indicating the presence of many positively charged residues at both ends of the linker connecting IMEF and TP. e, TP binding site (2-fold) highlighting key ionic interactions. The shell monomer is shown as ribbons, the TP is shown in stick representation.

### TP-mediated cargo-shell co-assembly

Additional cryo-EM density around the 2- and 5-fold symmetry axes reveals TP-binding sites and illuminates cargo-shell co-assembly. Through analysis of the T = 4 cryo-EM map, additional densities were identified that could not be explained by the encapsulin capsid protein (Figure 3f). These densities represent bound TPs anchoring IMEF cargo to the interior surface of the compartment. Even though only 42 cargo densities are observed, TP densities can be found at all 240 capsid monomers indicating averaging during cryo-EM reconstruction. Strong TP density is observed for all 180 monomers that are part of 2-fold symmetrical hexameric capsomers (Figure 3f) while substantially weaker density is found for TPs bound to the 60 pentameric monomers (Figure 3—figure supplement 1c) thus revealing higher occupancy and preferential TP binding around 2-fold symmetry axes which can be explained by different binding site conformations (Figure 3—figure supplement 1c–e) and higher local shell mobility (Figure 1—figure supplement 4). The main TP binding sites surrounding the 2-fold symmetry axes are formed by conserved residues of the P-domain and N-terminal helix (Figure 2—figure supplement 2) similar to the T. maritima T = 1 encapsulin system (Sutter et al., 2008). No TP binding site has been identified for T = 3 encapsulins yet. The presence of the N-terminal helix and the resulting binding site seems to generally underpin encapsulins’ ability to interact with TPs and encapsulate cargo proteins. The TP residues TVGSLIQ were tentatively built and refined into the additional density present at hexameric capsomers producing a model with good geometry (Figure 3—figure supplement 1e). The TP binds to a surface groove based on shape complementarity and two key ionic interactions with highly conserved positively charged residues locking the TP in place.

### Iron mineralization and storage by the IMEF-system

Heterologous expression of the IMEF core operon in E. coli leads to in vivo formation of large Fe- and P-rich electron-dense particles. Thin section negative stain transmission electron microscopy (TEM) of E. coli cells grown in Fe-rich (4 mM) medium and expressing the Qs IMEF core operon results in the formation of clusters of large intracellular electron-dense particles (Figure 4a and Figure 4—figure supplement 1a). Scanning TEM-energy-dispersive x-ray spectroscopy (EDS) revealed that these particles primarily contain uniformly distributed Fe, P and O with an estimated Fe:P ratio near 1 (Figure 4b). Selected area electron diffraction (SAED) further indicates that this mineralized material is amorphous (Figure 4—figure supplement 1b,c), similar to bacterioferritin systems (Andrews et al., 1993). The high P content and amorphous cores described for the IMEF encapsulin are similar to bacterioferritin systems (Aitken-Rogers et al., 2004; Mann et al., 1986). It has been hypothesized that amorphous material can be more readily mobilized under iron-limited condition than crystallized iron mineral (Watt et al., 1992; Watt et al., 2010).

![Figure 4.](https://cdn.elifesciences.org/articles/46070/elife-46070-fig4-v2.jpg)

**Figure 4.:** (a) Thin section micrographs of E. coli heterologously expressing the Qs IMEF core operon. Electron-dense particles often cluster together in regular arrays. Scale bars: 500 nm (left), 400 nm (right). (b) Close-up high angle angular dark field (HAADF) scanning TEM and EDS maps of a cluster of particles showing Fe, P and O as the main particle constituents. Scale bars: 100 nm. (c) Micrographs of uranyl formate (UF)-stained encapsulins produced in and isolated from E. coli grown in high iron media expressing the capsid protein alone (left) or the core operon (middle and right). Without UF stain, electron-dense particles are clearly visible (right). Scale bars: 250 nm. (d) Size distribution of electron-dense particles in unstained micrographs. (e) Electron energy loss spectroscopy (EELS) of 22 select cores carried out on isolated encapsulin particles. (f) HAADF-STEM micrographs and EELS maps of the two highlighted cores from (E). (g) In vitro ferroxidase assay of purified IMEF cargo at different Fe2+ concentrations. Mean values resulting from technical triplicates and error bands using standard deviation are shown. (h) Ferroxidase assay of cargo-loaded T = 4 encapsulin at different Fe2+ concentrations.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/46070/elife-46070-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (a) Top: Representative fields of view for E. coli expressing the core IMEF operon (IMEF cargo + capsid protein) under high iron conditions (4 mM Fe(NH4)2(SO4)2).Clusters of electron-dense particles are highlighted with white arrows. Bottom: E. coli cells expressing only the IMEF encapsulin capsid protein without the IMEF cargo. No clusters of electron-dense particles were observed. (b) HAADF-STEM images at high resolution show irregular non-crystalline material. (c) Selected area electron diffraction (SAED) of electron-dense particles was carried out on thin sections of E. coli expressing the core IMEF operon targeting clusters of electron-dense particles. No diffraction spots and thus no crystallinity could be observed meaning that the electron-dense material deposited inside IMEF encapsulin shells is amorphous (supported by the presence of faint concentric rings indicative of an amorphous phase). HAADF-STEM: high angle angular dark field scanning TEM. DF-TEM: dark field TEM.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/46070/elife-46070-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** (a) Top: Representative fields of unstained particles. Electron-dense cores are clearly visible even without stain. Bottom: Uranyl formate stained representative fields of the same particles. Images as shown on top were used to determine the core size distribution using ImageJ. (b) Geobacillus stearothermophilus ATCC 7953 was grown in high iron medium (4 mM) and samples prepared in early stationary phase (after 9 h). Representative fields of cells are shown with electron-dense cores highlighted by white arrows. Substantially fewer cores were observed in this strain that natively encodes the IMEF operon compared with recombinant E. coli heterologously expressing the IMEF operon. Consequently, no clustering of cores was observed. These thin section micrographs were not suitable for more detailed core analyses like EDS and EELS due to rapid carbon build-up and very high background. Thus, materials characterization of cores was done on purified iron-loaded particles that could be isolated in high quantity from recombinant E. coli resulting in less carbon build-up and better signal-to-noise. (c) Size distribution of native electron-dense cores formed in G. stearothermophilus. (d) Representative growth curve of G. stearothermophilus.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/46070/elife-46070-fig4-figsupp3-v2.jpg)

**Figure 4—figure supplement 3.:** (a) Three representative particles are shown with individual elemental EDS maps for Fe, P and O shown in orange, green and cyan, respectively. (b) Representative particles (HAADF-STEM images) and corresponding EELS maps are shown. (c) EELS spectra and fit for particle 1 and particle 13 (shown in Figure 4e and f in the main text, see also: Supplementary Table 5).

![Figure 4—figure supplement 4.](https://cdn.elifesciences.org/articles/46070/elife-46070-fig4-figsupp4-v2.jpg)

**Figure 4—figure supplement 4.:** Without a protein shell creating a barrier between the compartment interior and outside, autocatalytic oxidation of ferrous iron on enzymatically formed ferric iron precipitates is observed (left) leading to a sigmoidal time-course curve as shown in Figure 4g in the main text. However, in the presence of a protein shell, a characteristic hyperbolic enzyme catalysis curve is observed (Figure 4h). This suggests that the encapsulin shell strictly controls the influx of iron to the compartment interior and thus the internal concentration of iron substrate available to encapsulated IMEF cargo proteins. The overall effect of this arrangement is that mineralization inside the IMEF encapsulin is controlled and autocatalytic runaway iron precipitation prevented. This is likely of key importance for the functioning of this novel iron storage system in the bacterial cytoplasm resulting in an iron storage system able to safely store essential but also toxic iron in a soluble and bioavailable form.

The IMEF encapsulin mineralizes up to 30 nm Fe-rich cores in its interior with up to 23,000 Fe atoms stored per particle. IMEF encapsulins purified from E. coli grown under high Fe conditions contain electron dense cores visible in unstained samples with an average diameter of 23 nm (Figure 4c,d and Figure 4—figure supplement 2a). The largest observed particles are up to 30 nm in diameter. The theoretical size limit imposed by the T = 4 encapsulin protein shell is 36 nm and particles close to this size are observed in thin-sections of Geobacillus natively encoding the IMEF-system (Figure 4—figure supplement 2b–d). EDS analysis of particles isolated from E. coli and comparison with standards indicate a very similar elemental composition and elemental distribution as observed for thin section samples with a Fe:P ratio of 1:1.1 (Figure 4—figure supplement 3a). To determine the number of iron atoms stored per particle, we carried out electron energy loss spectroscopy (EELS) on purified Fe-loaded compartments (Figure 4e,f and Figure 4—figure supplement 3b,c). The highest observed number of stored Fe per particle was 23,293 (23.6 nm) (Supplementary file 5). Extrapolating to the maximum theoretical particle diameter of 36 nm and the highest density observed (3.40 Fe atoms/nm3) leads to a maximum number of Fe atoms that can be stored by the IMEF-system of around 83,000 (Supplementary file 5). Thus, IMEF-systems are able to store substantially more iron than any known ferritin system (2,000–4,000 Fe atoms) (Andrews, 1998; Harrison and Arosio, 1996).

To learn more about the mechanism of iron mineralization, we assayed peroxidase and ferroxidase activity. Due to the IMEF cargo being most closely related to Dps proteins we initially performed peroxidase assays using hydrogen peroxide as the oxidant. However, no peroxidase activity could be observed. Next, we assayed ferroxidase activity using O2 as the oxidant. For the IMEF cargo alone, a sigmoidal ferroxidase iron oxidation curve was observed indicative of autocatalytic Fe oxidation taking place at newly formed mineral surfaces (Bou-Abdallah et al., 2005; Sun and Chasteen, 1992). However, assaying the IMEF cargo-loaded encapsulin results in a typical hyperbolic enzyme catalysis curve. These observations imply that the encapsulin shell controls the flux of iron to the inside of the compartment leading to a controlled and low concentration of soluble iron in the encapsulin interior. Therefore, the IMEF cargo protein is able to enzymatically oxidize the majority of ferrous iron before uncontrolled autocatalytic mineralization can lead to bulk precipitation of iron which would likely destroy the iron storage function of the IMEF-system (Figure 4—figure supplement 4).

Our structural model and functional analysis of the IMEF encapsulin system reveal an alternative way to store large amounts of Fe independent of ferritins. The IMEF-system can in principle store more than 20 times more Fe than Ftn or Bfr systems. In contrast to ferritin systems, IMEF encapsulins are two-component systems with the catalytic activity separated from the protein shell. The IMEF cargo protein is flexibly tethered and primarily localizes 4.5 nm away from the capsid interior. This suggests that once iron enters the encapsulin interior via pores, it diffuses to the ferroxidase active site of the IMEF cargo, making it necessary to strictly control interior iron concentration to prevent runaway mineralization. This is different compared with ferritin systems where the ferroxidase activity is part of the shell and negatively charged surface patches guide iron from the pores to ferroxidase sites.

It is striking that IMEF-systems are confined to spore-forming Firmicutes. They inhabit a broad range of habitats with many of them initially isolated from hot springs or soil, environments with often limited or fluctuating iron availability (Colombo et al., 2014; Hou et al., 2013; Huang et al., 2013). The ability to store a much larger amount of iron than other microbes might benefit IMEF-encoding organisms in these environments and thereby contribute to their wide geographical distribution (Zeigler, 2014). In sum, we have elucidated the structure and mechanism of the largest iron storage complex to date indicating that alternative systems exist across nature to address the critical problem of safe and dynamic iron storage.

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
      <td>Strain, strain background (E. coli)</td>
      <td>MegaX DH10B T1R</td>
      <td>Thermo Fischer Scientific</td>
      <td>C640003</td>
      <td>Cloning strain</td>
    </tr>
    <tr>
      <td>Strain, strain background (E. coli)</td>
      <td>One Shot BL21 Star (DE3)</td>
      <td>Thermo Fischer Scientific</td>
      <td>C601003</td>
      <td>Expression strain</td>
    </tr>
    <tr>
      <td>Strain, strain background (Geobacillus stearothermophilus)</td>
      <td>ATCC 7953</td>
      <td>ATCC</td>
      <td>ATCC 7953</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pETDuet1</td>
      <td>EMD Millipore</td>
      <td>71146-3</td>
      <td>Expression vector</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Codon-optimized IMEF cargo protein gene + encapsulin capsid protein gene containing overhangs for Gibson Assembly (oligonucleotide gBlock)</td>
      <td>Integrated DNA Technologies (IDT)</td>
      <td>based on accessions: WP_039238473.1; WP_03923847</td>
      <td>gttaagtataagaaggagatatacaATGAAGGAAGAACTGGATGCTTTCCATCAGATTTTCACTACGACCAA AGAGGCAATCGAACGTTTTATGGCGATGCTGACCCCGGTCATTGAGAACGCGGAGGACGATCATGAGCGCCTGTATTATCATCATATCTACGAAGAGGAGGAGCAACGTCTGTCGCGCCTGGACGTTCTGATCCCACTGATCGAAAAGTTTCAAGATGAAACCGACGAAGGCCTCTTCTCCCCCTCCAACAACGCCTTTAACCGTCTGCTTCAGGAGCTGAATCTGGAAAAATTCGGTTTGCATAACTTTATCGAGCATGTTGACCTGGCCCTTTTTAGTTTCACCGACGAGGAACGCCAGACATTGCTTAAAGAACTGCGTAAAGATGCCTATGAAGGCTATCAGTATGTTAAAGAAAAACTGGCAGAAATTAACGCTCGTTTTGATCACGATTACGCAGACCCGCATGCGCACCATGATGAACACCGTGACCATCTTGCGGATATGCCCTCAGCGGGTTCATCGCACGAAGAAGTGCAGCCTGTTGCACATAAAAAGAAAGGTTTCACGGTGGGTTCATTAATCCAGTAAATTTCGCTTAAATATTACCGCTAGCTCAAAAAGGAGGAAAAGTGAATGAACAAAAGCCAACTTTATCCGGATTCACCACTGACGGATCAGGACTTCAACCAATTAGACCAAACCGTGATTGAGGCTGCTCGTCGTCAGCTGGTGGGTCGTCGCTTCATTGAGTTATATGGCCCATTGGGGCGTGG CATGCAGAGTGTCTTCAACGATATCTTCATGGAGTCTCATG AAGCGAAAATGGACTTCCAGGGCAGCTTTG ACACGGAGGTAGAGTCCTCCCGTCGTGTAAACTATACCATTCCGATGTTATATAAAGACTTCGTGCTTTACTGGCGCGATCTGGAACAGAGCAAGGCACTCGATATTCCGATCGACTTTTCAGTGGCAGCGAACGCTGCCCGCGACGTTGCGTTCCTGGAAGATCAGATGATTTTCCATGGAAGCAAAGAATTTGATATCCCGGGTCTGATGAACGTGAAAGGTCGCCTGACCCATCTGATTGGCAATTGGTATGAGTCGGGTAACGCCTTTCAGGATATTGTGGAGGCCCGCAATAAATTACTCGAAATGAACCACAATGGCCCATATGCTCTCGTGCTGTCCCCGGAGCTGTACTCACTCTTA CATCGTGTGCATAAAGACACGAATGTGCTGGAGATCGAACACGTGCGCGAGTTGATTACTGCTGGGGTTTTTCAGTCGCCTGTCCTCAAAGGGAAAAGTGGTGTGATCGTAAACACCGGTCGCAACAATCTGGATTTGGCTATCTCGGAAGATTTTGAGACTGCATACCTGGG CGAGGAAGGTATGAACCATCCCTTTCGCGTGTACGAGACAGTTGTTCTGCGCATCAAACGCCCGGCGGCCATTTGTACTTTAATCGATCCGGAAGAATAAattaacctaggctgctgccaccgct</td>
    </tr>
    <tr>
      <td>Sequence- based reagent</td>
      <td>Codon-optimized IMEF cargo protein gene w/o TP + encapsulin capsid protein gene containing overhangs for Gibson Assembly (oligonucleotide gBlock)</td>
      <td>Integrated DNA Technologies (IDT)</td>
      <td>based on accessions: WP_039238473.1; WP_039238471</td>
      <td>gttaagtataagaaggagatatacaATGAAGGAAGAACTGGATGCTTTCCATCAGATTTTCACTACGACCAAAGAGGCAATCGAACGTTTTATGGCGATGCTGACCCCGGTCATTGAGAACGCGGAGGACGATCATGAGCGCCTGTATTATCATCATATCTACGAAGAGGAGGAGCAACGTCTGTCGCGCCTGGACGTTCTGATCCCACTGATCGAAAAGTTTCAAGATGAAACCGACGAAGGCCTCTTCTCCCCCTCCAACAACGCCTTTAACCGTCTGCTTCAGGAGCTGAATCTGGAAAAATTCGGTTTGCATAACTTTATCGAGCATGT TGACCTGGCCCTTTTTAGTTTCACCGACGAGGAACGCCAGACATTGCTTAAAGAACTGCGTAAAGATGCCTATGAAGGCTATCAGTATGTTAAAGAAAAACTGGCAGAAATTAACGCTCGTTTTGATCACGATTACGCAGACCCGCATGCGCACCATGATGAACACCGTGACCATCTTGCGGATATGCCCTCAGCGGGTTCATCGCACGAAGAAGTGCAGCCTGTTGCATAAATTTCGCTTAAATATTACCGCTAGCTCAAAAAGGAGGAAAAGTGAATGAACAAAAGCCAACTTTATCCGGATTCACCACTGACGGATCAGGACTTCAACCAATTAGACCAAACCGTGATTG AGGCTGCTCGTCGTCAGCTGGTGGGT CGTCGCTTCATTGAGTTATATGGCCCA TTGGGGCGTGGCATGCAGAGTGTCTTCAACGATATCTTCATGGAGTCTCATGAAGCGAAAATGGACTTCCAGGGC AGCTTTGACACGGAGGTAGAGTCCTCCCGTCGTGTAAACTATACCATTCCGATGTTATATAAAGACTTCGTGCTTTACTGGCGCGATCTGGAACAGAGCAAGGCACTCGATATTCCGATCGACTTTTCAGTGGCAGCGAACGCTGCCCGCGACGTTGCGTTCCTGGAAGATCAGATGATTTTCCATGGAAGCAAAGAATTTGATATCCCGGGTCT GATGAACGTGAAAGGTCGCCTGACCCATCTGATTGGCAATTGGTATGAG TCGGGTAACGCCTTTCAGGATATTG TGGAGGCCCGCAATAAATTACTCGAAATGAACCACAATGGCCCATATGCTCTCGTGCTGTCCCCGGAGCTGTACTCACT CTTACATCGTGTGCATAAAGACACGAATGTGCTGGAGATCGAACACGTGCGCGAGTTGATTACTGCTGGGGTTTTTCAGTCGCCTGTCCTCAAAGGGAAAAGTGGTGTGATCGTAAACACCGGTCGCAACAATCTGGATTTGGCTATCTCGGAAGATTTTGAGACTGCATACCTGGGCGAGGAAGGTATGAACCATCCCTTTCGCGTGTACGAGACAGTTGTTCTGCGCATCAAACGCCCGGCGGCCATTTGTACTTTAATCGATCCGGAAGAATAAattaacctaggctgctgccaccgct</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Gibson Assembly Master Mix</td>
      <td>New England Biolabs</td>
      <td>E2611L</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>14% Novex Tris-Glycine Gel</td>
      <td>Thermo Fischer Scientific</td>
      <td>XP00140BOX</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>MIDAS screen</td>
      <td>Molecular Dimensions</td>
      <td>MD1–59</td>
      <td>Crystallization screen</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Pierce Coomassie Plus (Bradford) Assay</td>
      <td>Thermo Fischer Scientific</td>
      <td>23236</td>
      <td>Protein concentration determination4</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Isopropyl-β-D-thiogalactoside</td>
      <td>Millipore Sigma</td>
      <td>10724815001</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Lysozyme</td>
      <td>Millipore Sigma</td>
      <td>L6876</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>DNAse I</td>
      <td>Millipore Sigma</td>
      <td>11284932001</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Ni-NTA agarose resin</td>
      <td>Qiagen</td>
      <td>30210</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Polyethylene glycol 8000</td>
      <td>Millipore Sigma</td>
      <td>1546605</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Uranyl formate</td>
      <td>EMS</td>
      <td>22450</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Formaldehyde 37% in water</td>
      <td>Millipore Sigma</td>
      <td>252549</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Glutaraldehyde 25% in water</td>
      <td>Millipore Sigma</td>
      <td>G5882</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Picric acid</td>
      <td>Millipore Sigma</td>
      <td>197378</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Sodium cacodylate</td>
      <td>Millipore Sigma</td>
      <td>C0250</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Uranyl acetate</td>
      <td>EMS</td>
      <td>22400</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Propylene oxide</td>
      <td>Millipore Sigma</td>
      <td>82320</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Epon</td>
      <td>EMS</td>
      <td>14910</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Glycolic acid</td>
      <td>Millipore Sigma</td>
      <td>798053</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Trisodium citrate</td>
      <td>Millipore Sigma</td>
      <td>S1804</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Ammonium iron (II) sulfate</td>
      <td>Millipore Sigma</td>
      <td>F1543</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>ortho-phenylenediamine</td>
      <td>Millipore Sigma</td>
      <td>P9029</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Hydrogen peroxide 30 % in water</td>
      <td>Millipore Sigma</td>
      <td>216763</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Genome Neighborhood Network Tool (GNT)</td>
      <td>Gerlt et al., 2015</td>
      <td>https://efi.igb.illinois.edu/efi-gnt/</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>blastp</td>
      <td>NIH NCBI</td>
      <td>https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE=Proteins</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Clustal Omega</td>
      <td>McWilliam et al., 2013</td>
      <td>https://www.ebi.ac.uk/Tools/msa/clustalo/</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Simply Phylogeny</td>
      <td>Madeira et al., 2019</td>
      <td>https://www.ebi.ac.uk/Tools/phylogeny/simple_phylogeny/</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Geneious 9.14</td>
      <td>Biomatters Ltd</td>
      <td>https://www.geneious.com/</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>UCSF Chimera 1.13</td>
      <td>Pettersen et al., 2004</td>
      <td>https://www.cgl.ucsf.edu/chimera/</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Open Source PyMOL</td>
      <td>Schroedinger LLC</td>
      <td>https://github.com/schrodinger/pymol-open-source</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>I-TASSER</td>
      <td>Roy et al., 2010</td>
      <td>https://zhanglab.ccmb.med.umich.edu/I-TASSER/</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>IDT Codon Optimization Tool</td>
      <td>Integrated DNA Technologies (IDT)</td>
      <td>https://www.idtdna.com</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MotionCor2</td>
      <td>Zheng et al., 2017</td>
      <td>https://omictools.com/motioncor2-tool</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>CTFFIND4</td>
      <td>Rohou and Grigorieff, 2015</td>
      <td>http://grigoriefflab.janelia.org/ctffind4</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>SAMUEL</td>
      <td>Liao Lab</td>
      <td>https://liao.hms.harvard.edu/samuel</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Sam Viewer</td>
      <td>Liao Lab</td>
      <td>https://liao.hms.harvard.edu/samviewer</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Relion 3.0</td>
      <td>Scheres, 2012</td>
      <td>https://www3.mrc-lmb.cam.ac.uk/relion/index.php?title=Main_Page</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>SPIDER</td>
      <td>Frank et al., 1996</td>
      <td>https://spider.wadsworth.org/spider_doc/spider/docs/spider.html</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>ResMap</td>
      <td>Swint-Kruse and Brown, 2005</td>
      <td>http://resmap.sourceforge.net/</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Coot 0.8.9.1</td>
      <td>Emsley et al., 2010</td>
      <td>https://www2.mrc-lmb.cam.ac.uk/personal/pemsley/coot/</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Phenix 1.14</td>
      <td>Adams et al., 2010</td>
      <td>http://www.phenix-online.org/</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>XDS</td>
      <td>Kabsch, 2010</td>
      <td>http://xds.mpimf-heidelberg.mpg.de/</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>ACRIMBOLDO_LITE</td>
      <td>Sammito et al., 2015</td>
      <td>http://chango.ibmb.csic.es/arcimboldo_lite</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Phaser</td>
      <td>McCoy et al., 2007</td>
      <td>https://www.phaser.cimr.cam.ac.uk/index.php/Phaser_Crystallographic_Software</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>SHELX</td>
      <td>Thorn and Sheldrick, 2013</td>
      <td>http://shelx.uni-goettingen.de/</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>CCP4</td>
      <td>Winn et al., 2011</td>
      <td>http://www.ccp4.ac.uk/</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>REFMAC5</td>
      <td>Murshudov et al., 1997</td>
      <td>http://www.ccp4.ac.uk/html/refmac5.html</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Fiji-ImageJ 1.52h</td>
      <td>Schindelin et al., 2012</td>
      <td>https://fiji.sc/</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>UCSFImage4</td>
      <td>omicX</td>
      <td>https://omictools.com/ucsfimage-tool</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>200 Mesh Gold Grids</td>
      <td>EMS</td>
      <td>FCF-200-Au</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>400 Mesh Cu Holy Carbon Grids</td>
      <td>EMS</td>
      <td>Q410CR1.3</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Computational analysis of genomes, encapsulin gene clusters, sequences and protein structures

Initial identification of IMEF-systems was achieved by utilizing the Enzyme Similarity Tool (ESI) in combination with the Genome Neighborhood Network Tool (GNT) of the Enzyme Function Initiative (EFI) (Gerlt et al., 2015). The previously identified IMEF cargo protein from Q. thermotolerans (WP_039238471) was used as a query to initiate an ESI Sequence BLAST search of the UniProt database. UniProt BLAST Query E-value was chosen to be 5. After the initial dataset was created, we used an alignment score (based on the alignment score vs percent identity plot) that would correspond to a percent identity of 20 for initial outputting and interpretation of protein sequences and sequence similarity networks (SSNs). The resulting xgmml network file was then submitted to GNT. The resulting Genome Neighborhood Diagrams of all identified IMEF operons where analyzed using the GNT diagram explorer and operon diagrams were downloaded as svg files.

Genomes of IMEF-system-encoding organisms were searched for Ftn, Bfr and Dps proteins using NCBI’s blastp suite. As queries, Firmicute homologs of ferritin, bacterioferritin and Dps were used (Ftn: OTY20392, Bfr: EEK74551, Dps: WP_039234032).

Phylogenetic analysis was based on Clustal Omega (ClustalO) alignments carried out using the default settings of the Multiple Sequence Alignment online tool of the European Molecular Biology Laboratory’s European Bioinformatics Institute (EMBL-EBI). A nearest-neighbor phylogenetic trees based on the ClustalO alignment were generated using the Simple Phylogeny Tool at EMBL-EBI. Alignments and trees were then annotated and analyzed using Geneious 9.1.4.

Cryo-EM data and structural models were analyzed using UCSF Chimera 1.13.1rc and Open Source PyMOL 1.8.x. Structural alignments of capsid protein monomers were carried out in PyMOL using the align command. The IMEF model used for molecular replacement was generated using the I-TASSER webserver (Roy et al., 2010; Yang and Zhang, 2015).

### Molecular biology and cloning

All constructs used in this study were ordered as gBlock Gene Fragments from Integrated DNA Technologies (IDT). Codon usage was optimized for E. coli expression using the IDT Codon Optimization Tool with the amino acid sequences of the respective proteins of interest as input. For the IMEF operon containing multiple genes, intergenic regions were not changed. The IMEF cargo protein construct was ordered with a C-terminal His6 tag. For the operon construct containing the TP-less IMEF cargo, the 13 C-terminal residues (HKKKGFTVGSLIQ) were omitted from the IMEF cargo protein, thus removing the TP.

Gibson Assembly Master Mix was obtained from New England BioLabs (NEB). DNA sequencing was carried out by GENEWIZ. MegaX DH10B T1R electrocompetent E. coli cells (ThermoFisher) were used for all cloning procedures while One Shot BL21 Star (DE3) chemically competent E. coli cells (Invitrogen) were used for protein production and all other experiments. pETDuet1 was used as the expression vector for all constructs. For the construction of expression vectors, Gibson Assembly was employed. gBlock Gene Fragments containing 20 bp overlaps for direct assembly were combined with NdeI and PacI digested pETDuet1 resulting in assembled expression vectors (fragments were inserted in MCS2). Electrocompetent E. coli DH10B cells were transformed and the resulting plasmids confirmed via sequencing.

### Expression and purification of proteins and protein compartments

All non-high iron expression experiments were carried out in lysogeny broth (LB) supplemented with ampicillin (100 μg/mL). Size exclusion chromatography/gel filtration for capsid purification was performed with an ÄKTA Explorer 10 (GE Healthcare Life Sciences) equipped with a HiPrep 16/60 Sephacryl S-500 HR column (GE Healthcare Life Sciences). For analytical size exclusion, a Superdex 200 10/300 GL column (GE Healthcare Life Sciences) was used. Protein samples were concentrated using Amicon Ultra Filters (Millipore). For SDS-PAGE analysis, 14% Novex Tris-Glycine Gels (ThermoFisher Scientific) were used. DNA concentrations were measured using a Nanodrop ND-1000 instrument (PEQLab).

Sequence-confirmed plasmids were used to transform E. coli BL21 (DE3) Star cells (0.5 ng total plasmid DNA). Resulting colonies were used to inoculate pre-expression cultures.

For large scale protein expressions, 500 mL of LB in 2 L baffled flasks were inoculated (1:50) using an over-night culture, grown at 37°C and 200 rpm to an OD600 of 0.5. The temperature was then shifted to 30°C and the cultures induced with IPTG (final concentration: 0.05 mM). Cultures were grown at 30°C for 18 hr, harvested through centrifugation (4000 rpm, 15 min, 4°C) and pellets either immediately used or frozen in liquid nitrogen and stored at −20°C for later use.

For encapsulin and His-tagged protein purifications, pellets were thawed, resuspended in 5 mL Tris buffer (50 mM Tris, 150 mM NaCl, pH 8), then lysozyme (1 mg/mL) and DNaseI (1 μg/mL) were added and the cells incubated on ice for 20 min. Cell suspensions were subjected to sonication using a 550 Sonic Dismembrator (FisherScientific). Power level 3.25 was used with a pulse time of 8 s and an interval of 10 s. Total pulse time was 4 min. Cell debris was subsequently removed through centrifugation (8000 rpm, 15 min, 4°C). The cleared supernatant was then used either for protein affinity or encapsulin compartment purification.

His-tagged IMEF cargo was purified using Ni-NTA agarose resin (Qiagen) via the batch Ni-NTA affinity procedure following the supplier’s instructions. Buffer A (50 mM Tris, 150 mM NaCl, 20 mM imidazole, pH 8) was used to wash the resin after protein binding and buffer B (50 mM Tris, 150 mM NaCl, 250 mM imidazole, pH 8) was used to elute bound protein. Samples were concentrated and dialyzed using Amicon filters (10 kDa molecular weight cutoff) and Tris (pH 7.4) buffer and evaluated using SDS-PAGE. Further analyses were carried out directly or the next day with protein being stored on ice.

For encapsulin purification, 0.1 g NaCl and 0.5 g of PEG-8000 were added (10% w/v final concentration) to 5 mL cleared lysate, followed by incubation on ice for 20 min. The precipitate was collected through centrifugation (8000 rpm, 15 min, 4°C), suspended in 3 mL Tris (pH 8) buffer and filtered using a 0.2 μm syringe filter. The samples were then subjected to size exclusion chromatography using Tris (pH 8) buffer and a flow rate of 1 mL/min.

Fractions were evaluated using SDS-PAGE analysis and encapsulin-containing fractions were combined, concentrated and dialyzed using Amicon filters (100 kDa molecular weight cutoff) and Tris buffer without NaCl (20 mM Tris, pH 8).

The low salt sample was then loaded on a HiPrep DEAE FF 16/10 Ion Exchange column (GE Healthcare Life Sciences). The gradient used for ion-exchange chromatography was as follows: 100% A for 0–100 mL, 100% A to 50% A + 50% B for 100–200 mL, 100% B for 200–300 mL, 100% A for 300–400 mL (A: 20 mM Tris, pH 8, B: 20 mM Tris, 1 M NaCl, pH 8, flow rate: 3 mL/min). Again, SDS-PAGE was used to identify product fractions followed by Amicon filter concentration and buffer exchange to Tris buffer (50 mM Tris, 150 mM NaCl, pH 8).

Final samples were either directly subjected to additional experiments or stored on ice overnight.

### Negative stain transmission electron microscopy (TEM) of purified encapsulins

200 Mesh Gold Grids (FCF-200-Au, EMS) were used for all negative stain TEM experiments. TEM experiments of negatively stained protein samples were carried out at the HMS Electron Microscopy Facility using a Tecnai G2 Spirit BioTWIN instrument.

For negative-staining TEM, encapsulin samples were diluted to 1–10 μM using Tris buffer (50 mM Tris, 150 mM NaCl, pH 8) and subsequently adsorbed onto formvar/carbon coated gold grids. Prior to applying 5 μL of diluted sample, grids were glow-discharged using a 100x glow discharge unit (EMS) to increase their hydrophilicity (10 s, 25 mA). After 1 min adsorption time, excess liquid was blotted off using Whatman #1 filter paper, washed one time with distilled H2O and floated on a 10 μL drop of staining solution (0.75% uranyl formate in H2O) for 35 s. After removal of excess staining solution, samples were used for TEM analysis at 80 kV.

### Thin section TEM analysis of fixed bacterial cells

For TEM analysis of fixed cells, 0.5 mL of early stationary phase bacterial culture was fixed by adding fixative (1:1 v/v, 1.25% formaldehyde, 2.5% glutaraldehyde, 0.03% picric acid in 0.1 M sodium cacodylate buffer, pH 7.4). The sample was then incubated at 25°C for 1 hr and centrifuged for 3 min at 3000 rpm. The sample was then further incubated for 6–18 hr at 4°C. Cells were subsequently washed three times in cacodylate buffer, 4 times with maleate buffer pH 5.15 followed by staining with 1% uranyl acetate for 30 min. The sample was dehydrated (15 min 70% ethanol, 15 min 90% ethanol, 2 × 15 min 100% ethanol) and exposed to propyleneoxide for 1 hr. For infiltration, a mixture of Epon resin and proylenoxide (1:1) was incubated for 2 hr at 25°C before moving it to an embedding mold filled with freshly mixed Epon. The sample was allowed to sink and subsequently moved to a polymerization oven (24 hr, 60°C). Ultrathin sections (60–90 nm) were then cut at −120°C using a cryo-diamond knife (Reichert cryo-ultramicrotome) and transferred to formvar/carbon coated grids.

### Cryo-electron microscopy (cryo-EM) data collection and processing

To prepare grids for cryo-EM imaging, 2.5 μL of purified cargo-loaded IMEF encapsulin at a concentration of 1.5 mg/mL was applied to glow-discharged Quantifoil holey carbon grids (1.2/1.3, 400 mesh), and blotted for 3 s with ~90% humidity before plunge-freezing in liquid ethane using a Cryoplunge 3 System (CP3, Gatan). Cryo-EM images were collected at Harvard Medical School on a Tecnai F20 electron microscope (FEI) operating at 200 kV and equipped with a K2 Summit direct electron detector (Gatan). Movies were collected at a nominal magnification of 29,000 with a calibrated pixel size of 0.64 Å. All movies were collected in super-resolution counting mode using UCSFImage4, with a total exposure time of 7.2 s and a frame time of 200 milliseconds. The details of EM data collection parameters are listed in Supplementary file 2.

Dose-fractionated super-resolution movies collected on the K2 detector were binned over 2 × 2 pixels, and subjected to motion correction using the program MotionCor2 (Zheng et al., 2017). Dose-weighted sums from all frames were used for all subsequent image-processing steps except for defocus determination. The CTFFIND4 program (Rohou and Grigorieff, 2015) was used to determine the defocus values of the summed images from all movie frames without dose weighting. Semi-automated particle picking from 6x binned images was performed with SAMUEL and SamViewer (Ru et al., 2015). Selected particles were extracted from unbinned images with an initial box size of 512 pixels, and subsequently binned to a box size of 128 pixels with a pixel size of 5.12 Å for two rounds of 2D classification using RELION 3.0 (Scheres, 2012). An initial 3D model was generated via SPIDER (Frank et al., 1996) 3D projection matching refinement (samrefine.py) using 2D class averages, starting from a sphere density similar in size and shape of the IMEF encapsulin. The selected particles after 2D classification were binned to a box size of 480 pixels (corresponding to a pixel size of 1.365 Å) and used for 3D refinement in RELION 3.0 with icosahedral symmetry (‘I’) imposed. A final round of 3D refinement was performed in RELION 3.0 after fitting individual particle defocus parameters and beam-tilt with ‘relion_ctf_refine’. Post-processing was performed with ‘relion_postprocess’ to apply a negative b-factor and correct the amplitude information in the final map. The overall resolutions were estimated based on the gold-standard criterion of Fourier shell correlation (FSC) = 0.143. Local resolution variations were estimated from two half data maps using ResMap (Swint-Kruse and Brown, 2005).

### Cryo-EM model building and refinement

An initial model of an IMEF encapsulin monomer was generated by homology modeling with the I-TASSER webserver (Zhang, 2008) using the x-ray crystal structure of the T = 3 Pyrococcus furiosus encapsulin (PDB ID: 2E0Z) as a template. The monomer model was then fit into the 3D map in UCSF Chimera (Pettersen et al., 2004), and subsequently adjusted manually in COOT (Emsley et al., 2010) prior to refinement in PHENIX (Adams et al., 2010) with phenix.real_space_refine. The refined monomer coordinates were copied and manually positioned to occupy the four monomer positions of the asymmetric unit (ASU), followed by manual adjustment of each monomer in COOT. Several rounds of real-space refinement and manual adjustment of the coordinates for four monomers in the ASU were performed in phenix.real_space_refine and COOT. During refinement of coordinates in the ASU no non-crystallographic symmetry restraints were utilized in order to avoid distortion of the E-loop in each monomer. The refined coordinates for the ASU were subsequently expanded using the symmetry matrices utilized by RELION 3.0 during 3D reconstruction to generate a model of the entire encapsulin cage containing 60 ASUs and 240 total IMEF encapsulin capsid protein polypeptide chains. Coordinates for the entire IMEF encapsulin cage were refined in phenix.real_space_refine with proper NCS restraints between corresponding chains in individual ASUs in order to resolve any inter-protomer clashes.

### Symmetry expansion and focused classification

In an attempt to better resolve cargo density within the encapsulin shell we used an approach combining symmetry expansion and focused classification with residual signal subtraction. Prior to symmetry expansion and focused classification, particles were binned to a box size of 192 with a corresponding pixel size of 3.41 Å. Following refinement of binned particles with icosahedral symmetry, a 60 Å low-pass filtered mask of a hexameric encapsulin shell unit with associated cargo density was generated (Figure 1—figure supplement 3a). Symmetry expansion was performed with relion_particle_symmetry_expand specifying ‘I’ symmetry to generate a new particle stack with 60x increased particle number. Residual signal subtraction was performed as described previously (Bai et al., 2015) to subtract encapsulin shell and cargo densities outside of the 60 Å low-pass filtered mask from the symmetry expanded particle dataset (Figure 1—figure supplement 3b). Focused classification without alignment and without applied symmetry was then performed in Relion3.0 to resolve cargo density bound in different configurations to the encapsulin shell and potential connections between the cargo and targeting peptide (Figure 1—figure supplement 3c).

### Differential scanning fluorimetry (DSF) to test thermal stability of proteins

DSF measurements were performed using a NanoTemper Tycho NT.6 instrument according to the manufacturer’s instructions. Samples in Tris buffer (50 mM Tris, 150 mM NaCl, pH 8) at a concentration of 0.5 mg/mL were measured in triplicate and subjected to a temperature gradient from 35°C to 95°C at 0.5°C per second. Data were analyzed using NT Melting Control software. Melting temperatures (Tm) were determined by automatic fitting of experimental data using a polynomial function, where the maximum slope (Tm) is indicated by the peak of its first derivative.

### Crystallization and x-ray structure determination of the IMEF cargo protein

Initial crystallization conditions were determined using the Midas screen (Grimm et al., 2010). Large single crystals were grown in sitting drop plates by the vapor diffusion method. Reservoir solutions contained 10% v/v Pentaerythritol ethoxylate (3/4 EO/OH) and 10% butanol. Crystals were cryo-protected in reservoir solution supplemented with 15% ethylene glycol and 20 mM glycolic acid pH 7.5. Diffraction data were collected at the European Synchrotron Radiation Facility (ESRF) Grenoble outstation at the ID-30b beamline at 100 K with a Pilatus3 6M pixel detector (DECTRIS, Switzerland). Data were indexed, processed, and scaled with the XDS package (Kabsch, 2010). The structure was solved by molecular replacement using an I-TASSER homology model and the program ACRIMBOLDO_LITE (Sammito et al., 2015) incorporating PHASER (McCoy et al., 2007) and SHELX (Thorn and Sheldrick, 2013) from the CCP4 suite (Winn et al., 2011). Model building and refinement was carried using COOT (Emsley and Cowtan, 2004) and REFMAC5 (Murshudov et al., 1997),respectively.

### Determination of electron-dense core diameters

To determine the size distribution of electron-dense cores resulting from IMEF mineralization under high iron conditions, TEM micrographs were analyzed using the open source image processing package Fiji based on ImageJ 1.52 hr (Schindelin et al., 2012). Micrographs were converted to 8-bit binary images, thresholded and processed using the particle analyzer plugin. The diameters reported are based on Fiji Feret diameter output values.

### In vivo mineralization of electron-dense particles

Overnight cultures were used to inoculate 500 mL LB medium (1:50) supplemented with ampicillin and grown at 37°C to an OD600 of 0.5. Expression was induced with 0.05 mM IPTG. Cultures were incubated at 30°C for 2 hr. LB medium was removed and replaced with fresh modified LB (LB +50 mM Hepes, 4 mM Trisodium citrate, pH 7) supplemented with freshly prepared ammonium iron(II) sulfate (Fe(NH4)2(SO4)2, final concentration: 4 mM; stock solution: 400 mM in 0.1 M HCl). The cultures were then incubated at 30°C for 18 hr and used for either the purification of iron-loaded encapsulin compartments or thin section TEM analysis.

### Iron-rich core characterization via energy-dispersive x-ray spectroscopy (EDS) and electron energy loss spectroscopy (EELS)

TEM and high angle angular dark field (HAADF) STEM imaging and analysis were performed on a JEOL ARM 200F operated at 80 kV. EDS spectra were collected using an EDAX Octane W 100mm2 detector, and spectra analyzed post-collection both via TEAM software and offline using the k-ratio method (thin film approximation). EELS mapping data of the Fe L edge were acquired using a Gatan Enfinium spectrometer with dispersion 0.25 eV/ch using DualEELS mode with simultaneous zero loss spectrum collection. EELS data were processed using the Gatan EELS analysis plug-in. The processing steps involved a Gaussian fitting of the zero loss peak, integrating under the FeL edge up to 780 eV after applying a power law or first order log-polynomial (whichever fit the background better, as this depended on local carbon contamination levels) and correcting for the Fe cross section of 2664.9 barns, from which the average number of Fe per nm2 was calculated per pixel of data. These pixels were summed over the area of each particle to estimate the total number of Fe atoms. Errors in this measurement were calculated from a statistical analysis of the data fitting combined with the expected error from Fe cross sectional extrapolation. Particle diameters were estimated using a histogram method to determine the edge onset of each particle, with the mean of multiple measurements from each particle used (and error determined by the standard deviation of these measurements).

### Cultivation of Geobacillus stearothermophilus ATCC 7953

For normal growth of G. stearothermophilus, Meat Media (3 g meat extract, 5 g peptone, 1 L H2O) was utilized. G. stearothermophilus was maintained on Meat Media agar plates (15 g agar/L). All growth was carried out a 55°C. For high iron growth experiments Meat Media was supplemented with 50 mM Hepes, 4 mM Trisodium citrate and 4 mM Fe(NH4)2(SO4)2 and the pH adjusted to seven using HCl. Growth curves were recorded in high iron Meat Media in 96-well plates (volume: 500 μL) using a Synergy H1 plate reader (BioTek) and inoculated (1:50) from a pre-culture grown for 24 hr in standard Meat Media.

### Peroxidase assays

Peroxidase activity of free IMEF cargo and cargo-loaded IMEF encapsulin was assayed by measuring the oxidation of ortho-phenylenediamine (OP) by hydrogen peroxide (Pesek et al., 2011). OP dilutions from 10 to 80 mM were prepared from a stock solution (92.5 mM in 50 mM Tris, pH 8) using Tris buffer (pH 8). 96-well plates were used to carry out the assays in triplicate. Each well contained 100 μL of OP dilution and 0.5 μM of IMEF cargo protein (protein concentrations were determined via Bradford assay (Pierce Coomassie, ThermoFisher) following the manufacturer’s instructions). To start the assays, 2 μL of 30% hydrogen peroxide solution was added. After 15 min of incubation in the dark, assays were stopped by the addition of 100 μL of 0.5 M H2SO4. Then, absorbance at 490 nm was determined using a Synergy H1 plate reader.

### Ferroxidase assays

Protein solutions in Tris buffer (50 mM Tris, 150 mM NaCl, pH 8) and Fe(NH4)2(SO4)2 stock solutions in 0.1 M HCl were made anaerobic by incubation in a Vinyl Anaerobic Chamber (Coy Lab Products) for 24 hr. All solutions were exposed to the anaerobic atmosphere inside the chamber and protein solutions were kept on ice. IMEF cargo protein was used at a final concentration of 50 μM while cargo-loaded encapsulin concentrations were used that would correspond to 5 μM IMEF cargo (higher concentrations led to rapid protein precipitation upon iron addition). Final iron(II) concentrations ranged from 10 to 100 μM. Ferroxidase activity was initiated by combining appropriate dilutions of protein and iron solution to a final volume of 250 μL in a quartz cuvette in the air, directly after removing solutions from the anaerobic chamber. Ferroxidase activity was immediately measured by monitoring Fe3+ formation at a wavelength of 315 nm in a Nanodrop 2000c for 25 min.

### Data availability

A cryo-EM density map of the cargo-loaded IMEF encapsulin has been deposited in the Electron Microscopy Data Bank under the accession number 9383. The corresponding atomic coordinates for the atomic model have been deposited in the Protein Data Bank (accession number: 6NJ8). Atomic coordinates for the IMEF cargo protein have been deposited in the Protein Data Bank under accession number 6N63. Correspondence and requests for materials should be addressed to the corresponding authors.
