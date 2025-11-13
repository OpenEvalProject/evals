# Structural, mechanistic, and physiological insights into phospholipase A-mediated membrane phospholipid degradation in Pseudomonas aeruginosa

## Authors

- Florian Bleffert<sup>1</sup>
- Joachim Granzin<sup>2</sup>
- Muttalip Caliskan<sup>1</sup>
- Stephan N Schott-Verdugo<sup>3</sup>
- Meike Siebers<sup>6</sup>
- Björn Thiele<sup>8</sup>
- Laurence Rahme<sup>9</sup> ([ORCID: 0000-0002-5374-4332](https://orcid.org/0000-0002-5374-4332))
- Sebastian Felgner<sup>10</sup> ([ORCID: 0000-0003-0030-2490](https://orcid.org/0000-0003-0030-2490))
- Peter Dörmann<sup>6</sup> ([ORCID: 0000-0002-5845-9370](https://orcid.org/0000-0002-5845-9370))
- Holger Gohlke<sup>2</sup> ([ORCID: 0000-0001-8613-1447](https://orcid.org/0000-0001-8613-1447)) †
- Renu Batra-Safferling<sup>2</sup> ([ORCID: 0000-0002-8597-4335](https://orcid.org/0000-0002-8597-4335)) †
- Karl-Erich Jaeger<sup>1</sup>
- Filip Kovacic<sup>1</sup> ([ORCID: 0000-0002-0313-427X](https://orcid.org/0000-0002-0313-427X)) †

### Affiliations

1. Institute of Molecular Enzyme Technology, Heinrich Heine University Düsseldorf, Forschungszentrum Jülich GmbH Jülich Germany ([ROR:02nv7yv05](https://ror.org/02nv7yv05))
2. Institute of Biological Information Processing - Structural Biochemistry (IBI-7: Structural Biochemistry), Forschungszentrum Jülich GmbH Jülich Germany ([ROR:02nv7yv05](https://ror.org/02nv7yv05))
3. Institute for Pharmaceutical and Medicinal Chemistry, Heinrich Heine University Düsseldorf Duesseldorf Germany ([ROR:024z2rq82](https://ror.org/024z2rq82))
4. Centro de Bioinformática y Simulación Molecular (CBSM), Faculty of Engineering, University of Talca Talca Chile ([ROR:01s4gpq44](https://ror.org/01s4gpq44))
5. John von Neumann Institute for Computing (NIC), Jülich Supercomputing Centre (JSC), and Institute of Bio- and Geosciences (IBG-4: Bioinformatics), Forschungszentrum Jülich GmbH Jülich Germany ([ROR:02nv7yv05](https://ror.org/02nv7yv05))
6. Institute of Molecular Physiology, and Biotechnology of Plants (IMBIO), University of Bonn Bonn Germany ([ROR:041nas322](https://ror.org/041nas322))
7. Institute for Plant Genetics, Heinrich Heine University Düsseldorf Düsseldorf Germany ([ROR:024z2rq82](https://ror.org/024z2rq82))
8. Institute of Bio- and Geosciences, Plant Sciences (IBG-2), and Agrosphere (IBG-3), Forschungszentrum Jülich GmbH Jülich Germany ([ROR:02nv7yv05](https://ror.org/02nv7yv05))
9. Department of Microbiology, and Immunobiology, Harvard Medical School Boston United States ([ROR:03vek6s52](https://ror.org/03vek6s52))
10. Department of Molecular Bacteriology, Helmholtz Centre for Infection Research Braunschweig Germany ([ROR:03d0p2685](https://ror.org/03d0p2685))
11. Institute of Bio- and Geosciences (IBG-1: Biotechnology), Forschungszentrum Jülich GmbH Jülich Germany ([ROR:02nv7yv05](https://ror.org/02nv7yv05))

† Corresponding author

## Abstract

Cells steadily adapt their membrane glycerophospholipid (GPL) composition to changing environmental and developmental conditions. While the regulation of membrane homeostasis via GPL synthesis in bacteria has been studied in detail, the mechanisms underlying the controlled degradation of endogenous GPLs remain unknown. Thus far, the function of intracellular phospholipases A (PLAs) in GPL remodeling (Lands cycle) in bacteria is not clearly established. Here, we identified the first cytoplasmic membrane-bound phospholipase A1 (PlaF) from Pseudomonas aeruginosa, which might be involved in the Lands cycle. PlaF is an important virulence factor, as the P. aeruginosa ΔplaF mutant showed strongly attenuated virulence in Galleria mellonella and macrophages. We present a 2.0-Å-resolution crystal structure of PlaF, the first structure that reveals homodimerization of a single-pass transmembrane (TM) full-length protein. PlaF dimerization, mediated solely through the intermolecular interactions of TM and juxtamembrane regions, inhibits its activity. The dimerization site and the catalytic sites are linked by an intricate ligand-mediated interaction network, which might explain the product (fatty acid) feedback inhibition observed with the purified PlaF protein. We used molecular dynamics simulations and configurational free energy computations to suggest a model of PlaF activation through a coupled monomerization and tilting of the monomer in the membrane, which constrains the active site cavity into contact with the GPL substrates. Thus, these data show the importance of the PlaF-mediated GPL remodeling pathway for virulence and could pave the way for the development of novel therapeutics targeting PlaF.

## Introduction

Biological membranes are steadily changing and adapting to environmental and developmental conditions (Eickhoff and Bassler, 2018; Parsons and Rock, 2013). These changes affect processes indispensable for cell life, such as nutrient uptake (Higgins, 1992), chemical signaling (Venturi and Fuqua, 2013), protein secretion (Krampen et al., 2018), folding (Mackenzie, 2006), interaction with hosts (Baxter et al., 2015), and antibiotic resistance (García-Fernández et al., 2017). An important mechanism to maintain membrane functionality in bacteria is the alteration of lipid composition (Rowlett et al., 2017; Schniederjans et al., 2017; Zhang and Rock, 2008). The adjustment of the fatty acid (FA) composition of glycerophospholipids (GPLs) upon thermal adaptation represents one of the most important mechanisms of membrane lipid homeostasis (Sinensky, 1974; Cossins, 1994). Adaptive changes in membrane GPL composition were observed under numerous other conditions, including environmental stresses (Rowlett et al., 2017), the transition from planktonic to sessile lifestyle (Benamara et al., 2014), and heterologous protein production (Kanonenberg et al., 2019).

De novo synthesis of GPLs is the main pathway used to tune the proportions of different lipid classes in bacteria (Zhang and Rock, 2008; Jeucken et al., 2019). Furthermore, bacteria rapidly alter their membrane GPL composition by chemical modifications (cis-trans isomerization and cyclopropanation) of acyl chains in GPLs to respond to environmental changes (Zhang and Rock, 2008). However, the bacterial pathway for remodeling of GPLs involving a rapid turnover of the acyl chains of GPLs is unknown. Interestingly, such a pathway was discovered in eukaryotes by W. E. Lands more than 60 years ago (Lands, 1958). This Lands cycle involves PLA-catalyzed deacylation of membrane GPLs to mono-acyl GPLs (lysoGPLs) followed by lysophospholipid acyltransferase (LPLAT)-mediated acylation of lysoGPL to yield a new GPL molecule with acyl chain composition different from the starting GPL (Lands, 1958). Despite the importance of this metabolic process in different animal and plant tissues, it took nearly 50 years before the enzymes involved in phospholipid remodeling were discovered (Shindou and Shimizu, 2009). Fourteen different mammalian LPLAT with specificities for different GPL head groups were reported to be involved in the Lands cycle (Hishikawa et al., 2008; Valentine et al., 2022). The recently published structure of human LPLAT provided the first insights into the molecular mechanism by which lysoGPL is acylated to GPL (Zhang et al., 2021). At least 16 mammalian PLAs (cytosolic and calcium-independent families) that may act on the membrane GPLs with different substrate profiles and tissue expression patterns are known (Clark et al., 1990; Song et al., 1999; Underwood et al., 1998; Ohto et al., 2005). Some PLAs have a suggested role in the remodeling of membrane GPLs (Asai et al., 2003), while others are involved in producing lipid mediators and bioenergetics (Murakami et al., 2020). Detailed computational studies revealed that human iPLA2β is allosterically activated by binding to the membrane, which is required to extract a single GPL molecule from the membrane and subsequent hydrolysis (Mouchlis et al., 2015).

Whereas extensive studies have been carried out for secreted bacterial PLAs acting as host-cell effectors (Istivan and Coloe, 2006), only limited information is available for the enzymes from the intracellular PLA family (Flores-Díaz et al., 2016). Previously, we reported that periplasmic TesA from Pseudomonas aeruginosa is a multifunctional enzyme with lysoPLA activity (Kovačić et al., 2013). However, this enzyme has no PLA activity, and therefore it is most likely not related to membrane GPL remodeling (Leščić Ašler et al., 2010). We recently published a novel intracellular PLA from P. aeruginosa whose function for remodeling of GPLs still needs to be experimentally analyzed (Weiler et al., 2022). Comprehensive lipidomic profiling of 113 Escherichia coli strains with deleted or overexpressed lipid metabolism genes did not reveal the identity of an intracellular PLA suitable for the Lands cycle (Jeucken et al., 2019). Here, we describe PlaF from P. aeruginosa (Kovacic et al., 2016; Bleffert et al., 2019) as the first cytoplasmic membrane-bound PLA with a role in virulence and GPL remodeling pathway in bacteria. We determined the crystal structure of PlaF (Kovacic et al., 2016; Bleffert et al., 2019) as a basis to provide mechanistic insights into PLA-mediated membrane phospholipid degradation related to bacterial virulence.

## Results

### PlaF is an integral cytoplasmic membrane-bound enzyme

We previously purified PlaF from the Triton X-100 solubilized membranes of a P. aeruginosa strain carrying the p-plaF expression plasmid (Kovacic et al., 2016; Bleffert et al., 2019). Here, we show that catalytically active PlaF is an intrinsic integral membrane protein as it was absent in the soluble fraction of the P. aeruginosa p-plaF (Figure 1a) and remained membrane-associated after treatment of PlaF-containing membranes with denaturation agents (Na2CO3 or urea), which destabilize weak interactions between peripheral proteins and the membrane (Figure 1b). To identify if PlaF is associated with the inner or outer membrane, P. aeruginosa p-plaF membranes were fractioned by ultracentrifugation in a sucrose density gradient. Western blot analysis of the cytoplasmic membrane protein SecG (Bleves et al., 1996), and the outer membrane-associated Lipid A (Matsushita et al., 1978) combined with PlaF activity measurement revealed that the majority of PlaF was in the cytoplasmic membrane fractions (#9–13) (Figure 1c). As expected, the Lipid-A-containing fractions (#1–3) showed negligible PlaF activity (Figure 1c), overall demonstrating that PlaF is a cytoplasmic integral membrane protein. Proteolysis experiments in which P. aeruginosa p-plaF cells with a chemically permeabilized outer membrane were treated with trypsin revealed a time-dependent degradation of PlaF (Figure 1d). These results suggest that PlaF is likely anchored to the cytoplasmic membrane via a transmembrane (TM) domain at the N-terminus predicted from sequence analysis (Kovacic et al., 2016), and its catalytic C-terminal domain protrudes into the periplasm.

![Figure 1.](https://cdn.elifesciences.org/articles/72824/elife-72824-fig1-v2.jpg)

**Figure 1.:** (a) PlaF is a membrane protein of Pseudomonas aeruginosa. The membrane (M) and soluble fractions (SFs) of cell extracts from P. aeruginosa p-plaF, and the empty vector control strain (EV) were separated, analyzed by immunodetection with anti-His6-tag antibodies, and by esterase activity assay. The membrane protein marker P. aeruginosa XcpQ was detected with anti-XcpQ antibodies. (b) PlaF is an integral membrane protein of P. aeruginosa. The crude membranes of P. aeruginosa p-plaF were treated with sodium carbonate, urea, Triton X-100, or MES buffer control followed by ultracentrifugation (S, supernatant; M, membrane proteins). PlaF was detected as in (a). (c) PlaF is a cytoplasmic-membrane protein of P. aeruginosa. The membrane fractions of P. aeruginosa p-plaF and the EV strains were isolated and separated by ultracentrifugation in a sucrose density gradient. The esterase activity was assayed as in (a). P. aeruginosa SecG, and outer membrane lipid A were used as markers for cytoplasmic, and outer membranes, and detected by Western blotting using anti-SecG, and anti-Lipid A antibodies, respectively. Inlet: A model of PlaF cellular localization. All values are mean ± standard deviation (S.D.) of three independent experiments measured in triplicates. (d) The catalytic domain of PlaF is exposed to the periplasm. P. aeruginosa p-plaF cells with permeabilized outer membrane were treated with trypsin for the indicated periods, and PlaF was detected as described in (a).

### PlaF is a PLA1 involved in the alteration of membrane GPL composition as determined by global lipidomics

The previously reported carboxylesterase activity of PlaF (Bleffert et al., 2019) was here further analyzed using different PLA substrates. PlaF, purified with n-octyl-β-D-glucoside (OG) as described previously (Kovacic et al., 2016), showed PLA1 but no PLA2 activity toward the artificial substrates specific to each of these two phospholipase families (Figure 2a) and the natural phospholipid diacyl phosphatidylglycerol containing pentanoic and oleic acid at the sn-1 and sn-2 positions, respectively (Figure 2—figure supplement 1). The substrate profile of PlaF against natural di-acyl GPLs commonly occurring in P. aeruginosa membranes (Benamara et al., 2014) was determined with a spectrum of substrates (see legend to Figure 2b). In vitro, purified PlaF preferably hydrolyzed GPLs containing medium-chain FAs (C12 and C14) and showed comparable activities with phosphatidylethanolamine (PE), phosphatidylglycerol (PG), and phosphatidylcholine (PC) (Figure 2b).

![Figure 2.](https://cdn.elifesciences.org/articles/72824/elife-72824-fig2-v2.jpg)

**Figure 2.:** (a) PlaF is a phospholipase A1. Enzyme activities of PlaF were measured fluorimetrically using artificial PLA1, and PLA2 substrates containing either ethanolamine (PE) or choline (PC) head groups. The control enzymes were PLA1 of Thermomyces lanuginosus, and PLA2 of Naja mocambique. Results are means±S.D. of three independent measurements performed with at least three samples. (b) PlaF releases FAs from naturally occurring bacterial GPLs. PLA activity of PlaF was measured by quantification of released FAs after incubation of PE, PG, and PC substrates containing FAs with different chain lengths (C12–C18). (c) PlaF changes GPL composition of Pseudomonas aeruginosa cells. Crude lipids extracted from P. aeruginosa wild-type (WT), ΔplaF, and ΔplaF::plaF membranes were quantified by Q-TOF-MS/MS using an internal standard mixture of GPLs. PlaF substrates are elevated in ΔplaF and depleted in ΔplaF::plaF, while modified GPLs show inverse response than GPL substrates. The GPL amount (nmol) was normalized to mg of crude lipids, and optical density (Supplementary file 3). FA composition of GPL is depicted as XX:Y, where XX defines the number of carbon atoms, and Y defines the number of double bonds in FAs bound to GPL. Results are mean ± S.D. of four biological replicates of WT, ΔplaF, and three of the ΔplaF::plaF. T-test of normally distributed values, ** p<0.01, * p<0.05. FA, fatty acid; GPL, glycerophospholipid.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/72824/elife-72824-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (a) Total ion current chromatogram of fatty acid (FA) methyl ester standards. Standard curves of C15 (b) and C18:1 cis-Δ9 (c) methyl esters. (d) FAs were extracted with organic solvent from samples in which PG-15:0-18:1 was incubated with PlaF. Silylated FAs were quantified by GC-MS. Palmitic and stearic acids detected in these samples were probably bound to PlaF used in the experiment. (e) FA amounts detected in PlaF and blank samples. Results are means ± standard deviations of two independent experiments. GC-MS, gas chromatography-mass spectrometric.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/72824/elife-72824-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** (a) Generation of the mutagenesis vector pEMG-ΔplaF and homologous recombinant with a chromosome of P. aeruginosa PAO1 (Martínez-García and de Lorenzo, 2011). Upstream and downstream regions of the plaF gene were amplified by standard PCR using Phusion DNA polymerase, a genomic DNA of P. aeruginosa PAO1 as a template, and primer pairs 5′-ATATATGAATTCTCTGCTCGGCGCGAAACGCAGCGP-3′/5′-ATATATACGCGTGGGTGTCCGAAGGCTTCAGGAAAAAAGGGGC-3′ and 5′-ATATATACGCGTAAACGCGAACCGGCGCCTGGG-3′/5′-CTGGATGAATTCTGGCCTGGACACCGACAAGGAAGTGATCAAGG-3′, respectively. DNA fragments upstream and downstream of plaF gene were cloned into the pEMG vector by ligation of DNA fragments hydrolyzed with EcoRI restriction endonuclease. The white arrow indicates the neomycin phosphotransferase II gene (nptII) necessary for plasmid selection in the presence of kanamycin antibiotic. DNA recognition sequence for I-SceI restriction endonuclease is indicated with the red arrows. (b) Sequence alignment of DNA products of P. aeruginosa ΔplaF and the wild-type (WT) strain obtained by PCR as described in Figure 2—figure supplement 2. The start and stop codons of plaF gene are indicated in red, identical nucleotides are indicated in gray, the recognition site for MluI restriction endonuclease inserted on the chromosome using the mutagenesis vector pEMG-ΔplaF in yellow. The company Eurofins Genomics (Ebersberg, Germany) performed DNA sequencing. (c) Verification of P. aeruginosa ΔplaF and ΔplaF::plaF strains by PCR. Standard PCR was performed using Phusion DNA polymerase and the primers (5′-AAGGTCGCCGCCAGGAATTTCCG-3′/5′-CCGCCTGCGTGCCGACTACAAGG-3′) that bind to the up- and downstream regions of plaF gene. As PCR templates were used genomic DNA of P. aeruginosa PAO1 (WT), pEMG-ΔplaF plasmid and DNA obtained from the colony of P. aeruginosa ΔplaF or ΔplaF::ΔplaF scratched from the LB agar plate and suspended in water. The expected sizes of DNA fragments were 1494, 552, 552, and 322 bp for WT, ΔplaF, and pEMG-ΔplaF, and ΔplaF::plaF, respectively. DNA products were analyzed by electrophoresis on agarose gel (1% w/v). The sizes of standard DNA fragments are indicated on the left. (d) Generation of pUC18T-mini-Tn7T-Gm-plaF plasmid for recombination of plaF gene containing 128 bp upstream region of plaF with a chromosome of P. aeruginosa ΔplaF. DNA fragment containing upstream region and plaF gene was amplified using primer pair 5′-AATAGAGCTCACCGCCGTCCTTAGGTTC-3′/5′-AATAGAGCTCCGTTTTCAGCGACCGGC-3′ from the genomic DNA of P. aeruginosa PAO1. Both primers contained the restriction site SacI for cloning into the pUC18T-mini-Tn7T-Gm (gifts from Herbert Schweizer, Addgene plasmids #63121, #64968, and #64946) which consists of β-lactamase resistance gene (bla), ColE1 origin of replication (ori), the origin of conjugative transfer (oriT), left and right ends of Tn7 (Tn7L and Tn7R), Flp recombinase target (FRT) and gentamycin acetyltransferase gene (aacC1). (e) Phospholipase A1 activity of P. aeruginosa ΔplaF and ΔplaF::plaF. P. aeruginosa PAO1, ΔplaF, and ΔplaF::plaF strains were grown overnight in LB medium at 37°C, and cells were harvested at O.D.580nm~1 by centrifugation. Cells were suspended in Tris-HCl buffer (100 mM, pH 8) to equal cell count, and enzyme activities of these samples were measured using PLA1 assays with N-((6-(2,4-DNP)amino)hexanoyl)–1-(BODIPYFL C5)–2-hexyl-sn-glycero-3-phosphoethanolamine substrate. Activities are normalized on the activity of the WT which was set as 100%. The results are mean ± S.D. of two experiments with three biological replicates each measured three times. LB, lysogeny broth.

To examine the role of membrane-bound PlaF in the regulation of the membrane GPL composition in vivo, we constructed the P. aeruginosa deletion mutant ΔplaF lacking the entire plaF gene by homologous recombination, and a complemented ΔplaF::plaF strain as a control (Figure 2—figure supplement 2). The activity assay showed ~90% loss of PLA1 activity in the mutant strain, and restoration of activity in ΔplaF::plaF slightly above the wild-type (WT) level (Figure 2—figure supplement 2). These findings indicate that PlaF is a major but not the only intracellular PLA1 in P. aeruginosa.

The quantitative mass spectrometric (Q-TOF-MS/MS) analysis of total GPLs isolated from four biological replicates of P. aeruginosa WT, ΔplaF, and ΔplaF::plaF cells revealed significant differences in membrane GPL composition (Figure 2c, Supplementary files 1-3). Statistical analysis of 323 GPL molecular species identified six significantly (p<0.05) accumulating GPLs, varying in the composition of head groups (PE, PG, PC, and phosphatidylinositol, PI), length, and unsaturation of acyl chains, in P. aeruginosa ΔplaF. Interestingly, these GPLs were present at low concentrations in the cells which may explain why they were not detected in the previous lipidomic analyses of P. aeruginosa GPLs (Benamara et al., 2014; Le Sénéchal et al., 2019). In the complemented strain (ΔplaF::plaF), these GPLs were depleted compared to the ΔplaF, although not to the WT level (Supplementary file 2). These results strongly indicate that PlaF specifically hydrolyses low abundant GPLs in vivo. We furthermore observed that the other seven PE, PG, and PC species, which belong among the most abundant P. aeruginosa GPLs (Benamara et al., 2014; Le Sénéchal et al., 2019), were significantly depleted (Figure 2c) in P. aeruginosa ΔplaF, and their concentrations were significantly elevated in complementation strain (Figure 2c). This may explain why the net GPL contents of the WT and the ΔplaF strain were not significantly (p=0.67) different. Significantly affected GPLs in the ΔplaF strain account for ~11% (mol/mol) of the total GPL content, indicating the profound function of PlaF in membrane GPL remodeling.

Our quantitative lipidomics results, which revealed that several PE, PG, and PC molecular species accumulated or were depleted in ΔplaF, together with in vitro PLA activity data of PlaF with various PE, PG, and PC substrates, indicate that PlaF might be a major PLA involved in the Lands cycle (Figure 2d). Thus, the six low-abundant PE, PG, and PC species that accumulated in ΔplaF might be PlaF substrates. PlaF-mediated hydrolysis of these substrates yields lysoGPL intermediates. Acylation of these lysoGPLs by an unknown acyltransferase will produce modified GPLs typical to P. aeruginosa. The absence of lysoGPL intermediates in ΔplaF will lead to the depletion of modified GPLs (Figure 2d).

### PlaF is a potent virulence factor of P. aeruginosa affecting in vivo toxicology

We next addressed the question of whether PlaF contributes to the virulence of P. aeruginosa by using the G. mellonella infection model and the bone marrow-derived macrophages (BMDMs) viability assay. The results revealed a remarkable difference in the survival of G. mellonella larvae infected with P. aeruginosa WT or ΔplaF. While ΔplaF was avirulent during 20 hr of infection, the majority of the larvae (~80 %) did not survive 20 hr after infection with the P. aeruginosa WT (Figure 3a). The viability assays with P. aeruginosa-infected BMDMs showed a significantly (p<0.01) stronger killing effect of P. aeruginosa WT compared to ΔplaF 6 hr after infection (Figure 3b). As expected, the complemented strain (ΔplaF::plaF) restored the loss of virulence of ΔplaF in G. mellonella, and BMDM assays (Figure 3a and b). Comparison of the growth curves of P. aeruginosa ΔplaF, and the WT in nutrient-rich medium (Figure 3—figure supplement 1) showed that PlaF most likely does not reduce virulence by affecting the growth of P. aeruginosa.

![Figure 3.](https://cdn.elifesciences.org/articles/72824/elife-72824-fig3-v2.jpg)

**Figure 3.:** (a) Left: P. aeruginosa ΔplaF strain is less virulent than the respective wild-type (WT) strain in a Galleria mellonella larvae virulence assay. Kaplan-Meier plot of representative data of at least two experiments with 10 larvae per group. PBS treated and untreated larvae served as infection and viability controls, respectively. Right: Statistical analysis of the survival at the 20 hr using three independent experiments with 10 larvae each. (b) P. aeruginosa ΔplaF strain is less cytotoxic to bone marrow-derived macrophages (BMDMs) than the WT strain in cell culture. The BMDM cells (5×105) were infected with 5×105 bacteria in a 24-well plate, and lactate dehydrogenase activity in supernatants was determined as a measure of BMDM death. The ΔplaF phenotype could be complemented with P. aeruginosa ΔplaF::plaF. PBS or Triton-X100 (1% v/v) treated cells served as viability or 100% killing controls, respectively. Results are the representative data of two independent experiments (n=10). One-way ANOVA analysis, *** p<0.001, ** p<0.01, ns, not significant; PBS, phosphate-buffered saline.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/72824/elife-72824-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** P. aeruginosa strains (n=3) were grown in LB medium in Erlenmeyer flasks at 37°C. LB, lysogeny broth.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/72824/elife-72824-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** Pseudomonas alcaligenes (Pal-PlaF; sequence ID: A0A142IQQ0; sequence identity 68%, coverage 97%), Pseudomonas mendocina (sequence ID: A0A291K7Z5; sequence identity 63%, coverage 100%), Pseudomonas otitidis (sequence ID: A0A1I0U5Q8; sequence identity 62%, coverage 100%), Acinetobacter baumannii (sequence ID: A0A1G5KTV2; sequence identity 99.7%, coverage 100%), Klebsiella pneumoniae (sequence ID: OON65700.1; sequence identity 27%, coverage 90%), and Streptococcus pneumoniae (sequence ID: CGG52681.1; sequence identity 28%, coverage 90%). Residues identical and similar in at least five sequences were shaded in black and yellow, respectively. The catalytic triad residues of PlaF are indicated with an asterisk. The figure was prepared using BioEdit software. (Skjevik et al., 2016).

A BLAST search revealed PlaF orthologs in more than 90% of all sequenced P. aeruginosa genomes, including 571 clinical isolates (Supplementary file 4). Furthermore, we found PlaF homologs in pathogens from the Pseudomonas genus (P. alcaligenes, P. mendocina, and P. otitidis), and other high-priority pathogens (Acinetobacter baumannii, Klebsiella pneumoniae, and Streptococcus pneumoniae) (Figure 3—figure supplement 2). These results indicate that PlaF is a novel and potent P. aeruginosa virulence factor, which is conserved in important pathogens and, therefore, might be a promising target for developing novel broad-range antibiotics.

### Crystal structure of PlaF homodimer in the complex with natural ligands

To gain insights into the PlaF structure, we crystallized the OG-solubilized PlaF protein purified from P. aeruginosa membranes as described previously (Bleffert et al., 2019). The structure was refined at a resolution of up to 2.0 Å (Table 1). The final model in the asymmetric unit consists of two protein molecules (PlaFA and PlaFB), which are related by improper twofold non-crystallographic symmetry (Figure 4a). Active site cavities of both the monomers reveal non-covalently bound ligands—myristic acid (MYR), OG, and isopropyl alcohol (IPA) in PlaFA; and undecyclic acid (11A), OG, and IPA in PlaFB (Figure 4a, Supplementary file 5). These FAs are the natural ligands from the homologous organism P. aeruginosa that were co-purified with PlaF, as confirmed by gas chromatography-mass spectrometric (GC-MS) analysis of organic solvent extracts of purified PlaF (Figure 4—figure supplement 1). Compared to the protein chains, the bound FAs have higher average B-factor values for 11A (89.0 Å2) and MYR (66.6 Å2), indicating different flexibility of the ligands bound to the active sites of the two PlaF molecules.

**Table 1.**
 Data collection and refinement statistics on PlaF.


<table>
  <thead>
    <tr>
      <th colspan="2">X-ray data</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Beamline/detector</td>
      <td>ID29, ESRF (Grenoble, France)/DECTRIS PILATUS 6M</td>
    </tr>
    <tr>
      <td>Wavelength (Å)/monochromator</td>
      <td>λ=0.96863/channel-cut silicon monochromator, Si (111)</td>
    </tr>
    <tr>
      <td>Resolution range (Å)</td>
      <td>47.33–2.0 (2.05–2.0)*</td>
    </tr>
    <tr>
      <td>Space group</td>
      <td>I 41 2 2</td>
    </tr>
    <tr>
      <td>Unit cell (a=b), c (Å); α=β=γ</td>
      <td>a=133.87 c=212.36; 90°</td>
    </tr>
    <tr>
      <td>Total reflections</td>
      <td>669,964 (47,385)</td>
    </tr>
    <tr>
      <td>Unique reflections</td>
      <td>65,113 (4527)</td>
    </tr>
    <tr>
      <td>Multiplicity</td>
      <td>10.3 (10.5)</td>
    </tr>
    <tr>
      <td>Completeness (%)</td>
      <td>100.0 (100.0)</td>
    </tr>
    <tr>
      <td>Mean I/sigma (I)</td>
      <td>24.6 (2.5)</td>
    </tr>
    <tr>
      <td>Wilson B-factor (Å2)</td>
      <td>38.3</td>
    </tr>
    <tr>
      <td>R-merge (%)</td>
      <td>5.3 (91.3)</td>
    </tr>
    <tr>
      <td>R-meas (%)</td>
      <td>5.6 (100.6)</td>
    </tr>
    <tr>
      <td colspan="2">Refinement</td>
    </tr>
    <tr>
      <td>R-work (%)</td>
      <td>16.3 (23.15) (2.071–2.0)*</td>
    </tr>
    <tr>
      <td>R-free (%)</td>
      <td>18.57 (27.81)</td>
    </tr>
    <tr>
      <td>Number of atoms</td>
      <td>5187</td>
    </tr>
    <tr>
      <td>Macromolecules</td>
      <td>4831</td>
    </tr>
    <tr>
      <td>Ligands</td>
      <td>123</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>233</td>
    </tr>
    <tr>
      <td>Protein residues</td>
      <td>620</td>
    </tr>
    <tr>
      <td>RMS (bonds)</td>
      <td>0.008</td>
    </tr>
    <tr>
      <td>RMS (angles)</td>
      <td>1.07</td>
    </tr>
    <tr>
      <td>Ramachandran favored (%)</td>
      <td>99</td>
    </tr>
    <tr>
      <td>Ramachandran outliers (%)</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Clashscore</td>
      <td>3.14</td>
    </tr>
    <tr>
      <td>Average B-factor (Å2)</td>
      <td>49.1</td>
    </tr>
    <tr>
      <td>Macromolecules (Å2)</td>
      <td>48.8</td>
    </tr>
    <tr>
      <td>Ligands (Å2)</td>
      <td>79.2</td>
    </tr>
    <tr>
      <td>Solvent (Å2)</td>
      <td>47.9</td>
    </tr>
  </tbody>
</table>

_*Values in parentheses are for the highest resolution shell._

![Figure 4.](https://cdn.elifesciences.org/articles/72824/elife-72824-fig4-v2.jpg)

**Figure 4.:** (a) A unique N-terminal helix comprising a putative transmembrane helix (αTM1, L5–L27, gray) flanked by charged residues (K2, R3) on one side and, on another side, the juxtamembrane helix (αJM1, A28–L37, yellow). αJM1 links the αTM1 with the catalytic domain, which consists of an α/β-hydrolase (blue, α-helices; green, β-strands, and gray, loops), and a lid-like domain (brown). Ligands bound in the active site cleft are shown as ball-and-sticks (oxygen, red; carbon of OG, MYR, and IPA, green, orange, and blue, respectively). Thick gray lines roughly depict the membrane borders. (b) Dimer interface. Interactions involving TM-JM helices are predominantly hydrophobic with four weak H-bonds (indicated by a red asterisk) detected mostly in the αJM1. R83 is the only residue outside of the JM-TM helix involved in interactions. Residues of the PlaFB molecule are indicated in italics. A detailed list of interactions is provided in Supplementary file 6. (c) A model suggesting the orientation of PlaF in the membrane. The water molecules are indicated as green spheres. The transparent surface of PlaF was colored as in (a). PlaF is rotated by 180° along the normal to the membrane compared with Figure 4. (d) Interaction network within the ligand-binding cleft of PlaFA. MYR is linked via H-bond with the catalytic S137, and via hydrophobic interactions with OG. The sugar moiety of OG from PlaFA forms H-bonds with V33 of PlaFA, which is interacting with V33 and G36 of PlaFB. The part of the cleft in the direction of the opening 3 is occupied by several water molecules (W, yellow spheres). The cleft accommodates one IPA molecule bound to the water. Arrows indicate two openings not visible in this orientation. The cleft was calculated using the Pymol software and colored by elements: carbon, gray; oxygen, red; nitrogen, blue. FA, fatty acid.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/72824/elife-72824-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** FAs were extracted from purified PlaF samples with organic solvent followed by silylation and gas chromatographic separation with mass spectrometric detection (GC-MS). GC chromatograms of pure C10, C11, and C14 fatty acids as standards (a) were compared to PlaF extracts (b). Mass spectrometric analysis of compounds with retention times 23.43/23.42 min and 29.95 min for FA standards (c, e) and PlaF extracts (d, f) revealed the presence of undecanoic and myristic acid trimethylsilyl esters, respectively. The chemical structure of undecanoic and myristic acid trimethylsilyl ester and characteristic fragments (Diekman et al., 2002) (molecular weights in Da are indicated above) identified in mass spectra are shown.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/72824/elife-72824-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** (a) Superposition of PlaFA (cyan) and PlaFB (orange). The arrow indicates the kink in TM-JM helix. (b) Crystal packing of PlaF showing a four-helix bundle formed by TM-JM helices. For clarity, two dimers are shown in cyan and orange colors. The ligands present are shown as filled circles and colored according to the element (carbon yellow and oxygen red). The unit cell (black square) and the a-b axes are labeled. (c) Coiled-coil structure of the TM-JM. Enlarged section of PlaF viewed from the periplasmic side showing the coiled-coil organization of the TM-JM helix and the OG ligands located between JM and the loop preceding αF in both PlaF monomers. Elements of the PlaFB molecule are indicated in italics.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/72824/elife-72824-fig4-figsupp3-v2.jpg)

**Figure 4—figure supplement 3.:** Pairwise structural alignment of PlaFB (colored orange) with 1cqz (a), 1orw (b), 1yr2 (c), 1z68 (d), 2bkl (e), 2ecf (f), 2bgc (g), 2jbw (h), 2roq (i), 3mga (j), 3mun (k), 3o4j (l), 4hai (m), 4n8e (n), 5alj (o), 5l8s (p), 5t88 (q), 5yzm (r), 6eop (s), 6hxa (t), and 6igp (u). PlaF structural homologs (colored gray) containing conserved sequence in TM-JM helix region of PlaF (yellow highlighted in Supplementary file 6) and in catalytic domain as identified by Dali server.

![Figure 4—figure supplement 4.](https://cdn.elifesciences.org/articles/72824/elife-72824-fig4-figsupp4-v2.jpg)

**Figure 4—figure supplement 4.:** Lid-like domains, shown in pink, vary considerably among PlaF and hydrolytic enzymes (hydrolase HsaD from Mycobacterium tuberculosis, PDB ID 2VF2 Lack et al., 2010; lipase LipA from Pseudomonas aeruginosa, PDB ID 1E × 9 Nardini et al., 2000; and hydrolase CarC from Janthinobacterium sp. strain J3, PDB ID 1J1I Habe et al., 2003) with structurally conserved α/β-hydrolase domains (light blue).

![Figure 4—figure supplement 5.](https://cdn.elifesciences.org/articles/72824/elife-72824-fig4-figsupp5-v2.jpg)

**Figure 4—figure supplement 5.:** (a) Ribbon representation of the dimer structure colored according to B-factor. The lid domain and the N-terminal helices show significantly higher B-factors (color spectrum white—low B-factor, to red—high B-factor). The average B-factors of the αTM1 helix and the lid domain in PlaF dimer are ~74 and ~55 Å2, respectively. (b) Thermal ellipsoid representation of the dimer scaled by the B-factors combined with TLS (translation-libration-screw-rotation model) displays comparatively higher B-factors in the lid domain in molecule B and the αTM1 helix in molecule A. The figure was prepared using CCP4mg (Winn et al., 2011).

The N-terminal 38 amino acids form a long, kinked helix that comprises the putative TM (αTM1) and the JM (αJM1) helices, connecting the catalytic domain with the membrane (Figure 5a). The kink angle in the TM-JM helices is the main difference between the two monomers (Figure 4—figure supplement 2) and is likely caused by crystal packing effects (Figure 4—figure supplement 2). Dimerization is mediated primarily via hydrophobic interactions between symmetry-nonrelated residues from the TM-JM domains of two monomers (Figure 4b, Supplementary file 6), consistent with the hydrophobic effects that dominate in the stabilization of dimeric TM domains (MacKenzie et al., 1997). In addition, four weak H-bonds (Figure 4b) between JM residues stabilize the PlaF dimer. The TM-JM helices adopt a coiled-coil-like conformation (Figure 4—figure supplement 2), where the αTM1 crosses its counterpart at V14 to form an elongated X-shaped dimer interface with the buried surface area of 656 Å2 per monomer. The full-length PlaF dimer represents a unique structure, as neither a relevant match to the TM-JM helix (Figure 4—figure supplement 3) nor the membrane-spanning coiled-coil structure of the TM-JM dimer has been reported previously.

![Figure 5.](https://cdn.elifesciences.org/articles/72824/elife-72824-fig5-v2.jpg)

**Figure 5.:** (a) PlaF forms dimers in cell membranes.In vivo cross-linking experiments were performed by incubating Pseudomonas aeruginosa p-plaF or the empty vector control (EV) cells with different concentrations of DMP cross-linker followed by immunodetection of PlaF with anti-PlaF antiserum. (b) In vitro cross-linking of purified PlaF. Purified PlaF was incubated with DMP, BS2G, and BS3 cross-linking reagents or buffer control (ø) for 90 min, and the samples were analyzed by SDS-PAGE. Molecular weights of protein standard in kDa are indicated. (c) PlaF homodimerization, and activity are concentration-dependent. Protein-protein interactions of purified PlaF were monitored by measuring the changes in thermophoresis (ΔFnorm, gray circles) using the MST method. The MST results are mean ± S.D. of two independent experiments with PlaF purified with OG. Esterase activity (black squares) of PlaF was measured in three independent experiments using 4-methylumbelliferyl palmitate substrate. Dissociation (KD) and activation (Kact) constants were calculated using a logistic fit of sigmoidal curves.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/72824/elife-72824-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** The SDS-PAGE analysis of in vivo cross-linking samples of Pseudomonas aeruginosa strain carrying pBBR1mcs-3 (empty vector control, EV) or p-plaF obtained in the experiment shown in Figure 5a. Molecular weights of protein standard (St) in kDa are indicated.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/72824/elife-72824-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** PlaF (10 µl, 2 mg/ml) purified with OG and standard proteins, bovine serum albumin (BSA), equine myoglobin (Myo), and bovine ribonuclease A (RNase A) were separately analyzed using Biosep-SEC-S2000 column. Proteins were detected by measuring absorbance at a wavelength of 280 nm, and values were normalized to the maximal A280nm of each protein.

### The crystal structure of PlaF is indicative of a specific orientation in the membrane

The catalytic domain of PlaF adopts a canonical α/β-hydrolase fold (Ollis et al., 1992; Figure 4a) with three α-helices forming a distinct lid-like domain that covers the active site (Figure 4a). Despite the high homology of the catalytic domain, the lid-like domain varies significantly between PlaF homologs (Figure 4—figure supplement 4), as observed previously for other lipolytic enzymes (Figure 4—figure supplement 4; Chow et al., 2012). Furthermore, the lid-like domain shows a less ordered structure, as suggested by comparatively higher B-factors (Figure 4—figure supplement 5). This is likely a consequence of the lack of stabilizing interactions between the charged residue-rich (23 of the 77 residues) lid-like domain and the hydrophilic head groups of membrane GPLs in the native membrane environment. The TLS (translation-libration-screw-rotation) model revealed higher disorder in the TM-JM domains, presumably also due to the missing interactions with the hydrophobic membrane (Figure 4—figure supplement 5). No ordered water molecules in the vicinity of αTM1 (Figure 4c) and the presence of several charged and polar residues adjacent to αTM1 suggest a model where the TM-JM domain spans through the membrane with the catalytic domain localized on the membrane surface (Figure 4c).

### Ligand-mediated interaction network connects dimerization and active sites

The active site of PlaF comprises the typical serine-hydrolase catalytic triad with S137, D258, and H286 interacting through H-bonds (Jaeger et al., 1994; Supplementary file 7). Interestingly, S137 shows two side-chain conformations, where one conformer is within the hydrogen bond distance of the FA ligand (Figure 4d, Supplementary files 5 and 7). Additionally, S137 forms H-bonds with residues I160, D161, and A163 located in the lid-like domain. The active site cleft in PlaF is formed by residues from the helix αJM1, the α/β-hydrolase and the lid-like domains (Figure 4d, Supplementary file 8). In PlaF, the large T-shaped active site cleft formed by residues from the JM helix, the α/β-hydrolase, and the lid-like domains is amphiphilic, making it compatible with binding the bulky GPL substrates. Three openings are observed in the cleft—one, close to the catalytic S137, lined with residues from the loops preceding αE, and αF; second, in the middle pointing toward the putative membrane, lined mostly with polar residues of the loops preceding αB, and αF; and third, at the dimer interface, comprising residues from αJM1, and the loop preceding αF of the lid-like domain. The third opening accommodates a pseudo-ligand OG (Figure 4d), which with its pyranose ring interacts with residue V33 of PlaFA, which in turn participates in dimerization via interactions with V33 and T32 of PlaFB (Figure 4b). The alkyl chains of OG and MYR bound in the active site cleft are stabilized via hydrophobic interactions (Figure 4d). Finally, the H-bond interaction of catalytic S137 with the carboxyl group of MYR completes an intricate ligand-mediated interaction network bridging the catalytic (S137) and dimerization (V33) sites in PlaF (Figure 4d). The crystal structure presented thus suggests a role of dimerization and ligand binding in regulating PlaF function, which was subsequently analyzed biochemically.

### The PlaF activity is affected by dimerization

To investigate the oligomeric state of PlaF in vivo, we performed cross-linking experiments in which intact P. aeruginosa p-plaF cells were incubated with the cell-permeable bi-functional cross-linking reagent dimethyl pimelimidate (DMP). Western blot results revealed the presence of monomeric and dimeric PlaF in DMP-treated cells, whereas dimers were absent in untreated cells (Figure 5a and Figure 5—figure supplement 1). Size exclusion chromatography showed that PlaF was extracted from the membranes with detergent and purified by IMAC elutes as a monomer (Figure 5—figure supplement 2). Incubation of this purified PlaF for 90 min with bi-functional cross-linkers of different lengths (DMP; bis(sulfosuccinimidyl) glutarate, BS2G or bis(sulfosuccinimidyl) suberate, BS3) resulted in the formation of a substantial amount of PlaF dimers, suggesting spontaneous dimerization in the solution (Figure 5b). Microscale thermophoresis (MST) measurements were performed in which the fluorescence-labeled PlaF was titrated with an equimolar concentration of non-labeled PlaF to quantify spontaneous dimerization. The results revealed a sigmoidal binding curve from which a dissociation constant KD=637.9±109.4 nM was calculated, indicating weak binding (Figure 5c). Measurements of the esterase activity of PlaF samples used for MST experiments revealed that the specific activity of PlaF strongly decreased with increasing PlaF concentrations (Figure 5c). Enzyme activity measurements were employed to calculate the activation constant Kact=916.9±72.4 nM. The similar dissociation and activation constants support a model in which PlaF activity is regulated through reversible dimerization in vitro.

### FAs induce dimerization and inhibit PlaF

To investigate the effect of FA ligands on the activity of PlaF, we used mM concentrations of FAs with different chain lengths (C5–C15) in a competitive inhibition assay. PlaF was strongly inhibited (>80%) with FAs containing 10–14 carbon atoms (Figure 6a), while the shorter and longer FAs showed only moderate to weak inhibition (Figure 6a). To explore the underlining mechanism, we performed kinetic inhibition studies with increasing concentrations of decanoic acid (C10). The results showed that C10 FA lowered maximal hydrolysis rates (vmax) as expected for a competitive inhibitor. Yet, elevated binding constants (Km) in the presence of higher concentrations of C10 FA indicate that PlaF undergoes allosteric changes affecting the binding of FAs (Figure 6b, Supplementary file 9). We examined whether inhibitory FAs affect dimerization by cross-linking of PlaF in the presence of C10, C11, and C12 FAs. The results of SDS-PAGE revealed a significantly higher amount of dimeric PlaF in FA-treated than in untreated samples (Figure 6c). These results suggest a potential regulatory role of FAs on PlaF activity via FA-induced dimerization, which agrees with the previously demonstrated lower activity of the PlaF dimer compared to the monomer (Figure 5).

![Figure 6.](https://cdn.elifesciences.org/articles/72824/elife-72824-fig6-v2.jpg)

**Figure 6.:** (a) Inhibition of PlaF with FAs. Esterase activity of PlaF was measured in the presence of 7.5 mM FA (C5–C15); an untreated PlaF sample was set as 100%. The results are mean ± S.D. of three experiments with three samples each. (b) Kinetic studies with FA C10 show evidence of mixed-inhibition. Double-reciprocal plots of initial reaction velocities measured with the p-NPB substrate and FA C10 inhibitor at concentrations in a range of 0–7.5 mM. (c) The effect of FAs on PlaF dimerization. PlaF samples incubated with FAs (C10–C12), dimethyl sulfoxide (DM, DMSO used to dissolve FAs), and purification buffer (B, dilution control) were cross-linked with dimethyl pimelimidate (DMP). FA, fatty acid.

### The tilt of monomeric PlaF in a lipid bilayer permits direct GPL access to the active site

To better understand the molecular mechanism of PlaF activation through monomerization, we performed a set of 10 independent, unbiased 2 μs long MD simulations starting from dimeric or monomeric PlaF embedded in an explicit membrane with a GPL composition similar to the native P. aeruginosa membrane (Figure 7a). The simulations revealed only minor intramolecular structural changes in monomeric and dimeric PlaF compared to the initial structure (RMSDall atom <4.0 Å) (Figure 7—figure supplement 1, Supplementary file 10). Spontaneous monomerization was not observed during the MD simulations (Figure 7—figure supplement 1), in line with the sub-nanomolar dissociation constant and the simulation timescale. However, in 8 and 6 out of 10 simulations started, respectively, from PlaFA or PlaFB, a tilting of the monomer for ~25° toward the membrane was observed (Figure 7b, left and Figure 7—figure supplement 1). This tilting motion cooperatively with rotation of PlaF (Video 1) results in the active site cleft of the catalytic domain being oriented perpendicularly to the membrane surface, such that GPL substrates can have direct access to the active site through the opening at the dimer interface (Figure 7a, right). In dimeric PlaF, this opening is, according to the model suggested from the X-ray structure, at >5 Å above the membrane surface (Figure 7a) so that the diffusion of a GPL from the membrane bilayer to the cleft entrance in this configuration is thermodynamically unfavorable. In all MD simulations started from the tilted PlaF monomer, the protein remains tilted (Figure 7b, right and Figure 7—figure supplement 1), which corroborates the notion that the tilted orientation is preferred over the respective configuration in di-PlaF.

![Figure 7.](https://cdn.elifesciences.org/articles/72824/elife-72824-fig7-v2.jpg)

**Figure 7.:** (a) Structures used for MD simulations. di-PlaF: Crystal structure oriented in the membrane by the PPM method. PlaFA: Chain A from PlaF dimer oriented as in the dimer. The entrance of the active site cleft is more than 5 Å above the membrane bilayer surface. t-PlaFA: Extracted monomer A oriented using the PPM method. Cocrystallized MYR, 11A, and OG (depicted in pink), although not included in the simulations, are shown in the figures to highlight the orientation of the active site cleft. Arrows between the structures reflect the predicted states of equilibria under physiological conditions in Pseudomonas aeruginosa. Percentages of the different states are obtained from the molecular simulations (see main text and (e)). (b) MD simulations of monomeric PlaF. Time course of the orientation of monomeric PlaF with respect to the membrane starting from the PlaFA configuration as observed in the structure (left). In 80% of the trajectories, the monomer ends in a tilted configuration (marked with *). When starting from t-PlaFA (right), in all cases, the structure remains tilted. This shows a significant tendency of the monomer to tilt (McNemar’s Χ2=6.125, p=0.013). (c) Potential of mean force (PMF) of monomer tilting. The distance between the COM of Cα atoms of residues 33–37 (yellow, and gray spheres) and the COM of the C18 of the oleic acid moieties of all lipids in the membrane (continuous horizontal line in the membrane slab) was used as a reaction coordinate. The shaded area shows the standard error of the mean obtained by dividing the data into four independent parts of 50 ns each. The yellow shaded regions are the integration limits used to calculate Ktilting (Equation 5). The spheres in the PMF relate to monomer configurations shown in the inset. (d) PMF of dimer separation. The distance between the COM of Cα atoms of residues 25–38 of each chain was used as the reaction coordinate. The shaded area shows the standard error of the mean obtained by dividing the data into four independent parts of 50 ns each. Insets show representative structures at intermediate reaction coordinate values. (e) Percentage of PlaF monomer as a function of total PlaF concentration in the membrane according to the equilibria shown in (c) and (d). The monomer percentage was computed according to Equations 7–11 (see Materials and methods and SI for details). The red line shows the experimentally determined PlaF concentration under overexpressing conditions in P. aeruginosa p-plaF, while the blue-dashed region shows an estimated span for the PlaF concentration in P. aeruginosa wild-type (see Materials and methods for details). Calculated percentages are shown in (a).

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/72824/elife-72824-fig7-figsupp1-v2.jpg)

**Figure 7—figure supplement 1.:** (a) Root mean square deviations during 10 independent, unbiased molecular dynamics (MD) simulations of (I) the di-PlaF, where each chain was measured independently (green, left and right), (II) monomeric PlaF started in the PlaFA configuration (beige), and (III) monomeric PlaF started in the tilted configuration (t-PlaFA, gray), computed with respect to the respective initial structure. Most simulations reached a plateau at ~4 Å. (b) di-PlaF monomer distance during MD simulations. In 10 independent replicas of 2 µs, the dimer does not show a tendency to separate on the time scale of the MD simulations according to the distance between the COM of Cα atoms of residues 25–38 of each monomer. (c) Time course of the orientation of monomeric PlaF starting from the PlaFB (left) and t-PlaFB (right) configurations. Six out of 10 PlaFB replicas show tilting of the monomer in less than 2 μs, while all 10 replicas that started in the t-PlaFB configuration stayed tilted, similar to simulations started from PlaFA and t-PlaFA. (d) Convergence of the PMFs for dimer separation (left) and monomer tilting (right). The plots show PMFs computed every 25 ns of umbrella simulations for each window; the first 100 ns of umbrella simulations were considered equilibration phase and removed. (e) Electron density profiles of membrane components averaged over 10 independent, unbiased MD simulations of di-PlaF, PlaFA, or t-PlaFA configurations for the phospholipid head groups (PE and PG) and oleic acid tails (OL). The obtained shapes correspond with those generally found by experiment and MD simulations for biomembranes (Dickson et al., 2014; Tristram-Nagle et al., 1998; Liu and Nagle, 2004). (f) SCD order parameter of the lipid phase averaged over 10 independent, unbiased MD simulations of di-PlaF, PlaFA, or t-PlaFA configurations. The carbon atoms are numbered according to their position in the phospholipid tail. A clear dip is seen at the unsaturated position of the oleic acid tail, and the overall shape resembles a structured membrane bilayer, as previously described (Dickson et al., 2014; Vemparala et al., 2011). (g) Distribution of reaction coordinate values obtained by umbrella sampling of dimer separation (top) and monomer tilting (bottom). The dashed lines represent the restrained distance used for each window. In both cases, a force constant of 4 kcal mol–1 Å–2 was used, obtaining distributions with a median overlap of 8.2% and 8.6%, respectively. For details, see the main text. (h) Distance to membrane center versus tilting angle. The scatter plot shows the distance of the COM of residues 33–37 to the membrane center versus the tilting angle during the first microsecond of MD simulations of the tenth replica, starting from the PlaFA configuration (R2=0.997, p<0.001). The red dots represent the structures used as starting conformations for calculating the PMF of the tilting process.

![Figure 7—figure supplement 2.](https://cdn.elifesciences.org/articles/72824/elife-72824-fig7-figsupp2-v2.jpg)

**Figure 7—figure supplement 2.:** (a) Western blot was performed using anti-PlaF antiserum; Pseudomonas aeruginosa cells were from logarithmic (OD580nm 1) and stationary phase (OD580nm 3). Cell count was determined by counting colonies formed on LB agar plates. Purified PlaF was used as a positive control. Dimensions of P. aeruginosa cells in the exponential phase are 3.14×0.75 µm2 (Deforet et al., 2015), which yields the surface area of 3.12×106 nm2. (b) qRT-PCR analysis of transcription of rpoD, rpoS, and plaF genes in P. aeruginosa PA01 overnight culture. LB, lysogeny broth; qRT-PCR, quantitative real-time-PCR.

![Video 1.](https://cdn.elifesciences.org/articles/72824/elife-72824-video1.mp4.jpg)

**Video 1.:** Blue and red spheres indicate head groups of GPLs in two leaflets of the bilayer.

To further explore the transition of the monomeric PlaFA to its tilted orientation (t-PlaFA), we calculated the free energy profile or potential of mean force (PMF) for the tilting process by using umbrella sampling and post-processing the distributions with the WHAM method (Suzuki, 1975; Grossfield, 2016). As reaction coordinate, the distance (d) of the top of the JM domain (residues 33–37) to the membrane center was chosen. Distances of ~37 and ~17 Å were calculated for non-tilted PlaFA using the crystal structure and t-PlaFA using the structure obtained from the unbiased MD simulations where tilting spontaneously occurred, respectively. The converged and precise (Figure 7—figure supplement 1; SEM<0.4 kcal mol–1) PMF revealed two minima at d=19.6 and 30.6 Å, with t-PlaFA favored over PlaFA by 0.66 kcal mol–1 (Figure 7c). The free energy barrier of ~1.2 kcal mol–1 explains the rapid transition from PlaFA to t-PlaFA observed in the unbiased MD simulations. The equilibrium constant and free energy of PlaF tilting are Ktilting=3.35 and a ΔGtilting=–0.8±0.2 kcal mol–1. These results suggest a model in which PlaF is activated after monomerization by tilting with respect to the membrane surface, which allows substrate access to its catalytic site.

### Estimating the ratio of monomeric and dimeric PlaF in the cell

To investigate if dimerization-mediated PlaF inhibition is dependent on PlaF concentration in the GPL bilayer, we calculated the free energy profile of dimerization, similarly as for the tilting process. For this, the distance (r) between Cα atoms of the JM region of the two chains was used as a reaction coordinate. The converged (Figure 7—figure supplement 1) and precise (SEM<1.4 kcal mol–1) PMF revealed that di-PlaF is strongly favored at r=9.5 Å (–11.4 kcal mol–1) over the monomer (Figure 7d), fitting with the distance of 9.9 Å observed in the crystal structure of PlaF. From the PMF, the equilibrium constants (Ka=1.57×107 Å2; KX=2.58×105) and free energy (ΔG=–7.5±0.7 kcal mol–1) of PlaF dimerization were computed (Equations 1–3), taking into consideration that KX and ΔG relate to a state of one PlaF dimer in a membrane of 764 lipids, according to our simulation setup. Experimentally, a concentration of one PlaF dimer per ~3786 lipids in P. aeruginosa plaF-overexpressing cells (Bleffert et al., 2019) was determined. However, the concentration in P. aeruginosa WT is likely 100- to 1000-fold lower, as we could not detect PlaF by Western blot (Figure 7—figure supplement 2). Under such physiological conditions and considering that the equilibria for dimer-to-monomer transition and titling are coupled (Figure 7a), between 74% and 96% of the PlaF molecules are predicted to be in a monomeric, tilted, catalytically active state in P. aeruginosa (Figure 7e). Our quantitative real-time-PCR results revealed that plaF is constitutively expressed in P. aeruginosa WT at a much lower level than sigma factors rpoD and rpoS (Savli et al., 2003; Figure 7—figure supplement 2). This agrees with previous global proteomic and transcriptomic results (Erdmann et al., 2018). As a catalytically active form of PlaF is favored in the WT, PlaF is likely involved in the constant remodeling of membrane GPLs.

## Discussion

### PlaF catalyzed remodeling of membrane GPLs

Employing lipidomic profiling of P. aeruginosa WT and the plaF gene deletion mutant, we found substantial changes in membrane GPL composition consistent with in vitro PLA1 activity of PlaF and its integral cytoplasmic membrane-localization. The present understanding of bacterial PLAs is limited to extracellular (ExoU, YplA, and SlaA; Istivan and Coloe, 2006; Sawa et al., 2016) and outer membrane (PlaB and OMPLA; Snijder et al., 1999; Schunder et al., 2010) enzymes with a proposed role in host-pathogen interactions, but, so far, bacterial PLA proteins tethered to the cytoplasmic membrane were not described (Jeucken et al., 2019).

Although bacterial enzymes catalyzing de novo GPL synthesis, their physiological functions and biochemical mechanisms are becoming increasingly well understood (Jeucken et al., 2019), information about GPL turnover enzymes remains largely obscure. Several of our findings indicate that PlaF plays a hitherto unexplored role in the membrane remodeling (Figure 8) that becomes especially apparent during virulence adaptation.

![Figure 8.](https://cdn.elifesciences.org/articles/72824/elife-72824-fig8-v2.jpg)

**Figure 8.:** PlaF is anchored with the TM helix to the inner membrane of Pseudomonas aeruginosa (Figures 1c and 4c), where it forms an inactive dimer (Figure 5c). Monomerization (Figure 5c) and subsequent spontaneous tilting (Figure 7) lead to activation. Binding of dodecanoic acid (C12) to monomeric PlaF triggers dimerization (Figure 6c) and inhibits enzymatic activity (Figure 6a). Tilting constrains the active site cavity of PlaF to the membrane surface such that GPL substrates can enter (GPL1, Figure 2), which are hydrolyzed to FA and lysoGPL1. A yet unknown acyl transferase possibly acylates lyso-GPL1 to yield modified GPL2 (Figure 2). GPL, glycerophospholipid.

It is well known that the global diversity of GPL acyl chains in eukaryotes derives from de novo synthesis (Kennedy pathway) and remodeling (Lands cycle) pathways, which are differentially regulated (Jacquemyn et al., 2017). In the Lands cycle, GPLs are targeted by PLA and acyltransferases that respectively remove and replace acyl chains in GPLs by a recently described mechanism (Zhang et al., 2021; Mouchlis et al., 2015). We suggest that PlaF is the PLA that alters P. aeruginosa membranes by hydrolysis of the main classes of GPLs, namely PE, PG, and PC. Although the observed changes may be caused by the absence of PlaF in the membrane of P. aeruginosa, it is more likely that PlaF directly hydrolyses GPLs as only low concentrations of PlaF were detected in the cell (Figure 7—figure supplement 2). The exact molecular function of PlaF in GPL-remodeling and the regulation of virulence of P. aeruginosa remains unknown. One possibility is that PlaF tunes the concentration of low-abundance GPL species in the membrane, creating a suitable membrane environment for the stabilization of membrane proteins or protein complexes (Corradi et al., 2019). In addition, PlaF-generated GPLs might have a more sophisticated function for membrane-embedded virulence-related proteins. This was demonstrated for ABHD6, a human membrane-bound PLA, which controls the membrane concentration of lipid transmitter 2-arachidonoylglycerol involved in regulating the endocannabinoid receptor (Marrs et al., 2010). Notably, human ABHD6 and PlaF share ~50% sequence similarity and hydrolize similar substrates (Bleffert et al., 2019).

Although PlaF is an important enzyme involved in GPL metabolism, future research should reveal (i) which acyltransferase is involved in the acylation of lysoGPLs produced by PlaF, (ii) if PlaF has acyltransferase activity as described for cPLA2γ involved in the Lands cycle in humans (Asai et al., 2003), and (iii) if periplasmic lysophospholipase TesA (Kovačić et al., 2013) and the recently discovered intracellular PLA PlaB (Weiler et al., 2022) are involved in the Lands cycle.

### Structural insights into dimerization and ligand-mediated regulation of PlaF activity

The high-resolution structure of PlaF with the natural ligands (FAs) bound to its active site represents the first dimeric structure of a full-length, single-pass TM protein (Figure 4). It contributes to our understanding of the role of TM-JM domain-mediated dimerization for the biological activity of single-pass TM proteins, which is undisputed in bacteria and eukaryotes, yet, poorly understood at the atomic level due to the lack of full-length dimeric structures (Bocharov et al., 2017; Fink et al., 2012). The present structure-function relationship of single-pass TM dimers derives from structural data of isolated TM helices without their soluble domains. Therefore, their biological relevance remains questionable (Bocharov et al., 2017).

The crystal structure of PlaF reveals unprecedented details of interactions between the membrane-spanning TM-JM domains and underlines the role of PlaF for degradation of membrane GPLs. The TM and JM domains are not distinct but fold into a long kinked α-helix (Figure 4a). This is different from the structure of a human epidermal growth factor receptor (EGFR), the only structure of an isolated TM-JM domain, in which TM and JM helices are connected by an unstructured loop (Bragin et al., 2016; Endres et al., 2013). The mechanism undergoing PlaF dimerization likely differs from the EGFR family, although it is not excluded that the truncation of soluble domains might destabilize the TM-JM dimer of EGFR, leading to structural changes. We identified intramolecular interactions of 13 residues from the catalytic domain of PlaF with the JM domain, which clearly demonstrates the stabilizing role of the soluble domain on the TM-JM helix. Sole interactions of TM-JM helices result in the formation of a coiled-coil structure (Figure 4b) that stabilizes the PlaF dimer by burying the surface of 656 Å2, which is slightly larger than the interface of the glycophorin TM helix dimer (400 Å2) without the JM region (MacKenzie et al., 1997). The biological relevance of PlaF dimerization is corroborated by crosslinking experiments with P. aeruginosa cells, which revealed the in vivo occurrence of PlaF dimer (Figure 5a). Furthermore, enzyme activity measurements and MST analysis of protein-protein interactions revealed that the activity decreases and dimerization increases as a function of increasing PlaF concentration in vitro (Figure 5c). These findings open the question of regulation of dimerization-mediated PlaF inhibition in vivo and the role of membrane GPLs and their hydrolytic products in this process. Homodimerization mediated via TM-JM interactions was previously shown to be required for activation of single-span TM proteins from receptor tyrosine kinase (Li and Hristova, 2010) and ToxR-like transcriptional regulator (Buchner et al., 2015). However, structural and mechanistic details remained unknown.

A metabolic role of PlaF related to the liberation of FAs and lysoGPLs from membrane GPL substrates addresses the question of regulating PlaF function by substrates or products. A dimer interface with mainly hydrophobic interactions and a few H-bonds detected in the JM region (Figure 4b) seems to be designed to interact with amphipathic GPLs. However, it remains to be elucidated if PlaF-GPL interactions regulate PlaF dimerization and its activity as shown for interactions of SecYEG with cardiolipin and bacteriorhodopsin with sulfated tetraglycosyldiphytanylglycerol (Corradi et al., 2019; Essen et al., 1998).

C10–C14 FAs exert competitive inhibition as in vitro effectors of PlaF (Figure 6a) and enhance dimerization (Figure 6c) in the concentration range (0.5–7.5 mM) similar to the intracellular concentration of FAs in E. coli (~2–4 mM) (Lennen et al., 2013). The dimerization-triggering function of FAs is strengthened by observing a mixed-type inhibition (Figure 6b), which indicates that FAs affect PlaF not only by binding to the active site but also by modulating the oligomerization equilibrium (Gabizon and Friedler, 2014). Interestingly, we identified FA ligands in the PlaF structure bound to the PlaF active site cleft (Figure 4) that were copurified with PlaF from P. aeruginosa (Figure 4—figure supplement 1). Furthermore, we identified an OG molecule, used for purification, in the active site of PlaF. The pseudo-ligand (OG) and natural products (FAs) form an intricate interaction network connecting the catalytic (S137) with the dimerization site (S29, T32, and V33) in the JM domain (Figure 4e). Although the static structure of dimeric PlaF cannot explain how FAs trigger dimerization, we speculate that in vivo, the position of the OG molecule is occupied by FAs, which facilitates the interaction between the two JM-helices, stabilizing the dimer.

### Atomistic model of PlaF catalyzed hydrolysis of membrane GPLs

The question remains of how does the PlaF dimer-to-monomer transition activate PlaF in the GPL bilayer? The active sites in the crystal structure of di-PlaF already adopt catalytically active conformations (Figure 4a), suggesting that the activation of PlaF most likely does not involve structural rearrangements of the active site. To unravel a possible effect of the structural dynamics of PlaF in the membrane on enzyme regulation by dimerization, we performed extensive MD simulations and configurational free energy computations on dimeric and monomeric PlaF embedded into a GPL bilayer mimicking the bacterial cytoplasmic membrane. While structural changes within di-PlaF and monomeric PlaF were moderate (Supplementary file 10), monomeric PlaF spontaneously tilted as a whole toward the membrane, constraining the enzyme protein in a configuration with the opening of the active site cleft immersed into the GPL bilayer (Figure 7a and b). A configuration similar to t-PlaF was observed for monomeric Saccharomyces cerevisiae lanosterol 14α-demethylase, a single TM spanning protein acting on a membrane-bound substrate (Monk et al., 2014). In t-PlaF, GPL can access the active site cleft directly from the membrane with the sn-1 acyl chain entering the first (Wittgens et al., 2017). This is unlikely in di-PlaF, in which the opening of the active site cleft is >5 Å above the membrane (Figure 7e). There, a GPL would need to leave the bilayer into the water before entering the active site cleft, which is thermodynamically unfavorable.

Based on the experimental evidence, we propose a hitherto undescribed mechanism by which the transition of PlaF between a dimeric, not-tilted to a monomeric, tilted configuration is intimately linked to the modulation of the PlaF activity. This mechanism, to the best of our knowledge, expands the general understanding of mechanisms of inactivation of integral single-pass TM proteins and differs from suggested allosteric mechanisms implying structural rearrangements (even folding), mostly in the JM domain, upon ligand binding as underlying causes for functional regulation (Bocharov et al., 2017). Rather, for PlaF, monomerization followed by a global reorientation of the single-pass TM protein in the membrane is the central, function-determining element.

Based on computed free energies of association (Figure 7d) and tilting (Figure 7c), and taking into account the concentration range of PlaF in P. aeruginosa, PlaF preferentially exists as t-PlaF in the cytoplasmic membrane (Figure 7e). Increasing the PlaF concentration in the membrane will thus shift the equilibrium toward di-PlaF. This result can explain the observations that PlaF, an enzyme with membrane-disruptive activity, is found in only very low amounts (Figure 7—figure supplement 2) in WT P. aeruginosa cells and that overproduction of PlaF in P. aeruginosa is not harmful to the cells.

### Implications for drug development

Based on our observation that P. aeruginosa ΔpalF shows strongly attenuated virulence, we suggest that interfering with PlaF function might be a promising target for developing new antibiotics against P. aeruginosa. This class of antibiotics should be potent assuming that GPL remodeling plays a global role in the virulence adaptation in bacteria through simultaneous regulation of virulence-related processes (Benamara et al., 2014; Le Sénéchal et al., 2019; El Khoury et al., 2017; Blanka et al., 2015). Analogously, eukaryotic PLAs regulating inflammatory pathways through the release of arachidonic acid were recently suggested as potential targets of anti-inflammatory drugs (Mouchlis and Dennis, 2016). Our structural and mechanistic studies provide a basis for targeting PlaF by competitive inhibition and interfering with dimerization (Gabizon and Friedler, 2014; Hopkins and Groom, 2002).

## Materials and methods

### Cloning, protein expression, and purification

Molecular biology methods, DNA purification, and analysis by electrophoresis were performed as described previously (Kovacic et al., 2016). For the expression of PlaF, P. aeruginosa PAO1 (WT) cells transformed (Choi et al., 2006) with plasmid pBBR-pa2949 (Kovacic et al., 2016), here abbreviated as p-plaF, were grown overnight at 37°C in lysogeny broth (LB) medium supplemented with tetracycline (100 µg/ml) (Bleffert et al., 2019). The total membrane fraction of P. aeruginosa p-plaF was obtained by ultracentrifugation, membranes were solubilized with Triton X-100, and PlaF was purified using Ni-NTA IMAC and buffers supplemented with 30 mM OG (Bleffert et al., 2019). For biochemical analysis, PlaF was transferred to Tris-HCl (100 mM, pH 8) supplemented with 30 mM OG (Table 2).

**Table 2.**
 Material used in this work.


<table>
  <thead>
    <tr>
      <th>Material</th>
      <th>Ordering details</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Galleria mellonella larvae</td>
      <td>Fauna Topics GmbH, order number: 527</td>
    </tr>
    <tr>
      <td>Trypsin, porcine, MS grade</td>
      <td>Merck, order number: 650279</td>
    </tr>
    <tr>
      <td>Anti-SecG antiserum</td>
      <td>gift of R. Voulhoux, CNRS AMU LCB, Marseille</td>
    </tr>
    <tr>
      <td>Anti-lipid A antibodies</td>
      <td>Acris Antibodies, Herford, Germany, order number: BP 2235</td>
    </tr>
    <tr>
      <td>Ni-NTA agarose</td>
      <td>Macherey–Nagel, Düren, Germany, order number: 745400</td>
    </tr>
    <tr>
      <td>n-Octyl-β-D-glucoside</td>
      <td>Merck, order number: 850511P</td>
    </tr>
    <tr>
      <td>para-Nitrophenyl butyrate</td>
      <td>Sigma-Aldrich, order number: N9876</td>
    </tr>
    <tr>
      <td>Glycerophospholipids</td>
      <td>Avanti Polar Lipids, Alabaster, USA</td>
    </tr>
    <tr>
      <td>NEFA-HR(2) kit</td>
      <td>Wako Chemicals, Richmond, USA, order number: 999-34691</td>
    </tr>
    <tr>
      <td>[N-((6-(2,4-DNP)amino)hexanoyl)-1-(BODIPYFL C5)-2-hexyl-sn-glycero-3-phosphoethanolamine]</td>
      <td>Thermo Fisher Scientific Inc, Waltham, MA, order number: A10070</td>
    </tr>
    <tr>
      <td>1-O-(6-BODIPY558/568-aminohexyl)-2-BODIPYFL C5-Sn-glycero-3-phosphocholine</td>
      <td>Thermo Fisher Scientific Inc, Waltham, MA, order number: A10072</td>
    </tr>
    <tr>
      <td>N-((6-(2,4-dinitrophenyl)amino)hexanoyl)-2-(4,4-difluoro-5,7-dimethyl-4-bora-3a,4a-diaza-s-indacene-3-pentanoyl)–1-hexadecanoyl-sn-glycero-3-phosphoethanolamine triethylammonium salt</td>
      <td>Thermo Fisher Scientific Inc, Waltham, MA, order number: D23739</td>
    </tr>
    <tr>
      <td>Thermomyces lanuginosus PLA1</td>
      <td>Sigma-Aldrich, order number: L3295</td>
    </tr>
    <tr>
      <td>Naja mocambique mocambique PLA2</td>
      <td>Sigma-Aldrich, order number: P7778</td>
    </tr>
    <tr>
      <td>Dimethyl pimelimidate</td>
      <td>Merck, order number: 80490</td>
    </tr>
    <tr>
      <td>Bis(sulfosuccinimidyl) glutarate</td>
      <td>Thermo Fisher Scientific, order number: 21610</td>
    </tr>
    <tr>
      <td>Bis(sulfosuccinimidyl) suberate</td>
      <td>Thermo Fisher Scientific, order number: 21586</td>
    </tr>
    <tr>
      <td>PD-10 columns</td>
      <td>Merck, order number: GE17-0851-01</td>
    </tr>
    <tr>
      <td>NHS Labeling Kit</td>
      <td>NanoTemper, Munich, Germany, order number: MO-L011</td>
    </tr>
    <tr>
      <td>4-Methylumbelliferyl palmitate</td>
      <td>Sigma-Aldrich; order number: M7259</td>
    </tr>
    <tr>
      <td>CytoTox 96 non-radioactive cytotoxicity assay</td>
      <td>Promega, order number: G1780</td>
    </tr>
    <tr>
      <td>NucleoSpin RNA Preparation Kit</td>
      <td>Macherey–Nagel, Düren, Germany, order number: 740955</td>
    </tr>
    <tr>
      <td>RNase-Free DNase Kit</td>
      <td>Qiagen, Hilden, Germany, order number: 79254</td>
    </tr>
    <tr>
      <td>Ambion DNA-Free DNase Kit</td>
      <td>Thermo Fisher Scientific, Darmstadt, Germany, order number: AM1906</td>
    </tr>
    <tr>
      <td>Maxima First Strand cDNA Synthesis Kit</td>
      <td>Thermo Fisher Scientific, Darmstadt, Germany, Order number: K1641</td>
    </tr>
    <tr>
      <td>SYBR Green/ROX qPCR Master Mix</td>
      <td>Thermo Fisher Scientific, Darmstadt, Germany, order number: K0221</td>
    </tr>
    <tr>
      <td>N-Methyl-N-(trimethylsilyl) trifluoroacetamide</td>
      <td>Sigma-Aldrich; order number: 69479</td>
    </tr>
  </tbody>
</table>

### SDS-PAGE, zymography, and immunodetection

The protein analysis by electrophoresis under denaturation conditions (Laemmli, 1970), in-gel esterase activity (zymography), and immunodetection by Western blotting were performed as described previously (Kovacic et al., 2016). The protein concentration was determined by UV spectrometry using a theoretical extinction coefficient of PlaF containing a C-terminal His6-tag of 22,920 M–1 cm–1 (Bleffert et al., 2019).

### Enzyme activity assays, inhibition, and enzyme kinetic studies

Esterase activity assays with p-nitrophenyl FA esters as substrates were performed in 96-well microtiter plates as described previously (Kovacic et al., 2016). Phospholipid substrates purchased from Avanti Polar Lipids (Table 2) were prepared for PLA activity assays (25 µl enzyme+25 µl substrate) performed as described previously (Jaeger and Kovacic, 2014). The amount of FAs released by the PLA activity of PlaF was determined using the NEFA-HR(2) Kit (Wako Chemicals, Richmond, USA) (Bleffert et al., 2019). PLA1 and PLA2 activities of PlaF were measured using fluorescent substrates purchased from Thermo Fisher Scientific Inc (Table 2): PLA1-PE, [N-((6-(2,4-DNP)amino)hexanoyl)-1-(BODIPYFL C5)-2-hexyl-sn-glycero-3-phosphoethanolamine]; PLA2-PC, 1-O-(6-BODIPY558/568-aminohexyl)-2-BODIPYFL C5-Sn-glycero-3-phosphocholine; and PLA2-PE, N-((6-(2,4-dinitrophenyl)amino)hexanoyl)-2-(4,4-difluoro-5,7-dimethyl-4-bora-3a,4a-diaza-s-indacene-3-pentanoyl)-1-hexadecanoyl-sn-glycero-3-phosphoethanolamine triethylammonium as described by da Mata Madeira et al., 2016. Measurements were performed using a plate reader in 96-well plates at 25°C by combining 50 µl of the substrate with 50 µl PlaF (0.7 µg/ml), or control enzymes, the PLA1 of Thermomyces lanuginosus (5 U/ml) and the PLA2 or Naja mocambique mocambique (0.7 U/ml).

### Inhibition

The inhibition of PlaF by FAs was assayed by combining FA dissolved in DMSO (20-fold stock solution) with para-nitrophenyl butyrate (p-NPB)substrate solution followed by the addition of the PlaF sample (8 nmol) and spectrophotometric enzyme activity measurement using p-NPB substrate (Tian and Tsou, 1982). In control experiments, all compounds except FA were combined to assess PlaF activity in the absence of FA. Inhibition constants were calculated by fitting enzyme kinetic parameters obtained by varying FA concentration (0, 0.5, 1.5, 2.5, 5, and 7.5 mM) for different substrate concentrations (0.05, 0.1, 0.2, 0.3, 0.5, and 1 mM) (Kenakin, 2012).

### Subcellular localization

Membranes from P. aeruginosa WT and p-plaF (PlaF overproduction strain) were isolated as described previously (Kovacic et al., 2016). To separate integral from peripheral membrane proteins, total cell membranes were incubated for 30 min at room temperature with: 10 mM Na2CO3 (pH 11), 4 M urea (in 20 mM MES buffer pH 6.5) or 2% (w/v) Triton X-100 (in 20 mM MES buffer pH 6.5). After the incubation, the samples were centrifuged for 30 min at 180,000g to separate membranes from solubilized proteins.

The separation of the inner and outer membrane was performed with a discontinuous sucrose gradient by ultracentrifugation at 180,000g for 72 hr and 4°C (Viarre et al., 2009). The sucrose gradient consisted of 1.5 ml fractions with 35%, 42%, 46%, 50%, 54%, 58%, 62%, and 65% (w/v) sucrose in 100 mM Tris-HCl, pH 7.4. Isolated membranes from P. aeruginosa WT were suspended in buffer containing 35% (w/v) sucrose and loaded on the top of the discontinuous sucrose gradient. Fractions were collected from the bottom (pierced tube), and sucrose concentration was determined with a refractometer (OPTEC, Optimal Technology, Baldock, UK). To determine the orientation of catalytic PlaF domain P. aeruginosa p-plaF cells (10 ml culture with OD580nm 1 grown in LB medium at 37°C) were harvested by centrifugation (4000g, 4°C, 5 min) and suspended in 1 ml Tris-HCl buffer (50 mM, pH 7.5, 10% sucrose (w/v)) followed by shock freezing with liquid nitrogen (Eichler and Wickner, 1998). Cells were thawed to room temperature and centrifuged (4000g, 4°C, 5 min) followed by incubation of the pellet for 1 hr on ice in Tris-HCl buffer (30 mM, pH 8.1, sucrose 20% (w/v) EDTA 10 mM). Trypsin (20 µl, 1 mg/ml) was added to the suspension containing the cells with the permeabilized outer membrane and incubated at room temperature for up to 5 hr. The proteolytic reaction was stopped with onefold SDS-PAGE sample buffer and incubation for 10 min at 99°C. Immunodetection of SecG with anti-SecG antiserum (gift of R. Voulhoux, CNRS AMU LCB, Marseille) and lipid A antibodies (BP 2235, Acris Antibodies, Herford, Germany) was performed as described above for PlaF using the respective antisera at 1/2000 and 1/1000 dilutions.

### Cross-linking assays

In vitro cross-linking using the bifunctional cross-linking reagents DMP was performed as previously described (de Jong et al., 2017) with the following modifications. PlaF (10 µl, 15.5 µM) purified with OG was incubated with 6 µl freshly prepared DMP (150 mM in 100 mM Tris-HCl, pH 8.4), BS2G (5 mM in 100 mM Tris-HCl, pH 8.0) and BS3 (5 mM in 100 mM Tris-HCl, pH 8.0) for 90 min (Table 2). The cross-linking reaction was terminated with a 5 µl stop solution (50 mM Tris-HCl, 1 M glycine, NaCl 150 mM, pH 8.3). For in vivo cross-linking, P. aeruginosa p-plaF and EV strains were grown in LB medium at 37°C to OD580nm 1. Cells were harvested by centrifugation (10 min, 4000g, 4°C), suspended in 1/20 volume of Tris-HCl (pH 8.3, 100 mM, NaCl 150 mM), and treated with the same volume of freshly prepared cell-permeable cross-linking reagent DMP (0, 20, 30, and 50 mM in Tris-HCl buffer 100 mM, pH 8.4) for 2 h. The cross-linking reaction was terminated with the same volume of stop solution (50 mM Tris-HCl, 1 M glycine, 150 mM NaCl, pH 8.3).

### Analysis of concentration-dependent dimerization

Purified PlaF (20 µl, 50–60 µM) was transferred from the purification buffer into the labeling buffer (Na-PO4 20 mM, pH 8.3) supplemented with OG (30 mM) using PD-10 columns (GE Healthcare, Solingen, Germany) according to the manufacturer’s protocol. Labeling was performed by incubating PlaF with 15 µl dye (440 µM stock solution) for 2.5 hr using the NHS Labeling Kit (Table 2). PlaF was then transferred into a purification buffer using PD-10 columns. Non-labeled PlaF was diluted with the same buffer in 16 steps by combining the same volume of the protein and buffer, yielding samples with concentrations from 26.9 µM to 1.6 nM. Samples containing 100 nM labeled PlaF were incubated for 16 hr at room temperature in the dark, and MST experiments were performed using the Monolith NT.115 device (NanoTemper, Munich, Germany) with the following setup: MST power, 60%; excitation power 20%; excitation type, red; 25°C. Constants were calculated according to the four-parameter logistic, nonlinear regression model using Origin Pro 2018 software.

The enzymatic activity of PlaF samples used for MST analysis was assayed by combing 15 µl of enzyme and 15 µl 4-methylumbelliferyl palmitate (4-MUP, 2 mM) dissolved in purification Tris-HCl (100 mM, pH 8) containing 10% (v/v) propan-2-ol (Table 2). Fluorescence was measured for 10 min (5 s steps) using a plate reader in black 96-well microtiter plates at 30°C.

### Construction of a P. aeruginosa ∆plaF, and ∆plaF::plaF strains

The mutagenesis vector pEMG-ΔplaF (Figure 2—figure supplement 2) was generated with upstream and downstream regions of plaF gene amplified by standard PCR using Phusion DNA polymerase, a genomic DNA of P. aeruginosa PAO1 as a template, and primer pairs 5′-ATATATGAATTCTCTGCTCGGCGCGAAACGCAGCGP-3′/5′-ATATATACGCGTGGGTGTCCGAAGGCTTCAGGAAAAAAGGGGC-3′ and 5′-ATATATACGCGTAAACGCGAACCGGCGCCTGGG-3′/5′-CTGGATGAATTCTGGCCTGGACACCGACAAGGAAGTGATCAAGG-3′, respectively. DNA fragments upstream and downstream of the plaF gene were cloned into the pEMG vector by ligation of DNA fragments hydrolyzed with EcoRI restriction endonuclease. P. aeruginosa PAO1 (WT) cells were transformed with the pEMG-ΔplaF and P. aeruginosa ΔplaF mutant strain was generated by homologous recombination (Martínez-García and de Lorenzo, 2011). Generation of pUC18T-mini-Tn7T-Gm-plaF plasmid (Figure 2—figure supplement 2) for recombination of plaF gene containing 128 bp upstream region of plaF with a chromosome of P. aeruginosa ΔplaF. A DNA fragment containing the upstream region and plaF gene was amplified using primer pair 5′-AATAGAGCTCACCGCCGTCCTTAGGTTC-3′/5′-AATAGAGCTCCGTTTTCAGCGACCGGC-3′ from the genomic DNA of P. aeruginosa PAO1. Both primers contained the restriction site SacI for cloning into the pUC18T-mini-Tn7T-Gm (gifts from Herbert Schweizer, Addgene plasmids #63121, #64968, and #64946). P. aeruginosa ∆plaF was transformed with pUC18T-mini-Tn7T-plaF-Gm and helper plasmid pTNS2 encoding the Tn7 site-specific transposase ABCD by tri-parental conjugation and the positive clones were identified by PCR using primer pair 5′-GCACATCGGCGACGTGCTCTC-3′/5′-CACAGCATAACTGGACTGATTTC-3′. The gentamycin-resistance gene was excised from P. aeruginosa ∆plaF::plaF-Gm by Flp-recombinase produced from pFLP3 plasmid (Choi et al., 2005).

### G. mellonella virulence model

G. mellonella larvae (Table 2) were sorted according to size and split into groups of 10 in Petri dishes. P. aeruginosa WT, the ΔplaF, and the ΔplaF::plaF strains were grown overnight and sub-cultured to mid-log phase in LB media at 37°C. The bacteria were washed twice with PBS and adjusted to OD600 0.055, which equals 5×104 bacteria/µl. This suspension was diluted in PBS to the infection dose of 500 bacteria per 10 µl, which were injected into the hindmost left proleg of the insect. Hereby, PBS injections were used as infection control and untreated larvae as viability control. If more than one larvae was dying within the control group, the experiment was repeated. The survival of larvae incubated at 30°C was monitored (Koch, 2014).

### Cytotoxicity assay

BMDMs were isolated from the bones of C57BL/6 mice and cultured in RPMI supplemented with 20% (v/v) conditioned L929 medium to allow for differentiation into macrophages for at least 7 days. BMDMs were seeded at a concentration of 5×105 cells in a 24-well plate. The BMDMs cells (n=10) were infected with 5×105 bacteria (cultivated overnight in LB medium at 37°C), which accounts for MOI 1 (Mittal et al., 2016). PBS treated cells served as viability control. Supernatants were taken at 0, 1, 3, and 6 hr post-infection. LDH levels were determined (n=6) using the CytoTox 96 Non-Radioactive Cytotoxicity Assay according to the manufacturer’s protocol. As 100% killing control, uninfected cells were lysed with 1% (v/v) Triton-X100. Statistical analysis was performed using a one-way ANOVA to determine significant changes of normally distributed values obtained from two independent experiments with 10 samples each.

### Growth curves

The growth of P. aeruginosa WT and ΔplaF cultures in Erlenmeyer flasks (agitation at 160 rpm) was monitored by measuring OD580nm for 24 hr. OD580nm was converted to colony-forming units by multiplying with the factor 8×108 experimentally determined for P. aeruginosa PAO1 strain from our laboratory.

### Quantitative real-time-PCR

RNA was isolated from P. aeruginosa PA01 and ΔplaF grown overnight (37°C, LB medium) with the NucleoSpin RNA Preparation Kit and genomic DNA was quantitatively removed using RNase-Free DNase Kit and Ambion DNA-Free DNase Kit according to the manufacturer’s recommendations (Table 2). One µg of RNA was transcribed into cDNA using the Maxima First Strand cDNA Synthesis Kit (Table 2). For the quantitative real-time-PCR (qRT-PCR), 50 ng of cDNA was mixed with SYBR Green/ROX qPCR Master Mix (Table 2) to a total volume of 20 μl and qRT-PCR was performed as described previously (Savli et al., 2003). Following primers were used for rpoD (3′-CAGCTCGACAAGGCCAAGAA-5′, CCAGCTTGATCGGCATGAAC), rpoS (3′-CTCCCCGGGCAACTCCAAAAG-5′, 3′-CGATCATCCGCTTCCGACCAG-5′) and plaF (3′-CGACCCTGTTGCTGATCCAC-5′, 3′-ACGTCGTAGCTGGCCTGTTG-5′).

### Lipidomic analysis of GPLs extracted from cell membranes

The cells of P. aeruginosa WT, ∆plaF, and ∆plaF::plaF cultures grown overnight in 15 ml LB medium (Supplementary file 3) at 37°C were harvested by centrifugation at 4000g and 4°C for 15 min and suspended in 2 ml ddH2O followed by boiling for 10 min to inactivate phospholipases. Cells were harvested by centrifugation (4000g, 4°C, 15 min) and total lipids were extracted from the cell pellet (Gasulla et al., 2013). Briefly, after boiling the water was removed by centrifugation (4000g, 4°C, 15 min). Lipids were extracted with CHCl3:CH3OH=1:2 (v/v) and the organic phase was collected. The extraction was repeated with CHCl3:CH3OH=2:1 (v/v) and the organic phases were combined. One volume of CHCl3 and 0.75 volumes of an aqueous solution containing 1 M KCl and 0.2 M H3PO4 were added to the combined chloroform/methanol extracts. Samples were vortexed and centrifuged (2000g, 5 min). The organic phase was withdrawn and the solvent of the lipid extract was evaporated under a stream of N2. Total lipids were dissolved in CHCl3:CH3OH=2:1 (v/v). GPLs were quantified by Q-TOF mass spectrometry (Q-TOF 6530; Agilent Technologies, Böblingen, Germany) as described elsewhere (Gasulla et al., 2013). Statistical analysis of the GPL amount was performed using the T-test and the Shapiro-Wilk method to determine significant changes of normally distributed values obtained from four P. aeruginosa WT lipidome and four ∆plaF samples. Ratio of PlaF and GPLs was calculated knowing GPLs extraction yield of 40 µg GPLs per 1 ml P. aeruginosa p-plaF (OD580nm 1) and PlaF purification yield of ~1 µg from 1 ml P. aeruginosa p-plaF culture with OD580nm 1 (Bleffert et al., 2019).

### GC-MS analysis of FA

FAs were extracted from PlaF purified from 13 g P. aeruginosa p-plaF cells with OG using four parts of organic solvent (CHCl3:CH3OH=2:1). Extraction was repeated three times, the chloroform extracts were combined, chloroform was evaporated, and FAs were dissolved in 200 µl chloroform. The chloroform extract was mixed with 10 volumes of acetonitrile and filtered through a 0.2 µm pore size filter. For GC-MS analysis, FA extracts and standards (C10-, C11-, C14-, C15-, C16-, and C18-FA; C16-, C18-, and C20-primary fatty alcohol) were converted into their trimethylsilyl esters and trimethylsilyl ethers, respectively. 900 µl of the sample or standard solution (CHCl3:acetonitrile=1:5) was mixed with 100 µl N-methyl-N-(trimethylsilyl) trifluoroacetamide and heated to 80°C for 1 hr. The GC-MS system consisted of a Trace GC Ultra gas chromatograph, TriPlus autosampler, and an ITQ 900 mass spectrometer (Thermo Fisher Scientific, Waltham, MA). Analytes were separated on a Zebron-5-HT Inferno column (60 m × 0.25 mm i.d., 0.25 µm film thickness, Phenomenex, USA). Helium was used as carrier gas at a constant gas flow of 1.0 ml/min. The oven temperature program was as follows: 80°C; 5°C/min to 340°C, held for 5 min. The injector temperature was held at 290°C, and all injections (1 µl) were made in the split mode (1:10). The mass spectrometer was used in the electron impact (EI, 70 eV) mode and scanned over the range m/z 25–450 with an acquisition rate of 3 microscans. The transfer line and ion source were both kept at 280°C. Data processing was performed by the use of the software XCalibur 2.0.7 (Thermo Fisher Scientific). FAs from the PlaF sample were identified by comparison of their retention times and mass spectra with FA standards.

Reaction of purified PlaF (620 µl, 300 µg/ml) with 1-(9Z-octadecenoyl)-2-pentadecanoyl-glycero-3-phospho-(1′-rac-glycerol) (PG15:0-18:1, 0.5 mM) in 4 ml NEFA buffer was conducted for 24 hr at 37°C followed by extraction of FAs, derivatization, and GC quantification. FAs were transferred to 15 ml Falcon tubes by dissolving in 500 µL CH2Cl2 twice. After evaporation to dryness the remaining fatty acids were derivatized to their methyl esters according to Funada et al. with modifications (Funada and Hirata, 1999). Briefly the residues were dissolved in 1 ml 1 M sulfuric acid in methanol. For esterification the Falcon tubes were placed in an ultrasonic bath for 30 min. The fatty acid methyl esters (FAMEs) were extracted after addition of 3.3 ml water and 1.7 ml hexane by vigorous shaking on a Vortex for 1 min. The upper organic phase was withdrawn and dried over sodium carbonate. An aliquote was directy used for GC-MS analysis. A 1 mM fatty acid mixture in methanol (C10:0, C12:0, C14:0, C16:0, C18:0, C17:0 cyc (9,10), C18:1 cis-Δ9, C18:1 trans-Δ9, C18:1 trans-Δ11, C18:2 cis,cis-Δ9,12, C18:2 trans,trans-Δ9,12 and C18:3 cis,cis,cis-Δ9,12,15) was diluted to 50, 100, 200 and 400 µM and derivatized in the same manner as above. The Agilent GC-MS system consisted of a gas chromatograph 7890A and an autosampler G4513A coupled to a quadrupole mass spectrometer MS G3172A (Agilent, CA, USA). Analytes were separated on a SGE BPX70 column (30 m x 0.32 mm i.d., 0.25 µm film thickness, Thermo Fisher Scientific, USA). Helium was used as carrier gas at a constant gas flow of 1.5 ml/min. The oven temperature program employed for analysis of FAMEs was as follows: 120°C; 20°C/min to 160°C; 3°C/min to 200°C; 20°C to 220°C, held for 8.7 min. The injector temperature was held at 250°C, and all injections (1 µl) were made in the split mode (1:10). The mass spectrometer was used in the electron impact (EI) mode at an ionizing voltage of 70 eV. Analytes were scanned over the range m/z 50 - 400 with a spectrum recording interval of 4 scans/sec. The GC interface temperature was held at 250°C. The MS source and quadrupole temperatures were kept at 280°C and 150°C, respectively. Data processing was performed by use of the software ChemStation E.02.02.1431 (Agilent, CA, USA). Fatty acids from PlaF samples were identified by comparison of their retention times and mass spectra with those of fatty acid standards and published data (Yang et al., 2013; Benamara et al., 2014; Chao et al., 2010). Quantification of FAMEs C16:0 (1), C17:0 cyc(9,10) (4), C18:0 (5) and C18:1 trans-Δ11 (6) (Figure 1) were performed by external calibration with the corresponding reference compounds. C18:1 cis-Δ11 (7) was quantified by use of the calibration curve of oleic acid (C18:1 cis-Δ9) justified by the almost congruent calibration curves of elaidic acid (C18:1 trans-Δ9) and C18:1 trans-Δ11.

### Crystallization, data collection, structure determination, and analysis

PlaF purified with OG was crystallized as described previously (Bleffert et al., 2019). The X-ray diffraction data were recorded at beamline ID29 of the European Synchrotron Radiation Facility (ESRF, Grenoble, France) and processed as described (Bleffert et al., 2019). The structure was determined by molecular replacement using the automated pipeline ‘MrBUMP’ from the CCP4 package (Keegan et al., 2011). In detail, a combination of PHASER (McCoy et al., 2007), REFMAC (Murshudov et al., 1997), BUCCANEER (Cowtan, 2006), and SHELXE (Hübschle et al., 2011) resulted in an interpretable electron density map to expand the placed model by molecular replacement using the model built with HsaD from Mycobacterium tuberculosis (PDB code: 2VF2) (Lack et al., 2010). Phase improvement was achieved by running several cycles of automated model building (ARP/wARP, CCP4) and refinement using the PHENIX (Adams et al., 2011) package. The model was further corrected by manual rebuilding using the program COOT (Emsley and Cowtan, 2004). Detailed statistics on data collection and refinement are provided in Table 1. None of the residues is in disallowed regions according to Ramachandran plots generated with MolProbity (PHENIX) (Adams et al., 2002). The secondary structure was defined according to Kabsch and Sander (Kabsch and Sander, 1983). Interaction surface area was determined by PISA server (Krissinel and Henrick, 2007). Coordinates and structure factors for PlaF have been deposited in the Protein Data Bank under accession code 6I8W.

### Identification of structural homologs of PlaF

PlaF structural homologs were defined as protein structures from a non-redundant subset of PDB structures with less than 90% sequence identity to each other (PDB90 database, 12.10.2020) with a Z-score higher than 2 according to the DALI server (Holm and Rosenström, 2010). Sequence alignment based on structural superimposition of all 357 homologs of PlaFB (all 340 homologs of PlaFA were among PlaFB homologs) was used to identify proteins with homology in TM-JM helix of PlaF (residues 1–38). To evaluate homology, 39 3D structures with partial conservation of TM-JM helix were superimposed with the PlaF structure using Pymol (http://www.pymol.org) (Figure 4—figure supplement 3).

### Sequence analysis

A protein sequence of PlaF was used for a BLAST search of Pseudomonas Genome Databank (https://www.pseudomonas.com/) to identify PlaF orthologs in 4660 sequenced P. aeruginosa genomes. Pseudomonas Genome Databank BLAST search was extended to all pathogenic Pseudomonas species designated as those with assigned risk group 2 according to the German classification of prokaryotes into risk groups. NCBI BLAST (https://blast.ncbi.nlm.nih.gov/Blast.cgi) was used to identify PlaF homologs in other pathogenic bacteria.

### Molecular dynamics simulations of dimer and monomers

The crystal structure of the PlaF dimer was used as the starting point for building the systems for molecular dynamics (MD) simulations. Five missing C-terminal residues on both chains were added by using MODELLER (Sali and Blundell, 1993), and all small-molecule ligands were removed. The dimer was oriented into the membrane using the PPM server (Lomize et al., 2012). From the so-oriented dimer structure, chain B was deleted to obtain a PlaFA monomer in a dimer-oriented configuration; in the same way, chain A was deleted to keep PlaFB. Additionally, the PlaFA and PlaFB monomers were oriented by themselves using the PPM server, yielding tilted configurations (t-PlaFA and t-PlaFB). These five starting configurations, di-PlaF, PlaFA, PlaFB, t-PlaFA, and t-PlaFB, were embedded into a DOPE:DOPG=3:1 membrane with CHARMM-GUI v1.9 (Jo et al., 2009) resembling the native inner membrane of Gram-negative bacteria (Benamara et al., 2014; Murzyn et al., 2005). A distance of at least 15 Å between the protein or membrane and the solvation box boundaries was considered. KCl at a concentration of 0.15 M was included in the solvation box to obtain a neutral system. The GPU particle mesh Ewald implementation from the AMBER16 molecular simulation suite (Le Grand et al., 2013; Darden et al., 1993) with the ff14SB (Maier et al., 2015) and Lipid17 (Dickson et al., 2014; Skjevik et al., 2016; Case, 2017) parameters for the protein and the membrane lipids, respectively, were used; water molecules were added using the TIP3P model (Jorgensen et al., 1983). For each protein configuration, 10 independent MD simulations of 2 µs length were performed. Covalent bonds to hydrogens were constrained with the SHAKE algorithm (Ryckaert et al., 1977) in all simulations, allowing the use of a time step of 2 fs. Details of the thermalization of the simulation systems are given below. All unbiased simulations showed stable protein structures (Figure 7—figure supplement 1) and membrane phases, evidenced by electron density and order parameter calculations (Figure 7—figure supplement 1). The area per lipid through all simulations calculated for the leaflet opposite to the one where PlaF was embedded was 61.3±0.13 Å2 (mean ± SEM), similar to values reported previously (Murzyn et al., 2005).

### Thermalization and relaxation of simulated systems

Initially, systems were energy-minimized by three mixed steepest descent/conjugate gradient calculations with a maximum of 20,000 steps each. First, the initial positions of the protein and membrane were restrained, followed by a calculation with restraints on the protein atoms only, and finally a minimization without restraints. The temperature was maintained by using a Langevin thermostat (Quigley and Probert, 2004), with a friction coefficient of 1 ps–1. The pressure, when required, was maintained using a semi-isotropic Berendsen barostat (Berendsen et al., 1984), coupling the membrane (x-y) plane. The thermalization was started from the minimized structure, which was heated by gradually increasing the temperature from 10 to 100K for 5 ps under NVT conditions, and from 100 to 300K for 115 ps under NPT conditions at 1 bar. The equilibration process was continued for 5 ns under NPT conditions, after which production runs were started using the same conditions.

### Structural analysis of MD trajectories

All analyses were performed by using CPPTRAJ (Roe and Cheatham, 2013). The distance between the centers of mass (COM) of residues 25–38 Cα atoms of the chains in the dimer structure was evaluated (Figure 7—figure supplement 1); this residue range corresponds to the solvent-accessible half of helix TM-JM (Figures 7a and 8). For the monomer structures, the angle with respect to the membrane normal was assessed. For this, the angle between the membrane normal and the vector between the COM of residues 21–25 and residues 35–38 was calculated (Figure 7b).

### PMF and free energy calculations of dimer dissociation

For calculating a configurational free energy profile (PMF) of the process of dimer dissociation, 36 intermediate states were generated by separating one chain of the dimer along the membrane plane by 1 Å steps, resulting in a minimum and maximum distance between the chain COM of 40.8 and 68 Å, respectively. The generated structures represent the separation process of the PlaF dimer. To sample configurations along the chain separation in a membrane environment, each intermediate state was embedded into a membrane of approximately 157×157 Å2 by using PACKMOL-Memgen (Schott-Verdugo and Gohlke, 2019), and independent MD simulations of 300 ns length each, with a total simulation time of 10.8 µs. Umbrella sampling simulations were performed by restraining the initial distance between chains in every window with a harmonic potential, using a force constant of 4 kcal mol–1 Å–2 (Torrie and Valleau, 1977); the distance between the COM of Cα atoms of residues 25–38 of each monomer was used as a reaction coordinate, being restrained in every simulation. Values for the reaction coordinate, representing the intermonomer distance r, were recorded every 2 ps and post-processed with the Weighted Histogram Analysis Method implementation of A. Grossfield (WHAM 2.0.9) (Suzuki, 1975; Grossfield, 2016), removing the first 100 ns as an equilibration of the system. The kernel densities showed a median overlap of 8.2% between contiguous windows (Figure 7—figure supplement 1), well suited for PMF calculations (Chen and Kuyucak, 2011). The error was estimated by separating the last 200 ns of data in four independent parts of 50 ns each and then calculating the standard error of the mean of the independently determined energy profiles.

The association free energy was estimated from the obtained PMF following the membrane two-body derivation from Johnston et al., 2012 and our previous work (Pagani and Gohlke, 2018). The PMF of dimer association is integrated along the reaction coordinate to calculate an association constant (Ka), which is transformed to the mole fraction scale (Kx) taking into account the number of lipids NL per surface area A, and this value is used to calculate the difference in free energy between dimer and monomers (ΔG), according to Equations 1–3:

$$
K_{a}=\frac{||Ω||}{(2\pi)^{2}}\int_{0}^{D}re^{\frac{−w(r)}{k_{B}T}}dr
$$



$$
K_{x}=K_{a}\frac{N_{L}}{A}
$$



$$
ΔG=−RT ln(K_{x})
$$

where r is the value of the reaction coordinate, w(r) is the PMF at value r, D is the maximum distance at which the protein is still considered a dimer, kB is the Boltzmann constant, and T is the temperature at which the simulations were performed. The factor $\frac{Ω}{(2\pi)^{2}}$ considers the restriction of the configurational space of the monomers upon dimer formation in terms of the sampled angle between the two chains in the dimeric state (Equation 4) and the accessible space for the monomers, (2π)2.

$$
Ω=max⁡\theta_{a}-min⁡\theta_{a}*max⁡\theta_{b}-min⁡\theta_{b}
$$

In Equation 4, the angle θa is defined as the angle formed between the vectors connecting the COM of chain b with the COM of the chain a and with the COM of residues 25–38 of the latter chain; θb is defined analogously starting from the COM of chain a. A value for ||Ω|| of 0.55 computed from Equation 4 indicates the fraction of the accessible space that the PlaF monomers have in the dimeric state compared to when both chains rotate independently [(2π)2].

### PMF and free energy calculations of monomer tilting

The initial conformations used in every window for calculating the PMF of the monomer tilting were obtained from the first microsecond of MD simulations of replica 10 of PlaFA (oriented as in the di-PlaF crystal structure) where spontaneous tilting occurred. The distance d along the z-axis between the COM of Cα atoms of residues 33–37 of the monomer with the membrane center was used to select 22 intermediate tilting configurations. d significantly correlates (R2=0.997, p<0.001) with the angle formed by the second half of helix αJM1 of the monomer (residues 25–38) and the normal vector of the membrane (Figure 7—figure supplement 1). The starting conformations were extracted from the representative trajectory, taking the respective snapshots where d and the angle showed the least absolute deviation to the average value obtained by binning d in windows of 2 Å width and with an evenly distributed separation of 1 Å. The distance d was restrained for every configuration by a harmonic potential with a force constant of 4 kcal mol–1 Å–2, and sampling was performed for 300 ns per window. The data were obtained every 2 ps and analyzed as described above, resulting in 8.6% of median overlap between kernel densities of contiguous windows (Figure 7—figure supplement 1). The error was estimated in the same way as for the dimerization (see above).

For calculating the free energy difference between the obtained basins, the PMF of monomer tilting was integrated using Equations 5 and 6 (Doudou et al., 2009):

$$
K_{tilting}=\frac{\int_{B_{1}}e^{− \frac{w(d)}{k_{B}T}}dr}{\int_{B_{2}}e^{− \frac{w(d)}{k_{B}T}}dr}
$$



$$
ΔG_{tilting}=−RT ln K_{tilting}
$$

where d is defined as above, w(d) is the value of the PMF at that distance, and B1 and B2 represent the basins for the tilted and split configurations, respectively. The integration limits B1 and B2 included each basin portion below half of the value between the basin minimum and the energy barrier separating the basins, respectively (Figure 7c, yellow shaded regions).

### PlaF dimer versus monomer proportion under in vivo conditions

The dimer to monomer equilibrium of PlaF in the membrane results from the coupling of the following equilibria:

$$
2M ⇌K_{a}D        K_{a}=\frac{D}{M^{2}}
$$



$$
M⇌K_{tilting}M_{tilted}     K_{tilting}=\frac{M_{tilted}}{M}
$$

yielding,

$$
D ⇌K_{a} K_{tilting}^{−2}2M_{tilted}
$$

where D, M, and Mtilted represent the PlaF dimer, ‘split’ monomer, and tilted monomer, respectively, with Ka and Ktilting being the dimer association and monomer tilting equilibrium constants, obtained from the PMF calculations. Based on the association constant computed according to Equation 7, Ka=[D]/[M]2=1.57×107 Å2, with [D] and [M] as area concentrations of dimer and monomer, respectively, the proportion of PlaF dimer versus monomer in a live cell of P. aeruginosa can be computed. Experimentally, 40 µg GPLs per 1 ml P. aeruginosa p-plaF (OD580nm 1) were extracted, and a PlaF purification yield of ca. 1 µg from 1 ml P. aeruginosa p-plaF culture with OD580nm was obtained (Bleffert et al., 2019; Supplementary file 3). Considering the molecular weight of PlaF of 35.5 kDa and assuming 750 Da as the average molecular weight of membrane GPL, this relates to a concentration under overexpressing conditions of ~5.28×10–4 PlaF monomers per lipid. Under non-overexpressing conditions, the concentration of PlaF monomers is estimated to be at least 100- to 1000-fold lower, that is, 5.28×10–6 to 5.28 × 10–7 PlaF monomers per lipid. Considering that the area per lipid in a PE:PG=3:1 membrane at 300K is approximately 61 Å2 per leaflet (or 30.5 Å2 in a bilayer, computed in this work and Murzyn et al., 2005), the total area concentration of PlaF molecules then is

$$
T = 2D+ M=1.73 x 10^{-8}, 1.73 x 10^{-7}\frac{PlaF}{Å^{2}}.
$$

Expressing the association constant in terms of the monomer concentration using Equation 7 yields

$$
K_{a}=\frac{\frac{T-M}{2}}{M^{2}}         ⇔        2K_{a}M^{2}+M-T=0,
$$

and solving the quadratic equation then results in

$$
M=\frac{-1+\sqrt{1+8K_{a}T}}{4K_{a}}=1.25\times10^{-8},6.00\times10^{-8}\frac{PlaF}{Å^{2}}
$$

and

$$
D=\frac{T-M}{2}=2.43\times10^{-9},5.66\times10^{-8}\frac{PlaF dimer}{Å^{2}},
$$

These results show that in live cells, the fraction of PlaF in the monomeric (dimeric) state is between 35% and 72% (65% and 28%), where the PlaF monomer is considered to be in the ‘split’ configuration with respect to the membrane normal.

As the tilting of the PlaF monomer is energetically favorable compared to the ‘split’ configuration and, hence, depletes the concentration of ‘split’ PlaF monomers, the dimeric PlaF concentration will decrease (Figure 7a). To quantitatively consider the effect of the tilting, we express the overall equilibrium constant for the processes shown in Figures 7a and 8, and described in Equations 7–9 as

$$
K=K_{a} K_{tilting}^{-2}=\frac{D}{M_{tilted}^{2}},
$$

where

$K_{tilting}=\frac{M_{tilted}}{M}=3.35$, equivalent to $G_{tilting} = -0.72\frac{kcal}{mol},$ computed according to Equation 5.

Following the same procedure as before then yields

$$
M_{tilted}=1.66\times10^{-8},1.28\times10^{-7}\frac{PlaF}{Å^{2}}
$$



$$
D=3.83\times10^{-10},2.28\times10^{-8}\frac{PlaF dimer}{Å^{2}}
$$

showing that in live cells, the fraction of PlaF in the tilted monomeric (dimeric) state is between 74% and 96% (26 and 4%). A graphical representation of the percentage of protein as a tilted monomer with respect to the protein concentration in the membrane is shown in Figure 7e.
