# Drivers and sites of diversity in the DNA adenine methylomes of 93 Mycobacterium tuberculosis complex clinical isolates

## Authors

- Samuel J Modlin<sup>1</sup>
- Derek Conkle-Gutierrez<sup>1</sup>
- Calvin Kim<sup>1</sup>
- Scott N Mitchell<sup>1</sup>
- Christopher Morrissey<sup>1</sup>
- Brian C Weinrick<sup>2</sup>
- William R Jacobs<sup>3</sup> ([ORCID: 0000-0003-3321-3080](https://orcid.org/0000-0003-3321-3080))
- Sarah M Ramirez-Busby<sup>1</sup> ([ORCID: 0000-0001-7455-1903](https://orcid.org/0000-0001-7455-1903))
- Sven E Hoffner<sup>1</sup>
- Faramarz Valafar<sup>1</sup> ([ORCID: 0000-0002-3648-9384](https://orcid.org/0000-0002-3648-9384)) †

### Affiliations

1. Laboratory for Pathogenesis of Clinical Drug Resistance and Persistence, San Diego State University San Diego United States
2. Trudeau Institute Saranac Lake United States
3. Department of Microbiology and Immunology, Albert Einstein College of Medicine Bronx United States
4. Department of Public Health Sciences, Karolinska Institute Stockholm Sweden

† Corresponding author

## Abstract

This study assembles DNA adenine methylomes for 93 Mycobacterium tuberculosis complex (MTBC) isolates from seven lineages paired with fully-annotated, finished, de novo assembled genomes. Integrative analysis yielded four key results. First, methyltransferase allele-methylome mapping corrected methyltransferase variant effects previously obscured by reference-based variant calling. Second, heterogeneity analysis of partially active methyltransferase alleles revealed that intracellular stochastic methylation generates a mosaic of methylomes within isogenic cultures, which we formalize as ‘intercellular mosaic methylation’ (IMM). Mutation-driven IMM was nearly ubiquitous in the globally prominent Beijing sublineage. Third, promoter methylation is widespread and associated with differential expression in the ΔhsdM transcriptome, suggesting promoter HsdM-methylation directly influences transcription. Finally, comparative and functional analyses identified 351 sites hypervariable across isolates and numerous putative regulatory interactions. This multi-omic integration revealed features of methylomic variability in clinical isolates and provides a rational basis for hypothesizing the functions of DNA adenine methylation in MTBC physiology and adaptive evolution.

## Introduction

In 2017, tuberculosis (TB) killed 1.6 million people globally, the most of any infectious disease, despite significant TB control efforts and the availability of effective TB drugs (WHO, 2017). Multi-drug-resistant tuberculosis (MDR-TB) threatens control efforts and debilitates patients through a grueling and often ineffective treatment regimen (52% success) (WHO, 2017). The primary causative agent of TB, M. tuberculosis, has a low mutation rate, and is reported to evolve chiefly through single nucleotide polymorphisms (SNPs) (Cohen et al., 2015). However, subpopulations of the pathogen consistently persist through chemotherapeutics, eventually developing full antibiotic resistance (Jain et al., 2016). It is unclear how such a genetically static organism adapts so rapidly to drug treatment and varied immune pressures.

DNA methylation is a plausible yet scarcely explored alternative mechanism for phenotypic variation in M. tuberculosis. M. tuberculosis encodes three known DNA methyltransferases (MTases), MamA, MamB, and HsdM, which each target a different sequence motif for N6-adenine methylation (Shell et al., 2013; Zhu et al., 2016). Previous studies have shown that loss-of-function (inactive) variants in these genes are common, and often associate with lineage (Phelan et al., 2018; Zhu et al., 2016). These minor differences in genotype result in radically different methylomes, potentially explaining the phenotypic variation observed between lineages (Phelan et al., 2018). However, these studies examined only a handful of isolates from each lineage of the Mycobacterium tuberculosis complex (MTBC), included few or no resistant isolates, and did not directly examine kinetics at each motif, relying instead on the motifs identified from single-molecule, real-time sequencing (SMRT-sequencing) software to classify isolates as lacking methylation of a motif entirely.

Prokaryotic DNA methylation has been shown to mediate diverse functions (Hernday et al., 2002; Ringquist and Smith, 1992; Wright et al., 1997), far beyond its originally understood role as the self-protective component of Restriction-Modification systems (RM systems). MTases that lack restriction enzymes, termed ‘orphan’ MTases (Blow et al., 2016) are highly conserved within phyla, and nearly ubiquitous, though diverse, across phyla, suggesting orphan MTases are functionally important (Blow et al., 2016). In M. tuberculosis, both MamA and HsdM are orphan MTases, while MamB shares sequence homology with Type IIG RM enzymes (Zhu et al., 2016), and therefore ostensibly has a functional restriction endonuclease domain. One emerging role for orphan MTases is regulating transcription (Ardissone et al., 2016; Low and Casadesús, 2008). In M. tuberculosis, MamA-mediated transcriptional regulation has been demonstrated at four promoters in M. tuberculosis (Shell et al., 2013), presumably through interaction with the −10 promoter element. A second characterized mechanism of DNA methylation mediated cis-regulation is interaction between methylated bases, MTases, and transcription factors (Beaulaurier et al., 2015; Hernday et al., 2002; Stephenson and Brown, 2016), which has been hypothesized to occur at specific sites in M. tuberculosis (Phelan et al., 2018; Zhu et al., 2016).

Previous interrogation of cis-regulation by DNA methylation in M. tuberculosis through SMRT-sequencing identified seven differentially methylated sites upstream of differentially expressed genes (Gomez-Gonzalez et al., 2019). However, only Euro-American and Indo-Oceanic (IO) isolates were analyzed, and only the 200 base pairs (bp) upstream of differentially expressed genes were examined for methylation, rather than a window more rigorously informed by mapped promoters and potential mechanisms of cis-regulation. More recently, an integrative analysis of SMRT-sequencing kinetics and differential transcription (RNAseq) following MTase knockout (ΔhsdM) in a M. tuberculosis clinical isolate concluded that HsdM-methylation did not directly affect transcript levels under their tested conditions (Chiner-Oms et al., 2019). However, the single tested condition and limited definition of HsdM-methylated promoters (overlap with SigA Pribnow boxes) invoke skepticism toward this conclusion. Thus, the extent of DNA methylation mediated transcriptional regulation in the MTBC and its effect on phenotype remain open questions.

Heterogeneous DNA methylation has been reported in several bacterial species (Casadesús and Low, 2013). Heterogeneous methylation can be caused by spontaneous mutations inactivating MTase coding genes (Casadesús and Low, 2013), site-specific occlusion from DNA-binding proteins (Atack et al., 2018; Beaulaurier et al., 2015; Wallecha et al., 2002), or intracellular stochastic methylation (Beaulaurier et al., 2015). When DNA methylation regulates gene expression, heterogeneous methylation creates multiple phenotypes within isogenic populations (Casadesús and Low, 2013). This phenotypic plasticity aids rapid adaptation to changing environmental pressures (Cota et al., 2016) and nutrient constraints (Atack et al., 2018) for other bacteria. However, no study has examined heterogeneous methylation in M. tuberculosis.

Here, through comparative, functional, and heterogeneity analysis, we sought to characterize how DNA adenine methylomes vary within and across MTBC clinical isolates.

## Results

### Integrative analysis of whole DNA adenine methylomes of 93 MTBC clinical isolates

We analyzed MTBC DNA adenine methylomes through four strategies (Figure 1). First, we used finished genomes assembled from long-read sequencing data and transferred annotations of functional and regulatory elements from virulent M. tuberculosis type strain H37Rv. This retained syntenic relationships and enabled facile comparative analyses without invoking assumptions inherent to ab initio methods. Second, we included the sequencing kinetics at all MTase motif sites in every isolate. This contrasts with the approach of prior M. tuberculosis methylome studies (Chiner-Oms et al., 2019; Gomez-Gonzalez et al., 2019; Phelan et al., 2018; Shell et al., 2013; Zhu et al., 2016), which examined only the MTase motifs identified by PacBio MotifMaker (https://github.com/PacificBiosciences/MotifMaker). This systematic approach revealed MTase genotypes with partial function, previously mischaracterized as completely inactive (Gomez-Gonzalez et al., 2019). Third, we used phylogenetic analysis to identify convergent MTase activity and heterogeneity analysis to characterize epigenomic diversity in vitro. Finally, we integrated transcription start sites (TSSs), transcription factor binding sites (TFBSs), and sigma factor binding sites (SFBSs) into our methylomic analyses. This helped us identify promoter methylation and potential cis (promoters and SFBSs) and trans (TFBSs) interactions between MTase motif sites and regulatory effectors.

![Figure 1.](https://cdn.elifesciences.org/articles/58542/elife-58542-fig1-v1.jpg)

**Figure 1.:** (A) Isolate selection. M. tuberculosis clinical isolates were obtained from tuberculosis (TB) patient sputa from four countries of high TB-burden (India, Moldova, South Africa, and The Philippines), and Sweden (primarily isolated from migrants originating in high TB-burden countries). Isolates were cultured, DNA extracted and sent to the Genomic Medicine Genomics Center at UCSD for amplification-free sequencing (PacBio RSII, P6C4 chemistry). Clinical isolates were supplemented by technical replicate control runs of avirulent reference strains, and publicly available clinical isolates along with technical triplicates of H37Rv (BioProject Nos. PRJNA555636, PRJNA329548, PRJEB8783). (B) Methylome assembly and annotation. Raw kinetic data were log-transformed, scaled, and standardized according to run-specific statistics in unmodified bases (Figure 1—figure supplement 1). Variation between technical replicates were used to adjust priors based on coverage to build pdfs for a Bayesian classifier. Methylation status of characterized motifs was classified with a Bayes’ classifier based on kinetics of unmodified and modified bases for each motif (Materials and methods). We processed all motifs of identified MTBC complex methyltransferases (Zhu et al., 2016) and assembled the methylome of each isolate with each motif site classified as methylated, hypomethylated, or indeterminate. We annotated each assembled methylome with overlapping and proximal features transferred by Rapid Annotation Transfer Tool (RATT) (Otto et al., 2011) from virulent type strain H37Rv. (C) Methylome variation. We mapped MTase genotypes to methylation levels of their motifs to describe novel active, partially active, and inactive alleles responsible for varying degrees of motif methylation (Supplementary file 1). We analyzed heterogeneity with SMALR (Beaulaurier et al., 2015) to characterize the capacity for methylomic variation within isogenic colonies and to probe for phase variation. We applied phylogenetic analysis of MTase genotypes and their corresponding methylation activity profiles to determine how DNA methylation across evolutionary time and identify epigenetic convergence across lineages. (D) Comparative and functional methylomics. We surveyed whole methylomes to identify motif sites and isolates with anomalous patterns. To examine motif sites consistently classified as hypomethylated for previously described causes of hypomethylation (Beaulaurier et al., 2019), we screened against published TFBS affinities (Minch et al., 2015) for interactions with DNA methylation (Supplementary file 5). We also screened for proximal motif sites among hypomethylated bases, which can create epigenetic ‘switches’ (Hernday et al., 2002). To identify putative cis-regulatory interactions with DNA methylation (Supplementary file 6), MTase motif sites were integrated with promoter element annotations (transcription start sites and sigma factor binding motifs).

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/58542/elife-58542-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** (A) Distribution of inter-pulse duration (IPD) ratios across all bases for one of the replicate runs of avirulent type strain H37Ra. (B) log10-transformation converts log-normal distribution in A into normal distribution of log10 (IPD ratio). (C) Difference in sequencing kinetics (log2 (IPD ratio)) for each base between replicate H37Ra SMRT-sequencing runs across the genome. Only a subsample of bases (n = 100,000) are shown. Note that there were four discrepant bases the H37Ra replicates, each of which were single base insertions. This error rate (roughly 1/106, or QV60) is in line with that expected of a good PacBio run at our average coverage (Koren et al., 2013). We removed the insertions from the discrepant run before comparing the IPD ratios between runs. The red-dashed vertical line indicates the first position removed. (D) Difference in log10 (IPD ratio) between replicate runs as a function of coverage. This comparison showed a weak (R = −0.0872, Pearson’s correlation coefficient) but significant correlation (p = 1.04×10−10) with decreased discrepancy as coverage increased. (E) Quantile–Quantile plot comparing log10-transformed IPD ratios at a subset of mamA motif sites (blue) and at non-mamA motifs (red) to theoretical values in a perfect normal distribution (black diagonal line). Green horizontal lines depict extremes expected to appear only once in the theoretical normal distribution.

For every isolate, the average inter-pulse duration (IPD) ratio was calculated across the reads mapping to each base. To characterize the noise in these measurements, we compared the IPD ratios at each base between technical replicates of reference strain H37Ra (Figure 1—figure supplement 1). We then scanned the genomes for all matches to the known target motifs (Zhu et al., 2016) of established M. tuberculosis MTases and examined their IPD ratios (Figure 2A). Mean single-strand coverage at target motif sites within clinical isolates ranged from 25x-152x (median = 64).

![Figure 2.](https://cdn.elifesciences.org/articles/58542/elife-58542-fig2-v1.jpg)

**Figure 2.:** (A), Boxplots of inter-pulse duration (IPD) ratio distributions within MamA (top pane), HsdM (middle pane), and MamB (bottom pane) target motifs for each M. tuberculosis or M. africanum isolate. Boxplots are colored by mamA, hsdM, and mamB genotype. In one isolate, hsdS L119S mutation disrupted methylation capacity and is marked by an asterisk (*). In each pane, horizontal lines mark the mean log2 (IPD ratio) of motif sites for isolates with active (mint line) and inactive (red line) MTases. (B) SNP-based phylogenetic trees with mutations mapped for each MTase. Isolates are colored by MTase genotype using the same colors as the boxplots in A, except for MamB, which is colored by MTase activity. The phylogeny was built using maximum likelihood on a concatenation of 22,393 SNPs with M. bovis and M. canetti as outgroups. Colors of the outer rung indicate lineage. (C) Phylogeny of isolates in this study with branches colored according to the MTase activity profile. Colors of the outer rung indicate lineage according to the same color scheme as B. (D) Density traces of sequencing kinetics for each isolate at every motif site, organized into panes by MTase (columns) and lineage (rows), and colored by the activity of their MTase. The fill underneath each density trace is rendered translucent such that overlapping distributions from multiple isolates appear progressively darker as a function of the number of overlapping distributions.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/58542/elife-58542-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** Alignment of wild-type mamB and insertion element IS6110 to mutant mamB genes from clinical M. tuberculosis isolates. Recently, a clinical M. tuberculosis isolate (SRA:ERP009820) was reported with inactive DNA methyltransferase MamB and to harbor only mamB variant D59G (Chiner-Oms et al., 2019). Our analysis of that same isolate revealed a 1356 bp insertion of an IS6110 element, as well as variant V616A. Alignment to transposable element IS6110 determined the identity of this large insertion. (A) Alignment summary from a megablast of the wild-type mamB sequence against the variant mamB gene with the large insertion. Below is the alignment summary from a megablast of IS6110 against the variant mamB gene. (B) Alignment summary from a megablast of the wild-type mamB sequence against the mamB gene in a clinical isolate which shared the mamB variant D59G and V616A, but lacked the large insertion, and had active methylation of MamB target sites. The alignment had 0 gaps and two mismatches (identity 4819/4821).

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/58542/elife-58542-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** Activity profiles measured here by number of isolates in the dataset with that profile. Mint represents normal methyltransferase activity while red represents reduced or absent activity. *Includes partially active variant K1033T. **Includes reference strains H37Rv and H37Ra. ***Includes partially active variant G152S.

### Epigenomic convergence across lineages

Comparing the distribution of these IPD ratios in each isolate established their MTase activity profile and the functional impact of MTase mutations (Figure 2A, Supplementary file 1). Each MTase had at least three distinct loss-of-function or partially active mutations (Figure 2A). To determine how activity profiles distributed across M. tuberculosis evolution, we mapped the MTase genotypes to a phylogenetic tree (Figure 2B). MTase activity converged across lineage (through multiple distinct mutations) and varied within lineage (Figure 2B and D). The East-Asian (EAS), Euro-American, and IO lineages each had multiple profiles among their members (Figure 2B and D). This contradicts one previous analysis on a smaller isolate set that reported lineage-specific methylation (Phelan et al., 2018), and corroborates the opposing conclusion reached in another recent publication (Chiner-Oms et al., 2019).

### Diverse mutations drive DNA methyltransferase activity profiles

Cumulatively, the 93 M. tuberculosis and M. africanum isolates harbored 40 distinct mutations within the known MTase genes mamA, mamB, and hsdM/hsdS, including 29 previously unreported (Supplementary file 1). Comparing the IPD ratio at each base matching the MTase target motifs across isolates revealed the effect of each variant on MTase activity (Figure 2A). The isolates had four novel loss-of-function mutations: mamB H770N, mamB DELG2543, mamB INS1181-1583, and hsdM DEL900-909. This comparison also confirmed that variant hsdS L119R inactivates MTase activity in the HsdM complex. Previously, hsdS L119R had been observed only in tandem with another loss-of-function mutation, hsdM G173D (Chiner-Oms et al., 2019; Phelan et al., 2018). One isolate had hsdS L119R alone, and its HsdM motifs were unmodified (Figure 2A). Twenty-nine MTase mutations had no apparent effect on MTase activity, 23 of which were previously unreported (Supplementary file 1). All isolates had at least one active MTase (Figure 2C), yet only 32/93 clinical isolates had all three MTases active (Figure 2—figure supplement 2).

In total, 12 different mutations had reduced or inactive MTase function (three hsdM/hsdS, five mamB, and four mamA), demonstrating that MTase disrupting mutations are repeatedly selected for, although almost all individual mutations are monophyletic (Figure 2A and B).

Recently, mamB D59G was reported as the sole variant in a MamB inactive isolate (Chiner-Oms et al., 2019) (SRA: ERR956955, ERR964401). We identified four Indo-Oceanic isolates with mamB variant D59G, but all four also harbored V616A (Supplementary file 2). Two of these four isolates were active and had no other mutations. However, the other two were MamB inactive and carried a 1356 bp insertion that we have identified as an IS6110 insertion sequence (Figure 2—figure supplement 1). One of these inactive isolates was the same isolate recently reported with mamB D59G alone (Chiner-Oms et al., 2019). The prior study did not report the mamB insertion, likely due to their reference-mapping of short reads to call MTase variants (van Dijk et al., 2018). However, it is unclear why their methods did not capture V616A. Considering that MamB was active in isolates carrying mamB D59G without the insertion, we conclude the insertion was responsible for inactivating MamB.

Our approach resolves the disputed functional impact of mamA variant E270A (mamAE270A), common to the EAS lineage (ref (Phelan et al., 2018) and Supplementary file 2). Nucleoside digestion previously showed low-level methylation in mamAE270A mutants (Shell et al., 2013). However, subsequent SMRT-sequencing studies reported contradictory findings. Three studies reported a lack of methylation at all MamA motif sites in mamAE270A isolates (Gomez-Gonzalez et al., 2019; Phelan et al., 2018; Zhu et al., 2016) while another reported partial methylation in one mamAE270A isolate, and a complete lack of methylation in two mamAE270A isolates (Chiner-Oms et al., 2019). In the 34 isolates with mamAE270A, MamA motif sites had intermediate IPD ratios (Figure 2A, top), indicating partial activity. Our analysis revealed three additional MTase alleles that conferred partial MTase activity: hsdMK458N;E481A, mamAG152S, and mamBK1033T (Figure 2A). These isolates had IPD ratio distributions consistent with neither homogenously methylated nor unmethylated sites (Figure 2A & D).

We hypothesized that these isolates’ intermediate IPD ratios were due to heterogeneous methylation. IPD ratios are reported as the average IPD ratio observed across sequencing reads mapped to each position, which originate from different cells. Therefore, if isolate colonies contained subpopulations of cells with different methylomes, it would result in the intermediate IPD ratios we observed. Heterogeneous methylation can be caused by different phenomena, including phase-variant MTase activity, intracellular stochastic methylation, or transient hemimethylation from a subset of cells undergoing cell division. To distinguish between these possibilities, we examined IPD signals at the read level using SMALR (Beaulaurier et al., 2015).

### A subset of DNA MTase alleles drive constitutive intercellular mosaic methylation in M. tuberculosis

Within each sequencing read, the software SMALR (Beaulaurier et al., 2015) calculates the average IPD (natural log-transformed) across multiple motif sites targeted by the same MTase. This ‘native IPD value’ will be higher in reads where each motif site is methylated, lowest in reads with no motif sites methylated, and intermediate in reads with a fraction of motif sites methylated (Figure 3H). Thus, the distribution of native IPD values in an isolate can discriminate homogenous methylation (or unmethylation) from two types of heterogeneous methylation: phase-variant MTase activity and intracellular stochastic methylation (Beaulaurier et al., 2015). Phase-variant MTase activity causes a distinctive bimodal distribution in SMALR native IPD values, while intracellular stochastic methylation results in a unimodal distribution with a mean between that of fully methylated and fully unmethylated sequences (Beaulaurier et al., 2015). SMALR native IPD values can also potentially distinguish transient hemimethylation from intracellular stochastic methylation and phase-variant MTase activity. Previously, transient hemimethylation was attributed to the small fraction (0.07%) of unmethylated reads observed in cultures with otherwise fully methylated reads (Beaulaurier et al., 2015). Transient hemimethylation would thus likely manifest in SMALR native IPD values as a bimodal distribution with a small minority of entirely unmethylated reads among a majority of methylated reads.

![Figure 3.](https://cdn.elifesciences.org/articles/58542/elife-58542-fig3-v1.jpg)

**Figure 3.:** Native IPD value (nat) is the subread-mean normalized natural log of IPDs (as output from SMALR Beaulaurier et al., 2015) across all motif sites within a subread. (A-G) depict the distribution of mean native IPD values among subreads for each isolate of the specified MamA or MamB allele. Each colored trace corresponds an isolate. Each pane has two reference curves: a mean native IPD value, number of measurements (isolates), and identical standard deviation identical to those of the inactive genotypes (light blue) and a curve with a mean native IPD value, standard deviation, and number of observations (isolates) identical to that of isolates with wild-type MamA (A-D) or MamB (E-G) activity (light violet). (A) mamAWT. (B) mamAW136R. (C) mamAE270A. The dotted vertical line marks the mean native IPD value for all mamAE270A isolates. (D) mamAG152S. (E-G) Putative heterogeneous methylation by mamBK1033T mutant (same as A-D, but for mamB). Only isolates with >19 qualifying subreads are included (at least 6 CACGCAG motifs are required within the subread to qualify). (E) Wild-type MamB (n = 16 passing inclusion criteria). There is no consistent signature of stochastic heterogeneity or phase variation. (F) mamBK1033T (n = 1) appears to exhibit low MTase activity, with mean native IPD dotted line well below that of wild-type MamB and the inactive genotypes (solid black line) and significantly greater than the mean native IPD value of inactive genotypes, suggesting stochastic heterogeneity. This native IPD value resembles the low-level MTase activity in isolates harboring the mamAE270A allele. (G) All qualifying isolates (n = 5) with mamB inactive alleles. Despite harboring different nonsynonymous mamB mutations (n = 4), mamB motifs appear entirely unmethylated, with a native IPD value consistent with inactive MTase genotype (Beaulaurier et al., 2015) and no clear signals of phase variation or intracellular stochastic heterogeneity. (H) Stochastic versus phase-variable methylation. Conceptual illustration depicting the distinction between methylome diversity within colonies exhibiting phase-variable methylation (top) and stochastic methylation (bottom). Each gray segment represents a chromosome from an individual cell within the colony. Each oval within the segment represents a motif site, illustrated as methylated (mint) or unmethylated (red).

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/58542/elife-58542-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** (A) Effect of methionine starvation induces heterogeneous methylation within single subreads. Heterogeneity analysis of previously published SMRT-sequencing data from a methionine auxotroph H37Rv mutant (Berney et al., 2015) (H37Rv∆metA, blue trace). Simulated bimodal distributions scores were generated from mamAW136R (inactive MamA) strains and wild-type H37Rv runs (active MamA) to simulate a mixture of wholly methylated and wholly unmethylated reads (red traces). Reads were included according to the ratio of mean native IPD value in H37Rv∆metA to mean native IPD value of wholly methylated runs (dashed vertical lines), scaled between 0 (wholly unmethylated) and 1 (wholly methylated). (B) Kinetics of methionine-starved H37Rv differ from phase-variant-simulated mixture. Peak height on the bar chart depicts the simulated bimodal distribution subtracted from the observed distribution. Dotted lines mark mean native IPD values (post-scaling) of wholly non-methylated and methylated reads.

The native IPD values for MamA motif sites in each sequencing read distributed normally in the 49 mamA wild-type isolates, with a mean native IPD of 2.15 (per-isolate means: 1.96–2.28) (Figure 3A), indicating that MamA motifs on most reads in these isolates were entirely methylated (Beaulaurier et al., 2015). The four isolates with inactive allele mamAW136R each distributed normally (mean = −0.107, Figure 3B) indicating a consistent lack of MamA-methylation. In contrast, the four isolates with partially active variant mamAG152S distributed normally with varied per-isolate means (range: 0.22-0-1.19). Their consensus mean native IPD value (0.766) was substantially above mamAW136R (Cohen’s d = 1.10, 95% CI 1.04–1.17; two-tailed t-test p = 3.20×10−207) and below mamA wild-type isolates (d = 2.14, CI 2.09–2.20, p<2.23×10−308, Figure 3C, Figure 3—source data 1). Each mamAG152S isolate individually had a lower mean value than wild-type as well (d for isolate with lowest effect size = 0.48, CI 0.39–0.57, p = 9.74×10−21). This unimodal, normal distribution of intermediate native IPD values implies intracellular stochastic methylation, rather than phase-variant MTase activity (Beaulaurier et al., 2015). While phase-variant MTase activity has been observed in many bacteria, intracellular stochastic methylation has previously only been observed in a single species, Chromohalobacter salexigens (Beaulaurier et al., 2015).

After observing this intracellular stochastic methylation in mamAG152S isolates, we analyzed heterogeneity in isolates with partially active MamA (E270A) and MamB (K1033T). The 34 mamAE270A isolates had a methylated fraction (mean = 0.0558, Figure 3C) lower than those of wild-type isolates (mean = 2.15) and higher than the methylated fraction of isolates with inactive allele W136R (d = 0.23, p = 8.68×10−25), indicating intracellular stochastic methylation. Native IPD values for mamB wild-type (mean = 2.24) were significantly (p = 0.0006) though slightly (d = 0.15, CI 0.05–0.25) higher than for mamA wild-type, consistent with homogenous methylation. MamB inactive alleles (mean = −0.235) were modestly lower (d = 0.19, CI 0.008–0.377) than inactive allele MamAW136R with borderline statistical significance (p = 0.041), suggesting that mamAW136R may have retained a miniscule amount of MTase activity. However, the effect of methylation of sequencing kinetics can vary between motif sequences, and so we cannot conclude from our data that limited activity is present. We therefore continue to consider mamAW136R to be an inactive allele. Like mamAE270A, the mean native IPD value for mamBK1033T was greater than in inactive alleles (d = 0.77, CI 0.34–1.21, p = 0.007) consistent with intracellular stochastic methylation (Figure 3E–G). Multiple HsdM motif sites clustered together on the same subread too infrequently for analysis with SMALR, precluding analysis of potential heterogeneity with SMALR (isolates had on average 3898.6 MamA, 822.9 MamB, and 719.4 HsdM sites).

While these intermediate native IPD value distributions for mamAE270A, mamAG152S, and mamBK1033T are consistent with intracellular stochastic methylation, they would also be produced by consistent methylation of some motif sites and consistent lack of methylation in the remaining sites. By examining isolates with these partially active alleles, we see that mean IPD ratios for motif sites distribute unimodally at intermediate values rather than bimodally (purple-filled traces for MamA and MamB, Figure 2D). Therefore, we reject this alternative explanation and conclude that intracellular stochastic methylation generates diverse combinations of methylated motif sites within the bacilli from which the sequenced DNA was isolated. We call this epigenetic mosaicism ‘intercellular mosaic methylation’. The methylomic diversity in intercellular mosaic methylation is distinct from the two discrete phases generated from phase-variable methylation, instead generating a mosaic of methylation patterns among the cells comprising an isogenic colony (Figure 3H).

Next, we asked whether methionine restriction could induce intercellular mosaic methylation in isolates with wild-type MTase function. Methionine is directly linked to DNA methylation by its requirement of S-adenosyl methionine (SAM) as the methyl group donor (Parveen and Cornell, 2011). We reasoned that if methionine starvation induces intercellular mosaic methylation, the effect could be extrapolated to other nutrient restrictions that limit flux through the adenine methylation reaction, such as precursor metabolites for SAM synthesis or trace metal ion cofactors required for SAM biosynthesis (Czyrko et al., 2018) and adenine methylation (Bist and Rao, 2003). We ran SMALR on published kinetic data from metA-knockout H37Rv methionine auxotrophs (∆metA) SMRT-sequenced following 5 days of methionine starvation (Berney et al., 2015).

To test for intercellular mosaic methylation in ∆metA we compared its native IPD value distribution to a mixture of wholly methylated and wholly unmethylated reads (Figure 3—figure supplement 1A). This simulated mixture was sampled from mamA wild-type and inactive isolates, in proportion to produce the same mean as ∆metA. The ∆metA native IPD value distribution was distinct from the simulated mixture, with fewer fully methylated reads and more partially methylated reads (Figure 3—figure supplement 1). These results are consistent with a mixture of fully methylated reads inherited from bacilli born prior to methionine deprivation and stochastically methylated reads from daughter strands that underwent partial re-methylation following starvation. These results suggest that intercellular mosaic methylation can be induced by nutrient limitation (at least for methionine, and presumably other nutrient constraints that limit flux through the adenine methyltransferase reaction), providing a potential mechanism of environmentally induced phenotypic heterogeneity.

### Anomalous methylation patterns in orphan MTase motif sites

Next, we surveyed all common motif sites (present in ≥75 isolates, n = 4,486; Supplementary file 3) for patterns in their variation across isolates and motif sites. IPD ratio distributions were stable within isolates the same MTase allele except for partially active mutants (Figure 4A), consistent with prior observations that motif sites are typically invariably methylated or invariably unmethylated (Blow et al., 2016). Most of the isolates with anomalous methylation had mamA alleles with partial activity, while a few isolates with hsdM alleles with full activity had anomalous methylation patterns (arrows, Figure 4B).

![Figure 4.](https://cdn.elifesciences.org/articles/58542/elife-58542-fig4-v1.jpg)

**Figure 4.:** Heat maps of sequencing kinetics for (A) MamA, (B) HsdM, and (C) MamB motifs at all common (in ≥75 isolates) motif sites (y-axis), descending according to median sequencing kinetics (log2 (IPD ratio)). Isolates (x-axis) are sorted from left to right by activity level, lineage, and genotype in decreasing priority. Lineages are Indo-Oceanic (IO), East-Asian (EAS), East-African-Indian (EAI), Euro-American (E), Ethiopian (Lineage 7), and the M. africanum lineages 5 and 6. Dots on the rotated plot adjacent to the heatmap express the median log2 (IPD Ratio) for each site across isolates. Darker and lower dots indicate a lower median (log2 (IPD Ratio)). Red arrows mark isolates with wild-type or near wild-type MTase activity that exhibit hypomethylation at more motif sites (dark bands) than other wild-type isolates. Blue arrows mark two isolates with significantly fewer hypomethylated motif sites than other isolates with wild-type HsdM activity, for unknown reasons. The green arrow in the MamB plot marks an isolate with an IPD ratio significantly higher than expected for an inactive isolate, suggesting some MTase activity for the genotype. (D) Distribution of standard deviation (sd) sizes among MamA motif sites across isolates with one of three methylation activity levels: partial MamA activity from the E270A mutation common to EAS isolates, the loss-of-function W136R mutation (‘knockout mutant’), or one of the genotypes encoding MamA with wild-type methylation activity. (E) Position (x-axis) in a representative genome and variability sd of (log2 (IPD Ratio)) in sequencing kinetics across isolates with active MTase (y-axis) at common motif sites (present in 75 or more isolates). Motif sites within three sd of the mean for MamB motifs are gray, and the outliers (>3 sd from mean) are highlighted in red. CDSs within which each of the top 10 most variable sites for each MTase occur are labeled, along with their palindromic partner motif site.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/58542/elife-58542-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** Mapping of mutations in mamB and their effect on DNA methyltransferase (MTase) function, at the (A) primary, (B) secondary, and (C) tertiary levels of abstraction. Sequences from the assemblies examined in this study were drawn from the East-Asian (EAS), Indo-Oceanic (IO), and Euro-American (EAM) lineages, while those of the two ancestral mycobacteria, Mycobacterium bovis and Mycobacterium microti were obtained from a recent publication by Zhu and colleagues (Zhu et al., 2016). MamB amino acid sequences from these genomes were aligned with MTase functionality (inferred by methylation status of its motifs via SMRT-sequencing) indicated, and variants with respect to functional wild-type amino acid sequences mapped in the context of annotated domains from InterPro. These domains and mutations were in turn mapped colors are preserved from (B) to the left structure of (C) onto the predicted structure. This figure was adapted from the thesis of SJM (Modlin, 2018).

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/58542/elife-58542-fig4-figsupp2-v1.jpg)

**Figure 4—figure supplement 2.:** (A) Distribution of standard deviation (SD) size of kinetics (log2 of the IPD Ratio) for each common (n > 50) motif sites across isolates with the relevant DNA methyltransferase (MTase) active. MamB is least frequently hypomethylated and the three distributions appear similar outside of outliers and therefore defined the cutoff SD (of standard deviation size) for ‘hypervariable’ motif sites (SD size > 3 standard deviations above the MamB mean). (B) Distribution of the sequencing kinetics for consistently hypomethylated MTase motif sites (bin width = 0.2), across isolates with active genotype for the implicated MTase. Only sites present in ≥ half of the clinical isolates are shown. (C) Common motif sites plotted by mean and standard deviation of sequencing kinetics across isolates with active MTases, with points color indicating that the site is hypomethylated (blue), hypervariable (red), both hypervariable and hypomethylated (purple), or neither (gray). The top five most variable motif sites and bottom five mean sites for each MTase are labeled, if they classified as hypervariable and/or hypomethylated.

Analyzing variation across motif sites of active wild-type isolates revealed three interesting features. First, while most motif sites were primarily methylated (light yellow), a subset had significantly lower median IPD (Figure 4A–C). Second, among the mostly methylated motif sites, a handful had lower IPDs in a subset of isolates (Figure 4A–C, Figure 4—figure supplement 2B). The converse was also true; some motif sites with low median IPDs had higher IPDs in a subset of isolates. Third, partially active MTases had distinct methylation profiles with median IPDs between those of inactive and wild-type (Figure 4D). All three features were more pronounced in HsdM and MamA motif sites than in MamB (Figure 4A–C,E).

MamA and HsdM are orphan MTases, which frees their motif sites to remain unmethylated without risking degradation from a cognate restriction enzyme (Blow et al., 2016), potentially explaining their variable methylation (Zhu et al., 2016) compared to MamB. To corroborate MamB as a full RM system rather than an orphan MTase, we searched InterPro database for functional domains and identified a putative restriction endonuclease (REase) domain (Figure 4—figure supplement 1) as its cognate REase. Single chain restriction-modification fusions are a defining characteristic of Type IIG RM systems (Shen et al., 2011), which MamB belongs to Zhu et al., 2016. Orphaned MTases can safely leave motif sites unmethylated, affording the opportunity to evolve essential functions (Blow et al., 2016). At such sites, advantageous methylation states can be selected for following prolonged culturing. Considering this, we sought to identify motif sites that were hypervariable across strains with active MTases, reasoning that it would indicate differential selection for methylation status during culture prior to sequencing and highlight interesting differences between strains. To find hypervariable sites, we calculated the standard deviation (SD) in IPD ratio across isolates for each MTase site. Variation across isolates for each qualifying motif site was compared against the distribution of SD (standard deviation of SD across MamB sites) in MamB sites (Figure 4E, Figure 4—figure supplement 2C), because they distributed normally and with few outliers (Figure 4—figure supplement 2A). We defined motif sites with SD ≥3 standard deviations above the mean SD of MamB motif sites. Of 4486 common (in ≥75 isolates) MTase motif sites, 351 were hypervariable (Supplementary file 4). These hypervariable sites fell within 204 coding regions, and within promoter-proximal regions upstream (within 100 bp) of 25 TSSs (Supplementary file 4). Yet only seven hypervariable sites were MamB motifs. Hypervariability was 9.43-fold more prevalent in motif sites of orphan MTases than in MamB motif sites (95% CI: 4.50–23.7). This marked enrichment (p = 3.39×10−17, two-tailed Fisher’s exact test) of hypervariable motif sites in MamA (n = 240) and HsdM (n = 104) is consistent with the lack of selection pressure against unmethylated sites characteristic of orphan MTases (Blow et al., 2016).

### Hypomethylated MTase motif sites are rare yet remarkably consistent across isolates

One characteristic of orphan MTases is hypomethylated sites, specific genome sites lacking or absent of methylation despite the presence of an MTase target motif and active MTase (Blow et al., 2016). Hypomethylated sites have previously been found in M. tuberculosis (Zhu et al., 2016) and many other bacteria (Blow et al., 2016; Hernday et al., 2002; Ringquist and Smith, 1992). To identify hypomethylated sites in each of our isolates, we applied Bayesian classification to their sequencing kinetics. Active isolates averaged 20.7 hypomethylated HsdM sites, 13.4 hypomethylated MamA sites, and 0.289 hypomethylated MamB sites (Figure 5—figure supplement 1), comparable to previous reports (Zhu et al., 2016). However, while rare, these hypomethylated motif sites showed remarkable consistency, with the same MTase motif loci hypomethylated in multiple isolates. The most conserved hypomethylated locus was within mmpL4, 1,719 bp downstream of its start. Despite having a MamA target motif, this locus was unmethylated in 51 MamA active isolates (Table 1). In total, 34 MamA loci and 58 HsdM loci were consistently hypomethylated (p-value<4.72E-07, cumulative binomial, Supplementary file 5). These loci included 18 of the top 10 frequently hypomethylated MamA and HsdM sites in a previous study of 12 MTBC strains (Table 1). This consistency would be unlikely if hypomethylation occurred randomly, suggesting there are conserved mechanisms preventing methylation at these loci.

MamB motif sites, in contrast, were thoroughly methylated in MamB active isolates (Figure 5—figure supplement 1C). Only two MamB motif loci were hypomethylated in a significant number of isolates, and even these loci were methylated in most isolates (Table 1). The near uniform methylation of MamB target sites is likely to prevent DNA cleavage from its putative cognate restriction endonuclease (Figure 4—figure supplement 1).

**Table 1.**
 Consistently Hypomethylated MTase Motif Sites Across Clinical M.tuberculosis isolates.The top 20 most significant hypomethylated loci from each MTase. For each methyltransferase (‘MTase’) motif target locus (‘Gene’, ‘Sense’, and ‘Position’), we counted the number of isolates in which the isolate was hypomethylated and the total number of isolates that possessed the locus (‘Hypomethylated’). This fraction was used to perform a cumulative binomial probability test (‘p-value’). Loci with p-values below 4.72E-07 were considered significant at 0.01 significance level, after Bonferroni correction for multiple hypothesis testing. Loci were assigned by our methylome annotation pipeline using H37Rv reference annotations transferred from Rapid Annotation Transfer Tool (RATT) (Otto et al., 2011). For each palindromic pair, the locus with the most significant hypomethylated fraction is reported. In case of a tie, the locus on the same strand as the gene is reported. The fraction of active isolates hypomethylated at the partner site is included (‘Palindrome’). The surrounding 20 bases of each loci were scanned for transcription factor binding site motifs previously characterized in M. tuberculosis (Minch et al., 2015). The most significant motif match was included (‘Top TF’). Only transcription factor binding motifs with an E-value below 0.01 were scanned for, and only matches with a p-value (converted log-likelihood ratio score) below 0.0001 were reported. MTase motif loci less than 100 bp from another locus targeted by the same MTase were labeled (‘Yes’ in column ‘Nearby Motif’). Genes that were previously reported (Zhu et al., 2016) to contain frequently hypomethylated sites are marked with an asterisk.Table 1—source data 1.Multisequence fasta file with context sequence of each consistently hypomethylated MTase Motif Locus.Table 1—source data 2.Output file from FIMO, run with the fasta file Table 1—source data 1, and the probability weight matrices of TFBS motifs characterized in H37Rv (Minch et al., 2015).


<table>
  <thead>
    <tr>
      <th>Gene</th>
      <th>Sense</th>
      <th>Position</th>
      <th>Hypomethylated</th>
      <th>p-value</th>
      <th>Palin-drome</th>
      <th>Top TF</th>
      <th>Annotated Function</th>
      <th>Nearby Motif</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="9">HsdM</td>
    </tr>
    <tr>
      <td>rocA*</td>
      <td>sense</td>
      <td>834</td>
      <td>67/70</td>
      <td>2.49E-99</td>
      <td>67/70</td>
      <td>Rv3488</td>
      <td>Probable pyrroline-5-carboxylate dehydrogenase</td>
      <td></td>
    </tr>
    <tr>
      <td>cobK*</td>
      <td>sense</td>
      <td>304</td>
      <td>50/68</td>
      <td>6.15E-62</td>
      <td>50/68</td>
      <td>Rv2788</td>
      <td>Precorrin-6X reductase</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>Rv1461*</td>
      <td>antisense</td>
      <td>559</td>
      <td>47/70</td>
      <td>3.17E-55</td>
      <td>37/70</td>
      <td>Rv1956</td>
      <td>Iron-sulfur cluster assembly protein</td>
      <td></td>
    </tr>
    <tr>
      <td>Rv2963*</td>
      <td>sense</td>
      <td>683</td>
      <td>46/70</td>
      <td>2.10E-53</td>
      <td>46/70</td>
      <td>Rv2788</td>
      <td>putative ion transporter</td>
      <td></td>
    </tr>
    <tr>
      <td>PPE24*</td>
      <td>antisense</td>
      <td>2275</td>
      <td>33/33</td>
      <td>1.31E-51</td>
      <td>32/33</td>
      <td>Rv3133c</td>
      <td>PPE family protein PPE24</td>
      <td></td>
    </tr>
    <tr>
      <td>metA*</td>
      <td>antisense</td>
      <td>391</td>
      <td>42/70</td>
      <td>2.20E-46</td>
      <td>40/70</td>
      <td>Rv2324</td>
      <td>homoserine O-acetyltransferase</td>
      <td></td>
    </tr>
    <tr>
      <td>pks6*</td>
      <td>sense</td>
      <td>423</td>
      <td>26/34</td>
      <td>1.18E-33</td>
      <td>9/34</td>
      <td>Rv1719</td>
      <td>Probable membrane bound polyketide synthase</td>
      <td></td>
    </tr>
    <tr>
      <td>PPE24*</td>
      <td>antisense</td>
      <td>1807</td>
      <td>17/17</td>
      <td>6.14E-27</td>
      <td>16/17</td>
      <td>Rv3133c</td>
      <td>PPE family protein PPE24</td>
      <td></td>
    </tr>
    <tr>
      <td>pks6*</td>
      <td>sense</td>
      <td>424</td>
      <td>21/32</td>
      <td>3.97E-25</td>
      <td>14/32</td>
      <td>Rv1719</td>
      <td>Probable membrane bound polyketide synthase</td>
      <td></td>
    </tr>
    <tr>
      <td>pyrC</td>
      <td>sense</td>
      <td>744</td>
      <td>20/70</td>
      <td>5.90E-15</td>
      <td>19/70</td>
      <td>Rv1049</td>
      <td>Probable dihydroorotase PyrC</td>
      <td></td>
    </tr>
    <tr>
      <td>Rv3179</td>
      <td>upstream</td>
      <td>36</td>
      <td>9/9</td>
      <td>1.33E-14</td>
      <td>9/9</td>
      <td>Rv1816</td>
      <td>Conserved protein</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>Rv3179</td>
      <td>upstream</td>
      <td>49</td>
      <td>9/9</td>
      <td>1.33E-14</td>
      <td>9/9</td>
      <td>Rv1816</td>
      <td>Conserved protein</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>gcA*</td>
      <td>antisense</td>
      <td>467</td>
      <td>19/69</td>
      <td>5.89E-14</td>
      <td>14/69</td>
      <td>Rv1473A</td>
      <td>Possible GDP-mannose 4,6-dehydratase</td>
      <td></td>
    </tr>
    <tr>
      <td>Rv2279</td>
      <td>antisense</td>
      <td>693</td>
      <td>10/21</td>
      <td>1.01E-10</td>
      <td>9/21</td>
      <td>Rv1776c</td>
      <td>Probable transposase</td>
      <td></td>
    </tr>
    <tr>
      <td>lpqG</td>
      <td>upstream</td>
      <td>93</td>
      <td>14/54</td>
      <td>2.85E-10</td>
      <td>8/54</td>
      <td>Rv1219c</td>
      <td>Probable conserved lipoprotein LpqG</td>
      <td></td>
    </tr>
    <tr>
      <td>Rv2038c</td>
      <td>sense</td>
      <td>183</td>
      <td>14/69</td>
      <td>9.05E-09</td>
      <td>9/69</td>
      <td>Rv2989</td>
      <td>Probable sugar-transport ATP-binding protein ABC transporter</td>
      <td></td>
    </tr>
    <tr>
      <td>PPE24*</td>
      <td>sense</td>
      <td>1584</td>
      <td>5/5</td>
      <td>1.95E-08</td>
      <td>5/5</td>
      <td>Rv0818</td>
      <td>PPE family protein PPE24</td>
      <td></td>
    </tr>
    <tr>
      <td colspan="9">MamA</td>
    </tr>
    <tr>
      <td>mmpL4*</td>
      <td>sense</td>
      <td>1719</td>
      <td>51/51</td>
      <td>2.18E-126</td>
      <td>49/51</td>
      <td>Rv0678</td>
      <td>transmembrane transport protein</td>
      <td></td>
    </tr>
    <tr>
      <td>Rv1049</td>
      <td>upstream</td>
      <td>7</td>
      <td>39/51</td>
      <td>1.23E-85</td>
      <td>9/51</td>
      <td></td>
      <td>Oxidation-sensing regulator MosR</td>
      <td></td>
    </tr>
    <tr>
      <td>Rv1461*</td>
      <td>antisense</td>
      <td>472</td>
      <td>38/50</td>
      <td>2.73E-83</td>
      <td>35/50</td>
      <td></td>
      <td>Iron-sulfur cluster assembly protein Suf</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>treZ*</td>
      <td>antisense</td>
      <td>1272</td>
      <td>31/35</td>
      <td>2.14E-72</td>
      <td>26/35</td>
      <td></td>
      <td>Maltooligosyltrehalose trehalohydrolase</td>
      <td></td>
    </tr>
    <tr>
      <td>accE5</td>
      <td>downstream</td>
      <td>447</td>
      <td>20/33</td>
      <td>2.89E-41</td>
      <td>3/33</td>
      <td></td>
      <td>acetyl-/propionyl-coenzyme A carboxylase</td>
      <td></td>
    </tr>
    <tr>
      <td>PPE34*</td>
      <td>sense</td>
      <td>1664</td>
      <td>13/20</td>
      <td>7.05E-28</td>
      <td>7/20</td>
      <td></td>
      <td>PPE family protein PPE34</td>
      <td></td>
    </tr>
    <tr>
      <td>mptA*</td>
      <td>sense</td>
      <td>23</td>
      <td>14/31</td>
      <td>8.02E-27</td>
      <td>3/31</td>
      <td></td>
      <td>Alpha(1 -&gt;6) mannosyltransferase</td>
      <td></td>
    </tr>
    <tr>
      <td>accA1*</td>
      <td>sense</td>
      <td>598</td>
      <td>13/25</td>
      <td>4.65E-26</td>
      <td>6/25</td>
      <td>Rv0339c</td>
      <td>Probable acetyl-/propionyl-coenzyme A carboxylase alpha chain</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>Rv3282*</td>
      <td>antisense</td>
      <td>325</td>
      <td>12/18</td>
      <td>4.93E-26</td>
      <td>0/18</td>
      <td></td>
      <td>putative nucleoside-triphosphate diphosphatase</td>
      <td></td>
    </tr>
    <tr>
      <td>fadE7*</td>
      <td>sense</td>
      <td>1069</td>
      <td>13/43</td>
      <td>3.09E-22</td>
      <td>8/43</td>
      <td>Rv3488</td>
      <td>Acyl-CoA dehydrogenase FadE7</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>pks9*</td>
      <td>sense</td>
      <td>2728</td>
      <td>13/50</td>
      <td>2.93E-21</td>
      <td>3/50</td>
      <td>Rv0023</td>
      <td>polyketide synthase Pks9</td>
      <td></td>
    </tr>
    <tr>
      <td>bioB</td>
      <td>sense</td>
      <td>796</td>
      <td>11/49</td>
      <td>2.04E-17</td>
      <td>0/49</td>
      <td>Rv1049</td>
      <td>biotin synthetase</td>
      <td></td>
    </tr>
    <tr>
      <td>treZ*</td>
      <td>upstream</td>
      <td>880</td>
      <td>8/13</td>
      <td>2.46E-17</td>
      <td>5/13</td>
      <td></td>
      <td>Maltooligosyltrehalose trehalohydrolase</td>
      <td></td>
    </tr>
    <tr>
      <td>Rv1461*</td>
      <td>antisense</td>
      <td>416</td>
      <td>10/50</td>
      <td>2.08E-15</td>
      <td>2/50</td>
      <td></td>
      <td>Iron-sulfur cluster assembly protein</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>Rv1278</td>
      <td>sense</td>
      <td>1469</td>
      <td>9/44</td>
      <td>4.25E-14</td>
      <td>1/44</td>
      <td></td>
      <td>Putative transport protein</td>
      <td></td>
    </tr>
    <tr>
      <td>aldA</td>
      <td>antisense</td>
      <td>642</td>
      <td>8/48</td>
      <td>6.49E-12</td>
      <td>0/48</td>
      <td>Rv3830c</td>
      <td>Probable NAD-dependent aldehyde dehydrogenase AldA</td>
      <td></td>
    </tr>
    <tr>
      <td>Rv0370c</td>
      <td>antisense</td>
      <td>389</td>
      <td>8/50</td>
      <td>9.17E-12</td>
      <td>0/50</td>
      <td></td>
      <td>Possible oxidoreductase</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>frdA*</td>
      <td>antisense</td>
      <td>787</td>
      <td>8/51</td>
      <td>1.08E-11</td>
      <td>0/51</td>
      <td></td>
      <td>Probable fumarate reductase FrdA</td>
      <td></td>
    </tr>
    <tr>
      <td>PPE34*</td>
      <td>sense</td>
      <td>3454</td>
      <td>4/4</td>
      <td>1.39E-10</td>
      <td>2/4</td>
      <td></td>
      <td>PPE family protein PPE34</td>
      <td></td>
    </tr>
    <tr>
      <td>Rv1251c</td>
      <td>antisense</td>
      <td>1309</td>
      <td>7/46</td>
      <td>2.69E-10</td>
      <td>1/46</td>
      <td></td>
      <td>Putative ester hydrolase</td>
      <td></td>
    </tr>
    <tr>
      <td colspan="9">MamB</td>
    </tr>
    <tr>
      <td>PE_PGRS54</td>
      <td>sense</td>
      <td>112</td>
      <td>10/68</td>
      <td>8.16E-24</td>
      <td>N/A</td>
      <td>Rv0767c</td>
      <td>PE-PGRS family protein PE_PGRS54</td>
      <td></td>
    </tr>
    <tr>
      <td>PE_PGRS57</td>
      <td>sense</td>
      <td>112</td>
      <td>9/68</td>
      <td>3.94E-21</td>
      <td>N/A</td>
      <td>Rv0767c</td>
      <td>PE-PGRS family protein PE_PGRS57</td>
      <td></td>
    </tr>
  </tbody>
</table>

MamA and HsdM are palindromic, each targeting both a motif and its reverse complement (Zhu et al., 2016). Thus, every adenine methylated by these enzymes comes with a potentially methylated partner on the opposite strand. HsdM palindromic pairs were mostly hypomethylated together. In contrast, many MamA motif pairs were hemimethylated, with one site consistently hypomethylated and the other frequently methylated (Table 1). Site-specific hemimethylation functions as part of multiple characterized processes in other bacterial species (Braun and Wright, 1986; Roberts et al., 1985) but what role it serves in M. tuberculosis, if any, remains unknown.

### Sequence contexts of most hypomethylated sites are consistent with transcription factor occlusion

In other bacteria, hypomethylation has been attributed to transcription factors occluding MTase access to DNA when their respective target motifs overlap (Beaulaurier et al.; Hernday et al., 2002; Stephenson and Brown, 2016). To determine if this may be the case in M. tuberculosis, we scanned the context sequence of each consistently hypomethylated site for TFBS motifs previously characterized in M. tuberculosis (Minch et al., 2015). All 58 consistently hypomethylated HsdM loci matched at least one significant TFBS motif (p-value<0.0001, converted log-likelihood ratio score), suggesting transcription factor occlusion was responsible. In contrast, only 14 of the 34 consistently hypomethylated MamA loci significantly matched a TFBS motif (p-value<0.0001, converted log-likelihood ratio score; Table 1). The abundance of TFBS matches at HsdM motif loci may be due to the lower stringency of its motif (HsdM: GATNNNNRTAC, MamA: CTGGAG). Notably, the TFBS motif of oxidation-sensing regulator mosR (Rv1049) (Peterson et al., 2014) matched multiple hypomethylated MamA and HsdM loci, and the mosR gene itself had a hypomethylated MamA locus 7 bp upstream of its TSS (Table 1).

One particularly intriguing example of site-specific hypomethylation was cobK 304, the HsdM motif site 304 bp inside the gene cobK. This locus was hypomethylated in 50/68 HsdM-active isolates (Table 1). The IPD ratio at cobK 304 across HsdM-active isolates was bimodal (Figure 5A), supporting this finding. The 18 cobK 304 methylated isolates were all IO and grouped together in our phylogenetic tree (Figure 5B). The context sequence around cobK 304 matched the binding site motif of transcription factor mntR (Rv2788) (q-value = 0.0136, Table 1), a manganese dependent repressor (Pandey et al., 2015). This could explain the 50 cobK 304 hypomethylated isolates. If mntR bound to that site, it could prevent HsdM from methylating it. Meanwhile, genotyping mntR revealed that all 18 IO isolates shared the variant mntR Q131* (Figure 5B), a nonsense mutation found previously in IO isolates (Gomez-Gonzalez et al., 2019) that truncates MntR. This truncation could explain why cobK 304 was methylated in all 18 IO isolates.

![Figure 5.](https://cdn.elifesciences.org/articles/58542/elife-58542-fig5-v1.jpg)

**Figure 5.:** (A) Histogram showing the distribution of IPD ratios at the HsdM motif locus cobK:304, 304 bp downstream from the start codon of gene cobK. Included isolates have active HsdM and possess the HsdM target motif at the cobK:304 locus. IPD ratios are normalized to the mean IPD ratio of adenine bases in their respective isolates (excluding bases targeted by known MTase motifs) and log2-transformed. The histogram uses a bin width of 0.1. Red bars count isolates classified as ‘hypomethylated’ at the cobK site, while mint bars count isolates classified as methylated at the site. (B) Phylogenetic tree of the 90 clinical and reference M. tuberculosis isolates and 3 M. africanum isolates included in this study, along with outgroups M. bovis and M. canetti. Isolates are colored in the middle ring by their methylation status at the HsdM motif site cobK:304. Red isolates are classified as hypomethylated at the cobK site; green isolates are classified as methylated at the site, and gray isolates either have an inactive HsdM methyltransferase, or are missing the HsdM target motif 304 bp within their cobK gene. Isolates are colored in the outer ring by the genotype of their mntR (Rv2788) gene. mntR encodes for a transcription factor whose binding motif matches the context sequence of the cobK 304 site (p = 2.63×10−5, converted log-likelihood ratio score). Gold isolates had the variant mntR Q131STOP, a nonsense mutation that introduces an early stop codon that truncated the gene and presumably removed its function. The blue isolates do not have a nonsense mutation, though one isolate had the missense mutation mntR P149L.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/58542/elife-58542-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** (A) MamA, (B) HsdM, and (C) MamB. Methyltransferase (MTase) target bases in each of 93 single-molecule real-time (SMRT) sequenced clinical isolates were classified as methylated (not shown), hypomethylated, or indeterminate based on their sequencing kinetics. Stacked histograms depict the proportion of motif sites (y-axis) classified as hypomethylated (red) or indeterminate (purple) in each isolate (each bar represents an isolate, x-axis). Isolates are sorted (right to left) by the proportion of hypomethylated motifs. Only isolates with an active genotype for each MTase are included in the histograms.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/58542/elife-58542-fig5-figsupp2-v1.jpg)

**Figure 5—figure supplement 2.:** Histograms depicting the distribution of IPD ratios among bases within the target motifs of known methyltransferases HsdM, MamA, and MamB, after normalizing the IPD ratios of each base to the mean IPD ratio of all adenines within the isolate, and log-transforming the data. The bin width is 0.1 and the bars are labeled by the Bayesian classification of each base. The isolate shown is a clinical strain of M. tuberculosis with an active genotype of all three methyltransferases.

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/58542/elife-58542-fig5-figsupp3-v1.jpg)

**Figure 5—figure supplement 3.:** Violin plots showing the distribution of coverage at MTase motif sites, aggregated from all clinical isolates. Only MTase sites whose respective MTase had an active genotype in their respective isolate were included. MTase sites that were classified as Indeterminate by the Bayesian classifier were grouped separately (purple) from the remaining sites (gray). The MTase sites with a definitive classification call had a higher mean coverage (68.2) than the MTase sites called Indeterminate (54.7), significant at 0.01 confidence level (Welch’s two sample t-test, p<2.2×10−16, one sided).

Close proximity between MTase motif sites can also cause bacterial hypomethylation (Casadesús and Low, 2013), wherein methylation of one site is negatively associated with the other, often forming a regulatory switch. To find evidence of this phenomenon in M. tuberculosis, we scanned consistently hypomethylated loci for nearby MTase motifs on the same strand (Table 1), including locus cobK 304. In most isolates, cobK 304 was only 8 bp distant from another HsdM site, cobK 312 (together making four palindromic motif matches within cobK). In these isolates, cobK 312 was methylated while cobK 304 was hypomethylated. However, in IO isolates the HsdM motif at cobK 312 was disrupted by a nearby deletion. If MTase crowding was responsible for the hypomethylation of cobK 304, then the removal of cobK 312 in IO isolates may be responsible for cobK 304 methylation in that lineage. As cobK 304 was consistent with both previously described phenomena, it is uncertain whether its hypomethylation was caused by its neighboring MTase motif, or by occlusion by transcription factor MntR.

### DNA adenine methylation is widespread and distinctly patterned at promoters

Next, we systematically probed promoters with MTase motif sites to identify common configurations between motif sites and characterized TSSs (Cortes et al., 2013; Shell et al., 2015). Within promoter regions (≤50 bp upstream from the TSS), targeted adenines of MamA and HsdM motifs had distinct peaks at the edges of the −10 element (Figure 6A). The MamA peak comprised 22 promoters coincident with the −10 element in the configuration that has been shown previously to modulate transcription (Shell et al., 2013) (4–5 and 7–8 bp upstream from TSS, Figure 7). These included the four shown to affect transcription (Figure 7, blue stars). Notably, none of these four were hypomethylated or hypervariable, indicating that lack of anomalous methylation in vitro does not preclude a role in transcriptional regulation. Common (n ≥ 75) HsdM motif sites overlapped with the −10 element of 33 promoters. While nineteen of these match those recently reported (Chiner-Oms et al., 2019), 13 are novel. These HsdM motif sites frequently overlap with the −10 promoter element in a configuration analogous to that common in MamA motifs, but on the distal (−10 to −13 bp) end (Figure 8). In total, 212 genes have common (in ≥75 isolates) promoter MTase motif sites (Supplementary file 6).

![Figure 6.](https://cdn.elifesciences.org/articles/58542/elife-58542-fig6-v1.jpg)

**Figure 6.:** (A) Consistent MTase-SFBS-promoter configuration. Number of promoters with MTase motif sites (in ≥ 50 isolates) by distance upstream of TSSs, for each MTase. The canonical SigA −10 element binding motif is superimposed for conceptual clarity, all motif sites within the −7 to −12 bp window upstream of annotated TSSs are included, irrespective of SFBS overlap. MTase Motifs for overrepresented configurations (peaks) are shown in the orientation and positions that explain the observed peaks. (B) The number of promoters with the −10 element overlapping an MTase motif site (≥30 isolates), for each MTase and sigma factor. (C) Stacked histograms of the number of genes harboring promoter motif sites for each MTase. Darker shades indicate overlap with progressively more substantiated overlap with promoter elements. In ‘full promoters’ MTase motifs overlapped a SFBS that is part of a classical promoter architecture (Materials and methods); ‘Element’ matches overlap either the −10 or −35 SFBS the expected distance from the TSS but have neither an extended −10 promoter element nor the complementary element; ‘Location’ matches are the distance upstream of the TSS expected to overlap with −10 or −35 elements but do not overlap known SFBS motifs; ‘Sequence’ matches coincide with SFBSs but not in the expected position with respect to TSS; ‘none’ are ≤ 50 bp upstream of a TSS but meet none of the aforementioned criteria. (D) Variability (SD of log2 (IPD Ratio) across isolates) across isolates with active MTase (y-axis) for common (≥75 isolates) promoter motifs and their distance upstream of the TSS (x-axis). Downstream genes of hypervariable motif sites (≥3 SD above the mean MamB variability, red). (E) Genes with annotated HsdM promoter motifs integrated with a recent ΔHsdM differential expression (DE) study (Chiner-Oms et al., 2019). All HsdM promoter motifs plotted by position within the promoter (x-axis) and Benjamini-Hochberg adjusted -log10 (p-value) for DE (y-axis). Downstream genes of motif sites of significantly DE genes (red, BH-adjusted p≤0.05) genes overlapping the −10 element (7 to 13 bp upstream of TSS) are labeled. The two genes without overlapping sites the −10 element have both their motif sites labeled (if within 50 bp).

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/58542/elife-58542-fig6-figsupp1-v1.jpg)

**Figure 6—figure supplement 1.:** Histogram bar height corresponds to the number of TSSs harboring an overlap MTase motif-SFBS at that position. Only those appearing in at least 40 isolates are depicted. Bar color represents whether the SFBS motif was for a −35 or −10 element. The −10 and −35 regions are highlighted with dashed vertical lines in each plot.

![Figure 7.](https://cdn.elifesciences.org/articles/58542/elife-58542-fig7-v1.jpg)

**Figure 7.:** Heatmap depicting degree of methylation (scaled log2 of IPD ratio averaged across reads) across all 93 clinical isolates (columns) at all common (present in ≥ 75 isolates) MamA promoter (≤50 bp upstream of a TSS) motif sites (rows). The coloring scale of the heatmap boxes max out at the median scaled IPD across all motif sites across all isolates with active MamA allele and bottom out at 0 (corresponding to no methylation). For each isolate, HsdM activity (bottom) and lineage (top) are indicated. Isolates within each heatmap are sorted first by activity, and then by lineage. MamA motifs in configuration with −10 promoter element akin to that of the promoters shown to exhibit MamA-methylation-dependent transcriptional response under hypoxia (Shell et al., 2013) (blue pop-out) and those within a region with a high density of hypervariable sites (red pop-out) are highlighted. Color of axis labels highlights the specific motif sites shown by Shell and colleagues to affect transcriptional response to hypoxia (Shell et al., 2013) (blue) and motif sites hypervariable across isolates with active MamA (red).

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/58542/elife-58542-fig7-figsupp1-v1.jpg)

**Figure 7—figure supplement 1.:** All are either transcriptional regulators or involved in clinically relevant processes. These genes mediate known intrinsic and acquired resistance and mechanisms, induction and maintenance of dormancy, and metal ion homeostasis. ‘MamA −10 element’ refers to the configuration described by Shell and colleagues (Shell et al., 2013) while ‘HsdM −10 element’ refers to the analogous configuration, where targeted adenines within HsdM motifs coincide with the distal end of the −10 promoter element.

![Figure 8.](https://cdn.elifesciences.org/articles/58542/elife-58542-fig8-v1.jpg)

**Figure 8.:** Similar to Figure 7 but for HsdM motif sites. Heatmap depicting degree of methylation (scaled log2 of IPD ratio averaged across reads) across all 93 clinical isolates (columns) at all common (present in ≥ 75 isolates) HsdM promoter (≤50 bp upstream of a TSS) motif sites (rows). The coloring scale of the heatmap boxes max out at the median scaled IPD across all motif sites across all isolates with an active HsdM allele and bottom out at 0 (corresponding to no methylation). For each isolate, HsdM activity (bottom) and lineage (top) are indicated. Isolates are sorted first by activity, and then by lineage. ‘Putative SFBS-overlapping sites’ are those with an analogous configuration with the −10 promoter element shown the MamA motif overlap highlighted in Figure 7, but overlapping the end of the −10 promoter element distal to the TSS, rather than the proximal end. ‘Partner sites’ are loci at the position that includes the palindromic partners of putative SFBS-overlapping sites. Promoter MTase motif sites with hypervariable kinetics across HsdM-active isolates (red text) or upstream of genes differentially expressed in HsdM knockout (blue stars) are indicated. Isolates with convergent methylation levels at a subset of notable loci despite having divergent HsdM genotypes and belonging to different lineages are indicated by asterisks (*).

Next, we scanned for SFBS motifs overlapping promoter MTase motif sites. Sigma factors SigA and SigB overlapped MTase motif sites most frequently (Figure 6B), though SigC, SigD, SigI, and SigF overlapped motif sites as well (Figure 6—figure supplement 1, Supplementary file 6). MamB motif sites rarely overlapped SFBSs, while orphan MTase motif sites frequently did (Figure 6A–C). MamA motif sites were more frequent in promoter regions than HsdM sites, however HsdM sites more frequently overlapped a SFBS (Figure 6B, perhaps explainable by both HsdM and SigA target motifs including the dinucleotide ‘TA’). The −10 promoter element guides formation of transcription initiation complexes (Browning and Busby, 2016), and DNA methylation alters biophysical properties that tune promoter strength (Polaczek et al., 1998) (DNA melting temperature Gries et al., 2010 and DNA bending during open complex formation Saecker et al., 2002). This mechanism is particularly plausible for MTase motifs that overlap SigA SFBSs (Figure 6B). SigA is a sigma-70 homolog, which contacts the −10 promoter element at positions −7 through −12 upstream of the TSS (Feklistov and Darst, 2011), precisely where overlap with HsdM and MamA-methylated adenines are frequent (Figure 6). These findings provide a potential mechanism for cis-regulation of dozens of genes with orphan MTase motifs in M. tuberculosis.

Promoters of fifteen genes harbored hypervariable motif sites. Most (11/15) were hypervariable in both palindromic sites (Figure 6D). Seven motif sites comprise a cluster of hypervariable MamA motif sites in the spacer between the −10 and −35 promoter elements (19–24 bp range, Figure 7). While this region does not overlap with SFBSss, transcriptional effectors commonly bind here to tune gene expression (Newberry and Brennan, 2004; Pandey et al., 2015), providing a candidate mechanism driving the differences between strains and mechanistic plausibility for transcriptional influence at these sites. No MamB promoter motif sites were hypervariable (Figure 6C), consistent with a classic RM-system without regulatory roles, once again contrasting with the signatures of gene regulation present at orphan MTase sites.

### HsdM promoter methylation is associated with transcription levels of downstream genes

Notably, Rv1813c is hypervariable and has a motif site 11 bp upstream of its TSS, overlapping a SigA SFBS. Rv1813c was recently reported to be significantly under-expressed following ΔhsdM, but the authors did not identify the SigA overlap with this motif site in the Rv1813c promoter (Chiner-Oms et al., 2019). This discovery prompted us to re-evaluate the ΔhsdM differential expression results recently reported to have no direct influence on transcription at methylated promoters. In that work, the authors defined ‘differentially expressed’ genes using thresholds on both significance (adjusted p-value≤0.05) and magnitude (|log2-foldchange| ≥ 1). Since we were interested in the mechanism (Does HsdM promoter methylation have the capacity to influence transcription?) rather than the magnitude of its effect, we defined differentially expressed genes according only to significance. With these criteria, 310 genes (Figure 6—source data 4, Supplementary file 7) were differentially expressed between hsdMWT and ΔhsdM (ΔhsdM-DE). Genes with HsdM motif sites in their promoters (n = 11) were significantly enriched among ΔhsdM-DE genes (p = 0.000215, OR = 4.47, 95% CI: 1.99–9.37, two-tailed Fisher’s Exact; Figure 6E). Therefore, we conclude that HsdM promoter motifs are associated with expression change following HsdM knockout, though the magnitude of the effect is subtle in vitro (|log2-foldchange| ≤ 1.16).

Nine of these 11 ΔhsdM-DE genes with HsdM promoter motifs overlapped with the −10 promoter element (Figure 6E), suggesting a direct effect on transcription analogous to the configuration for MamA previously described (Shell et al., 2013). Within these nine are 3 of the four genes with hypervariable HsdM-methylation in promoter motifs, suggesting that differential selection on the methylome during growth in vitro may affect gene expression.

## Discussion

Here, we assembled, annotated, and investigated DNA adenine methylomes of 93 M. tuberculosis complex (MTBC) clinical isolates from patients in high TB-burden countries (Figure 1), the largest survey of methylomic diversity in the MTBC to date. Through functional, comparative, integrative, and heterogeneity analyses of these methylomes, we identified drivers and sites of variability in DNA adenine methylomes across the MTBC. Mapping DNA methyltransferase (MTase) variants to methylomic data expanded the allele-function mappings for the three known MTBC DNA adenine methyltransferases (Supplementary file 1), clarified several disputed or errant reports of MTase function (Chiner-Oms et al., 2019; Phelan et al., 2018; Shell et al., 2013; Figure 2—figure supplement 1), and determined that the MTase variants mamAE270A, mamAG152S, and mamBK1033T conferred partial MTase activity (Figure 2). Heterogeneity analysis revealed that these three alleles drive intracellular stochastic methylation (Figure 3A–G), conferring Intercellular Mosaic Methylation (IMM) to 38/93 studied isolates, including 34/36 EAS isolates (Supplementary file 2). Comparative methylomic analysis identified subsets of motif sites consistently hypomethylated (Table 1, Supplementary file 5) and hypervariable across isolates (Figure 4, Supplementary file 4). Functional and integrative analyses uncovered previously unreported promoters harboring methylation motif sites (Figures 6–8, Supplementary file 6), implicating clinically important phenotypes as potentially regulated by DNA adenine methylation (Figure 7—figure supplement 1, Supplementary file 6), and put forth evidence that HsdM promoter methylation directly influences transcription methylation (Figure 6E), contradicting conclusions from previous work (Chiner-Oms et al., 2019). These findings add to the growing body of literature demonstrating bacterial epigenomics is an important complementary focus to genetic and phenotypic analysis in studying microbial diversity, gene regulation, and evolution.

Sequencing kinetics of MTase target motif sites indicated heterogeneous methylation in isolates with MTase variants mamAE270A, mamAG152S, and mamBK1033T (Figure 2A). Read-level kinetic analysis confirmed this heterogeneity, and characterized the phenomenon as intracellular stochastic methylation, rather than phase-variable methylation (Figure 3). Further heterogeneity analysis demonstrated that methionine starvation can induce intracellular stochastic methylation in isolates with wild-type MTase activity (Figure 3—figure supplement 1). In stochastic methylation, the methylation status of each MTase target site varies independently between cells (Beaulaurier et al., 2015). The resulting subpopulations thus carry diverse combinations of methylated and unmethylated sites, a phenomenon we have termed ‘intercellular mosaic methylation’ (IMM, Figures 3 and 9). Thus, the potential diversity of DNA methylation patterns in IMM across cells scales logarithmically with the number of motif sites targeted by the MTase exhibiting IMM.

![Figure 9.](https://cdn.elifesciences.org/articles/58542/elife-58542-fig9-v1.jpg)

**Figure 9.:** Conceptual illustration contrasting DNA methylome diversification and epigenetic inheritance between IMM and other mosaic-like mechanisms of heterogeneous DNA adenine methylation. (A) Cartoon illustrating the nature of methylomic diversity depicts individual cells’ chromosomes (gray bars) with methylation motifs (ovals). Oval colors represent distinct DNA methyltransferases (MTases). *Practically infinite, estimated as 21,978 (there are roughly 1,978 MamA motif sites per replisome) under the assumption that methylation propensity on the daughter strand is independent from methylation status of other motif sites on the daughter strand and parent strand. **Assumes there are two phases. Some phase-variable MTases with more than two phases have been described. In these cases, potential states would be equivalent to the product of the sequence of numbers of phases for all independent phase-variable MTases. ***Calculated by Furuta and Kobayashi as the product of 1,000 DNA sequence specificities per MTase across 5 MTases in Helicobacter pylori (Furuta and Kobayashi, 2012). (B) Diagram illustrating the relationship between daughter and parent strains as it relates to conservation of the whole methylome (top) and at a single methylation site (bottom). Under the assumption of genuine stochasticity, IMM would practically never re-pattern the daughter strand identically to its parent. In contrast, the methylation status at any given methylation site would match between parent and daughter cells in 50% of cases.

This is not the first report of mosaic-like patterning of DNA adenine methylation in prokaryotes. Mosaicism can result from independent ON/OFF switching of multiple phase-variable MTases (Atack et al., 2018) or from domain movement of the target recognition domain (TRD) (Furuta and Kobayashi, 2012), a phenomenon known as ‘DoMo’ (Furuta et al., 2014). However, IMM departs from these two previously described types of mosaic-like methylation heterogeneity in two important respects. First, in the degree of methylomic diversity it generates (Figure 9A). Just as independent state-changes of multiple modification enzymes (Casadesús and Low, 2013) increases the diversity of epigenetic bacterial lineages beyond that of individual phase variation systems, IMM extends this diversity further still, scaling logarithmically with the number of motif sites targeted by the stochastic MTase. In nature, the set of methylation states that manifest may be constrained below this theoretical set by a variety of mechanisms, such as interaction with DNA-binding proteins, or switch-like behavior between proximal MTase sites (Casadesús and Low, 2013). Nonetheless, the number of adoptable states is large enough that states are practically certain to differ between parent and daughter cells. Second, IMM is distinct in the pattern of epigenetic inheritance from parent to daughter cell (Figure 9B). In mosaic-like methylomes driven by independent switching of phase-variable MTases (canonically a frameshift) and DoMo (Furuta et al., 2014) (via homologous recombining of TRDs) the methylome-patterning determinant is passed genetically to the daughter strand, unless there is a phase change (Sánchez-Romero and Casadesús, 2020). IMM lacks a genetic basis for transgenerational methylome inheritance and no epigenetic mechanism of inheritance for IMM in M. tuberculosis is known at present. Consequently, our current knowledge suggests a greater degree of methylomic diversity is spread throughout the population in each replication event, but that any advantageous methylation patterns would lack a stabilizing mechanism. This apparent differential capacity to produce epigenetic lineages assumes that in IMM, the methylation status of parent strand motif sites has no effect on the probability of daughter strand motif sites being methylated. Empirically testing this assumption would refine our understanding of the implications IMM has for adaptive evolution.

Transcriptional influence by DNA adenine methylation is prevalent among human pathogens (Casadesús and Low, 2013). Previous study of M. tuberculosis genes with MamA-methylated promoters demonstrated that DNA adenine methylation directly influences the expression of genes with MamA target motifs in their promoters (Shell et al., 2013). Our promoter annotation expands the set of promoters potentially regulated by MamA-methylation (Figure 7, Supplementary file 6) and our ΔhsdM-DE analysis (Figure 6E) strongly suggests that HsdM-methylation at promoters directly influences transcription. This provides a potential mechanism in M. tuberculosis for heterogeneous methylation to produce heterogeneous phenotypes.

The physiological consequences of mycobacterial gene expression control by DNA methylation, however, remain to be identified. Therefore, the adaptive benefits of phenotypic heterogeneity ostensibly conferred by IMM remain hypothetical. Theoretical grounds for phenotypic heterogeneity to confer survival benefits have been described previously (Wolf et al., 2005), as have examples of adaptive phenotypic heterogeneity driven by DNA methylation in bacterial pathogens (Atack et al., 2018; Low and Casadesús, 2008). The adaptive benefit of any epigenetically influenced process depends on the degree to and manner in which it is heritable across generations. In the absence of an identified mechanism favoring self-perpetuity, our description of IMM provides bacterial populations with a means for retaining adaptive methylation patterns, but not for amplifying them. Without heritability, IMM-driven phenotypic heterogeneity could still confer adaptive benefit through a ‘bet-hedging’ strategy (Casadesús and Low, 2013; Wolf et al., 2005). This hypothesis is consistent with observations of M. tuberculosis ‘persister cells’ (Vilchèze et al., 2017), minority groups that are pre-adapted to tolerate initial exposure to macrophage (Daniel et al., 2011) and drug pressure (Keren et al., 2011), by entering dormancy (Jain et al., 2016) or activating efflux pumps (Colangeli et al., 2005; Mustyala et al., 2016).

Future work examining changes in methylation patterns in strains with IMM-conferring MTases under selective pressure would help determine whether DNA adenine methylation patterns are heritable in M. tuberculosis, and whether IMM is compatible with the hypothesis of ‘epigenetic-driven adaptive evolution’ (Furuta and Kobayashi, 2012). The hypervariability of numerous orphan MTase loci (n = 344, Supplementary file 4) could be taken to imply differential selection of methylation patterns across isolates (in vitro). Two observations provide circumstantial evidence in support of this interpretation. First, hypomethylation (which coincides with many hypervariable sites, Table 1, Supplementary files 4 and 5) is a signature of epigenetic regulation in prokaryotes (Blow et al., 2016), suggesting genes with hypervariable promoter motif sites (n = 11, Figures 6–8) are epigenetically regulated, providing a potential basis for differential selection across strains. Second, several sites are methylated at similar levels between three EAS isolates and a genetically distant (SNP distance ≥ 2,722) M. africanum isolate (Figures 4A and 8) suggesting convergent epigenomic selection in vitro. This convergence was not driven by MTase genotype, as the isolates had discordant HsdM alleles. Notably, convergently methylated sites between these isolates included ΔhsdM-DE persistence (raaS) and dormancy (Rv1813c and glpX) genes (Figure 6), suggesting methylation at these sites affect promoter strength and raising the possibility that these methylation patterns have important phenotypic consequences. However, both these observations may be due to a secondary effect, such as MTase antagonism driven by mutations in DNA-binding proteins, as we observed at cobK 304 (Figure 5), or some other primary factor. Taken together, the evidence from this work is insufficient to conclude that any sites are under epigenetic selection.

Our promoter methylation analysis produced different results than a recently published analysis (Chiner-Oms et al., 2019) and reached opposing conclusions for the role of HsdM in regulating promoter strength. While the authors conclude that ‘methylation seems to play a minimal role in shaping in-vitro gene expression’, integration of our HsdM motif-harboring promoters with their ΔhsdM RNAseq data shows a clear association between HsdM promoter methylation and in vitro gene expression (Figure 6E). We believe differences in approach drove our disparate conclusions. For their analysis, Chiner-Oms and colleagues relied on reference-mapping and a single source of TSSs, and they focused on SigA motifs to identify promoter MTase motifs (Chiner-Oms et al., 2019). In contrast, we transferred TSS annotations from two M. tuberculosis transcriptomic studies (Cortes et al., 2013; Shell et al., 2015) to contiguous regions of finished de novo assemblies, and scanned for SigA-SigM SFBS motifs (Chauhan et al., 2016) and promoters lacking known SFBSs. These differences explain why our analysis captured the association between HsdM-methylation and expression of downstream genes.

By integrating DNA adenine methylomes with fully-annotated genome assemblies and TSS-mapping data, this work generates a corpus of putative interactions between DNA methylation and regulatory effectors (Supplementary files 4–7), providing a basis for generating specific, testable functional hypotheses for DNA adenine methylation in M. tuberculosis. The functions of genes with promoter motif sites that were hypervariable (Figures 7 and 8, Figure 7—figure supplement 1) or in stereotyped configurations with −10 promoter elements (Figures 6 and 8; Supplementary file 6) implicate clinically important processes as under control of DNA adenine methylation (Supplementary files 1 and 6, Figure 7—figure supplement 1). These include drug resistance, metal ion homeostasis (corA (Park et al., 2019), lpqS (Darwin, 2015), mmpS4 (Jones et al., 2014), higA (Schuessler et al., 2013), mbtJ (Chownk et al., 2018), and hemN McMahon et al., 2012), and the induction and maintenance of dormancy—all functions with examples of modulation by DNA adenine methylation in other human pathogens (Beaulaurier et al.; Brunet et al., 2020; Cohen et al., 2016; Sánchez-Romero and Casadesús, 2020). The resistance-implicating genes among these mediate resistance through gene regulation (whiB7-controlled expression of eis, tap, and Rv1473 (Duan et al., 2019; Morris et al., 2005), and raaS-controlled expression of Rv1218c and Rv1217c Wang et al., 2013), drug efflux (drrA (Mustyala et al., 2016), iniA (Colangeli et al., 2005), Rv3728 (Gupta et al., 2010), and efflux-targets of whiB7 and raaS), and other mechanisms (glf (Chen and Bishai, 1998), mshC (Parida et al., 2015), mshD (Vilchèze et al., 2008), pafA (Samanovic and Darwin, 2016), Rv3050c (Nieto R et al., 2018), and gyrB (Nosova et al., 2013).

Our finding that most (34/36, Supplementary file 2) Beijing clinical isolates exhibited constitutive IMM prompts the question of whether IMM might contribute to their global success. Methylated promoters implicate some hallmarks of the Beijing sublineage: facile dormancy induction, increased host-lipid utilization, TAG accumulation in aerobic environments (Reed et al., 2007), and increased synthesis of cell envelope components and virulence lipids (Huet et al., 2009; Figure 7—figure supplement 1, Supplementary file 6). While some of these hallmarks have been attributed to genetic factors, such as higher basal expression of the DosR-regulon (Reed et al., 2007), gaps remain in our understanding. One hypothesis is that, in Beijing isolates, MamAE270A-driven mosaicism confers phenotypic heterogeneity, thereby enabling access to a greater number of phenotypic solutions during adaptive evolution. This hypothesis could be investigated by exposing MamAWT and MamAE270A mutants to different selection pressures and comparing evolutionary outcomes and methylomes of the adapted strains.

We cannot extrapolate directly from the DNA methylation patterns we report here to what occurs during infection. Sequencing kinetics are measured from DNA extracted after extensive culturing, during which any methylomic adaptation to the host environment may have changed. Directly sequencing from patient specimens would be ideal to assay DNA methylation patterns in vivo, but DNA input requirements necessitate culturing prior to DNA extraction (PACBIO, 2013), as DNA amplification erases epigenetic markings. Studying methylomic adaptation to host-like conditions (e.g. hypoxia, host-lipids as carbon source) can reveal context-dependent selection of methylation patterns, and time-course serial sequencing could characterize the dynamics of their selection. Coupling these sequencing studies with transcriptomic, proteomic, and phenotypic assays could clarify the relationship between DNA adenine methylation, gene expression, and phenotype.

Throughout this manuscript we have referred to the DNA adenine methyltransferase encoded by Rv2756c as HsdM (hsdM for the gene) and its specificity subunit encoded by Rv2761, as HsdS (hsdS for the gene) to be consistent with previous work (Shell et al., 2013). It appears that Rv2756c was originally referred to as HsdM based on homology to hsdM in R-M systems—before the existence of its restriction component had been investigated—and has propagated through subsequent studies (Chiner-Oms et al., 2019; Gomez-Gonzalez et al., 2019; Phelan et al., 2018; Zhu et al., 2016). However, it has since been determined that Rv2756c lacks a functional HsdR component (Zhu et al., 2016). According to the prevailing nomenclature conventions, the symbol ‘hsd’ is for Type 1 R-M systems (Loenen et al., 2014; Roberts et al., 2003), which Rv2756c is not part of, since it lacks a functional restriction component. Therefore, we propose that the orphan methyltransferase encoded by Rv2756c be renamed to MamC (mamC for the gene) Mycobacterial Adenine Methyltransferase C (since MamA and MamB are assigned to other mycobacterial DNA adenine methyltransferases). Likewise, we propose that the specificity subunit of MamC encoded by Rv2761 be renamed to mamS/MamS (formerly hsdS/HsdS) and the specificity subunit fragment encoded by Rv2755 (formerly hsdS.1/HsdS.1) to mamS.1/MamS.1. This proposed nomenclature retains the S and S.1 from hsdS and hsdS.1, is consistent with the extant naming convention of MamA and MamB, and removes the erroneous implication that HsdM/HsdS/HsdS.1 are part of a Type 1 R-M system.

This integrative analysis of 93 clinical isolates’ DNA adenine methylomes spotlights DNA methylation as a fundamental source of diversity in the MTBC. The results provide a basis for further investigation of the roles played by DNA adenine methylation in M. tuberculosis’ physiology and adaptive evolution. In particular, the discovery of constitutive IMM-driven by MTase genotype raises the possibility that DNA adenine methylation translates into differences in adaptive capacity between MTBC strains.

## Materials and methods

### Isolate acquisition and inclusion criteria

MTBC colonies were isolated from sputa of 154 tuberculosis patients, originating from Hinduja National Hospital (PDHNH) in Mumbai, India; Phthisiopneumology Institute (PPI) in Chisinau, Moldova; Tropical Disease Foundation (TDF) in Manila, the Philippines; The National Health Laboratory Service of South Africa (NHLS) in Johannesburg, South Africa; and World Health Organization Supranational References Laboratories in Stockholm, Sweden and Antwerp, Belgium (PRJNA555636). Of these 154 isolates, 113 were originally collected by the Global Consortium for Drug-resistant Tuberculosis Diagnostics (Hillery et al., 2014) and chosen for resequencing.

We also included two technical replicate control runs of avirulent reference strain H37Ra reported in a previous paper (PRJNA329548) (Elghraoui et al., 2017). An additional 24 publicly available SMRT-sequencing reads of clinical M. tuberculosis and M. africanum isolates were downloaded from the Sequence Read Archive, along with a triplicate run of virulent type strain H37Rv, and triplicate samples of a metA knockout strain of H37Rv before and after five days of methionine starvation (PRJEB8783) (Berney et al., 2015).

Of these isolates, 97 clinical M. tuberculosis isolates, 3 M. africanum isolates, and nine reference strains passed assembly quality control. Of them, seven clinical isolates and one metA knockout isolate failed our methylome pipeline (five isolates had multiple contigs and three isolates had position inconsistencies between their kinetics data and consensus sequence FASTA file). In total, our downstream analysis included 93 MTBC clinical isolates (including 3 M. africanum) and 8 runs of reference strains and laboratory mutants.

### Sample preparation and extraction

The M. tuberculosis and M. africanum samples were prepared and extracted at the World Health Organization Supranational Reference Laboratory in Stockholm, Sweden, and the Institute for Genomic Medicine at the University of California, San Diego in La Jolla, CA, USA. DNA preparation and extraction was performed as previously described (Elghraoui et al., 2017). All samples were streaked for isolation using standard microbiological methods, after which well-separated colonies were selected, emulsified, and sub-cultured on Löwenstein–Jensen slants and incubated until growth of a full bacterial lawn. To ensure enough bacterial material for extraction of sufficient high molecular weight DNA for amplification-free SMRT-sequencing well-outgrown solid cultures (Löwenstein–Jensen medium). Typically, enough bacterial cells were obtained after 3–4 weeks of culture. At this stage, cultures reached the early- to mid-stationary phase. DNA was extracted from cultures in the stationary growth phase. DNA was extracted using Genomic-tips (Qiagen Inc, Germantown, MD, USA) following the manufacturer's sample preparation and lysis protocol for bacteria with the following modifications. Each culture was harvested directly into buffer B1/RNAse solution, homogenized by vigorous vortex mixing and inactivated at 80°C for 1 hr. Lysozyme was added and incubated at 37°C for 30 min followed by the addition of proteinase K and further incubation at 37°C for an additional 60 min. Buffer B2 was added and the mixture was incubated overnight at 50°C. The remainder of the Genomic-tip protocol was carried out exactly as described by the manufacturer. DNA purity and concentration were analyzed on a Nanodrop 1000 (Thermo Scientific, Waltham, MA, USA).

### DNA sequencing

DNA sequencing was performed at the Institute for Genomic Medicine at the University of California, San Diego. DNA libraries for PacBio (Pacific Biosciences, Menlo Park, CA) were prepared using PacBio’s DNA Template Prep Kit with no follow-up PCR amplification. Briefly, sheared DNA was end repaired, and hairpin adapters were ligated using T4 DNA ligase. Incompletely formed SMRTbell templates were degraded with a combination of Exonuclease III and Exonuclease VII. The resulting DNA templates were purified using SPRI magnetic beads (AMPure, Agencourt Bioscience, Beverly, MA) and annealed to a twofold molar excess of a sequencing primer that specifically bound to the single-stranded loop region of the hairpin adapters. SMRTbell templates were subjected to standard SMRT-sequencing using an engineered phi29 DNA polymerase on the PacBio RSII system according to manufacturer's protocol.

### Genome assembly

For isolates that were sequenced on multiple SMRT cells, all SMRT cell raw reads were combined and assembled with either HGAP2 (Chin et al., 2013) or canu (Koren et al., 2017) with default parameters. Circularization was then performed to confirm a circular genome using minimus2 from amos or circlator (Hunt et al., 2015). Gene dnaA was set as the first gene in each genome. Iterative rounds of consensus polishing using BLASR (Chaisson and Tesler, 2012) and Quiver were executed three times. Default parameters were used except max coverage was set to 1000 for Quiver. Genomes failed assembly quality control if they could not be circularized, if their consensus polishing resulted in five or more variants after three iterations, or if PBHoney (English et al., 2014) detected a structural variant in the assembly supported by at least 10% of the reads. PBHoney was run with default parameters. Full details of methods are described by Ramirez-Busby and colleagues (manuscript in preparation).

### Lineage determination

For the isolates originally collected by the Global Consortium for Drug-resistant Tuberculosis Diagnostics, lineage information was obtained by inputting the MIRU-VNTR and spoligotype patterns determined previously3 into TBInsight (Shabbeer et al., 2012). For all other genomes, a custom script, MiruHero (https://gitlab.com/LPCDRP/miru-hero), determined lineage. MiruHero takes in FASTA files with the whole genome sequences M. tuberculosis strains and in silico determines the strain’s spoligotype and MIRU type. MiruHero then determines the strain’s lineage by applying the same spoligotype and MIRU type interpretation rules used by TBInsight.

### Genome annotation

Gene annotations were transferred to each isolate from a well-characterized reference, virulent M. tuberculosis type strain H37Rv (Lew et al., 2011) with additional functional annotations curated from literature (Modlin et al., 2018). The transfer step was implemented using the Rapid Annotation Transfer Tool (RATT Otto et al., 2011) with the ‘Strain’ parameter. For each isolate, RATT read a FASTA file with the isolate’s whole genome sequence, and read the curated reference annotation EMBL file of H37Rv, then created an EMBL annotation file for the isolate. RATT transfers annotated genome features to an isolate in regions of sequence similarity to the reference, adjusting genome position based on synteny blocks. RATT transferred both genes and transcriptional start sites (TSS) from our curated H37Rv annotation. These TSSs were originally determined experimentally in the H37Rv strain by Cortes et al., 2013 and Shell et al., 2015.

### MTase genotyping

To determine the genotype of the MTase genes mamA (Rv3263), mamB (Rv2024c), and hsdM (Rv2756c)/hsdS (Rv2761c) in each isolate, first eggNOG-mapper (Powell et al., 2012) identified these genes in each clinical isolate. However, MamB and HsdM are inactive in virulent type strain H37Rv (Zhu et al., 2016), we did not use the H37Rv genes as the wild-type allele. Instead, sequencing kinetics and the previously characterized target motifs were used to determine which isolates had active copies of each MTase gene, and the most common allele among active isolates was defined as the wild-type sequence. To call variants in these genes using these wild-type sequences, BLASTn then aligned the wild-type sequences against all genes predicted in each isolate by Prodigal (Hyatt et al., 2010). Each matching nucleotide sequence was translated into an amino acid sequence using transeq (EMBOSS 6.6.0.0, available online at www.ebi.ac.uk/Tools/emboss/transeq/index.html) to obtain nonsynonymous variants and truncations. The amino acid sequences were then aligned using MAFFT (Katoh and Standley, 2013) v7.205 with the – clustalout option, and a custom script converted the alignment to a genotype. To verify the identity of the 1356 bp mamB insertion variant, BLASTn aligned the M. tuberculosis insertion element IS6110 against the variant mamB gene (Figure 2—figure supplement 1). The IS6110 sequence is included in Supplementary file 8.

### Phylogenetic analysis

The genomes of Mycobacterium canettii CIPT 140070010 (NC_019951.1) and Mycobacterium bovis BCG Pasteur 1173P2 (AM408590.1) were used as outgroups. Then, dnadiff (Marçais et al., 2018) (v1.3) aligned each assembled genome to M. tuberculosis H37Rv (NC_000962.3) to call SNPs and small indels with default parameters. A custom Perl script then converted the out.snps file from dnadiff for each isolate into a VCF v4.0 file. A multi-FASTA file of concatenated variants was then created using each isolate's VCF file. The resulting multi-FASTA file was used to create a maximum likelihood phylogenetic tree using RAxML version 8.2 (Stamatakis, 2014), specifying a general time-reversible model of nucleotide evolution with 100 bootstrap replicates. All other settings were default. To visualize the phylogenetic distribution of MTase genotypes, a custom python script converted a CSV file with the MTase genotypes of each isolate into a tree color annotation file. The tree color annotation file and RAxML tree file were then uploaded to the Interactive Tree of Life (iTOL) (Letunic and Bork, 2016) webtool for visualization.

### Determination of IPD of MTase motif sites

To determine the IPD ratio at each nucleotide in each isolate, we ran SMRTanalysis with the Base Modification Detection with Motif Finding protocol with default parameters. A custom R script then scanned the FASTA sequence file of each isolate for matches to the MTase target motifs previously characterized in M. tuberculosis (Zhu et al., 2016) (https://gitlab.com/LPCDRP/dna-methylation/-/tree/publication/targets), then extracted the IPD ratio of the targeted adenine in each matching site from the Base Modification output. These IPD ratios were then log-transformed to produce a normal distribution and standardized by subtracting the mean IPD ratio (also log-transformed) of all adenines outside of MTase motifs in the isolate.

### MTase motif locus assignment

To track MTase motif sites across isolates, each MTase motif site in each isolate was assigned a locus tag based on the nearest gene. For each isolate, a custom python script read a CSV file with the genome positions of each MTase motif site in the isolate, and the isolate’s genome annotation EMBL file. Using the genome positions of annotated coding sequences (CDS), the script identified the nearest gene boundary (CDS start or CDS stop) to each MTase motif site and assigned each site a locus tag. The locus tag contained the gene name of the neighboring gene boundary, the distance in nucleotides between the MTase site and the gene’s CDS start position, an indicator whether the MTase site was on the same strand as the gene (sense) or the opposite strand (antisense), and an indicator whether the gene was downstream or upstream of the CDS start.

### Characterizing the kinetic error profile across technical replicates

We characterized the error profile of sequencing kinetics by comparing the IPD ratio of each base between replicate sequencing runs, and measuring how that variance increased with coverage. We used two sequencing runs on DNA isolated from avirulent type strain H37Ra sequenced at UCSD, and two publicly available sequencing runs on virulent type strain H37Rv (Bioproject accession PRJEB8783). We first log-transformed the IPD ratio of each base to account for the skewed distribution of ratio values (Figure 1—figure supplement 1A–B). We then plotted the difference in log-transformed IPD ratio of each base between runs by genome position (Figure 1—figure supplement 1C) and by per base coverage (Figure 1—figure supplement 1D). Using R’s cor.test function with the ‘pearson’ method, we tested the significance of the correlation between per base coverage and the difference in log-transformed IPD ratio of each base between runs (Figure 1—figure supplement 1D).

### Characterization of MTase activity of MTase genotypes

For each MTase and each isolate, a custom R script plotted the distribution of log-transformed, scaled IPD ratios of each MTase motif site (Figure 2A & D). For all three MTases, MTase genotype reliably corresponded to distribution of sequencing at their respective motif sites. For most isolates, sequencing kinetics centered around 0 (consistent with no methylation) or around a narrow band consistent with full m6A methylation. MTase genotypes for these cases were labeled accordingly as ‘fully active’ or ‘inactive’ (loss-of-function). MTase genotypes for the remaining minority of cases, where sequencing kinetics distributed around a mean between 0 and the value around which fully active isolates distributed, were labeled as ‘partially active’.

### Identification of hypervariable MTase motif loci

For each MTase, a custom R script found the set of MTase motif site loci present in at least 75 isolates. For each locus, summary statistics (mean, median, and standard deviation) of mean log2 (IPD Ratio) were calculated exclusively from isolates with active genotypes of the relevant MTase. The same was then performed to obtain median and standard deviation of mean log2 (IPD Ratio) for inactive isolates of each activity profile for each MTase, and, for MamA, for isolates with the common E270A mamA genotype. Hypervariable HsdM, MamA, and MamB motif sites were classified as those more than 3 s.D above the mean variability (standard deviation across isolates with active MamB at that site) for MamB motif sites, since they had the fewest outliers and are not an orphan MTase.

### Heterogeneous methylation analysis

SMALR (Beaulaurier et al., 2015) requires a de novo assembled genome FASTA file, a target motif, and a cmp.h5 file with aligned reads, to extract the IPD data from each MTase target motif site within each read. We ran SMALR on 96 samples using the MamA target motif CTGGAG. The isolates had the following mamA genotypes: 49 were wild-type, four were W136R, four were G152S, and 34 were E270A. We also ran SMALR on 70 isolates using the MamB target motif CACGCAG. The isolates had the following mamB genotypes: 60 were wild-type, nine had an loss-of-function variant, and one had the partially active variant K1033T. We then filtered out isolates with fewer than 20 total reads from downstream analysis. We additionally ran SMALR with the MamA target motif CTGGAG on one isolate assembled from published sequencing reads from a ∆metA mutant of H37Rv that was SMRT-sequenced following 5 days of methionine starvation (Berney et al., 2015).

For each isolate, a cmp.h5 was generated by aligning its reads to its assembled FASTA file using BLASR (Chaisson and Tesler, 2012). SMALR was run on each isolate with the SMp (single-molecule, pooled distribution) argument. For MamA sites, the motif argument was set to CTGGAG, the modified position within the motif to 5, and the minimum number of motif sites per read to 6. For MamB sites, the motif argument was set to CACGCAG, the modified position to 6, and the motifs per read threshold to 6. The native IPD value of each read was used in place of SMp score. This substitution is susceptible to noise from local sequence contexts, but should still resolve differences between isolates and distinguish methylated and unmethylated reads (Beaulaurier et al., 2015). The distribution of native IPD values within each isolate for MamA and MamB sites was visualized using ggplot2 (Wickham, 2016), and comparisons between genotypes was performed using two-tailed Student’s t-tests with the t.test and effect sizes estimated with cohen.d functions in R (R Development Core Team, 2018).

### Identification of promoters

To identify MTase motif sites in probable gene promoters, for each isolate a custom python script read a CSV file with the genome positions of each MTase motif site in the isolate, and the isolate’s genome annotation EMBL file. The script scanned the surrounding sequence on either strand of each MTase motif site for Sigma Factor Binding Sight (SFBS) motifs previously characterized in M. tuberculosis (Chauhan et al., 2016) (https://gitlab.com/LPCDRP/dna-methylation/-/tree/publication/targets). If a SFBS motif match overlapped with an MTase motif site, the MTase motif site was labeled with the sigma factor type corresponding to the SFBS motif (Sigma Factor A through Sigma Factor M, −10 element or −35 element). The script then compared the genome position and strand of the SFBS motif match to the genome position and strand of each annotated TSS in the isolate’s genome annotation EMBL file. To meet the most stringent criteria for probable promoter sites (‘full promoters’, Figure 6C) an SFBS motif had to be the appropriate nucleotide distance upstream from an annotated TSS. If the SFBS motif match was the −10 component of a SFBS motif, the script checked if a there was a TSS on the same strand with a genome position 8 to 12 bp downstream of the matching sequence. If the SFBS match was a −35 component of a SFBS, the script instead checked for a TSS between 30 and 40 bp downstream. To capture MTase promoter interactions excluded by this conservative definition of SFBS, for the analysis in Figure 6C, categories were assigned indicating the substantiveness of the evidence supporting overlap with promoter elements. The following logic was executed programmatically in R to assign categories: ‘Element’ matches overlap either the −10 or −35 SFBS the expected distance from the TSS (see above) but have neither an extended −10 promoter element nor the complementary element; ‘Location’ matches are at the appropriate distance upstream of the TSS to overlap with −10 or −35 elements but do not overlap known SFBS motifs; ‘Sequence’ matches coincide with SFBSs but not in the expected position with respect to TSS; ‘none’ are within 50 bp upstream of a TSS but meet criteria for none of the aforementioned categories.

### Bayesian classification of base-specific methylation status

Even within isolates with active MTase genotypes, not every base with an MTase target motif was methylated. To identify MTase motif sites with no base modification (hypomethylated sites) despite an active MTase we took a Bayesian approach. In each isolate a custom R script estimated the distribution of normalized IPD ratios among unmodified bases by calculating the standard deviation and mean normalized IPD ratios of bases not within MTase motifs. The script then estimated the distribution of methylated bases by calculating the standard deviation and mean of bases targeted by MTase motifs. This estimate assumed that most bases targeted by MTase motifs were methylated, which held true in isolates with active MTase genotypes (Figure 2A). For each MTase motif site, the script calculated the conditional probability of the base belonging to either the modified or unmodified population, given its normalized IPD ratio and coverage. The script classified all bases more than nine times more likely to belong to the unmodified population as hypomethylated, all bases more than nine times more likely to belong to the modified population as methylated, and the remaining bases as indeterminate.

The coverage of each MTase site in each isolate was used to adjust the standard deviation of the distributions used to calculate its conditional probability, as bases with lower coverage have less consistent IPD ratios (Figure 1—figure supplement 1D). To perform this coverage adjustment, for each isolate we trained a model to estimate the expected standard deviation of any base given its coverage. After log-transforming and normalizing the IPD ratios of all bases in an isolate, the script calculated each base’s number of standard deviations from the median normalized IPD ratio. Next, linear regression estimated the relationship between these standard deviations and the inverse coverage of each base. The resulting model estimated the standard deviation for each possible coverage value. When estimating the conditional probabilities of each MTase motif site, the code first calculated the mean and standard deviation of normalized IPD ratios in adenines within and without MTase motifs. It then multiplied these two standard deviations by the standard deviation predicted from the sequencing coverage at that MTase motif site. These adjusted standard deviations were then used to estimate the distribution of normalized IPD ratios and calculate the conditional probability of the MTase motif site belonging to those distributions.

### Conserved hypomethylation patterns

Using the Bayesian classification of each MTase motif target and the loci labeled by our methylome annotation pipeline, we searched for hypomethylated loci that occurred in multiple isolates. For each locus, a custom R script counted the number of isolates with that locus, including only isolates with active genotypes of the MTase targeting the locus. Our script also counted the number of these isolates in which the locus was hypomethylated. To estimate the significance of these findings, we used a cumulative binomial test, with the first count as the sample size and the second count as the number of successes. To find the probability of hypomethylation for each Bernoulli trial if hypomethylation occurred randomly, we calculated the total frequency of hypomethylation among MTase motif sites in active isolates. A separate per trial probability was calculated for MamA, MamB, and HsdM. The Bonferroni correction adjusted for multiple hypothesis testing, by dividing the significance threshold by the total number of unique loci in this study. No reference strains were included in the analysis of hypomethylated loci.

### Transcription factor binding motif scanning

We searched for Transcription Factor (TF) binding motifs near hypomethylated bases using the command line motif scanner FIMO (Grant et al., 2011) version 4.12.0. For each hypomethylated locus in an MTase target motif, we extracted the sequence surrounding the locus, 20 bases on each side in a randomly selected representative isolate (only isolates hypomethylated at that locus were chosen). The context sequences were combined into a multisequence FASTA file. Position-dependent letter-probability matrices of each TF binding motif were kindly provided by Minch and colleagues (Minch et al., 2015), who derived them from a ChIP-Seq experiment on virulent M. tuberculosis type strain H37Rv. We then ran FIMO using each TF motif on the context FASTA file with a threshold p-value of 0.01. For comparison we also scanned for TF motifs in the context sequences of consistently methylated loci (consistently methylated loci here defined as loci present in at least 30 isolates and methylated in at least 95% of those isolates). Custom scripts then parsed the FIMO output files for each TF binding motif and counted the number of methylated loci and the number of hypomethylated loci matching each TF with a q-value of at least 0.1.

To genotype the transcription factor MntR in each isolate, we used the same method used for the MTase genotyping. The wild-type sequence of mntR (Rv2788) was taken from the annotated reference genome H37Rv. BLASTn aligned the wild-type sequence against all genes predicted in each isolate by Prodigal (Hyatt et al., 2010). Each matching nucleotide sequence was translated into an amino acid sequence using transeq (EMBOSS 6.6.0.0, available online at www.ebi.ac.uk/Tools/emboss/transeq/index.html) to obtain nonsynonymous variants and truncations. The amino acid sequences were then aligned using MAFFT (Katoh and Standley, 2013) v7.205 with the –clustalout option, and a custom script converted the alignment to a genotype.

### Proximal motif site search

Multiple MTase motif sites in close proximity targeted by the same MTase can also potentially cause hypomethylation (Casadesús and Low, 2013). To find potential cases of this phenomenon, for each isolate a custom R script read a CSV file with the genome positions of each MTase motif site in the isolate. For each MTase motif site, the script found the nearest MTase motif site of the same type (MamA, MamB, and HsdM) and the same strand, then recorded the nucleotide distance between them. If the distance was less than 100 bp, the sites were considered neighbors (‘Nearby Motif,’ Table 1).

### RNA-Seq analysis

Supplementary table 9 of https://www.nature.com/articles/s41467-019-11948-6 was downloaded and merged by locus tag with our annotated promoters for HsdM. A Benjamini-Hochberg adjusted p-value threshold of 0.05 was set as the criteria for being considered ‘differentially expressed’, using the column labeled ‘padj (BH)'. Two-sided Fisher’s exact test was implemented in R to test for independence of HsdM motif site presence in the promoter and differentially expressed genes following hsdM knockout. Genes with an HsdM-targeted adenine within 50 bp upstream of the TSS were considered to have an HsdM promoter motif.
