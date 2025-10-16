# DNA methylation in Arabidopsis has a genetic basis and shows evidence of local adaptation

## Authors

- Manu J Dubin<sup>1</sup> †
- Pei Zhang<sup>1</sup>
- Dazhe Meng<sup>1</sup>
- Marie-Stanislas Remigereau<sup>2</sup>
- Edward J Osborne<sup>3</sup>
- Francesco Paolo Casale<sup>4</sup>
- Philipp Drewe<sup>5</sup>
- André Kahles<sup>5</sup>
- Geraldine Jean<sup>5</sup>
- Bjarni Vilhjálmsson<sup>1</sup>
- Joanna Jagoda<sup>1</sup>
- Selen Irez<sup>1</sup>
- Viktor Voronin<sup>1</sup>
- Qiang Song<sup>2</sup>
- Quan Long<sup>1</sup>
- Gunnar Rätsch<sup>5</sup>
- Oliver Stegle<sup>4</sup>
- Richard M Clark<sup>3</sup>
- Magnus Nordborg<sup>1</sup> ([ORCID: 0000-0001-7178-9748](https://orcid.org/0000-0001-7178-9748)) †

### Affiliations

1. Gregor Mendel Institute, Austrian Academy of Sciences Vienna Biocenter Vienna Austria
2. Molecular and Computational Biology University of Southern California Los Angeles United States
3. Department of Biology University of Utah Salt Lake City United States
4. European Molecular Biology Laboratory, European Bioinformatics Institute Wellcome Trust Genome Campus Cambridge United Kingdom
5. Friedrich Miescher Laboratory Max Planck Society Tübingen Germany
6. Memorial Sloan-Kettering Cancer Center New York United States
7. Center for Cell and Genome Science University of Utah Salt Lake City United States

† Corresponding author

## Abstract

10.7554/eLife.05255.001 Epigenome modulation potentially provides a mechanism for organisms to adapt, within and between generations. However, neither the extent to which this occurs, nor the mechanisms involved are known. Here we investigate DNA methylation variation in Swedish Arabidopsis thaliana accessions grown at two different temperatures. Environmental effects were limited to transposons, where CHH methylation was found to increase with temperature. Genome-wide association studies (GWAS) revealed that the extensive CHH methylation variation was strongly associated with genetic variants in both cis and trans , including a major trans -association close to the DNA methyltransferase CMT2. Unlike CHH methylation, CpG gene body methylation (GBM) was not affected by growth temperature, but was instead correlated with the latitude of origin. Accessions from colder regions had higher levels of GBM for a significant fraction of the genome, and this was associated with increased transcription for the genes affected. GWAS revealed that this effect was largely due to trans -acting loci, many of which showed evidence of local adaptation. DOI: http://dx.doi.org/10.7554/eLife.05255.001

## Main

To better understand how genotype and environment interact to affect DNA methylation and transcription, we grew 150 Arabidopsis thaliana accessions from Sweden (Long et al., 2013) in two different environments, 10°C and 16°C, chosen because they lead to very different flowering behavior (Atwell et al., 2010). Relying on existing genome sequence information (Long et al., 2013), methylome- and transcriptome-sequencing data were generated (see ‘Materials and methods’).

In plants, DNA methylation occurs on cytosines in the CG, CHG, and CHH contexts (where H is any nucleotide except for C), each of which is catalyzed by independent pathways (

![Figure 1.](https://cdn.elifesciences.org/articles/05255/elife-05255-fig1-v1.jpg)

**Figure 1.:** (A) Genome-wide average methylation level reaction norms for each accession (156 samples at 10°C and 125 samples at 16°C). Only CHH levels differ significantly between temperatures (Wilcoxon rank sum test; p = 1.7e-16). (B) Manhattan plot of genome-wide association studies (GWAS) results using average levels of CHH methylation for 151 accessions at 10°C on large transposons as the phenotype (the peak is also seen at 16°C [not shown]). The threshold line indicates a Bonferroni-corrected p-value of 0.05. (C) CHH methylation on large (over 2 kb) transposons at 10°C by CMT2 two-locus genotype (population sizes are 36, 82, and 24 for CMT2anr/nr/CMT2br/r, CMT2ar/r/CMT2br/r, CMT2ar/r/CMT2bnr/nr, respectively). The values plotted are the Best Linear Unbiased Predictor (BLUP) estimates after correcting for population structure. Since accessions are homozygous, only four genotypes are possible, of which only three exist due to complete linkage disequilibrium between CMT2a and CMT2b. Figure 1—figure supplement 1 shows Manhattan plots of GWAS results for global methylation averages. Figure 1—figure supplement 2 shows Stepwise GWAS using average CHH methylation of TE's.DOI: http://dx.doi.org/10.7554/eLife.05255.003

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/05255/elife-05255-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** (A) CG methylation at 10°C. (B) CHG methylation at 10°C. (C) CHH methylation at 10°C. Results for methylation at 16°C were similar (data not shown).DOI: http://dx.doi.org/10.7554/eLife.05255.004

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/05255/elife-05255-fig1-figsupp2-v1.jpg)

**Figure 1—figure supplement 2.:** (A) Without a cofactor. (B) Including SNP on chr 4 at position 10,459,127 (CMT2a) as a cofactor. (C) Including snps on chr 4 at 10,459,127 (CMT2a) and 10,454,628 (CMT2b) as cofactors. The threshold line indicates a Bonferroni-corrected p-value of 0.05.DOI: http://dx.doi.org/10.7554/eLife.05255.005

The association centered around a SNP at 10,459,127 on chromosome 4, 38 kb downstream from the locus AT4G19020, which encodes a homolog of the CHG methyltransferase chromo-methylase-3 (

![Figure 2.](https://cdn.elifesciences.org/articles/05255/elife-05255-fig2-v1.jpg)

**Figure 2.:** (A) CHH methylation on large transposons by CMT2 genotype in an F2 population of 113 individuals (population sizes are 19, 52, and 38 for CMT2anr/nr/CMT2br/r, CMT2ar/r/CMT2br/r, CMT2ar/r/CMT2bnr/nr, respectively; 4 individuals whose genotype at CMT2 could not be accurately inferred were omitted). (B) Mapping of CHH methylation of long TEs in the same population. The dotted line indicates a LOD threshold with a genome-wide p-value of 0.05 obtained using 1000 permutations, and the vertical blue line shows the marker interval that contains CMT2.DOI: http://dx.doi.org/10.7554/eLife.05255.006

The effect of genetic variation on local CHH methylation was examined by calculating the methylation level in 200 bp sliding windows across the genome (100 bp overlap between windows) and running GWAS for the 200,000 differentially methylated regions (DMRs; see ‘Materials and methods’) that varied most between individuals. 36023 DMRs had at least one genome-wide significant association (Bonferroni-corrected p-value of 0.05; 7273 remain after correcting for multiple GWAS using an FDR of 0.05). 45% (15,031) of the DMRs had a significant

![Figure 3.](https://cdn.elifesciences.org/articles/05255/elife-05255-fig3-v1.jpg)

**Figure 3.:** (A) GWAS for CHH differentially methylated regions (DMRs) at 10°C in 151 accessions, defined using 200 bp sliding windows across the genome and selecting the 200,000 most variable ones. For each DMR, SNPs significantly associated at the Bonferroni-corrected 0.05-level are plotted. (B) Variance-components analysis of the CHH DMRs. For each DMR, a mixed model with cis, CMT2, and genome-wide trans effects, plus environment and genetic interactions with environment was fitted (see ‘Materials and methods’). DMRs were binned by the total variance explained by the model. The density of DMRs in each bin is shown at the top, and the bottom shows the average variance-decomposition for each bin.DOI: http://dx.doi.org/10.7554/eLife.05255.007

To quantify the regulation of DMRs, we partitioned the variance of CHH methylation into environmental (E), CMT2, CMT2 X E, cis, cis X E, trans, and trans X E using a mixed model (Figure 3B). The analysis confirmed substantial cis and trans associations, with the environment modulating the genetic effects rather than having a major direct effect. At least for the cis associations, a possible explanation is that SNPs tag polymorphic TE insertions, with the insertion allele being silenced in a temperature-sensitive manner.

The effect of temperature on CHH methylation could also be seen at the local level. We defined ‘temperature DMRs’ by looking for windows that differed significantly between temperatures. Comparing 16°C–10°C, each accession on average gained CHH methylation at ∼400 temperature DMRs and lost it at ∼200 temperature DMRs (false discovery rate = 0.05). CHH methylation is associated with transposable elements (TEs;

![Figure 4.](https://cdn.elifesciences.org/articles/05255/elife-05255-fig4-v1.jpg)

**Figure 4.:** (A) Average methylation levels over variable transposons at 10°C (orange) vs 16°C (red), and over non-variable transposons at 10°C (purple) vs 16°C (dark blue). Methylation for variable TEs is significantly higher (permutation p-value for CHH methylation = 0.05). (B) The density of variable (red) and non-variable TEs along chromosomes in 500 kb windows. Density is defined as the percentage of the total number in either category in each window; pericentromeric regions are shaded grey. (C) The expression of TEs at both temperatures. Variable TEs are more highly expressed than non-variable TEs, but the difference is only statistically significant at 16°C (Wilcoxon: 10°C, p = 0.15; 16°C, p = 0.023).DOI: http://dx.doi.org/10.7554/eLife.05255.008

In order to gain further insight into the mechanisms responsible for variation in CHH methylation, we bisulfite-sequenced knockout lines of CMT2 (SAIL_906_G03) and DCL3 (

![Figure 5.](https://cdn.elifesciences.org/articles/05255/elife-05255-fig5-v1.jpg)

**Figure 5.:** CHH methylation at CMT2- and DCL3-dependent DMRs in natural accessions grown at 10°C and 16°C (cf. Figure 1A, each population has 110 individuals). The difference between temperatures was highly significant for both types of DMR (Wilcoxon p-value = 9.1e-11 and p-value = 5.9e-12 respectively). Black points/grey lines indicate accessions with the CMT2 reference allele; green, the CMT2a non-reference allele; and orange, the CMT2b non-reference allele. Red is the TAA-03 accession, which has a putative null allele of CMT2. Average methylation levels for each of the genotypes are shown in bars to the side Figure 5—figure supplement 1 shows GWAS on CMT2 and DCL3 dependant DMRs. Figure 5—figure supplement 2 shows a putative null allele of CMT2.DOI: http://dx.doi.org/10.7554/eLife.05255.010

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/05255/elife-05255-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** (A) GWAS for CMT2-dependent DMRs at 10°C. (B) GWAS on DCL3-dependent DMRs at 10°C. Results from 16°C were similar in both cases. The threshold line indicates a Bonferoni-corrected p-value of 0.05.DOI: http://dx.doi.org/10.7554/eLife.05255.011

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/05255/elife-05255-fig5-figsupp2-v1.jpg)

**Figure 5—figure supplement 2.:** A screenshot from a genome browser indicating the lack of read coverage for CMT2 stretching from intron 7 to exon 16 in the accession TAA-03.DOI: http://dx.doi.org/10.7554/eLife.05255.012

Interestingly, we observed one accession from northern Sweden, TAA-03, with almost undetectable levels of CHH methylation at CMT2-dependant DMRs (Figure 5). Further investigation suggested that it has a deletion or rearrangement in CMT2, as we were unable to map reads between positions 2813 and 4944 (intron 7 to exon 16, Figure 5—figure supplement 2). Sanger-sequencing indicates the insertion of a stretch of TC dinucleotide repeats of at least 330 bp. The same deletion appears to be present in three more accessions from northern Sweden (TAA-14, TAA-18, and Gro-3) a situation reminiscent of the homologous CMT1 gene, which seems to be non-functional in most Arabidopsis accessions (Henikoff and Comai, 1998). Although CMT2 null alleles have no obvious phenotype, the gene is highly conserved in plants (with the exception of maize; Zemach et al., 2013; West et al., 2014).

It has recently been suggested that natural variation in CMT2 is associated with adaptation to climate (

![Figure 6.](https://cdn.elifesciences.org/articles/05255/elife-05255-fig6-v1.jpg)

**Figure 6.:** (A) Global CG methylation levels at 10°C for 151 accessions are strongly correlated with minimum temperature at the location of origin. Results for 16°C are similar. (B) Genes with GBM are more highly expressed at 10°C in northern (blue) than in southern (red) accessions (wilcoxon rank sum test p = 2.1e-03), whereas genes without GBM show little difference (p = 1.9e-02). At 16°C the difference for genes with GBM is more significant (p = 6.4e-05), whereas the difference for genes without GBM is insignificant (p = 0.49).DOI: http://dx.doi.org/10.7554/eLife.05255.014

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/05255/elife-05255-fig6-figsupp1-v1.jpg)

**Figure 6—figure supplement 1.:** Above, GBM at 10°C and 16°C. Below, TE CG methylation at 10°C and 16°C.DOI: http://dx.doi.org/10.7554/eLife.05255.015

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/05255/elife-05255-fig6-figsupp2-v1.jpg)

**Figure 6—figure supplement 2.:** (A) Genes with low or no CHG methylation have variable levels of CG methylation, while genes with appreciable CHG methylation have very high CG (and CHH) methylation. (B) Among genes with only CG GBM, variance-component analysis reveals a bimodal distribution of the total variance explained: variation in methylation for genes with low levels of methylation typically does not appear to have a genetic basis.DOI: http://dx.doi.org/10.7554/eLife.05255.016

![Figure 6—figure supplement 3.](https://cdn.elifesciences.org/articles/05255/elife-05255-fig6-figsupp3-v1.jpg)

**Figure 6—figure supplement 3.:** The histogram shows the average methylation level for each individual CG dinucleotide on GBM genes in all accessions in the north (blue) or in the south (red).DOI: http://dx.doi.org/10.7554/eLife.05255.017

![Figure 6—figure supplement 4.](https://cdn.elifesciences.org/articles/05255/elife-05255-fig6-figsupp4-v1.jpg)

**Figure 6—figure supplement 4.:** The histogram shows the average methylation level for each individual CG dinucleotide on GBM genes in all accessions in the north minus the average methylation level in the south for each dinucleotide.DOI: http://dx.doi.org/10.7554/eLife.05255.018

![Figure 6—figure supplement 5.](https://cdn.elifesciences.org/articles/05255/elife-05255-fig6-figsupp5-v1.jpg)

**Figure 6—figure supplement 5.:** DOI: http://dx.doi.org/10.7554/eLife.05255.019

![Figure 6—figure supplement 6.](https://cdn.elifesciences.org/articles/05255/elife-05255-fig6-figsupp6-v1.jpg)

**Figure 6—figure supplement 6.:** Mean per-gene variation in expression between 10°C and 16°C is reduced for GBM containing genes in northern (blue) accessions compared to southern (red) accessions (wilcoxon rank sum test p = 1.2e-05), whereas for genes without GBM the difference between north (light blue) and south (pink) is insignificant.DOI: http://dx.doi.org/10.7554/eLife.05255.020

As for CHH DMRs, the genetic basis of GBM was examined using a variance-component approach (

![Figure 7.](https://cdn.elifesciences.org/articles/05255/elife-05255-fig7-v1.jpg)

**Figure 7.:** (A) Variance component analysis of GBM. (B) Significant associations (Bonferroni-corrected 0.05-level) from a GWAS of GBM for individual genes. (C) Correlation between non-reference allele at associated SNPs and GBM.DOI: http://dx.doi.org/10.7554/eLife.05255.021

![Figure 8.](https://cdn.elifesciences.org/articles/05255/elife-05255-fig8-v1.jpg)

**Figure 8.:** (A) Correlation between non-reference allele at associated SNPs and latitude. (B) Non-reference allele frequency distribution for cis and trans SNPs compared to random SNPs. (C) Accessions carrying the non-reference alleles are limited to northern Sweden (accessions with the non-reference allele at 8 or more of the 15 loci blue, remaining accessions are red).DOI: http://dx.doi.org/10.7554/eLife.05255.022

![Figure 8—figure supplement 1.](https://cdn.elifesciences.org/articles/05255/elife-05255-fig8-figsupp1-v1.jpg)

**Figure 8—figure supplement 1.:** DOI: http://dx.doi.org/10.7554/eLife.05255.023

The 15 highly associated trans-SNPs were largely limited to northern Sweden, and were in strong linkage disequilibrium with each other (Figure 8—figure supplement 1). A. thaliana from northern Sweden show signs of multiple strong selective sweeps (Long et al., 2013) and harbors many polymorphisms that appear to be involved in local adaptation (specifically to minimum temperature; Hancock et al., 2011). The 15 SNPs were more than ninefold over-represented in the previously identified sweep regions (empirical p-value = 5.1e-03) and over fivefold over-represented within 2 kb of SNPs in the 1% tail of those associated with minimum temperature (Hancock et al., 2011) (empirical p-value = 3.1e-04), (Table 3). The ancestral state could be determined for 10 of the 15 SNPs, and in 8 of these cases, the non-reference allele was derived, further supporting sweeps in northern Sweden.10.7554/eLife.05255.024Table 3.15 SNPs associated with gene body methylation (GBM) at 5 or more genesDOI: http://dx.doi.org/10.7554/eLife.05255.024ChrPositionAssociated with GBM at how many genes?Non-reference allele countSNP-latitude correlationOverlap with sweep (Long et al., 2013)Overlap with min. temp. Assoc. SNPs (Hancock et al., 2011)19122918420.73none1_914088_0.21144051035660.64nonenone176141015480.66nonenone1197559675880.75none1_19757140_0.24269986316550.872_6931030none276550166810.612_7613651none276604699550.782_76136512_7662427_0.30276660595690.722_76136512_7665507_0.25276808825820.632_7613651none279157126510.83none2_7913782_0.23293824955730.71none2_9383856_0.34296538789480.80nonenone34193098660.68nonenone45199828660.70nonenone4132900345740.74nonenone

That the difference in GBM between north and south is likely to reflect local adaptation is also clear from its relative magnitude. The north vs south divide explains a much higher fraction of the additive genetic variance for GBM (Qst = 0.772; see ‘Materials and methods’) than of the SNP variance (Fst = 0.187). This strongly suggest that the phenotypic differentiation is driven by selection rather than genetic drift (Leinonen et al., 2013).

Identifying the causal variants is challenging, a gene-ontology analysis of genes within 100 kb (the average size of the sweep regions, Long et al., 2013), of the 15 trans-SNPs found enrichment of loci associated with mRNA transcription (GO0009299, p-value = 2.62e-03). Genes involved in epigenetic processes are not captured well by standard gene-ontology, but we found that genes from the plant chromatin database (www.chromdb.org/) were significantly overrepresented in these regions as well (permutation p-value = 0.012; Table 4).10.7554/eLife.05255.025Table 4.Genes in the plant chromatin database that are within 100 kb of one of the 15 SNPs associated with GBM at 5 or more genesDOI: http://dx.doi.org/10.7554/eLife.05255.025ChromDBLocusARID3AT2G17410ARP3AT1G13180CHB4AT1G21700CHR9AT1G03750CHR35AT2G16390CONS3AT3G02380DNG12AT1G21710FLCP39AT3G02310FLCP16AT2G22630FLCP9AT2G22540GTI1AT2G22720HMGB4AT2G17560JMJ27AT4G00990NFA1AT4G26110SDG23AT2G22740SDG37AT2G17900YDG2AT2G18000HON3AT2G18050

We also looked for genes whose expression variation is consistent with a causal role. We identified 68 genes within 100 kB of one of the 15-trans SNPs whose expression is highly correlated (Wilcoxon test p < 0.001) with the adjacent SNP after correction for population structure (Table 5). No significant enrichment of Gene Ontology terms was observed among these genes, and manual inspection identified no proteins directly involved in DNA methylation. Instead, a number of proteins involved in the regulation of gene expression and/or chromatin accessibility were present (Table 5). This may suggest that the increased gene-body methylation observed in the north is not directly due to increased DNA methylation, but may be caused by increases in gene expression driven either by differences in transcription factors networks or chromatin compaction. Identification of the causal variants behind this phenomenon should provide insight into how plants adapt to their local environment.10.7554/eLife.05255.026Table 5.Genes within 100 kb of the 15 SNPs associated with GBM at 5 or more genes whose expression is also correlated with the SNPDOI: http://dx.doi.org/10.7554/eLife.05255.026SNPLocusDesciptionp-value1_19755967AT1G53030Encodes a copper chaperone4.72E-071_19755967AT1G52880NO APICAL MERISTEM (NAM) Transcription factor with a NAC domain5.47E-071_19755967AT1G52990Thioredoxin family protein2.36E-051_19755967AT1G52780Protein of unknown function (DUF2921)1.46E-041_4405103AT1G12750RHOMBOID-like protein 6 (RBL6); FUNCTIONS IN: serine-type endopeptidase activity3.74E-081_4405103AT1G12790RuvA domain 2-like2.76E-051_4405103AT1G12730GPI transamidase subunit2.81E-051_4405103AT1G13080CYTOCHROME P450 FAMILY 71 SUBFAMILY B POLYPEPTIDE 2 (CYP71B2)1.65E-041_7614101AT1G21790TRAM LAG1 and CLN8 (TLC) lipid-sensing domain containing protein1.10E-051_7614101AT1G21900Encodes an ER-localized p24 protein8.81E-051_7614101AT1G21760F-BOX PROTEIN 7 (FBP7) putative translation regulator in temperature stress response8.54E-041_912291AT1G03660Ankyrin-repeat containing protein1.26E-101_912291AT1G03770RING1B protein with similarity to polycomb repressive core complex1 (PRC1)5.76E-071_912291AT1G03940HXXXD-type acyl-transferase family protein1.18E-061_912291AT1G03610Protein of unknown function (DUF789)6.91E-061_912291AT1G03580Pseudogene with weak similarity to ubiquitin-specific protease 121.29E-051_912291AT1G03830Guanylate-binding family protein3.50E-052_6998631AT2G16340Unknown protein1.35E-082_6998631AT2G16210Transcriptional factor B3 family protein1.69E-042_7666059AT2G17630Pyridoxal phosphate (PLP)-dependent transferases superfamily protein2.47E-182_7660469AT2G17620Cyclin B2;1 (CYCB2;1)9.68E-072_7655016AT2G17740Cysteine/Histidine-rich C1 domain family protein1.22E-042_7655016AT2G17420NADPH-DEPENDENT THIOREDOXIN REDUCTASE 2 (NTR2)9.96E-042_7666059AT2G17430MILDEW RESISTANCE LOCUS O 7 (MLO7)7.56E-042_7915712AT2G18100Protein of unknown function (DUF726)1.73E-062_7915712AT2G17980ATSLY member of SLY1 Gene Family1.33E-052_7915712AT2G18400Ribosomal protein L6 family protein1.26E-042_7915712AT2G18150Haem peroxidase8.05E-042_7915712AT2G18050HISTONE H1-3 (HIS1-3)9.47E-042_9382495AT2G22260HOMOLOG OF E. COLI ALKB (ALKBH2) enzyme involved in DNA methylation damage repair1.21E-082_9382495AT2G21850Cysteine/Histidine-rich C1 domain family protein5.38E-062_9382495AT2G22240MYO-INOSITOL-1-PHOSPHATE SYNTHASE 1 (MIPS1)8.71E-052_9382495AT2G21940SHIKIMATE KINASE 1 (ATSK1) localized to the chloroplast1.80E-042_9653878AT2G22660Protein of unknown function (duplicated DUF1399)2.22E-142_9653878AT2G22900Galactosyl transferase GMA12/MNN10 family protein5.08E-092_9653878AT2G22830Squalene epoxidase 2 (SQE2)3.91E-062_9653878AT2G22640BRICK1 (BRK1)6.17E-052_9653878AT2G22540SHORT VEGETATIVE PHASE (SVP) Floral repressor involved in thermosensory pathway2.46E-042_9653878AT2G22570NICOTINAMIDASE 1 (NIC1)2.67E-042_9653878AT2G22770NAI1 Transcription factor7.71E-043_419309AT3G02220Protein of unknown function (DUF2039)2.06E-163_419309AT3G02230REVERSIBLY GLYCOSYLATED POLYPEPTIDE 1 (RGP1)4.58E-143_419309AT3G02300Regulator of chromosome condensation (RCC1) family protein1.25E-103_419309AT3G02120Hydroxyproline-rich glycoprotein family protein1.81E-093_419309AT3G01980Short-chain dehydrogenase/reductase (SDR)3.91E-093_419309AT3G02370Unknown protein4.53E-083_419309AT3G02020ASPARTATE KINASE 3 (AK3)4.18E-073_419309AT3G02160Bromodomain transcription factor2.60E-063_419309AT3G02390Unknown chloroplast protein5.60E-063_419309AT3G02050K+ UPTAKE TRANSPORTER 3 (KUP3)1.28E-053_419309AT3G02125Unknown chloroplast protein2.12E-053_419309AT3G02200Proteasome component (PCI) domain protein1.16E-043_419309AT3G02180SPIRAL1-LIKE3 Regulates cortical microtubule organization4.56E-043_419309AT3G02250O-fucosyltransferase family protein5.31E-043_419309AT3G02110Serine carboxypeptidase-like 25 (scpl25)6.18E-044_13290034AT4G26255Non-coding RNA of unknown function1.67E-134_13290034AT4G26450WPP DOMAIN INTERACTING PROTEIN 1 (WIP1)1.13E-044_13290034AT4G26230Ribosomal protein L31e family protein1.74E-044_13290034AT4G26160ATYPICAL CYS HIS RICH THIOREDOXIN 1 (ACHT1)5.72E-044_519982AT4G01090Protein of unknown function (DUF3133)1.23E-064_519982AT4G01230Reticulon family protein2.33E-054_519982AT4G01410Late embryogenesis abundant (LEA) hydroxyproline-rich glycoprotein family5.44E-054_519982AT4G01330Serine/threonine-protein kinase2.22E-044_519982AT4G01200Calcium-dependent lipid-binding (CaLB domain) family protein3.93E-044_519982AT4G01390TRAF-like family protein3.99E-044_519982AT4G01040Glycosyl hydrolase superfamily protein5.66E-044_519982AT4G01000Ubiquitin-like superfamily protein8.55E-04

In conclusion, genes with GBM are generally up-regulated and more heavily methylated in northern accessions, and the change appears to be due to trans-acting polymorphisms that have been subject to directional selection. The candidate regions show an overrepresentation of genes involved in transcriptional processes. We also found that CHH methylation of TEs is temperature sensitive, and identified a major trans-acting controller, CMT2. Taken together, these observations suggest that local adaptation in A. thaliana involves genome-wide changes in fundamental mechanisms of gene regulation, perhaps as a form of temperature compensation.

## Materials and methods

## Raw data generation

## Plant growth

A diverse set of 150 Swedish accessions were sown on soil and stratified for 3 days at 4°C in the dark. They were then transferred to environmentally controlled growth chambers set at 10°C or 16°C under long day conditions (04:00–20:00) and individual seedlings were transplanted to single pots after 1 week. When plants attained the 9-true-leaf stage of development, whole rosettes were collected between 15:00 and 16:00 hr and flash frozen in liquid nitrogen.

In addition, a cross between the T550 and Brösarp-11-135 accessions was created and F2 seed obtained. 113 individual F2 lines were grown in the same manner as the accessions.

## RNA-seq library preparation

For each accession, three plants were pooled and total RNA was extracted by TRIzol (Invitrogen, Carlsbad, California, 15596-018), DNase treated and mRNA purified with oligo dT Dynabeads (Life Technologies, Carlsbad, California). RNA was then fragmented using Ambion Fragmentation buffer (Life Technologies) and first and second strand cDNA synthesis was carried out using Invitrogen kit 18064-071. The ends of sheared fragments were repaired using Epicentre (Madison, Wisconsion) kit ER81050. After A-tailing using exo-Klenow fragment (New England Biolabs, Ipswich, Massachusetts, NEB M0212L), barcoded adaptors were ligated with Epicentre Fast-Link DNA Ligation Kit (Epicentre LK6201H). Adaptor-ligated DNA was resolved on 1.5% low melt agarose gels for 1 hr at 100 V. DNA in the range of 200–250 bp was excised from the gel and purified with the Zymoclean Gel DNA recovery kit (Zymo Research). The libraries were amplified by PCR for 15 cycles with Illumina PCR primers 1.1 and 1.2 with Phusion polymerase (NEB F-530L).

Single-end 32 bp sequencing was performed at the University of Southern California Epigenome Center on an Illumina (San Diego, California) GAIIx instrument using fourfold multiplexing.

## MethylC-seq library preparation

For each accession two individual plants were pooled and total DNA was extracted using CTAB and phenol-chloroform. Approximately two micrograms of genomic DNA was used for MethylC-seq library construction and sequencing (92 bp paired-end) by BGI.

## Sequence analysis

## Genome sequences

Illumina sequencing data from 180 published Swedish genomes (Long et al., 2013) were combined with sequencing data from another 79 (1001genomes.org), which had been processed using the same pipeline to yield polymorphism data for a total of 259 accessions (including those used for MethylC-seq and RNA-seq here). Linkage disequilibrium calculated using the R package LDHeatmap (version 0.9.1; Shin et al., 2006).

## RNA-seq data processing

## Read mapping

After demultiplexing, 36 bp RNA-Seq reads were trimmed from barcodes (4 nt) and mapped to the TAIR10 reference genome including known variation with the PALMapper aligner (Jean et al., 2010) using a variant-aware alignment strategy. Two different sources of variants were used: (1) single nucleotide variants (SNV) and structural variants (SV) from genome sequencing (2.1) and (2) SNVs and SVs called in an initial alignment round of the RNA-Seq reads to the TAIR10 reference genome with PALMapper (relevant parameters: -M 4 -G 4 -E 6 -I 25000 -NI 1 -S). For both sources of variants we applied stringent filter criteria to reduce false calls: (1) genome variants had to appear in at least 40 strains with a minor allele count of at least 5 strains, (2) RNA-Seq variants had to be confirmed by at least 2 alignments within the same strain and had to have less than factor 2 many non-confirming alignments within the same strain. Variants from both sources were integrated into one file that was used for a second, variant-aware alignment round with PALMapper (relevant parameters: -M 2 -G 0 -E 2 -I 5000 -NI 0 -S). In variant-aware alignment mode, PALMapper builds an implicit representation of the reference genome that reflects all possible variant combinations that exist for a genomic region. The output is automatically projected to the TAIR10 coordinate system. To account for reads ambiguously mapping to multiple locations in the genome, we used a custom python script (Supplementary file 3) to remove all reads that showed at least one mapping additional to the best hit with the same edit distance. Additional hits were only counted as ambiguous, if they differed at least 3 nt in start and stop coordinates to the best hit. On average, 5.7 M reads were mapped per sample after removal of ambiguous reads. Low complexity libraries with less than 30% of mappable reads or samples with less than 800,000 mappable reads (6 in total) where excluded from further analysis.

## Sample validation

To correct for possible sample or data mix-ups, SNP were called from the RNA-seq alignments using a custom python script and compared to independently collected SNPs from the Arabidopsis 250K SNP array (Supplementary materials; Kim et al., 2007). Samples not matching the expected genotype were reassigned to the correct genotype where possible or otherwise excluded from further analysis.

## Filter for gene expression quantification

We quantified gene expression by counting the number of reads that were longer than 24 bp and that mapped to genes on all non-chloroplast and non-mitochondrial chromosomes. To obtain a stable quantification, we only used those reads that were uniquely mapped into the exonic regions of genes. Furthermore, we required that the reads did not map completely into regions where two genes overlap in order to avoid mixing quantifications of different genes. In the later text we will refer to this estimate as the raw expression estimate.

We also quantified the gene expression when additionally accounting for SV, alternative splicing and repetitive sequences that can all bias gene expression quantification. This estimate will be referred to as sv-corrected expression. For this quantification we additionally filtered for reads that start in an insertion or deletions and their two neighboring bases, that mapped into regions that are not contained in all transcripts of a gene and reads which were mapped completely into regions which are repetitive based on a 50 bp window.

## Quantification per ecotype and environment

After filtering (see ‘Filter for gene expression quantification’), there were 499 RNA-Seq libraries left for analysis. Next, we merged libraries per ecotype and environment, yielding 323 unique merged RNA-Seq libraries for a unique ecotype and environment (160 in 10°C, 163 in 16°C).

## Estimation of library size and abundance estimates

We followed the low level normalization proposed by Anders and Huber (2010), jointly applied to the set of expression estimates across ecotypes and environmental backgrounds. First, we estimated effective library sizes as the median expression estimates across all genes. Based on this, we derived correction factors to adjust individual libraries for differences in size.

## RKPM values

Library-size adjusted raw counts were used to obtain standard read counts per million expression estimates for each gene.

## MethylC-seq data processing

## Read mapping

Reads were aligned as previously described (Dinh et al., 2012) to a modified pseudo-reference chromosome in which SNPs were inserted into the TAIR10 reference genome using NextGenMap (version 0.4.3; Sedlazeck et al., 2013) allowing up to 10% mismatch between the reads (-i 0.90) and the reference sequence and discarding reads that map equally well to more than one genomic location or have less than 45 nucleotides mapping without error to the reference sequence (-R 45). Average coverage was 12.6 X.

To correct for sample or data mix-ups, the raw data was also aligned to the first chromosome of the Columbia-0 TAIR reference genome as described above and SNP calling performed using the BISsnp package (Liu et al., 2012). The polymorphism data were then compared to data from genome sequencing (1001genomes.org). Accessions that did not have the highest similarity to the expected genotype were excluded from further analysis.

## DNA methylation analysis

Methylation was estimated individually for each cytosine using a python script provided with the BSMAP software package (Xi and Li, 2009). Conversion efficiency was estimated from the fraction of methylated cytosines in chloroplasts using the R software package (www.r-project.org, version 2.15.2). After eliminating one outlier, the samples had conversion efficiencies ranging from 99.25%–99.80% (mean = 99.59%). Genome wide average methylation levels were calculated separately for the CG, CHG and CHH contexts. The average variance between 11 biological replicates was 2.2%, 3.2% and 7.3% for CG, CHG and CHH methylation respectively, while for identical genotypes grown at different temperatures (111 pairs) CG, CHG and CHH methylation variance was 2.7%, 4.6% and 15.9% respectively. The variance in genome wide methylation levels for the 152 accessions grown at 10°C was respectively 7.6%, 9.2% and 13.2% for CG, CHG and CHH methylation, while for the 121 accessions grown at 16°C genome wide CG, CHG and CHH methylation varied 8.5%, 9.5% and 14.3% respectively.

The Bioconductor package Repitools (version 0.6.0; Statham et al., 2010) was used to average methylation over genomic features of interest (e.g., all genes, all transposons over 4 kB or a subset of transposons of interest). Pairwise DMRs were called individually for each accession using the R software package methylKit (version 0.5.6; Akalin et al., 2012) using a window size of 100 bp, an FDR rate of 0.05 and a minimum fold change of 0.3. Overlap of DMRs with (TAIR10) genomic features such as transposons and genes was calculated using the Bioconductor package ChIPpeakAnno (version 2.8.0; Zhu et al., 2010). For each accession, methylation data was smoothed independently for each context using the Bioconductor package BSmooth (version 0.4.5; Hansen et al., 2012) using the default settings. Average methylation was then calculated for (overlapping) 200 bp sliding windows centered every 100 bp across the genome. Further analysis was limited to the 200,000 windows showing the most variance among accessions.

## Population genetic analysis

## GWAS

Linear mixed models that correct for confounding by the genetic background using a kinship matrix calculated from genetic data were used throughout (Kang et al., 2010; Segura et al., 2012). To examine the effect of genotype on local CHH methylation variation, DMRs were defined by filtering the 200 bp methylation windows to remove those containing missing data (no coverage) in one or more accessions, then selecting the 105 remaining windows with the greatest variance in DNA methylation. For GBM, genes were filtered to remove those that had more than 0.05 average CHG methylation or less than 0.05 average CG methylation across the accessions (Figure 6—figure supplement 2).

## Variance component analysis

To investigate the relative contributions of genetic and environmental effects to methylation differences we used LIMIX (Lippert et al., 2014), which efficiently estimates variance components using linear mixed models.

For each DMR, we considered a linear mixed model with a fixed effect for the environment and random effects for the contributions from cis and trans genetic variants and variants from the CMT2 locus. Indicating with N and E respectively the number of samples and environments (E = 2), the NxE multivariate phenotype Y can be written asY=1N,1μT+UCMT2+Ucis+Utrans+ψ,where μ is a Ex1 vector of environment-specific mean values, andUCMT2∼MVN(0,CCMT2,RCMT2), Ucis∼MVN(0,Ccis,Rcis),Utrans∼MVN(0,Ctrans,Rtrans), ψ∼MVN(0,Σ,IN),where MVN(0,C,R) denotes a matrix normal distribution with mean 0, column covariance matrix C and row covariance matrix R. Rcis and Rtrans indicate the genetic relatedness matrices based on cis and trans variants respectively, where all variants within 50 kb from the DMR were defined as cis-acting and all others as trans–acting. Similarly, RCMT2 denotes the genetic relatedness matrix based on genotypes at the CMT2 locus. The row covariance of the noise component IN corresponds to an N x N identity matrix.

The covariance matrices CCMT2, Ccis, Ctrans and Σ describe phenotypic correlations across environments due to these contributions, and were estimated from the data using maximum likelihood. For each DMR, we considered up to 10 random restarts for the optimization and stopped as soon as convergence was achieved. DMRs for which no convergence was achieved were discarded from genome-wide summary statistics.

Once the model parameters have been estimated, the variance explained by environment can be calculated from μ, while environment-persistent and environment-specific effects from a given random effect can be estimated by decomposing the corresponding trait covariance into a shared and an independent component (Lippert et al., 2014).

## QTL mapping

MethylC-seq data for the 113 F2 individuals was mapped as described in section ‘Read mapping’ to the Columbia-0 TAIR reference genome. SNP-calling was done directly from the methylC-seq data using the BIS-SNP package (Liu et al., 2012). From these SNPs local haplotype was inferred for sequential 500 Mb windows which were then used to create a haplotype map using the R package R/qtl (Broman et al., 2003). Mapping was done using Haley-Knot regression (Arends et al., 2010) with a 4 centimorgan steps size. Genome wide significance was estimated by permutation testing (1000 permutations).

## DMR calling on DNA methylation mutants

Pairwise DMRs were called for T-DNA mutants vs the wild-type control using the R software package methylKit (version 0.5.6; Akalin et al., 2012) using a window size of 100 bp, an FDR rate of 0.05 and a minimum fold change of 0.3. Overlap between these DMRs and ‘temperature DMRs” calculated for the accessions was calculated and significance testing (Fisher's exact test) was calculated using R software.

## Qst-Fst test

Fst was computed using the Hudson estimate as suggested in Bhatia et al. (2013). We note that our estimate of 0.187 is consistent with the recent estimate of Huber et al. (2014) (although the samples only overlap in part). For Qst, we first estimated northern, southern, and overall additive variance using the Hasemann-Elston regression, and a SNP-based identity-by-state matrix (Chen, 2014), then calculated Qst as σB2/(σB2+2σw2), where σw2 is the weighted average of variance within north and south populations, and σB2 is the variance between populations, obtained by subtracting σw2 from the overall additive variance.
