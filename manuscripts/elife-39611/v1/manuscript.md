# Multiple serine transposase dimers assemble the transposon-end synaptic complex during IS607-family transposition

## Authors

- Wenyang Chen<sup>1</sup> ([ORCID: 0000-0003-3035-1496](https://orcid.org/0000-0003-3035-1496))
- Sridhar Mandali<sup>1</sup>
- Stephen P Hancock<sup>1</sup> ([ORCID: 0000-0003-4205-7913](https://orcid.org/0000-0003-4205-7913))
- Pramod Kumar<sup>1</sup>
- Michael Collazo<sup>2</sup>
- Duilio Cascio<sup>2</sup>
- Reid C Johnson<sup>1</sup> ([ORCID: 0000-0002-5562-1934](https://orcid.org/0000-0002-5562-1934)) †

### Affiliations

1. Department of Biological Chemistry David Geffen School of Medicine, University of California at Los Angeles Los Angeles United States
2. Department of Energy Institute of Genomics and Proteomics University of California at Los Angeles Los Angeles United States
3. Molecular Biology Institute University of California at Los Angeles Los Angeles United States

† Corresponding author

## Abstract

IS607-family transposons are unusual because they do not have terminal inverted repeats or generate target site duplications. They encode two protein-coding genes, but only tnpA is required for transposition. Our X-ray structures confirm that TnpA is a member of the serine recombinase (SR) family, but the chemically-inactive quaternary structure of the dimer, along with the N-terminal location of the DNA binding domain, are different from other SRs. TnpA dimers from IS1535 cooperatively associate with multiple subterminal repeats, which together with additional nonspecific binding, form a nucleoprotein filament on one transposon end that efficiently captures a second unbound end to generate the paired-end complex (PEC). Formation of the PEC does not require a change in the dimeric structure of the catalytic domain, but remodeling of the C-terminal α-helical region is involved. We posit that the PEC recruits a chemically-active conformer of TnpA to the transposon end to initiate DNA chemistry.

## Introduction

Although sometimes thought of as DNA parasites, transposable elements (TE) are widely recognized as playing prominent roles in the evolution of genomes (Biémont, 2010; Brunet and Doolittle, 2015; Volff, 2006). TE-derived sequences make up almost half of the human genome, and in some organisms like Maize, make up the vast majority of the genome (International Human Genome Sequencing Consortium et al., 2001; Springer et al., 2009). TEs can be usurped or ‘domesticated’ to perform critical functions, such as promoting DNA rearrangements essential for immunity in mammals or in the development of the micronucleus in ciliated protozoa (Baudry et al., 2009; Kapitonov and Jurka, 2005; Nowacki et al., 2009). In bacteria, mobile DNA elements promote horizontal spread of pathogenicity determinants and antibiotic resistance genes (Frost et al., 2005; Hooper et al., 2009). TEs are also exploited for genome engineering (Ivics and Izsvák, 2010; Woodard and Wilson, 2015).

Transposases have been reported to be the most frequently occurring functional group of proteins (Aziz et al., 2010). Among the four major classes of DNA transposases, the large and diverse DDE/D family that contain an RNase H fold and typically transpose through a cut-and-paste mechanism has been the most intensively studied (Hickman et al., 2010; Yuan and Wessler, 2011). Recently, the mechanism of transposition by HUH-family elements, which undergo a rolling circle replicative mechanism of DNA transfer, has been elucidated (He et al., 2015). The tyrosine- and serine-family of recombinases, which have been extensively studied in the context of site-specific recombination reactions, also promote DNA transposition. Respectively, these enzymes splice DNA through a sequential pair of single-strand exchanges or through double strand breaks, generating a transient covalent linkage between the cleaved DNA end and a tyrosine or serine on the protein (Rubio-Cosials et al., 2018; Stark, 2014; Wood and Gardner, 2015). In this study, we investigate the mechanism by which the IS607-family of serine recombinases transpose DNA. As described below, IS607-family TEs have a number of properties that are unusual among TEs, and the serine transposase structure has features unlike other serine recombinases.

Serine recombinases (SRs) have been broadly classified into three subfamilies (Smith and Thorpe, 2002). The small SRs (smSR) typically catalyze highly regulated recombination reactions between specific DNA sites that are usually on the same DNA molecule (Johnson, 2015; Rice, 2015). The serine integrase or large SR (LSR) subfamily typically promote phage integration and excision between specific sites (Smith, 2015; Van Duyne and Rutherford, 2013), but certain members promote DNA translocation reactions (Bannam et al., 1995; Wang et al., 2006). SmSRs and LSRs have their DNA binding domains (DBDs) at the C-terminal end of the protein, albeit the LSRs have a more elaborate C-terminal DNA binding and regulatory domain. The SRs found in IS607-family transposable elements, however, are distinguished by the location of their DBDs at their N-termini (experimentally confirmed below). This domain architecture is paradoxical because studies on smSRs imply that an N-terminally located DBD would be incompatible with the formation of active tetramers, which is the critical regulatory step of these reactions (Johnson, 2015; Rice, 2015; Stark, 2014).

The founding member of the IS607 family was first described by Berg and co-workers (Kersulyte et al., 2000), who also noted the relationship between the Helicobacter pylori IS607 element and annotated insertion sequence elements like IS1535 in the Mycobacteria tuberculosis genome sequence (Cole et al., 1998). IS607-family elements have been subsequently found in a wide range of bacterial species, including cyanobacteria, and in archea (Filée et al., 2007b; Kuno et al., 2010). IS607-related sequences have also been found in eukaryotic genomes and viruses, probably primarily through horizontal DNA transfer events, and have been described as the most widely distributed transposon in nature (Filée et al., 2007a; Gilbert and Cordaux, 2013).

IS607 elements encode two orfs, which often overlap in their coding sequence (Figure 1A). OrfA exhibits homology with SRs and is sufficient to mediate transposition of IS607 in E. coli (this paper and Kersulyte et al., 2000). The OrfB sequence bears a clear relationship with RuvC and Cas9, and is also present in some IS200/IS605 family members, some eukaryotic transposons, and as standalone genes (Bao and Jurka, 2013; Kapitonov et al., 2015). Surprisingly, the DNA sequences at the termini of individual IS607 elements are not related, but an inverted repeat sequence, often imperfect, is present near but at different distances from the ends of the element (Figure 1B). A common feature of the ends of IS607 elements is the presence of short directly-repeated motifs, which are positioned at different spacings with respect to each other and to the host DNA junction (Figure 1B). An additional unusual feature is that the IS607 transposition reaction does not create target site duplications (this paper and Blount and Grogan, 2005; Kersulyte et al., 2000). The absence of target site duplications may make IS607 elements useful as vehicles for delivering and subsequently removing genes from chromosomes without generating a genetic scar, similar to applications of the TE piggyBac (Woltjen et al., 2009; Woodard and Wilson, 2015).

![Figure 1.](https://cdn.elifesciences.org/articles/39611/elife-39611-fig1-v1.jpg)

**Figure 1.:** (A) Overall structure of IS607-family transposons with lengths given for the orfA and orfB coding regions (amino acid residues) of elements discussed in this paper. (B) DNA sequences at the ends of IS607-family transposons. The bottom strand of the left end (b–LE) and top strand of the right end (t–RE) are aligned with flanking host DNA sequences in green. Arrows highlight common sequences (inverted repeats) between the ends, and short sequence motifs (bold type are matches) for individual elements are denoted above and below the end sequences (for IS607 and ISC1926, sequence motif lengths can be extended with A or T on either side). The transposon-host borders for each of these elements have been reassigned based on alignments with related elements in their respective genomes and sequence analysis of transposition events (IS607 and ISC1926). The termini contain a GG, and the unoccupied host target sequences also contain a GG at the exchange site (e.g., panel C). (C) Transposition by IS607 in E. coli. Top: reconstructed IS607 transposons used in the transposition assays. OrfA and orfB, when present, are transcribed from the E. coli lac promoter (P) and contain ribosome binding sites. Middle: transposition frequencies onto phage λ of IS607 derivatives. Average and standard deviations are given for IS607orfA (n = 6) and Tn5 (n = 3) as a comparative control. Bottom: an example of a λ::IS607orfA transposition product. Sequences of the IS607 ends (bold), the unoccupied target, and the left and right end junctions after insertion of IS607orfA are shown. The site of DNA exchange is boxed. Additional insertion site sequences and a compilation are given in Figure 1—figure supplement 1.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/39611/elife-39611-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** Additional insertion site sequences of λ::IS607orfA transposition events are listed. Below is a sequence logo (https://weblogo.berkeley.edu) derived from 21 target sites from this work (orfA only, eight sites) and from Kersulyte et al. (orfA+B, F plasmid pOX38 target, 13 sites; Kersulyte et al., 2000). No preferential target sequence is evident outside of (G/C)GG.

In this work we investigate the serine transposase from three IS607-family elements: IS607 from H. pylori (Kersulyte et al., 2000), IS1535 from M. tuberculosis, and ISC1926 from the hypothermophilic archea Sulfolobus islandicus (Blount and Grogan, 2005). We confirm that OrfA is the only IS607-encoded protein required to catalyze transposition in E. coli, determine the domain structure of the three transposases, and describe X-ray structures of the OrfA catalytic domains from IS1535 and ISC1926, which exhibit remarkable differences in quaternary structure from other SR-family members. We show that OrfA from IS1535 efficiently generates paired-end complexes by an unexpected mechanism involving cooperative assembly of multiple proteins, which is both unlike other transposases studied to date and unlike synaptic complex formation by other SR-family members.

## Results

### IS607 transposition in vivo

We first sought to confirm and extend salient features of IS607 transposition originally described by Berg and co-workers (Kersulyte et al., 2000). We engineered tetracycline-resistant IS607 derivatives containing the left and right transposon ends and orfA or orfA+orfB genes (Figure 1C). Transposition onto λ was measured after phage induction in a recA E. coli λ lysogen, and the resulting λ lysates were used for transduction selecting tetracycline resistance. λ::IS607-tet transpositions were obtained for IS607orfA at a frequency of 1 × 10−7/pfu (Figure 1C), but no confirmed transposition events were obtained with IS607orfAB. We note that the relative expressions of orfB and orfA in the IS607 constructs are likely to be different than in the native element; nevertheless, these results indicate that OrfA is sufficient for promoting transposition and that OrfB is inhibitory, as concluded earlier (Kersulyte et al., 2000). No transposition events were obtained when OrfA contained a glycine substituted for the predicted active site serine (residue 72), consistent with OrfA catalyzing the transposition reaction through an SR mechanism. The frequency of IS607orfA-tet transposition into λ DNA was about 0.4% of that measured for the well-characterized transposon Tn5.

PCR analysis of the λ::IS607orfA-tet insertions confirmed the events were simple insertions and sequences of the new transposon-host boundaries showed that all insertions were at a GG dinucleotide target with no duplications of host sequence at the junctions (Figure 1C and Figure 1—figure supplement 1). A compilation of transposition events promoted by IS607orfA (this work) and IS607orfAB elements (Kersulyte et al., 2000) show that a (G)GG sequence is a preferred target, but no additional sequence relationships among the targets are evident (Figure 1—figure supplement 1). A GG dinucleotide at the transposon termini, together with an invariant GG at the insertion target site, is consistent with a DNA exchange reaction over a 2 bp identical sequence that is observed for other SRs.

### IS607-family TnpA domain architecture

The in vivo studies indicate that OrfA, hereafter called TnpA, is the only IS607 protein required for transposition. Purified preparations of recombinant TnpA from IS607, IS1535, and ISC1926 were obtained, and each protein was shown to be active for DNA binding to its cognate transposon ends (below and not shown). To probe domain architectures, each TnpA was subjected to partial proteolysis under native conditions followed by SDS-PAGE and mass spectrometry (Figure 2A and Figure 2—figure supplement 1). In each case, a trypsin-resistant fragment representing the catalytic domain and helix E region attached to a 3- (TnpAISC1926) to 11- (TnpAISC1535) residue N-terminal segment, which is predicted to be unstructured, was generated. Trypsin also cleaves near the middle of the helix E region of TnpAIS1535 and TnpAIS607 where available crystal structures show a ~ 4 residue turn separating the N- and C-terminal sections of the helix (see below). Structural models (Phyre2) of the N-terminal domains predict winged-helix motifs that closely match protein-DNA structures present in the PDB (Figure 2—figure supplement 1).

![Figure 2.](https://cdn.elifesciences.org/articles/39611/elife-39611-fig2-v1.jpg)

**Figure 2.:** (A) Domain architecture of TnpA proteins. Domain structures were derived from partial proteolysis/mass spectrometry (Figure 2—figure supplement 1), X-ray crystallography for TnpAIS1535 and TnpAISC1926, and Phyre2 models for the N-terminal DBDs (Figure 2—figure supplement 1) and the TnpAIS607 CTD. S denotes the predicted active site serine residue. (B and C) X-ray structures of the dimeric CTDs of TnpAIS1535 and TnpAISC1926, respectively. The helix E region folds into a 4-helix bundle that stacks on the catalytic core and occludes the catalytic serines. (D) Structure of the smSR γδ resolvase bound to DNA (PDB code: 1GDT). Unlike the TnpA proteins, the dimer interface is over the extended E-helices (salmon), and the DBD (dark green) is at the C-terminus. (E) Subunit structures of TnpA-CTDISC1926 and γδ resolvase highlighting the common folds of the catalytic cores but different helix E structures. (F) TnpAIS1535 (blue) and TnpAISC1926 (green) dimers are aligned over the catalytic domains of subunits A (rmsd = 1.1 Å). Helices B and D at the core dimer interface and the helix E bundles are highlighted to illustrate differences.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/39611/elife-39611-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** (A) TnpAIS607(His6) digested with trypsin and subjected to 18% SDS-PAGE. MALDI-TOF analysis of an aliquot from the 20 min digestion (*) gave a major peak consistent with the mass of a peptide from residue 55 (cleavage at Arg54) to the C-terminus and a second peak consistent with a peptide from Ser55 – Arg192 (located within the predicted turn between the N- and C-terminal segments of helix E). Below the SDS gel is a Phyre2 model of the N-terminal winged-helix domain structure (residues 6 – 55, blue) superimposed over a BMRR-DNA X-ray structure (grey protein, brown DNA; rmsd = 1.44 Å over protein backbone atoms). (B) TnpAIS1535(His6) digested with trypsin. MALDI-TOF analysis of an aliquot from the 15 min digestion (*) gave a major peak consistent with a peptide from residue 41 (cleavage at Lys40) to the C-terminus and a second major peak consistent with a peptide from Thr41 to Arg176 (located close to the turn between the N- and C-terminal segments of helix E). The Phyre2 model of the N-terminal winged-helix domain structure (residues 3 – 42, blue) is superimposed over a phage λ Xis-DNA X-ray structure (grey protein, brown DNA; rmsd = 0.74 Å). (C) TnpAISC1926(His6) digested with 2x the amount of trypsin used above and Ca2+ in the buffer. MALDI-TOF analysis of an aliquot from the 20 min digestion gave a dominant peak consistent with a peptide from residue 12 (cleavage at Arg11) to Lys220 and a second peak consistent with peptides from residues 62/63 (cleavage at Lys61 and Arg62) to Lys220. Cleavage of the linker between the DBD and catalytic domains was much weaker for TnpAISC1926 as compared to TnpAIS607 and TnpAIS1535, which may reflect the short intervening peptide chain. MALDI-TOF/TOF analysis of a different preparation of TnpAISC1926 (purified from an N-terminal SUMO fusion) and different trypsin gave products corresponding to peptides from 1-Lys61 and 1-Arg62 (weak) and Arg62 to the C-terminus. The Phyre2 model of the N-terminal winged-helix domain structure (residues 12 – 61, blue) is superimposed over a RacA-DNA X-ray structure (grey protein, brown DNA; rmsd = 1.41 Å).

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/39611/elife-39611-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** (A) The backbone of the TnpAIS1535 dimer structure is shown with its experimental electron density map contoured at 1.0 σ. The phases were determined by anomalous dispersion of six selenomethionine residues within the labeled dimer. (B) Stereo pair showing atomic details of helix E residues from TnpAIS1535. The 2Fo-Fc refined electron density map at 1.0 σ is shown for the N-terminal (orange) and C-terminal (blue) sections of helix E from subunit A. (C) TnpAISC1926 crystallized with two dimers in the asymmetric unit: chain A (blue), B (green), C (magenta), and D (orange). (D) Fo-Fc difference OMIT map (3.0 σ) describing the only well resolved core-helix E linker (TnpAISC1926 chain A; blue). The linker is stabilized by interactions (black dashes) with a symmetry-related dimer (orange). (E) Related X-ray structures from the PDB. IS1904 is an IS607-family transposon. The catalytic core dimer interfaces (helices B and D) and orientations of the helix E bundle relative to the catalytic domain of each of these proteins are more similar to TnpAISC1926 (rmsds 0.85 – 1.24 Å, peptide backbone atoms) than to TnpAIS1535 (rmsds 2.12 – 2.66). (F) Cysteine crosslinking of TnpAIS1535. On the left is a backbone trace of TnpAIS1535 with positions highlighted where cysteines were substituted. On the right are reducing and non-reducing SDS gels of the WT and mutant proteins before and after oxidation with diamide, respectively. The TnpAIS1535 CTD is also included in the reducing gel. A134C and A182C only weakly formed disulfide-linked dimers, presumably because the cysteines are well buried and therefore excluded from the oxidant and because of suboptimal geometry. Endogenous cysteines were not replaced in this experiment, which may account for some of the different higher MW species upon oxidation (compare with Figure 7B where oxidation products of single-cysteine mutants are shown).

### IS607-family TnpA structures

X-ray crystal structures for the C-terminal domains (CTDs) of TnpA from IS1535 (residues 51 – 193) and ISC1926 (residues 65 – 221) were determined and found to contain either one or two dimers in their asymmetric unit, respectively (Figure 2B,C, Figure 2—figure supplements 2A–D; Table 1). Each chain adopts a structure that includes four α-helices sandwiching four β-strands from the beginning of the CTD to the end of β4 (TnpAIS1535 residues 51 – 144 and TnpAISC1926 residues 65 – 162), a topology that is identical to that of the catalytic core of smSRs (Figure 2D,E). Pairwise structure alignments to the end of β4 between the catalytic domains of TnpAIS1535 and TnpAISC1926 and the smSRs γδ resolvase (PDB code 1GDT) and Sin (PDB code 2R0Q) dimers give rms deviations from 1.6 to 3.3 Å, even though pairwise sequence comparisons between the catalytic domains TnpA proteins and smSRs typically exhibit <30% amino acid identity (with short indels).

**Table 1.**
 X-ray diffraction data and refinement statistics.


<table>
  <thead>
    <tr>
      <th>Structure PDB code</th>
      <th>ISC1926-TnpA 6DGC</th>
      <th>IS1535-TnpA – Native 6DGB</th>
      <th>IS1535-TnpA – SeMet</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Data collection</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Beamline</td>
      <td>APS 24 ID-C</td>
      <td>APS 24 ID-C</td>
      <td>APS 24 ID-C</td>
    </tr>
    <tr>
      <td>Space group</td>
      <td>C1</td>
      <td>P212121</td>
      <td>P212121</td>
    </tr>
    <tr>
      <td>Unit cell dimensions</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>a, b, c (Å)</td>
      <td>97.1, 212.3, 61.6</td>
      <td>52.6, 54.2, 104.38</td>
      <td>52.3, 54.1, 104.5</td>
    </tr>
    <tr>
      <td>α, β, γ (o)</td>
      <td>90.0, 126.7, 90.0</td>
      <td>90.0, 90.0, 90.0</td>
      <td>90.0, 90.0, 90.0</td>
    </tr>
    <tr>
      <td>Wavelength (Å)</td>
      <td>0.9793</td>
      <td>0.9792</td>
      <td>0.9792</td>
    </tr>
    <tr>
      <td>Resolution range (Å)*</td>
      <td>20 - 2.9 (3.0-2.9)</td>
      <td>48.1 - 2.5 (2.6-2.5)</td>
      <td>52.3 - 2.5 (2.6-2.5)</td>
    </tr>
    <tr>
      <td>Measured reflections</td>
      <td>71134</td>
      <td>44467</td>
      <td>68063</td>
    </tr>
    <tr>
      <td>Unique reflections</td>
      <td>19649</td>
      <td>10275</td>
      <td>19606</td>
    </tr>
    <tr>
      <td>Rmerge†</td>
      <td>5.0 (51.1)</td>
      <td>9.9 (64.8)</td>
      <td>7.9 (75.9)</td>
    </tr>
    <tr>
      <td>CC1/2</td>
      <td>0.99 (0.76)</td>
      <td>0.99 (0.85)</td>
      <td>0.99 (0.82)</td>
    </tr>
    <tr>
      <td>I/σ</td>
      <td>12.8 (1.3)</td>
      <td>6.5 (1.5)</td>
      <td>10.0 (1.3)</td>
    </tr>
    <tr>
      <td>Completeness (%)</td>
      <td>88.6 (56.8)</td>
      <td>95.2 (91.4)</td>
      <td>98.8 (95.0)</td>
    </tr>
    <tr>
      <td>Refinement</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Resolution (Å)</td>
      <td>2.9</td>
      <td>2.5</td>
      <td></td>
    </tr>
    <tr>
      <td>No. of reflections</td>
      <td>15775</td>
      <td>7951</td>
      <td></td>
    </tr>
    <tr>
      <td>Rwork</td>
      <td>22.0</td>
      <td>22.8</td>
      <td></td>
    </tr>
    <tr>
      <td>Rfree‡</td>
      <td>24.6</td>
      <td>26.1</td>
      <td></td>
    </tr>
    <tr>
      <td>RMSD bond length (Å)</td>
      <td>0.01</td>
      <td>0.01</td>
      <td></td>
    </tr>
    <tr>
      <td>RMSD bond angle (o)</td>
      <td>1.15</td>
      <td>1.17</td>
      <td></td>
    </tr>
    <tr>
      <td>No. of atoms</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Protein</td>
      <td>3996</td>
      <td>2002</td>
      <td></td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>24</td>
      <td></td>
    </tr>
    <tr>
      <td>Average B factors</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Protein</td>
      <td>76.4</td>
      <td>50.2</td>
      <td></td>
    </tr>
    <tr>
      <td>Solvent</td>
      <td></td>
      <td>28.9</td>
      <td></td>
    </tr>
    <tr>
      <td colspan="2">Ramachandran statistics§</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Favored</td>
      <td>97.1</td>
      <td>95.2</td>
      <td></td>
    </tr>
    <tr>
      <td>Allowed</td>
      <td>2.9</td>
      <td>4.6</td>
      <td></td>
    </tr>
    <tr>
      <td>Outliers</td>
      <td>0</td>
      <td>0.2</td>
      <td></td>
    </tr>
  </tbody>
</table>

_*Values in parentheses refer to the highest resolution shell.†Rmerge = Σ | I-<I> | / Σ I‡Calculated using 5% (IS1535) and 10% (ISC1929) of the data.§Percentage of residues in Ramachandran plot regions were determined using PROCHECK_

Although there is considerable structural similarity between the catalytic core domains of the subunits, the quaternary structures of the TnpA and smSRs dimers are radically different. The dimerization interface of the core domains of TnpA is between helices B and D of each subunit (Figure 2B,C), which do not share contacts in the smSR dimer structures (e.g., Figure 2D). The 961 Å2 (TnpAIS1535) and 924 Å2 (TnpAISC1926) dimer interfaces within the core are relatively flat and hydrophobic, but there are a few polar connections between the subunits. By contrast, smSR subunits are associated in the dimer via their helix E regions through almost exclusively hydrophobic contacts (Figure 2D). Although the overall configurations of the TnpAIS1535 and TnpAISC1926 dimers are similar, there are significant differences in the details of the dimer interfaces within the core (Figure 2F). The TnpAISC1926 subunits are shifted apart by about 3 Å relative to TnpAIS1535, the TnpAISC1926 D helices are angled by about 15° rather than being parallel, and the TnpAISC1926 B helices are one turn longer than in TnpAIS1535.

The active site serines of each TnpA dimer (TnpAIS1535 residue 59 and TnpAISC1926 residue 74) are separated by 28.6 and 31.5 Å (Cα atoms), respectively (Figure 2B,C). This is a much longer distance than would be predicted to catalyze cleavage of scissile phosphates across the minor groove of B-DNA, assuming a 2 bp staggered cleavage (~14 Å separation) that is common to other SRs. An even longer separation between active site serines is present in the catalytically-inactive dimers of γδ resolvase and Sin (Mouw et al., 2008; Yang and Steitz, 1995).

The helix E regions of the TnpA dimer structures are also completely different from those of other SRs (Figure 2E). After β4 in the TnpA dimers, a poorly structured 9 – 10 residue peptide travels along one side of the active site to connect to the helix E region (Figure 2—figure supplement 2D). The E helices are interrupted by a four residue β-turn (GRRG in TnpAIS1535 and GMRS in TnpAISC1926) and fold into an antiparallel structure. The split E helices from each subunit associate into a 4-helix bundle, with the C-terminal segments of TnpAIS1535 helix E rotated 35° relative to those of TnpAISC1926 (Figure 2F). The helix E region excludes a total of about 3685 Å2 of solvent accessible surface area in both proteins and would sterically prevent DNA from associating with the active sites (Figure 2B C F). The helix E conformation and the separation of active site serines indicate that this dimer conformation cannot be active for DNA chemistry (see also Boocock and Rice, 2013).

The structures of the IS1535 and ISC1926 TnpA dimers are very similar to SRs from Methanocaldococcus jannaschii (PDB code 3LHK;) and Sulfolobus solfataricus (PDB codes 3ILX and 3LHF) (Figure 2—figure supplement 2E), which have been discussed previously (Boocock and Rice, 2013). Nevertheless, because the quaternary structures of the TnpA-like proteins are so different from other SRs and because these differences have profound functional implications, we tested aspects of the dimeric structure by cysteine crosslinking. Cysteines were substituted at TnpAIS1535 residues within the catalytic core and helix E region where they would be proximal and oriented appropriately for intersubunit disulfide formation (Figure 2—figure supplement 2F). F126C, located just before the start of helix D, and Q138C at the C-terminal end of helix D efficiently formed dimers after oxidation. Within the helix E bundle, L162C generated substantial amounts of covalently-linked dimers and A182C generated a small amount of dimers after oxidation. These solution results substantiate the dimeric structures observed by crystallography.

### Binding of TnpA to the transposon ends

DNA binding by full-length TnpA proteins of IS607, IS1535, and ISC1926 to their respective transposon ends was observed by gel mobility shift assays (EMSAs). Binding by the TnpAIS1535 to its left end (LE) was the most robust so we focus on IS1535 in the analysis below. As expected, no DNA binding was observed for TnpAIS1535 missing residues 1 – 50 comprising the N-terminal winged-helix domain.

Figure 3A shows complexes formed with increasing amounts of TnpAIS1535 incubated with radiolabeled DNA probe of the IS1535 LE plus adjacent host DNA and separated by native PAGE. Formation of a slowly migrating complex is accompanied by loss of the free LE probe. We show in Figure 3F (lanes 2 – 10) that the slowly migrating complex contains two LE DNA segments (i.e., a pair-end complex, PEC) by incubating TnpA with the radiolabeled 140 bp probe plus excess unlabeled 240 bp LE fragments. This results in formation of a supershifted complex, demonstrating the presence of both the labeled and unlabeled LE DNA fragments. Most of the LE probe associates into PECs with <10 nM TnpA (Figure 3A,B). A much lower level of a complex (complex 1) that accumulates with increasing TnpA concentration is also evident, and a small amount of an additional complex (complex 2) is formed at high TnpA concentrations. Appearance of complex 2 is accompanied by a similar decrease of PECs. Formation of PECs is strongly enhanced by Mg2+, Ca2+, Mn2+, or spermidine; in the presence of EDTA, PEC levels severely decrease and complex 1 coordinately increases (Figure 3—figure supplement 1). A time course of PEC assembly on left ends by 10 nM TnpA indicates that PECs form relatively slowly, requiring about 30 min to reach maximum levels (Figure 3C,D). Neither time course experiments performed at the optimal 37° or at lower temperatures (not shown), where both rates of formation are slower and yields of PECs are decreased, provide evidence that complex 1 is a kinetic intermediate.

![Figure 3.](https://cdn.elifesciences.org/articles/39611/elife-39611-fig3-v1.jpg)

**Figure 3.:** (A) Increasing amounts of TnpA (1 to 128 nM in 2-fold increments) were incubated with a 149 bp 32P-labeled DNA fragment containing the left transposon end and adjacent host sequence. After 1 hr at 37°C, the samples were subjected to native PAGE. The locations of unbound probe (free LE), paired-end complex (PEC), complex 1 (c1) and complex 2 (c2) are denoted. (B) Plot showing relative amounts of the PEC, complex 1, and complex 2 as a function of TnpA concentration. The insert expands the lower TnpA concentration range leading to maximum levels of PECs. (C) Time course of LE-PEC formation. TnpA (8 nM) was incubated with the LE probe at 37°C for increasing times as denoted and applied to a native gel. (D) Plot of the accumulation of LE-PECs and complex 1 as a function of time. (E) TnpA complexes formed on the right end. Reactions were performed as in panel A except that a 139 bp RE DNA probe was used. (F) Formation of hetero-PECs with different lengths LE or RE DNA fragments. In lanes 2 and 12, 100 nM TnpA was incubated with 0.5 nM 149 bp radiolabeled LE probe (*LE). In lanes 3 – 10, increasing amounts of unlabeled 240 bp LE fragments (2 to 128 nM, in 2-fold increments) were included in the reaction. Radiolabeled PECs, but not complex 1 or 2, shift to a slower migrating species in the presence of excess 240 bp LE fragments indicating that these complexes contain both 149 and 240 bp LE DNA molecules. In lanes 13 – 19, increasing amounts of unlabeled 230 bp RE fragments (2 to 128 nM, in 2-fold increments) were included in the reaction with *LE. A small amount of LE + RE PECs form at high RE concentrations. Lanes 1 and 11 are *LE only.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/39611/elife-39611-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** Gel mobility shift assays were performed as in Figure 3A except 5 mM EDTA, 5 mM Mg acetate (same as Figure 3A), 2.5 mM CaCl2, or 1 mM spermidine was present in the binding reaction, and the gel buffer was Tris-acetate plus 1 mM EDTA, Mg acetate, CaCl2, or Mg acetate, respectively. MnCl2 can also effectively support PEC formation (not shown).

Gel mobility shift assays performed on the right transposon end (RE) generate a different profile (Figure 3E). Only a small amount of PECs (3% of total probe) are generated, peaking at 8 nM TnpA, whereas complex 1 continues to increase to become the dominant product at high TnpA concentrations. The RE is also inefficient at forming PECs with the LE (Figure 3F, lanes 12 – 19). The poor substrate activity of the RE correlates with the presence of only two sequence motifs (Figure 1B).

### TnpAIS1535 binds over a remarkably long DNA segment in LE-PECs

TnpAIS1535 LE-PEC assembly reactions were subjected to DNase I footprinting. Protections from DNase I cleavage occurred from LE bp 7 (LE 7; LE 11 on the bottom strand) and extend internally to about LE 75 at TnpA concentrations generating PECs (Figure 4A,E). DNA sequences over motifs a-d show particularly strong protections together with a series of cleavage enhancements that are separated by about 10 bp. The protected region, albeit weaker, continues internally from motif d to about LE 75. Clear evidence of TnpA binding over motif e is present, but surprisingly weak protections are detectable at nucleotides surrounding the transposon-host junction. Notably, sequences outside of core motifs a-d become protected with increasing TnpA concentrations coordinately with the core motifs, implying cooperative binding of TnpA over about 70 bp of the LE concurrent with formation of the PEC (Figure 4—figure supplement 1).

![Figure 4.](https://cdn.elifesciences.org/articles/39611/elife-39611-fig4-v1.jpg)

**Figure 4.:** (A) DNase I footprints of TnpA to 5′ end-labeled bottom (left panel) and top (right panel) strands of the LE. TnpA concentrations were from 4 to 128 nM, in 2-fold increasing concentrations, 0 is no TnpA added, and ATCG are dideoxy sequencing lanes primed by the same oligonucleotide used to prepare the footprinting probe. Numbers on the left denote transposon sequence coordinates and are positioned relative to the 0 lane. The black bar on the right marks transposon sequences with arrows showing motif locations. The dashed line denotes regions of significant changes in DNase I cleavage by TnpA. See Figure 4—figure supplement 1 for EMSAs of binding reactions just prior to DNase I digestion showing relative amounts of PECs. (B) Boundaries of TnpA binding to the LE delineated by Exo III digestion. PEC-assembly reactions, containing from 1 to 128 nM TnpA in 2-fold increasing concentrations, were incubated with Exo III for 30 min. Lane 0 is no TnpA and -exo is no Exo III added. Solid arrowheads indicate major Exo III digestion stops, and open arrowheads denote minor Exo III stops that are TnpA dependent. (C) Time course of Exo III digestion on LE PECs. Preassembled PECs were subjected to Exo III digestion for 0 – 40 min as labeled. (D) Exo III digestion stops on the RE. Reactions were the same as in panel B except that 5′ end-labeled DNA probes representing the RE DNA strands were used. (E) Summary of DNase I and Exo III footprinting data on the LE and RE sequences. Changes in DNase I reactivity by TnpA are denoted with blue lines; dashed lines indicates weak protection. Red arrows denote Exo III digestion stops; shorter arrows signify minor stops and arrows in parentheses are stops appearing after long digestion times. IS1535 end sequence motifs (open arrows) are positioned above the sequence.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/39611/elife-39611-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** 1 µl aliquots of footprint binding reactions just prior to DNase I digestion were added to 20 µl EMSA buffer and applied to a native gel to assess the relative amounts of PECs in the footprint reactions. TnpAIS1535 concentrations were from 1 to 128 nM.

Digestion by Exo III, a 3′ to 5′ exonuclease, generates a weak TnpAIS1535-dependent stop at LE 8 and a strong stop at LE 18 on the top strand (Figure 4B,E). On the bottom strand, Exo III digestion stops occur at LE 78/77 (weak) and LE 68/67 (strong). Increasing Exo III digestion times on LE-PECs suggest that the nuclease can progressively remove 10 bp blocks of TnpAIS1535-mediated protection (Figure 4C). For example, the weaker stop at LE 8 near the host boundary is nearly lost at long digestion times, and longer digestion times on the bottom strand result in loss of the LE 78/77 stop, increasing amounts of the LE 68/67 stop, and a new product at LE 59/58. Taken together, the Exo III and DNase I footprinting results indicate that strong TnpA binding to the LE occurs between approximately LE 18 and LE 67 with weaker binding extending at least 10 bp in both directions. Both footprinting methods indicate weak, if any, binding over and adjacent to the transposon-host boundary.

### TnpAIS1535 binds only over the two motifs on the IS1535 RE

As described above, TnpA binding to the IS1535 RE primarily forms a complex I product (Figure 3E). Incubation of TnpA-RE reactions with Exo III resulted in digestion stops at RE 7 (top strand) and RE 28 (bottom strand), which flank the two motifs present on this end (Figure 4D,E). TnpA was unable to protect the IS1535 RE from DNase I cleavage, although weak cleavage enhancements were evident at positions within the two motifs that are analogous to the strong enhancements observed in the LE motifs (not shown). The 20 bp Exo III protected region on the RE provides evidence that complex I reflects TnpA binding to two adjacent motifs.

### LE-PEC formation requires IS1535 motifs a-d plus flanking non-specific DNA sequences

Gel mobility shift assays on probes with progressively truncated endpoints internal to the LE reveal that about 84 bp are required for robust PEC formation (Figure 5, top panel, and Figure 5—figure supplement 1A). Less efficient PEC assembly is observed with LE segments deleted down to 69 bp, with substrates containing endpoints at LEΔ74 and LEΔ69 generating faster migrating PECs, suggesting fewer molecules of TnpA in the complex. No detectable PECs form with a substrate truncated at LEΔ64. Amounts of complex I generally increase as PEC levels decrease until LEΔ44 where levels of complex I diminish, and LEΔ39, where complex I is not detectable. Addition of non-specific DNA to the LE 39 end restores complex I formation (Figure 5—figure supplement 1D).

![Figure 5.](https://cdn.elifesciences.org/articles/39611/elife-39611-fig5-v1.jpg)

**Figure 5.:** Top series are LE truncations beginning internal to the transposon. Middle series are truncations beginning within host DNA (H) flanking the transposon. Bottom series are LE sequences from transposon nt 20 to various internal endpoints embedded in vector DNA. PEC assembly was averaged from at least three different experiments for each probe. The concentrations of TnpAIS1535 required for 50% conversion of the probe to PECs are listed; if <50% of the probe was converted to PECs, the maximum yield of PECs obtained over the TnpA titration series (up to 128 nM TnpA) is given in parentheses. ND indicates PECs are not detected in the EMSAs. The presence of complex 1 is denoted by +, absence by -, and barely detectable levels by +/-. See Figure 5—figure supplement 1 for supporting data.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/39611/elife-39611-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** (A) Deletion series of LE sequences from the transposon side. All probes contain 102 bp of DNA on the host end. Representations of the truncated LE probes are given below the schematic of the LE. H indicates host sequence, and dashes indicate appended vector sequence. EMSAs were performed with 1 to 128 nM TnpAIS1535 in 2-fold increasing concentrations. The position of the free probe, complex 1, and PECs are marked; the asterisks denote faster migrating PECs, which were confirmed for LEΔ69 to contain two DNA duplexes by the method used in Figure 3F. (B) Deletion series from the host side. All probes contain 149 bp on the transposon side with DNA endpoints on the right side as labeled. (C) Truncated LE segments embedded in vector DNA. Each probe has LE sequences beginning at nt 20 and varying amounts of upstream transposon sequence, as designated, with vector sequence (dotted lines) appended to each end. LE(v44-20v) PECs were confirmed to contain two DNA duplexes. (D) PEC formation by deleted LE probes without or with appended non-specific (vector) DNA. Shown are deletions ending in LE-20 and LE-25 at the border of motif a, and LE-39 on the border of motif b, without and with vector DNA appended to the deletion end points.

Resections of host DNA and sequences at the transposon end result in moderately decreasing efficiencies of PEC formation, with LE5Δ, which removes 4 bp of the transposon end, requiring about 10-fold more TnpA than full length substrates (Figure 5, middle panel, and Figure 5—figure supplement 1B). Low levels of PECs are generated with LE10Δ, LE15Δ, and LE20Δ, which remove DNA up to the beginning of motif a, and PECs are not detectable with LE25Δ, which removes part of motif a. As observed with the upstream resections, complex 1 levels increase somewhat as PEC assembly becomes less efficient but decrease markedly with the LE25Δ truncation where motif a is disrupted.

The upstream and downstream truncation series define the minimal LE DNA segment required for detectable PEC assembly to be between LE 69 and LE 20. These boundaries are consistent with the major Exo III protected borders between LE 67 and LE 18. Appending vector DNA onto the LE20Δ junction (LE20v) fully restores efficient PEC assembly (Figure 5—figure supplement 1D). However, appending vector DNA onto the LE25Δ junction did not enable PEC formation or increase levels of complex 1. Although LEΔ64 is inactive for PEC formation (Figure 5, top panel, Figure 5—figure supplement 1A), appending vector DNA onto the LEΔ64 end (in the context of LE20v) fully restores PEC assembly (Figure 5, bottom panel, and Figure 5—figure supplement 1C). PEC formation remains efficient on a probe containing transposon sequences down to LE 54 when fused to vector DNA; LE(v54-20v) contains part of motif d through motif a. Removal of transposon sequences into motif c (v49-20v and v44-20v), however, markedly decreases PEC formation, and a substrate containing only LE transposon sequence comprising motifs a and b (v39-20v) only forms barely detectable levels of PECs but generates complex 1 (Figure 5, bottom panel).

Taken together, these results demonstrate that transposon sequences contained in motifs a-d (LE 59 to LE 20) encompass the minimal IS1535 DNA required for efficient PEC assembly. However, PEC formation requires at least an additional 10 bp of non-specific DNA upstream of motif d (an additional 25 bp for robust formation), and about 30 bp of nonspecific DNA downstream of motif a for fully efficient PEC formation.

### IS1535 LE core motif sequences nucleate formation of the PEC

LE(v54-20v) efficiently forms PECs even though it contains only 35 bp of transposon sequence corresponding to motif a through part of motif d (Figure 5, bottom panel, and Figure 5—figure supplement 1C). TnpAIS1535 strongly protects sequences from DNase I cleavage on LE(v54-20v) PECs over the core motifs a-d, and protections extend into vector sequences on either side of the core motifs at least as far as observed for the native LE (Figure 6,C). The major Exo III stops on LE(v54-20v) are at the boundaries of motifs a-d (Figure 6B,C).

![Figure 6.](https://cdn.elifesciences.org/articles/39611/elife-39611-fig6-v1.jpg)

**Figure 6.:** (A) DNase I footprints of PEC assembly reactions on 5′-32P-labeled bottom and top strands of LE(v54-20v). TnpA concentrations were from 4 to 128 nM in 2-fold increasing amounts. Shaded rectangles on the left of the gels denote the positions of transposon sequences; coordinates labeled with v are vector sequences with vH being the equivalent locations of host DNA. The bars on the right of the gels denote regions of significant changes in DNase I reactivity by TnpA with dashes indicating weakly protected regions. (B) Exonuclease III delineated boundaries of TnpA binding. TnpA concentrations are the same as in panel A. (C) Summary of DNase I (strongly protected regions, blue) and Exo III digestion boundaries on the LE(v54-20v) sequence. Small letters denote vector sequence.

The profile on LE(v54-20v) suggest a mechanism by which TnpAIS1535 binds cooperatively and with high affinity to the four core motifs a-d, even with only half of the native motif d sequence present. Additional molecules of TnpA then spread in either direction from the core ‘nucleation’ segment in a sequence-independent manner. When the motif d sequence is completely absent, as in LEΔ49 (Figure 5, bottom panel, and Figure 5—figure supplement 1C), PEC formation is inefficient, and no PECs are formed when motif a is partially removed (LE25v, Figure 5—figure supplement 1C).

### The helix E region, but not the TnpA catalytic core domain, is remodeled during PEC assembly

As discussed above, the quaternary structure of TnpA solution dimers are very different from other serine recombinases and are predicted to be in an inactive conformation for DNA chemistry. We asked whether conformational changes were required for cooperative DNA binding and formation of the PEC. Single-cysteine derivatives of TnpAIS1535 were oxidized to form disulfide-linked dimers and evaluated for their ability to assemble PECs. Cys126 near the N-terminal end of helix D and Cys138 at the C-terminal end of helix D were efficiently oxidized into covalent dimers that lock the two dimeric subunits together within the catalytic domain core (Figure 7A,B). Both of these disulfide-linked mutant dimers efficiently formed PECs (Figure 7C,D). We conclude that a rearrangement of subunits within the catalytic core of the dimer is not required for PEC assembly.

![Figure 7.](https://cdn.elifesciences.org/articles/39611/elife-39611-fig7-v1.jpg)

**Figure 7.:** (A) TnpAIS1535 dimer structure highlighting residues 126, 138, and 162, which are modeled as cysteines in rotomers compatible for disulfide formation. The helix E region on the right is rotated clockwise in the Y plane about 90° to better visualize Cys162. (B) Non-reducing SDS-PAGE of reduced and oxidized preparations of TnpAIS1535 mutants containing single cysteine residues. The three native cysteines were replaced with serines in these mutants. (C–E) EMSAs of PEC assembly by reduced and oxidized preparations of Cys126, Cys138, and Cys162 mutants, respectively. The LE probe was incubated with 1 to 64 nM TnpA mutant in 2-fold increasing concentrations. (F) PEC assembly by wild-type TnpA and a deletion mutant missing the helix E region (residues 147 – 193). TnpA concentrations are the same as in panels C-E except that a reaction with 128 nM TnpAΔ(147-193) was included. The location of residue 146 at the C-terminus of this mutant is shown in panel A.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/39611/elife-39611-fig7-figsupp1-v1.jpg)

**Figure 7—figure supplement 1.:** Binding of 1 to 64 nM full-length TnpA and Δ(147-193) to the IS1535 RE. TnpAΔ(147-193) forms complex 1, but not PECs, with the RE.

Cys162, within the helix E region, generated only about 40% disulfide-linked dimers upon oxidation (Figure 7A,B). Nevertheless, oxidized Cys162 was completely defective in PEC formation, whereas the reduced cysteine mutant was active (Figure 7E). In an additional experiment, we removed the entire helix E region. TnpAΔ(147-193), which contains residues up to the end of β4, was defective for PEC formation (Figure 7F). However, at very high protein concentrations a small amount of product migrating as a PEC is observed. Incubation of TnpAΔ(147-193) with the RE fails to generate PECs, as expected, but products migrating as complex 1 are formed (Figure 7—figure supplement 1), indicating the truncated protein remains active for forming this species. The properties of the helix E deletion mutant provide evidence that helix E performs an important function in cooperative binding to form PECs but probably not directly in synaptic interactions because a small amount of LE-LE PEC can form. The inability of the covalently-crosslinked E helices to assemble PECs suggests that a conformational rearrangement of the helix E region of the dimer is required, perhaps to enable helix E interactions between adjacent dimers bound to the transposon ends.

## Discussion

The IS607 family of DNA transposable elements exhibits many features that are not typically found in other transposable elements. The ends of IS607 elements are not bordered by terminal inverted repeated sequences, and there are no duplications of target sequence at the transposon-host DNA borders; however, multiple short sequence motifs internal to the ends are present (this paper, Blount and Grogan, 2005; Kersulyte et al., 2000). Most IS607-family members terminate in GG, and in the cases of IS607 and ISC1926, insert into a GG target sequence. IS607-family elements encode two orfs whose coding sequences encompass nearly all of the DNA between the transposon ends. For IS607, orfA/tnpA is necessary and sufficient for transposition in E. coli (this paper and Kersulyte et al., 2000). TnpA binds specifically to the transposon ends and is a member of the SR family of DNA exchange enzymes, which are most often associated with site-specific recombination reactions. Residues implicated in catalysis by SRs are well conserved within IS607-family TnpA proteins, and we demonstrate here that the presumed active site serine is required for transposition. Strikingly, however, the dimeric structure is radically different from other SRs. OrfB, whose presence appears to negatively impact IS607 transposition rates in E. coli (this paper and Kersulyte et al., 2000), may function as a negative regulator, or perhaps in an ancillary role such as DNA repair, in particular hosts (Kapitonov et al., 2015; Kersulyte et al., 2000). OrfB-like genes are often associated with IS605/608-family transposons, and OrfB (TnpB) from ISDra2 has also been reported to function as a negative regulator (Pasternak et al., 2013).

### Assembly and architecture of the paired-end complex

The first major step in a transposition reaction is formation of a paired-end (synaptic) complex leading to a chemically-active transpososome (Hickman and Dyda, 2015). We show that TnpAIS1535 binds in a robust and highly cooperative manner to multiple binding sites within the LE of the element and can efficiently recruit a second LE to generate a paired-end complex. Binding nucleates over four 9 bp directly-repeated motifs that are positioned in a helically-phased manner from about 20 to 60 bp from the IS1535 LE terminus (Figure 1B). Transposon sequences beginning at motif a (LE bp 21) through the conserved half of motif d (LE bp 54) are essential for efficient paired-end complex formation. However, additional non-specific DNA sequences extending to about 84 bp from the left end are required for efficient PEC assembly. Likewise, additional DNA extending from motif a to shortly beyond the transposon-host junction improves the efficiency of PEC assembly. Although this region contains motif e, which is spaced one bp closer to motif a than the spacing between motifs a-d, the presence of the motif e sequence has little discernable effect on PEC assembly. We find it surprising that the sequence identity of the terminal 19 bp of the LE does not significantly influence PEC formation.

Footprinting data on LE-TnpAIS1535 PEC complexes are consistent with the LE resections. TnpAIS1535 strongly binds over motifs a-d, but the overall region of binding extends from before motif e to about 75 bp from the LE terminus. Significantly, only very weak binding is evident at sequences surrounding the transposon-host junction where DNA chemistry must occur. PECs formed with LE substrates containing nonspecific sequences downstream of motif a actually exhibited greater protections from DNase I cleavage over the region that would be positioned at the transposon border, possibly implying that the native sequence near the LE terminus may be suboptimal for TnpA dimer binding. The boundaries of TnpA binding within LE PECs revealed by Exo III digestion support a model whereby multiple TnpA proteins coat long segments of the left ends. Initial Exo III stops indicate TnpA binding from 8 to 78 bp from the left end terminus. Profiles obtained upon increasing Exo III digestion are consistent with the exonuclease removing TnpA molecules bound to units of about 10 bp, revealing borders of the TnpA nucleoprotein filament from 8 and 18 (major) bp from the host junction extending to 78, 68 (major) and 59 bp within the element.

In contrast to the LE, the IS1535 RE is a poor substrate for TnpA binding. Only a small amount of RE-RE PECs or RE-LE PECs are detectable, although a complex 1 species is formed at high protein concentrations. Exo III footprinting shows that the RE complex 1 contains TnpA bound only to the two sequence motifs that are present between bp 10 and 28 from the RE-host junction. The significance of the differences in the IS1535 ends on its transposition reaction remains to be determined. However, the distribution of sequence motifs, along with our preliminary end binding experiments with TnpA from IS607 or ISC1926, suggests that this disparity is not present in these elements and thus may not be a general feature of IS607-family transposons.

The structures of the IS607-family TnpA catalytic domain dimers pose a number of questions with respect to how DNA binding and catalysis occur, especially in the light of the radically different oligomeric conformations of other SR family members. Whereas the catalytic domains of the smSRs oligomerize via interactions between their helix E regions, TnpA catalytic domains dimerize over their B and D helices. The helix E regions of TnpA dimers are split and folded into a physically separate four helix bundle that is attached to the catalytic domains by a flexible polypeptide linker. The helix E bundle would sterically exclude DNA from associating with the active site. Therefore, minimally, a reconfiguration of the helix E region would be required to enable DNA catalysis. In addition, the active site is located on the opposite side of the subunit from its DNA binding domain (see models below), raising the possibility that cleavage of the synapsed transposon end and/or target DNA may be in trans with respect to the DNA to which the N-terminal DBD is bound (Boocock and Rice, 2013), a recurring feature of transpososome structures (Hickman and Dyda, 2015). By contrast, smSRs cleave the half site to which they are bound (Boocock et al., 1995; Li et al., 2005). An additional paradoxical feature with respect to catalysis is that the active site serines in the TnpA dimer structures are separated by >25 Å, much too far to cleave on either side of the GG dinucleotide at the transposon ends and host target in a manner consistent with other SRs. These and other comparative features with smSRs make it likely that a large conformational change in the oligomeric structure of TnpA precedes DNA cleavage and exchange.

Nevertheless, we show here that the quaternary structure of the catalytic domain is active for assembling PECs, as evidenced by the robust formation of PECs by IS1535 TnpA dimers covalently crosslinked over the core subunit interface. However, the inability of dimers with covalently-linked E helices to cooperatively bind the LE and form PECs provides strong evidence that the helix E region does undergo conformational rearrangement during PEC assembly. An attractive model is that the helix E regions from adjacent dimers remodel to interact with each other during the cooperative loading of proteins along the transposon end. IS1535 TnpA proteins deleted for the entire helix E region appear competent to form PECs at very high protein concentrations, supporting a role for a remodeled helix E in promoting cooperative binding between dimers bound laterally along the transposon ends. The finding that a small amount of PECs appear to still form when the entire helix E region is deleted suggests that helix E is not directly required for synaptic interactions.

Proteolysis experiments and structure modeling suggests that winged-helix DNA binding domains are linked to the N-terminal end of the catalytic domain by peptide chains ranging in length from just three residues (ISC1926) to about 10 residues (IS1535). Structural models of DNA-bound TnpAISC1926 dimers, where there is predicted to be less conformational freedom between the DBD and catalytic domains, are shown in Figure 8. In panel A, the recognition α-helices of the two DBDs are inserted into the major groove of a DNA model of the IS1535 LE segment containing motifs a and b at positions consistent with protections from dimethyl sulfate reactivity at guanines by TnpAIS1535 (Figure 8—figure supplement 1). The N-termini of the catalytic domains of the TnpAIS1535 and TnpAISC1926 dimers are separated by a distance that is close to the pitch of B DNA. Thus, the two DBDs can readily fit into adjacent major groove segments on the same helical face even with the short three residue linker that is present in TnpAISC1926.

![Figure 8.](https://cdn.elifesciences.org/articles/39611/elife-39611-fig8-v1.jpg)

**Figure 8.:** (A) Model of a TnpA dimer in a configuration where the two DBDs are binding to LE motifs a and b (orange DNA) in a manner consistent with DMS protection data (Figure 8—figure supplement 1) and where the wing is over the A/T-rich minor groove. Guanine N7 atoms protected from DMS reactivity by bound TnpA are highlighted as blue spheres. The tandem G/C base pairs at the LE terminus are red and the host DNA is green. The TnpA dimer model is derived from the Phyre2 model of the TnpAISC1926 NTD (Figure 2—figure supplement 1C) linked by three residues to the TnpAISC1926 CTD X-ray structure. We posit this conformation on DNA represents complex 1 (see Figure 8—figure supplement 4). (B) TnpA dimer configuration where only one DBD is associated with a single end. The dimer is rotated orthogonally about the DBD-CTD linker in relation to the dimer in panel A. (C) Four TnpA dimers are bound as in panel B to motifs a-d on one LE. The helix E regions are proposed to engage in helix-swapped interactions between adjacent dimers (e.g., Figure 8—figure supplement 2) to promote cooperative binding. This structure, with additional dimers bound laterally along the LE, may reflect complex 2. (D) Model in panel (C) rotated to show the DNA in an end-on view, highlighting the set of unbound DBDs. (E) Model of the PEC with a second LE associated. Although represented as parallel straight DNAs, the two transposon ends may be in a more interwrapped structure. TnpA protomers in a different, chemically-active, conformation are proposed to be recruited to the end of the filament at the transposon-host junction.

![Figure 8—figure supplement 1.](https://cdn.elifesciences.org/articles/39611/elife-39611-fig8-figsupp1-v1.jpg)

**Figure 8—figure supplement 1.:** An LE probe end labeled on the G-rich bottom strand was incubated with 0, 32, 64, and 128 nM TnpAIS1535 for 1 hr under PEC assembly conditions and then reacted with DMS. The first four lanes are dideoxy sequencing reactions and the next four lanes are DMS reactions without and with TnpA. Guanines within motifs a-c that are protected from DMS modification, and therefore cleavage by piperidine, are highlighted with asterisks and circled. Carets (^) indicate guanines exhibiting moderately increased reactivity with DMS. LE-1 is the first base of the left end. Dideoxy-terminated or piperidine-cleaved DNA fragments migrate slightly differently.

![Figure 8—figure supplement 2.](https://cdn.elifesciences.org/articles/39611/elife-39611-fig8-figsupp2-v1.jpg)

**Figure 8—figure supplement 2.:** The C-terminal segments (arrows) of the E helices are swapped with neighboring dimers. The DNA in this model has an average helical twist of 34.2° corresponding to 10.52 bp/turn.

![Figure 8—figure supplement 3.](https://cdn.elifesciences.org/articles/39611/elife-39611-fig8-figsupp3-v1.jpg)

**Figure 8—figure supplement 3.:** (A) An IS1535 substrate was generated by PCR that contains 59 bp of pUC18 fused to 91 bp of LE DNA plus 37 bp of flanking host DNA that terminates at an EcoR1 site. Digestion with EcoR1 and ligation generates a 380 bp product (IR) containing two LEs in an inverted orientation, which was gel purified and then 5′ end-labeled with 32P using polynucleotide kinase and γ-32P-ATP. Incubation of the IR with TnpAIS1535 is predicted to generate a PEC if the LEs align in a parallel manner, as illustrated. An interwrapped parallel configuration of the LEs that allows for a similar looped extension of the intervening host DNA, rather than an elongated structure as schematically pictured, is also compatible with PEC formation. The length of the intervening loop used in the IR substrate in panel C is 80 bp from the LE termini or 116 bp from the primary Exo I digestion stop site next to motif a (Figure 4B E). (B) Schematic representation of a PEC formed on the starting DNA fragment in panel A with LEs synapsed in an antiparallel configuration. This configuration is incompatible with formation of a PEC with the ends of the host DNA covalently joined after ligation. Moreover, footprinting data provide no evidence for TnpA binding to the host DNA as drawn (note that motif d ends at bp 59, whereas only 37 bp of host DNA are present). (C) PEC formation on the IR substrate. The first four lanes were incubation of 0, 8, 16, and 32 nM TnpAIS1535 with the unligated substrate (panel A top) and next four lanes were with the IR substrate. The IR-PEC, which migrates similarly to the LE-LE PEC, provides evidence for a parallel configuration of the LEs (panel A). These reactions were performed with 2% of the standard amount of substrate DNA to favor intramolecular synapsis. Bimolecular products formed on the IR substrate may be present in the wells.

![Figure 8—figure supplement 4.](https://cdn.elifesciences.org/articles/39611/elife-39611-fig8-figsupp4-v1.jpg)

**Figure 8—figure supplement 4.:** (A) If TnpA binds as a dimer to form complex I, then either TnpA (MW 21.9 kDa) or TnpA-MBP (MW 65.5 kDa) dimeric forms would bind to motifs a and b as represented in Figure 8A to generate complex one with different electrophoretic migrations. (B) If TnpA binds to motifs a and b as a tetramer (two dimers) to form complex I, then a band of intermediate mobility consisting of the two different dimers should form, which is not observed in panel C. (C) EMSA assay on LEΔ54, which only gives complex I. In lanes 2 – 5, LEΔ54 was incubated with 8, 16, 32, and 64 nM TnpA, respectively. In lanes 14 – 17, LEΔ54 was incubated with 16, 32, 64 and 128 nM TnpA-MBP, respectively. In lanes 6 – 13, LEΔ54 was incubated with 32 nM of TnpA. plus 8 to 256 nM TnpA-MBP in 2-fold increasing amounts. No subunit mixing between dimers is evident during the time frame of the experiment.

An alternative arrangement is shown in Figure 8B where only one subunit of the dimer binds to a motif on an individual transposon end, leaving the other subunit free to bind a second DNA. In this model, additional dimers would bind in a similar manner to adjacent motifs (Figure 8C) with binding stabilized by remodeling of the helix E regions to generate intermolecular contacts between dimers (e.g., Figure 8—figure supplement 2). This dimer binding configuration accounts for the cooperative assembly of TnpA units covering about 10 bp each, as evidenced in the Exo III footprints. Most importantly, it accounts for the near simultaneous recruitment of both DNA ends into a PEC; a TnpA dimer array on a single transposon end will have an array of appropriately spaced free DBDs (Figure 8D) ready to capture a second unbound transposon end with high affinity (Figure 8E). The parallel arrangement of ends in the PEC is consistent with PEC assembly by a substrate containing two inverted copies of IS1535 LEs separated by only 80 bp (Figure 8—figure supplement 3).

We suggest that complex 1, which is formed in vitro at high TnpA concentrations and does not appear to be a precursor to the PEC (Figure 3A–D), has a TnpA dimer bound in the conformation depicted in Figure 8A. In support of this, a mixture of IS1535 TnpA and TnpA-MBP dimers to a LE deletion substrate that only forms complex I generates only DNA-bound products representing the two homodimers (Figure 8—figure supplement 4). If complex 1 consisted of two dimers bound as in Figure 8B, a heterotetrameric species that would migrate between the complexes formed by the separate dimer reactions would also be expected.

Complex 2, which also contains only one transposon end, is observed only at very high concentrations of TnpA relative to transposon ends (Figure 3A,B). The presence of complex 2 is correlated with a decrease of PECs as the TnpA to transposon end ratio increases (Figure 3A,B,F). We propose that this complex has dimers bound along individual LEs as in Figure 8C,D, but unbound transposon ends are unavailable to generate a PEC, consistent with a model whereby TnpA bound to one end captures a second unbound end. Alternatively, complex 2 could have two dimers bound in the conformation in Figure 8A to motifs a-d.

### Comparison with other transpososome structures

Many transposases, for example Tn5, function as dimers where each subunit associates with the short terminal inverted repeats of both DNA ends within the assembled transpososome (Davies et al., 2000). However, some transposases utilize multiple binding sites within longer end segments, and in some cases, contain distinct DNA binding domains. For example, each subunit of the Mos1 Mariner-family transposase dimer binds to one transposon terminus and additional separate DNA binding domains associate with two subterminal binding sites on the other transposon end within the active complex (Richardson et al., 2009). Assembly of the phage Mu transpososome, which contains four copies of the Mu A protein, is more complex as it involves interactions with a remote enhancer-like element by a distinct DNA binding domain (Harshey, 2014). hAT-family transposons often have many subterminal repeats at variable spacings and orientations, which in some elements, can be located hundreds of base pairs from the transposon termini (Atkinson, 2015). The transposase from the hAT element Hermes is a preassembled donut-shaped octamer that is proposed to bind to four subterminal repeats on each end along with the transposon termini using distinct DNA binding regions (Hickman et al., 2014). The presence of subterminal repeats on hAT-family elements bears some similarity to the sequence motifs of IS607-family transposon ends, but the manner of transposase binding and synapsis proposed here for IS1535 is different.

### Current understanding of the IS607-family transposition reaction

We propose the following pathway for formation of the paired-end complex that is expected to be a critical early intermediate in the IS607-family transposition reaction. Multiple TnpA dimers are initially targeted to DNA motifs that can be located over 60 bp from the transposon end (Figure 1B). In the case of the IS1535 LE, four dimers cooperatively bind over four helically-phased motifs beginning 20 bp from the end (Figure 8C), and the nucleoprotein filament continues to spread in a largely sequence-neutral manner to cover at least 70 bp. The active sites are positioned well away from the DNA in the filament, avoiding any spurious cleavage. The single-end complex then captures an unbound end to generate a stable PEC (Figure 8D,E). Because formation of the PEC is relatively slow (Figure 3C,D), we imagine that initial binding to a IS1535 LE limits the rate of PEC formation, but once the single-end filament is formed, an unbound end is rapidly captured. Although we illustrate this complex as two parallel transposon ends, a more interwrapped structure may form. No quaternary change in the dimer structure over the catalytic core domain is required for PEC assembly, but our evidence indicates that the helix E region remodels to facilitate cooperative assembly of the nucleoprotein filament. Most all IS607-family transposon ends have multiple motifs (the IS1535 RE is an exception with only two), but they are not always spaced by increments of 10 – 11 bp (Figure 1B). The flexible peptide linkers between the DBD and catalytic domains and between the catalytic domains and helix E regions may enable similar nucleoprotein filaments to assemble, even if some of the recognition motifs are not in helical phase.

Whereas an 80 bp segment within the IS1535 LE beginning near the transposon terminus is required for maximally efficient PEC assembly, only very weak TnpA binding is observed over the transposon-host DNA junction where TnpA-mediated chemistry on DNA must occur. For the reasons discussed above, and because the active sites in the solution dimer are not positioned appropriately with respect to the terminal GG cleavage sites, an alternate conformation of TnpA is almost certainly required for DNA catalysis. Recruitment of TnpA in a catalytically-active conformer may be a key regulatory step and could require co-translational synthesis or folding localized to a preformed PEC (Duval-Valentin and Chandler, 2011). This could explain the requirement in vivo for the IS607 tnpA gene to be located close to the transposon ends for transposition to occur (Kersulyte et al., 2000) (W.C. and R.C.J., unpublished). Thus, correct assembly of the PEC, with the two transposon ends in correct register, may be a prerequisite or checkpoint for recruiting catalytically-active subunits to bind to the junction, or alternatively, for allosterically activating weakly bound subunits over the junction.

In addition to the structure of the recombination complex, the steps of DNA exchange by serine transposases may also be quite different from other SRs. A subunit rotation mechanism for strand exchange on the complex depicted in Figure 8E would lead to an intramolecular inversion, not transposition. Instead, we suggest that the element may excise from the donor site and then insert into a target locus using serine chemistry without strand transfer coupled to subunit rotation. It is also possible that capture of the target locus could be a prerequisite for DNA cleavage. Because both transposon ends need to recombine into a single GG target, it seems likely that the strand transfer reactions must occur sequentially. As none of these DNA cleavage–transfer steps would necessarily require a subunit rotation reaction, the structure of chemically-active TnpA oligomers may be very different from other SRs that have been trapped in tetrameric structures competent for DNA exchange by subunit rotation.

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
      <td>Gene (Mycobacterium tuberculosis)</td>
      <td>IS1535 orfA/tnpA</td>
      <td>H37Rv genome DNA</td>
      <td>Gene ID: RV0921</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (Helicobacter pylori)</td>
      <td>IS607 orfA/tnpA</td>
      <td>synthetic gene</td>
      <td>NCBI protein ID: AAF05600.1</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (Helicobacter pylori)</td>
      <td>IS607 orfB</td>
      <td>synthetic gene</td>
      <td>NCBI protein ID: WP_001274345.1</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (Sulfolobus islandicus)</td>
      <td>ISC1926 orfA/tnpA</td>
      <td>S. islandicus genome DNA, PMID: 15612937</td>
      <td>NCBI protein ID: AAV87873.1</td>
      <td>S. islandicus  pyrE::ISC1926 Dennis Grogan, University of Cincinnati</td>
    </tr>
    <tr>
      <td>Strain, strain background (E. coli)</td>
      <td>RJ1224</td>
      <td>Laboratory collection</td>
      <td>recA56, srl, Δ(pro-lac), ara, rpsL, λbbnin [λ cI857,b515, b519, nin5, Sam7]</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (E. coli)</td>
      <td>Hfl-1</td>
      <td>PMID: 4352176</td>
      <td>hfl-1, fhuA2::IS2, lacY1, tsx-1, glnX44, gal-6, xyl-7, mtlA2, mut-14</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (E. coli)</td>
      <td>LE392</td>
      <td>PMID: 6291786</td>
      <td>hsdR514 (rk–, mk+), glnX (supE44), tyrT (supF58), Δ(codB-lacI)3, galK2, galT22, metB1, trpR55</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (E. coli)</td>
      <td>BW14879</td>
      <td>PMID: 2160940</td>
      <td>pMW11 Muc62 Δ(lac)X74, Δ(phoA532 Pvull) phn(EcoB), arcA1655, fnr-1655</td>
      <td>B. Wanner, Purdue University</td>
    </tr>
    <tr>
      <td>Strain, strain background (E. coli)</td>
      <td>BW5104</td>
      <td>PMID: 2160940</td>
      <td>Mu-1 Δlac169, creB510, hsdR514</td>
      <td>B. Wanner, Purdue University</td>
    </tr>
    <tr>
      <td>Strain, strain background (E. coli)</td>
      <td>RJ3960</td>
      <td>This work</td>
      <td>BW5104 λR mal</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (E. coli)</td>
      <td>RJ3388</td>
      <td>Laboratory collection</td>
      <td>BL21 (DE3) endA::tet8, fis::str/spc-985</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (E. coli)</td>
      <td>RJ3431</td>
      <td>Laboratory collection</td>
      <td>BL21 (DE3) metC::Tn10</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>See supplementary file 2</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>See supplementary file 3</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>DNase I</td>
      <td>Thermo Fisher, Waltham, MA</td>
      <td>Catalog number: EN0521</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>Exonuclease III</td>
      <td>NEB, Ipswich, MA</td>
      <td>Catalog number: M0206L</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>Proteinase K</td>
      <td>Roche, Germany</td>
      <td>Catalog number: 03115828001</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>Trypsin</td>
      <td>Promega, Madison, WI</td>
      <td>Catalog number: V511A</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Sequenase Quick-Denature Plasmid Sequencing Kit</td>
      <td>Affymetrix, Santa Clara, CA</td>
      <td>Catalog number: 70140</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Coomassie ProteinAssay Reagent</td>
      <td>Thermo Fisher, Waltham, MA</td>
      <td>Catalog number: 1856209</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Dimethyl sulfate</td>
      <td>Thermo Fisher, Waltham, MA</td>
      <td>Catalog number: AC430831000</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Piperidine</td>
      <td>Sigma-Aldrich</td>
      <td>Catalog number: 10409–4</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Diamide</td>
      <td>Sigma-Aldrich</td>
      <td>Catalog number: 87751</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>AEBSF</td>
      <td>Gold Biotechnology</td>
      <td>Catalog number: A-540–1</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>ImageQuant</td>
      <td>GE Healthcare</td>
      <td>RRID:SCR_014246</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>PyMOL Molecular Graphics System</td>
      <td>Schrodinger, LLC</td>
      <td>RRID:SCR_000305</td>
      <td>https://pymol.org/2/</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Protein Prospector/MS-Digest</td>
      <td>http://prospector.ucsf.edu/prospector/cgi-bin/msform.cgi?form=msdigest</td>
      <td>RRID:SCR_014558</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Phyre2</td>
      <td>PMID: 25950237</td>
      <td>RRID:SCR_010270</td>
      <td>www.sbg.bio.ic.ac.uk/phyre2/</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>XDS</td>
      <td>PMID: 20124692</td>
      <td>RRID:SCR_015652</td>
      <td>http://xds.mpimf-heidelberg.mpg.de/</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>PHASER</td>
      <td>PMID: 19461840</td>
      <td>RRID:SCR_014219</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>SHELX</td>
      <td>doi.org/10.1107/S0021889804018047</td>
      <td>RRID:SCR_014220</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Coot</td>
      <td>PMID: 15572765</td>
      <td>RRID:SCR_014222</td>
      <td>https://www2.mrc-lmb.cam.ac.uk/personal/pemsley/coot/</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Phenix</td>
      <td>PMID: 20124702</td>
      <td>RRID:SCR_014224</td>
      <td>https://www.phenix-online.org/</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Buster</td>
      <td>PMID: 22505257</td>
      <td>RRID:SCR_015653</td>
      <td>https://www.globalphasing.com/buster/</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>CCP4</td>
      <td>PMID: 21460441</td>
      <td>RRID:SCR_007255</td>
      <td>http://www.ccp4.ac.uk/</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Procheck</td>
      <td>doi.org/10.1107/S0021889892009944</td>
      <td>RRID:SCR_006511</td>
      <td>https://www.ebi.ac.uk/thornton-srv/software/PROCHECK/</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Clustal Omega</td>
      <td>https://www.ebi.ac.uk/Tools/msa/clustalo/</td>
      <td>RRID:SCR_001591</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Strains and plasmids

E. coli strain genotypes are given in Supplementary file 1. ISC1926 was amplified from S. islandicus pyrE::ISC1926 genomic DNA (gift of D. Grogan), and IS1535 was amplified from Mycobacterium tuberculosis H37Rv genomic DNA (gift of D. Eisenberg). Synthetically-derived IS607 orfA and orfB sequences (E. coli codon optimized, Genewiz, South Plainfield, NJ), along with all plasmids used in this work and details of their constructions, are given in Supplementary file 2 and 3.

### Transposition assays

RJ1224 (recA λbbnin [λcI857 b515 b519 nin5 Sam7]) containing pBR322 with an IS607-tet derivative was grown at 30°C in 2 x YT and 10 µg/ml tetracycline. λ lysates were obtained upon shifting the culture to 42°C for 20 min and then to 37°C for 3 hr to allow phage development. Lysates were titered on LE392 (supF) and used to transduce early stationary phase LB cultures of the high frequency lysogenizing strain Hfl-1 (Belfort and Wulff, 1973) at a multiplicity of infection of about 0.3. After 20 min at 30°C, 2 volumes of LB were added, and incubation continued for 60 min. Cells were plated onto LB +10 µg/ml tetracycline, and the number of TetR (AmpS, temperature-sensitive) transductants per plaque forming unit (PFU) were scored as transposition events.

λ genomic fragments containing IS607-tet were transferred to plasmids for DNA sequencing by the in vivo mini-Mu cloning method (Groisman and Casadaban, 1986). Lysates of the Hfl-1 λbbnin::IS607-tet transductants were used to lysogenize BW14879 containing the mini-Mu cloning plasmid pMW11 (str/spcR) and Muc62 (Metcalf et al., 1990). Mini-Mu lysates were prepared by thermal-induction and used to infect RJ3960, a λR derivative of BW5104 selected as a maltose non-fermenting survivor after λcI- b221 infection. After growth for 60 min at 30°C the cells were plated on LB +10 µg/ml tetracycline and 25 µg/ml streptomycin. Plasmid DNA from TetR, StrR colonies were sized on agarose gels, and plasmids < 15 kb were subjected to DNA sequencing using primer oRJ878 that reads out from the left end of IS607. The sequence identified the insertion position on the λ genome, and insertion-specific λ primers flanking the transposon were then used to amplify the region from the original λ::IS607-tet lysate as a template and to sequence the right junction using primer oRJ879 that reads out from the right end of IS607-tet. All amplicon sizes were consistent with simple insertions.

### Purification of TnpA and TnpA-CTD

TnpA proteins were expressed in RJ3388 in 2xYT at OD600 = 1 with 0.4 mM IPTG for ~16 hr at 15°C. Cells expressing full-length proteins were lysed in 25 mM MES-NaOH, pH 6.0, 300 mM NaCl, 5 mM β-mercaptoethanol (βME), 5 mM EDTA, and 10% glycerol by three passes through a French Press. Clarified extracts were batch incubated with SP Sepharose Fast Flow resin (GE Healthcare, Chicago, Illinois) for 2 hr at 4°C, the resin was washed extensively with lysis buffer containing 400 mM NaCl, and protein was eluted with 50 mM HEPES, pH 7.5, 1 M NaCl, 10% glycerol, and 5 mM βME. The partially purified TnpA was then bound to Ni-NTA agarose (Goldbio, St. Louis, Missouri) in the same buffer. The resin was washed with Buffer A (25 mM HEPES, pH 7.5, 1 M NaCl, 5 mM βME, and 10% glycerol) + 50 mM imidazole, and TnpA was eluted with Buffer A + 500 mM imidazole. Batch chromatography was used to avoid protein precipitation upon elution. TnpA was dialyzed into storage buffer (25 mM HEPES, pH 7.5, 1 M Na acetate, 5 mM βME, and 50% glycerol) and stored at −20°C or at −80°C after quick freezing.

RJ3388 expressing the TnpA-CTD were lysed by French Press in Buffer A (50 mM MOPS, pH 7.0, 1 M NaCl, 25 mM imidazole, 5 mM βME, and 10% glycerol). For Se-methionine (Se-met) labeling, RJ3431 (metC) containing pRJ3347 was grown in M9 glucose +20 µg/ml methionine to an OD600 = 1.5. Cells were chilled and transferred to M9 glucose, incubated for 20 min at 15°C followed by addition of 60 µg/ml Se-met and 0.4 mM IPTG. Clarified extracts were incubated with Ni-NTA resin, washed in Buffer A + 50 mM imidazole, and eluted in Buffer B (50 mM MES-NaOH, pH 6.0, 5 mM βME, 10% glycerol) plus 500 mM NaCl and 250 mM imidazole. Eluted proteins were mixed with an equal volume of Buffer B and then incubated with SP Sepharose Fast Flow for 2 hr. The resin was washed with Buffer B + 400 mM NaCl, and near pure TnpA-CTD eluted in Buffer B + 1 M NaCl. The protein was concentrated with an Amicon Ultra-15 centrifugal filter (3 K Da cutoff, MilliporeSigma, Burlington, MA) and applied to a Superdex 75 (16/600; GE Healthcare) column on an FPLC in Buffer B + 1 M NaCl. The peak fractions containing the CTD were pooled, exchanged into crystallization buffer, and concentrated.

### Domain mapping by limited proteolysis and mass spectrometry

IS607 and IS1535 TnpA (3 µg) were incubated in 20 µl 25 mM HEPES (pH 7.5), 300 mM NaCl, 10% glycerol and 5 mM 2-mercaptoethanol at 37°C with 50 ng trypsin (Promega, Madison, WI) for varying times up to 30 min. TnpAISC1926 reactions were identical except that 10 mM CaCl2 was included in the cleavage buffer, and 100 ng of trypsin was added. Proteolysis reactions were quenched with 5 mM AEBSF (4-(2-aminoethyl)benzenesulfonyl fluoride hydrochloride; Sigma-Aldrich, St. Louis, MO), and subjected to 18% SDS-PAGE in Tricine buffer with 10% glycerol in the separating gel and stained with Coomassie Blue. Aliquots were analyzed by MALDI-TOF-MS on an Applied Biosystems Voyager DE-STR instrument operated in positive ion mode with and without the reflectron. Upon testing several matrices, sinapinic acid was found to yield the best mass spectra. Peptide molecular weights were compared to all trypsin cleavage products calculated for the protein using the MS-Digest tool in Protein Prospector (http://prospector.ucsf.edu/prospector/cgi-bin/msform.cgi?form=msdigest) to determine most likely endpoints.

### Electrophoretic (gel) mobility shift assays

TnpAIS1535 binding reactions were performed in 20 µl 25 mM HEPES, pH 7.5, 150 mM Na acetate, 5 mM Mg acetate, 1 mM DTT, 500 µg/ml BSA, 5% glycerol, 25 µg/ml sonicated salmon sperm DNA (Rockland, Limerick, PA)+1 nM 32P-labeled DNA probe. DNA probes were generated by PCR with LE or RE specific primers using pRJ3234 (IS1535 LE) or pRJ3348 (IS1535 RE) as the template (Supplementary file 2 and 3) and PAGE purified. The standard 149 bp LE probe (91 bp LE side, 58 bp host side) used in Figures 3 and 7 was generated using oRJ839 and oRJ840. A portion was end-labeled with γ-32P-ATP (Perkin Elmer, Waltham, MA) and polynucleotide kinase (NEB) and free label removed with a G-50 Micro column (GE Healthcare). Labeled probe was added to unlabeled probe to generate 1 nM in the binding reaction. Freshly diluted TnpA in 25 mM HEPES, pH 7.5, 1 M Na acetate, 1 mM DTT, 500 ug/ml BSA, and 20% glycerol was added to the binding mixture and typically incubated at 37°C for 60 min before applying to a 6% polyacrylamide (acrylamide:bisacrylamide 37.5:1) in 25 mM Tris-acetate, pH 7.5, and 1 mM Mg acetate (gel and running buffer). Electrophoresis was typically at 3.5 v/cm for 12 hr at 23°C. TnpAIS1535 proteins were oxidized for disulfide crosslinking by incubation at 4°C overnight in 25 mM HEPES, pH 7.5, 1 M Na acetate, 20% glycerol and 0.2 mM diamide, and the binding buffer contained 0.2 mM diamide in place of DTT. A Typhoon phosphorimager was used for image acquisition, and analysis was performed with ImageQuant (GE Healthcare).

### Nuclease and chemical probing of TnpA complexes

Binding reactions were the same as for the EMSAs except that the labeled probe was generated by amplifying pRJ3234 (IS1535 LE), pRJ3348 (IS1535 RE) (Figure 4 and Figure 8—figure supplement 1) or pRJ3352 (Figure 6) with 5′-labeled oRJ880 or oRJ881. After 60 min incubation at 37°C with TnpAIS1535, DNase I (0.02 u, Thermo Fisher, Waltham, MA) or Exonuclease III (10 u, NEB, Ipswich, MA) was added for 30 s or 5 min, respectively. Reactions were quenched with 150 mM Tris-HCl, pH 8.5, 10 mM CDTA, 0.8% SDS, and 12.5 µg/ml proteinase K and incubated 10 min at 65°C. The DNA was ethanol-precipitated, dissolve in formamide-NaOH dye and electrophoresed through 6% acrylamide-urea sequencing gels in TBE. Dimethyl sulfate reactions (10 mM, 30 s) under the same binding conditions and DNA cleavage with piperidine were performed essentially as described (Shaw and Stewart, 1994). Sequence ladders were generated using the Sequenase Quick-Denature Plasmid Sequencing Kit (Affymetrix, Santa Clara, CA).

### Crystallization and structure determination

The best diffracting crystals of TnpAISC1926 CTD were obtained using the hanging drop method by mixing equal volumes of a 10 mg/ml protein solution in 20 mM MOPS, pH 7.0, 100 mM Na-acetate, 0.1 mM DTT with a reservoir solution containing 8% (v/v) tacsimate, pH 4.0, and 20% (w/v) PEG3350. Crystals grew at 25°C, and although additional cryoprotectants were screened, they show no increase in diffraction relative to the drop solution alone. For TnpAIS1535 CTD, optimal crystals were grown by mixing equal volumes of a 5 – 9 mg/ml protein solution in 0.3 M sodium acetate, pH 5.0, and 1 mM TCEP with a reservoir solution containing 0.2 M sodium citrate + 20% (w/v) PEG3350. Crystals were cryoprotected in reservoir solution plus 30% glycerol.

All X-ray diffraction data were collected at 100 K at the Advanced Photon Source (Chicago IL) beamline 24-ID-C on a DECTRIS-PILATUS 6M detector. TnpAISC1926 CTD data were collected to 2.9 Å and integrated and scaled with XDS (Kabsch, 2010). The phases were solved by molecular replacement with PHASER (McCoy et al., 2007) using 3LHK chain D as the search model. Model building and refinement were performed using Coot (Emsley and Cowtan, 2004), PHENIX (Adams et al., 2002), and BUSTER (Smart et al., 2012). TnpAIS1535 CTD native and Se-met data were both collected to 2.5 Å resolution, and integrated and scaled using XDS. MAD phases were calculated from six selenium atoms with HKL2MAP (Pape and Schneider, 2004). Automatic model building was performed with BUCCANEER (Winn et al., 2011), which traced approximately 90% of the two chains. This model was then used to continue model building and refinement on the native dataset using Coot and BUSTER. X-ray data and refinement statistics are given in Table 1; the PDB code for the TnpAISC1926 CTD is 6DGC and for TnpAIS1535 CTD is 6DGC. Molecular graphics images of the structures were produced with PyMOL (Schrödinger, https://pymol.org/2/).

### Modeling

Structure models of the N-terminal domains were generated by Phyre2 (Kelley et al., 2015). A structural model of an intact TnpAISC1926 dimer was generated from the Phyre2 model of the TnpAISC1926 NTD (residues 12 – 61, Figure 2—figure supplement 2C) linked to residue 65 of the CTD by the native residues Arg-Glu-Glu using Coot. The NTD was docked onto a DNA model (3DNA, [Lu and Olson, 2003]) of the IS1535 LE sequence with the aid of the closely related RacA-DNA complex (Figure 2—figure supplement 2C) and DMS protection data (Figure 8—figure supplement 1) using PyMOL and Coot.
