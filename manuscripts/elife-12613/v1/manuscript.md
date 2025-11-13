# Evolutionary genomics of epidemic visceral leishmaniasis in the Indian subcontinent

## Authors

- Hideo Imamura<sup>1</sup>
- Tim Downing<sup>2</sup> ([ORCID: 0000-0002-8385-6730](https://orcid.org/0000-0002-8385-6730))
- Frederik Van den Broeck<sup>1</sup> ([ORCID: 0000-0003-2542-5585](https://orcid.org/0000-0003-2542-5585))
- Mandy J Sanders<sup>2</sup>
- Suman Rijal<sup>4</sup>
- Shyam Sundar<sup>5</sup>
- An Mannaert<sup>1</sup>
- Manu Vanaerschot<sup>1</sup>
- Maya Berg<sup>1</sup>
- Géraldine De Muylder<sup>1</sup>
- Franck Dumetz<sup>1</sup>
- Bart Cuypers<sup>1</sup>
- Ilse Maes<sup>1</sup>
- Malgorzata Domagalska<sup>1</sup>
- Saskia Decuypere<sup>1</sup>
- Keshav Rai<sup>4</sup> ([ORCID: 0000-0002-9747-3431](https://orcid.org/0000-0002-9747-3431))
- Surendra Uranw<sup>4</sup>
- Narayan Raj Bhattarai<sup>4</sup>
- Basudha Khanal<sup>4</sup>
- Vijay Kumar Prajapati<sup>5</sup>
- Smriti Sharma<sup>5</sup>
- Olivia Stark<sup>7</sup>
- Gabriele Schönian<sup>7</sup>
- Harry P De Koning<sup>8</sup> ([ORCID: 0000-0002-9963-1827](https://orcid.org/0000-0002-9963-1827))
- Luca Settimo<sup>8</sup>
- Benoit Vanhollebeke<sup>10</sup> ([ORCID: 0000-0002-0353-365X](https://orcid.org/0000-0002-0353-365X))
- Syamal Roy<sup>11</sup>
- Bart Ostyn<sup>12</sup>
- Marleen Boelaert<sup>12</sup> ([ORCID: 0000-0001-8051-6776](https://orcid.org/0000-0001-8051-6776))
- Louis Maes<sup>13</sup>
- Matthew Berriman<sup>2</sup> ([ORCID: 0000-0002-9581-0377](https://orcid.org/0000-0002-9581-0377))
- Jean-Claude Dujardin<sup>1</sup> †
- James A Cotton<sup>2</sup> ([ORCID: 0000-0001-5475-3583](https://orcid.org/0000-0001-5475-3583)) †

### Affiliations

1. Department of Biomedical Sciences Institute of Tropical Medicine Antwerp Belgium
2. Wellcome Trust Sanger Institute Hinxton United Kingdom
3. School of Maths, Applied Maths and Statistics National University of Ireland Galway Galway Ireland
4. BP Koirala Institute of Health Sciences Dharan Nepal
5. Department of Medicine, Institute of Medical Sciences Banaras Hindu University Varanasi India
6. Telethon Kids Institute University of Western Australia Perth Australia
7. Institut für Mikrobiologie und Hygiene Charité Universitätsmedizin Berlin Berlin Germany
8. Institute of Infection, Immunity and Inflammation, College of Medical, Veterinary and Life Sciences University of Glasgow Glasgow United Kingdom
9. Department of Chemistry and Chemical Biology Northeastern University Boston United States
10. Laboratory of Molecular Parasitology Université Libre de Bruxelles Gosselies Belgium
11. Department of Infectious Diseases and Immunology, Council of Scientific and Industrial Research Indian Institute of Chemical Biology Kolkata India
12. Department of Public Health Institute of Tropical Medicine Antwerp Belgium
13. Department of Biomedical Sciences, Faculty of Pharmaceutical, Biomedical and Veterinary Sciences University of Antwerp Antwerp Belgium

† Corresponding author

## Abstract

Leishmania donovani causes visceral leishmaniasis (VL), the second most deadly vector-borne parasitic disease. A recent epidemic in the Indian subcontinent (ISC) caused up to 80% of global VL and over 30,000 deaths per year. Resistance against antimonial drugs has probably been a contributing factor in the persistence of this epidemic. Here we use whole genome sequences from 204 clinical isolates to track the evolution and epidemiology of L. donovani from the ISC. We identify independent radiations that have emerged since a bottleneck coincident with 1960s DDT spraying campaigns. A genetically distinct population frequently resistant to antimonials has a two base-pair insertion in the aquaglyceroporin gene LdAQP1 that prevents the transport of trivalent antimonials. We find evidence of genetic exchange between ISC populations, and show that the mutation in LdAQP1 has spread by recombination. Our results reveal the complexity of L. donovani evolution in the ISC in response to drug treatment.

## Introduction

Parasites of the Leishmania donovani species complex cause visceral leishmaniasis (VL), the most severe presentation of leishmaniasis that is usually fatal if untreated. There are probably between 200,000 and 300,000 VL cases annually (Alvar et al., 2012), leading to as many as 50,000 deaths per year (den Boer et al., 2011; Lozano et al., 2012). VL is widespread in both the New and Old Worlds (Pigott et al., 2014), but as much as 80% of the global VL burden occurs in the Indian sub-continent (Alvar et al., 2012). Recent intensified control efforts have led to a notable decline in cases (Chowdhury et al., 2014) but the problem is not yet eliminated. VL is a key neglected tropical disease, affecting the poorest regions of the world and the poorest communities within these regions (Boelaert et al., 2009). VL was first reported in the Indian sub-continent (ISC) in the 1820s, but initially confused with malaria until the discovery of L. donovani in 1903 (Gibson, 1983). Although VL was nearly eliminated from the ISC in the 1960s (Thakur, 2007) by antimalarial spraying campaigns with DDT, it re-emerged in 1977 and has caused several subsequent major epidemics (Dye and Wolpert, 1988). Widespread chemotherapy for VL in the region has been ongoing since the 1820s, initially with quinine and other drugs, followed by extensive use of the trivalent antimonial SbIII (1915) and compounds of the less toxic pentavalent SbV (1922) such as sodium stibogluconate (SSG), and since 2005 with miltefosine (MIL) that is freely supplied through a government-subsidized control program. The parasite developed resistance to both SbIII and SbV, and after ten years of clinical use there has been a notable decline in MIL efficacy (Rijal et al., 2013; 2007; Sundar et al., 2012).

Leishmania parasites can re-shape their genome rapidly in vitro in response to stress (Leprohon et al., 2009), suggesting structural variation is an important feature by which they can rapidly adapt to changing environmental conditions and drug pressure. However, there is little data on the diversity of clinical Leishmania populations or how they evolve during treatment. While an extensive literature has made use of molecular methods to study the population genetics of Leishmania (e.g. Alam et al., 2009; Lukes et al., 2007; Mauricio et al., 2006; Schonian et al., 2008), existing genetic markers have relatively poor resolution, and in particular L. donovani within the ISC show very little genetic differentiation based on these approaches (Alam et al., 2009; Downing et al., 2012). Whole-genome sequence data has the potential to show significant population structure within the ISC, and also allows us to identify changes in genome structure.

Here we report the genome sequences of 204 L. donovani isolates (Figure 1, Supplementary file 1), obtained from VL patients between 2002 and 2011 from regions in Nepal (N=98), India (N=98) and Bangladesh (N=8) that represent the epicentre of the on-going VL epidemic in the ISC (Figure 1a).

![Figure 1.](https://cdn.elifesciences.org/articles/12613/elife-12613-fig1-v1.jpg)

**Figure 1.:** (a) Location of the patients from which the 204 L. donovani genomes were isolated, and of historical Kala-Azar outbreaks. Genetic groups of the parasite isolates are indicated by the colour of the dots representing them, matching those in Figure 2a,c. Sampling dates and locations are summarised in Figure 1—figure supplement 1, and detailed information about each strain including GPS coordinates are given in the source data file. Citations are to historical primary literature reviewed and cited in (Gibson, 1983). Posterior probability distributions of estimated ages for the oldest split in (b) the main population in Bihar and Nepal and (c) the ISC5 group associated with Sb resistance. Dark shading shows estimates under a strict molecular clock, light shading from relaxed molecular clock and lines show relaxed clock results with Bangladeshi and putative hybrid isolates included. (d) Estimated effective population size through time for ISC5 population (green) and the rest of the parasite population (black/grey). Lines show median of posterior distributions, dark and light shading cover 50% and 95% of the posterior density respectively. Dates for all splits on this phylogeny and other results of phylogeographic analysis are shown in Figure 1—figure supplement 2.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/12613/elife-12613-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** Pie charts indicate the number of samples in each year (columns), for each genetic group (rows) coming from each country (grey shading). Horizontal lines connect and surround isolates of each group, with colours matching the groups shown in panels (b) and (c). *8 samples from Bangladesh were all sampled in 2006, and form a distinct population to Nepalese and Indian isolates (ISC2).

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/12613/elife-12613-fig1-figsupp2-v1.jpg)

**Figure 1—figure supplement 2.:** (a) Maximum posterior probability phylogeny, with tips coloured by country of origin for sample (green for India, blue for Nepal), and branches coloured by maximum posterior probability of country reconstructed in discrete phylogeography model. Values on nodes indicate posterior probability of assigned country/colour, with filled circles marking nodes with probability 1. Other panels represent posterior probability distributions for rates of migration (lineage switches per month) from (b) Nepal to India and (c) from India to Nepal. Note the mode (maximum posterior probability estimate) for migration from Nepal is zero, but non-zero migration in the reverse direction is supported.

## Results

Calling variants against a reference genome assembly for a Nepalese L. donovani strain (BPK282/0cl4; Figure 2—figure supplement 1), we identify three divergent genetic lineages circulating in this region (Figure 2b): a core group of 191 closely related parasites found in the highly endemic lowlands of all three countries, a small population of 12 Nepalese isolates found most frequently in the highlands (ISC1) and a single divergent Nepalese isolate (BPK512/0cl9) (Downing et al., 2011). These two main groups show fixed differences at 45,743 sites (Supplementary file 2, table a), and two previously sequenced Sri Lankan L. donovani isolates (Zhang et al., 2014) were more closely related to the core population (21,546 fixed differences) than to ISC1 (45,743 fixed differences). Parasites within each group show little SNP variation with only 5,628 variable sites in ISC1 and just 2,418 sites varying within the core population (Supplementary file 2, table b) and correspondingly few SNPs in protein-coding regions (Supplementary file 2, table c). Core population isolates differ at an average of 88.3 nucleotide sites with an average nucleotide diversity of 9.7 per Mb (Supplementary file 2, table d).

![Figure 2.](https://cdn.elifesciences.org/articles/12613/elife-12613-fig2-v1.jpg)

**Figure 2.:** (a) Maximum-likelihood tree based on SNPs called for 191 strains (see Figure 2—figure supplement 1) from the core population in the Indian subcontinent. Samples are coloured by population assignment, with putative hybrid strains not clustered in the main groups in black. Further analysis confirms the hybrid ancestry of some of these isolates (Figure 2—figure supplement 2). (b) Unrooted phylogenetic network of the L. donovani complex based on split decomposition of maximum-likelihood distances between isolates described here, reference genome isolates and two published Sri Lankan isolates (Zhang et al., 2014). (c) Model-based clustering of 191 isolates from the core population reveals six discrete monophyletic groups, and some groups and other samples of less certain ancestry. Coloured bars show the fraction of ancestry per strain assigned to a given cluster, with colours assigned to the population most closely related to each cluster. More detailed population clustering analysis shows largely congruent results (Figure 2—figure supplements 3 and 4).

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/12613/elife-12613-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** Overview of the SNP detection method COCALL (COnsensus of SNP CALL). COCALL finds genetic variants that show a concordant signal over five different SNP callers (Cortex, Freebayes, GATK, Samtools Mpileup and Pileup). See supplementary methods for details.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/12613/elife-12613-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** Haplotype networks indicate putative hybrids as isolates with ancestry from multiple distinct populations. Chromosomal haplotype neighbour-joining networks of the phased data for the core population were constructed using the R ape package. Each node represents one haplotype variant for (a) chromosome 32 and (b) chromosome 35, coloured by group. Black lines are network edges and red lines connect haplotype variants from the same isolate for selected isolates where haplotypes appear in different parts of the network (with isolate names shown). Six ungrouped isolates (BHU815/0, BHU764/0cl1, BHU274/0, BHU574cl4, BHU581cl2, BHU572cl3) have mixed ancestry from ISC5 and other groups, and two (BHU744/0 and BHU774/0) have a mix of ISC6/7/8/9/10 haplotypes. No mixing among ISC2/3/4 was evident.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/12613/elife-12613-fig2-figsupp3-v1.jpg)

**Figure 2—figure supplement 3.:** Heatmap showing the mean expected number of haplotypes shared between pairs of core population isolates. Samples listed on the y-axis are haplotype donors to those on the x-axis. 18,747 phased genotypes at 2397 SNPs sites were computed with Chromopainter v0.0.2 using recombination rates from PHASE for 79 haplotype chunks with c=0.00054 effective chunks. This image confirms six discrete populations ISC2-7 and illustrates complex ancestry in certain samples not belonging to these groups.

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/12613/elife-12613-fig2-figsupp4-v1.jpg)

**Figure 2—figure supplement 4.:** Representative samples from three potentially parental groups (BPK282/0cl4, ISC6; BHU200/0, ISC7; BPK275/0cl18, ISC5) were compared to eight putative hybrid samples (BHU815/0, BHU764/0cl1, BHU274/0, BHU574cl4, BHU581cl2, BHU572cl3, BHU744/0 and BHU774/0). To the left is a maximum-likelihood tree constructed with RAxML showing the evolutionary history of the aligned haplotypes. The table shows a set of SNPs for which ChromoPainter assigned ancestry probability values >0.4 in any of these eight hybrids. Individual SNPs are coloured if the sample had an ancestry probability >0.4: uncoloured ones represent those observed in multiple ISC populations. All isolates have mixed ancestry from the two groups, but four isolates (BHU574cl4, BHU764/0cl1, BHU815/0 and BHU274/0) have haplotypes that appear to have a more complex origin.

While a panel of microsatellite markers shows no variation between isolates from the core population (Downing et al., 2012), we reveal significant spatial and temporal genetic structure within this group despite this extremely low level of overall diversity (Figure 2a,c; Supplementary file 2, table e). Phylogenetic and clustering methods identify six congruent monophyletic groups (ISC2-7). Three other groups (ISC8-10) and 21 ungrouped isolates had more complex and less certain evolutionary histories (Figure 2a,c; Supplementary file 2, table f). Most of the ISC groups are present throughout our sampling window (2002–2011), and many are present in both India and Nepal (Figure 1—figure supplement 1). There are some exceptions: ISC7 represents a recent radiation (first observed in 2006) with almost no diversity (20 unique SNPs; Supplementary file 2, table g; π=1.8 per Mb) and is restricted to India, while ISC6 is an older and more diverse group restricted to Nepal (π=12.2 per Mb). We observe subsequent evolution within some groups: ISC5 is distinguished from other groups by just 32 SNP sites (Supplementary file 2, table h), but contains a subgroup with multiple novel SNPs and lower somy (Supplementary file 2, table i).

Bayesian phylogenetic models in an explicit temporal and spatial framework revealed that the core population diverged in the mid 19th century (Figure 1b), matching the dates of the earliest reports of large-scale VL outbreaks in the ISC (Gibson, 1983) and thus suggesting that modern lowland parasites descend from these early epidemics. Within the core population, the Indo-Nepalese population itself appeared around 1900 (Figure 1—figure supplement 2), almost certainly in India (0.89 posterior probability), matching the dates of the first reported outbreaks in Bihar (Gibson, 1983), more precisely in Purnea (Figure 2d). Most subsequent diversification is more recent, with many groups (ISC2 & ISC4-6) radiating from the 1960s (Figure 1b), coinciding with the end of the DDT spraying campaign. The estimated rate of migration from India to Nepal in the Core 191 group was significantly greater than that from Nepal to India, suggesting that India acts as a source population seeding the Nepalese epidemic (Figure 1—figure supplement 2).

A lack of linkage disequilibrium decay between SNP pairs with genomic distance in the core population (r2~0.33 at 5–1,400 kb) reflects a lack of detectable recombination within the six main genetic groups (ISC2-7) across the entire genome (Supplementary file 2, table j). While the low number of SNPs varying within the core population limits our power to detect recombination, we find compelling evidence of hybridisation among eight of the samples not assigned to any of the ISC groups (Figure 2—figure supplements 2–4). The identity of these isolates as hybrids and our assignment of other isolates to groups is supported by allele-frequency based methods (f-statistics), which should be robust to gene flow between groups (Supplementary file 2, tables e,f) and population structure analysis based on haplotype sharing (Supplementary files 2, tables k–n). The four-allele test also confirms that recombination is largely restricted to these hybrids (Supplementary file 2, table o). These isolates appear to result from multiple independent recent hybridizations between distinct ancestors of either ISC5 and ISC6, ISC5 and ISC7, or ISC6 and ISC7 (Figure 2—figure supplement 2).

We detect extensive variation in the structure of these L. donovani genomes. Local copy-number variants (CNVs) cover ~11% of the genome. These include sporadic gene duplication, dynamic tandem gene array sizes (Figure 3—figure supplement 1) and long sub-telomeric amplifications/deletions, the latter generally spanning whole transcription units. While structural variation in Leishmania is often considered a transient adaptation, particularly to culture conditions in vitro, we find striking conservation of many CNVs across all core population groups here. Two multigenic intra-chromosomal duplicated regions (MAPK1 and H-locus; Downing et al., 2011) are present in variable numbers in all core population isolates but are absent in ISC1 (Figure 3b,c; Figure 3—figure supplement 2). Conserved heterozygous SNPs in both of these structural variants confirm that these regions have duplicated once and been maintained throughout the evolution of this population. All known genes on these duplicated regions are associated with virulence (MAPK1, ASS, sAcP; Fernandes et al., 2013; Lakhal-Naouar et al., 2012; Wiese, 1998) or drug resistance (Brotherton et al., 2013), indicating that extensive structural variation allows these parasites to alter local copy number in response to changing environments: both aneuploidy and CNV regulate gene expression (Leprohon et al., 2009). Most isolates are aneuploid (Figure 3—figure supplement 3), even excluding the generally tetrasomic chromosome 31, and almost all chromosomes show some variation in somy (Figure 3a). Aneuploidy (r2=0.15, p=2.7x10-118), CNVs (r2=0.26, p=7.5x10-218) and indels (r2=0.30, p=2.1x10-254) are significantly correlated with SNP variation in the core isolates, suggesting that these variants have appeared gradually during the evolution of the population in the field. Most strikingly, we find two cases of recent epidemic expansions associated with major changes in aneuploidy and heterozygosity (Figure 4). Variation in somy can thus lead to changes in heterozygosity, which could allow selection to eradicate recessive deleterious mutations in the absence of recombination (Roze and Michod, 2010).

![Figure 3.](https://cdn.elifesciences.org/articles/12613/elife-12613-fig3-v1.jpg)

**Figure 3.:** (a) Stacked barplots per chromosome showing the proportion of ISC strains that are monosomic, disomic, trisomic, tretrasomic or pentasomic for the respective chromosome. A full breakdown of somy per strain is presented in Figure 3—figure supplement 3, and a complete catalogue of other structural variants in Figure 3—figure supplement 1. Violin plots showing the copy number of MAPK1 (b) and H-locus (c) per ISC group, except for ISC1 where these amplicons were absent. These amplicons are intra-chromosomal (Figure 3—figure supplement 2). (d) Tetrameric protein model of the transport protein aquaglyceroporin-1. The C-terminus part that is affected by the 2-nucleotide frameshift found in all ISC5 isolates is shown in magenta. Image was created using PyMOL version 1.50.04 (Schrödinger).

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/12613/elife-12613-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** The position in the genome is shown on the y-axis, while individual isolates are shown on the x-axis. Colours of each copy number variant (CNV) represent the haploid depth variation (D) compared to the median depth for that chromosome (see legend for colour key). When the depth of the majority of the strains is high like the episome in ch23, this appears as a reduced depth in the strains that lack the episome. The length of each CNV is reflected by its length along the y-axis (i.e. thickness of the line). Four major CNVs – gp63, rDNA, an episome in ch23 and the MAPK amplification – are indicated with arrows. Group-specific copy number variants were highlighted with a box and numbered – detailed information about these CNVs are given in the table. The 206 samples included here are 204 ISC samples with L. infantum JPCM5 (MCAN/ES/1998/LLM-877) and L. donovani LV9 (MHOM/ET/1967/HU3) for reference.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/12613/elife-12613-fig3-figsupp2-v1.jpg)

**Figure 3—figure supplement 2.:** (a, c) Chromosomes from L. donovani BPK282/0cl4 (ISC6), BPK380/0 (ISC9) and BPK026/0cl5 (ISC1) were separated by pulsed-field gel electrophoresis (PFGE). (b) The MAPK1-locus and H-locus were detected by southern blot hybridization with probes specific for MAPK1 or HTBF, respectively. Hybridization was only observed in fragments of lengths equal to those of chr36 (~2.5 Mb) and chr23 (~1 Mb) and no additional smaller fragments were observed, indicating the absence of extra-chromosomal amplifications. (d) In contrast, linear extrachromosomal amplification (as evidenced by a second and smaller band) is shown for chromosome 35 in BPK380/0 by hybridization of a probe specific to the LinJ35.4130 gene.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/12613/elife-12613-fig3-figsupp3-v1.jpg)

**Figure 3—figure supplement 3.:** Average number of chromosomes found within each cell culture for each of the 36 chromosomes (y-axis) and each of the 204 L. donovani strains (x-axis). Samples are coloured by population assignment following Figure 1c, with strains not clustered in the main populations shown in white.

![Figure 4.](https://cdn.elifesciences.org/articles/12613/elife-12613-fig4-v1.jpg)

**Figure 4.:** Two subclades show an expansion of polysomic strains from disomic ancestors (below) and an expansion of disomic strains from polysomic ancestors (above). Somy variation per chromosome (1–36; above heatmap) and the total number of heterozygote SNPs (right to heatmap) are shown for each individual strain.

We find no statistically significant association between any individual SNP or structural genetic variant and in vitro SSG resistance, or SSG or MIL treatment outcomes (Supplementary file 2, tables p–r), but the distribution of antimony susceptibility was uneven across different ISC populations (Supplementary file 1). 9 of 11 ISC5 samples tested were highly SbV-resistant and two out of four ISC5-ISC6/7 hybrids tested have intermediate levels of resistance. One variant – a two-bp insertion introducing a frameshift and premature stop codon in the aquaglyceroporin-1 gene (LdBPK_310030, AQP1) – is homozygous in all 52 ISC5 isolates (Table 1), and heterozygous in six hybrids between ISC5 and either ISC6 or ISC7. ISC5 isolates also share other genomic features – such as higher copy number of both the H-locus and MAPK1 amplicons (Figure 3b,c). The H-locus includes MRPA, a gene involved in the efflux of SbIII and associated with drug resistance (Leprohon et al., 2009). Other lines of evidence strongly link AQP1 with antimony resistance. While recent antimonial drugs such as SSG are compounds of pentavalent antimony (SbV), SbV is thought to act mostly as a pro-drug, being reduced to SbIII in both the macrophage phagolysosome (Frézard et al., 2001) and in the parasite itself (Denton et al., 2004; Decuypere et al., 2012). AQP1 is known to assist with SbIII uptake, both genetic and transcriptional changes at this locus have been associated with Sb resistance (Gourbal et al., 2004; Monte-Neto et al., 2015; Mukherjee et al., 2013; Uzcategui et al., 2008) and a homologous transporter is associated with drug resistance in trypanosomes (Baker et al., 2012). Recently, an AQP1 knockout line of Leishmania major was shown to be resistant to SbIII due to reduced uptake (Plourde et al., 2015). The truncated frameshift protein found in ISC5 is predicted to be incapable of forming a functional trans-membrane channel (Figure 3d). We find three other independent frameshifts in AQP1 gene in other antimony resistant isolates, including one in BPK181/12 (ISC6), an isolate taken from a patient following failure of ten months of antimony treatment that was absent in the pre-treatment isolate from the same patient (BPK181/ 0cl11, Table 1).

**Table 1.**
 Small indels. The first half of the table summarises the numbers and types of indels detected in each group. The second half of the table shows the proportion of samples within a cluster that share each group-specific coding-region indel.


<table>
  <tbody>
    <tr>
      <td colspan="3">1. Number of indels</td>
      <td>ISC002</td>
      <td>ISC003</td>
      <td>ISC004</td>
      <td>ISC005</td>
      <td>ISC006</td>
      <td>ISC007</td>
      <td>ISC008</td>
      <td>ISC009</td>
      <td>ISC010</td>
    </tr>
    <tr>
      <td colspan="3">Total number ofindels found within each group</td>
      <td>58</td>
      <td>60</td>
      <td>73</td>
      <td>79</td>
      <td>65</td>
      <td>55</td>
      <td>55</td>
      <td>84</td>
      <td>60</td>
    </tr>
    <tr>
      <td colspan="3">Number of group-specific Indels shared by part of the strains of that group</td>
      <td>9</td>
      <td>5</td>
      <td>11</td>
      <td>12</td>
      <td>7</td>
      <td>0</td>
      <td>8</td>
      <td>22</td>
      <td>7</td>
    </tr>
    <tr>
      <td colspan="3">Number of group-specific Indels shared by all the strains of that group</td>
      <td>6</td>
      <td>1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
    </tr>
    <tr>
      <td colspan="3">Number of group-specific Indels within coding regions</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
      <td>1</td>
    </tr>
    <tr>
      <td colspan="3">2. Indels within coding region</td>
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
      <td>Gene ID</td>
      <td>Gene product</td>
      <td>Position</td>
      <td>Type</td>
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
      <td>LdBPK_310030</td>
      <td>Aquaglyceroporin</td>
      <td>Ld31_0007774</td>
      <td>2</td>
      <td></td>
      <td>0.04</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>LdBPK_310030</td>
      <td>Aquaglyceroporin</td>
      <td>Ld31_0007735</td>
      <td>2</td>
      <td></td>
      <td></td>
      <td>1</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>LdBPK_310030</td>
      <td>Aquaglyceroporin</td>
      <td>Ld31_0007662</td>
      <td>1</td>
      <td></td>
      <td></td>
      <td></td>
      <td>0.04</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>LdBPK_310030</td>
      <td>Aquaglyceroporin</td>
      <td>Ld31_0008099</td>
      <td>2</td>
      <td></td>
      <td></td>
      <td></td>
      <td>0.11</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>LdBPK_291860</td>
      <td>Putative historie H2A</td>
      <td>Ld29_0816454</td>
      <td>-2</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>0.25</td>
      <td></td>
    </tr>
    <tr>
      <td>LdBPK_040410</td>
      <td>Conserved hypothetical protein</td>
      <td>Ld04_0155491</td>
      <td>3</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>0.08</td>
      <td></td>
    </tr>
    <tr>
      <td>LdBPK_070540</td>
      <td>Conserved hypothetical protein</td>
      <td>Ld07_0230487</td>
      <td>-3</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>0.12</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>LdBPK_190080</td>
      <td>Conserved hypothetical protein</td>
      <td>Ldl9_0015151</td>
      <td>1</td>
      <td></td>
      <td></td>
      <td>0.04</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>LdBPK_261790</td>
      <td>Conserved hypothetical protein</td>
      <td>Ld26_0651748</td>
      <td>4</td>
      <td></td>
      <td></td>
      <td></td>
      <td>0.11</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>LdBPK_301000</td>
      <td>Conserved hypothetical protein</td>
      <td>Ld30_0311376</td>
      <td>-1</td>
      <td></td>
      <td></td>
      <td>0.02</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>LdBPK_310690</td>
      <td>Conserved hypothetical protein</td>
      <td>Ld31_0241951</td>
      <td>-3</td>
      <td></td>
      <td></td>
      <td></td>
      <td>0.11</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>LdBPK_332580</td>
      <td>Conserved hypothetical protein</td>
      <td>Ld33_0995960</td>
      <td>1</td>
      <td></td>
      <td>0.04</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>LdBPK_366590</td>
      <td>Conserved hypothetical protein</td>
      <td>Ld36_2473775</td>
      <td>-3</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>0.25</td>
    </tr>
    <tr>
      <td>LdBPK_110650</td>
      <td>hypothetical, unknown function</td>
      <td>Ldll_0245832</td>
      <td>-3</td>
      <td>0.56</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>LdBPK_292330</td>
      <td>hypothetical, unknown function</td>
      <td>Ld29_1008496</td>
      <td>-3</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>0.08</td>
      <td></td>
    </tr>
  </tbody>
</table>

We propose that the AQP1 truncation is associated with antimonial resistance in the ancestor of ISC5, and has been transmitted to a group of hybrid parasites. The ISC5 lineage emerged following the end of the DDT campaigns but then proliferated quickly in the 1970s (Figure 1c,d), when antimonial dosage had to be doubled because of its declining efficacy. The persistence of this lineage beyond the era of Sb treatment perhaps reflects the increased fitness (Vanaerschot et al., 2013) of Sb-resistant parasites. These observations tally with a stronger signature of purifying selection on the ISC5 lineage, measured as a lower rate of derived allele accumulation compared to other ISC populations, which may be a consequence of higher historical exposure to drug stress (Supplementary file 2, table s). Sb resistance is also present in other genetic groups, with 4 out of 15 ISC4 lines tested in vitro being SbV-R, indicating resistance has emerged independently and recently multiple times in ISC L. donovani, and that other genetic variants responsible for SbV resistance must be present in this population. Indeed, other SbV resistance mechanisms are known in this population: previous work has shown that two resistant strains from ISC4 (BPK087 and BPK190) show significantly decreased transcription of an AQP1 locus encoding a wildtype protein sequence (Decuypere et al., 2005), and BHU764 combines a different indel mutation in AQP1 and reduced expression of MRPA, an efflux transporter of SbIII (Mukhopadhyay et al., 2011). The failure of any single resistance locus to sweep through this population may reflect the low level of gene flow and the presence of a large reservoir of untreated asymptomatic cases (Ostyn et al., 2011).

## Discussion

We have shown that genomic data can retrospectively unravel the evolution and epidemiology of this parasite population, and gain new insight into possible mechanisms of drug resistance against a background of extensive variation in genome structure. We report the first analysis of the structure and history of a Leishmania population, aligned with clinical and epidemiological records, enabled by the higher resolution of genome sequence data than other genotyping approaches. These data have allowed us to describe a mechanism of resistance to one of the most ancient drugs used in the human pharmacopeia, antimonials, not only identifying a key locus, but also showing the epidemiological dynamics of a population carrying a loss-of-function variant at this locus.

Continued genetic surveillance of parasite populations is key to rapidly identify and respond to the emergence of treatment failure. In the recent emergence of artemisinin resistance in Plasmodium falciparum, genomic data has led to the identification of the major locus underlying resistance (Ariey et al., 2014; Cheeseman et al., 2012), revealed the genetic architecture of resistance (Miotto et al., 2015) and shed light on the population genetic context in which resistance is appearing (Miotto et al., 2013). Genomic surveillance is playing a key role in defining the geographic boundaries of the spreading artemisinin-resistant population. Failure of anti-Leishmania chemotherapy could become a similar public health emergency: miltefosine has shown reduced efficacy in both India (Sundar et al., 2012) and Nepal (Rijal et al., 2013). While amphotericin B is now being used against visceral leishmaniasis in ISC, few alternative treatments are available, and continued genomic surveillance will facilitate tracking the response of the Leishmania population to continued use of these drugs.

Monitoring drug resistance in clinical settings is challenging: the data set we present was generated as part of a five-year collaboration between clinicians in the endemic countries, parasitologists and genome biologists. This collaboration is critical in generating data that reflects the evolution of parasite populations in close to real time and as such is directly applicable in a public health context. The data we present here provide baseline information on the diversity of Leishmania donovani in the ISC that will contribute to future studies of drug resistance and epidemiology of this population. Our results show the promise of genomic surveillance for other Leishmania populations, where patient symptoms, the parasites involved and the main treatment modalities all differ from those in the ISC (Sundar and Chakravarty, 2015).

## Materials and methods

### Sample collection

The ethics committee of (i) the Nepal Health Research Council, Kathmandu, (ii) the Institute of Medical Sciences, Banaras Hindu University (BHU), Varanasi, India and (iii) the corresponding bodies at the Institute of Tropical Medicine of Antwerp and the Antwerp University, Belgium, reviewed and approved the study protocol. Informed written consent was obtained from each patient or his/her guardian for those <18 years of age. All the patients and caretakers/parents had the study purpose explained to them in local language.

A total of 204 parasite isolates were obtained from clinically confirmed VL patients in the high endemic regions of the Indian subcontinent (ISC) by the B.P. Koirala (BPK) Institute of Health Sciences in Dharan (Nepal, Terai, N=98), the Kala-azar Medical Research Center in Muzaffarpur (India, Bihar, N=98) and the Mymensingh Medical College in Mymensingh (Bangladesh, BD, N=8). The Indian and Nepalese isolates were collected as part of a multi-center collaborative project to investigate drug resistance in ISC and were all typed as Leishmania (Leishmania) donovani. Complete clinical and epidemiological data were available for the Indian and Nepalese isolates (Supplementary file 1).

The 204 L. donovani isolates were obtained from confirmed visceral leishmaniasis patients in previous clinical studies as described elsewhere (Rijal et al., 2013; 2007). PCR-RFLP of the cysteine proteinase gene (Quispe Tintaya et al., 2004) typed all isolates as Leishmania donovani. Strain names consisted of 2–3 letters that indicated the location of isolation (BD, BHU, BPK), 2–4 digits that indicated the patient number in that location, a forward slash followed by 1–2 digits that indicated when the sample was isolated (0: before treatment, 1: 1 month after treatment, etc) and optionally the number of the parasite clone if the strain was cloned (clone one is listed as 'cl1'; clone two is listed as 'cl2', etc). Cloning was performed using the micro-drop method (Van Meirvenne et al., 1975). Patient treatment outcome was monitored at the end of treatment and at 3, 6 and 12 months post-treatment). Treatment non-response was defined as a case with positive parasitology at the end of the treatment course. Patients who were successfully cured at the end of treatment but in whom symptoms re-emerged within the 12 month follow-up period were classified as relapse cases. Patients who were cured at the end of treatment and remained cured within the 12 month follow-up period were classified as definite cures. If patients were lost to follow-up, the last known treatment outcome was recorded. Seven pre- and post-treatment samples coming from the same patients were obtained. Patient treatment outcome after treatment with miltefosine (MIL) and pentavalent antimonials (SSG) was monitored during 12 months (at the end of treatment, month 3, month 6 and month 12 after treatment).

### Sample phenotyping

50 strains were phenotyped for their susceptibility to SSG using a standardized in vitro susceptibility test as described elsewhere (Downing et al., 2011; Rijal et al., 2007). An SSG-susceptible reference strain (BPK206/0cl10) was included in each assay. The classification into resistance and susceptible strains was determined by calculating the activity index (AI): the ratio of the EC50 of the strain in question versus the EC50 of the susceptible reference strain. AI values clustered strongly, with most strains showing an AI≤1 (25; classified as SSG-sensitive) or ≥6 (18; classified as SSG- resistant). A few strains (7) showed AI values around 3 and were considered as showing intermediate resistance.

### Genome sequencing

DNA isolation, sample preparation, DNA quantification and DNA library preparation were done as outlined previously (Downing et al., 2011). 100 bp paired-end sequence reads were generated (median coverage 44 per sample) with the Illumina Hiseq 2000 platform according to standard protocols. Read data are available under study ERP000140 at the European Nucleotide Archive (http://www.ebi.ac.uk/ena/data/view/ERP000140).

### DNA read mapping

Reads were mapped to the reference L. donovani genome BPK282/0cl4 using Smalt v5.7 (www.sanger.ac.uk/resources/software/smalt/). Options for exhaustive searching for alignments and random assignment of repetitively mapped reads were used to properly estimate read coverage. Non-mapping read exclusion, read file merging, sorting and elimination of PCR duplicates were implemented with Samtools v0.1.18 and Picard v1.85.

### Reference genome masking

The reference genome was masked at regions of the genome that were repetitive, duplicated, close to contig edges, structurally variable, or potentially mis-assembled. Five criteria masked a total of 6,358,203 bp out of the 32,444,998 bp reference genome sequence for L. donovani BPK282/0cl4, resulting in SNPs being called at 26,086,795 or 80.4% of the nuclear genome. Criteria were: 1. Manually identified repeats, commonly duplicated or deleted regions, regions with excessive rates of common SNPs and non-unique regions (Downing et al., 2011) identified with Gnuplot, the Artemis Comparison Tool, Artemis and Samtools tview (1,740,084 bp). 2. Duplicated regions determined by DNA similarity as Blast v2.2.25 (Altschul et al., 1990) hits between the two reference genome sequences for L. donovani BPK282/0cl4 and L. infantum JPCM5, with E-value less than 10e-20 (2,082,546 bp). 3. Low complexity repeat regions determined by Tantan v0.13 (www.cbrc.jp/tantan/); (2,495,070 bp). 4. 100 bp regions adjacent to each contig edge (1,641,511 bp) – initially 13.8% of candidate SNPs were in these regions. 5. The first 300 bp and last 5 kb of all chromosomes, which are more likely to contain mis-assemblies.

### SNP detection using COCALL

SNPs were ascertained using a consensus calling approach (COCALL) that is based on the framework outlined for the 1000 Genomes project (1000 Genomes Project Consortium, 2012). COCALL applied five different variant detection approaches and combines evidence from them to calculate the support for each genotype. For complete details on the algorithm testing and development, see Appendix 1. In short, this approach avoids bias associated with systematic errors unique to each individual SNP caller by examining their consistency and identifying discordant mutations symptomatic of false positives. The five callers used were FreeBayes v0.9.5, GATK 2.0–38, Samtools Pileup v0.1.16 and Mpileup v0.1.18 based on the DNA read mapping by Smalt, and Cortex v1.0.5.13 based on its own de novo assembly and mapping. In a large population of genetically homogenous strains, superior inference power was achieved by examining the population-wide genotype at each candidate SNP site (i.e. population-based COCALL; Figure 2—figure supplement 1). Candidate SNPs with genotype qualities of 40+ across all five callers were retained. SNPs with population normalized read depth ≤0.5 or ≥1.75 or with multiple derived alleles across the five callers were excluded. Candidate SNPs in soft-masked regions were accepted where the number of callers ≥3.5; those in non-masked regions were kept where the number of callers ≥2.5. SNP sites retained in the final set of retained SNP sites were supported by a mean of 4.5 callers out of 5.

### Copy number variant, somy and indel detection

Chromosomal read depths were computed using a trimmed median read depth (calculated as the median of read depths for sites with depths within one standard deviation of an initial, untrimmed, median read depth of each chromosome) and normalized as the depth per haploid genome as outlined previously (Downing et al., 2011). Somy levels were estimated as the median normalized chromosomal read depths (Downing et al., 2011). Local copy number variants (CNVs) were detected where the local read depth was significantly different from the median depth of approximately 60 samples from ICS4, ISC6 and ISC8 whose depth profile is similar to that of BPK282/0cl4, and were measured with respect to the haploid depth to exclude somy variability. Two CNVs in particular, the MAPK1 and H-locus, were further investigated as they show functions potentially relevant to parasite adaptation (Downing et al., 2011). A quantitative PCR assay in a subset of 46 samples was performed to confirm the copy number variation of the MAPK1 and H-locus amplicons. The nature of the amplification (extra- or intra-chromosomal) was determined by pulsed-field gel electrophoresis (PFGE) and southern blot hybridization comparing two strains that showed differential amplification of these loci (ISC6 strain BPK282/0cl4: amplification; and ISC1 strain BPK026/0cl5: no amplification). To exclude the possibility that the amplicons are a culturing artefact, PCRs using primers that enabled amplification of circular episomes or tandem duplications was also attempted directly on five bone marrow samples from VL patients. Indels were detected using a consensus calling method based on the concordance of results across four tools: Cortex, Freebayes, GATK and Samtools Mpileup. For complete details on the Somy, CNV, indel and episome detection, see Appendix 2.

### Haplotype inference and linkage disequilibrium

Haplotypes were inferred using PHASE v2.1.1 (Stephens et al., 2001): 0.1% of genotypes in the Core 191 and 0.9% in ISC1 had confidence scores <0.95. Haplotypes were inferred with a general recombination rate model (Li and Stephens, 2003) with ten runs, each with a burn-in of 100 steps, 100 iterations and a single MC thinning step and recombination rate estimated for each chromosome. Convergence was examined for each chromosome: recombination estimates were consistent, though there was more variation between phasing runs for chromosome 16 in the core population and consequently inferred haplotypes are less certain for that chromosome. There was no correlation between the mean chromosome copy number and mean recombination rate or PHASE probability values for inferred haplotypes (r2=0.011). While variation in somy is not explicitly accounted for in the phasing process, the rapid flux in the somy levels of aneuploid chromosomes may mean this variation has no effect on haplotype inference. Of 3,567 heterozygous sites, 3,076 (86%) had a PHASE probability of exactly 100% and 437 had PHASE probabilities < 0.95: these lower-confidence haplotypes were masked. Haplotypes for BHU1087/0 were inferred along with the core population. The phased core population SNP set had 2,401 SNPs: 17 singletons were masked. The smaller sample size meant that phasing within ISC1 was less successful: phase was successfully inferred for 2,308 sites using the same (0.95) confidence score threshold: 524 were not phased and were excluded from further analysis. No correlation between phasing confidence score and trisomy or tetrasomy was apparent.

Linkage disequilibrium (LD) was inferred as the correlation in genotypes (r2 values) between SNP pairs using Bcftools v0.1.17 screened with Samtools Mpileup given SNP mapping qualities >30 and base qualities >25. These pairwise r2 values were used to examine genome-wide LD patterns and LD decay with distance. Recombination was confirmed using the four-gamete test (Hudson and Kaplan, 1985). Mean chromosomal estimates of LD in the core population did not correlate with somy level if the tetrasomic chromosome 31 was excluded (r2=0.001) but did if chromosome 31 was included (r2=0.167). Somy had little impact on the variance of LD per chromosome (r2=0.017 with chr31, r2=0.000 without chr31). Variance in somy level across chromosomes had no association with either the mean or variance of LD per chromosome. We calculated zygosity as the probability that a SNP exists at a distance d from a SNP at a site x assuming diploidy (Lynch, 2008). No differences between homozygous and heterozygous SNP clustering measured as a product of chromosomal distance was observed.

### Population genomic identification of groups

L. infantum JPCM5 (MCAN/ES/1998/LLM-877) from Spain and LV9 (MHOM/ET/1967/HU3) from Sudan were used (Downing et al., 2012) for comparison with the L. donovani genomes generated in this study. Variants were called for these two samples using the approaches outlined above. For two additional L. donovani isolates from Sri Lanka (Zhang et al., 2014), we mapped Illumina GAII reads using Smalt v5.7 as above and called candidate SNPs at non-masked regions using Samtools Pileup v0.1.16 (Li et al., 2009), followed by screening steps as above. Two genomes were excluded in the final analyses because sequence reads were of insufficient quality (for MHOM/IN/10/BHU1087/0) or because of a suspected mixed infection (for MHOM/IN/10/BHU790/0). BHU790/0 is distantly related to the core population (most likely ISC3) and appears to be a mixed infection rather than a hybrid because its average read allele frequency of heterozygous SNPs approximates 0.17, whereas most detected hybrids had mean read allele frequencies of 0.4–0.5. Remaining data were used to construct phylogenies using the 211,536 sites containing verified SNPs in the entire sample set (ISC1/2/3/4/5/6/7/8/9/10 and ungrouped, LV9, JPCM5, BPK512/0cl9). JPCM5, LV9, the two Sri Lankan isolates and one sample from our collection (BPK512/0cl9) represented genetically distinct lineages, distinct to both the ISC1 (n=12) and core populations (n=191). Seven SNPs in the core population and ten in ISC1 had multiple derived alleles compared to reference genome sample BPK282/0cl4 (Supplementary file 2, table t). These were included in all diversity analyses, but not those involving phased haplotypes.

Genome-wide phylogenetic trees were constructed with RAxML v8.1.1 (Stamatakis, 2014) using the GTR+G substitution model and 1000 bootstrap replicates for 10 runs for the core population (881 alignment patterns), ISC1 (349 alignment patterns), and all samples including the CL and VL samples from Sri Lanka (Zhang et al., 2014) (2274 alignment patterns). The best fitting substitution model determined using MEGA v6 (Tamura et al., 2011) for the core population was GTR+G. The final phylogenies were visualised using MEGA v6 (Tamura et al., 2011) and Splitstree v4 (Huson and Bryant, 2006). Unrooted haplotype trees for the phased SNPs for each chromosome were constructed from maximum-likelihood distances for the TN93 substitution model using the package Ape (Paradis et al., 2004) v3.1–4 in R version 3.12.

Samples in the core population of 191 isolates were classified using model-based clustering as implemented in Structure v2.3.2.1 (Pritchard et al., 2000) and principal component analysis (PCA) of the allele frequencies. Given a number of genetically distinct clusters (K), samples were probabilistically assigned to a population independent of a mutation model with a prior of 1/K based on the correlation in genotypes of each sample with estimated population allele frequencies. 1≤K≤15 was examined with admixture and incomplete membership allowed to reduce overfitting. We used 105 burn-in steps before a run of 2x106 steps with three independent runs per K to confirm chain convergence. The most likely number of clusters was based on the second-order rate of change of the likelihood function (ΔK, Evanno et al., 2005). At K=4 the groups were composed of ISC2/3/9/10, ISC4, ISC5 and ISC6/7/8. Inter-population differentiation was lower for ISC2/3/9/10 (FST=0.36) compared to the others (0.85<FST<0.98). K=7 was the most probable K value (ΔK=25.8): the groups were composed of ISC2, ISC3, ISC4, ISC5, ISC6/7/8, and ISC9/10 (all FST>0.79) – the 21 ungrouped samples collectively had an FST=0. Most population membership assignments were >0.97 with few ambiguous values (range 0.80–0.97). At K=9, ISC6/7/8 split into ISC6 and ISC7/8 (both FST>0.85). At K=10, ISC7/8 segregated into ISC7 and ISC8.

### Inference of historical population sizes, geographic locations and migration rates

Dated phylogenies, historical population sizes and migration patterns were modelled for the 191 core clinical isolates using BEAST v1.8.1 (Drummond et al., 2012). For molecular clock analyses, hybrid isolates not assigned to any of the ISC groups were removed from the dataset, as were the Bangladeshi outgroups for most analyses. Dates for each were fixed to the month of isolation, with sampling dates for those for which only isolation year data was available estimated during the MCMC but given a uniform prior on sampling ages within that year. Broadly consistent date estimates were obtained under three different models: with an uncorrelated lognormal relaxed clock model and a TVM substitution model and a Bayesian skyride model for population sizes, under the same model but with a strict clock model and finally under a GTR substitution model, with a simple constant population size coalescent model for data including the outgroups. Migration rate estimates were obtained by including a simple continuous-time Markov model of a discrete trait representing the country (Nepal/India) of isolation, so that ancestral states and rates of change in geographical location were estimated along the phylogeny. All analyses were made with a minimum of 8 independent MCMC runs, for 200 million update generations per run. Convergence was assessed by inspection in Tracer v1.6, confirming that at least 5 of the 8 runs had converged to the same stationary distribution of parameters and that this had the highest likelihood. In most analyses, seven or eight chains all converged to the same posterior distribution, but the Bayesian skyride analyses converged more slowly. ESS estimates for almost all parameters across runs was over 500, except for some skyride population size parameters. The first 20 million generations of each MCMC run were removed before combining all converged runs for inference. Historical population sizes were estimated both with the Bayesian skyride model and by transforming lineage-through-time data for all trees in the posterior probability distribution from the strict clock model above using the package Ape (Paradis et al., 2004) v3.1–4 in R version 3.12. To compare population sizes between the drug resistant clade and others, we split ISC5 from other data and removed coalescent events between the ISC groups (the oldest six) to make these comparable with the ISC5 coalescence.

### Population genomic identification of admixture using allele frequency correlations

f-statistics describe the correlation in allele frequencies between populations (Patterson et al., 2012; Reich et al., 2009). The simplest (f2) is simply the sum-of-squares difference in allele frequency between two populations averaged across loci, and so captures the amount of divergence, or branch length between two populations. Two more complex statistics, f3 and f4 are calculated as differences between f2 statistics between groups of 3 and 4 related populations. f3(C;A,B) has the property that, for a population C derived from populations A and B, it is expected to be positive if A,B and C are related by a simple history of divergence and genetic drift, but negative if admixture from A or B has contributed to the genetic composition of population C, while being robust to the details of the relationship between the three populations. In contrast, the value of f4(A,B,C,D) does depend on the evolutionary history of populations A, B, C and D and so can be used to test a proposed relationship: if the four populations are related as ((A,B),(C,D)) the f4 statistic is expected to be zero; for ((A,C),(B,D)) it is expected to be positive and for ((A,D),(B,C)), negative. Finally, if the evolutionary history of three ancestral populations is known, the ratio of two f4 ratios is an estimate of the relative contribution of two potential parental populations to a fourth admixed population, given an outgroup.

### Population genomic identification of admixture using haplotype sharing

Whereas groups ISC2/3/4/5/6/7 seemed clearly defined phylogenetically and by Structure, ISC8/9/10 were not and no simple relatedness among the 21 ungrouped samples was detected. Consequently, we used inferred haplotypes to test whether these represented genetically discrete populations, or whether some of those samples were mixtures of ISC3/4/5/6/7 generated by hybridisation between these groups (Lawson et al., 2012). Chromopainter v0.0.2 and FineStructure v0.0.2 inferred ancestral patterns of haplotype similarity among samples without a prior assumption of a given number of populations or of independence between mutations.

Co-ancestry matrices for the core population were computed using Chromopainter v0.0.2 as the number of segments potentially donated to or received from individual samples, using the phased haplotypes. Recombination rates between pairs of SNPs inferred by PHASE were used for each of 36 unlinked chromosomes. Groups of SNPs on a single chromosome were expected to be exchanged as blocks of different sizes, so a higher number and longer lengths of shared blocks indicate recent common ancestry. The most likely ancestral sample or population was assigned according to its similarity to corresponding segments in a set of donor isolates. Two main datasets were generated by ChromoPainter: a co-ancestry matrix where all 191 could donate to all 191 as recipients (191x191), and another where six representative samples were used as the only donors (191x6: BD09 for ISC2, BPK067/0cl2 for ISC3, BPK087/0cl11 for ISC4, BPK275/0cl18 for ISC5, BPK282/0cl4 for ISC6, BHU200/0 for ISC7). The expected number of chunks was minimised for the six representative samples, with k=80 segments and an effective number of chunks c=0.02. Reducing the number of representative strains to represent distinct groups identified by Structure with smaller K parameters resulted in smaller k and larger c values, suggesting that using six representative samples was the optimal number for discrimination within the core population. Though ISC7 was a subset of ISC6, ISC7 had a large number of fixed SNPs sufficient to differentiate it from ISC6 with Structure, so it was included. For the 191x191 comparison, k=79 segments was expected and the effective number of chunks was lower (c=0.00054) because the total diversity of the donor set per SNP had decreased.

These 191x191 and 191x6 co-ancestry matrices represented the most probable number of segments copied from each donor to each recipient, and also the relative probability of ancestry across the set of donors for each SNP for each sample. The number of donors per recipient was set to 100. 20 expectation-maximisation algorithm iterations was sufficient to maximise the recombination-scaling coefficient (Ne) and copying probabilities with 10<k<1000 iterations across different number of donor samples assuming a minimum recombination rate of 10-15 Morgans/bp. For the 191x191 matrix, the Ne=523.3 and the mutation rate (µ) was 0.000181. For the 191x6 matrix, the Ne=1015.1 and µ=0.000628: Ne and µ were higher because there were more mutations per sample.

The 191x191 matrix was clustered for 106 MCMC (Markov chain Monte Carlo) steps with a burn-in of 10,000 and a skip of 100 steps using FineStructure v0.02 to obtain aggregated expected segment sharing between samples and populations with 100 trees examined per merge step. This distinguished complex ancestral patterns of segment sharing for the strains which Structure could not fully assign to single populations.

To verify FineStructure and Structure results, the correlation in the SNP allele frequencies across samples was examined in the core population for six principal components with p<10-7 using PCA implemented by smartPCA in Eigensoft v4.2 (Price et al., 2006). The first PC separated ISC2 (10.1% of all variation), the second ISC4 (6.4%), the third ISC5 (5.8%), the fourth ISC3 (4.9%), the fifth BPK035/0cl1 and BPK043/0cl2 (4.2%) and the sixth a subset from ISC9/10 (3.9%). This was repeated for the 2353 variable sites in the core population (ISC3/4/5/6/7/8/9/10 and ungrouped samples, n=183) excluding the 8 samples from Bangladesh (ISC2). This partitioned ISC5 (PC1, 7.4%), then ISC4 (6.8%), third ISC3 (5.6%), and fourth BPK035/0cl1-BPK043/0cl2 (4.8%). Eigenstrat and FineStructure PCA results were effectively the same but with some different axis labels – PC1 in the former was PC3 in the latter. FineStructure 191x191 ancestry patterns partitioned ISC4 vs ISC6 over PC1 (16.8% of variation), and ISC5 vs ISC6 over PC2 (15.5%). The next (12.3%) differentiated ISC2, and PCs 4 (6.4%) and 5 (5.7%) separated ISC3. PC6 in FineStructure differentiated the BPK035/0cl1-BPK043/0cl2 pair.

### Population genomic identification of drug-resistance elements

Information on in vitro SbV-resistance was available for 50/191 Core 191 isolates, from which 25 were sensitive and 25 resistant (Supplementary file 1). Links between genetic diversity (SNP, indel, CNV and somy) and in vitro SbV-resistance were assessed using the Fisher Exact test (FET), Mann Whitney U-tests (MWU) and odds ratios (ORs), implemented on 103 CNVs and 17 indels (in 14 genes) as well as 2,392 phased SNPs genotypes. SNPs were assigned to the 5’ and 3’ UTR if they were within 1 kb of the start or end of the gene (respectively). To counter bias associated with the small sample size, FET and MWU were used initially. For the FET, variants were defined as discrete variables: SNPs as 0, 1 or 2 non-reference alleles, and small indels as the diploid number of inserted or deleted basepairs. For the MWU, mutations were considered as a continuous variable such that the somy state was the haploid chromosome state, and CNVs were the haploid copy number times the somy state. The null hypothesis was that there were no significant genetic differences between SbV-R and SbV-S strains (subject to p<0.01). The FETs and MWU were limited by the partial association of different mutations with the phenotypes, so we examined ORs of the derived alleles segregating in multiple ISC populations with 6+ non-reference alleles for which the absolute difference in SbV-R and SbV-S allele frequencies >0.1 using the log-scaled EC50 values. We compared the log-scaled EC50 values of each allele pair using t-tests.

We also examined samples for which the patient was treated with SbV and was either cured or not, samples for which the patient was treated with miltefosine (MIL) and was either cured or not, and also in vitro MIL resistance levels as implemented above for SbV.

### Testing for selective processes among ISC populations

Evidence of historical differences in selective processes on the ancestors of the major ISC populations was assessed as the rate of accumulation of derived alleles. Stronger purifying selection should purge deleterious derived alleles more quickly, detected as an excess of nonsynonymous changes relative to synonymous ones, as previously observed for ISC isolates (Downing et al., 2011). This signature should be most apparent for derived alleles, which should accumulate at a net rate dependent on the historical effective population sizes and selective coefficients. Using L. infantum JPCM5 as the outgroup, the relative abundance of derived alleles in one population that were absent in the other for each ISC population pair (ISC2-7) were determined as the statistic R (Do et al., 2015). The associated ratio R2 denoted the relative rate of homozygous derived allele accumulation between populations. R and R2 should approximate 1 assuming no difference in the strength of selection, and primarily depend on the derived allele frequency per population, so the main confounder was variance in historical effective population sizes among ISC populations. To calculate confidence intervals for these R values that take into account correlation between neighbouring sites, we used a Weighted Block Jackknife by splitting the SNPs according to chromosome (Busing et al., 1999) to counter the extensive linkage disequilibrium between SNPs (Moorjani et al., 2011): discrete chromosomal blocks may still be linked. This was adjusted for the number of SNPs per block to reflect the variability in the relative selective pressure (Kunsch, 1989). A threshold of four times the standard error of these jackknife estimates was used as a criteria for identifying comparisons deviating significantly from expected values (Do et al., 2015).

### AQP1 modelling

A protein model of the intact Leishmania donovani AQP1 from BPK282/0cl4 was created using MODELLER 9.14 (Sali and Blundell, 1993). The template for homology modelling was the crystal structure of the aquaglyceroporin from Plasmodium falciparum in complex with glycerol (PDB code: 3c02) published by Newby and co-workers (Newby et al., 2008). The sequence identity between the target and the template was approximately 33%. PyMOL version 1.50.04 (Schrödinger) was used to generate the biological units for the aquaglyceroporin from Plasmodium falciparum (generation of symmetry mates function in pymol). The C-alpha atoms of chain A, B, C and D of the tetramer template were restrained during homology modeling using MODELLER in order to reduce the number of interatomic distances that needed to be calculated.
