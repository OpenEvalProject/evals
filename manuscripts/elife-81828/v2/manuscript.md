# Drosophila SUMM4 complex couples insulator function and DNA replication control

## Authors

- Evgeniya N Andreyeva<sup>1</sup>
- Alexander V Emelyanov<sup>1</sup>
- Markus Nevil<sup>2</sup>
- Lu Sun<sup>3</sup>
- Elena Vershilova<sup>1</sup>
- Christina A Hill<sup>4</sup>
- Michael-C Keogh<sup>3</sup> ([ORCID: 0000-0002-2219-8623](https://orcid.org/0000-0002-2219-8623))
- Robert J Duronio<sup>4</sup>
- Arthur I Skoultchi<sup>1</sup>
- Dmitry V Fyodorov<sup>1</sup> ([ORCID: 0000-0002-3080-1787](https://orcid.org/0000-0002-3080-1787)) †

### Affiliations

1. Department of Cell Biology, Albert Einstein College of Medicine Bronx United States ([ROR:05cf8a891](https://ror.org/05cf8a891))
2. UNC-SPIRE, University of North Carolina Chapel Hill United States ([ROR:0130frc33](https://ror.org/0130frc33))
3. EpiCypher Durham United States ([ROR:021skqj79](https://ror.org/021skqj79))
4. Integrative Program for Biological and Genome Sciences, University of North Carolina at Chapel Hill Chapel Hill United States ([ROR:0130frc33](https://ror.org/0130frc33))
5. Lineberger Comprehensive Cancer Center, University of North Carolina Chapel Hill United States ([ROR:0130frc33](https://ror.org/0130frc33))
6. Department of Biology, University of North Carolina Chapel Hill United States ([ROR:0130frc33](https://ror.org/0130frc33))
7. Department of Genetics, University of North Carolina Chapel Hill United States ([ROR:0130frc33](https://ror.org/0130frc33))

† Corresponding author

## Abstract

Asynchronous replication of chromosome domains during S phase is essential for eukaryotic genome function, but the mechanisms establishing which domains replicate early versus late in different cell types remain incompletely understood. Intercalary heterochromatin domains replicate very late in both diploid chromosomes of dividing cells and in endoreplicating polytene chromosomes where they are also underreplicated. Drosophila SNF2-related factor SUUR imparts locus-specific underreplication of polytene chromosomes. SUUR negatively regulates DNA replication fork progression; however, its mechanism of action remains obscure. Here, we developed a novel method termed MS-Enabled Rapid protein Complex Identification (MERCI) to isolate a stable stoichiometric native complex SUMM4 that comprises SUUR and a chromatin boundary protein Mod(Mdg4)-67.2. Mod(Mdg4) stimulates SUUR ATPase activity and is required for a normal spatiotemporal distribution of SUUR in vivo. SUUR and Mod(Mdg4)-67.2 together mediate the activities of gypsy insulator that prevent certain enhancer–promoter interactions and establish euchromatin–heterochromatin barriers in the genome. Furthermore, SuUR or mod(mdg4) mutations reverse underreplication of intercalary heterochromatin. Thus, SUMM4 can impart late replication of intercalary heterochromatin by attenuating the progression of replication forks through euchromatin/heterochromatin boundaries. Our findings implicate a SNF2 family ATP-dependent motor protein SUUR in the insulator function, reveal that DNA replication can be delayed by a chromatin barrier, and uncover a critical role for architectural proteins in replication control. They suggest a mechanism for the establishment of late replication that does not depend on an asynchronous firing of late replication origins.

## Introduction

Replication of metazoan genomes occurs according to a highly coordinated spatiotemporal program, where discrete chromosomal regions replicate at distinct times during S phase (Rhind and Gilbert, 2013). The replication program follows the spatial organization of the genome in Megabase-long constant timing regions interspersed by timing transition regions (Marchal et al., 2019). The spatiotemporal replication program exhibits correlations with genetic activity, epigenetic marks, and features of 3D genome architecture and subnuclear localization. Yet the reasons for these correlations remain obscure. Interestingly, the timing of firing for any individual origin of replication is established during G1 before pre-replicative complexes (pre-RC) are assembled at origins (Dimitrova and Gilbert, 1999), suggesting a mechanism that involves factors other than the core replication machinery.

Most larval tissues of Drosophila melanogaster grow via G-S endoreplication cycles that duplicate DNA without cell division, resulting in polyploidy (Zielke et al., 2013). Endoreplicated DNA molecules frequently align in register to form giant polytene chromosomes (Zhimulev et al., 2004). Importantly, in some cell types, genomic domains corresponding to the latest replicated regions of dividing cells, specifically pericentric (PH) and intercalary (IH) heterochromatin, fail to fully replicate during each endocycle resulting in underreplication (UR). These regions are depleted of sites for binding the Origin of Replication Complex (ORC), and thus, their replication primarily relies on forks progressing from external origins (Sher et al., 2012) in both dividing and endoreplicating cells, which suggests that both cell types utilize related mechanisms of regulation of late replication. Although cell cycle programs are dissimilar between endoreplicating and mitotically dividing cells (Zielke et al., 2013), they likely share the components of core biochemical machinery for DNA replication. Thus, underreplication provides a facile readout for late replication initiation and delayed fork progression.

The Suppressor of UnderReplication (SuUR) gene is essential for polytene chromosome underreplication in intercalary and pericentric heterochromatin (Belyaeva et al., 1998). In SuUR mutants, the DNA copy number in underreplicated regions is partially restored to almost reach those for fully polyploidized regions of the genome. SuUR encodes a protein (SUUR) containing a helicase domain with homology to that of the SNF2/SWI2 family. The occupancy of ORC in intercalary and pericentric heterochromatin is not increased in SuUR mutants (Sher et al., 2012), and, thus, the increased replication of underreplicated regions is likely not due to the firing of additional origins. Rather, SUUR negatively regulates the rate of replication fork progression (Nordman et al., 2014) by an unknown mechanism. It has been proposed (Posukh et al., 2015) that retardation of the replisome by SUUR takes place via simultaneous physical association with the components of the fork (e.g., CDC45 and PCNA) (Kolesnikova et al., 2013; Nordman et al., 2014) and repressive chromatin proteins, such as HP1a (Pindyurin et al., 2008).

Using a newly developed proteomics approach, we discovered that SUUR forms a stable stoichiometric complex with a chromatin boundary protein Mod(Mdg4)-67.2. We demonstrate that SUUR and Mod(Mdg4)-67.2 together are required for maximal underreplication of intercalary heterochromatin and full activity of the gypsy insulator, thereby implicating insulators in obstructing replisome progression and the control of late DNA replication.

## Results

### Identification of SUMM4, the native form of SUUR in Drosophila embryos

To determine how SUUR functions in replication control, we sought to identify its native complex. Previous attempts to characterize the native form of SUUR by co-IP or tag-affinity purification gave rise to multiple putative binding partners (Kolesnikova et al., 2013; Munden et al., 2018; Nordman et al., 2014; Pindyurin et al., 2008). However, evaluating whether any of these proteins are present in a native SUUR complex is problematic because of the low abundance of SUUR, which also precludes its purification by conventional chromatography. Therefore, we developed a novel biochemical approach using embryonic extracts (which can be obtained in large quantities) that relies on partial purification by multistep FPLC (fast protein liquid chromatography) (Figure 1A) and shotgun proteomics of chromatographic fractions by quantitative LCMS. We term this technology MERCI for MS-Enabled Rapid protein Complex Identification (‘Materials and methods’).

![Figure 1.](https://cdn.elifesciences.org/articles/81828/elife-81828-fig1-v2.jpg)

**Figure 1.:** (A) Schematic of FPLC purification of the native form of SUUR using MERCI approach. ILR, ion library obtained by information-dependent acquisitions (IDA) of recombinant FLAG-SUUR; IL1-5, ion libraries obtained by IDA of FPLC fractions from chromatographic steps 1–5. KPi, potassium phosphate, pH 7.6. (B) Representation of SUUR in ion libraries ILR and IL1-5 (Supplementary file 1). Total number of identified proteins and the confidence rank of SUUR among them as well as the total number of detected peptides (95% confidence) and the number of SUUR-specific peptides are shown. (C) Recombinant FLAG-SUUR expressed in Sf9 cells. Identities of eight most prominent bands were determined by mass-spectroscopy. p130 and p65 correspond to full-length and C-terminally truncated FLAG-SUUR, respectively (red arrows). Other bands represent common Sf9-specific contaminants purified by FLAG chromatography (blue dashed lines), cf. purified EGG-F (green arrow). Molecular mass marker bands are indicated (kDa). (D–H) SWATH quantitation profiles of SUUR fractionation across individual FPLC steps. Ion libraries (IL) used for SWATH quantitation are shown at the bottom of each panel. Z-scores across indicated column fractions are plotted; error bars, standard deviations (N = 3). Gray rectangles, fraction ranges used for the next FPLC step; in (G), black arrows, expected peaks of globular proteins with indicated molecular masses in kDa. (I) SWATH quantitation profiles of SUUR fractionation across five FPLC steps. IL5 ion library was used for SWATH quantification.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/81828/elife-81828-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) Schematic of SWATH quantification of recombinant SUUR, nuclear extract (starting material) and FPLC fractions for SUUR using ion library ILR. (B) SUUR titration curve obtained by SWATH quantitation of 10 fg to 1 µg recombinant FLAG-SUUR in the presence of 25 µg E. coli lysate; both axes are logarithmic (log10). Red rectangle, SUUR quantification in 25 µg nuclear extract; error bars, standard deviations (N = 3). (C) SWATH quantitation profiles of SUUR fractionation across individual FPLC steps. Ion library ILR was used for SWATH quantification, and relative amounts were converted to estimated ng SUUR per fraction. Error bars, standard deviations (N = 3); colored boxes, peak fractions of SUUR. (D) SUUR purification by FPLC. Total protein was measured by BCA assay, and SUUR was measured as in (C). Relative purity, purification factor in each step and cumulative purification factor are shown.

Shotgun quantification of complex mixtures of polypeptides by LCMS is performed in two steps. First, the composition of the mixture is examined by information-dependent acquisitions (IDA) that establish protein identities based on MS1 and MS2 spectra of detected tryptic peptides. This information is used to compile a so-called ‘ion library’ (IL), which is then utilized to quantify spectral information obtained from the same samples by unbiased, data-independent acquisitions (DIA), sometimes termed sequential window acquisitions of all theoretical mass spectra (SWATH-MS/SWATH). Importantly, the depth of proteomic quantification is limited by the range of peptides in the IL originally built by IDA.

SUUR-specific peptides could not be found in ILs obtained from acquisitions of crude nuclear extracts or any fractions from the first, phosphocellulose, step (IL1, Figure 1B, Supplementary file 1), and therefore, SUUR could not be quantified in SWATH acquisitions of phosphocellulose fractions when IL1 alone is used as a reference. Thus, to measure the relative abundance of SUUR in phosphocellulose fractions, we augmented IL1 with the IL obtained by IDA of recombinant SUUR (ILR, Figure 1B and C). In ion libraries from subsequent chromatographic steps (IL2–IL5), peptides derived from native SUUR were detected (Figure 1B, Supplementary file 1) and used for quantification of cognate DIA/SWATH acquisitions (Figure 1D–H).

The final aspect of the MERCI algorithm calls for re-quantification of FPLC fraction SWATH acquisitions with an IL from the last step (IL5) that is enriched for peptides derived from SUUR and co-purifying polypeptides (Figure 1A) and includes only 140 proteins (Figure 1B, Supplementary file 1). In this fashion, scarce polypeptides (including SUUR and, potentially, SUUR-binding partners) that may not be detectable in earlier steps will not evade quantification. Purification profiles of proteins quantified in all five FPLC steps (132) were then artificially stitched into 83-point arrays of Z-scores (Figure 1I, Supplementary file 2). These profiles were Pearson-correlated with that of SUUR and ranked down from the highest Pearson coefficient, PCC (Figure 2A). Whereas the PCC numbers for the bottom 130 proteins lay on a smooth curve, the top two proteins, SUUR (PCC = 1.000) and Mod(Mdg4) (PCC = 0.939) fell above the extrapolated (by polynomial regression) curve (Figure 2B). Consistently, SUUR and Mod(Mdg4) exhibited nearly identical purification profiles in all five FPLC steps (Figure 2C), unlike the next two top-scoring proteins, EGG (PCC = 0.881) and CG6700 (PCC = 0.874) (Figure 2—figure supplement 1A and B). Also, HP1a (PCC = 0.503), which had been proposed to form a complex with SUUR (Pindyurin et al., 2008) did not co-purify with SUUR in any FPLC steps (Figure 2—figure supplement 1C).

![Figure 2.](https://cdn.elifesciences.org/articles/81828/elife-81828-fig2-v2.jpg)

**Figure 2.:** (A) Pearson correlation of fractionation profiles for individual 132 proteins to that of SUUR, sorted from largest to smallest. Red box, the graph portion shown in (B). (B) Top 10 candidate proteins with the highest Pearson correlation to SUUR. Red dashed line, trend line extrapolated by polynomial regression (n = 5) from the bottom 130 proteins. (C) SWATH quantitation profiles of SUUR (red) and Mod(Mdg4) (cyan) fractionation across five FPLC steps, Figure 1I. IL5 ion library was used for SWATH quantification. (D) Western blot analyses of Superdex 200 fractions with SUUR and ModT antibodies, Figure 1G. Molecular mass markers are shown on the left (kDa). (E) Co-IP experiments. SUUR (red arrowhead) co-purifies from nuclear extracts with Mod(Mdg4)-67.2 (cyan arrowheads) but not HP1a (green arrowhead). Anti-XNP co-IPs HP1a but not SUUR of Mod(Mdg4)-67.2. Asterisks, IgG heavy and light chains detected due to antibody cross-reactivity. Mod(Mdg4)-67.2(FL) antibody recognizes all splice forms of Mod(Mdg4).

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/81828/elife-81828-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A–C) SWATH quantitation of SUUR (red), EGG (A, green), CG6700 (B, blue), and HP1a (C, black) fractionation profiles across five FPLC steps as in Figures 1I and 2C. Pearson coefficients (PCC) are shown (Figure 2A and B).

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/81828/elife-81828-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** (A) Mod(Mdg4)-specific peptides from ion library IL5 (Supplementary file 1). Gray shading, peptides specific to the common part (coding exons 2–4) of Mod(Mdg4); cyan shading, peptides specific to polypeptide Mod(Mdg4)-67.2 encoded by pre-mod(mdg4)-T, exons 2–3. Peptide sequences, confidence levels, charges (z), theoretical and observed m/z, column retention times (RT), and total MS2 ion counts are shown. (B) Mod(Mdg4)-67.2 polypeptide sequence. The common part is shaded in gray, and splice form-specific part is shaded in cyan. Peptides from ion library IL5 (as in A) are highlighted in bold red. (C) Mod(Mdg4)-59.1 polypeptide sequence. The common part is shaded in gray, and splice form-specific part is shaded in light green.

Mod(Mdg4) is a BTB/POZ domain protein that functions as an adapter for architectural proteins that promote various aspects of genome organization (Georgiev and Gerasimova, 1989; Gerasimova et al., 1995). It is expressed as 26 distinct polypeptides generated by splicing in trans of a common 5′-end precursor RNA with 26 unique 3′-end precursors (Büchner et al., 2000). IL5 contained seven peptides derived from Mod(Mdg4) (99% confidence). Whereas four of them mapped to the common N-terminal 402 residues, three were specific to the C-terminus of a particular form, Mod(Mdg4)-67.2 (Figure 2—figure supplement 2). Peptides specific to other splice forms were not detected. We raised an antibody to the C-terminus of Mod(Mdg4)-67.2, designated ModT antibody, and analyzed size-exclusion column fractions by immunoblotting. Consistent with SWATH analyses (Figures 1G and 2C), SUUR and Mod(Mdg4)-67.2 polypeptides copurified as a complex with an apparent molecular mass of ~250 kDa (Figure 2D). Finally, we confirmed that SUUR specifically co-immunoprecipitated with Mod(Mdg4)-67.2 from embryonic nuclear extracts (Figure 2E). As a control, XNP co-immunoprecipitated with HP1a as shown previously (Emelyanov et al., 2010), but did not with SUUR or Mod(Mdg4) (Figure 2E). We conclude that SUUR and Mod(Mdg4) form a stable stoichiometric complex that we term SUMM4 (Suppressor of Underreplication – Modifier of Mdg4).

### Biochemical activities of recombinant SUMM4 in vitro

We reconstituted recombinant SUMM4 complex by co-expressing FLAG-SUUR with Mod(Mdg4)-67.2-His6 in Sf9 cells and purified it by FLAG affinity chromatography (Figure 3A). Mod(Mdg4)-67.2 is the predominant form of Mod(Mdg4) expressed in embryos (e.g., Figure 2E, left panel). Thus, minor Mod(Mdg4) forms may have failed to be identified by IDA in IL5 (Figure 2—figure supplement 2A). We discovered that FLAG-SUUR did not co-purify with another splice form, Mod(Mdg4)-59.1 (Figure 3A, Figure 2—figure supplement 2C). Whereas the identity of an ~100 kDa Mod(Mdg4)-67.2-His6 band co-purifying with FLAG-SUUR was confirmed by mass-spec sequencing, the FLAG-purified material from Sf9 cells expressing FLAG-SUUR and Mod(Mdg4)-59.1 did not contain Mod(Mdg4)-specific peptides. Therefore, the shared N-terminus of Mod(Mdg4) (1–402) is not sufficient for interactions with SUUR. However, this result does not exclude a possibility that SUUR may form complex(es) with some of the other, low-abundance 24 splice forms of Mod(Mdg4). The SUUR-Mod(Mdg4)-67.2 interaction is specific as the second-best candidate from our correlation analyses (Drosophila SetDB1 ortholog EGG; Figure 2B) did not form a complex with FLAG-SUUR (Figure 3—figure supplement 1A), although it is associated with its known partner WDE, an ortholog of hATF7IP/mAM (Wang et al., 2003).

![Figure 3.](https://cdn.elifesciences.org/articles/81828/elife-81828-fig3-v2.jpg)

**Figure 3.:** (A) Recombinant SUMM4. Mod(Mdg4)-His6, 67.2 (p100, cyan arrowhead) and 59.1 (p75, green arrowhead) splice forms were co-expressed with FLAG-SUUR (red arrowheads, p130 and p65) or separately in Sf9 cells and purified by FLAG or Ni-NTA affinity chromatography. Mod(Mdg4)-67.2 forms a specific complex with SUUR. Identities of the 130, 100, 75, and 65 kDa protein bands from FLAG- and Ni-NTA-purified material were determined by mass spectroscopy. (B) ATPase activities of recombinant ISWI (brown bars), FLAG-SUUR (red bars), and SUMM4 (FLAG-SUUR + Mod(Mdg4)-67.2-His6, purple bars). Equimolar amounts of proteins were analyzed in reactions in the absence or presence of plasmid DNA or equivalent amounts of reconstituted oligonucleosomes,±H1. SUUR(KA) and MMD4, ATPases activities of K59A mutant of SUUR (gray bars) and Mod(Mdg4)-67.2-His6 (cyan bars). Hydrolysis rates were converted to moles ATP per mole protein per minute. All reactions were performed in triplicate (N=3), error bars represent standard deviations. p-Values for statistically significant differences are indicated (Mann–Whitney test). (C) DNA- and nucleosome-dependent stimulation or inhibition of ATPase activity. The activities were analyzed as in (B). Statistically significant differences are shown (Mann–Whitney test). (D) Nucleosome sliding activities by EpiDyne-PicoGreen assay (see ‘Materials and methods’) with 5 nM of recombinant ISWI, SUUR, or SUMM4. Reaction time courses are shown for terminally (6-N-66) and centrally (50-N-66) positioned mononucleosomes (Figure 3—figure supplement 2B–E). RFU, relative fluorescence units produced by PicoGreen fluorescence.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/81828/elife-81828-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) Physical interactions of recombinant EGG, SUUR, and WDE. Untagged EGG (green arrowhead) was co-expressed with FLAG-SUUR (red arrowheads, p130 and p65) or WDE-FLAG (purple arrowhead) in Sf9 cells and purified by FLAG affinity chromatography. EGG forms a specific complex with WDE but not SUUR. Molecular mass markers (kDa) are shown on the left. (B) Recombinant FLAG-SUUR(K59A) expressed in Sf9 cells and ISWI expressed in E. coli. See legend to Figure 1C. (C) Protein composition of in vitro reconstituted chromatin. Oligonucleosomes prepared from plasmid DNA and core histones with (+H1) or without H1 (–H1) were analyzed by SDS-PAGE and Coomassie staining. Positions of BSA, H1, and core histone bands are indicated on the right. (D) Micrococcal nuclease (MNase) analysis of reconstituted chromatin. Partial digestion with five different dilutions of MNase was performed on H1-free (–H1) and H1-containing (+H1) oligonucleosomes. Deproteinated DNA fragments were analyzed by agarose gel electrophoresis and stained with ethidium. Note the increased nucleosome repeat length in (+H1) lanes consistent with H1 incorporation. Triangles at the top indicate increasing MNase concentrations; 123 bp ladder was used as a molecular mass marker. (E) Chromatosome stop assay. Oligonucleosomes assembled with or without H1 were subjected to partial MNase digestion, and DNA was analyzed by agarose gel electrophoresis and ethidium bromide staining. Positions of the core particle and chromatosome DNA are indicated by arrowheads. DNA fragment sizes in the 20 bp DNA ladder marker are shown.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/81828/elife-81828-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** (A) EpiCypher EpiDyne-PicoGreen assay design. EpiDyne nucleosomes encompass a restriction site shielded by the initial nucleosome position but exposed for Dpn II cleavage upon remodeling (sliding or displacement). Biotinylated substrates are immobilized on streptavidin magnetic beads. Digest by Dpn II releases the substrates from beads, and supernatant is quantified by PicoGreen (dsDNA detection reagent) fluorescence. (B) Titration of Drosophila ISWI remodeling activity using terminally (6-N-66) or centrally (50-N-66) positioned mononucleosomes. Early reaction time points were separately plotted to indicate linear ranges. RFU, relative fluorescence units. (C) Early remodeling rates for ISWI were calculated by linear regression analyses of data in respective linear ranges. ISWI exhibits a stronger remodeling activity with a centrally positioned nucleosome substrate. (D) Titration of human BRG1 remodeling activity. Data are presented as in (B). (E) Early remodeling rates for BRG1 were calculated and plotted as in (D). BRG1 does not exhibit a bias toward remodeling centrally or terminally positioned nucleosomes.

The N-terminus of SUUR contains a region homologous with SNF2-like DEAD/H helicase domains. Although SUUR requires its N-terminal domain to function in vivo (Munden et al., 2018), it has been hypothesized to be inactive as an ATPase (Nordman and Orr-Weaver, 2015). We analyzed the ability of recombinant SUUR and SUMM4 (Figure 3A) to hydrolyze ATP in vitro in comparison to recombinant Drosophila ISWI (Figure 3—figure supplement 1B). Purified recombinant Mod(Mdg4)-67.2 (Figure 3A) and a variant SUUR protein with a point mutation in the putative Walker A motif (K59A) were used as negative controls (Figure 3A, Figure 3—figure supplement 1B). Contrary to the prediction, both SUUR and SUMM4 exhibited strong ATPase activities (Figure 3B). SUMM4 was 1.4- to 2-fold more active than SUUR alone, indicating that Mod(Mdg4)-67.2 stimulates SUUR enzymatic activity. We then examined whether DNA and nucleosomes can stimulate the activity of SUUR. To this end, we reconstituted oligonucleosomes on plasmid DNA (Figure 3—figure supplement 1C–E). Linker histone H1-containing chromatin was also used as a substrate/cofactor because SUUR has been demonstrated to physically interact with H1 (Andreyeva et al., 2017). In contrast to ISWI, SUUR was not stimulated by addition of DNA or nucleosomes and moderately (by about 70%) activated by H1-containing oligonucleosomes (Figure 3C) consistent with its reported direct physical interaction with H1 (Andreyeva et al., 2017).

We examined the nucleosome remodeling activities of SUUR and SUMM4; specifically, their ability to expose a positioned DNA motif in the EpiDyne-PicoGreen assay (‘Materials and methods’ and Figure 3—figure supplement 2A). Centrally or terminally positioned mononucleosomes were efficiently mobilized by ISWI and human BRG1 in a concentration- and time-dependent manner (Figure 3—figure supplement 2B–E). In contrast, SUUR and SUMM4 did not reposition either nucleosome (Figure 3D). Thus, SUUR and SUMM4 do not possess a detectable remodeling activity and may resemble certain other SNF2-like enzymes (e.g., RAD54) that utilize the energy of ATP hydrolysis to mediate alternate DNA translocation reactions (Jaskelioff et al., 2003).

### The distribution of SUMM4 complex in vivo

We examined the positions of SUUR and Mod(Mdg4)-67.2 within polytene chromosomes by indirect immunofluorescence (IF) and discovered that they overlap at numerous locations (Figure 4A, Figure 4—figure supplement 1A and B). In late endo-S phase, when SUUR exhibited a characteristic distribution, it co-localized with Mod(Mdg4)-67.2 at numerous (hundreds of) loci along the chromosome arms (Figure 4—figure supplement 1B). Mod(Mdg4)-67.2 was present at classical regions of SUUR enrichment, such as underreplicated domains in 75C and 89E (Figure 4—figure supplement 1A). The chromocenter, which consists of underreplicated pericentric heterochromatin, contains SUUR but did not show occupancy by Mod(Mdg4)-67.2 (Figure 4—figure supplement 1A). Conversely, there were multiple sites of Mod(Mdg4)-67.2 localization that were free of SUUR (Figure 4—figure supplement 1A and B). Individual pixel intensities of IF signals for SUUR and Mod(Mdg4)-67.2 were plotted as a 2D scatter plot (Figure 4—figure supplement 1C) and were found to exhibit a weak positive correlation (R2 = 0.278). Consistent with the possible multi-phasic relative distribution of SUUR and Mod(Mdg4)-67.2 (Figure 4—figure supplement 1B), the 2D plot encompassed four distinct areas, where SUUR and Mod(Mdg4)–67.2-were co-localized, enriched separately, or absent (Figure 4—figure supplement 1D). When regions of SUUR-alone and Mod(mdg4)-67.2-alone enrichment were excluded, and only the regions of their apparent colocalization were considered, the anti-SUUR and anti-ModT signals exhibited a strong positive correlation (R2 = 0.568, Figure 4—figure supplement 1D).

![Figure 4.](https://cdn.elifesciences.org/articles/81828/elife-81828-fig4-v2.jpg)

**Figure 4.:** (A) Colocalization of SUUR and Mod(Mdg4)-67.2 in wild-type polytene chromosomes. Localization patterns of Mod(Mdg4)-67.2 and SUUR in L3 polytene chromosomes were analyzed by indirect immunofluorescence (IF) staining. The polytene spread fragment (3L and 3R arms) corresponds to a nucleus in late endo-S phase, according to PCNA staining (Figure 4—figure supplement 1A). Left panel, DAPI staining shows the overall chromosome morphology. Middle panel, ModT (green) and SUUR (red) signals overlap extensively in euchromatic arms. Right panel, a colocalization image with swapped red (ModT) and green (SUUR) channels is shown for comparison. Note the additional strong ModT IF loci that are SUUR-free as well as Mod(Mdg4)-67.2-free SUUR in pericentric 3LR. (B) SUUR loading into chromosomes during early endo-S phase is compromised in mod(mdg4) mutants. SuUR mutation does not appreciably change the distribution of Mod(Mdg4)-67.2. Endo-S timing was established by PCNA staining (Figure 4—figure supplement 3B). (C) Abnormal subcellular distribution of SUMM4 subunits in mod(mdg4) and SuUR mutants. L3 salivary glands were fixed and whole-mount-stained with DAPI, ModT, and SUUR antibodies. Whereas both polypeptides are mostly nuclear in wild-type, they are partially mis-localized to the cytoplasm in mod(mdg4)u1 mutant.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/81828/elife-81828-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A) Colocalization of SUUR and Mod(Mdg4)-67.2 in wild-type polytene chromosomes. See legend to Figure 4A. 3L and 3R telomeres are marked; approximate boundaries of cytological regions are shown according to Lefevre, 1976; positions of intercalary heterochromatin regions 75C and 89E that are underreplicated and responsive to SuUR mutation are marked by circles. (B) The patterns of colocalization and independent loading of SUUR and Mod(Mdg4)-67.2 in wild-type polytene chromosomes. Subtracted and overlapping images were produced in ImageJ (‘Materials and methods’). Green, enriched Mod(Mdg4)-67.2 and low SUUR; red, enriched SUUR and low Mod(Mdg4)-67.2; magenta or cyan, overlapping enriched Mod(Mdg4)-67.2 and SUUR. (C) Quantification of the overlap between SUUR and Mod(Mdg4)-67.2 in wild-type polytene chromosomes (Figure 4A). Individual pixel intensities of anti-SUUR and anti-ModT IF signals are normalized to Z-scores and plotted on x- and y-axes, respectively (’Materials and methods’); they exhibit a weak positive correlation (R2 > 0.2). (D) Visually, the 2D plot (C) is split into four separate areas demarcated by ZModT = 1 and ZSUUR = 3. When pixels representing ModT-only and SUUR-only areas (green and red, respectively) are removed, the remaining pixels that are simultaneously enriched for Mod(Mdg4)-67.2 and SUUR (blue) exhibit a strong positive correlation (R2 > 0.5).

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/81828/elife-81828-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** (A) Schematic of partial FPLC purification of an alternative complex of Mod(Mdg4)-67.2. Cyan boxes, fraction ranges used for the next chromatographic step. (B) Western blot analyses of Q Sepharose FF fractions with SUUR and ModT antibodies. SUUR and ~25% total Mod(Mdg4)-67.2 present in the starting material (SM) fractionate in the flow-through (FT, arrows), whereas Mod(Mdg4)-67.2 also fractionates as an additional, SUUR-free peak (cyan box). Molecular mass markers are as in Figure 2D. (C) Western blot analysis of Source 15S fractions with the ModT antibody. (D) Western blot analyses of Superose 6 fractions with the ModT antibody. Black arrows, expected peaks of globular proteins with indicated molecular masses in kDa.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/81828/elife-81828-fig4-figsupp3-v2.jpg)

**Figure 4—figure supplement 3.:** (A) Western blot analyses of lysates of whole salivary glands. L3 salivary glands from homozygous animals of indicated genotypes were probed with ModT (green) and β-tubulin antibodies (red, loading control). Mass marker sizes (kDa) are shown on the left. (B) Spatiotemporal distribution of SUUR in polytene chromosomes. See legend to Figure 4B. Although SUUR is not properly loaded into mod(mdg4) chromosomes during early endo-S phase (as in wild-type), its deposition partially recovers during late endo-S.

The existence of chromosome loci heavily enriched for Mod(Mdg4)-67.2 but devoid of SUUR suggests that there are additional native form(s) of Mod(Mdg4)-67.2, either as an individual polypeptide or in complex(es) other than SUMM4. When we fractionated Drosophila nuclear extract using a different progression of FPLC steps (Figure 4—figure supplement 2A), we found that Mod(Mdg4)-67.2 can form a megadalton-sized complex that did not contain SUUR (Figure 4—figure supplement 2B–D). Therefore, a more intricate pattern of Mod(Mdg4)-67.2 distribution likely reflects loading of both SUMM4 and an alternative Mod(Mdg4)-67.2-containing complex.

We tested whether SUUR and Mod(Mdg4) loading into polytene chromosomes were mutually dependent using mutant alleles of SuUR and mod(mdg4). SuURES is a null allele of SuUR (Makunin et al., 2002). mod(mdg4)m9 is a null allele with a deficiency that removes gene regions of the shared 5′-end precursor and eight specific 3′-precursors (Savitsky et al., 2016). mod(mdg4)u1 contains an insertion of a Stalker element in the last coding exon of Mod(Mdg4)-67.2 3′-precursor (Gerasimova et al., 1995), and thus is predicted only to disrupt expression of this isoform. SuURES and mod(mdg4)u1 are homozygous viable, and mod(mdg4)m9 is recessive adult pharate lethal. Although homozygous mod(mdg4)m9 animals die after the pupal stage, they survive until late third-instar larvae (L3). Therefore, this allele cannot be used to study adult phenotypes, but it is possible to analyze its effects in L3, such as on polytene chromosome structure. Importantly, however, since the homozygous progeny is produced by heterozygous parents, the recessive phenotypes would not reveal themselves until the maternally loaded protein and RNA are exhausted (diluted and/or degraded) by late larval stages, as frequently occurs for other Drosophila mutants.

We could not detect Mod(Mdg4)-67.2 expression in homozygous mod(mdg4)m9 L3 salivary glands by immunoblotting, whereas mod(mdg4)u1 expressed a truncated polypeptide (cf., ~70 kDa and ~100 kDa, Figure 4—figure supplement 3A). The truncated 70 kDa polypeptide failed to load into polytene chromosomes (Figure 4B, Figure 4—figure supplement 3B). As shown previously, SUUR could not be detected in SuURES chromosomes. Since homozygous mod(mdg4)m9 L3 larvae were produced by inter se crosses of heterozygous parents, the very low amounts of Mod(Mdg4)-67.2 in mod(mdg4)m9 polytene chromosomes (barely above the detection limit) were presumably maternally contributed.

The absence (or drastic decrease) of Mod(Mdg4)-67.2 also strongly reduced the loading of SUUR (Figure 4B, Figure 4—figure supplement 3B). The normal distribution pattern of SUUR in polytene chromosomes is highly dynamic (Andreyeva et al., 2017; Kolesnikova et al., 2013). SUUR is initially loaded in chromosomes at the onset of endo-S phase and then redistributes through very late endo-S, when it accumulates in underreplicated domains and pericentric heterochromatin. In both mod(mdg4) mutants, we observed a striking absence of SUUR in euchromatic arms of polytene chromosomes during early endo-S (Figure 4B, Figure 4—figure supplement 3B), which indicates that the initial deposition of SUUR is dependent on its interactions with Mod(Mdg4). Although SUUR deposition slightly recovered by late endo-S, it was still several fold weaker than that in wild-type control. Potentially, in the absence of Mod(Mdg4), SUUR may be tethered to intercalary and pericentric heterochromatin loci by direct binding with linker histone H1 as shown previously (Andreyeva et al., 2017). Finally, the gross subcellular distribution of SUUR also strongly correlated with that of Mod(Mdg4): a mis-localization of truncated Mod(Mdg4)-67.2 from nuclear to partially cytoplasmic was accompanied by a similar mis-localization of SUUR (Figure 4C). This result indicates that the truncation of Mod(Mdg4) in mod(mdg4)u1 may have an antimorphic effect by mis-localization and deficient chromatin loading of interacting polypeptides, including SUUR (Figure 4C) and others (Figure 4—figure supplement 2B–D).

### The role of SUMM4 as an effector of the insulator/chromatin barrier function

Mod(Mdg4)-67.2 does not directly bind DNA but instead is tethered by a physical association with zinc finger factor Suppressor of Hairy Wing, Su(Hw) (Gause et al., 2001). Su(Hw) directly binds to consensus sequences that are present in gypsy transposable elements and are also widely distributed across the Drosophila genome in thousands of copies (Adryan et al., 2007). Mod(Mdg4)-67.2 was previously shown to be essential for the insulator activity of gypsy (Gerasimova et al., 1995), which functions in vivo to prevent enhancer–promoter interactions and establish a barrier to the propagation of chromatin forms (Cai and Levine, 1995; Roseman et al., 1993). We therefore tested whether SUMM4 contributes to the gypsy insulator functions.

The ct6 allele of Drosophila contains a gypsy element inserted between the wing enhancer and promoter of the gene cut. The insertion inactivates cut expression and results in abnormal wing development (Figure 5A). We discovered that both mod(mdg4)u1 and SuURES mutations partially suppressed this phenotype (Figure 5A) and significantly increased the wing size compared to ct6 allele alone (Figure 5B). Thus, both subunits of SUMM4 are required to mediate the full enhancer-blocking activity of gypsy. Interestingly, the double, SuURES and mod(mdg4)u1, mutant produced an additional suppression of the ct6 phenotype compared to that by mod(mdg4)u1 alone (Figure 5A, red arrowhead), which suggests that SUUR may contribute to the insulator function in the absence of Mod(Mdg4)-67.2.

![Figure 5.](https://cdn.elifesciences.org/articles/81828/elife-81828-fig5-v2.jpg)

**Figure 5.:** (A) SUMM4 subunits are required for the enhancer-blocking activity in ct6. Top: schematic diagram of the ct6 reporter system; the gypsy retrotransposon is inserted in between the wing enhancer and promoter of cut (Bag et al., 2019). Bottom left: the appearance of wild-type adult wing; bottom right: the appearance of ct6 adult wing in the wild-type background. SuURES and mod(mdg4)u1 alleles are recessive suppressors of the ct6 phenotype. Red and black arrowheads point to distinct anatomical features of the wing upon SuUR mutation. (B) Relative sizes (areas) of wings in adult male flies of the indicated phenotypes were measured (N=17) as described in ‘Materials and methods.’ p-Values for statistically significant differences are indicated (t-test). (C) SUMM4 subunits are required for the chromatin barrier activity of Su(Hw) binding sites. Top: schematic diagram of the P{SUPor-P} reporter system (Bellen et al., 2004); clustered 12 copies of gypsy Su(Hw) binding sites flanks the transcription unit of white. KV00015 and KV00138 are P{SUPor-P} insertions in pericentric heterochromatin of 2L. SuURES and mod(mdg4)u1 alleles are recessive suppressors of the boundary that insulates white from heterochromatin encroachment.

Another insulator assay makes use of a collection of P{SUPor-P} insertions that contain the white reporter flanked by 12 copies of gypsy Su(Hw)-binding sites (Figure 5C, top). When P{SUPor-P} is inserted in heterochromatin, white is protected from silencing, resulting in red eyes (Roseman et al., 1995). Both mod(mdg4)u1 and SuURES relieved the chromatin barrier function of Su(Hw) sites, causing repression of white (Figure 5C). We conclude that SUMM4 is an insulator complex that contributes to the enhancer-blocking and chromatin boundary functions of gypsy by a mechanism schematized in Figure 6A and B.

![Figure 6.](https://cdn.elifesciences.org/articles/81828/elife-81828-fig6-v2.jpg)

**Figure 6.:** (A) Schematic model for the function of SUMM4 in blocking enhancer–promoter interactions in the ct6 locus. A gypsy mobile element inserted between wing enhancer and gene cut encompasses multiple Su(Hw) binding sites. (B) Schematic model for the function of SUMM4 in establishing a chromatin barrier in heterochromatin-inserted P{SUPor-P} elements. The reporter gene white is flanked on both sides by 12 copies of gypsy insulator element. (C) Schematic model for a putative function of SUMM4 in blocking/retardation of replication fork progression in intercalary heterochromatin domains. Black oval, Su(Hw) protein bound to a gypsy insulator element(s); cyan oval, Mod(Mdg4)-67.2 protein tethered to Su(Hw); red oval, SUUR protein associated with Mod(Mdg4)-67.2 in SUMM4 complex; brown ovals represent heterochromatin components; gray rectangles, gene cut and its upstream wing enhancer; orange rectangle, gene white.

### The role of SUMM4 in the regulation of DNA replication in polytene chromosomes

A similar, chromatin partitioning-related mechanism may direct the function of SUUR in the establishment of underreplication in late-replicating intercalary heterochromatin domains of polytene chromosomes (Figure 6C). It has been long known that 3D chromosome partitioning maps show an ‘uncanny alignment’ with replication timing maps (Rhind and Gilbert, 2013). To examine the possible roles of SUMM4 in underreplication, we measured DNA copy number genome-wide in salivary glands of L3 larvae by next-generation sequencing (NGS). In w1118 control salivary glands, the DNA copy profile revealed large (>100 kbp) domains of reduced ploidy (Figure 7A), similar to previous reports (Andreyeva et al., 2017; Sher et al., 2012; Yarosh and Spradling, 2014). Excluding pericentric and sub-telomeric heterochromatin, we called 70 underreplicated regions (Table 1) in euchromatic arms, as described in ‘Materials and methods’.

![Figure 7.](https://cdn.elifesciences.org/articles/81828/elife-81828-fig7-v2.jpg)

**Figure 7.:** (A) Genome-wide analyses of DNA copy numbers in Drosophila salivary gland cells (w1118 control). DNA from L3 salivary glands was subjected to high-throughput sequencing. DNA copy numbers (normalized to diploid embryonic DNA) are shown for chromosomes X, II, and III. Chromosome arms are indicated in white. Brown- and green-shades boxes, mapped pericentric and telomeric heterochromatin regions (Hoskins et al., 2015), respectively. Asterisks, positions of underreplicated domains (Table 1). Genomic coordinates in Megabase pairs are indicated at the bottom. (B) Analyses of DNA copy numbers in Drosophila salivary gland cells from wild-type and mutant alleles. Normalized DNA copy numbers are shown across the X chromosome. The control trace (w1118 allele) is shown as semitransparent light gray in the foreground; SuURES (homozygous null) and mod(mdg4)m9 (zygotic null from crosses of heterozygous parents) traces are shown in the background in red and green, respectively; their overlaps with w1118 traces appear as lighter shades of colors. Black box, 4C9-E3 cytological region. (C) Close-up view of DNA copy numbers in region 4C9-E3 from high-throughput sequencing data are presented as in (B). DNA copy numbers were also measured independently by real-time qPCR. The numbers were calculated relative to embryonic DNA and normalized to a control intergenic region. The X-axis shows chromosome positions (in Megabase pairs) of target amplicons. Black, w1118; red, SuURES (homozygous null); green, mod(mdg4)m9 (zygotic null from crosses of heterozygous parents); purple, SuURES (zygotic null from crosses of heterozygous parents). Error bars represent the confidence interval (N=9, see ‘Materials and methods’). Black arrowheads, positions of mapped Su(Hw) binding sites (Nègre et al., 2010). Yellow boxes show approximate boundaries of cytogenetic bands. (D) Close-up view of DNA copy numbers by high-throughput sequencing and by qPCR for region 75B11-C2 and DAPI-stained polytene chromosome segments around cytological regions 75B-75C. Yellow lines or brackets in DAPI images indicate positions of 75C1 and 75C2 bands (w1118 control) or fused 75C1-2 band (mutants); cyan, mod(mdg4)u1 (homozygous null); for other designations see (C).

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/81828/elife-81828-fig7-figsupp1-v2.jpg)

**Figure 7—figure supplement 1.:** (A) Genome-wide analyses of DNA copy numbers in Drosophila salivary gland cells in chromosome arms 2L, 2R, 3L, and 3R. The data were obtained and presented as for the X chromosome (Figure 7B). Black box, 75B11-C2 cytological region. (B) Close-up view of DNA copy numbers by high-throughput sequencing for additional genomic regions. Approximate cytogenetic locations are indicated at the top of each panel. Short vertical bars at the bottom, positions of mapped Su(Hw) binding sites (Nègre et al., 2010). See legend to Figure 7C and D for other designations. (C) Sample plots of DamID profiles for SUUR (red) and Su(Hw) (purple), log2 enrichment over Dam-only control (Filion et al., 2010). Positive values are plotted in dark colors and negative values in light colors for contrast. DNA copy numbers in salivary gland cells (black) indicate underreplicated intercalary heterochromatin domains. Vertical bars, Su(Hw) binding sites (Nègre et al., 2010).

**Table 1.**
 Underrepli cated domains and suppression of underreplication in (UR) SUMM4 subunit mutant alleles.Domains of UR in euchromatic arms of polytene chromosomes were called in w1118 as described in ‘Materials and methods.’ Their genomic coordinates, approximate cytological location (‘Cyto band’), and average DNA copy numbers (‘<CN>’) in homozygous w1118, SuURES, and mod(mdg4)m9 L3 larvae are shown. <CN> numbers were normalized to the average DNA copy numbers across euchromatic genome. UR percent recovery levels were calculated as (<CN> mut –<CN>w1118) / (1 – <CN >w1118); negative numbers indicate increased UR. UR p-values were calculated using the DESeq2 package by averaging the Wald test p-values of each 5 kbp bin significantly different than the w1118 signal. UR was called as suppressible by a mutant if p<0.01; p-values for regions that exhibit a statistically significant recovery of UR are shown in bold blue. Averages of <CN> across all called underreplicated domains and averages of percent Recovery across all suppressible underreplicated domains (‘<Recovery>’, bottom row) were adjusted for each underreplicated domain length; calculation errors = standard deviations.


<table>
  <thead>
    <tr>
      <th rowspan="2">N</th>
      <th colspan="4">Chromosome coordinates</th>
      <th rowspan="2">Length</th>
      <th>UR, w1118</th>
      <th colspan="3">UR, SuURES</th>
      <th colspan="3">UR, mod(mdg4)m9</th>
    </tr>
    <tr>
      <th>Arm</th>
      <th>Left</th>
      <th>Right</th>
      <th>Cyto band</th>
      <th>&lt;CN&gt;</th>
      <th>&lt;CN&gt;</th>
      <th>Recovery (%)</th>
      <th>p-Value</th>
      <th>&lt;CN&gt;</th>
      <th>Recovery (%)</th>
      <th>p-Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>X</td>
      <td>2,950,001</td>
      <td>3,140,000</td>
      <td>3C3-C7</td>
      <td>190,000</td>
      <td>0.51</td>
      <td>0.93</td>
      <td>86</td>
      <td>7.3E-05</td>
      <td>0.58</td>
      <td>14</td>
      <td>1.1E-02</td>
    </tr>
    <tr>
      <td>2</td>
      <td>X</td>
      <td>4,710,001</td>
      <td>4,900,000</td>
      <td>4C15-D5</td>
      <td>190,000</td>
      <td>0.56</td>
      <td>0.96</td>
      <td>92</td>
      <td>3.9E-04</td>
      <td>0.81</td>
      <td>57</td>
      <td>6.9E-05</td>
    </tr>
    <tr>
      <td>3</td>
      <td>X</td>
      <td>4,965,001</td>
      <td>5,070,000</td>
      <td>4E1-E2</td>
      <td>105,000</td>
      <td>0.72</td>
      <td>0.86</td>
      <td>50</td>
      <td>5.6E-04</td>
      <td>0.80</td>
      <td>28</td>
      <td>1.4E-02</td>
    </tr>
    <tr>
      <td>4</td>
      <td>X</td>
      <td>6,415,001</td>
      <td>6,525,000</td>
      <td>6A1-B1</td>
      <td>110,000</td>
      <td>0.71</td>
      <td>0.90</td>
      <td>65</td>
      <td>1.4E-03</td>
      <td>0.80</td>
      <td>29</td>
      <td>7.3E-03</td>
    </tr>
    <tr>
      <td>5</td>
      <td>X</td>
      <td>7,335,001</td>
      <td>7,560,000</td>
      <td>7B1-B4</td>
      <td>225,000</td>
      <td>0.65</td>
      <td>0.98</td>
      <td>95</td>
      <td>1.2E-03</td>
      <td>0.79</td>
      <td>40</td>
      <td>2.8E-03</td>
    </tr>
    <tr>
      <td>6</td>
      <td>X</td>
      <td>7,750,001</td>
      <td>7,865,000</td>
      <td>7B7-C1</td>
      <td>115,000</td>
      <td>0.64</td>
      <td>0.94</td>
      <td>84</td>
      <td>3.0E-09</td>
      <td>0.84</td>
      <td>55</td>
      <td>5.2E-07</td>
    </tr>
    <tr>
      <td>7</td>
      <td>X</td>
      <td>8,880,001</td>
      <td>9,005,000</td>
      <td>8B5-C2</td>
      <td>125,000</td>
      <td>0.73</td>
      <td>0.86</td>
      <td>50</td>
      <td>5.5E-03</td>
      <td>0.76</td>
      <td>9</td>
      <td>4.6E-03</td>
    </tr>
    <tr>
      <td>8</td>
      <td>X</td>
      <td>9,405,001</td>
      <td>9,555,000</td>
      <td>8D12-E7</td>
      <td>150,000</td>
      <td>0.72</td>
      <td>0.91</td>
      <td>67</td>
      <td>3.6E-04</td>
      <td>0.85</td>
      <td>47</td>
      <td>3.6E-03</td>
    </tr>
    <tr>
      <td>9</td>
      <td>X</td>
      <td>11,170,001</td>
      <td>11,325,000</td>
      <td>10A10-B3</td>
      <td>155,000</td>
      <td>0.67</td>
      <td>0.84</td>
      <td>53</td>
      <td>3.2E-03</td>
      <td>0.78</td>
      <td>35</td>
      <td>2.6E-03</td>
    </tr>
    <tr>
      <td>10</td>
      <td>X</td>
      <td>12,040,001</td>
      <td>12,430,000</td>
      <td>11A2-A10</td>
      <td>390,000</td>
      <td>0.38</td>
      <td>0.97</td>
      <td>94</td>
      <td>1.4E-08</td>
      <td>0.42</td>
      <td>6</td>
      <td>6.8E-03</td>
    </tr>
    <tr>
      <td>11</td>
      <td>X</td>
      <td>13,950,001</td>
      <td>14,100,000</td>
      <td>12D1-E1</td>
      <td>150,000</td>
      <td>0.69</td>
      <td>0.72</td>
      <td>10</td>
      <td>1.0E-02</td>
      <td>0.73</td>
      <td>14</td>
      <td>1.4E-02</td>
    </tr>
    <tr>
      <td>12</td>
      <td>X</td>
      <td>14,290,001</td>
      <td>14,565,000</td>
      <td>12E7-F1</td>
      <td>275,000</td>
      <td>0.51</td>
      <td>0.94</td>
      <td>87</td>
      <td>4.1E-04</td>
      <td>0.69</td>
      <td>36</td>
      <td>8.1E-04</td>
    </tr>
    <tr>
      <td>13</td>
      <td>X</td>
      <td>17,925,001</td>
      <td>18,030,000</td>
      <td>16F3-F5</td>
      <td>105,000</td>
      <td>0.67</td>
      <td>0.99</td>
      <td>98</td>
      <td>1.7E-15</td>
      <td>0.90</td>
      <td>68</td>
      <td>3.4E-05</td>
    </tr>
    <tr>
      <td>14</td>
      <td>X</td>
      <td>20,000,001</td>
      <td>20,105,000</td>
      <td>19A4-B1</td>
      <td>105,000</td>
      <td>0.79</td>
      <td>1.12</td>
      <td>157</td>
      <td>1.4E-13</td>
      <td>0.82</td>
      <td>12</td>
      <td>6.1E-03</td>
    </tr>
    <tr>
      <td>15</td>
      <td>X</td>
      <td>20,525,001</td>
      <td>21,020,000</td>
      <td>19D2-E7</td>
      <td>495,000</td>
      <td>0.50</td>
      <td>0.97</td>
      <td>93</td>
      <td>1.3E-07</td>
      <td>0.51</td>
      <td>2</td>
      <td>4.9E-03</td>
    </tr>
    <tr>
      <td>16</td>
      <td>X</td>
      <td>21,630,001</td>
      <td>22,450,000</td>
      <td>20A5-C1</td>
      <td>820,000</td>
      <td>0.04</td>
      <td>0.32</td>
      <td>29</td>
      <td>1.8E-03</td>
      <td>0.06</td>
      <td>2</td>
      <td>6.4E-03</td>
    </tr>
    <tr>
      <td>17</td>
      <td>X</td>
      <td>22,550,001</td>
      <td>22,995,000</td>
      <td>20C2-F3</td>
      <td>445,000</td>
      <td>0.48</td>
      <td>0.81</td>
      <td>64</td>
      <td>7.8E-05</td>
      <td>0.74</td>
      <td>51</td>
      <td>3.5E-04</td>
    </tr>
    <tr>
      <td>18</td>
      <td>2L</td>
      <td>3,920,001</td>
      <td>4,025,000</td>
      <td>24D1-D4</td>
      <td>105,000</td>
      <td>0.63</td>
      <td>0.93</td>
      <td>81</td>
      <td>7.9E-07</td>
      <td>0.80</td>
      <td>46</td>
      <td>5.9E-05</td>
    </tr>
    <tr>
      <td>19</td>
      <td>2L</td>
      <td>4,585,001</td>
      <td>4,790,000</td>
      <td>25A2-A5</td>
      <td>205,000</td>
      <td>0.66</td>
      <td>0.99</td>
      <td>98</td>
      <td>1.9E-08</td>
      <td>0.78</td>
      <td>36</td>
      <td>1.3E-03</td>
    </tr>
    <tr>
      <td>20</td>
      <td>2L</td>
      <td>5,400,001</td>
      <td>5,510,000</td>
      <td>25E1-E4</td>
      <td>110,000</td>
      <td>0.82</td>
      <td>0.99</td>
      <td>95</td>
      <td>4.0E-08</td>
      <td>0.90</td>
      <td>45</td>
      <td>8.3E-03</td>
    </tr>
    <tr>
      <td>21</td>
      <td>2L</td>
      <td>6,155,001</td>
      <td>6,320,000</td>
      <td>26B9-C2</td>
      <td>165,000</td>
      <td>0.74</td>
      <td>1.08</td>
      <td>130</td>
      <td>7.3E-14</td>
      <td>0.88</td>
      <td>54</td>
      <td>4.7E-04</td>
    </tr>
    <tr>
      <td>22</td>
      <td>2L</td>
      <td>9,030,001</td>
      <td>9,150,000</td>
      <td>29F8-30A2</td>
      <td>120,000</td>
      <td>0.76</td>
      <td>0.98</td>
      <td>93</td>
      <td>1.5E-04</td>
      <td>0.95</td>
      <td>79</td>
      <td>3.3E-03</td>
    </tr>
    <tr>
      <td>23</td>
      <td>2L</td>
      <td>11,535,001</td>
      <td>11,795,000</td>
      <td>32F2-33A1</td>
      <td>260,000</td>
      <td>0.44</td>
      <td>0.90</td>
      <td>83</td>
      <td>2.9E-04</td>
      <td>0.57</td>
      <td>24</td>
      <td>1.5E-03</td>
    </tr>
    <tr>
      <td>24</td>
      <td>2L</td>
      <td>12,215,001</td>
      <td>12,340,000</td>
      <td>33D3-E1</td>
      <td>125,000</td>
      <td>0.58</td>
      <td>0.86</td>
      <td>66</td>
      <td>3.6E-11</td>
      <td>0.75</td>
      <td>40</td>
      <td>1.1E-04</td>
    </tr>
    <tr>
      <td>25</td>
      <td>2L</td>
      <td>12,765,001</td>
      <td>12,970,000</td>
      <td>33F5-34A3</td>
      <td>205,000</td>
      <td>0.55</td>
      <td>0.91</td>
      <td>79</td>
      <td>8.8E-04</td>
      <td>0.73</td>
      <td>40</td>
      <td>7.0E-05</td>
    </tr>
    <tr>
      <td>26</td>
      <td>2L</td>
      <td>14,685,001</td>
      <td>15,010,000</td>
      <td>35B4-B8</td>
      <td>325,000</td>
      <td>0.41</td>
      <td>0.88</td>
      <td>80</td>
      <td>5.7E-04</td>
      <td>0.54</td>
      <td>23</td>
      <td>7.2E-04</td>
    </tr>
    <tr>
      <td>27</td>
      <td>2L</td>
      <td>15,295,001</td>
      <td>15,735,000</td>
      <td>35D1-D4</td>
      <td>440,000</td>
      <td>0.49</td>
      <td>0.76</td>
      <td>53</td>
      <td>2.3E-05</td>
      <td>0.54</td>
      <td>9</td>
      <td>4.0E-03</td>
    </tr>
    <tr>
      <td>28</td>
      <td>2L</td>
      <td>15,770,001</td>
      <td>15,900,000</td>
      <td>35D4-D6</td>
      <td>130,000</td>
      <td>0.54</td>
      <td>0.87</td>
      <td>71</td>
      <td>4.5E-08</td>
      <td>0.68</td>
      <td>31</td>
      <td>6.7E-04</td>
    </tr>
    <tr>
      <td>29</td>
      <td>2L</td>
      <td>15,925,001</td>
      <td>16,240,000</td>
      <td>35D6-F1</td>
      <td>315,000</td>
      <td>0.29</td>
      <td>0.90</td>
      <td>87</td>
      <td>6.7E-07</td>
      <td>0.38</td>
      <td>12</td>
      <td>1.4E-05</td>
    </tr>
    <tr>
      <td>30</td>
      <td>2L</td>
      <td>16,925,001</td>
      <td>17,375,000</td>
      <td>36B4-C7</td>
      <td>450,000</td>
      <td>0.23</td>
      <td>0.89</td>
      <td>85</td>
      <td>1.4E-04</td>
      <td>0.26</td>
      <td>4</td>
      <td>4.3E-03</td>
    </tr>
    <tr>
      <td>31</td>
      <td>2L</td>
      <td>17,515,001</td>
      <td>18,100,000</td>
      <td>36C10-E4</td>
      <td>585,000</td>
      <td>0.34</td>
      <td>0.87</td>
      <td>80</td>
      <td>5.0E-06</td>
      <td>0.36</td>
      <td>2</td>
      <td>3.7E-03</td>
    </tr>
    <tr>
      <td>32</td>
      <td>2L</td>
      <td>18,160,001</td>
      <td>18,300,000</td>
      <td>36E6-F2</td>
      <td>140,000</td>
      <td>0.67</td>
      <td>0.99</td>
      <td>97</td>
      <td>3.3E-06</td>
      <td>0.90</td>
      <td>69</td>
      <td>3.1E-06</td>
    </tr>
    <tr>
      <td>33</td>
      <td>2L</td>
      <td>20,110,001</td>
      <td>20,290,000</td>
      <td>38C1-C4</td>
      <td>180,000</td>
      <td>0.48</td>
      <td>0.69</td>
      <td>41</td>
      <td>8.9E-04</td>
      <td>0.46</td>
      <td>–5</td>
      <td>1.8E-03</td>
    </tr>
    <tr>
      <td>34</td>
      <td>2L</td>
      <td>20,485,001</td>
      <td>20,620,000</td>
      <td>38C8-D1</td>
      <td>135,000</td>
      <td>0.77</td>
      <td>0.98</td>
      <td>93</td>
      <td>1.0E-06</td>
      <td>0.99</td>
      <td>97</td>
      <td>2.1E-05</td>
    </tr>
    <tr>
      <td>35</td>
      <td>2L</td>
      <td>21,400,001</td>
      <td>21,550,000</td>
      <td>39D3-E2</td>
      <td>150,000</td>
      <td>0.10</td>
      <td>0.15</td>
      <td>5</td>
      <td>3.2E-03</td>
      <td>0.14</td>
      <td>3</td>
      <td>4.4E-03</td>
    </tr>
    <tr>
      <td>36</td>
      <td>2L</td>
      <td>21,805,001</td>
      <td>22,125,000</td>
      <td>40A4-E4</td>
      <td>320,000</td>
      <td>0.53</td>
      <td>0.94</td>
      <td>87</td>
      <td>6.9E-05</td>
      <td>0.54</td>
      <td>1</td>
      <td>9.5E-03</td>
    </tr>
    <tr>
      <td>37</td>
      <td>2R</td>
      <td>4,875,001</td>
      <td>5,050,000</td>
      <td>41C4-D1</td>
      <td>175,000</td>
      <td>0.35</td>
      <td>0.86</td>
      <td>78</td>
      <td>2.3E-10</td>
      <td>0.34</td>
      <td>–1</td>
      <td>4.0E-03</td>
    </tr>
    <tr>
      <td>38</td>
      <td>2R</td>
      <td>5,410,001</td>
      <td>5,535,000</td>
      <td>41F1-F3</td>
      <td>125,000</td>
      <td>0.58</td>
      <td>0.79</td>
      <td>50</td>
      <td>1.1E-03</td>
      <td>0.52</td>
      <td>–13</td>
      <td>2.2E-03</td>
    </tr>
    <tr>
      <td>39</td>
      <td>2R</td>
      <td>6,290,001</td>
      <td>6,505,000</td>
      <td>42A14-B1</td>
      <td>215,000</td>
      <td>0.13</td>
      <td>0.50</td>
      <td>42</td>
      <td>9.3E-04</td>
      <td>0.14</td>
      <td>1</td>
      <td>2.7E-03</td>
    </tr>
    <tr>
      <td>40</td>
      <td>2R</td>
      <td>13,620,001</td>
      <td>13,760,000</td>
      <td>50B6-C3</td>
      <td>140,000</td>
      <td>0.63</td>
      <td>0.95</td>
      <td>88</td>
      <td>4.1E-18</td>
      <td>0.78</td>
      <td>41</td>
      <td>1.3E-05</td>
    </tr>
    <tr>
      <td>41</td>
      <td>2R</td>
      <td>20,355,001</td>
      <td>20,540,000</td>
      <td>56F17-57A5</td>
      <td>185,000</td>
      <td>0.56</td>
      <td>0.92</td>
      <td>83</td>
      <td>2.0E-06</td>
      <td>0.71</td>
      <td>35</td>
      <td>8.2E-04</td>
    </tr>
    <tr>
      <td>42</td>
      <td>2R</td>
      <td>21,830,001</td>
      <td>21,945,000</td>
      <td>58A2-A4</td>
      <td>115,000</td>
      <td>0.72</td>
      <td>0.95</td>
      <td>83</td>
      <td>1.1E-05</td>
      <td>0.71</td>
      <td>–3</td>
      <td>2.2E-02</td>
    </tr>
    <tr>
      <td>43</td>
      <td>2R</td>
      <td>23,145,001</td>
      <td>23,320,000</td>
      <td>59D1-D6</td>
      <td>175,000</td>
      <td>0.62</td>
      <td>1.04</td>
      <td>110</td>
      <td>1.3E-22</td>
      <td>0.67</td>
      <td>13</td>
      <td>7.7E-03</td>
    </tr>
    <tr>
      <td>44</td>
      <td>3L</td>
      <td>4,840,001</td>
      <td>5,100,000</td>
      <td>64C1-C5</td>
      <td>260,000</td>
      <td>0.38</td>
      <td>0.92</td>
      <td>87</td>
      <td>3.5E-08</td>
      <td>0.40</td>
      <td>3</td>
      <td>6.6E-03</td>
    </tr>
    <tr>
      <td>45</td>
      <td>3L</td>
      <td>5,385,001</td>
      <td>5,510,000</td>
      <td>64C15-D3</td>
      <td>125,000</td>
      <td>0.51</td>
      <td>0.88</td>
      <td>76</td>
      <td>1.9E-22</td>
      <td>0.73</td>
      <td>45</td>
      <td>6.0E-09</td>
    </tr>
    <tr>
      <td>46</td>
      <td>3L</td>
      <td>6,290,001</td>
      <td>6,485,000</td>
      <td>65A11-B3</td>
      <td>195,000</td>
      <td>0.52</td>
      <td>0.89</td>
      <td>77</td>
      <td>4.9E-05</td>
      <td>0.71</td>
      <td>38</td>
      <td>1.2E-04</td>
    </tr>
    <tr>
      <td>47</td>
      <td>3L</td>
      <td>9,180,001</td>
      <td>9,300,000</td>
      <td>67A1-A7</td>
      <td>120,000</td>
      <td>0.67</td>
      <td>0.97</td>
      <td>90</td>
      <td>6.5E-09</td>
      <td>0.73</td>
      <td>20</td>
      <td>1.0E-02</td>
    </tr>
    <tr>
      <td>48</td>
      <td>3L</td>
      <td>10,000,001</td>
      <td>10,195,000</td>
      <td>67D3-D10</td>
      <td>195,000</td>
      <td>0.62</td>
      <td>0.97</td>
      <td>93</td>
      <td>4.4E-13</td>
      <td>0.79</td>
      <td>44</td>
      <td>5.7E-06</td>
    </tr>
    <tr>
      <td>49</td>
      <td>3L</td>
      <td>13,085,001</td>
      <td>13,220,000</td>
      <td>70A1-A2</td>
      <td>135,000</td>
      <td>0.66</td>
      <td>1.01</td>
      <td>104</td>
      <td>3.6E-09</td>
      <td>0.89</td>
      <td>66</td>
      <td>2.9E-06</td>
    </tr>
    <tr>
      <td>50</td>
      <td>3L</td>
      <td>13,550,001</td>
      <td>13,855,000</td>
      <td>70B6-C4</td>
      <td>305,000</td>
      <td>0.26</td>
      <td>0.95</td>
      <td>94</td>
      <td>1.8E-06</td>
      <td>0.39</td>
      <td>18</td>
      <td>7.3E-04</td>
    </tr>
    <tr>
      <td>51</td>
      <td>3L</td>
      <td>15,175,001</td>
      <td>15,500,000</td>
      <td>71B7-D3</td>
      <td>325,000</td>
      <td>0.39</td>
      <td>0.94</td>
      <td>89</td>
      <td>5.6E-04</td>
      <td>0.46</td>
      <td>10</td>
      <td>3.7E-03</td>
    </tr>
    <tr>
      <td>52</td>
      <td>3L</td>
      <td>17,115,001</td>
      <td>17,240,000</td>
      <td>73F1-74A1</td>
      <td>125,000</td>
      <td>0.71</td>
      <td>1.02</td>
      <td>106</td>
      <td>4.3E-05</td>
      <td>0.84</td>
      <td>45</td>
      <td>2.7E-03</td>
    </tr>
    <tr>
      <td>53</td>
      <td>3L</td>
      <td>18,175,001</td>
      <td>18,525,000</td>
      <td>75B11-75D2</td>
      <td>350,000</td>
      <td>0.45</td>
      <td>0.87</td>
      <td>76</td>
      <td>6.8E-05</td>
      <td>0.47</td>
      <td>4</td>
      <td>4.6E-03</td>
    </tr>
    <tr>
      <td>54</td>
      <td>3L</td>
      <td>20,555,001</td>
      <td>20,695,000</td>
      <td>77D1-77E3</td>
      <td>140,000</td>
      <td>0.60</td>
      <td>1.02</td>
      <td>106</td>
      <td>2.2E-22</td>
      <td>0.84</td>
      <td>61</td>
      <td>3.6E-11</td>
    </tr>
    <tr>
      <td>55</td>
      <td>3R</td>
      <td>6,060,001</td>
      <td>6,310,000</td>
      <td>83D2-E4</td>
      <td>250,000</td>
      <td>0.70</td>
      <td>0.92</td>
      <td>72</td>
      <td>7.6E-04</td>
      <td>0.63</td>
      <td>–22</td>
      <td>1.0E-02</td>
    </tr>
    <tr>
      <td>56</td>
      <td>3R</td>
      <td>6,495,001</td>
      <td>6,635,000</td>
      <td>83F1-84A1</td>
      <td>140,000</td>
      <td>0.53</td>
      <td>0.96</td>
      <td>91</td>
      <td>7.8E-08</td>
      <td>0.71</td>
      <td>39</td>
      <td>2.2E-04</td>
    </tr>
    <tr>
      <td>57</td>
      <td>3R</td>
      <td>6,915,001</td>
      <td>7,055,000</td>
      <td>84B1-B2</td>
      <td>140,000</td>
      <td>0.64</td>
      <td>0.93</td>
      <td>80</td>
      <td>3.9E-04</td>
      <td>0.82</td>
      <td>49</td>
      <td>1.9E-05</td>
    </tr>
    <tr>
      <td>58</td>
      <td>3R</td>
      <td>7,550,001</td>
      <td>7,785,000</td>
      <td>84D9-84E2</td>
      <td>235,000</td>
      <td>0.44</td>
      <td>0.80</td>
      <td>65</td>
      <td>8.0E-06</td>
      <td>0.51</td>
      <td>12</td>
      <td>4.2E-03</td>
    </tr>
    <tr>
      <td>59</td>
      <td>3R</td>
      <td>10,450,001</td>
      <td>10,660,000</td>
      <td>86B6-C4</td>
      <td>210,000</td>
      <td>0.55</td>
      <td>0.98</td>
      <td>97</td>
      <td>8.1E-11</td>
      <td>0.66</td>
      <td>25</td>
      <td>7.6E-04</td>
    </tr>
    <tr>
      <td>60</td>
      <td>3R</td>
      <td>10,910,001</td>
      <td>11,140,000</td>
      <td>88C15-86D4</td>
      <td>230,000</td>
      <td>0.45</td>
      <td>0.94</td>
      <td>89</td>
      <td>2.3E-10</td>
      <td>0.46</td>
      <td>2</td>
      <td>2.3E-03</td>
    </tr>
    <tr>
      <td>61</td>
      <td>3R</td>
      <td>12,050,001</td>
      <td>12,165,000</td>
      <td>87A5-B1</td>
      <td>115,000</td>
      <td>0.63</td>
      <td>0.96</td>
      <td>88</td>
      <td>9.9E-24</td>
      <td>0.81</td>
      <td>49</td>
      <td>5.9E-09</td>
    </tr>
    <tr>
      <td>62</td>
      <td>3R</td>
      <td>12,745,001</td>
      <td>12,935,000</td>
      <td>87C8-D4</td>
      <td>190,000</td>
      <td>0.67</td>
      <td>0.89</td>
      <td>68</td>
      <td>7.5E-05</td>
      <td>0.60</td>
      <td>–21</td>
      <td>1.1E-02</td>
    </tr>
    <tr>
      <td>63</td>
      <td>3R</td>
      <td>14,935,001</td>
      <td>15,055,000</td>
      <td>88D8-D10</td>
      <td>120,000</td>
      <td>0.70</td>
      <td>0.88</td>
      <td>61</td>
      <td>7.6E-06</td>
      <td>0.84</td>
      <td>47</td>
      <td>1.0E-04</td>
    </tr>
    <tr>
      <td>64</td>
      <td>3R</td>
      <td>16,670,001</td>
      <td>16,970,000</td>
      <td>89D6-E5</td>
      <td>300,000</td>
      <td>0.40</td>
      <td>0.92</td>
      <td>87</td>
      <td>2.7E-09</td>
      <td>0.47</td>
      <td>10</td>
      <td>3.2E-03</td>
    </tr>
    <tr>
      <td>65</td>
      <td>3R</td>
      <td>17,160,001</td>
      <td>17,355,000</td>
      <td>89F1-90A2</td>
      <td>195,000</td>
      <td>0.62</td>
      <td>0.94</td>
      <td>84</td>
      <td>1.0E-03</td>
      <td>0.86</td>
      <td>64</td>
      <td>2.8E-04</td>
    </tr>
    <tr>
      <td>66</td>
      <td>3R</td>
      <td>20,085,001</td>
      <td>20,290,000</td>
      <td>92C4-E1</td>
      <td>205,000</td>
      <td>0.61</td>
      <td>0.81</td>
      <td>53</td>
      <td>1.5E-03</td>
      <td>0.71</td>
      <td>26</td>
      <td>3.6E-03</td>
    </tr>
    <tr>
      <td>67</td>
      <td>3R</td>
      <td>20,340,001</td>
      <td>20,525,000</td>
      <td>92E4-E12</td>
      <td>185,000</td>
      <td>0.58</td>
      <td>0.96</td>
      <td>91</td>
      <td>5.0E-05</td>
      <td>0.79</td>
      <td>50</td>
      <td>7.2E-04</td>
    </tr>
    <tr>
      <td>68</td>
      <td>3R</td>
      <td>22,110,001</td>
      <td>22,295,000</td>
      <td>94A2-A4</td>
      <td>185,000</td>
      <td>0.61</td>
      <td>0.93</td>
      <td>83</td>
      <td>3.4E-11</td>
      <td>0.76</td>
      <td>39</td>
      <td>3.0E-04</td>
    </tr>
    <tr>
      <td>69</td>
      <td>3R</td>
      <td>28,005,001</td>
      <td>28,295,000</td>
      <td>98B7-C3</td>
      <td>290,000</td>
      <td>0.40</td>
      <td>0.91</td>
      <td>85</td>
      <td>2.5E-05</td>
      <td>0.60</td>
      <td>32</td>
      <td>6.9E-04</td>
    </tr>
    <tr>
      <td>70</td>
      <td>3R</td>
      <td>28,370,001</td>
      <td>28,480,000</td>
      <td>98C5-D2</td>
      <td>110,000</td>
      <td>0.73</td>
      <td>0.98</td>
      <td>94</td>
      <td>1.2E-09</td>
      <td>0.91</td>
      <td>66</td>
      <td>4.3E-07</td>
    </tr>
    <tr>
      <td colspan="7">UR domains: 70&lt;Length&gt; : 216 ± 64 kbpAverage &lt;CN&gt; across all UR domains: 0.49 ± 0.08</td>
      <td colspan="3">Suppressed UR domains: 69&lt;Length&gt; : 217 ± 64 kbp&lt;Recovery&gt; : 78 ± 11%</td>
      <td colspan="3">Suppressed UR domains: 60&lt;Length&gt; : 225 ± 67 kbp&lt;Recovery&gt; : 26 ± 9%</td>
    </tr>
  </tbody>
</table>

In both SuUR and mod(mdg4)m9 null larvae, we observed statistically significant suppression of underreplication in intercalary heterochromatin (Figure 7B, Figure 7—figure supplement 1A, Table 1). In line with its lack of accumulation within the chromocenter of polytene chromosomes (Figure 4A), Mod(Mdg4) was largely dispensable for underreplication in pericentric heterochromatin. The NGS data strongly correlated with qPCR measurements of DNA copy numbers (Figure 7C and D). Furthermore, cytological evidence in the 75C region supported the molecular analyses in that both mutants exhibited a brighter DAPI staining of the 75C1-2 band than that in w1118, indicative of higher DNA content (Figure 7D). Importantly, consistent with the role of Mod(Mdg4)-dependent insulators in the establishment of underreplication, the boundaries of underreplicated domains frequently encompass multiple clustered Su(Hw) binding sites (Figure 7C and D).

Uniformly, SuUR mutation gave rise to a stronger relief of underreplication than that produced by the mod(mdg4)m9 null allele (Table 1). This result can be explained by embryonic deposition of functional Mod(Mdg4) proteins and RNA by heterozygous mothers, unlike the complete absence of SUUR throughout the life cycle of the homozygous viable and fertile SuURES animals. Although third-instar larvae are >1000-fold larger, volume-wise, than the embryos, persistent Mod(Mdg4)-67.2 can still be detected in polytene chromosomes of these larvae by IF despite its dilution and degradation (Figure 4B, Figure 4—figure supplement 3B). In contrast, unlike L3, first-instar larvae (L1) are nearly identical in size to the embryos. Therefore, since the endoreplication cycles initiate in embryos and L1, in mod(mdg4)m9 animals the first few out of 10–11 rounds of chromosome polytenization take place with an almost normal amount of Mod(Mdg4) present, which may substantially limit the effect of mod(mdg4)m9 mutation on underreplication as measured in L3.

Seemingly, there is a contradiction between a strong effect that mod(mdg4) null mutation has on the loading of SUUR in polytene chromosomes (Figure 4B) and a weaker effect on underreplication (Figure 7B–D, Figure 7—figure supplement 1A and B, Table 1). However, the SUUR occupancy is examined in L3 after the maternal mod(mdg4) product is nearly eliminated (Figure 4B). On the other hand, the DNA copy number, although also measured in L3 (Figure 7B–D, Figure 7—figure supplement 1A and B, Table 1), is a product of multiple rounds of endoreplication that initiate before Mod(Mdg4) is exhausted. To validate the putative effect of maternally contributed SUMM4 on the establishment of underreplication, we performed qPCR measurements of DNA copy numbers in salivary glands of homozygous SuUR animals produced by inter se crosses of heterozygous SuURES/+ parents (Figure 7C and D, zygotic SuURES). Similar to the maternal Mod(Mdg4), the initial maternal contribution of SUUR partially limited the reversal of underreplication in cytological regions 4D and 75C. Thus, when the SuUR and mod(mdg4) null mutant animals are similarly derived from heterozygous mothers that deposit wild-type gene product into their progeny, the mutant underreplication phenotypes in the third-instar larval salivary gland are essentially indistinguishable. Finally, we analyzed the effect of homozygous mod(mdg4)u1 mutation, which is viable and fertile, on DNA copy numbers in the 75C underreplicated domain by qPCR and cytologically (Figure 7D). We observed a substantially stronger suppression of underreplication than that in mod(mdg4)m9, presumably due to the absence of maternal contribution of full-length Mod(Mdg4)-67.2.

We conclude that SUUR and Mod(Mdg4)-67.2 act together as subunits of stable SUMM4 complex, which is required for the establishment of underreplication in the intercalary heterochromatin domains of Drosophila polytene chromosome.

## Discussion

### MERCI is a powerful new approach to characterize stable stoichiometric protein complexes

We present here a facile method, termed MERCI, to rapidly identify subunits of stable native complexes by only partial chromatographic purification. It allows one to circumvent the conventional, rate-limiting approach to purify proteins to apparent homogeneity. Since a multistep FPLC scheme invariably leads to an exponential loss of material, reducing the number of purification steps in the MERCI protocol allows identification of rare complexes, such as SUMM4, which may be present in trace amounts in native sources. On the other hand, MERCI obviates introduction of false-positives frequently associated with tag purification of ectopically expressed targets that render results less reliable. Notably, MERCI is not limited to analyses of known polypeptides since it is readily amenable to fractionation of native factors based on a correlation with their biochemical activities in vitro.

The dissection of protein interactome by extract fractionation on orthogonal FPLC columns and MS-based approaches has been previously attempted (Havugimana et al., 2012; Shatsky et al., 2016). However, unlike the newly developed MERCI approach, these studies were aimed at comprehensive, proteome-wide analyses, which managed to only yield data for the most abundant complexes. The major distinction of the MERCI protocol is that it is targeted toward a particular protein (SUUR in this study). The crucial final stage of the MERCI algorithm is re-quantification of all acquired SWATH data using a library acquired from fractions of the last column (IL5, Figure 1A, B, and I). The target protein and co-purifying polypeptides are substantially enriched after several chromatographic steps and, thus, yield a greater number of detected peptides, which helps a more precise quantification. Although SWATH allows reliable measurement of picogram amounts of proteins (Figure 1—figure supplement 1A and B), the range of quantified polypeptides is always limited by those present in IDA (ion libraries). For low-abundance proteins, such as SUUR and Mod(Mdg4), specific peptides are not detectable by IDA in earlier chromatographic steps (Supplementary file 1). Consequently, SWATH quantification using only the cognate ion libraries would not discern the near perfect co-fractionation of SUUR and Mod(Mdg4) in all five steps (Figure 2C), precluding identification of the SUUR-Mod(Mdg4) complex (Figure 2B and C).

One limitation of the MERCI protocol is its failure to measure the absolute amounts of identified polypeptides. For instance, quantification of SWATH data (Figure 1D–H) measures the relative (to reference proteins and each other) amounts of SUUR across fractions. To measure the absolute levels of SUUR, a semi-quantitative approach was used by building a titration curve from SWATH acquisitions of known amounts of recombinant SUUR (Figure 1—figure supplement 1A and B). We estimated the amount of SUUR in the nuclear extract (~140 pg in 25 µg total protein, Figure 1—figure supplement 1B) and in individual fractions from all chromatographic steps (Figure 1—figure supplement 1C). Although in five FPLC steps we achieved >3000-fold purification of SUUR, it remained only ~2% pure (Figure 1—figure supplement 1D). A progressive loss of material precludes further purification (300 ng of SUUR in 16 µg total protein). Thus, the SUMM4 complex would be nearly impossible to purify to homogeneity from a substantial amount of starting material (~1 kg Drosophila embryos, ~2.5 g protein), suggesting that SUMM4 could not be identified by the classical FPLC approach.

### SUMM4 regulates the function of gypsy insulator elements

Both subunits of SUMM4 contribute to the known functions of gypsy insulator (Figure 5A–C). Although a SuUR mutation decreased the insulator activity, the suppression was universally weaker than that by mod(mdg4)u1. It is possible that SUUR is not absolutely required for the establishment of the insulator. For instance, the loss of SUMM4 may be compensated by the alternative complex of Mod(Mdg4)-67.2 (Figure 4—figure supplement 2). Furthermore, the mod(mdg4)u1 allele is expected to have an antimorphic function since it can mis-localize interacting partner proteins, including SUUR itself (Figure 4C). Interestingly, SuUR has been previously characterized as a weak suppressor of variegation of the whitem4h X chromosome inversion allele, which places the white gene near pericentric heterochromatin (Belyaeva et al., 2003). In contrast, SuUR mutation enhances variegation in the context of insulated, heterochromatin-positioned white (Figure 5C). Therefore, this phenotype is unrelated to the putative Su(var) function of SuUR but, rather, is insulator-dependent.

### ATP-dependent motor proteins are required for the establishment of chromatin barrier and chromosome partitioning

Our discovery and analyses of SUMM4 provide a biochemical link between ATP-dependent motor factors and the activity of insulators in the regulation of gene expression and chromatin partitioning. Insulator elements organize the genome into chromatin loops (Gerasimova et al., 1995) that are involved in the formation of topologically associating domains [TADs] (Peterson et al., 2021; Rowley et al., 2017; Szabo et al., 2019). In mammals, CTCF-dependent loop formation requires ATP-driven motor activity of SMC complex cohesin (Davidson et al., 2019). In contrast, CTCF and cohesin are thought to be dispensable for chromatin 3D partitioning in Drosophila (Matthews and White, 2019). Instead, the larger, transcriptionally inactive domains (canonical TADs) are interspersed with smaller active compartmental domains, which themselves represent TAD boundaries (Rowley et al., 2017). It has been proposed that in Drosophila, domain organization does not rely on architectural proteins but is established by transcription-dependent, A-A compartmental (gene-to-gene) interactions (Rowley et al., 2017). However, Drosophila TAD boundaries are enriched for architectural proteins other than CTCF (Van Bortle et al., 2014), and their roles have not been tested in loss-of-function models. Thus, it is possible that in Drosophila, instead of CTCF, the 3D partitioning of the genome is facilitated by another group of insulator proteins, such as Su(Hw) and SUMM4, that together associate with class 3 insulators (Schwartz et al., 2012).

Moreover, SUUR may provide the DNA motor function to promote a physical separation of active and inactive loci and help establish chromosome contact domains (Figure 6A–C). We propose that within the SUMM4 complex, SUUR utilizes its putative ATP-dependent motor activity to translocate along chromatin strands, thus facilitating the establishment of higher-order structures that isolate promoters from enhancers (Figure 6A) and stabilize DNA loops/domains to prevent unrestricted heterochromatin encroachment (Figure 6B) and penetration of replication forks (Figure 6C). The translocation model is consistent with observations of an asymmetric, selective occupancy of SUUR away from its initial sites of deposition via Su(Hw)-Mod(Mdg4) binding toward inside of intercalary heterochromatin regions but not outside (Figure 7—figure supplement 1C; Filion et al., 2010), which may be facilitated by physical interactions between SUUR and linker histone H1 enriched in intercalary heterochromatin (Andreyeva et al., 2017). It has been reported that another Drosophila BTB/POZ domain insulator protein CP190 forms a complex with a DEAD-box helicase Rm62 that contributes to the insulator activity (Lei and Corces, 2006). Thus, ATP-dependent motor proteins may represent an obligatory component of the insulator complex machinery.

### SUMM4 mediates known biological functions of SUUR

Our discovery explains previous observations about biological functions of SUUR. For instance, the initial deposition of SUUR and its colocalization with PCNA has been proposed to depend on direct physical interaction with components of the replisome (Kolesnikova et al., 2013). Our model indicates that, instead, the apparent colocalization of SUUR with PCNA throughout endo-S phase (Figure 4—figure supplement 3B) may be caused by a replication fork retardation at insulator sites. SUUR is deposited in chromosomes as a subunit of SUMM4 complex at thousands of loci by tethering via Mod(Mdg4)-Su(Hw) interactions. As replication forks progress through the genome, they encounter insulator complexes where replication machinery pauses for various periods of time before resolving the obstacle. Thus, the increased co-residence time of PCNA and SUUR manifests cytologically as their partial colocalization. With the progression of endo-S phase, some of the SUMM4 insulator complexes are evicted and, thus, the number of SUUR-positive loci is decreased, until eventually the replication fork encounters nearly completely impenetrable insulators demarcating the underreplicated domain boundaries.

This mechanism is especially plausible given that boundaries of intercalary heterochromatin loci very frequently encompass multiple, densely clustered Su(Hw) binding sites (e.g., Figure 7C and D). We examined the data from genome-wide proteomic analyses for Su(Hw) and SUUR performed by DamID in Kc167 cells (Filion et al., 2010). Strikingly, Su(Hw) DamID-measured occupancy does not exhibit a discrete pattern expected of a DNA-binding factor. Instead, it appears broadly dispersed, together with SUUR, up to tens of kbp away from mapped Su(Hw) binding sites (Figure 7—figure supplement 1C). Interestingly, when hidden Markov modeling was applied to the DamID data, Su(Hw), Mod(Mdg4)-67.2, and SUUR occupancies were found to strongly correlate genome-wide in a novel chromatin form (‘malachite’) that frequently demarcates the boundaries of intercalary heterochromatin (Khoroshko et al., 2016). These observations strongly corroborate the translocation model for the mechanism of action of SUMM4. According to this model, upon tethering to DNA-bound Su(Hw), SUMM4 traverses the underreplicated region, which helps to separate it in a contact domain. As DNA within the underreplicated region is tracked by SUUR (Figure 6C), it is brought into a transient close proximity with both SUMM4 and the associated Su(Hw) protein, which is detected by DamID (or ChIP) as an expanded occupancy pattern.

The deceleration of SUUR-bound replication forks was also invoked as an explanation for the apparent role of SUUR in the establishment of epigenetic marking of intercalary heterochromatin (Posukh et al., 2015). We propose that global epigenetic modifications observed in the SuUR mutant likely do not directly arise from derepression of the replisome as suggested but, rather, result from the coordinate insulator-dependent regulatory functions of SUUR in both the establishment of a chromatin barrier and DNA replication control (Figure 6B and C).

### Architectural proteins can attenuate replication forks and regulate replication timing

Our work demonstrates for the first time that insulator complexes assembled on chromatin can attenuate the extent of replication in discrete regions of the salivary gland polyploid genome. Despite distinct cell cycle programs in dividing and endoreplicating cells (Zielke et al., 2013), the core biochemical composition of replisomes in both cell types is likely similar. Although the putative relationship is limited by a paucity of comparative biochemical analyses of replication factors in different cell types, related insulator-driven control mechanisms for DNA replication may be conserved in endoreplicating and mitotically dividing diploid cells. Our data thus implicates insulator/chromatin boundary elements as a critical attribute of DNA replication control. Our model suggests that delayed replication of repressed chromatin (e.g., intercalary heterochromatin) during very late S phase can be imposed in a simple, two-component mechanism (Figure 6C). First, it requires that an extended genomic domain be completely devoid of functional origins of replication. The assembly and licensing of proximal pre-RC complexes can be repressed epigenetically or at the level of DNA sequence. Second, this domain is separated from flanking chromatin by a barrier element associated with an insulator complex, such as SUMM4. This structural organization is capable of preventing or delaying the entry of external forks fired from distal origins.

An important frequent feature of the partially suppressed underreplication in mod(mdg4) animals is its asymmetry (Figure 7D, Figure 7—figure supplement 1B), which is consistent with a unidirectional penetration of the underreplicated domain by a replication fork firing from the nearest external origin (Figure 6C). The SUMM4-dependent barrier may be created as a direct physical obstacle to MCM2-7 DNA-unwinding helicase or other enzymatic activities of the replisome. Alternatively, SUMM4 may inhibit the replication machinery indirectly by assembling at the insulator a DNA/chromatin structure that is incompatible with replisome translocation. This putative inhibitory structure may involve epigenetic modifications of chromatin as proposed earlier (Gaszner and Felsenfeld, 2006), linker histone H1 as shown previously (Andreyeva et al., 2017) and may also be dependent on Rif1, a negative DNA replication regulator that acts downstream of SUUR (Munden et al., 2018).

In conclusion, we used a newly developed MERCI approach to identify a stable stoichiometric complex termed SUMM4 that comprises SUUR, a previously known negative effector of replication, and Mod(Mdg4), an insulator protein. SUMM4 subunits cooperate to mediate transcriptional repression and chromatin boundary functions of gypsy-like (class 3) insulators (Schwartz et al., 2012) and inhibit DNA replication likely by slowing down replication fork progression through the boundary element. Thus, SUMM4 is required for coordinate regulation of gene expression, chromatin partitioning, and DNA replication timing. The insulator-dependent regulation of DNA replication offers a novel mechanism for the establishment of replication timing in addition to the currently accepted paradigm of variable timing of replication origin firing.

## Materials and methods

### Recombinant proteins

Recombinant proteins were expressed in Sf9 cells using baculovirus system (SUUR, Mod(Mdg4), EGG, and WDE), in Escherichia coli (ISWI, ModT antigen, and LCMS reference proteins), or obtained from EpiCypher Inc (human BRG1/SMARCA4).

### Sf9 cells

All baculovirus constructs were cloned by PCR with Q5 DNA polymerase (New England Biolabs) and ligation or Gibson assembly with NEBuilder HiFi DNA Assembly Cloning kit (New England Biolabs) into pFastBac vector (Thermo Fisher) under the control of polyhedrin promoter. All constructs were validated by Sanger sequencing. Baculoviruses were generated according to the protocol by Thermo Fisher. The baculoviruses were isolated by plaque purification, amplified three times, and their titers were measured by plaque assay. FLAG-SUUR construct was cloned from SuUR-RA cDNA (LD13959, DGRC). The following open-reading frame (ORF) was expressed: MDYKDDDDKH-SUUR-PA(1..962)-VEACGTKLVEKY*. To generate ATPase-dead mutant, SUUR-PA(K59) codon was replaced with an alanine codon by PCR and Gibson cloning. Mod(Mdg4)-67.2-V5-His6 and Mod(Mdg4)-59.1-V5-His6 constructs were cloned from cDNAs mod(mdg4)-RT and mod(mdg4)-RI synthesized as gBlocks by IDT, Inc. The following ORFs were expressed: Mod(Mdg4)-67.2 (1..610)-GILEGKPIPNPLLGLDSTGASVEHHHHHH* and Mod(Mdg4)-59.1 (1..541)-GILEGKPIPNPLLGLDSTGASVEHHHHHH*. EGG-FLAG and EGG (untagged) were cloned by PCR from egg-RA cDNA (IP14531). The following ORF was expressed: EGG-PA(1..1262)-DYKDDDDK* and EGG-PA(1..1262)-*. FLAG-WDE was cloned by PCR from wde-RA cDNA (LD26050). The following ORF was expressed: MDYKDDDDK-WDE-PA(2..1420)-*. The sequences of FLAG and V5 tags are highlighted in bold typeface.

Cells, 2•106/ml in Sf-900 II SFM medium (Gibco), were infected at multiplicity of infection (MOI) of ~10 in PETG shaker flasks (Celltreat, Inc). After infection for 48–72 hr at 27°C, cells were harvested, and recombinant proteins were purified by FLAG or Ni-NTA affinity chromatography (Fyodorov and Kadonaga, 2003). Whereas, typically, amplified baculovirus stocks had titers above 5•109 pfu/ml, FLAG-SUUR viruses reached no more than 2–4•108 pfu/ml, presumably due to the inhibitory effect of overexpressed protein on viral DNA replication. Accordingly, whereas typical yields of purified recombinant proteins were >100 µg from 1 L Sf9 cell culture, SUUR polypeptides were produced at no more than 2 µg from 1 L culture, which also adversely affected the protein purity (Figures 1C and 3A, Figure 3—figure supplement 1A and B).

### E. coli

The expression construct for untagged recombinant Drosophila ISWI was prepared from a full-length ISWI cDNA (Ito et al., 1999). Human TXNRD1 sequence was cloned from a cDNA provided by Addgene (#38863), and TXNRD2 was synthesized as a gBlock gene fragment by IDT, Inc. The ORFs were inserted by Gibson cloning in a pET backbone vector in frame with a C-terminal intein-CBD (chitin-binding domain) tag. Protein expression was induced by IPTG in Rosetta 2 cells, and proteins were purified in non-denaturing conditions by chitin affinity chromatography and intein self-cleavage as described (Emelyanov et al., 2014), followed by anion-exchange chromatography (Source 15Q) on FPLC (see below). Note that the cloned human thioredoxin reductase ORFs do not express the C-terminal selenocysteines. They were thus presumed catalytically inactive (Arnér et al., 1999; Cheng and Arnér, 2017) and designated hTXNRD1ci and hTXNRD2ci. They were used exclusively as spike-in mass standards in LCMS acquisitions of Drosophila proteins.

Polypeptide corresponding to the C-terminal specific region of Mod(Mdg4)-67.2 was cloned in pET24b vector in frame with a C-terminal His6 tag. M-Mod(Mdg4)-67.2 (403..610)-GILEHHHHHH* was expressed in Rosetta 2 and purified by Ni-NTA affinity chromatography in non-denaturing conditions. The polypeptide (ModT) was dialyzed into PBS (137 mM NaCl, 3 mM KCl, 8 mM NaH2PO4, 2 mM KH2PO4) and used as an antigen for immunizations (see below). All recombinant proteins were examined by SDS-PAGE along with Pierce BSA mass standards (Thermo Fisher), and their concentrations were calculated from infrared scanning of Coomassie-stained gels (Odyssey Fc Imaging System, LI-COR Biosciences). Detailed cloning and purification methods are provided below.

### Molecular cloning

#### pFastBac-FLAG-SUUR

The coding sequence was amplified from LD13959 by PCR using the following primers: NdeI-SUURf, TCCATATGTATCACTTTGTATCCGAGCAAAC and Sal1-SUURr, AAGTCGACCTTGAACAGTTCCAATCGCTTTC (NdeI and SalI restriction sites are underlined). The PCR product was digested with NdeI and SalI and ligated with the vector produced by NdeI-XhoI digestion of pFastBac-Flag-ATRX construct (Emelyanov et al., 2010).

#### pFastBac-FLAG-SUUR(K59A)

The complete pFastBac-FLAG-SUUR construct was amplified by PCR using the following primers: SUUR-KAf, CTTGGGCAGGTCGCTACGGTGGCGG and SUUR-KAr, GTAGCGACCTGCCCAAGGCCACTCTCATCATTCAGG (mutated residues are underlined). The linear PCR product was re-circularized by Gibson assembly.

#### pFastBac-Mod(Mdg4)-67.2-V5-His6

The following gBlock (MMD4-RT) was synthesized by IDT, Inc: CGAAGCGCGCGGAATTCATATGGCCGATGACGAACAGTTTTCGCTGTGCTGGAACAACTTTAACACAAATTTGTCGGCAGGATTTCACGAGAGTCTCTGTCGGGGCGACTTGGTAGACGTCTCCTTGGCAGCAGAGGGACAAATTGTCAAGGCCCATCGTCTGGTACTCTCCGTCTGCAGCCCATTTTTTCGGAAAATGTTCACTCAGATGCCAAGCAACACTCACGCCATAGTATTTCTGAACAATGTTAGTCACAGCGCTTTGAAAGATCTGATCCAATTTATGTATTGTGGCGAAGTGAACGTTAAGCAAGACGCATTGCCGGCATTTATCTCCACTGCAGAAAGTCTGCAAATTAAAGGATTGACCGATAACGACCCAGCTCCGCAACCCCCACAAGAGAGCTCGCCACCTCCCGCTGCGCCTCATGTGCAGCAACAGCAAATCCCAGCCCAGCGGGTGCAACGACAACAGCCGCGTGCTAGCGCCCGCTATAAAATTGAGACTGTGGATGATGGACTGGGCGACGAAAAACAAAGTACCACTCAGATTGTTATCCAAACAACAGCTGCCCCGCAAGCAACTATTGTTCAACAACAACAGCCTCAACAAGCTGCACAACAAATACAGTCGCAACAGTTGCAGACAGGTACAACAACAACTGCAACATTGGTAAGTACTAATAAGAGGAGTGCTCAGCGCTCGTCCCTGACGCCGGCGTCCAGTAGTGCGGGTGTTAAAAGGAGTAAGACAAGCACTAGCGCAAACGTGATGGATCCGCTGGATTCGACTACGGAGACAGGCGCAACTACAACGGCTCAACTGGTACCTCAGCAAATCACTGTACAAACATCCGTTGTCAGCGCTGCTGAGGCGAAGCTCCATCAGCAGAGTCCCCAACAGGTTCGCCAGGAAGAGGCGGAGTATATAGATCTGCCTATGGAGCTGCCGACCAAGTCGGAACCGGATTACTCGGAAGATCATGGCGACGCGGCCGGTGACGCTGAGGGTACGTATGTCGAGGATGATACGTACGGTGACATGCGATACGACGATTCCTATTTTACAGAAAATGAGGACGCAGGCAACCAGACGGCCGCCAATACAAGCGGAGGTGGCGTGACAGCGACCACTAGCAAAGCTGTTGTGAAACAACAGTCGCAGAACTATTCGGAGAGTAGTTTCGTAGATACCAGTGGCGACCAAGGTAACACCGAGGCACAGGCAGCCACAAGTGCTTCGGCGACCAAGATTCCGCCCCGGAAACGGGGTCGACCGAAAACAAAAGTTGAGGACCAGACCCCTAAACCTAAATTGCTtGAGAAGTTGCAGGCCGCAACACTGAACGAGGAAGCAAGTGAACCGGCCGTATATGCGTCGACCACGAAAGGCGGTGTTAAACTGATATTTAACGGCCATTTGTTTAAATTCTCGTTTAGGAAAGCGGATTACAGTGTCTTCCAGTGTTGTTATAGGGAGCATGGTGAAGAGTGCAAGGTCAGGGTCGTCTGCGATCAAAAGCGTGTATTTCCTTACGAGGGTGAACACGTGCACTTCATGCAAGCTTCCGATAAGTCCTGCCTCCCTAGTCAGTTCATGCCAGGTGAGTCCGGTGTCATTTCCAGTTTGAGCCCATCGAAAGAGCTCTTGATGAAGAATACCACTAAGCTCGAAGAGGCGGATGATAAGGAAGACGAAGATTTCGAAGAGTTTGAGATCCAAGAAATAGACGAGATAGAATTGGACGAACCGGAGAAGACCCCCGCAAAGGAAGAAGAAGTTGACCCGAACGACTTTCGGGAGAAGATTAAGCGACGGCTCCAGAAGGCCTTGCAAAACAAAAAGAAAGGAATTCTCGAGGGTAAGCCTATCCCTAACCCTCTCCTCGGTCTCGATTCTACCGGTGCTAGCGTCGAGCACCACCACCACCACCACTGAGATCCGGCTGCTAAC (sequence coding for V5 tag is underlined; translation initiation/termination codons and codon 610 of mod(mdg4)-RT are shown in bold). The vector fragment was amplified by PCR from pFastBac by using the following primers: His-Stop-Vf, CACTGAGATCCGGCTGCTAAC and NdeI-Vr, CATATGAATTCCGCGCGCTTC. The expression construct was assembled by Gibson cloning.

#### pFastBac-Mod(Mdg4)-59.1-V5-His6

The following gBlock (MMD4-RI) was synthesized by IDT, Inc: GGTAACACCGAGGCACAGGTATGTGATGATCTCGATGACATGAAAGGCGCTATTAAGCATAGCCTGTTGACTTTTATTCGCGGTCAGCGCGGCTGCAAACTGCTGGCTTTTAACGGTCATAATTATGTTCGTAACAGGCGTTCCAATCTCAAGACGTATTGGATATGCAGCAAAAAAGGCAGCACTAAATGCAACGCTCGTGTTGTTACAAACGTAGTTGAGGGTGTTCACAAGATAGTTCTGGAAAGTTGCCATCATACGTGTCTGAACACCGAGAGGAAGAAAAGGCTCTCGGTGACTAATGTAGTAGGAAAAGCGCGGTCGAAGTCCGAAAAAAGTGTATCCACGGGCTTTATTAAAGAAGAAGGAGACGAGGACCTCACGTTGGAATTGCGGACCCTCAACCTGTCGATTGAGGATCTGAATAACCTCCAGGGAATTCTCGAGGGTAAGCC (sequence corresponding to V5 tag is underlined; variant-specific codons 403–541 of mod(mdg4)-RI are shown in bold). The vector fragment additionally encompassing mod(mdg4) codons 1–402 were amplified by PCR from pFastBac-Mod(Mdg4)-67.2-V5-His6 by using the following primers: GIL-V5f, GGAATTCTCGAGGGTAAGCC and MMD397-402r, CCTGTGCCTCGGTGTTACC. The expression construct was assembled by Gibson cloning.

### pFastBac-EGG (untagged)

pFastBac-ATRX (untagged) construct (Emelyanov et al., 2010) was digested with EcoRI and XhoI. The vector fragment (4.7 kbp) was ligated with a 4 kbp EcoRI-XhoI fragment of egg-RA cDNA (IP14531).

#### pFastBac-EGG-FLAG

Double-stranded oligonucleotide was produced by annealing ApaI-FLAG-AflII-f, CCCAATTGCCGCCTTCGTCTGCTCGATTACAAGGATGATGATGACAAATAAC and AflII-FLAG-ApaI-r, TTAAGTTATTTGTCATCATCATCCTTGTAATCGAGCAGACGAAGGCGGCAATTGGGGGCC (sticky ends are underlined; sequences corresponding to FLAG tag are shown in bold; stop codon is in bold and italics) was cloned into ApaI-AflII-digested IP14531 by ligation. The resulting construct was digested with EcoRI and XhoI, and the 4 kbp EGG-FLAG fragment was cloned into pFastBac as described above.

#### pFastBac-FLAG-WDE

pFastBac-ATRX (untagged) construct (Emelyanov et al., 2010) was digested with NdeI and NcoI. The vector fragment additionally encompassing 1.1 kbp of ATRX cDNA sequence with a XhoI site (5.8 kbp total) was ligated with a double-stranded oligonucleotide produced by annealing NdeI-FLAG-NcoI-f, TATGGATTACAAGGATGATGATGACAAAATGGGAGTAAACCAGAC and NcoI-FLAG-NdeI-r, CATGGTCTGGTTTACTCCCATTTTGTCATCATCATCCTTGTAATCCA (sticky ends are underlined; sequences corresponding to FLAG tag are shown in bold). A 4.6 kbp NcoI-XhoI fragment of wde-RA cDNA (LD26050) was cloned in the resulting construct by restriction digest and ligation.

### pET24-ISWI-intein-CBD

ISWI cDNA was amplified from pFastBac-ISWI construct (Ito et al., 1999) by PCR using the following primers: NdeI-ISWIf, GTTTCATATGGCTAGCAAAACAGATAC and XhoI-ISWIr, GGAAGGTACCCTTGGCAAAGCACCCCTTCTTCTTCTTTTTC (NdeI and XhoI sites are underlined; sequences corresponding to the ISWI ORF are shown in bold). The 3.1 kbp PCR fragment was digested with NdeI and XhoI and cloned into pET24-intein-CBD construct in place of Protamin B (Emelyanov et al., 2014) by ligation.

#### pET24-hTXNRD1ci-intein-CBD

Human TXNRD1 cDNA (Addgene #38863) was amplified by PCR using the following primers:

NdeI-hTXNRD1f, AACATATGAACGGCCCTGAAGATCTTC and SalI-hTXNRD1r, TAGTCGACGCAGCCAGCCTGGAGG (NdeI and SalI sites are underlined; sequences corresponding to the TXNRD1 ORF are shown in bold). The 1.5 kbp PCR fragment was digested with NdeI and SalI and cloned into NdeI and XhoI sites of pET24-intein-CBD construct in place of Protamin B (Emelyanov et al., 2014) by ligation.

#### pET24-hTXNRD2ci-intein-CBD

The following gBlock (TXNRD2) was synthesized by IDT, Inc: TTTTCATATGGAAGATCAGGCGGGCCAGCGCGATTATGATCTGCTGGTGGTGGGCGGCGGCAGCGGCGGCCTGGCGTGCGCGAAAGAAGCGGCGCAGCTGGGCCGCAAAGTGGCGGTGGTGGATTATGTGGAACCGAGCCCGCAGGGCACCCGCTGGGGCCTGGGCGGCACCTGCGTGAACGTGGGCTGCATTCCGAAAAAACTGATGCATCAGGCGGCGCTGCTGGGCGGCCTGATTCAGGATGCGCCGAACTATGGCTGGGAAGTGGCGCAGCCGGTGCCGCATGATTGGCGCAAAATGGCGGAAGCGGTGCAGAACCATGTGAAAAGCCTGAACTGGGGCCATCGCGTGCAGCTGCAGGATCGCAAAGTGAAATATTTTAACATTAAAGCGAGCTTTGTGGATGAACATACCGTGTGCGGCGTGGCGAAAGGCGGCAAAGAAATTCTGCTGAGCGCGGATCATATTATTATTGCGACCGGCGGCCGCCCGCGCTATCCGACCCATATTGAAGGCGCGCTGGAATATGGCATTACCAGCGATGATATTTTTTGGCTGAAAGAAAGCCCGGGCAAAACCCTGGTGGTGGGCGCGAGCTATGTGGCGCTGGAATGCGCGGGCTTTCTGACCGGCATTGGCCTGGATACCACCATTATGATGCGCAGCATTCCGCTGCGCGGCTTTGATCAGCAGATGAGCAGCATGGTGATTGAACATATGGCGAGCCATGGCACCCGCTTTCTGCGCGGCTGCGCGCCGAGCCGCGTGCGCCGCCTGCCGGATGGCCAGCTGCAGGTGACCTGGGAAGATAGCACCACCGGCAAAGAAGATACCGGCACCTTTGATACCGTGCTGTGGGCGATTGGCCGCGTGCCGGATACCCGCAGCCTGAACCTGGAAAAAGCGGGCGTGGATACCAGCCCGGATACCCAGAAAATTCTGGTGGATAGCCGCGAAGCGACCAGCGTGCCGCATATTTATGCGATTGGCGATGTGGTGGAAGGCCGCCCGGAACTGACCCCGACCGCGATTATGGCGGGCCGCCTGCTGGTGCAGCGCCTGTTTGGCGGCAGCAGCGATCTGATGGATTATGATAACGTGCCGACCACCGTGTTTACCCCGCTGGAATATGGCTGCGTGGGCCTGAGCGAAGAAGAAGCGGTGGCGCGCCATGGCCAGGAACATGTGGAAGTGTATCATGCGCATTATAAACCGCTGGAATTTACCGTGGCGGGCCGCGATGCGAGCCAGTGCTATGTGAAAATGGTGTGCCTGCGCGAACCGCCGCAGCTGGTGCTGGGCCTGCATTTTCTGGGCCCGAACGCGGGCGAAGTGACCCAGGGCTTTGCGCTGGGCATTAAATGCGGCGCGAGCTATGCGCAGGTGATGCGCACCGTGGGCATTCATCCGACCTGCAGCGAAGAAGTGGTGAAACTGCGCATTAGCAAACGCAGCGGCCTGGATCCGACCGTGACCGGCTGCCTCGAGTTTTTTTTTT (NdeI and XhoI sites are underlined; translation initiation codon and codon 492 of hTXNRD2 are shown in bold). The DNA fragment was digested with NdeI and XhoI and cloned by ligation in pET24-intein-CBD as described above.

#### pET24-ModT-His6

Mod(Mdg4)-67.2-specific fragment of mod(mdg4)-RT cDNA was amplified from pFastBac-Mod(Mdg4)-67.2-V5-His6 by PCR using the following primers: NdeI-ModTf, CCGAGCATATGGCAGCCACAAGTGCTTC and XhoI-ModTr, GGGTAGGCTTACCCTCGAGAATTCCTTTC (NdeI and XhoI sites are underlined). The 0.6 kbp PCR fragment was digested with NdeI and XhoI and cloned in pET24b (Millipore/Sigma) by ligation.

### FPLC purification of recombinant ISWI, hTXNRD1ci, and hTXNRD2ci

Protein samples eluted from the chitin resin (1–5 ml total sample volume) were diluted threefold with chromatographic Buffer A (Figure 1—source data 1) and injected on a 0.5 ml Source 15Q equilibrated to 5% Buffer B (Figure 1—source data 1) + 95% Buffer A. The column was washed with 20 cv (column volumes) of 5% Buffer B, and proteins were eluted with a 20 cv linear gradient of 5–100% Buffer B. 200 µl fractions were collected and analyzed by SDS-PAGE. Three to five peak fractions were pooled, aliquoted, flash-frozen in liquid nitrogen, and stored at –80°C.

### Crude cell extracts

#### Nuclear extract from Drosophila embryos

Approximately 1 kg or approximately 200 g wild-type (Oregon R) Drosophila embryos were collected 0–12 hr after egg deposition (AED) from population cages. The embryos were dechorionated, and nuclear extracts were prepared as described (Kamakaka et al., 1991). Protein concentration was measured by Pierce BCA assay (Thermo Fisher). The extracts were fractionated by FPLC (Figure 1A, Figure 4—figure supplement 2A) on AKTA PURE system (Cytiva Life Sciences). Aliquots of chromatographic fractions were examined by quantitative shotgun proteomics or Western blot analyses as described below. Peak SUUR or Mod(Mdg4) fractions were diluted to an appropriate ionic strength (if applicable) and used as a starting material for the next chromatographic step. Details on FPLC column sizes and run parameters are shown in Figure 1—source data 1 and Figure 4—figure supplement 2—source data 1.

#### E. coli lysate

A 40 ml Rosetta 2 overnight culture was harvested by centrifugation, resuspended in 20 ml HEG (25 mM HEPES, pH 7.6, 0.1 mM EDTA, 10% glycerol) supplemented with 0.1 M KCl, 1 mM DTT, and 2 mM CaCl2. Cells were disrupted by sonication and centrifuged to remove insoluble material. Nucleic acids were digested with 15 units micrococcal nuclease (Sigma-Aldrich) for 20 min at 37°C, and the proteins were precipitated with 2 M ammonium sulfate. The pellet was resuspended in 10 ml HEG + 0.1 M KCl +1 mM DTT with protease inhibitors (0.5 mM benzamidine, 0.2 mM PMSF) and dialyzed against the same buffer. After centrifugation, the concentration of soluble protein was measured by BCA assay, the E. coli lysate was diluted to 1 mg/ml using 100 mM ammonium bicarbonate (ABC) and stored at –80°C.

### Mass-spectroscopy samples

#### Column fractions

For each chromatographic step, 14–20 fractions were selected based on the protein fractionation profile according to the UV (A280) absorbances measurements. 50–100 µl aliquots of chromatographic fractions, starting material (SM) and column flow-through (FT, if applicable) were saved, and protein concentrations were estimated based on their UV absorbances (1000 mU A280 was considered to be equivalent to 5 mg/ml total protein). Equal volumes of each fraction, SM, and FT were used for MS acquisitions, so that no more than 40 µg total protein was processed in each reaction. As a reference, the reactions were supplemented with 1.5 µg each of purified recombinant human thioredoxin reductases 1 and 2 (hTXNRD1ci and hTXNRD2ci, catalytically inactive) expressed in E. coli. Dithiotreitol (DTT) was added to the protein samples to 10 mM and NP-40 – to 0.02%. Reaction volumes were brought to 85 µl with 50 mM ABC. All reagents, including water, were HPLC/MS grade. The proteins were reduced for 1 hr at 37°C and then alkylated with 30 mM iodoacetamide (IAA, 15 µl 200 mM IAA in water) for 45 min at room temperature in the dark. Alkylated proteins were desalted into 50 mM ABC using ZebaSpin columns (40 kDa MWCO) and digested with 1 µg trypsin for 2 hr at 37°C. 1 µg more trypsin was added, and the digestion progressed at 37°C overnight. Tryptic peptides were lyophilized for 2 hr on SpeedVac with heat and resuspended in 100 µl Sample Buffer: 1% acetonitrile (ACN) and 0.1% formic acid (FA) in water. Equal volumes (23 µl) of samples were used for IDA and SWATH acquisitions (in triplicate) as described below.

### Recombinant SUUR

To generate the recombinant SUUR reference spectral library (ILR), ~0.5 µg purified recombinant FLAG-SUUR (both 130 and 65 kDa bands, Figure 1C) was mixed with 1.5 µg each of hTXNRD1ci and hTXNRD2ci and processed for an IDA as described above, except for 0.5 µg trypsin was used in each cleavage step, and the peptide sample was resuspended in 30 µl Sample Buffer. For SWATH titration of SUUR (Figure 1—figure supplement 1B), 1 µg recombinant FLAG-SUUR was mixed with 25 µg E. coli lysate protein and 1.5 µg each of hTXNRD1ci and hTXNRD2ci. Tenfold serial dilutions down to 10 fg SUUR were also prepared using the mixture of E. coli lysate with reference proteins. The samples were processed for SWATH acquisitions in triplicate as described above, 30 µl of sample per injection.

### In-gel digestion of recombinant proteins for LCMS identification

Recombinant SUUR or SUMM4 purified by FLAG immunoaffinity chromatography was resolved on SDS-PAGE, stained with Coomassie Blue (Figures 1C and 3A, Figure 3—figure supplement 1A), and up to eight most prominent protein bands were excised. The gel slices were transferred to 1.5 ml Eppendorf tubes, gently crushed with a RotoDounce pestle, and destained with 25 mM ABC in 50% methanol and then with 25 mM ABC in 50% ACN (30 min each at room temperature). The proteins were reduced in 50 µl 10 mM DTT for 1 hr at 55°C and alkylated with 30 mM IAA for 45 min at room temperature in the dark. The gel fragments were washed with 25 mM ABC in 50% ACN, dehydrated with 100% ACN, dried in a SpeedVac, rehydrated by addition of 50 µl 50 mM ABC, and digested with 0.25 µg trypsin overnight at 37°C. The peptides were extracted once with 50 µl 10% FA and once with 100 µl 3% FA in 60% ACN, both extracts were combined, dried in a SpeedVac and resuspended in 50 µl Sample Buffer. Then, 40 µl of each sample was injected for IDA as described below.

### Mass-spectroscopy acquisition methods

LC-MS/MS analyses were performed on a TripleTOF 5600+ mass spectrometer (AB SCIEX) coupled with M5 MicroLC system (AB SCIEX/Eksigent) and PAL3 autosampler.

#### Instrument settings

LC separation was performed in a trap-elute configuration, which consists of a trapping column (LUNA C18(2), 100 Å, 5 μm, 20 × 0.3 mm cartridge, Phenomenex) and an analytical column (Kinetex 2.6 µm XB-C18, 100 Å, 50 × 0.3 mm microflow column, Phenomenex). The mobile phase consisted of water with 0.1% FA (phase A) and 100% ACN containing 0.1% FA (phase B). Then, 200 ng to 10 μg total protein was injected for each acquisition. Peptides in Sample Buffer were injected into a 50 µl sample loop, trapped and cleaned on the trapping column with 3% mobile phase B at a flow rate of 25 μl/min for 4 min before being separated on the analytical column with a gradient elution at a flow rate of 5 μl/min. The gradient was set as follows: 0–48 min: 3% to 35% phase B, 48–54 min: 35% to 80% phase B, 54–59 min: 80% phase B, 59–60 min: 80% to 3% phase B, and 60–65 min at 3% phase B. An equal volume of each sample (23 µl) was injected four times, once for information-dependent acquisition (IDA), immediately followed by DIA/SWATH in triplicate. Acquisitions of distinct samples were separated by a blank injection to prevent sample carryover. The mass spectrometer was operated in positive ion mode with EIS voltage at 5200 V, Source Gas 1 at 30 psi, Source Gas 2 at 20 psi, Curtain Gas at 25 psi, and source temperature at 200°C.

#### IDA and data analyses

IDA was performed to generate reference spectral libraries for SWATH data quantification. The IDA method was set up with a 250 ms TOF-MS scan from 400 to 1250 Da, followed by MS/MS scans in a high-sensitivity mode from 100 to 1500 Da of the top 30 precursor ions above 100 cps threshold (100 ms accumulation time, 100 ppm mass tolerance, rolling collision energy, and dynamic accumulation) for charge states (z) from +2 to +5. IDA files were searched using ProteinPilot (version 5.0.2, ABSciex) with a default setting for tryptic digest and IAA alkylation against a protein sequence database. The Drosophila proteome FASTA file (21,970 protein entries, UniProt UP000000803, 3/21/2020) augmented with sequences for common contaminants as well as hTXNRD1 and hTXNRD2 was used as a reference for the search. Up to two missed cleavage sites were allowed. Mass tolerance for precursor and fragment ions was set to 100 ppm. A false discovery rate (FDR) of 5% was used as the cutoff for peptide identification.

#### SWATH acquisitions and data analyses

For SWATH (SWATH-MS, Sequential Window Acquisition of All Theoretical Mass Spectra) acquisitions (Zhu et al., 2014), one 50 ms TOF-MS scan from 400 to 1250 Da was performed, followed by MS/MS scans in a high-sensitivity mode from 100 to 1500 Da (15 ms accumulation time, 100 ppm mass tolerance, +2 to +5 z, rolling collision energy) with a variable-width SWATH window (Zhang et al., 2015). DIA data were quantified using PeakView (version 2.2.0.11391, ABSciex) with SWATH Acquisition MicroApp (version 2.0.1.2133, ABSciex) against selected spectral libraries generated in ProteinPilot. Retention times for individual SWATH acquisitions were calibrated using 20 or more peptides for hTXNRD1ci and hTXNRD2ci. The following software settings were utilized: up to 25 peptides per protein, 6 transitions per peptide, 95% peptide confidence threshold, 5% FDR for peptides, XIC extraction window 20 minutes, and XIC width 100 ppm. Protein peak areas were exported as Excel files (Supplementary file 2) and processed as described below.

### MERCI

MERCI is a novel approach for rapid identification of native protein complexes. It combines enrichment for a target subunit of a putative complex by consecutive FPLC steps and quantitative shotgun proteomics of chromatographic fractions. Crude nuclear extract from Drosophila embryos was fractionated as in Figure 1A and Figure 1—source data 1. At every step, 40 µg or less total protein from each of 10–20 fractions (equal volumes) was supplemented with a fixed amount (1.5 µg each) of exogenous reference proteins (human thioredoxin reductases), reduced, alkylated, and digested with trypsin (see above). MS1 and MS2 spectra of tryptic peptides were acquired by IDA, and relative SUUR abundance in fractions was measured by DIA/SWATH in triplicate. SWATH data were quantified using cognate IDA-derived ion libraries. Protein areas for all quantified proteins were normalized to the sum of those for reference proteins. The relative numbers were averaged across triplicates, with standard deviations calculated. The average numbers for all quantified proteins were further normalized by converting them to Z-scores (see Supplementary file 2 for an example of calculations). Peak SUUR fractions (1–5) were then subjected to the next FPLC/MERCI step. After five column steps, the IL from the ultimate FPLC step (IL5) was used to requantify SWATH data from all steps. Z-scores for all purification steps were stitched together, and the large array encompassing all data points for every protein was analyzed by Pearson correlation with SUUR (Supplementary file 2). The most closely correlated purification profiles served as an indication for protein co-purification, potentially, as subunits of a stable complex.

### Biochemical assays with recombinant proteins

#### Oligonucleosome substrates

Oligonucleosomes were reconstituted in vitro as described (Lu et al., 2013) from supercoiled plasmid DNA (3.2 kb, pGIE-0), native core histones and H1 prepared from Drosophila embryos (Fyodorov and Levenstein, 2002) by gradient salt dialysis in the presence of 0.2 mg/ml nuclease-free bovine serum albumin (BSA, New England Biolabs). Quality of reconstitution was assessed by SDS-PAGE (Figure 3—figure supplement 1C), MNase (Figure 3—figure supplement 1D), and chromatosome stop assays (Figure 3—figure supplement 1E).

#### ATPase assay

40 nM recombinant proteins were incubated in 25 µl reaction buffer containing 20 mM HEPES, pH 7.6, 0.15 M NaCl, 4 mM MgCl2, 1 mM ATP, 0.1 mM EDTA, 0.02% (v/v) NP-40, and 0.1 mg/ml nuclease-free BSA for 60 min at 27°C. Some reactions additionally contained 10 nM pGIE-0 plasmid DNA or equivalent amounts of oligonucleosomes ± H1. ATPase assays were performed using ADP-Glo Max kit (Promega). All reactions were performed in triplicate, the results were normalized to the ADP-ATP titration curve according to the kit manual and converted to enzymatic rates (molecules of ATP hydrolyzed per molecule of enzyme per minute). Averages and standard deviations were calculated. Statistical differences were calculated by Mann–Whitney test.

#### EpiDyne-PicoGreen nucleosome remodeling assay

EpiDyne-PicoGreen is a restriction enzyme accessibility assay modified for increased throughput and sensitivity (Figure 3—figure supplement 2A). Briefly, a recombinant ATPase over a concentration range (Figure 3—figure supplement 2B–E) was mixed with 10 nM EpiDyne biotinylated nucleosome remodeling substrate (EpiCypher), terminally positioned 6-N-66 (217 bp fragment) or centrally positioned 50-N-66 (263 bp) and 1 mM ATP in 20 µl remodeling buffer, 20 mM Tris-HCl, pH 7.5, 50 mM KCl, 3 mM MgCl2, 0.01% (v/v) Tween-20, 0.01% (w/v) BSA. The remodeling reactions were incubated at 23°C in 384-well format. At indicated time points, the reactions were quenched, and nucleosome substrates were immobilized on an equal volume of streptavidin-coated magnetic beads (NEB), pre-washed and resuspended in 2× quench buffer, 20 mM Tris-HCl, pH 7.5, 600 mM KCl, 0.01% (v/v) Tween-20, and 0.01% (w/v) BSA. Beads were successively washed by collection on a magnet (three times with wash buffer, 20 mM Tris-HCl, pH 7.5, 300 mM KCl, 0.01% [v/v] Tween-20) and buffer replacement (once with RE buffer, 20 mM Tris-HCl, pH 7.5, 50 mM KCl, 3 mM MgCl2, 0.01% [v/v] Tween-20). Beads were resuspended in 20 µl restriction enzyme mix, 50 units/ml Dpn II (NEB) in RE buffer, and incubated at 23°C for 30 min, collected on a magnet, and supernatants from all wells were transferred to a new plate. They were mixed with an equal volume of Quant-iT PicoGreen dsDNA reagent (Thermo Fisher, Component A) and 1 unit/ml thermolabile proteinase K (NEB) in TE and incubated at 23°C for 1 hr. Fluorescence intensity was detected on an EnVision microplate reader with excitation at 480 nm and emission at 531 nm, and data expressed as relative fluorescence units (RFUs) through the EnVision Workstation (version 1.13.3009.1409).

### Drosophila population culture, mutant stocks, and genetics

Wild-type (Oregon R) flies were maintained in population cages on agar-grape juice and yeast paste plates at 26°C, 60% humidity with 12 hr dark–light cycle. Mutant flies were reared, and crosses were performed at 26°C on standard cornmeal/molasses medium with dry yeast added to the surface. SuURES was a gift of Igor Zhimulev, and mod(mdg4)m9 was a gift of Yuri Schwartz. All other alleles were obtained from the Bloomington Stock Center, Indiana. Combinations of alleles were produced either by crosses with appropriate balancers and segregation of markers or by female germline meiotic recombination. Intra-chromosomal recombination events were confirmed by PCR of genomic DNA. To genotype SuURES, mod(mdg4)u1 recombined chromosomes, the following PCR primers were used: SUUR-Fwd: CCTCAAAGAACAGCCAGAGC; SUUR-Rev: TTTGCTACTTCTGGGCGTTT; diver-Rev: TCAGTTTGAACTCGCACCAG; Mod-Fwd: CAGGGCCACACGCACTTAC; Mod-Rev: GTGAAGCCCTTAGGCAGCTC; and Stalker-Rev: GCTTGCAGCACAGTTAGCAC. SUUR-Fwd/SUUR-Rev combination of primers produced a 770 bp PCR product for wild-type SuUR. SUUR-Fwd/diver-Rev combination produced an ~850 bp PCR product for SuURES. Mod-Fwd/Mod-Rev combination produced a 1532 bp PCR product for wild-type mod(mdg4). Mod-Fwd/Stalker-Rev combination produced an ~1700 bp PCR product for mod(mdg4)u1.

Fly wings were dissected from ~5-day-old adult males and transferred to a drop of PBS + 0.1% Triton X-100 (PBST). The wings were soaked in 80% glycerol in PBST and photographed using Zeiss AxioVert 200M microscope with EC Plan-Neofluar 2.5×/0.075 lens in bright field and CCD monochrome camera AxioCam MRm. For wing area measurements, images were processed using Fiji/ImageJ2 software package. Statistical differences were calculated by two-tailed t-test, assuming unequal variances. Adult fly eye images were taken on live, CO2-anesthetized 2-day-old females on Zeiss stereomicroscope Discovery.V12 using CCD color camera AxioCam MRc.

### Antibodies, immunoblots, and immunoprecipitation (IP)

Polyclonal antibody (anti-ModT) was raised in guinea pigs by Pocono Rabbit Farm & Lab. Rabbit polyclonal antibody to the C-terminus of Drosophila XNP/ATRX (anti-XNP) was described previously (Emelyanov et al., 2010). Rabbit and guinea pig polyclonal antibodies to Drosophila SUUR were a gift of Alexey Pindyurin (Nordman et al., 2014) and Igor Zhimulev (Pindyurin et al., 2008). Rabbit polyclonal Mod(Mdg4)-FL antibody to full-length Mod(Mdg4)-67.2 that recognizes all splice forms of Mod(Mdg4) was a gift of Jordan Rowley and Victor Corces. Mouse monoclonal anti-FLAG (M2, Sigma Aldrich), anti-PCNA (PC10, Cell Signaling), anti-β-tubulin and anti-HP1a (E7 and C1A9, Developmental Studies Hybridoma Bank) were obtained commercially.

Western blotting was performed using standard techniques. For FPLC column fraction analyses, 5–10 µl of starting material and flow-through (if applicable) and 5–15 µl of column fractions were loaded per lane. For expression analyses in salivary glands, 10 salivary glands from L3 larvae of indicated genotype were frozen and thawed, boiled extensively in 40 µl 2× SDS-PAGE loading buffer, centrifuged, and the material equivalent to four salivary glands was loaded per lane. The following dilutions were used: 1:200,000 anti-ModT, 1:1,000 anti-Mod(Mdg4)-FL, 1:1000 guinea pig and rabbit anti-SUUR, 1:1000 anti-HP1a, 1:1000 anti-β-tubulin, and 1:2000 anti-FLAG. Infrared-labeled secondary antibodies: donkey anti-guinea pig IRDye 800CW, goat anti-mouse IRDye 800CW, goat anti-rabbit IRDye 800CW, goat anti-rabbit IRDye 680CW, and goat anti-mouse IRDye 680RD were obtained from Li-COR Biosciences and used at 1:10,000. The blots were scanned on Odyssey Fc Imaging System (LI-COR Biosciences).

Immunoprecipitation experiments were performed as described (Emelyanov et al., 2012). 400 µl Drosophila embryonic nuclear extracts (~10 mg total protein) were incubated with 10 µl guinea pig anti-ModT, 30 µl rabbit anti-SUUR, or 20 µl rabbit anti-XNP antibodies for 3 hr at 4°C. Immunocomplexes were collected by addition of 25 µl protein A-agarose plus (Thermo Fisher) for 2 hr at 4°C. After washing four times with 1 ml of buffer HEG (25 mM HEPES, pH 7.6, 0.1 mM EDTA, 10% glycerol) + 0.15 M NaCl, the immunoprecipitated proteins were eluted with 80 µl 2× SDS-PAGE loading buffer and analyzed by SDS-PAGE and Western blot using guinea pig or rabbit anti-SUUR and anti-Mod(Mdg4) and mouse anti-HP1a antibodies. For Mod(Mdg4) and HP1a, 8 µl of immunoprecipitated material (equivalent to 1 mg nuclear extract proteins) and 5% input (2 µl nuclear extract, 50 µg total protein) were analyzed. For SUUR, 20 µl of immunoprecipitated material (equivalent to 2.5 mg nuclear extract proteins) and 10% input (10 µl nuclear extract, 250 µg total protein) were analyzed.

### Polytene chromosomes and indirect IF analyses

For all cytological experiments, larvae were reared and collected at 18°C. Polytene chromosomes and whole-mount salivary glands were prepared and analyzed as described previously (Andreyeva et al., 2017). Briefly, salivary glands from wandering third-instar larvae were dissected in PBS. Glands were transferred into a formaldehyde-based fixative (one ∼15 μl drop of 3% lactic acid, 45% acetic acid, 3.7% formaldehyde on a coverslip) for 2 min, squashed, and frozen in liquid N2. The coverslips were removed, and slides were placed in 70% ethanol for 20 min and stored at −20°C. The slides were washed three times for 5 min in PBST. Primary antibodies were incubated overnight at 4°C in PBST + 0.1% BSA and washed three times for 5 min each with PBST. Secondary antibodies were incubated for 2 hr at room temperature in PBST + 0.1% BSA and washed three times for 5 min each with PBST.

DNA was stained with 0.1 μg/ml DAPI in PBST for 3 min, and squashes were mounted in Prolong Glass anti-fade mountant (Molecular Probes). Primary and secondary antibodies were used at the following dilutions: guinea pig anti-ModT, 1:50,000; rabbit anti-SUUR, 1:100; mouse anti-PCNA, 1:1000; mouse anti-FLAG, 1:100; Alexa Fluor 488 highly cross-absorbed (HCA) goat anti-mouse, Alexa Fluor 568 HCA goat anti-guinea pig, and Alexa Fluor 647 plus HCA goat anti-rabbit (all Thermo Fisher), all 1:800. IF images were obtained with Zeiss AxioVERT 200M microscope and AxioCam MRm mono microscopy camera using a ×40/1.3 Plan-Neofluar or ×63x/1.40 Plan-Apochromat lenses with oil immersion. Images were acquired using AxioVision software.

For whole-mount IF staining, L3 larvae were reared at 26°C, and salivary glands were dissected in PBS and fixed in 3.7% formaldehyde (Sigma-Aldrich) for 20 min at room temperature. The glands were washed in PBS + 0.3% Triton X-100 and permeabilized for 30 min at 37°C in PBS + 1% Triton X-100. Blocking was performed for 30 min at room temperature in PBS + 0.3% Triton X-100 supplemented with 10% fetal calf serum and 1% BSA. The glands were incubated with primary antibodies diluted in blocking solution for 48 hr at 4°C, washed three times with PBS + 0.3% Triton X-100 for 30 min, and incubated with secondary antibodies in blocking solution overnight at 4°C. The stained glands were washed three times with PBS + 0.3% Triton X-100 for 30 min, stained with DAPI (0.1 μg/ml) for 30 min, and mounted in Prolong Gold anti-fade (Invitrogen). IF images were obtained on a Leica SP8 confocal microscope using a ×20/0.75 PLAPO lens and processed using Fiji/ImageJ software.

To quantify the putative colocalization of SUUR and Mod(Mdg4)-67.2 in polytene chromosomes (Figure 4A), the image resolution was reduced to 1388 by 1040. Pixel intensities (1,443,520) for SUUR and ModT channels were extracted from Bitmap files (ImageJ), normalized to Z-scores, and plotted as an X-Y scatter plot (Figure 4—figure supplement 1C). For colocalization analyses, the plot regions (ZModT > 1 and ZSUUR < 3, green) and (ZModT < 1 and ZSUUR > 3, red) were excluded from consideration (Figure 4—figure supplement 1D).

### Next-generation sequencing analyses (NGS)

Salivary glands from female wandering third-instar larvae were isolated and flash-frozen in liquid N2 until all samples were collected. Genomic DNA for sequencing was prepared from 25 L3 salivary gland pairs or 10 mg embryos (0–6 hr AED) using DNeasy Blood and Tissue kit (QIAGEN). Each sample was prepared in triplicate. The tissues were soaked in 180 µl buffer ATL + 20 µl proteinase K (15 mg/ml) and lysed for 2–3 hr at 55°C. The reactions were cooled to room temperature, supplemented with 4 µl RNase A, ~40 mg/ml (Sigma-Aldrich), and RNA was digested for 10 min. The genomic DNA was fragmented with 0.002 units DNase I (Thermo Fisher) in 100 µl reactions containing 10 mM Tris-HCl, pH 7.5, 10 mM MnCl2, 0.1 mM CaCl2, 0.1 mg/ml RNase A, and 0.2 mg/ml nuclease-free BSA (1× reaction buffer) for 15 min at 37°C. (DNAse I dilutions were prepared using 1× reaction buffer.) Reactions were stopped by adding 5 µl 0.5 M EDTA, and DNase I was inactivated for 20 min at 65°C. The fragmented DNA was purified on QiaQuick columns using PCR purification kit (QIAGEN) and eluted in 40 µl 10 mM Tris-HCl, pH 8.0. The size distribution of DNA fragments (200–600 bp, average ~400 bp) was confirmed and DNA concentration was measured on 2100 BioAnalyzer (Agilent). Libraries were prepared from 20 ng of fragmented genomic DNA with the ThruPLEX DNA-seq kit using SMARTer DNA Unique Dual Indexes (TakaraBio) and sequenced 150 bp paired-end reads on an NovaSeq 6000 (Novagene).

The sequencing quality of each sample was assessed using FASTQC version 0.11.7 (Andrews, 2010). Raw paired-end reads were trimmed of adapters using BBDuk from the BBTools software version 38.71 using the parameters: ktrim=r ref=adapters rcomp=t tpe=t tbo=t hdist=1 mink=11 (Bushnell, 2014). Reads were aligned to the BDGP Release 6 of the Drosophila melanogaster genome (dm6) (dos Santos et al., 2015) using Bowtie2 version 2.3.4.1 (Langmead and Salzberg, 2012) and parameters -q --local --very-sensitive-local --no-unal --no-mixed --no-discordant --phred33 -I 10 -X 700. Duplicate reads were marked using Picard 2.2.4 (BroadInstitute, 2020) and SAM files were converted to BAM format, filtered for quality (-bq 5), and removed of duplicates (-bF 0x400) using Samtools version 1.9 (Danecek et al., 2021). To examine replicate concordance, a principal component analysis (PCA) was performed using the deepTools package. Replicates clustered indicating high genome-wide similarity within genotypes (not shown). For visualization, replicates were merged (samtools merge) and coverage was calculated across 50 bp bins and normalized to counts per million (CPM) using deeptools version 3.2.0: bamCoverage -bs 50 –normalizeUsing CPM (Ramírez et al., 2016). Each genotype was scaled to the diploid Oregon R embryo signal in 5 kb bins: bigWigCompare –-operation first -bs 5000. DamID-chip data for SUUR and Su(Hw) were retrieved from GSE22069 (Filion et al., 2010). ChIP-chip data for Su(Hw) insulator elements were also used (Nègre et al., 2010). Underreplicated domains were called using a custom R script to identify regions at least 100 kb in length that fell below the average chromosomal read count as described (Andreyeva et al., 2017). Visualization of all data was performed on the UCSC Genome browser using the dm6 release of the Drosophila genome (Kent et al., 2002). Each data set was auto-scaled to its own min and maximum, and the data were windowed by mean with 16-pixel smoothing applied.

### Quantitative real-time PCR

Genomic DNA samples prior to DNase I fragmentation (see above) were diluted to ~0.25 ng/µl. Real-time PCR was performed using 0.5 ng genomic DNA on a ViiA7 thermocycler (Applied Biosystems) with a three-step protocol (95°C 15 s, 60°C 30 s, 68°C 60 s) and iTaq Universal SYBR Green Supermix (Bio-Rad). Primer sequences are provided in Figure 7—source data 1. Each reaction was performed in three technical replicates for each of the three biological samples (N = 9). For each amplicon, the average Ct value (<Ct>) was calculated and normalized to the average Ct value for a random intergenic genomic sequence as a loading control. Further, for each template, the ∆Ct was normalized to the average Ct value for embryonic DNA (diploid control). Standard deviation (σCt) for each reaction in triplicate was also calculated. The following ΔΔCt formula was used: <∆∆Ct> = (<Cttarget> – <Ctintergenic86D>)SG – (<Cttarget> – <Ctintergenic86D>)embryo. Standard deviations for <∆∆Ct> were calculated as σ∆∆Ct = square root of (σ2target + σ2intergenic86D)/2. ∆∆Ct’s were converted to DNA copy numbers as 2–<∆∆Ct>. The confidence interval was calculated in the range between 2–<∆∆Ct>–σ and 2–<∆∆Ct>+σ.

To examine the putative zygotic function(s) of SuUR, heterozygous SuURES parents were produced by balancing with TM6B, Tb, and crossed inter se. L3 salivary glands were dissected from homozygous SuUR mutant progeny, and DNA copy numbers were measured by qPCR as described above.
