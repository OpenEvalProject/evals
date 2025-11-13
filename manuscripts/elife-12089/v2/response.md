# Author response - Round 1

Authors:
- Prithvi Raj
- Ekta Rai
- Ran Song
- Shaheen Khan
- Benjamin E Wakeland
- Kasthuribai Viswanathan
- Carlos Arana
- Chaoying Liang
- Bo Zhang
- Igor Dozmorov
- Ferdicia Carr-Johnson
- Mitja Mitrovic
- Graham B Wiley
- Jennifer A Kelly
- Bernard R Lauwerys
- Nancy J Olsen
- Chris Cotsapas
- Christine K Garcia
- Carol A Wise
- John B Harley
- Swapan K Nath
- Judith A James
- Chaim O Jacob
- Betty P Tsao
- Chandrashekhar Pasare
- David R Karp
- Quan Zhen Li
- Patrick M Gaffney
- Edward K Wakeland ([ORCID: 0000-0002-7107-0992](https://orcid.org/0000-0002-7107-0992))

## Response text

DOI: [10.7554/eLife.12089.041](https://doi.org/10.7554/eLife.12089.041)

Essential revisions:

1) For the RNA-seq analysis throughout, normalized RPKMs (normalized for the length of the gene) should be used, not raw RPKMs. More information on the methods used (average depth, read length, single or paired end, mapping of reads, software used to compute RPKM values) are needed. Report how many samples were excluded for <25X coverage, how many excluded for HWD in controls. How many samples were at start and how many at the end after filtering? (For example: in Figure 4G, what is being plotted: mean or median RPKM? What are sample sizes for each genotype? Please show p-values for all).

We apologize for the confusion, but the RPKM values presented in the manuscript were normalized for the length of the gene. We have used the term “normalized RPKM” in the revised figures and the manuscript text as suggested by the reviewers.

We have added details and additional information throughout the Methods section. We expanded the description of the protocol used for the culturing and production of monocyte-derived dendritic and macrophages, together with an expanded description of the methods for RNA-SEQ data production and analysis, including read depth, read length, read mapping and software used for these RNA-Seq analyses to the Methods section.

For the filtering of samples, the study started with 1775 samples, all of which were sequenced following targeted enrichment. Of these, 88 samples had missing case/control status information and 249 were PCA outliers for the HapMap CEU reference sample in principal component analysis, most of which were self designated as African American or Hispanic. Of the remaining 1438 PCA pass samples, 11 and 5 were excluded due to poor call rate (<85%) and being duplicate samples, respectively. In addition, 73 samples were excluded due to poor sequencing fold coverage (<25x, n=54) or significant p value (p>0.001) of HWE in controls (n=19). Thus, final set of 1349 samples which included 773 SLEs and 576 normal controls passed all quality criteria and were used for association analysis. This information is incorporated into the Methods section in the subsection “Defining high quality variants in the EA population”.

Mean RPKM values are plotted for all graphs of eQTL data, including in Figure 4G and the sample size of each genotype is given in parentheses for each genotype along the X axis.P-values are now shown for both the plots in the revised manuscript.

2) In several instances the authors claim either confirmation or stronger association for some of the known loci studied. To what extent are the samples independent from those used in previous GWAS and association studies?

More than 50% of SLE cases and all of the control samples used in the present study were new recruitments and have not been used in any previous association or GWAS on SLE. The remainders were provided by Dr. Betty Tsao and were used in our original GWAS study by Harley et al. (2008). This information has been added to the subsection “Targeted sequencing of SLE risk loci” in the Methods section.

3) Could the authors comment on previous studies showing the effects of compound heterozygotes of HLA DR2 and DR3 haplotypes in the genetic association of SLE and the relationship with XL9? One line can be added to mention compound heterozygozity.

HLA is a well-established genetic risk locus associated with SLE. Many MHC gene studies and GWAS have shown strong association of HLA-DR2 and HLA-DR3 alleles with SLE. A study by Graham et al. (2007) have explored the effects of different combinations of HLA-class II alleles in the context of SLE and its component phenotypes and showed that DR3 allele pose stronger SLE risk than DR2 allele. The study also found that individuals homozygous for DR3 or compound heterozygote for DR3 and DR2 allele demonstrated highest disease risk. As shown in Author response image 1 below, this is also true for comparisons of the regulatory haplotypes for XL9 that are in strongest LD with DR3 (HAP3) and DR2 (HAP2). We have added sentences concerning these issues and added the appropriate citation in the subsection “HLA-D polymorphisms, antigen presentation pathways, and autoimmune disease” in the Discussion section.10.7554/eLife.12089.024Author response image 1.A comparison of OR for individuals homozygous for XL9 HAP3 (DR3), XL9 HAP2 (DR2), and HAP2/HAP3 heterozygotes.

