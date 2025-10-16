# De novo synthesis of a sunscreen compound in vertebrates

## Authors

- Andrew R Osborn<sup>1</sup>
- Khaled H Almabruk<sup>1</sup>
- Garrett Holzwarth<sup>2</sup>
- Shumpei Asamizu<sup>1</sup>
- Jane LaDu<sup>4</sup>
- Kelsey M Kean<sup>5</sup>
- P Andrew Karplus<sup>5</sup>
- Robert L Tanguay<sup>4</sup>
- Alan T Bakalinsky<sup>2</sup>
- Taifo Mahmud<sup>1</sup> ([ORCID: 0000-0001-9639-526X](https://orcid.org/0000-0001-9639-526X)) †

### Affiliations

1. Department of Pharmaceutical Sciences Oregon State University Corvallis United States
2. Department of Food Science and Technology Oregon State University Corvallis United States
3. Department of Microbiology Oregon State University Corvallis United States
4. Department of Environmental and Molecular Toxicology Oregon State University Corvallis United States
5. Department of Biochemistry and Biophysics Oregon State University Corvallis United States

† Corresponding author

## Abstract

10.7554/eLife.05919.001 Ultraviolet-protective compounds, such as mycosporine-like amino acids (MAAs) and related gadusols produced by some bacteria, fungi, algae, and marine invertebrates, are critical for the survival of reef-building corals and other marine organisms exposed to high-solar irradiance. These compounds have also been found in marine fish, where their accumulation is thought to be of dietary or symbiont origin. In this study, we report the unexpected discovery that fish can synthesize gadusol de novo and that the analogous pathways are also present in amphibians, reptiles, and birds. Furthermore, we demonstrate that engineered yeast containing the fish genes can produce and secrete gadusol. The discovery of the gadusol pathway in vertebrates provides a platform for understanding its role in these animals, and the possibility of engineering yeast to efficiently produce a natural sunscreen and antioxidant presents an avenue for its large-scale production for possible use in pharmaceuticals and cosmetics. DOI: http://dx.doi.org/10.7554/eLife.05919.001

## Introduction

The sunscreen compounds, mycosporine-like amino acids (MAAs) and related gadusols, commonly found in bacteria, fungi, algae, and marine invertebrates (Shick and Dunlap, 2002; Miyamoto et al., 2014), have been proposed to fulfill a variety of functions, such as sunscreen, antioxidant, stress response, intracellular nitrogen reservoir, and/or optical filter (Gao and Garcia-Pichel, 2011; Bok et al., 2014). Although their formation had long been proposed to originate from the shikimate pathway, more recent bioinformatic and biochemical studies revealed that in cyanobacteria, MAAs are synthesized by desmethyl-4-deoxygadusol synthase (DDGS), a dehydroquinate synthase (DHQS) homolog (Wu et al., 2007; Balskus and Walsh, 2010; Singh et al., 2010; Asamizu et al., 2012). Interestingly, inactivation of the DDGS gene in Anabaena variabilis ATCC 29413 did not abolish the production of MAAs, suggesting that additional pathways exist for the biosynthesis of MAAs (Spence et al., 2012). DDGS converts sedoheptulose 7-phosphate (SH7P) to desmethyl-4-deoxygadusol via a unique sequence of dephosphorylation, aldol condensation, enolization, dehydration, reduction, and tautomerization reactions (Figure 1—figure supplement 1) (Balskus and Walsh, 2010; Asamizu et al., 2012). The product is subsequently converted by a methyltransferase to 4-deoxygadusol, the building block of MAAs.

4-Deoxygadusol has also been proposed to be the precursor of gadusol (Starcevic et al., 2010; Rosic and Dove, 2011), a related compound initially isolated from cod roe (Gadus morhua L.) (Plack et al., 1981), but also found in roes of other marine fish (Plack et al., 1981; Arbeloa et al., 2010), sea urchin eggs (Chioccara et al., 1986), cysts and nauplii of brine shrimp (Grant et al., 1985), mantis shrimp crystalline cones (Bok et al., 2014), and sponges (Bandaranayake et al., 1997). As genes responsible for the production of 4-deoxygadusol and MAAs are commonly found in bacteria (e.g., cyanobacteria), algae, and other marine microorganisms (Shick and Dunlap, 2002; Miyamoto et al., 2014), the accumulation of these compounds in marine animals has been proposed to be of dietary or symbiont origin (Arbeloa et al., 2010; Gao and Garcia-Pichel, 2011; Loew, 2014). On the other hand, a gene cluster like that in cyanobacteria apparently encoding a four-step DDGS-based pathway for converting SH7P to MAAs was discovered in the genomes of a coral (Acropora digitifera) and sea anemone (Nematostella vectensis), suggesting that these invertebrates can produce MAAs autonomously (Rosic and Dove, 2011; Shinzato et al., 2011).

DDGS is a member of the sugar phosphate cyclase (SPC) superfamily (Wu et al., 2007). In addition to DHQS, this superfamily includes four enzymes known for their roles in the biosynthesis of natural products with therapeutic application: 2-epi-5-epi-valiolone synthase (EEVS), 2-epi-valiolone synthase, aminoDHQS, and 2-deoxy-scyllo-inosose synthase (DOIS) (Wu et al., 2007; Mahmud, 2009; Asamizu et al., 2012; Kang et al., 2012). EEVS catalyzes the entry step to the biosynthesis of pseudosugar-containing natural products, such as the antidiabetic drug acarbose and the crop protectant validamycin A, and has so far only been identified and characterized in bacteria (Mahmud, 2009).

Recently, we surprisingly also found genes that encode EEVS-like proteins (annotated as ‘PREDICTED: pentafunctional AROM polypeptide-like’) in the genomes of fish, amphibians, reptiles, and birds (

![Figure 1.](https://cdn.elifesciences.org/articles/05919/elife-05919-fig1-v1.jpg)

**Figure 1.:** (A) Bayesian phylogenetic tree of SPCs. Numbers represent posterior probability. The stramenopile Aureococcus anophagefferens, denoted by the blue star, has EEVS and MT-Ox proteins strikingly similar (over 50% identical) to those in vertebrates. The micro algae Coccomyxa subellipsoidea, denoted by the red star, also has EEVS and MT-Ox. (B) Genetic organizations of EEVS and MT-Ox genes in fish, amphibians, birds, and reptiles. Humans and other mammals lack these genes (indicated in dashed red box). For a complete list of vertebrates whose genomes are known to contain EEVS and MT-Ox genes, see Table 1. FRMD4B, FERM domain-containing protein 4B; MitF, microphtalmia-associated transcription factor; MDFIC, MyoD-family inhibitor domain-containing protein-like; and FoxP1, Forkhead-related transcription factor 1. (C) Biochemical characterization of recombinant LOC100003999 and zgc:113054 proteins. (D) WebLogo (Crooks et al., 2004) images of residue conservation patterns at the three metal ligand positions and two active site fingerprint sites known (Kean et al., 2014) to distinguish bacterial EEVSs from DDGSs. The residue numbers given correspond to the reference proteins D. rerio EEVS, ValA, and A. variabilis DDGS, respectively. WebLogos were based on 126 vertebrate, 63 bacterial EEVS, and 160 bacterial DDGS sequences, respectively, that had BLASTP E-values <10−120 in searches using the reference proteins noted above as queries. Each group was aligned using ProMals (Pei and Grishin, 2007).DOI: http://dx.doi.org/10.7554/eLife.05919.00310.7554/eLife.05919.004Figure 1—source data 1.DOI: http://dx.doi.org/10.7554/eLife.05919.004

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/05919/elife-05919-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** Anabaena variabilis (Balskus and Walsh, 2010).DOI: http://dx.doi.org/10.7554/eLife.05919.005

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/05919/elife-05919-fig1-figsupp2-v1.jpg)

**Figure 1—figure supplement 2.:** Numbers represent bootstrap confidence values. Blue star denotes the stramenopile A. anophagefferens, and red star denotes the micro algae C. subellipsoidea.DOI: http://dx.doi.org/10.7554/eLife.05919.006

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/05919/elife-05919-fig1-figsupp3-v1.jpg)

**Figure 1—figure supplement 3.:** (A) SDS PAGE of purified recombinant ValA, LOC100003999, and zgc:113054, and E. coli cell free extracts containing the enzymes. (B) TLC analysis of enzymatic products of purified ValA and purified LOC100003999. (C) TLC analysis of EEV and the zgc:113054 product (gadusol) using FeCl3 solution as a spraying agent. Only gadusol, but not EEV, can be detected as a maroon spot.DOI: http://dx.doi.org/10.7554/eLife.05919.007

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/05919/elife-05919-fig1-figsupp4-v1.jpg)

**Figure 1—figure supplement 4.:** (A) SH7P with E. coli cell free extracts containing LOC100003999. (B) SH7P with purified ValA. (C) Authentic EEV. Samples were converted to their trimethylsilyl derivatives using Tri-Sil HTP (Thermo Scientific).DOI: http://dx.doi.org/10.7554/eLife.05919.008

![Figure 1—figure supplement 5.](https://cdn.elifesciences.org/articles/05919/elife-05919-fig1-figsupp5-v1.jpg)

**Figure 1—figure supplement 5.:** Alignment of the sequence of the only structurally known EEVS–ValA from Streptomyces hygroscopicus (ShEEVS; PDB entry 4P53) with representative related enzymes. The family consensus secondary structure elements shown schematically shown above the sequences and within each sequence the residues involved in secondary structures are color coded: β-strands (yellow), α-helices (teal), 310 helices (blue), and π helices (orange). ValA is shown first, and other sequences in order are DrEEVS (Danio rerio EEVS), CsEEVS (C. subellipsoidea EEVS), AaEEVS (A. anophagefferens EEVS), AvDDGS (A. variabilis DDGS; Ava_3858), AmEVS (Actinosynnema mirum EVS; Amir_2000), PDB entry 1DQS (Aspergillus nidulans DHQS), and PDB entry 2D2X (Bacillus circulans DOIS). The 14 ‘fingerprint’ active site positions identified by Kean et al. (Kean et al., 2014) are indicated by an asterisk (*) below the sequences. Above the sequences are indicated a subset of those residues that ligate the catalytic metal (m) and another subset with notable variation between the family members that have different types of activity (↓). The DrEEVS sequence and those of all known vertebrate homologs (not shown) match ShEEVS at all fourteen active site positions. The putative algal EEVS enzymes, AaEEVS and CsEEVS, sequences match the EEVS residues at the positions thought to be important for distinguishing the EEVS activity, but respectively differ at one and two positions; these positions are the ones that are of unknown importance for EEVS activity.DOI: http://dx.doi.org/10.7554/eLife.05919.009

![Figure 1—figure supplement 6.](https://cdn.elifesciences.org/articles/05919/elife-05919-fig1-figsupp6-v1.jpg)

**Figure 1—figure supplement 6.:** Shown are the 13 active-site residues conserved in all EEVS enzymes (pale purple carbons), the NAD+ (gray carbons), and the Zn2+ atom (silver sphere with black coordination bonds), along with a mesh that delineates the pocket suitable for binding an SH7P substrate. Residue numbers in LOC100003999 identifying twelve of the active site residues are shown; the third metal ligand, H366, is behind the zinc and is not labeled. For the two positions that differ between EEVS and DDGS, the residue type present in DDGS is shown in green in parentheses. Figure made with Pymol (Schrödinger L. The PyMOL Molecular Graphics System, Version 1.3.) using the coordinates of ValA, an EEVS from S. hygroscopicus subsp. jinggangensis 5008 (Kean et al., 2014).DOI: http://dx.doi.org/10.7554/eLife.05919.010

## Results and discussion

To investigate the function of the vertebrate EEVS-like genes, the protein encoded by the zebrafish EEVS-like gene (LOC100003999) was expressed in Escherichia coli. Incubation of the recombinant protein with SH7P gave a product, which was confirmed by thin-layer chromatography (TLC) and GC-MS to be EEV (Figure 1C, Figure 1—figure supplements 3, 4), identifying the protein as an EEVS. The best-characterized bacterial EEVS is ValA from the validamycin pathway in Streptomyces hygroscopicus subsp. jinggangensis 5008 (Bai et al., 2006), and the crystal structure of ValA (Protein Data Bank [PDB] entry 4P53) (Kean et al., 2014), allowed identification of a fingerprint set of 14 active-site residues with characteristic variations that could differentiate the various SH7P cyclases. Further supporting the assignment of the LOC100003999-encoded protein as an EEVS, sequence comparisons show that all animal EEVS-like proteins are highly similar (60–72% identity) and also match the sequence of ValA at all 14 fingerprint sites (Figure 1D, Figure 1—figure supplements 5, 6). This firmly establishes the presence of EEVS activity in animals.

The second gene, MT-Ox (zgc:113054), is predicted to encode a protein that contains two domains: the

![Figure 2.](https://cdn.elifesciences.org/articles/05919/elife-05919-fig2-v1.jpg)

**Figure 2.:** (A–B) HPLC traces and UV absorptions of gadusol produced from Escherichia coli cell-free extract containing EEVS and purified MT-Ox protein at pH 7.0 and 2.5. (C–D) Transcription patterns of EEVS and MT-Ox genes during zebrafish embryonic development. qRT-PCR analysis of mRNA isolated from zebrafish embryos (n = 3) at 12, 24, 48, 72, 96, and 120 hpf. (E) Time course of gadusol production in yeast harboring the zebrafish genes. The yeast was cultured in YNB + 2% glucose supplemented with leucine and lysine at 30°C for 2 days, and growth was monitored as A600 values (control, dotted blue line; gadusol producer, solid red line). Gadusol concentration in the supernatant of 20 ml cultures (n = 3) was monitored as A296 values in 50 mM phosphate buffer, pH 7.0 (dashed green line) corrected for non-gadusol background absorbance in the control supernatant, normalized to A600 value. Gadusol was quantified based on an extinction coefficient of 21,800 M−1 cm−1 in 50 mM phosphate buffer, pH 7. (F–H) Comparative HPLC analysis of gadusol from recombinant enzymatic reaction, zebrafish extract, and yeast extract. (I) Gadusol suppresses the UVB sensitivity of a rad1∆ yeast mutant; and (J) Gadusol increases the UVB tolerance of a wild-type (RAD1) strain. Cells suspended in control supernatant (CS) or gadusol+ supernatant (G+S) were irradiated with UVB and subsequently spotted in 3 µl aliquots (n = 4) onto YEPD plates, which were incubated at 30°C for 24 hr.DOI: http://dx.doi.org/10.7554/eLife.05919.012

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/05919/elife-05919-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** (A) SH7P incubated with E. coli cell free extracts containing LOC100003999 (zebrafish EEVS) and boiled zgc:113054 (MT-Ox). (B) SH7P incubated with E. coli cell free extracts containing EEVS and purified MT-Ox. (C) SH7P incubated with purified ValA (a bacterial EEVS) and boiled MT-Ox. (D) Synthetic EEV incubated with purified MT-Ox. (E) Deuterated EEV incubated with purified MT-Ox. (F) MS/MS spectrum of gadusol obtained from the EEVS and MT-Ox reaction. (G) Proposed ion species of gadusol observed in F.DOI: http://dx.doi.org/10.7554/eLife.05919.013

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/05919/elife-05919-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** 1H NMR spectrum of gadusol obtained from E. coli cell free extracts containing LOC100003999 and zgc:113054 reactions.DOI: http://dx.doi.org/10.7554/eLife.05919.014

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/05919/elife-05919-fig2-figsupp3-v1.jpg)

**Figure 2—figure supplement 3.:** The dotted arrows show the three steps thought to be a part of the MT-Ox catalyzed reaction.DOI: http://dx.doi.org/10.7554/eLife.05919.015

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/05919/elife-05919-fig2-figsupp4-v1.jpg)

**Figure 2—figure supplement 4.:** Asamizu et al., 2012) and the shunt pathway to gadusol.DOI: http://dx.doi.org/10.7554/eLife.05919.016

In zebrafish, both of the LOC100003999 and zgc:113054 genes are expressed during embryonic development. qRT-PCR analysis of mRNA isolated from zebrafish embryos at 12, 24, 48, 72, 96, and 120 hpf showed maximal expression at 72 hpf (Figure 2C–D). To demonstrate de novo synthesis of gadusol in zebrafish, the embryos were collected at 72 hpf, lyophilized and extracted with methanol, and the extract was analyzed by HPLC and ESI-MS (Figure 2G). Our finding of gadusol in the extract unambiguously confirms the ability of zebrafish to synthesize gadusol and amends the current perception that gadusol found in fish and other vertebrates is necessarily of dietary or symbiont origin. However, as MAAs are synthesized via a different pathway and there is no evidence that fish have those biosynthetic enzymes, the accumulation of MAAs in fish would still appear to be of dietary origin (Mason et al., 1998; Zamzow, 2004).

To show that the recombinant LOC100003999 and zgc:113054 genes are sufficient for encoding gadusol synthesis, they were cloned into a yeast expression vector and transferred into a Saccharomyces cerevisiae strain, in which the transaldolase gene TAL1 had been deleted. Yeast possesses a robust pentose–phosphate pathway (Figure 2—figure supplement 4), and by removing the transaldolase enzyme, which normally metabolizes SH7P, and adding EEVS and MT-Ox, we expected to facilitate an effective shunt pathway from SH7P to gadusol. Analysis of the culture broth by HPLC, ESI-MS, and UV spectrophotometry revealed the presence of gadusol (Figure 2H) and its accumulation to ∼20 mg/l after 5 days (Figure 2E). The results not only demonstrate the ability of the engineered yeast to produce and secrete gadusol but also present a new avenue for large-scale production of the compound for possible commercial uses, for example, sunscreen and/or antioxidant (Plack et al., 1981; Schmid et al., 2006; Cardozo et al., 2007; Arbeloa et al., 2010).

To test the UV-protective activity of gadusol, a yeast rad1∆ mutant, which is sensitive to UVB, was suspended at approximately 107 cells/mL in the concentrated supernatant from the gadusol-producing yeast strain or from an otherwise isogenic control strain that did not produce gadusol. The gadusol-containing supernatant suppressed the UVB-sensitivity of the rad1∆ mutant (Figure 2I), confirming the UVB-protective activity of gadusol. Analogous experiments with a wild-type strain (RAD1) at higher doses of UVB showed comparable results (Figure 2J), consistent with UVB protective activity.

As noted above, the SPCs EEVS, EVS, DDGS, aminoDHQS, and DOIS are all related to DHQS and are widespread in bacteria and fungi, but other than this report, are not known to exist in vertebrates or prevertebrates. We suggest that the vertebrate EEVS and MT-Ox genes were most plausibly acquired via horizontal gene transfer. Interestingly, searches identify the stramenopile Aureococcus anophagefferens and the microalgae Coccomyxa subellipsoidea, as the only non-vertebrate organisms in current databases that harbor a similar bifunctional MT-Ox gene, and both organisms have a predicted EEVS gene adjacent to that of MT-Ox. As algae are known to be active horizontal gene transfer agents (Ni et al., 2012), algae such as these become a plausible place both for the development of this alternate pathway for gadusol production and as a source of the genes found in vertebrates. Further supporting such a relationship, the A. anophagefferens EEVS protein is substantially more similar to the vertebrate EEVSs than it is to bacterial EEVSs (Figure 1A and Figure 1—figure supplement 2, denoted by the blue star).

Further bioinformatics studies also showed that the tunicates and lancelets lack the EEVS and MT-Ox genes, suggesting that the gene transfer occurred sometime during the evolution of primitive chordates to bony fishes (

![Figure 3.](https://cdn.elifesciences.org/articles/05919/elife-05919-fig3-v1.jpg)

**Figure 3.:** The genes entered an early vertebrate genome as a linked pair (vertical blue arrow) and were retained in the modern ray-finned fish, amphibians, reptiles, and birds as indicated by thick dark cyan arrows. Coelacanths and mammals lost the genes (thick red arrows). No full genome sequence is available for assessing the presence of EEVS and MT-Ox in lungfish. The phylogenetic trees of the EEVS and MT-Ox proteins or mRNA from a selected set of vertebrates can be found in Figure 3—figure supplements 1–3 and Supplementary files 1, 2.DOI: http://dx.doi.org/10.7554/eLife.05919.017

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/05919/elife-05919-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** The distantly related E. coli protein CglD was used as an out-group. Numbers represent bootstrap confidence values.DOI: http://dx.doi.org/10.7554/eLife.05919.018

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/05919/elife-05919-fig3-figsupp2-v1.jpg)

**Figure 3—figure supplement 2.:** E. coli K12 dam was used as an out-group. Numbers represent bootstrap confidence values.DOI: http://dx.doi.org/10.7554/eLife.05919.019

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/05919/elife-05919-fig3-figsupp3-v1.jpg)

**Figure 3—figure supplement 3.:** E. coli cglD was used as an out-group. Numbers represent bootstrap confidence values.DOI: http://dx.doi.org/10.7554/eLife.05919.020

## Materials and methods

## Molecular phylogenetic analysis

For phylogenetic analysis, full-length amino acid sequences and vertebrate mRNA sequences were analyzed. A reciprocal BLAST hit analysis was performed with the EEVS protein (see Supplementary file 3). Sequences were aligned using MUSCLE. ProtTest was used to determine the best model of protein evolution (LG+G) (Darriba et al., 2011), and MEGA6 was used to determine the best fit nucleic acid evolutionary model (K80+G) (Tamura et al., 2013). RAxML was used for maximum likelihood analysis, and the robustness of the trees was assessed by bootstrap analysis (1000 replicates) (Stamatakis, 2014). Bayesian analysis was performed by MrBayes (version 3.2.3), using a random starting tree, running eight chains for 4,000,000 generations, sampling every 250 trees (Ronquist et al., 2012). The first 5000 trees were discarded as the burnin, with the remaining trees used to calculate posterior probability. RAxML and MrBayes were run on the CIPRES science gateway (Miller et al., 2010). MEGA6 was used for maximum likelihood analysis of vertebrate mRNA sequences with tree robustness assessed by bootstrap (500 replicates). Sources of proteins for the analyses are listed in Supplementary file 1.

## Construction of LOC100003999 and zgc:113054 gene expression vectors

The LOC100003999 gene was codon optimized for E. coli and synthesized commercially (GeneScript USA Inc., Piscataway, NJ). The product was cloned into EcoRV site of pUC57-kan vector. The plasmid was digested with BglII and EcoRI and ligated into BamHI and EcoRI site of pRSET-B (Life Technologies, Carlsbad, CA) for the expression of N-terminal hexa-histidine-tagged protein. The zgc:113054 gene was also codon optimized for E. coli and commercially synthesized (GeneScript USA Inc.). The product was cloned into EcoRV site of pUC57-amp vector. The plasmid was digested with BglII and EcoRI and ligated into BamHI and EcoRI site of pRSET-B (Life Technologies) for the expression of N-terminal hexa-histidine-tagged protein.

## Expression of valA, LOC100003999, and zgc:113054 genes in E. coli

pRSETB-valA, pRSETB-LOC100003999, and pRSETB-zgc:113054 plasmids were individually used to transform E. coli BL21 GOLD (DE3) pLysS. Transformants were grown overnight at 37°C on LB agar plate containing ampicillin (100 μg/ml) and chloramphenicol (25 μg/ml). A single colony was inoculated into LB medium (2 ml) containing the above antibiotics and cultured at 37°C for 8 hr. The seed culture (1 ml) was transferred into LB medium (100 ml) in a 500-ml flask and grown at 30°C until OD600 reached 0.6. Then, the temperature was reduced to 18°C. After 1-hr adaptation, isopropyl-D-1-thiogalactopyranoside (IPTG) (0.1 mM) was added to induce the N-terminal hexa-histidine-tagged proteins. After further growth for 16 hr, the cells were harvested by centrifugation (5000 rpm, 10 min, 4°C), washed twice with cold water, and stored at −80°C until used.

## Purification of recombinant ValA, LOC100003999, and zgc:113054

Cell pellets from a 400-ml culture of E. coli BL21 GOLD (DE3) pLysS containing pRSETB-valA, pRSETB-LOC100003999, or pRSETB-zgc:113054 plasmids were resuspended in 20 ml of B buffer (40 mM Tris-HCl, 300 mM NaCl, 10 mM imidazole, pH 7.5). Cells were disrupted by sonication for 1 min (4 times, 2 min interval) at 13 watts on ice (Probe sonicator, Misonix, Farmingdale, NY). 20 ml of lysate was divided into 2-ml tubes and centrifuged (14,500 rpm, 20 min, 4°C). Soluble fractions were collected and transferred into a 50-ml tube. Ni-NTA (QIAGEN, Valencia, CA) resin (5 ml) was applied into 10-ml vol empty column, and the Ni-NTA resin was equilibrated with B buffer (50 ml, 10 CV). About 20 ml of supernatant from cell lysate was applied to the column (flow rate; 0.8 ml/min). The column was then washed with 100 ml (20 CV) of W buffer (40 mM Tris-HCl, 300 mM NaCl, 20 mM imidazole, pH 7.5) at 0.8 ml/min. The hexa-histidine-tagged proteins were eluted by imidazole addition using a gradient mixer containing 100 ml of W buffer and 100 ml of E buffer (40 mM Tris-HCl, 300 mM NaCl, 300 mM imidazole, pH 7.5). The fractions (150 drops or about 5 ml) were collected and checked by SDS-PAGE (Coomassie Blue staining). Fractions containing pure proteins were combined (25 ml) and dialyzed against 2 l of D buffer (10 mM Tris-HCl, pH 7.5) 3 times (every 3 hr). Dialyzed protein solution was concentrated by ultrafiltration (MWCO 10 K) to 200 μM and flash frozen in liquid N2 prior to storage at −80°C. The yields of the purified proteins were 57 mg/l for ValA, 18 mg/l for LOC100003999, and 79 mg/l for zgc:113054.

## LOC100003999 assay conditions

Each reaction mixture (25 μl) contained Tris-HCl buffer (20 mM, pH 7.5), NAD+ (1 mM), CoCl2, or ZnSO4 (0.1 mM), SH7P (4 mM), and purified enzymes (0.12 mM). The mixture was incubated at 30°C for 2 hr. ValA (instead of LOC100003999) was used as a positive control. No enzyme (buffer only) was used as a negative control.

## Coupled LOC100003999 and zgc:113054 assay conditions

Each reaction mixture (50 μl) contained potassium phosphate buffer (10 mM, pH 7.4), NAD+ (2 mM), CoCl2 (0.2 mM), SH7P (4 mM), and LOC100003999 cell-free extract (20 μl) was incubated at 30°C. After 6 hr, S-adenosylmethionine (5 mM) and purified zgc:113054 (0.1 mM) were added. The mixture was incubated at 30°C for another 6 hr. ValA was used (instead of LOC100003999) as a positive control. Extract of E. coli harboring pRSET B empty vector was used as a negative control.

## Zgc:113054 assay using [6,6-2H2]-EEV as substrate

A reaction mixture (25 μl) containing potassium phosphate buffer (10 mM, pH 7.4), NAD+ (2 mM), CoCl2 (0.2 mM), S-adenosylmethionine (5 mM), [6,6-2H2]-EEV (4 mM), and purified zgc:113054 (0.1 mM) was incubated at 30°C for 2 hr. Boiled zgc:113054 was used as a negative control.

## TLC analysis of EEV and gadusol

Analytical TLC was performed using silica gel plates (60 Å) with a fluorescent indicator (254 nm), which were visualized with a UV lamp and ceric ammonium molybdate (CAM) or 5% FeCl3 in MeOH-H2O (1:1) solutions.

## GC-MS analysis of EEV

The enzymatic reaction mixtures were lyophilized, and the products were extracted with MeOH. The MeOH extract was then dried and Tri-Sil HTP (Thermo Scientific, Waltham, MA) (100 μl) was added and left to stand for 20 min. The solvent was removed in a flow of argon gas, and the silylated products were extracted with hexanes (100 μl) and injected into the GC-MS (Hewlett Packard 5890 SERIES II Gas chromatograph).

## Enzymatic synthesis, purification, and analysis of gadusol

Fifty eppendorf tubes containing reaction mixtures (100 μl each), which consist of potassium phosphate buffer (10 mM, pH 7.4), SH7P (5 mM), NAD+ (2 mM), CoCl2 (0.2 mM), and LOC100003999 cell-free extract (40 μl), were incubated at 30°C. After 6 hr, S-adenosylmethionine (5.5 mM) and zgc:113054 cell-free extracts (30 μl) were added. The reaction mixtures were incubated at 30°C for another 6 hr. The reaction mixtures were quenched with 2 vol of MeOH, left to stand at −20°C for 20 min, then centrifuged at 14,500 rpm for 20 min. The supernatants were pooled and dried under vacuum. The residual water was frozen and lyophilized. The crude sample was dissolved in water (1 ml) and subjected to Sephadex LH-20 column chromatography using phosphate buffer (2.5 mM, pH 7) as an eluant. Fractions containing the product as judged by MS were combined and lyophilized. Furthermore, the product was purified by HPLC (Shimadzu LC-20AD, C18 column [YMC], 250 × 10 mm, 4 μm, flow rate 1 ml/min). Solvent system: MeOH—phosphate buffer (5 mM, pH 7), gradient 1–100% of MeOH (0–40 min). Peak at 12.74 min was collected and dried to give gadusol (0.4 mg). 1H NMR (700 MHz, D2O, cryo-probe): δ 4.10 (s, 1H, H-4), 3.71 (d, J = 12 Hz, H-7α), 3.56 (d, J = 12 Hz, H-7β), 3.49 (s, 3H, OCH3), 2.68 (d, J = 17 Hz, H-6α), 2.38 (d, J = 17 Hz, H-6β). HR-MS (ESI-TOF) (m/z): (M+H)+ calculated for C8H13O6, 205.0707; found, 205.0709.

## Zebrafish lines and embryos

Adult wild-type 5D zebrafish were housed at the Sinnhuber Aquatic Research Laboratory on a recirculating system maintained at 28 ± 1°C with a 14 hr light per 10 hr dark schedule. Embryos were collected from group spawns of adult zebrafish as described previously (Reimers et al., 2006), and all experiments were conducted with fertilized embryos according to Oregon State University Institutional Animal Care and Use Protocols. Embryos were staged accordingly as previously described (Kimmel et al., 1995) and collected by hand for all experiments. Embryos were reared in media consisting of 15 mM NaCl, 0.5 mM KCl, 1 mM MgSO4, 0.15 mM KH2PO4, 0.05 mM Na2HPO4, and 0.7 mM NaHCO3 (Westerfield, 2000).

## Polymerase chain reaction

All polymerase chain reaction (PCR) reactions were performed according to manufacturer's specifications. Cycling conditions: 96°C for 3 min, 95°C for 1 min, 65°C for 1 min, and 72°C for 1 min per kB DNA; 35 cycles were used followed by 10 min at 72°C. All PCR products were characterized on an agarose gel. If needed, the PCR product was excised from the gel and purified using the E.Z.N.A. Gel Extraction Kit (Omega Bio-tek, Norcross, GA).

## Quantitative PCR of zebrafish samples

qPCR was performed on a Applied Biosystems StepOnePlus machine. The super mix PerfeCTa SYBR Green FastMix, ROX (Quanta biosciences, Gaithersburg, MD) was used. cDNA (100 ng) from time points at 6, 12, 24, 48, 72, 96, and 120 hpf was used. Super mix (18 µl) was added to bring the final volume to 20 µl. PCR conditions suggested by the supplier were used. For total RNA isolation, 30 embryos were homogenized in RNAzol (Molecular Research Center, Cincinnati, OH); RNA was purified according to the manufacturer's protocol. RNA was quantified by A260/280 ratios measured using a SynergyMx microplate reader (Biotek, Winooski, VT) and analyzed with the Gen5 Take3 module. 1 µg of RNA was used for cDNA synthesis. Superscript III First-Strand Synthesis (Life Technologies) and oligo d(T) primers were used to synthesize cDNA from the total RNA.

## Isolation of gadusol from zebrafish

Embryos were collected and euthanized at 72 hpf by induced hypoxia through rapid chilling on ice for 30 min. Embryo media were removed until about 5 ml were left and frozen at −80°C. Embryos were lyophilized overnight. The freeze-dried embryos were then ground with a pestle and mortar under liquid nitrogen. The powder was collected and placed in a pre-weighed glass vial. The mortar was washed with MeOH-H2O (80:20), and the solvent was added to the powder. The solvent was evaporated, and powder was weighed. The embryo powder was extracted twice with MeOH-H2O (80:20). The two extracts were combined, dried, and weighed. The extract was suspended in MeOH-H2O (80:20) (1 ml) and extracted twice with hexanes. The aqueous layer was recovered, dried, and weighed. The extract was suspended in MeOH for analysis by mass spectrometry. The extract was dissolved in phosphate buffer pH 7.0 for identification by HPLC (Shimadzu SPD-20A system, YMC ODS-A column (4.6 id × 250 mm), MeOH—5 mM phosphate buffer (1% MeOH for 20 min followed by a gradient from 1 to 95% MeOH in 20 min), flow rate 0.3 ml/min, 296 nm. The isolated gadusol was analyzed by MS (ThermoFinnigan LCQ Advantage system) and NMR (in D2O; Bruker Unity 300 [300.15 MHz] spectrometer).

## Construction of yeast mutants

The yeast strains used are listed in Supplementary file 4. The TRP1 gene was replaced in BY4742 tal1∆::KanMX4 with a wild-type URA3 allele from S288c by standard methods (Baudin et al., 1993). The deletion was confirmed by PCR using primer pairs TRP1DisUP/TRP1DisLO and URA3DisUP/TRP1DisLO. The BY4742 tal1∆::KanMX4 trp1∆::URA3 strain was then co-transformed (Gietz et al., 1992) with pXP416 and pXP420 to generate an empty vector control strain and with pXP420-EEVS and pXP416-MT-Ox to generate a gadusol-producing strain. The RAD1 gene was replaced in BY4742 tal1∆::KanMX4 trp1∆::URA3 with a wild-type LEU2 allele from S288c by standard methods (Reynolds et al., 1987). The deletion was confirmed by PCR using primer pairs RAD1UP/RAD1LO. The resultant BY4742 tal1∆::KanMX4 trp1∆::URA3 rad1Δ::LEU2 strain was then co-transformed with pXP416 and pXP420.

## Media and yeast growth conditions

Cells were pre-grown in YEPD (1% yeast extract, 2% peptone, and 2% glucose) for transformations, and in YNB (Bacto yeast nitrogen base without amino acids) + 2% glucose supplemented with 30 µg/ml leucine and 30 µg/ml lysine to select for transformants and to produce gadusol. Liquid media were sterilized by filtration using a 0.45-µm filter, and agar-based media were sterilized by autoclaving. Liquid cultures were grown at 30°C for 48 hr and 200 rpm; plates were incubated at 30°C.

## Yeast overexpression plasmid construction

Plasmids are listed in Supplementary file 5. Primers used for PCR are listed in Supplementary file 6. PCR amplicons with SpeI and XhoI terminal restriction sites were generated for the EEVS gene and MT-Ox gene using pRSETB-EEVS and pRSETB-MTOx as templates, respectively. The EEVS and MT-Ox amplicons were then digested with SpeI and XhoI and ligated into SpeI-digested pXP420 and XhoI-digested pXP420 and pXP416, respectively, and introduced into competent E. coli (Top 10; Life Technologies) by transformation. E. coli transformants were selected on LB plates supplemented with ampicillin (100 µg/ml). Transformants were then screened by digesting plasmid DNA with SpeI and XhoI restriction enzymes and analyzing fragments by agarose gel electrophoresis.

## Identification of gadusol production in S. cerevisiae

S. cerevisiae cell pellets from 5 ml cultures were extracted with MeOH, and the supernatant was extracted with nBuOH. Extracts were concentrated and analyzed by HPLC (Shimadzu SPD-20A system, YMC ODS-A column [4.6 id × 250 mm], MeOH—5 mM phosphate buffer (1% MeOH for 20 min followed by a gradient from 1 to 95% MeOH in 20 min), flow rate 0.3 ml/min, 296 nm.

## Irradiation protocol

A rad1∆ mutant (MATα his3∆1 leu2∆0 lys2∆0 trp1∆::URA3 ura3∆0 rad1∆::LEU2 tal1∆::KanMX4/pXP416, pXP420) or wild-type RAD1 strain (S288c, MATα SUC2 gal2 mal2 mel flo1 flo8-1 hap1 ho bio1 bio6) was grown at 30°C and 200 rpm in YNB + 2% glucose + 30 µg/ml leu + 30 µg/ml lys. Cells were harvested after 24 hr by centrifugation, washed twice in the ninefold concentrated supernatant of either the gadusol-producing strain BY4742 tal1∆ trp1∆/pXP416-MTOx, pXP420-EEVS or of the control strain BY4742 tal1∆ trp1∆/pXP416, pXP420, and suspended in the respective concentrated supernatants at 107 cells/ml. Cells (375 µl) were irradiated with UVB (302 nm) at the indicated doses in wells of a 24-well microtiter plate shaken at 900 rpm. 3 µl aliquots of cells were then spotted onto a YEPD plate, which was incubated 24 hr at 30°C prior to being photographed. The supernatants of the gadusol producing and control strains were obtained by centrifugation following 5 day of growth in YNB + 2% glucose + 30 µg/ml leucine + 30 µg/ml lysine at 30°C and 200 rpm. Supernatants were freeze-dried, dissolved in a volume of distilled water 1/10 of the initial culture volume, and stored at 4°C until use. Just prior to suspension of cells, the concentrated supernatant was adjusted to 50 mM phosphate, pH 7.0 resulting in a final ninefold concentrate.
