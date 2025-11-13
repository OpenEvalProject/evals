# Insights into AMS/PCAT transporters from biochemical and structural characterization of a double Glycine motif protease

## Authors

- Silvia C Bobeica<sup>1</sup> ([ORCID: 0000-0001-5058-5543](https://orcid.org/0000-0001-5058-5543))
- Shi-Hui Dong<sup>2</sup> ([ORCID: 0000-0002-1743-2163](https://orcid.org/0000-0002-1743-2163))
- Liujie Huo<sup>1</sup>
- Nuria Mazo<sup>3</sup>
- Martin I McLaughlin<sup>1</sup> ([ORCID: 0000-0003-4410-0786](https://orcid.org/0000-0003-4410-0786))
- Gonzalo Jiménez-Osés<sup>3</sup> ([ORCID: 0000-0003-0105-4337](https://orcid.org/0000-0003-0105-4337))
- Satish K Nair<sup>2</sup> ([ORCID: 0000-0003-1790-1334](https://orcid.org/0000-0003-1790-1334)) †
- Wilfred A van der Donk<sup>1</sup> ([ORCID: 0000-0002-5467-7071](https://orcid.org/0000-0002-5467-7071)) †

### Affiliations

1. Roger Adams Laboratory, Department of Chemistry University of Illinois at Urbana-Champaign Urbana United States
2. Roger Adams Laboratory, Department of Biochemistry University of llinois at Urbana-Champaign Urbana United States
3. Departamento de Química, Centro de Investigación en Síntesis Química Universidad de La Rioja La Rioja Spain
4. CICbioGUNE Derio Spain
5. Center for Biophysics and Computational Biology University of Illinois at Urbana-Champaign Urbana United States
6. Howard Hughes Medical Institute, University of Illinois at Urbana-Champaign Urbana United States

† Corresponding author

## Abstract

The secretion of peptides and proteins is essential for survival and ecological adaptation of bacteria. Dual-functional ATP-binding cassette transporters export antimicrobial or quorum signaling peptides in Gram-positive bacteria. Their substrates contain a leader sequence that is excised by an N-terminal peptidase C39 domain at a double Gly motif. We characterized the protease domain (LahT150) of a transporter from a lanthipeptide biosynthetic operon in Lachnospiraceae and demonstrate that this protease can remove the leader peptide from a diverse set of peptides. The 2.0 Å resolution crystal structure of the protease domain in complex with a covalently bound leader peptide demonstrates the basis for substrate recognition across the entire class of such transporters. The structural data also provide a model for understanding the role of leader peptide recognition in the translocation cycle, and the function of degenerate, non-functional C39-like domains (CLD) in substrate recruitment in toxin exporters in Gram-negative bacteria.

## Introduction

The translocation of peptides and proteins across the membrane bilayer is a fundamental process in all three domains of life (Rapoport et al., 2017). Bacteria secrete peptides and proteins for survival and adaptation to different ecological niches, to mediate intercellular signaling, and to deter or kill other microorganisms that may compete for limited resources (Abele and Tampé, 2018). Transport of intracellularly produced peptides in bacteria is mediated by ABC transporters, which utilize the energy of ATP binding and hydrolysis to translocate substrates across the bilayer (ter Beek et al., 2014; Beis, 2015). These transporters often contain an N-terminal protease domain, which belongs to the C39 class of cysteine proteases (Interpro:IPR005897) (Rice et al., 2014; Michiels et al., 2001). The dual-functional transporters, called ABC-transporter maturation and secretion (AMS) proteins or peptidase-containing ATP-binding transporters (PCAT), excise a leader sequence concomitant with the unidirectional extracellular export of the mature peptide (Håvarstein et al., 1995; van Belkum et al., 1997).

In Gram-positive bacteria, the AMS/PCATs export peptides that mediate quorum signaling (Pestova et al., 1996) or exert antimicrobial activity upon removal of the leader peptide (van Belkum et al., 1997). Peptide substrates for the transporters contain leader sequences that typically end in a double Gly motif (Gly-Gly; Gly-Ala; Gly-Ser), and mutational analysis of the ComA transporter identified a consensus recognition sequence of Leu(−12)-(X)3-Glu(−8)-Leu(−7) located N-terminal to this double Gly motif (Ishii et al., 2010).

In Gram-negative bacteria, the AMS/PCATs are a component of a membrane protein complex containing an outer membrane protein/factor (OMF) and an accessory protein to form the type I secretion system (T1SS) (Létoffé et al., 1996). Some T1SS complexes contain an AMS/PCAT transporter that lacks proteolytic activity due to the absence of the catalytically requisite Cys, and their N-terminal extension has thus been named C39-like domain (CLD) (Kanonenberg et al., 2013). Despite the lack of proteolytic activity, the CLD domain is necessary to recruit and tether the unfolded substrate during secretion through a yet-to-be established mechanism (Lecher et al., 2012).

The biosynthetic clusters of bacteriocins typically contain an AMS/PCAT exporter that directs the processing and secretion of double Gly-type leader sequences. Examples include colicin V and similar class II bacteriocins, and various classes of ribosomally synthesized and posttranslationally modified peptides (RiPPs) (Arnison et al., 2013). RiPPs are made from a precursor peptide that is morphed into a final bioactive product with a much larger structural diversity than can be achieved with the 20 proteinogenic amino acids. During this process, posttranslational modification enzymes often act iteratively on a subset of amino acids present in a C-terminal core peptide in a process that is directed by an N-terminal leader peptide (Oman and van der Donk, 2010). Following the installation of these posttranslational modifications, the cognate AMS/PCAT catalyzes the removal of the leader peptide via cleavage at the double Gly motif and extracellular secretion of the bioactive natural product (Håvarstein et al., 1995). Two particularly large classes of these double-Gly leader peptides belong to the Nif11 and nitrile hydratase families (Haft et al., 2010). Notably, the dual-functional transporters must ensure that modified and processed bacteriocins or RiPPs are directly shuttled out of the producing organism but the details for this fail-safe mechanism are not yet known.

The structure of a full-length PCAT from Clostridium thermocellum (termed PCAT1), containing both the C39 protease and the ABC transporter, demonstrated that the protease domain interacts with a transmembrane channel in the absence of bound nucleotide (Lin et al., 2015). Binding of ATP results in the disengagement of the protease domain from the helices of the transmembrane domain (TMD), suggesting an ‘alternating-access’ model for peptide translocation. Notably, biochemical studies of PCAT1 using a peptide substrate showed that proteolytic activity is enhanced during association with the TMD, but the underpinnings of this enhancement were unclear in the absence of a peptide substrate-bound structure.

Here, we identified and characterized LahT150, a sequence tolerant protease domain of the full-length AMS/PCAT LahT. We show that this protease can remove leader peptides from a large number of double Gly motif-containing peptides. In order to explain this tolerance for a broad range of substrates, we determined the 2.0 Å resolution crystal structure of the LahT protease domain in complex with a covalently bound leader peptide analog. Our structural and biochemical data provide insights into the determinants of substrate specificity. Modeling studies based on the structure of full-length PCAT1 provide insights how the AMS/PCAT transporters may prevent the escape of processed substrate into the cytoplasm of the producing cells. These studies explain much prior data on this large class of bifunctional exporters.

## Results and discussion

### Diversity and distribution of AMS/PCAT Transporters

We used the EFI-EST Tools (Gerlt et al., 2015) to generate a sequence similarity network (SSN) of likely AMS/PCAT members in GenBank. An alignment cutoff of at least 45% sequence identity was used to separate the clusters in this analysis. The results show that AMS/PCAT transporters are distributed across various phyla of both Gram-positive and Gram-negative bacteria (Figure 1). Interestingly, the largest cluster from this SSN contains members from both Gram-positive (Firmicutes, Actinobacteria, Proteobacteria) and Gram-negative bacteria (Bacteroidetes, Cyanobacteria, Spirochaetes).

![Figure 1.](https://cdn.elifesciences.org/articles/42305/elife-42305-fig1-v2.jpg)

**Figure 1.:** Alignment cutoff of at least 45% sequence identity was applied to separate the clusters. The nodes representing LahT homolog sequences are colored by their corresponding phylum. Nodes of several characterized LahT homologs are marked by red circles and are labeled. The SSN tool draws sequences from UniProt; To increase the coverage of the network, additional sequences not in UniProt were added manually (grey nodes).

### Identification of a substrate tolerant protease

As a step toward advancing a biochemical and structure-function understanding of AMS/PCAT transporters and providing a tool for removing leader peptides from RiPP products, we sought to identify protease domains that retained catalytic activity in the absence of the TMD. Previous studies have demonstrated that the N-terminal 150 amino acids of AMS/PCAT proteins constitute peptidase C39 family members that can be expressed as individual active domains (Håvarstein et al., 1995; Furgerson Ihnken et al., 2008; Ishii et al., 2006; Wu and Tai, 2004; Wang et al., 2016). In search of a substrate tolerant protease domain, we first surveyed AMS transporters encoded in gene clusters containing multiple genes for precursor peptides with diverse core peptide sequences, because these proteases are expected to be inherently tolerant with respect to residues in the P’ positions. We initially focused on the N-terminal protease domain of a transporter in Prochlorococcus MIT9313, which encodes 30 different RiPP substrates with leader peptides of the double Gly type (Li et al., 2010). Unfortunately, this domain did not prove active in our hands. We next turned to the protease domain of the FlvT transporter from Ruminococcus flavefaciens FD-1, encoded in a cluster with 12 substrate peptides (Zhao and van der Donk, 2016), but it also did not provide the desired robust activity. The lack of activity for these excised C39 protein domains is not unexpected, given prior studies that show that association with the TMD significantly enhances proteolytic activity of the protease domain in PCAT1 (Lin et al., 2015) and NukT (Nishie et al., 2011).

We next investigated an AMS/PCAT transporter LahT encoded in a gene cluster in a member of the human commensal microbiota, Lachnospiraceae bacterium C6A11 (genome from Bioproject ID 223496/Accession PRJNA223496). This cluster encodes nine different putative precursor peptides (LahA1-9) with diverse core peptide sequences and relatively conserved double Gly-motif leader peptides of the Nif11 type (Figure 2). Expression of the N-terminal 150 amino acids of LahT as a His6-tagged fusion protein resulted in an active protease termed LahT150 that readily removed the leader peptide from the seven tested substrates encoded in the lah cluster at the predicted double Gly motif as monitored with matrix-assisted laser desorption time-of-flight mass spectrometry (MALDI-TOF MS) (Figure 3 and Figure 3—figure supplement 1). Given the high divergence of the core peptide sequences of these peptides (Figure 2), the enzyme is highly tolerant to variation of the substrate sequence in the P’ positions.

![Figure 2.](https://cdn.elifesciences.org/articles/42305/elife-42305-fig2-v2.jpg)

**Figure 2.:** The double Gly motif is boxed.

![Figure 3.](https://cdn.elifesciences.org/articles/42305/elife-42305-fig3-v2.jpg)

**Figure 3.:** (A–B) MALDI ToF MS analysis of full length N-terminally hexahistidine tagged LahA4 and LahA7. (C) MALDI ToF MS analysis of the core peptides of LahA4 and LahA7 after LahT150 cleavage. Core peptide masses are [M + H]+: LahA4 (calcd 2352.2; obsd 2352.0), LahA7 (calcd 2660.3; obsd 2659.8). (D) MALDI TOF MS analysis of the leader peptides of LahA4 and LahA7 after LahT150 cleavage. Leader peptide average masses are [M + H]+: LahA4-leader (calcd 10188.8, obsd 10187.5), LahA7-leader (calcd 9246.9, obsd 9248.7). For five additional LahA substrates, see Figure 3—figure supplement 1.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/42305/elife-42305-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** MALDI ToF MS analysis of LahA peptides treated with LahT150. Core peptide ([M + H]+) masses: LahA1 (theor 2616.4; obs 2616.5). LahA2 (theor 2761.4; obs 2762.0). LahA3 (theor 2740.4; obs 2740.7). LahA5 (theor 2811.4; obs 2810.8). LahA6 (theor 2771.4; obs 2771.4). Leader peptide average [M + H]+ masses: LahA1-leader (theor 9973.6, obs 9973.3), LahA2-leader (theor 9827.6, obs 9830.1), LahA3-leader (theor 9756.5, obs 9751.2); LahA5-leader (theor 9964.8, obs 9969.1), LahA6-leader (theor 9458.6, obs 9462.9).

### Substrate tolerance of LahT150

Having established that LahT150 is highly forgiving with respect to the sequence of the core peptide of its cognate substrates as illustrated by the amino acids accepted after the cleavage site (Figure 2 and Figure 3), we investigated its tolerance toward variations in the leader peptide. Select members of the ProcA peptides from Prochlorococcus MIT 9313 were first tested. This strain makes up to 30 different prochlorosins, members of the lanthipeptide family that are characterized by multiple thioether crosslinks introduced by posttranslational modifications (Figure 4A). Removal of their leader peptides has been challenging and has hampered production of the mature lanthipeptide products (Tang and van der Donk, 2012). We therefore tested LahT150 with a selection of ProcA peptides that were first posttranslationally modified by ProcM to introduce a variety of thioether ring structures (Li et al., 2010; Shi et al., 2011; Bobeica and van der Donk, 2018). The ProcM-modified ProcA peptides tested (five in total) proved to be substrates for LahT150 (Figure 4B and Figure 4—figure supplement 1), producing the mature prochlorosins (Pcns) and demonstrating that the enzyme can process substrates that contain polycyclic structures in the core peptide.

![Figure 4.](https://cdn.elifesciences.org/articles/42305/elife-42305-fig4-v2.jpg)

**Figure 4.:** Serine and threonine residues are dehydrated by a lanthionine synthetase, resulting in dehydroalanine (Dha) and dehydrobutyrine (Dhb). The synthetase then catalyzes the Michael type addition of neighboring cysteine residues to the dehydrated residues. (B) Removal of the leader peptide of posttranslationally modified ProcA2.8 monitored by MALDI-TOF MS. Core peptide (two-fold dehydrated) [M + H]+: calcd 2050.8, obsd 2050.9. For four additional ProcA substrates, see Figure 4—figure supplement 1. (C) In vitro leader peptide removal of AzoA6 bearing an N-terminal maltose binding protein tag. Core peptide [M + H]+: calcd 3399.9, obsd 3400.4. For two additional AzoA substrates, see Figure 4—figure supplement 2. (D–F) MALDI TOF MS analysis of LahT150 catalyzed cleavage of the RiPP precursor peptides HalA2, LctA and SunA. Core peptide masses (left panels): HalA2 (calcd 3064.4; obsd 3064.6); LctA (calcd [M + H]+ 3011.3 and [M + H + O]+ 3027.3; obsd 3011.4 and 3027.4); SunA (calcd 3718.7; obsd 3718.6). Leader peptide ([M + H]+) masses (right panels): HalA2-leader peptide (calcd avg. 5969.5; obsd 5969.5); LctA-leader peptide (calcd avg. 4754.2; obsd 4754.6); SunA-leader peptide (calcd avg. 4311.7, obsd 4311.2). (G) Sequence conservation logo (Crooks et al., 2004) showing the frequency of each amino acid (height of the letter) at the C-terminus of the 49 leader peptides in Figure 4—figure supplement 2. (H) Structure of peptide aldehyde inhibitor 1 based on the ProcA2.8 leader peptide.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/42305/elife-42305-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** MALDI ToF MS analysis of a selection of ProcM-modified ProcA peptides treated with LahT150. Core peptide products (Pcns) and their ([M + H]+) masses are shown (for sequences see Figure 4—figure supplement 2): Pcn1.7 (theor 2167.1; obs 2166.8). Pcn2.1 (theor 2750.2; obs 2749.9). Pcn2.4 (theor 1808.9; obs 1809.3. Pcn2.8 (cald 2050.8; obs 2051.0). Pcn1.3 (theor 2214.0; obs 2214.5).

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/42305/elife-42305-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** (A) MALDI ToF MS analysis of the LahT150-catalyzed cleavage of MBP-tagged-AzoA2 and MBP-tagged-AzoA7. Both peptides have a C-terminal Asp-Ala-His6 added to the native core peptide sequence to improve their ionization; without these tags, the core peptides ionize poorly. Core peptide [M + H]+ masses: AzoA2 (theor 4718.5, obs 4717.7), AzoA7 (theor 4895.6, obs 4894.8). (B) Sequence alignment for LahA, ProcA, XY33a, and AzoA peptides show strong conservation in the C-terminal 12 amino acids of the leader peptide and very divergent core peptides with no detectable homology. LctA, HalA2 and SunA have low homology to all other peptides but are cleaved by LahT150.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/42305/elife-42305-fig4-figsupp3-v2.jpg)

**Figure 4—figure supplement 3.:** (A) Sequence alignment of XY33a, ProcA2.8 (11–82), (21-82 , 31-82) and the XY33a-trypsin generated truncant. (B–E) MALDI ToF MS analysis of the products of N-terminally truncated ProcA2.8 treated with LahT150. LahT150 cleaves all three truncated mutants. ProcA2.8 core peptide mass [M + H-2H2O]+: (theor 2050.8; obs 2051.1). (F) XY33a was treated with trypsin to generate the XY33a truncant shown in panel (B), then the trypsin was inactivated by boiling before treatment with LahT150. LahT150 processed the trypsin-generated XY33a truncant. Core peptide masses: ([M + H]+): XY33a-trypsin truncant (theor 3485.6; obs 3485.7); XY33a-core peptide (theor 2101.0; obs 2100.9). (G) MALDI ToF MS analysis of the synthetic peptide in Figure 4—figure supplement 3A without LahT150 (top panel) and with LahT150 (bottom panel). Synthetic peptide [M + H]+ (theor 1617.8, obs 1617.8), Cleaved synthetic peptide N-terminal fragment [M + H]+ (theor 1275.6, obs 1275.5 Da).

![Figure 4—figure supplement 4.](https://cdn.elifesciences.org/articles/42305/elife-42305-fig4-figsupp4-v2.jpg)

**Figure 4—figure supplement 4.:** LahT150 catalyzed cleavage reactions of XY33a wild-type and leader peptide mutants. XY33a-core peptide mass [M + H]+ theor 2100.0; obs 2100.9–2101.1 in all spectra.

The ProcA and LahA leader peptides are relatively close in sequence (Figure 4—figure supplement 2A) and are all members of the Nif11 family. We next tested a series of maltose binding protein-tagged peptides that are phylogenetically more distant. Remarkably, LahT150 was able to cleave the leader peptide from a group of peptides encoded in Azospirillum sp. B510 (Figure 4C and Figure 4—figure supplement 2B) even though these peptides have leader peptides of the nitrile hydratase family (for sequences see Figure 4—figure supplement 2A).

### Determination of a minimum substrate recognition motif

As shown in the sequence alignment in Figure 4—figure supplement 2A, the peptides that are successfully cleaved after the double Gly motif are quite diverse in sequence, but some conservation can be detected. To determine a minimal substrate sequence, we first deleted the N-terminal 10, 20, and 30 residues from ProcA2.8. The resulting N-terminally truncated peptides were all substrates for LahT150 (Figure 4—figure supplement 3A–E). We then treated some of the substrates with commercial proteases to further trim the leader peptide. We first used a ProcA derivative (XY33a, Figure 4—figure supplement 3A) that expresses well and that was recently investigated in a screen for peptides that could inhibit the interaction between the UEV domain of TSG101 and the HIV p6 peptide (Yang et al., 2018). We digested XY33a with trypsin resulting in a truncated leader peptide containing only its C-terminal 14 residues attached to the core peptide (for sequence see Figure 4—figure supplement 3A). This truncant was a good substrate for LahT150 (Figure 4—figure supplement 3E). Next, we purchased a synthetic substrate encoding the last 13 amino acids of the leader peptide followed by Ala-Ala-Ser-Leu. This 17-amino acid peptide was cleaved by LahT150 at the expected position, which suggested that the recognition motif resides in the 13 C-terminal amino acids of the leader peptide (Figure 4—figure supplement 3F). Given this relatively short motif, we also investigated other RiPP precursor peptides that have much shorter leader peptides than the Nif11 and nitrile hydratase-type. The precursor peptides for haloduracin β and lacticin 481, lanthipeptides that have been previously produced in E. coli (Shi et al., 2011; Oman et al., 2012), were also successfully cleaved after GA and GS sequences even though the sequence homology is relatively low (Figure 4D and E; for sequences see Figure 4—figure supplement 2A). Cleavage after the GS sequence was also observed for the glycocin precursor peptide SunA (Figure 4F) (Oman et al., 2011), demonstrating the extension of the utility of LahT150 to a different RiPP class.

Site-directed mutagenesis was used next to provide information regarding critical residues. Positions −1 and −2 (the double Gly motif) have been investigated previously for other AMS enzymes (Furgerson Ihnken et al., 2008) and we therefore focused on residues N-terminal to this motif. Position −3 is almost invariably an Ala (Figure 4G) but variants of XY33a in which this Ala was mutated to Tyr, Phe, Lys, or Glu were all cleaved by LahT150 (Figure 4—figure supplement 4). Position −4 is usually a Val, Leu or Ile. Mutagenesis to Lys or Asp resulted in mutants that were not substrates for LahT150, but the XY33a V−4T mutant was completely processed. Surprisingly, the nearly invariant Glu at position −5 was not important as mutation to Lys, Ala, and Asp was tolerated (Figure 4—figure supplement 4). The same observation was made for the Glu at position −8, since mutation to Lys, Ala, and Asp did not abrogate catalysis. In contrast, mutation of Leu−7 to Lys or Asp had a strong negative effect on catalysis indicating that this residue is important (Figure 4—figure supplement 4). Mutagenesis of Leu−12 to Ala resulted in a peptide that was partially processed by LahT150; however, changing this residue to a Lys, Asp, Phe or Trp significantly impaired cleavage activity (Figure 4—figure supplement 4).

### Protease structure and substrate recognition

We next sought to obtain a structure of the protease domain with a covalently bound substrate analog that contained the leader sequence. LahT150 is a Cys protease, and substrate analogs terminating in an aldehyde at the scissile amide have been used successfully to obtain covalently bound inhibitors (Westerik and Wolfenden, 1972; Thompson, 1973). We therefore synthesized peptide 1 representing the C-terminal 13 amino acids of the ProcA2.8 leader peptide with an aldehyde in the terminal position (Figure 4H). Crystallization efforts with the LahT150 expression construct failed, and we reasoned that the presence of flexible regions, including the His6-tag may pose a hindrance. A shorter construct, including residues 1–147 (hereafter LahT147; as identified by secondary structure analysis) and a TEV cleavable His6-tag, was used for crystallography. Incubation of peptide 1 with LahT147 prior to crystallization yielded crystals of the binary complex that diffracted to 2.0 Å resolution. Crystallographic phases were determined by the single wavelength anomalous diffraction method using data from a mercury-soaked crystal. The crystallographic asymmetric unit contains four copies of the complex allowing for multiple independent and unbiased views of the protein-peptide complex structure.

The overall structure of LahT147 recapitulates the α/β fold observed in the structures of other papain-like peptidase C39 members, wherein a central six-stranded antiparallel β-sheet is surrounded by five α-helices that pack on either side (Figure 5A). A DALI search against the Protein Data Bank shows that the closest structural homologs include the peptidase domain of the ComA transporter involved in quorum signaling (Ishii et al., 2010) (PDB Code 3K8U; Z-score = 21.1, RMSD of 1.3 Å over 129 aligned Cα atoms), and the protease domain of full-length PCAT1 Lin et al., 2015 (PDB Code 4RY2; Z-score = 18.8, RMSD of 1.8 Å over 128 aligned Cα atoms). Notably, structural similarity is also detected with the non-functional C39-like domain (CLD) from the HlyB transporter from the T1SS involved in α-hemolysin secretion (Lecher et al., 2012) (PDB Code 3ZUA; Z-score = 14.5, RMSD of 2.4 Å over 123 aligned Cα atoms).

![Figure 5.](https://cdn.elifesciences.org/articles/42305/elife-42305-fig5-v2.jpg)

**Figure 5.:** (A) Overall structure of the complex showing the orientation of the peptide aldehyde (colored in green and labeled as Inh). (B) Simulated annealing difference Fourier map (calculated without the coordinates for Cys27 and the peptide aldehyde and shown at 2.3 σ) superimposed on the coordinates of the complex. (C) Close-up view of the active site showing residues implicated in catalysis. (D) Hydropathy analysis of LahT147 (based on the Kyte and Doolittle scale [Kyte and Doolittle, 1982]) superimposed in a color scheme onto a surface rendering of the final structure. Note that Val−4, Leu−7, and Leu−12 of the leader are positioned in suitable hydrophobic pockets. The figure was generated using the Chimera software package (Pettersen et al., 2004).

The catalytic triad of LahT147 is interspersed among the secondary structural elements, with His101 and Asp117 situated on strands β4 and β5, respectively, and the nucleophilic Cys27 on helix α1, which borders one side of the central sheet assembly. Clear and continuous density corresponding to the peptide aldehyde 1 can be observed bound covalently to Cys27 as a thiohemiacetal in all four crystallographically independent molecules. The peptide binds in a groove formed between helices α1–α3 and the central antiparallel β-sheet (Figure 5A and B). The C-terminus of peptide 1, which consists of residues Gly−1 through Ala−3 that correspond to the P1 through P3 positions of the precursor substrate (per the nomenclature of Schechter and Berger [Schechter and Berger, 1967]) binds in a linear manner to the corresponding protease subsites. In contrast, residues Val−4 through Ser−11 form a short two-turn helix, which positions residues Val−4, Leu−7, and Leu−12 of the leader peptide into a hydrophobic groove in LahT150, located roughly 20 Å away from the active site.

A closer view of the active site provides insights into the roles of specific residues in catalysis (Figure 5C). Prior studies on other AMS protease domains suggested that Gln21 may stabilize the oxyanion upon formation of the tetrahedral intermediate (Ishii et al., 2010), but in the cocrystal structure, this residue is located 4.3 Å away from the thiohemiacetal oxygen atom originating from the former carbonyl group. Another residue that can function in this role is the catalytic His101, which is positioned in line with the carbonyl oxygen at a distance of 2.7 Å. Studies of other proteolytic enzymes, such as the PCY1 macrocyclase involved in orbitide biosynthesis, are also consistent with multiple functional roles for the catalytic His (Chekan et al., 2017).

Mapping the amino acid hydropathy onto a surface rendering of LahT147 (using the Kyte and Doolittle scale [Kyte and Doolittle, 1982] as implemented in the Chimera software package [Pettersen et al., 2004]) reveals that the surface of the protease largely consists of polar residues with the exception of the aforementioned hydrophobic groove that engages the two-turn helix of the substrate (Figure 5D). There is also an increase in hydrophobicity in the region flanking the active site, which is accompanied by a narrowing of the binding pocket. The hydrophobic packing interactions between LahT147 and peptide inhibitor 1 provide a rationale for our mutational data, wherein LahT147 could not process variants of the full-length precursor peptide that contained replacements of either Val−4 or Leu−7 with an acidic or basic residue nor most mutations of Leu−12 (Figure 4—figure supplement 4).

### Implications for proteolysis and transport

The structural and biochemical studies of an excised, active C39 protease afford the opportunity to understand prior data on substrate selectivity of AMS/PCAT transporters (Michiels et al., 2001). Our co-crystal structure illustrates that substrate recognition occurs roughly 20 Å away from the double Gly motif, and residues in this region form an α-helix that positions residues Val−4, Leu−7, and Leu−12 of the substrate peptide into a hydrophobic groove in the protease domain. Such ‘knobs-into-holes’ type packing is conceptually analogous to leader peptide recognition in RiPP biosynthetic enzymes (Ortega et al., 2015; Koehnke et al., 2015; Grove et al., 2017; Evans et al., 2017) wherein hydrophobic residues in the precursor peptide, distal from the core peptide are positioned into suitably arranged nonpolar pockets.

A plausible model for substrate translocation in the context of a full-length AMS/PCAT can be envisioned by superimposing the cocrystal structure of the LahT protease domain onto the structure of full-length PCAT1 in the absence of nucleotides (Lin et al., 2015). Despite overall low (~25%) sequence identity between the respective protease domains, the structures align with a RMSD of 1.6 Å over 128 Cα atoms. In the model, the helical region of the substrate peptide is oriented in a small groove located between the protease domain and the nucleotide-binding domain, providing an effective means to lock these domains together. The substrate peptide cargo would be directed out from the active site of the protease domain and positioned directly into the TMD to facilitate export. This pocket is increasingly narrow near the site of proteolysis, explaining the identity of small residues at the double Gly cleavage site (Figure 6A). There is also an increase in the hydrophobicity of the pocket near this site, which may serve to further direct the substrate into the TMD. The leader peptide may provide a backstop that prevents the cleaved cargo from leaking back into the cytoplasm, and ensuring the extracellular directionality of transport upon binding of ATP to the NBDs. The conformational changes observed in the structure of PCAT1 upon nucleotide binding both ensure shuttling of the cleaved cargo to the extracellular region, and result in disengagement of the protease domain for subsequent rounds of coupled export (Lin et al., 2015).

![Figure 6.](https://cdn.elifesciences.org/articles/42305/elife-42305-fig6-v2.jpg)

**Figure 6.:** (A) Close-up view of the LahT147-inhibitor complex structure superimposed on the crystal structure of full-length PCAT1. Note that the leader sequence directs the core peptide ‘cargo’ into the transmembrane domain (TMD) and is flanked by the nucleotide-binding domain (NBD). (B) Overall structure of the PCAT1 dimer with one monomer colored grey and the other monomer blue and pink showing the relative orientations of the protease domain and the inhibitor. Binding of the peptide cargo is poised to stabilize the interdomain interactions in the full-length transporter.

The structural and biochemical data presented here also inform on the cryptic non-catalytic C39-like domains (CLDs) associated with type I secretion systems in Gram-negative bacteria. Analysis of transport of hemolysin A (HlyA) mediated by the ABC transporter HlyB demonstrates that the CLD is essential for secretion, despite lacking proteolytic activity (Lecher et al., 2012). Pull-down assays demonstrate that the CLD interacts only with the unfolded HlyA substrate, leading to the suggestion that the CLD may play a chaperone-like role. Our studies suggest that the CLD may also play a role in stabilizing the nucleotide-free state of HlyB by binding the substrate peptide, which may optimally position the peptide cargo for export upon ATP binding.

### Utility of the LahT150 protease domain

Because of the direct link between the genome-encoded precursor peptide and the final natural product, RiPPs are attractive for genome mining (Velásquez and van der Donk, 2011; Hetrick and van der Donk, 2017) and synthetic biology (Yang et al., 2018; Sardar et al., 2015; Burkhart et al., 2017; van Heel et al., 2013; Montalbán-López et al., 2017; Urban et al., 2017; Hetrick et al., 2018), and numerous studies have described the successful reconstitution of RiPP machinery in heterologous hosts, including E. coli. In many such genome mining exercises, the leader peptide is not removed inside the heterologous host to prevent potential toxicity of the final compound (Valsesia et al., 2007). An additional advantage of retaining the leader peptide during heterologous production is that it enables attachment of an affinity tag that allows one-step purification, which avoids tedious purification of compounds that may be produced in small quantities (Shi et al., 2011; Nagao et al., 2005). However, developing general methods for leader peptide removal has been challenging (Li et al., 2010; Shi et al., 2011; Goto et al., 2010; Plat et al., 2011; Lohans et al., 2014; Ökesli et al., 2011), especially for the double Gly leader peptides. This study shows that LahT150 is a highly versatile and useful protease for RiPP research as it removes the leader peptide from a remarkably diverse set of peptides including leader peptides of the Nif11 and nitrile hydratase families.

## Materials and methods

For all materials used or generated in this study, see the Key Resources Table.

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
      <td>Gene (XY33a_V-4K_gene)</td>
      <td>XY33a_V-4K_gene</td>
      <td>IDT. Representative of other purchased XY33a mutant genes (see Table 5)</td>
      <td>XY33a_V-4K_gene</td>
      <td>5 ng/μL stock solution (1 μL) used as amplification template</td>
    </tr>
    <tr>
      <td>Strain, strain background (Escherichia coli BL21 (DE3)-T1R)</td>
      <td>E. coli BL21 (DE3)-T1R</td>
      <td>Sigma Aldrich B2935</td>
      <td>BL21 (DE3)-T1R</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (Lachnospiraceae C6A11)</td>
      <td>Lachnospiraceae C6A11</td>
      <td>Dr. William Kelly (AgResearch, New Zealand)</td>
      <td>Lachnospiraceae C6A11</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (Escherichia coli Rosetta 2 (DE3))</td>
      <td>E. coli Rosetta 2 (DE3)</td>
      <td>Novagen Catalog no. 71400–3</td>
      <td>E. coli Rosetta 2 (DE3)</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (Azospirillum sp. B510 (JCM 14679))</td>
      <td>Azospirillum sp. B510 (JCM 14679)</td>
      <td>JCM Riken http://www.jcm.riken.jp/cgi-bin/jcm/jcm_number?JCM=14679</td>
      <td>Azospirillum sp. B510 (JCM 14679)</td>
      <td></td>
    </tr>
    <tr>
      <td>Transformed construct (pETDuet LahT150)</td>
      <td>pETDuet-LahT150</td>
      <td>this work</td>
      <td>pETDuet LahT150</td>
      <td>50 ng/μL stock solution (1 μL) used in E. coli BL21 transformation</td>
    </tr>
    <tr>
      <td>Transformed construct (pRSFDuet XY33a)</td>
      <td>pRSFDuet-XY33a</td>
      <td>PMID: 22574919</td>
      <td>pRSFDuet XY33a</td>
      <td>50 ng/μL stock solution (1 μL) used in E. coli BL21 transformation</td>
    </tr>
    <tr>
      <td>Transformed construct (pRSFDuet XY33a A-3Y)</td>
      <td>pRSFDuet XY33a A-3Y</td>
      <td>this work. Representative XY33a mutant</td>
      <td>pRSFDuet XY33a A-3Y</td>
      <td>50 ng/μL stock solution (1 μL) used in E. coli BL21 transformation</td>
    </tr>
    <tr>
      <td>Transformed construct (pRSFDuet LahA1)</td>
      <td>pRSFDuet-LahA1</td>
      <td>this work</td>
      <td>pRSFDuet LahA1</td>
      <td>50 ng/μL stock solution (1 μL) used in E. coli BL21 transformation</td>
    </tr>
    <tr>
      <td>Transformed construct (pRSFDuet LahA2)</td>
      <td>pRSFDuet-LahA2</td>
      <td>this work</td>
      <td>pRSFDuet LahA2</td>
      <td>50 ng/μL stock solution (1 μL) used in E. coli BL21 transformation</td>
    </tr>
    <tr>
      <td>Transformed construct (pRSFDuet LahA3)</td>
      <td>pRSFDuet-LahA3</td>
      <td>this work</td>
      <td>pRSFDuet LahA3</td>
      <td>50 ng/μL stock solution (1 μL) used in E. coli BL21 transformation</td>
    </tr>
    <tr>
      <td>Transformed construct (pRSFDuet LahA4)</td>
      <td>pRSFDuet-LahA4</td>
      <td>this work</td>
      <td>pRSFDuet LahA4</td>
      <td>50 ng/μL stock solution (1 μL) used in E. coli BL21 transformation</td>
    </tr>
    <tr>
      <td>Transformed construct (pRSFDuet LahA5)</td>
      <td>pRSFDuet-LahA5</td>
      <td>this work</td>
      <td>pRSFDuet LahA5</td>
      <td>50 ng/μL stock solution (1 μL) used in E. coli BL21 transformation</td>
    </tr>
    <tr>
      <td>Transformed construct (pRSFDuet LahA6)</td>
      <td>pRSFDuet-LahA6</td>
      <td>this work</td>
      <td>pRSFDuet LahA6</td>
      <td>50 ng/μL stock solution (1 μL) used in E. coli BL21 transformation</td>
    </tr>
    <tr>
      <td>Transformed construct (pRSFDuet LahA7)</td>
      <td>pRSFDuet-LahA7</td>
      <td>this work</td>
      <td>pRSFDuet LahA7</td>
      <td>50 ng/μL stock solution (1 μL) used in E. coli BL21 transformation</td>
    </tr>
    <tr>
      <td>Transformed construct (pET28-MBP-AzoA2)</td>
      <td>pET28-MBP-AzoA2</td>
      <td>this work</td>
      <td>pET28-MBP-AzoA2</td>
      <td>150 ng/μL stock solution (1 μL) used in E. coli Rosetta 2 (DE3) transformation</td>
    </tr>
    <tr>
      <td>Transformed construct (pET28-MBP-AzoA3)</td>
      <td>pET28-MBP-AzoA3</td>
      <td>this work</td>
      <td>pET28-MBP-AzoA3</td>
      <td>150 ng/μL stock solution (1 μL) used in E. coli Rosetta 2 (DE3) transformation</td>
    </tr>
    <tr>
      <td>Transformed construct (pET28-MBP-AzoA6)</td>
      <td>pET28-MBP-AzoA6</td>
      <td>this work</td>
      <td>pET28-MBP-AzoA6</td>
      <td>150 ng/μL stock solution (1 μL) used in E. coli Rosetta 2 (DE3) transformation</td>
    </tr>
    <tr>
      <td>Transformed construct (pET28-MBP-AzoA7)</td>
      <td>pET28-MBP-AzoA7</td>
      <td>this work</td>
      <td>pET28-MBP-AzoA7</td>
      <td>150 ng/μL stock solution (1 μL) used in E. coli Rosetta 2 (DE3) transformation</td>
    </tr>
    <tr>
      <td>Transformed construct (pRSFDuet ProcA 2.8 (MCSI) - ProcM (MCSII))</td>
      <td>pRSFDuet ProcA2.8 (MCSI) - ProcM (MCSII)</td>
      <td>PMID: 22574919</td>
      <td>pRSFDuet ProcA 2.8 (MCSI) - ProcM (MCSII)</td>
      <td>50 ng/μL stock solution (1 μL) used in E. coli BL21 transformation</td>
    </tr>
    <tr>
      <td>Transformed construct (pRSFDuet ProcA 1.7 (MCSI) - ProcM (MCSII))</td>
      <td>pRSFDuet ProcA1.7 (MCSI) - ProcM (MCSII</td>
      <td>PMID: 22574919</td>
      <td>pRSFDuet ProcA 1.7 (MCSI) - ProcM (MCSII</td>
      <td>50 ng/μL stock solution (1 μL) used in E. coli BL21 transformation</td>
    </tr>
    <tr>
      <td>Transformed construct (pRSFDuet ProcA 2.1 (MCSI) - ProcM (MCSII))</td>
      <td>pRSFDuet ProcA2.1 (MCSI) - ProcM (MCSII</td>
      <td>this work</td>
      <td>pRSFDuet ProcA 2.1 (MCSI) - ProcM (MCSII</td>
      <td>50 ng/ μL stock solution (1 μL) used in E. coli BL21 transformation</td>
    </tr>
    <tr>
      <td>Transformed construct (pRSFDuet ProcA 2.4 (MCSI) - ProcM (MCSII))</td>
      <td>pRSFDuet ProcA2.4 (MCSI) - ProcM (MCSII)</td>
      <td>this work</td>
      <td>pRSFDuet ProcA 2.4 (MCSI) - ProcM (MCSII)</td>
      <td>50 ng/ μL stock solution (1 μL) used in E. coli BL21 transformation</td>
    </tr>
    <tr>
      <td>Transformed construct (pRSFDuet ProcA 1.3 (MCSI) - ProcM (MCSII))</td>
      <td>pRSFDuet ProcA1.3 (MCSI) - ProcM (MCSII)</td>
      <td>this work</td>
      <td>pRSFDuet ProcA 1.3 (MCSI) - ProcM (MCSII)</td>
      <td>50 ng/ μL stock solution (1 μL) used in E. coli BL21 transformation</td>
    </tr>
    <tr>
      <td>Sequence- based reagent</td>
      <td>Benzonase Endonuclease</td>
      <td>EMD Millipore Catalog no. 1.01656.001</td>
      <td>Benzonase</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence- based reagent</td>
      <td>EcoRI-HF</td>
      <td>New England Biolabs R3101S</td>
      <td>EcoRI</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence- based reagent</td>
      <td>BamHI-HF</td>
      <td>New England Biolabs R3136S</td>
      <td>BamHI</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence- based reagent</td>
      <td>NotI-HF</td>
      <td>New England Biolabs R3189S</td>
      <td>Not1</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence- based reagent</td>
      <td>HindIII-HF</td>
      <td>New England Biolabs R3104S</td>
      <td>HindIII</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant protein</td>
      <td>XY33a</td>
      <td>PMID: 29507389</td>
      <td>XY33a</td>
      <td>recombinant substrate peptide tested with LahT150</td>
    </tr>
    <tr>
      <td>Recombinant protein</td>
      <td>XY33a A-3Y</td>
      <td>this work; representative XY33a mutant</td>
      <td>XY33a A-3Y</td>
      <td>recombinant substrate peptide mutant tested with LahT150</td>
    </tr>
    <tr>
      <td>Recombinant protein</td>
      <td>LahA1</td>
      <td>this work</td>
      <td>LahA1</td>
      <td>recombinant substrate peptide tested with LahT150</td>
    </tr>
    <tr>
      <td>Recombinant protein</td>
      <td>LahA2</td>
      <td>this work</td>
      <td>LahA2</td>
      <td>recombinant substrate peptide tested with LahT150</td>
    </tr>
    <tr>
      <td>Recombinant protein</td>
      <td>LahA3</td>
      <td>this work</td>
      <td>LahA3</td>
      <td>recombinant substrate peptide tested with LahT150</td>
    </tr>
    <tr>
      <td>Recombinant protein</td>
      <td>LahA4</td>
      <td>this work</td>
      <td>LahA4</td>
      <td>recombinant substrate peptide tested with LahT150</td>
    </tr>
    <tr>
      <td>Recombinant protein</td>
      <td>LahA5</td>
      <td>this work</td>
      <td>LahA5</td>
      <td>recombinant substrate peptide tested with LahT150</td>
    </tr>
    <tr>
      <td>Recombinant protein</td>
      <td>LahA6</td>
      <td>this work</td>
      <td>LahA6</td>
      <td>recombinant substrate peptide tested with LahT150</td>
    </tr>
    <tr>
      <td>Recombinant protein</td>
      <td>LahA7</td>
      <td>this work</td>
      <td>LahA7</td>
      <td>recombinant substrate peptide tested with LahT150</td>
    </tr>
    <tr>
      <td>Recombinant protein</td>
      <td>AzoA2</td>
      <td>this work</td>
      <td>MBP-AzoA2</td>
      <td>recombinant substrate peptide tested with LahT150</td>
    </tr>
    <tr>
      <td>Recombinant protein</td>
      <td>AzoA3</td>
      <td>this work</td>
      <td>MBP-AzoA3</td>
      <td>recombinant substrate peptide tested with LahT150</td>
    </tr>
    <tr>
      <td>Recombinant protein</td>
      <td>AzoA6</td>
      <td>this work</td>
      <td>MBP-AzoA6</td>
      <td>recombinant substrate peptide tested with LahT150</td>
    </tr>
    <tr>
      <td>Recombinant protein</td>
      <td>AzoA7</td>
      <td>this work</td>
      <td>MBP-AzoA7</td>
      <td>recombinant substrate peptide tested with LahT150</td>
    </tr>
    <tr>
      <td>Recombinant protein</td>
      <td>LahT150</td>
      <td>this work</td>
      <td>LahT150</td>
      <td>protease domain of LahT</td>
    </tr>
    <tr>
      <td>Recombinant protein</td>
      <td>Pcn 2.8</td>
      <td>PMID: 22574919</td>
      <td>Pcn 2.8</td>
      <td>recombinant posttranslationally modified ProcA2.8 substrate peptide tested with LahT150</td>
    </tr>
    <tr>
      <td>Recombinant protein</td>
      <td>Pcn 1.7</td>
      <td>PMID: 22574919</td>
      <td>Pcn 1.7</td>
      <td>recombinant posttranslationally modified ProcA1.7 substrate peptide tested with LahT150</td>
    </tr>
    <tr>
      <td>Recombinant protein</td>
      <td>Pcn 2.1</td>
      <td>this work</td>
      <td>Pcn 2.1</td>
      <td>recombinant posttranslationally modified ProcA2.1 substrate peptide tested with LahT150</td>
    </tr>
    <tr>
      <td>Recombinant protein</td>
      <td>Pcn 2.4</td>
      <td>this work</td>
      <td>Pcn 2.4</td>
      <td>recombinant posttranslationally modified ProcA2.4 substrate peptide tested with LahT150</td>
    </tr>
    <tr>
      <td>Recombinant protein</td>
      <td>Pcn 1.3</td>
      <td>this work</td>
      <td>Pcn 1.3</td>
      <td>recombinant posttranslationally modified ProcA1.3 substrate peptide tested with LahT150</td>
    </tr>
    <tr>
      <td>Minimum peptide substrate</td>
      <td>Synthetic peptide</td>
      <td>Genscript</td>
      <td>Synthetic peptide</td>
      <td>synthetic minimal substrate peptide tested with LahT150</td>
    </tr>
    <tr>
      <td>Commercial kit</td>
      <td>QIAprep Spin Miniprep kit</td>
      <td>Qiagen catalog no. 27106</td>
      <td>QIAprep Spin Miniprep kit</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial kit</td>
      <td>QIAquick Gel Extraction kit</td>
      <td>Qiagen catalog no. 28115</td>
      <td>QIAquick Gel Extraction kit</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial kit</td>
      <td>Gibson Assembly</td>
      <td>New England Biolabs E2611S</td>
      <td>Gibson Assembly</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>TCEP (Tris (2-Carboxyethyl) phosphine hydrochloride)</td>
      <td>Goldbio Catalog ID TCEP</td>
      <td>TCEP</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Terrific Broth granulated</td>
      <td>Fisher Scientific BP97285</td>
      <td>TB</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Glycerol</td>
      <td>Fisher Scientific BP-229–4</td>
      <td>Glycerol</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Dextrose</td>
      <td>Fisher Scientific BP350500</td>
      <td>Glucose or dextrose</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>kanamycin monosulfate, USP grade</td>
      <td>Goldbio Catalog ID K-120</td>
      <td>kanamycin</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Adobe Illustrator CS6</td>
      <td>Adobe</td>
      <td>Adobe Illustrator</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>FlexAnalysis 3.4 (Bruker Daltonik GmbH)</td>
      <td>Bruker Daltonik GmbH</td>
      <td>FlexAnalysis 3.4 (Bruker Daltonik GmbH)</td>
      <td>Mass spectrometry data processing</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Clontech His60 Ni Superflow resin</td>
      <td>Clontech Catalog no. 636660</td>
      <td>Clontech His60 Ni Superflow resin</td>
      <td>Used for gravity purification of all recombinant proteins except LahT150</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>GE Healthcare HisTrap HP</td>
      <td>GE Healthcare 17524701</td>
      <td>5 mL HiTrap Ni Chelating column</td>
      <td>Used for FPLC purification of recombinant LahT150</td>
    </tr>
  </tbody>
</table>

E. coli BL21 (DE3)-T1R transformants containing pETDuet encoding N-terminally His-tagged LahT150 in MCSI were grown overnight at 37°C in Terrific Broth (TB) containing 2% glucose and 100 μg/mL ampicillin and used to inoculate production cultures. Cultures were grown aerobically at 37°C until OD600 reached 0.8, then cooled on ice for 20 min before induction with 0.2 mM IPTG. The cells were then incubated at 18°C for 16–20 hr. Cells were harvested by centrifugation at 5,000 × g at 4°C, then resuspended in LahT150 Lysis Buffer (20 mM Tris, 1 M NaCl, pH 7.8) and stored at −80°C until purification. To the thawed cells, 40 mg lysozyme and 10 μL benzonase (≥250 units/μL, EMD Millipore) per 12 g cell paste (approximate cell mass obtained from 1 L of culture) were added and the cells were incubated for 90 min in a beaker on ice. The cells were then sonicated at 60% amplitude for 6 min using 2 s pulse on and 8 s pulse off using a Sonics and Materials Inc. Vibra Cell VCX 500 or VCX 700 or passed through an Avestin C3 Cell Homogenizer. The lysed cells were then centrifuged at 24,000 × g for 30 min at 4°C. The supernatants were transferred to new tubes and again centrifuged. The supernatant was applied to a 5 mL HiTrap Ni chelating column pre-equilibrated with 10 column volumes (CV) of LahT150 Lysis Buffer using a peristaltic pump using ~2 mL/min flow rate. The HiTrap column was washed with five more CV of Lysis Buffer before transferring to an ÄKTA fast protein liquid chromatography (FPLC) system (GE Healthcare) using solvent A (LahT150 Lysis Buffer) as stationary phase and solvent B (LahT150 Elution Buffer, 20 mM Tris, 1 M NaCl, 500 mM imidazole, pH 7.8 at 25°C) as mobile phase. The gradient increased linearly from 0% Solvent B to 20% Solvent B in Solvent A at a flow rate of 2.0 mL/min over 10 CV, followed by a linear increase from 20% to 100% Solvent B over 4 CV during which the protein eluted, and a final wash step at 100% Solvent B for 8 CV. The fractions with 280 nm absorbance were analyzed by SDS-PAGE, fractions containing the desired protein were concentrated to ~3 mL, and then applied to a HiLoad 16/60 gel filtration column containing Superdex200 resin (GE Healthcare). The column was eluted with 120 mL (2 CV) LahT150 storage buffer (10% glycerol, 20 mM Tris, 1 M NaCl, pH 7.8) and the fractions containing protein were concentrated to 4–6 mg/mL and aliquoted. Final yields varied between 40 and 50 mg/L of culture.

### In vitro protease assays

LahT150 cleavage assays contained 100 μM substrate and 10 μM LahT150 in 50 mM Tris pH 8.0. The cleavage assays produced identical results with and without the presence of 5 mM (tris(2-carboxyethyl)phosphine) (TCEP) and with as low as 1 μM LahT150. For mass spectrometry details, see Table 1.

**Table 1.**
 Calculated and observed MALDI ToF [M + H]+ masses for the leader peptides in Figure 4—figure supplement 4. n.d., not detected.


<table>
  <thead>
    <tr>
      <th>[M + H]+</th>
      <th>WT</th>
      <th>V-4K</th>
      <th>V-4T</th>
      <th>V-4D</th>
      <th>E-6A</th>
      <th>E-6K</th>
      <th>E-6D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Calcd</td>
      <td>8169.8</td>
      <td>8227.0</td>
      <td>8199.8</td>
      <td>8229.8</td>
      <td>8139.8</td>
      <td>8168.9</td>
      <td>8183.8</td>
    </tr>
    <tr>
      <td>Obsd</td>
      <td>8169.3</td>
      <td>8229.9</td>
      <td>8201.4</td>
      <td>n.d.</td>
      <td>8137.8</td>
      <td>8170.0</td>
      <td>8183.1</td>
    </tr>
    <tr>
      <td></td>
      <td>L-7A</td>
      <td>L-7K</td>
      <td>L-7D</td>
      <td>E-8A</td>
      <td>E-8K</td>
      <td>E-8D</td>
      <td></td>
    </tr>
    <tr>
      <td>Calcd</td>
      <td>8127.7</td>
      <td>8212.9</td>
      <td>8199.8</td>
      <td>8111.8</td>
      <td>8168.9</td>
      <td>8155.8</td>
      <td></td>
    </tr>
    <tr>
      <td>Obsd</td>
      <td>8126.2</td>
      <td>n.d.</td>
      <td>n.d.</td>
      <td>8111.0</td>
      <td>8167.7</td>
      <td>8157.5</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>D-9A</td>
      <td>D-10A</td>
      <td>D-9E,D-10E</td>
      <td>A-3Y</td>
      <td>A-3F</td>
      <td>A-3K</td>
      <td>A-3E</td>
    </tr>
    <tr>
      <td>Calcd</td>
      <td>8125.8</td>
      <td>8125.8</td>
      <td>8197.9</td>
      <td>8261.9</td>
      <td>8245.9</td>
      <td>8226.9</td>
      <td>8227.9</td>
    </tr>
    <tr>
      <td>Obsd</td>
      <td>8125.4</td>
      <td>8127.0</td>
      <td>8196.7</td>
      <td>8261.1</td>
      <td>8246.5</td>
      <td>8225.8</td>
      <td>8226.8</td>
    </tr>
    <tr>
      <td></td>
      <td>L-12A</td>
      <td>L-12K</td>
      <td>L-12D</td>
      <td>L-12F</td>
      <td>L-12W</td>
      <td>L-12Y</td>
      <td></td>
    </tr>
    <tr>
      <td>Calcd</td>
      <td>8127.7</td>
      <td>8184.8</td>
      <td>8171.7</td>
      <td>8203.8</td>
      <td>8242.8</td>
      <td>8184.8</td>
      <td></td>
    </tr>
    <tr>
      <td>Obsd</td>
      <td>8126.0</td>
      <td>n.d.</td>
      <td>n.d.</td>
      <td>n.d.</td>
      <td>8241.0</td>
      <td>n.d</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Bioinformatics

The top 5000 homologous sequences were retrieved using a BLASTp search against non-redundant protein sequences database using full length LahT sequence as query. The LahT sequences were imported into EFI-Enzyme Similarity Tool webserver using option C with FASTA header reading to construct the SSN (Gerlt et al., 2015). The 90% representative node network was opened and analyzed by Cytoscape, and 45% sequence identity was applied to separate the clusters. Nodes are shown in different colors based on the phylum classification, and several characterized LahT homologs are marked with red circles and their names shown on the side.

### Crystallization and structure determination

Repeated attempts to produce crystals of LahT150 failed, presumably due to the presence of the His6 tag, as well as other potentially flexible regions. Multiple sequence alignments and secondary structure prediction analysis suggest that the last three C-terminal residues in the LahT150 construct were flexible. A new construct, encompassing residues 1–147 of LahT, was generated using the PCR and cloned into pET His6 TEV LIC cloning vector using HiFi DNA Assembly Master Mix for protein overexpression. The resultant plasmid (verified by sequencing) was used to transform chemically competent E. coli BL21 Rosetta 2 cells for overproduction. Starter cultures (each with 6 mL LB) were grown overnight and used to inoculate 2 L LB containing ampicillin (100 µg/mL) and chloramphenicol (25 µg/mL).

Cultures were grown at 37°C with vigorous shaking until the OD600 reached ~0.6 before cooling down in ice water for 15 min. Protein expression was induced by the addition of 0.5 mM IPTG and cultures were shaken for an additional 18 hr at 18°C and 200 rpm. Cell pellets were harvested by centrifugation at 4°C, resuspended with 40 mL suspension buffer (500 mM NaCl, 10% glycerol, 20 mM Tris, pH 8.0). Harvested cells were lysed by sonication, and the lysates were clarified by centrifugation at 4°C. The clear supernatant was loaded onto a 5 mL immobilized metal ion affinity resin column (Hi-Trap Ni-NTA, G.E. Healthcare) pre-equilibrated with binding buffer (1 M NaCl, 5% glycerol, 20 mM Tris, pH 8.0). The column was washed with 50 mL of 12% elution buffer (1 M NaCl, 250 mM imidazole, 20 mM Tris, pH 8.0), and then eluted by a linear gradient to 100% elution buffer. Fractions containing pure protein (as determined by SDS-PAGE) were combined and dialyzed against dialysis buffer (300 mM NaCl, 10% glycerol, 20 mM Tris-HCl, pH 7.5) overnight at 4°C. Purified proteins were concentrated, and the final concentration was quantified by Bradford analysis (Thermo Scientific), concentrated to ~10 mg/ml, and flash frozen in liquid nitrogen.

Prior to crystallization, flash-frozen aliquots of recombinant, purified LahT150 were thawed and purified by size-exclusion chromatography (Superdex Hiload 75 16/60, GE Healthcare) using an isocratic gradient buffer composed of 100 mM KCl, 20 mM HEPES, pH 7.5 and concentrated. The purified protein (8 mg/mL) was incubated with 1 mM of peptide aldehyde inhibitor for 2 hr before mixing with precipitant solution in a 1:1 ratio (v/v). The precipitant solution consisted of 0.02 M D-glucose, 0.02 M D-mannose, 0.02 M D-galactose, 0.02 M L-fucose, 0.02 M D-xylose, 0.02 M N-acetyl-D-glucosamine, 0.05 M Tris and BICINE pH 8.5, 20% v/v polyethylene glycol 500 monomethyl ether, 10% w/v polyethylene glycol 20000, and 8% v/v formamide. Crystals of the protease-inhibitor appeared after 2 days incubation at 9°C, reached their largest size at 3–7 days, and were subsequently flash frozen by direct immersion into liquid nitrogen. All diffraction data were collected at LS-CAT (Sector 21, Advanced Photon Source, Argonne National Labs, IL) using MX-300 or Eiger 9M detectors. All data were integrated and scaled using either HKL2000 (Minor et al., 2006) or XDS (Kabsch, 2014).

Crystallographic phases were determined by the single wavelength anomalous diffraction method via AutoSol (Terwilliger et al., 2009) from data collected on a crystal soaked in precipitant solution with additional 2 mM 4-chloromercuribenzenesulfonate (PCMBS) for 2 hr. Phases for the native data set was determined using molecular replacement (McCoy, 2007). For each structure, iterative model building was carried out using the PHENIX suite of programs (Afonine et al., 2012) and further improved by manual rebuilding using COOT (Emsley and Cowtan, 2004). Cross-validation, using 5% of the data for the calculation of the free R factor (Brunger, 2007) was utilized throughout the model building process in order to monitor building bias. The stereochemistry of all of the models was routinely monitored throughout the course of refinement using PROCHECK (Laskowski et al., 1996). Relevant data collection and refinement parameters are provided in Table 2. The coordinates for the LahT147-peptide structure can be accessed under PDB code 6MPZ.

**Table 2.**
 Data collection, phasing and refinement statistics.


<table>
  <thead>
    <tr>
      <th></th>
      <th>LahT-inhibitor 1 complex</th>
      <th colspan="2">PCMBS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Data collection</td>
      <td></td>
      <td colspan="2"></td>
    </tr>
    <tr>
      <td>Space group</td>
      <td>C2</td>
      <td colspan="2">C2</td>
    </tr>
    <tr>
      <td>Unit cell (a,b,c,β)</td>
      <td>37.9, 119.4, 76.5, 93.8</td>
      <td colspan="2">37.3, 119.8, 83.5, 112.8</td>
    </tr>
    <tr>
      <td>Resolution</td>
      <td>76.4–1.98 (1.985–1.98)</td>
      <td colspan="2">59.9–2.04 (2.05–2.04)</td>
    </tr>
    <tr>
      <td>Total reflections</td>
      <td>239,058</td>
      <td colspan="2">124,854</td>
    </tr>
    <tr>
      <td>Unique reflections</td>
      <td>47,187</td>
      <td colspan="2">21,494</td>
    </tr>
    <tr>
      <td>Rsym (%)*</td>
      <td>0.102 (0.727)</td>
      <td colspan="2">0.090 (0.690)</td>
    </tr>
    <tr>
      <td>I/σ(I)*</td>
      <td>9.3 (2.1)</td>
      <td colspan="2">12.9 (2.5)</td>
    </tr>
    <tr>
      <td>Completeness (%)*</td>
      <td>99.8 (99.8)</td>
      <td colspan="2">99.9 (100)</td>
    </tr>
    <tr>
      <td>Redundancy</td>
      <td>5.1 (5.1)</td>
      <td colspan="2">5.9 (6.0)</td>
    </tr>
    <tr>
      <td>Refinement</td>
      <td></td>
      <td colspan="2"></td>
    </tr>
    <tr>
      <td>Resolution (Å)</td>
      <td>50.0–2.0</td>
      <td colspan="2"></td>
    </tr>
    <tr>
      <td>No. reflections</td>
      <td>43,389</td>
      <td colspan="2"></td>
    </tr>
    <tr>
      <td>Rwork / Rfree†</td>
      <td>23.4/26.8</td>
      <td colspan="2"></td>
    </tr>
    <tr>
      <td>Number of atoms</td>
      <td></td>
      <td colspan="2"></td>
    </tr>
    <tr>
      <td>Protein</td>
      <td>4479</td>
      <td colspan="2"></td>
    </tr>
    <tr>
      <td>Inh</td>
      <td>352</td>
      <td colspan="2"></td>
    </tr>
    <tr>
      <td>Water</td>
      <td>123</td>
      <td colspan="2"></td>
    </tr>
    <tr>
      <td>B-factors</td>
      <td></td>
      <td colspan="2"></td>
    </tr>
    <tr>
      <td>Protein</td>
      <td>37.6</td>
      <td colspan="2"></td>
    </tr>
    <tr>
      <td>Inh</td>
      <td>34.5</td>
      <td colspan="2"></td>
    </tr>
    <tr>
      <td>Water</td>
      <td>35.9</td>
      <td colspan="2"></td>
    </tr>
    <tr>
      <td>R.m.s deviations</td>
      <td></td>
      <td colspan="2"></td>
    </tr>
    <tr>
      <td>Bond lengths (Å)</td>
      <td>0.015</td>
      <td colspan="2"></td>
    </tr>
    <tr>
      <td>Bond angles (°)</td>
      <td>1.81</td>
      <td colspan="2"></td>
    </tr>
  </tbody>
</table>

_*Highest resolution shell is shown in parenthesis.†R-factor = Σ(|Fobs|-k|Fcalc|)/Σ |Fobs|and R-free is the R value for a test set of reflections consisting of a random 5% of the diffraction data not used in refinement._

### Cloning of LahT150

The N-terminal 450 nucleotides of the lahT gene harboring flanking sequences homologous to pETDuet-1 multiple cloning site I (MCSI) were amplified from genomic DNA of Lachnospiraceae C6A11 as template and the primers LahT150_fp (5’- accatcatcaccacagccaggatccgaGTAAAAAGC AGATACAGCCTGTCACAAGAG-3’) and LahT150_rp (5’- tctgttcgacttaagcattatgcggccgcTTA CTGTTCAAATCTATCAGTAGGCTTG-3’). The pETDuet homology is displayed in lowercase letters. The PCR product was cloned into EcoRI/HindIII-linearized pETDuet by Gibson assembly (50°C, 1 hr) using a molar ratio of 10:1 (insert: backbone) (Gibson et al., 2009). The final construct was confirmed by DNA sequencing.

### Cloning of LahA substrates

The lahA genes were amplified using genomic DNA from Lachnospiraceae bacterium C6A11 as template and LahAx_fp and LahAx_rp as primers (Table 3) by touchdown PCR (Korbie and Mattick, 2008) with the annealing temperature decreasing from 70°C to 54°C over 80 cycles (−0.2°C/cycle). An example PCR amplification cycle consisted of denaturing (98°C for 10 s), annealing (from 70°C to 55°C, 0.2°C lower every cycle for a total of 80 cycles) for 30 s and extension (72°C for 30 s). Subsequently the PCR fragment was cloned by using Gibson assembly into the multiple cloning site 1 (MCSI) of the pRSFDuet-1 vector previously linearized by HindIII and EcoRI digestion.

**Table 3.**
 Primers used in the generation of LahA constructs.Homology with vector backbone is displayed as lowercase letters.


<table>
  <thead>
    <tr>
      <th>Primer Name</th>
      <th>Sequence 5’−3’</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>LahA1_fp</td>
      <td>accatcatcaccacagccaggatccgaattcgaACGAGAATTTAGAGAAGTTTTTTCAGA</td>
    </tr>
    <tr>
      <td>LahA1_rp</td>
      <td>ttctgttcgacttaagcattatgcggccgcAGATTGCTCCTGCAGCGAAATTGGTAAG</td>
    </tr>
    <tr>
      <td>LahA2_fp</td>
      <td>accatcatcaccacagccaggatccgaattcgaACGAGAATTTAAAGATGTTTTTGCAGA</td>
    </tr>
    <tr>
      <td>LahA2_rp</td>
      <td>ttctgttcgacttaagcattatgcggccgcTTAGATTGCTGTTGCAGCGAAAAGGGAAT</td>
    </tr>
    <tr>
      <td>LahA3_fp</td>
      <td>accatcatcaccacagccaggatccgaattcgaATGATAGTTTAAAAGAGTTTTTGAA</td>
    </tr>
    <tr>
      <td>LahA3_rp</td>
      <td>ttctgttcgacttaagcattatgcggccgcTTAGACGGCTCCGGCTGACGATGCCGCAA</td>
    </tr>
    <tr>
      <td>LahA4_fp</td>
      <td>accatcatcaccacagccaggatccgaattcgaACGAGAATTTAAAGATGTTTTTACAGA</td>
    </tr>
    <tr>
      <td>LahA4_rp</td>
      <td>ttctgttcgacttaagcattatgcggccgcTTAAACCGCAAGTAAACTCATCGTTACAGC</td>
    </tr>
    <tr>
      <td>LahA5_fp</td>
      <td>accatcatcaccacagccaggatccgaattcgaACGAGAATCTCAAGCTATTTTTACAA</td>
    </tr>
    <tr>
      <td>LahA5_rp</td>
      <td>ttctgttcgacttaagcattatgcggccgcTTACATTGCCGATAATGATAATGATAATGC</td>
    </tr>
    <tr>
      <td>LahA6_fp</td>
      <td>accatcatcaccacagccaggatccgaattcgaATGAAAGGATAAAAGATTTATTTACCG</td>
    </tr>
    <tr>
      <td>LahA6_rp</td>
      <td>ttctgttcgacttaagcattatgcggccgcTTACATAAGTGCCTTTCTTATTGCAGTAAG</td>
    </tr>
    <tr>
      <td>LahA7_rp</td>
      <td>accatcatcaccacagccaggatccgaattcgaACGAGAACTTGAAGAAATTCCTGGAGG</td>
    </tr>
    <tr>
      <td>LahA7_fp</td>
      <td>ttctgttcgacttaagcattatgcggccgcTTATGAAGCAATCCTTGACCAACTATTGA</td>
    </tr>
  </tbody>
</table>

### Cloning of AzoA substrates

AzoA2, 3, 6, and 7 were amplified from Azospirillum sp. B510 genomic DNA (JCM 14679) via PCR using the appropriate AzoA forward and reverse primers (Table 4) and ligated into the pRSFDuet-1 vector (Novagen) after digestion with the restriction enzymes BamHI and NotI (for AzoA2) or BamHI and HindIII (for AzoA3, 6, 7). The N- and C-terminally His6-tagged E. coli mbp gene was amplified from the MBP-pET28 vector (a gift from Douglas A. Mitchell, University of Illinois at Urbana-Champaign) (Lee et al., 2008) using the appropriate MBP-AzoA G1/G4 primers. The gene encoding MBP was introduced such that MBP was appended to the N-termini of the AzoAs via Gibson assembly with the linearized AzoA-pRSFDuet vectors (amplified using MBP-AzoA G2/G3 primers). A sequence encoding a C-terminal tag with the amino acid sequence DAHHHHHH was added to the AzoA2, 3, and 7 constructs via overlap-extension PCR with the MBP-AzoACHis G1/G2 primers and one-component Gibson assembly (Gibson et al., 2009).

**Table 4.**
 Primers used in the cloning of AzoA constructs.Homology with vector backbone is displayed as lowercase letters.


<table>
  <thead>
    <tr>
      <th>Primer name</th>
      <th>Sequence 5'−3'</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AzoA2 fwd</td>
      <td>aaaGGATCCatgacaaccgaaacgcaaacc</td>
    </tr>
    <tr>
      <td>AzoA2 rev</td>
      <td>aaaGCGGCCGCctaccattttctgggaatggccaag</td>
    </tr>
    <tr>
      <td>AzoA3 fwd</td>
      <td>caatggacggtGGATCCGatgacagaccaaacccagtccacatcc</td>
    </tr>
    <tr>
      <td>AzoA3 rev</td>
      <td>cggaaacagccAAGCttactgttgtcgcaaacgcggtggtga</td>
    </tr>
    <tr>
      <td>AzoA6 fwd</td>
      <td>aaaggacttcgGGATCCgatgacaaatgaaacgcagcccacc</td>
    </tr>
    <tr>
      <td>AzoA6 rev</td>
      <td>ttatgggatcCAAGCTTctaccatttcctcgttccgagaatggc</td>
    </tr>
    <tr>
      <td>AzoA7 fwd</td>
      <td>caatggacccaGGATCCgatgacagaccaaacgcagtccgcc</td>
    </tr>
    <tr>
      <td>AzoA7 rev</td>
      <td>catggacatcCAAGCTTctaccattttgcacacacccccctgat</td>
    </tr>
    <tr>
      <td>MBP-AzoA G1</td>
      <td>aataaggagatataccatgGGCAGCAGCCATCATCATCATC</td>
    </tr>
    <tr>
      <td>MBP-AzoA G2</td>
      <td>TGGCTGCTGCCcatggtatatctccttattaaagttaaacaaaattatttctacagggg</td>
    </tr>
    <tr>
      <td>MBP-AzoA2 G3</td>
      <td>CTGTACTTCCAATCCatgacaaccgaaacgcaaaccgcc</td>
    </tr>
    <tr>
      <td>MBP-AzoA2 G4</td>
      <td>cgtttcggttgtcatGGATTGGAAGTACAGGTTCTCAGATCCACGC</td>
    </tr>
    <tr>
      <td>MBP-AzoA3 G3</td>
      <td>CTGTACTTCCAATCCatgacagaccaaacccagtccac</td>
    </tr>
    <tr>
      <td>MBP-AzoA3 G4</td>
      <td>ggtttggtctgtcatGGATTGGAAGTACAGGTTCTCAGATCCACGC</td>
    </tr>
    <tr>
      <td>MBP-AzoA6 G3</td>
      <td>CTGTACTTCCAATCCatgacaaatgaaacgcagccc</td>
    </tr>
    <tr>
      <td>MBP-AzoA6 G4</td>
      <td>cgtttcatttgtcatGGATTGGAAGTACAGGTTCTCAGATCCACGC</td>
    </tr>
    <tr>
      <td>MBP-AzoA7 G3</td>
      <td>CTGTACTTCCAATCCatgacagaccaaacgcagtccgcc</td>
    </tr>
    <tr>
      <td>MBP-AzoA7 G4</td>
      <td>gcgtttggtctgtcatGGATTGGAAGTACAGGTTCTCAGATCCACGC</td>
    </tr>
    <tr>
      <td>AzoA2CHis G1</td>
      <td>tctaGTGATGGTGATGGTGATGTGCATCccattttctgggaatggccaagc</td>
    </tr>
    <tr>
      <td>AzoA2CHis G2</td>
      <td>GATGCACATCACCATCACCATCACtagaagcttgcggccgcataatgcttaagtcg</td>
    </tr>
    <tr>
      <td>AzoA3CHis G1</td>
      <td>tctaGTGATGGTGATGGTGATGTGCATCctgttgtcgcaaacgcggtggtg</td>
    </tr>
    <tr>
      <td>AzoA3CHis G2</td>
      <td>GATGCACATCACCATCACCATCACtagaagcttgcggccgcataatgcttaagtcg</td>
    </tr>
    <tr>
      <td>AzoA7CHis G1</td>
      <td>tctaGTGATGGTGATGGTGATGTGCATCccattttgcacacacccccctgattccacc</td>
    </tr>
    <tr>
      <td>AzoA7CHis G2</td>
      <td>GATGCACATCACCATCACCATCACtagaagcttgcggccgcataatgcttaagtcg</td>
    </tr>
  </tbody>
</table>

### Cloning of XY33a substrates

The gene encoding XY33a was amplified from a pRSFDuet plasmid containing XY33a in MCSI and ProcM in MCSII (Yang et al., 2018) using primers XY33A_fp and XY33A_rp and touchdown PCR (Korbie and Mattick, 2008) with the annealing temperature decreasing from 70°C to 54°C over 80 cycles (−0.2°C/cycle). An example PCR amplification cycle consisted of denaturing (98°C for 10 s), annealing (from 70°C to 55°C, 0.2°C lower every cycle for a total of 80 cycles) for 30 s and extension (72°C for 30 s). The genes encoding XY33a variants A−3Y, A−3F, A−3K and A−3E, V−4K, V−4T, and V−4D, L−12A, L−12K, L−12D, L−12F, L−12W, L-12Y were amplified using the same protocol with the purchased synthetic genes in Table 5 as templates. All PCR products above, containing homology for Gibson assembly (Gibson et al., 2009) into an EcoRI/HindIII pRSFDuet digest, were purified by agarose gel electrophoresis and extracted using a Qiaquick Gel Extraction kit. The inserts were assembled into the EcoRI/HindIII-linearized pRSFDuet backbone using a molar ratio of 10:1 (insert: backbone) using the Gibson method (Gibson et al., 2009). The final construct was confirmed by sequencing. XY33a mutants D−10E/D−9E, D−9A, D−10A, E−8A, E−8K, E−8D, L−7A, L−7K, L−7D, E−6A, E−6K, and E−6D were generated in the following manner. The XY33a-wild type (MCSI) pRSFDuet plasmid was used as a template for two PCR reactions. One reaction used the RSF_fp primer and the gene-specific reverse primer encoding the mutation, and the other reaction used the RSF_rp primer and the forward primer encoding the desired mutation. The PCR amplification cycles were identical to the ones used for amplifying the gene encoding wild-type XY33a, except the extension time was 150 s. This strategy splits the pRSFDuet-1 vector in two roughly equal parts for Gibson assembly. The two PCR products were gel purified and extracted using a Qiaquick Gel Extraction kit and used in a Gibson assembly reaction in equimolar amounts. The Gibson reactions were used to transform E. coli DH10b, and the identities of the resulting constructs was verified by sequencing.

### Expression and purification of MBP-tagged AzoA2, 3, 6 and 7

MBP-AzoA-pRSFDuet constructs were used to transform E. coli Rosetta 2 (Novagen). Overnight cultures were diluted 1:100 into 1–2 L of LB containing kanamycin (50 μg/mL) and chloramphenicol (34 μg/mL), grown aerobically at 37°C (200 rpm) to OD600 0.6 and induced with 250 μM isopropyl β-D-1-thiogalactopyranoside (IPTG). Induction was allowed to proceed at 18°C (200 rpm) for 1–5 days. Cells were harvested at 8,000 × g and resuspended in 30–60 mL of lysis buffer (25 mM Tris pH 8.0, 500 mM NaCl, 20 mM imidazole, 10% [v/v] glycerol) containing 0.2–0.3 mg/mL lysozyme (Gold Biotech) and ¼ of a protease inhibitor tablet (Roche cOmplete, EDTA-free) for 1–2 hr before lysis by sonication for 8–9 × 60 s while stirring on ice. Lysate was clarified by centrifugation at 38,000 × g and loaded onto columns containing 2–5 mL of HisPur Ni-NTA Superflow agarose (Thermo Scientific) equilibrated in lysis buffer. The resin was washed with 30–50 mL each of lysis buffer and wash buffer (lysis buffer with 40 mM imidazole) before elution with 10–15 mL elution buffer (lysis buffer with 300 mM NaCl and 200 mM imidazole). Eluted protein was concentrated to <2.5 mL using a centrifugal concentrator (EMD Millipore) and exchanged into storage buffer (25 mM Tris pH 8.0, 500 mM NaCl, 10% [v/v] glycerol) using a PD-10 desalting column (GE Healthcare), concentrated to <500 μL, flash frozen, aliquoted, and stored at −80°C until use. Protein concentration was estimated by absorbance at 280 nm using extinction coefficients calculated by ExPASy (http://web.expasy.org/protparam); yields ranged from 5 to 15 mg/L culture.

### Expression and purification of XY33a, ProcA, and LahA

E. coli BL21 (DE3) cells were transformed with pRSFDuet-1 plasmids encoding either the N-terminally His-tagged ProcA 2.8 variants or LahAs in MCSI. An overnight culture was added to a culture flask containing TB with 2% glucose (1:50; v/v; overnight culture: overexpression culture), kanamycin (50 μg/mL) and 2.0 mM MgCl2. The culture was incubated in a 37°C shaker until OD600 reached 1.2–1.5. The cultures were cooled to 22°C and IPTG (500 μM final concentration for ProcA and XY33a peptides, 250 μM for LahA peptides) was used to induce expression. Following 16–20 hr incubation at 22°C, the cells were harvested at 5000 × g for 10 min and resuspended in LanA B1 Buffer (6.0 M guanidine hydrochloride, 0.5 mM imidazole, 20 mM NaH2PO4, pH 7.5), using 30–50 mL of LanA B1 Buffer for each liter of culture. Resuspended cells were stored at −80°C until purification. Freeze-thawing in 6.0 M guanidine hydrochloride lead to lysis of the cells, and the thawed cells were directly centrifuged at 30,000 × g for 30 min at 4°C. The supernatants were applied to 2–3 mL of His60 Clontech Ni superflow resin (catalog number 635660) that had been charged with two column volumes (CV) of 0.1 M NiSO4, washed with 10 CV of water and equilibrated with 10 CV of LanA B1 Buffer. The column was washed with ten CV of LanA B2 Buffer (4.0 M guanidine hydrochloride, 20 mM NaH2PO4, 30 mM imidazole, 300 mM NaCl, pH 7.5). Then, between 5–7 CV of LanA Elute Buffer (4.0 M guanidine hydrochloride, 20 mM TrisHCl, 1.0 M imidazole, 100 mM NaCl, pH 7.5) was used to elute the peptide. Peptides were desalted by SPE using an Agilent Bond Elut C18 SPE column following the manufacturer instructions and lyophilized. Dry peptides were resuspended in 5–10% Solvent B (0.1% TFA in MeCN) and purified by RP-HPLC using a Phenomenex C5 column (5 μm, 100 Å, 250 mm ×10 mm) with a linear gradient from 2% Solvent B in Solvent A (0.1% TFA in water) to 100% Solvent B in 45 min, monitoring absorbance at 220 nm. Fractions containing His-tagged peptide were identified by MALDI-TOF MS and lyophilized. Final yields varied between 3–5 mg/mL His-tagged peptide per liter of culture.

### Synthesis of inhibitor 1

ProTide Cl-TCP Cl resin (CEM) was used for the solid phase peptide synthesis (SPPS) of the ProcA2.8 sequence-based aldehyde inhibitor on a 0.2 mmol scale. The resin was suspended in 5 mL dichloromethane (DCM) at 0°C and SOCl2 (1.2 equiv.) and pyridine (2.4 equiv.) were added. The resin was stirred at reflux for 3 hr, filtered through a fritted funnel, washed with DCM and dried for 20 min under vacuum. FmocGly (five equiv.) was dissolved in 3 mL DCM in a round bottom flask and diisopropylethylamine (DIPEA, 8 equiv.) was added and the resulting solution was stirred for 20 min at room temperature. The dried resin was added to the round bottom flask and the reaction was stirred overnight at room temperature. The resin was then transferred to a fritted funnel, washed with DCM and dried under vacuum, then capped twice for 10 min using DCM:MeOH:DIPEA (80:15:5 v/v/v) as capping solution while sparging with nitrogen. After capping, the resin was washed with DCM and dried under vacuum. Fmoc-Gly-loaded-resin (7 mg) were deprotected using 3 mL of 20% piperidine in DMF. Loading was determined by absorbance at 290 nm measured on a NanoDrop 2000 (ThermoFisher), using 20% piperidine in DMF as a blank. SPPS conditions involved 0.2 M Fmoc-protected amino acid in DMF, 0.5 M (7-azabenzotriazol-1-yloxy)tripyrrolidinophosphonium hexafluorophosphate (PyAOP) and 0.5 M 1-hydroxybenzotriazole (HOBt) as activator, 2 M DIPEA as activator base, and 20% piperidine in DMF with 0.1 M HOBt as deprotection solution. After coupling of the first amino acid (Ala−2), the remainder of the synthesis (residues −3 through −13) was performed on a CEM Liberty Microwave peptide synthesizer. Final Fmoc deprotection was performed under microwave activation, then the resin was transferred to a glass fritted funnel and washed with DCM and dried under vacuum for 20 min. The resin was then transferred to a round bottom flask and N-terminally acetylated using a solution of acetic anhydride:pyridine (5 mL, 1:2 v/v) for 1 hr at room temperature. The resin was again transferred to a fritted funnel, washed with DCM, dried under vacuum for 20 min, and then transferred to a clean round bottom flask. Selective cleavage of the fully protected peptide was performed with 20% hexafluoroisopropanol in DCM for 1 hr at room temperature. This step cleaves the fully protected peptide from the resin leaving only the C-terminal carboxylic acid available for further reaction. This solution was filtered into a clean oven-dried round bottom flask and concentrated under vacuum. The peptide was dissolved in 5 mL anhydrous DCM under a nitrogen atmosphere. Aminoacetaldehyde (three equiv.), PyAOP (three equiv.) and N-methylmorpholine (10 equiv.) were mixed in 3 mL anhydrous DCM under nitrogen, then slowly added to the fully protected peptide solution over 30–40 min. The reaction was stirred at room temperature overnight, then concentrated by rotovap before total deprotection using a mixture of trifluoroacetic acid:water (95:5 v/v) for 1 hr at room temperature. The use of triisopropylsilane (TIPS) resulted in the reduction of the C-terminal aldehyde to the corresponding alcohol and hence TIPS was not added to the deprotection cocktail. The peptide was precipitated by adding 10-fold excess (v/v) of cold diethylether, centrifuged at 10,000 × g for 20 min, the supernatant removed, and the peptide dried under a nitrogen stream. The overall yield of the Ac-NLSDDELEGVAGG(aldehyde) peptide was 8% after RP-HPLC of the crude material resulting from SPPS, using a linear gradient from 1% Solvent B (0.1% TFA in acetonitrile) in Solvent A (0.1% TFA in water) to 61% solvent B over 61 min.

**Table 5.**
 Primers and synthetic genes used in the cloning of XY33a constructs.Mutations are shown in bold font. Homology with vector backbone is displayed as lowercase letters.


<table>
  <thead>
    <tr>
      <th>Primer or synthetic gene name</th>
      <th>Sequence (5’−3’)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>XY33A_fp</td>
      <td>catcaccatcatcaccacagccaggatccGTCTGAAGAGCAACTGAAGGC</td>
    </tr>
    <tr>
      <td>XY33A_rp</td>
      <td>gtacaatacgattactttctgttcgacttaagcattatTTAGCAAATATCGAGGACGTG</td>
    </tr>
    <tr>
      <td>RSF_fp</td>
      <td>Gcaggcgtttttccatagg</td>
    </tr>
    <tr>
      <td>RSF_rp</td>
      <td>Ctggcttgagcgtcgatttttg</td>
    </tr>
    <tr>
      <td>XY33a_D-9A_fp</td>
      <td>CGCCAAAATCTGTCTGAA GCA AGCTGGAAGGTGTGGC</td>
    </tr>
    <tr>
      <td>XY33a_D-9A_rp</td>
      <td>GCCACACCTTCCAGCT TGC TTCAGACAGATTTTGGCG</td>
    </tr>
    <tr>
      <td>XY33a_D-10A_fp</td>
      <td>CGCCAAAATCTGTCT GCA GAAAGCTGGAAGGTGTGGC</td>
    </tr>
    <tr>
      <td>XY33a_D-10A_rp</td>
      <td>GCCACACCTTCCAGCTTTC TGC AGACAGATTTTGGCG</td>
    </tr>
    <tr>
      <td>XY33a_D-10E,D-9E_fp</td>
      <td>CGCCAAAATCTGTCT GAA GAA AGCTGGAAGGTGTGGCTG</td>
    </tr>
    <tr>
      <td>XY33a_D-10E,D-9E_rp</td>
      <td>CAGCCACACCTTCCAGCT TTC TTC AGACAGATTTTGGCG</td>
    </tr>
    <tr>
      <td>XY33a_E-8A_fp</td>
      <td>CAAAATCTGTCTGATGAT GCA CTGGAAGGTGTGGCTGGG</td>
    </tr>
    <tr>
      <td>XY33a_E-8A_rp</td>
      <td>CCCAGCCACACCTTCCAG TGC ATCATCAGACAGATTTTG</td>
    </tr>
    <tr>
      <td>XY33a_E-8K_fp</td>
      <td>CAAAATCTGTCTGATGAT AAA CTGGAAGGTGTGGCTGGG</td>
    </tr>
    <tr>
      <td>XY33a_E-8K_rp</td>
      <td>CCCAGCCACACCTTCCAG TTT ATCATCAGACAGATTTTG</td>
    </tr>
    <tr>
      <td>XY33a_E-8D_fp</td>
      <td>CAAAATCTGTCTGATGAT GAT CTGGAAGGTGTGGCTGGG</td>
    </tr>
    <tr>
      <td>XY33a_E-8D_rp</td>
      <td>CCCAGCCACACCTTCCAG ATC ATCATCAGACAGATTTTG</td>
    </tr>
    <tr>
      <td>XY33a_L-7A_fp</td>
      <td>CTGTCTGATGATGAG GCA GAAGGTGTGGCTGGGG</td>
    </tr>
    <tr>
      <td>XY33a_L-7A_rp</td>
      <td>CCCCAGCCACACCTTC TGC CTCATCATCAGACAG</td>
    </tr>
    <tr>
      <td>XY33a_L-7K_fp</td>
      <td>CTGTCTGATGATGAG AAA GAAGGTGTGGCTGGGG</td>
    </tr>
    <tr>
      <td>XY33a_L-7K_rp</td>
      <td>CCCCAGCCACACCTTC TTT CTCATCATCAGACAG</td>
    </tr>
    <tr>
      <td>XY33a_L-7D_fp</td>
      <td>CTGTCTGATGATGAG GAT GAAGGTGTGGCTGGGG</td>
    </tr>
    <tr>
      <td>XY33a_L-7D_rp</td>
      <td>CCCCAGCCACACCTTC ATC CTCATCATCAGACAG</td>
    </tr>
    <tr>
      <td>XY33a_E-6A_fp</td>
      <td>GTCTGATGATGAGCTG GCA GGTGTGGCTGGGGGAG</td>
    </tr>
    <tr>
      <td>XY33a_E-6A_rp</td>
      <td>CTCCCCCAGCCACACC TGC CAGCTCATCATCAGAC</td>
    </tr>
    <tr>
      <td>XY33a_E-6K_fp</td>
      <td>GTCTGATGATGAGCTG AAA GGTGTGGCTGGGGGAG</td>
    </tr>
    <tr>
      <td>XY33a_E-6K_rp</td>
      <td>CTCCCCCAGCCACACC TTT CAGCTCATCATCAGAC</td>
    </tr>
    <tr>
      <td>XY33a_E-6D_fp</td>
      <td>GTCTGATGATGAGCTG GAT GGTGTGGCTGGGGGAG</td>
    </tr>
    <tr>
      <td>XY33a_E-6D_rp</td>
      <td>CTCCCCCAGCCACACC ATC CAGCTCATCATCAGAC</td>
    </tr>
    <tr>
      <td>XY33a_V-4K_gene</td>
      <td>TCTGAAGAGCAACTGAAGGCATTCCTCACCAAAGTTCAAGCCGATACTTCACTACAGGAACAGTTAAAGATAGAAGGAGCTGATGTTGTAGCCATTGCCAAAGCTGTAGGCTTCTCGATTACCACAGAAGACCTAAACTCTCATCGCCAAAATCTGTCTGATGATGAGCTGGAAGGTAAAGCTGGGGGAGCGG CCTGTCATTTCCTTCTTTTCTCTATGCCTCCATCCCACGTCCTCGATATTTGCTAA</td>
    </tr>
    <tr>
      <td>XY33a_V-4T_gene</td>
      <td>TCTGAAGAGCAACTGAAGGCATTCCTCACCAAAGTTCAAGCCGATACTTCACTACAGGAACAGTTAAAGATAGAAGGAGCTGATGTTGTAGCCATTGCCAAAGCTGTAGGCTTCTCGATTACCACAGAAGACCTAAACTC TCATCGCCAAAATCTGTCTGATGATGAGCTGGAAGGTACCGCTGGGGGAGCGGCCTGTCATTTCCTTCTTTTCTCTATGCCTCCATCCCACGTCCTCGATATTTGCTAA</td>
    </tr>
    <tr>
      <td>XY33a_V-4D_gene</td>
      <td>TCTGAAGAGCAACTGAAGGCATTCCTCACCAAAGTTCAAGCCGATACTTCACTACAGGAA CAGTTAAAGATAGAAGGAGCTGATGTTGTAGCCATTGCCAAAGCTGTAGGCTTCTCGATTACCACAGAAGACCTAAACTCTCATCGCCAAAATCTGTCTGATGATGAGCTGGAAGGTGATGCTGGGGGAGCGGCCTGTCATTTCCTTCTTTTCTCTATGCCTCCATCCCACGTCCTCGATATTTGCTAA</td>
    </tr>
    <tr>
      <td>XY33a_A-3Y_gene</td>
      <td>TCTGAAGAGCAACTGAAGGCATTCCTCACCAAAGTTCAAGCCGATACTTCACTACAGGAACAGTTAAAGATAGAAGGAGCTGATGTTGTAGCCATTGCCAAAGCTGCAGGCTTCTCGATTACCACAGAAGACCTAAACTCTCAT CGCCAAAATCTGTCTGATGATGAGCTGGAAGGTGTGTATGGGGGAGCGGCCTGTCATTTCCTTCTTTTCTCTATGCCTCCATCCCACG TCCTCGATATTTGCTAA</td>
    </tr>
    <tr>
      <td>XY33a_A-3F_gene</td>
      <td>TCTGAAGAGCAACTGAAGGCATTCCTCACCAAAGTTCAAGCCGATACTTCACTACAGGAACAGTTAAAGATAGAAGGAGCTGATGTTGTAGCCATTGCCAAAGCTGCAGGCTTCTCGATTACCACAGAAGACCTAAACTCTCATCGCCAAAATCTGTCTGATGATGAGCTGGAAGGTGTGTTTGGGGGAGCGGCCTGTCATTTCCTTCTTTTCTCTATGCCTCCATCCCACGTCCTCGATATTTGCTAA</td>
    </tr>
    <tr>
      <td>XY33a_A-3E_gene</td>
      <td>TCTGAAGAGCAACTGAAGGCATTCCTCA CCAAAGTTCAAGCCGATACTTCACTACAGGAACAGTTAAAGATAGAAGGAGCTGATG TTGTAGCCATTGCCAAAGCTGCAGGCTTCTCGATTACCACAGAAGACCTAAACTC TCATCGCCAAAATCTGTCTGATGATGAGC TGGAAGGTGTGGAAGGGGGAGCGGCCT GTCATTTCCTTCTTTTCTCTATGCCTCC ATCCCACGTCCTCGATATTTGCTAA</td>
    </tr>
    <tr>
      <td>XY33a_A-3K_gene</td>
      <td>TCTGAAGAGCAACTGAAGGCATTCCTCA CCAAAGTTCAAGCCGATACTTCACTACAG GAACAGTTAAAGATAGAAGGAGCTGATGTTGTAGCCATTGCCAAAGCTGCAGGCTTCTCGATTACCACAGAAGACCTAAACTCT CATCGCCAAAATCTGTCTGATGATGAGCTGGAAGGTGTGAAAGGGGGAGCGGCCTGTCATTTCCTTCTTTTCTCTATGCC TCCATCCCACGTCCTCGATATTTGCTAA</td>
    </tr>
    <tr>
      <td>XY33a_L-12A_gene</td>
      <td>TCTGAAGAGCAACTGAAGGCATTCCTC ACCAAAGTTCAAGCCGATACTTCACTACAGGAACAGTTAAAGATAGAAGGAGC TGATGTTGTAGCCATTGCCAAAGCTGCAGGCTTCTCGATTACCACAGAAGAC CTAAACTCTCATCGCCAAAATGCGTC TGATGATGAGCTGGAAGGTGTGGCTGGGGGAGCGGCCTGTCATTTCCTTCTTTTCTCTATGCCTCCATCCCACGTCCTCGATATTTGCTAA</td>
    </tr>
    <tr>
      <td>XY33a_L-12K_gene</td>
      <td>TCTGAAGAGCAACTGAAGGCATTCCTCACCAAAGTTCAAGCCGATACTTCACTACAGGAACAGTTAAAGATAGAAGGAGCTGATGTTGTAGCCATTGCCAAAGCTGCAGGCTTCTCGATTACCACAGAAGACCTAAACTCTCATCGCCAAAATAAATCTGATGATGAGCTGGAAGGTGTGGCTGGGGGAGCGGCCTGTCATTTCC TTCTTTTCTCTATGCCTCCATCCCACGTCCTCGATATTTGCTAA</td>
    </tr>
    <tr>
      <td>XY33a_L-12D_gene</td>
      <td>TCTGAAGAGCAACTGAAGGCATTCCTCACCAAAGTTCAAGCCGATACTTCACTACAGGAACAGTTAAAGATAGAAGGAGCTGATGTTGTAGCCATTGCCAAAGCTGCAGGCTTCTCGATTACCACAGAAGACCTAAACTCTCATCGCCAAAATGATTCTGATGATGAGCTGGAAGGTGTGGCTGGGGGAGCGGCCTGTCATTTCCTTCTTTTCTCTATGCCTCCATCCCACGTCCTCGATATTTGCTAA</td>
    </tr>
    <tr>
      <td>XY33a_L-12F_gene</td>
      <td>TCTGAAGAGCAACTGAAGGCATTCCTCACCAAAGTTCAAGCCGATACTTCACTACAGGAACAGTTAAAGATAGAAGGAGCTGATGTTGTAGCCATTGCCAAAGCTGCAGGCTTCTCGATTACCACAGAAGACCTAAACTCTCATCGCCAAAATTTTTCTGATGATGAGCTGGAAGGTGTGGCTGGGGGAGCGGCCTGTCATTTCCTTCTTTTCTCTATGCCTCCATCCCACGTCCTCGATATTTGCTAA</td>
    </tr>
    <tr>
      <td>XY33a_L-12W_gene</td>
      <td>TCTGAAGAGCAACTGAAGGCATTCCTCACCAAAGTTCAAGCCGATACTTCACTACAGGAACAGTTAAAGATAGAAGGAGCTGATGTTGTAGCCATTGCCAAAGCTGCAGGCTTCTCGATTACCACAGAAGACCTAAACTCTCATCGCCAAAATTGGTCTGATGATGAGCTGGAAGGTGTGGCTGGGGGAGCGGCCTGTCATTTCCTTCTTTTCTCTATGCCTCCATCCCACGTCCTCGATATTTGCTAA</td>
    </tr>
    <tr>
      <td>XY33a_L-12Y_gene</td>
      <td>TCTGAAGAGCAACTGAAGGCATTCCTCACCAAAGTTCAAGCCGATACTTCACTACAGGAACAGTTAAAGATAGAAGGAGCTGATG TTGTAGCCATTGCCAAAGCTGCAGGCTTCTCGATTACCACAGAAGACCTAAACTCTCATCGCCAAAATTATTCTGATGATGAGCTG GAAGGTGTGGCTGGGGGAGCGGCCTGTCATTTCCTTCTTTTCTCTATGCCTCCATCCCACGTCCTCGATATTTGCTAA</td>
    </tr>
  </tbody>
</table>