4) Figure 6 – Some attention is needed on this figure. Mismapping of RNA-seq reads is a known problem for HLA eQTL analysis and may lead to false positives. Which steps have you taken to avoid this? Panel E: the central figure in (iv), the legend misses the second allele (A). Also keep strands the same in this figure (ii vs. iii). Panel A: What cell type for the DNAse hypersensitivity track? The SNPs shown in 6E are not the same SNPs that reside in the IRF4 binding motif (6B), while the figure with the arrow from panel C to E seems to imply a direct connection. Please clarify.

We agree with the reviewers that mapping sequencing reads into the highly polymorphic HLA region is troublesome. We applied the following measures to control for false positive eQTLs for all of the MDM eQTLs reported in this manuscript (including HLA-DR and DQ in Figure 6): 1) High read depth of sequencing (>31,000,000 reads on average/sample) and removal of poor quality reads (still leaving >96% genome alignment on average of all pass filters reads for all samples in cohort); 2) Concordance rate for genomic versus RNA-Seq variant calls of >98% for heterozygous calls as a measure of mapping accuracy; and 3) Validation of previously published eQTLs in our monocytes derived macrophage data reported here.

To ensure the accurate alignments and mapping of RNA-Seq reads to the reference genome for the allelic bias studies of HLA-DR and DQ shown in Figure 6, we used CLC-Biosystems tools to map the RNA-Seq sequencing reads to the reference genome and validated all variant calls using additional variant calling software. As shown with representative data in Figure 6 C (iii) and C(iv) in the manuscript and in the data shown below in Author response image 2, the read depth for HLA was very high. Further, all variants called in the RNA-Seq datasets were coincided with and were confirmed by the variants called in the individual’s genomic sequence.

The most significant alignment issues involve reads mapping into the highly polymorphic exon 2 segments of HLA class II genes (which encodes the highly diversified peptide binding groove of HLA class II molecules). Therefore, for our analysis of allelic bias, we looked at multiple SNPs throughout exon 2 and throughout the much less polymorphic exon 3 (which encodes the membrane-proximal structural domains) of DRB1, DQB1, and DQA1. As shown in Author response image 2 below, multiple variants in exon 2 and exon 3 were found to be in significant bias with all of these variants trending towards the same allelic imbalance. In this regard, the exon 3 variants, two of which were used for Figure 6Ciii-iv, showed more bias then many of the exon 2 variants. These results confirm the observed allelic bias and indicate that it is not only observed in the highly polymorphic exon 2, but is also found in variants in exon 3.10.7554/eLife.12089.025Author response image 2.Representative data from heterozygote samples used for analysis of allelic expression bias in Figure 6 iii and iv.Note that multiple variants in exon 2 and exon 3 showed allelic bias in the same direction, although the magnitude of the effect varied between SNPs, presumably due to variations in read depth at specific locations in the exons.In this regard, variations in the less polymorphic exon 3 showed a stronger allelic bias than those in exon 2, although all of these SNPs showed significant allelic bias in frequency within the RNA-seq data favouring the variants associated with the risk allele..

Note that multiple variants in exon 2 and exon 3 showed allelic bias in the same direction, although the magnitude of the effect varied between SNPs, presumably due to variations in read depth at specific locations in the exons.In this regard, variations in the less polymorphic exon 3 showed a stronger allelic bias than those in exon 2, although all of these SNPs showed significant allelic bias in frequency within the RNA-seq data favouring the variants associated with the risk allele..

For the other points raised:

1) Figure 6 legend in Figure 6E(iv) and strand order in the tables in Figure 6E(ii) has been corrected as suggested.

2) The DNase hypersensitivity track shown in Figure 6A is generated based on 125 different cell types studied in the ENCODE project and is available on the UCSC human genome browser as an option. These include immune cells such as CD4+T cells, CD20+ B cells, lymphoblastic cells, monocytes, etc., which are important in the context of SLE disease. More details on cell types studied can be found at: https://www.encodeproject.org/search/?type=Biosample&organism.scientific_name=Homo+sapiens.

3) The IRF4 binding motif SNP is not shown here. But the RNAseq data shown in Figure 6E(iv) is based on four independent human donors who were heterozygous for IRF4 SNPs. For simplicity, we used the peak tagging SNP to show the LD relationships between the specific coding variants and the risk and protective regulatory haplotypes. The arrow from Figure 6C to Figure 6E was intended to point to the observed biased in RNAseq data as modeled in Figure 6C. To avoid the confusion, we have removed the arrow in the revised manuscript.

We have modified Figure 6E in the revised manuscript as discussed above and have expanded the text describing these experiments.

5) Figure 7: Provide a key for the heat map, and p-values for differences. Was quantitative RNA expression performed on these same donors? If so, please include. Please include in legend or on the figure the actual MFIs for the various genotypes. Please also clarify that R848 is a TLR7/8 ligand.

We have added a key for the heatmap and p-values for the differences in Figure 7 for the revised manuscript. Also, RNAseq expression data from the same donors and expression of HLA class II genes in both the donors are now included in revised Figure 7B. In addition, we have included graphs of the MFIs for all of the donors and an independent replicate of the HLA-DR donors. Reference to R848 as TLR7/8 ligand is given and stated in the figure legend. The text has been modified to add these additional details.
