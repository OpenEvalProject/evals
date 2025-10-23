# Adaptation of hepatitis C virus to interferon lambda polymorphism across multiple viral genotypes

## Authors

- Nimisha Chaturvedi<sup>1</sup> ([ORCID: 0000-0002-3065-0202](https://orcid.org/0000-0002-3065-0202)) †
- Evguenia S Svarovskaia<sup>3</sup>
- Hongmei Mo<sup>3</sup>
- Anu O Osinusi<sup>3</sup>
- Diana M Brainard<sup>3</sup>
- G Mani Subramanian<sup>3</sup>
- John G McHutchison<sup>3</sup>
- Stefan Zeuzem<sup>4</sup>
- Jacques Fellay<sup>1</sup> ([ORCID: 0000-0002-8240-939X](https://orcid.org/0000-0002-8240-939X)) †

### Affiliations

1. School of Life Sciences École Polytechnique Fédérale de Lausanne Lausanne Switzerland
2. Swiss Institute of Bioinformatics Lausanne Switzerland
3. Gilead Sciences Inc Foster City United States
4. Goethe University Hospital Frankfurt Germany
5. Precision Medicine Unit Lausanne University Hospital Lausanne Switzerland

† Corresponding author

## Abstract

10.7554/eLife.42542.001 Genetic polymorphism in the interferon lambda (IFN-λ) region is associated with spontaneous clearance of hepatitis C virus (HCV) infection and response to interferon-based treatment. Here, we evaluate associations between IFN-λ polymorphism and HCV variation in 8729 patients (Europeans 77%, Asians 13%, Africans 8%) infected with various viral genotypes, predominantly 1a (41%), 1b (22%) and 3a (21%). We searched for associations between rs12979860 genotype and variants in the NS3, NS4A, NS5A and NS5B HCV proteins. We report multiple associations in all tested proteins, including in the interferon-sensitivity determining region of NS5A. We also assessed the combined impact of human and HCV variation on pretreatment viral load and report amino acids associated with both IFN-λ polymorphism and HCV load across multiple viral genotypes. By demonstrating that IFN-λ variation leaves a large footprint on the viral proteome, we provide evidence of pervasive viral adaptation to innate immune pressure during chronic HCV infection.

## Introduction

Infection with hepatitis C virus (HCV), a positive strand RNA virus of the Flaviviridae family, represents a major health problem, with an estimated 71 million chronically infected patients worldwide (WHO, 2017). In the absence of treatment, 15–30% of individuals with chronic HCV infection develop serious complications including cirrhosis, hepatocellular carcinoma and liver failure (Shepard et al., 2005; Alter and Seeff, 2000; Li et al., 2015; Drummer, 2014).

Seven major genotypes of HCV have been described, further divided into several subtypes (Simmonds, 2004; Smith et al., 2014). Moreover, within each infected individual, multiple distinct HCV variants co-exist as quasipecies (Farci et al., 2000). Inter-host and intra-host HCV evolution is shaped by multiple forces, including human immune pressure (Merani et al., 2011). To investigate the complex interactions between host and pathogen at the level of genetic variation, we proposed a genome-to-genome approach that allows the joint analysis of host and pathogen genomic data (Bartha et al., 2013). Using an unbiased association study framework, a genome-to-genome analysis aims at identifying the escape mutations that accumulate in the pathogen genome in response to host genetic variants. Ansari et al. (2017) used this approach to analyze a cohort of individuals of white ancestry predominantly infected with genotype 3a HCV; they identified associations between viral variants and human polymorphisms in the interferon lambda (IFN-λ) and HLA regions, demonstrating an impact of both innate and acquired immunity on HCV sequence variation during chronic infection.

The IFN-λ association is of particular interest considering the known impact of this polymorphic region on spontaneous clearance of HCV and on response to interferon-based treatment (Ge et al., 2009; Rauch et al., 2010; Thomas et al., 2009; Tanaka et al., 2009). The rs12979860 variant, which is located 3 kb upstream of IL28B (encoding IFN-λ3) and lies within intron 1 of IFNL4, showed the strongest correlation with treatment-induced clearance of infection in the first report (Ge et al., 2009). More recent studies have shown that rs12979860 is in fact a marker for a dinucleotide insertion/deletion polymorphism, IFNL4 rs368234815 [ΔG > TT], which causes a frameshift that abrogates IFN-λ4 protein production (Prokunina-Olsson et al., 2013). The two variants (rs12979860 and rs368234815) are in strong linkage disequilibrium in European and Asian populations (r2 = 0.98 in CEU and 1.00 in CHB and JPT): the rs12979860 C allele, associated with a higher rate of spontaneous HCV clearance and better response to interferon-based treatment, is found on the same haplotype as the rs368234815 TT allele and is thus tagging the absence of IFN-λ4 protein.

Here, we aim at characterizing the importance of innate immune response in modulating chronic HCV infection by describing the footprint of IFNL4 variation in the viral proteome. Using samples and data from a heterogeneous group of 8,729 HCV-infected individuals in a cross-sectional study design, we genotyped the single nucleotide polymorphism (SNP) rs12979860 and obtained partial sequences of the HCV genome (NS3, NS4A, NS5A and NS5B genes). We tested for associations between rs12979860, HCV amino acid variants and pre-treatment viral load. We show that the presence or absence of the IFN-λ4 protein has a pervasive impact on HCV, by describing multiple associations between host and pathogen variants in subgroups defined by viral genotype or human ancestry. We also present association analyses of human and viral variants with HCV viral load, which allows for a better understanding of the connections between genomic variation, biological mechanisms and clinical outcomes.

## Results

## Host and pathogen data

We obtained paired human and viral genetic data for 8,729 HCV-infected patients participating in various clinical trials of anti-HCV drugs. The samples were heterogeneous in terms of self-reported ancestry (85% Europeans, 13% Asians and 2% Africans) and HCV genotypes, with a majority of HCV genotype 1a, 2a and 3a (Table 1). We genotyped the human SNP rs12979860 and performed deep sequencing of the coding regions of the HCV non-structural proteins NS3, NS4A, NS5A and NS5B (Bartenschlager et al., 2004). A binary variable was generated for each alternate amino acid, indicating the presence or absence of that allele in a given sample (N = 10,681). For the analysis, we used only amino acids that were present in at least 0.3% of the samples (N = 4,022).

## Associations between IFN-λ polymorphism and HCV amino acids

We performed a separate analysis for each HCV genotype, using an additive logistic model with binary amino acid variables as traits of interest. To control for population stratification, we added host and viral covariates in the model and to control for multiple testing we used a Bonferroni threshold of 4.7 × 10−6, which was calculated based on the number of tests performed (more information in the Materials and methods section). We restricted the analysis to genotypes 1a, 1b, 2a, 2b, 3a and 4a, which were present in at least 100 participants.

We observed highly significant associations between rs12979860 and HCV amino acid variables for each HCV genotype that we examined (Figure 1, Table 2). The highest number of significant associations was detected in the largest group of patients, infected with genotype 1a, most likely reflecting an effect of sample size on statistical power. Most associations were specific to a single viral genotype; however, some associations were significant across genotypes. As an example, two strong associations were observed between rs12979860 and amino acid variables at position 2576 in viral protein NS5B, with the T allele associating with proline in genotypes 1a (p=1.5×10−10), 2b (p=5.4×10−15), 3a (p=8.3×10−12) and 4a (p=1.2×10−7), and the C allele associating with alanine in genotypes 1a (p=1.2×10−11), 2a (p=3.8×10−6), 2b (p=4.02×10−8) and 3a (p=1.04×10−14).

In patients infected with genotype 3a, we replicated the previously reported associations (Ansari et al., 2017) between IFNL4 variation and valine at position 2570 in NS5B (p=5.5×10−20), histidine at position 2991 in NS5B (p=4.6×10−12) and asparagine at position 2414 in NS5A (p=2.4×10−7). We also observed novel associations with alanine (p=2.6×10−7) and threonine (p=8.8×10−15) at position 2570 in NS5B, as well as with glycine (p=5.2×10−7) and serine (p=1.04×10−11) at position 2414 in NS5A. All these associations were only detected in the 3a subgroup. In concordance with a previous study (Peiffer et al., 2016), we also observed a significant association with histidine at position 2065 of NS5A in patients infected with HCV genotypes 1a (p=9.8×10−7) and 1b (p=1.3×10−7).

We also observed multiple significant associations in the interferon-sensitivity determining region (ISDR, amino acid positions 2209 to 2248 in NS5A) in patients infected with genotype 1b, the strongest one being with the presence of leucine at position 2224 (p=1.5×10−12). For genotype 1a, we observed a single significant association in the ISDR region with the presence of leucine at position 2211 (p=2.8×10−6).

To check whether the association of IFNL4 genotype with HCV amino acid variables could be dependent of the effect of IFNL4 genotype on viral replication rates, we also compared the results from two sets of logistic regression models: one that does and one that does not include HCV viral load as an additional covariate. We did not observe any significant difference in the results of the two models (Figure 1—figure supplement 1).

## Viral load association analyses

To further understand the clinical implications of viral mutations associated with IFN-λ polymorphism, we searched for associations between rs12979860, HCV amino acid variants and viral load. For this, we first searched for associations between rs12979860 and Box-Cox transformed pre-treatment HCV viral load, in subgroups defined by HCV genotypes. Pre-treatment viral load was found to be significantly associated (p<0.05) with rs12979860 for all HCV genotypes, with the rs12979860 T allele consistently associated with lower viral load (Figure 1—figure supplement 2). The strength of the association p-values varied between genotypes due to sample size, but the effect size associated with the T allele was comparable across genotype groups.

We then searched for associations between viral load and HCV amino acid variables. These analyses identified significant associations in all viral genotype groups except 4a (Figure 2). Amongst the viral amino acids that associated with viral load, a number also associated with rs12979860 genotype (genotype 1a, 9 of 18 amino acids; 1b, 5 of 17 amino acids; 2a, 0 of 2 amino acids; 2b, 0 of 6 amino acids; 3a, 2 of 3 amino acids). As an example of such a complex association pattern, we looked at position 2224 of NS5A (in the ISDR) in genotype 1b. Mean viral load was higher in patients infected with a virus harboring a leucine in comparison to the most common amino acid alanine (t-test p-value: 5.6 x10−9, with Halternative =μvlL− μvlA>0) (Figure 3A). This was true for both CC and non CC genotypes of SNP rs12979860 (t-test p-value: 6.2 x10−6 for CC,L vs. CC,non-L; t-test p-value: 4.1 x10−2 for CT,L vs. CT,non-L), indicating a possible impact of that leucine residue on viral replication (Figure 3B).

![Figure 2.](https://cdn.elifesciences.org/articles/42542/elife-42542-fig2-v1.jpg)

**Figure 2.:** Manhattan plot for associations between human Box-Cox transformed pre-treatment viral load and HCV amino acid variants. The dotted line shows the Bonferroni-corrected significance threshold.

We also replicated the previously shown (Ansari et al., 2017) association between viral load and the change from a serine to an asparagine at position 2414 in NS5A protein (p=4.5×10−7) in genotype 3a and observed a lower mean viral load for patients with non-CC genotype and presence of serine at position 2414 (Figure 3—figure supplement 1).

To further understand these associations, we performed a residual regression analysis. We searched for associations between the amino acid variables and viral load residuals, obtained after regressing the transformed viral load on rs12979860. The objective of this analysis was to identify amino acids associated with changes in viral load that cannot be entirely explained by rs12979860 genotype. We observed multiple significantly associated amino acids with residual viral load across genotypes (Figure 3—figure supplement 2). A total of 7 amino acids in genotype 1a (supplementary file 1) and six amino acids in genotype 1b (supplementary file 2) associated with rs12979860 genotype, viral load and viral load residuals, including again leucine at position 2224 of NS5A in genotype 1b (presidual = 4.9×10−8).

## Ancestry-specific sub-analyses

We also ran association analyses between IFN-λ variations and the variations in the HCV genome in subgroups defined by self-reported ancestry: European, Asian, and African. The association results are broadly similar to per genotype analysis and are presented in supplementary file 3.

We further dissected the association signals within the largest ancestry group, Europeans, by running a per genotype analysis within this sample (Figure 3—figure supplement 3). The strongest association was observed with the presence of isoleucine at position 2252 of viral protein NS5A in patients infected with HCV genotype 1a (p=1.2×10−24). All the significant results from this study are presented in supplementary file 4.

Results of the ancestry-specific sub-analyses of associations with HCV viral load are comparable to the results obtained in the whole study population and are presented in Figure 3—figure supplement 4, Figure 3—figure supplement 5 and supplementary file 5.

## Discussion

We used an integrated association analysis approach to explore the impact of human genetic variation in the IFN-λ region on part of the HCV proteome during chronic infection. Our results reveal a strong footprint of innate immune pressure on the non-structural regions of the HCV genome and provide strong evidence for pervasive HCV adaptation to innate immunity. We performed analyses in different sub-groups, which showed an impact of IFNL4 variation on HCV across genotypes and ancestry categories. Finally, we report viral amino acids significantly associated with both IFNL4 variation and HCV viral load, indicating that some of the HCV clinical and biological outcomes could be explained by traceable host–pathogen interactions.

Because we genotyped the human SNP rs12979860, a reliable marker for the dinucleotide insertion/deletion polymorphism rs368234815, our analyses exclusively focus on the effects of the presence or absence of the IFN-λ4 protein on HCV amino acids and viral load. Therefore, one clear limitation of our study is the impossibility to distinguish between the two haplotypes encoding the IFN-λ4 P70 and S70 isoforms, which have been shown to have distinctive influences on HCV pathogenesis (Ansari, 2018).

Our analysis detected multiple associations in all tested proteins, including NS5A. This protein is required for HCV RNA replication and virus assembly and has been shown to associate with interferon signaling and hepatocarcinogenesis (Nakamoto et al., 2014). Previous studies have also shown strong associations between variants in the ISDR of NS5A and HCV viral load as well as response to IFN-based therapy (Enomoto et al., 1995; Frangeul et al., 1998). Some of the strongest associations that we observed were in and around this highly variable region, suggesting a possible role of these variants in determining the response to IFN-based antiviral treatment. The strongest association in the ISDR was with leucine at position 2224 in patients infected with 1b genotype, with higher mean viral load observed in presence of leucine for patients with the rs12979860 CC genotype. We also confirmed previously reported findings in the region, including associations with histidine at position 206518 (also known as the NS5A Y93H variant) and with asparagine at position 241411. Using a genotype three replicon assay, Ansari et al. showed that this later variant - a change from a serine to asparagine at site 2414 - is associated with an increase in RNA replication, which is concordant with our results.

This is the first comprehensive analysis of IFN-λ-driven HCV adaptation across different viral genotypes and ancestry groups. In addition to identifying genotype or ancestry-specific associations, we observed sites of interaction that were consistent across HCV genotypes and ethnicities; for example, the NS5A variant Y2065H, which was found to be associated with rs12979860 in individuals infected with HCV genotypes 1a and 1b. These results indicate that IFN-λ-driven viral adaptation is a part of evolution across HCV genotypes.

In an attempt to delineate the biological impact of these associations, we evaluated the associations between HCV amino acid variants and pre-treatment viral load. We were able to detect a subset of amino acids that associated with both IFN-λ variation and HCV viral load across different viral genotypes, supporting the clinical relevance of host and pathogen interactions. Furthermore, we also performed a similar analysis with residual viral load, that is the fraction of the viral load variance that that is not explained by IFN-λ variation. We detected a group of viral amino acid variants that associated with SNP variations as well as residual viral load, indicating a stronger role of host–pathogen interactions in explaining the variations in HCV viral load.

Interestingly, only a fraction of the host-driven HCV amino acid variants was found to be associated with viral load, indicating that an integrated association analysis between host and pathogen genome variations can reveal correlations that would go unnoticed in association studies that use more downstream laboratory measurements or clinical outcomes as phenotypes.

IFN-λ polymorphism is the strongest human genetic predictor of spontaneous HCV clearance and response to IFN-based therapy. By integrating IFN-λ and HCV amino acid variation in a joint analysis, we here contribute to a better understanding of the genomic mechanisms involved in inter-individual differences in HCV disease outcomes. Our results confirm that IFN-λ4 is a functional gene that plays a pivotal role in HCV pathogenesis. The large footprint left by IFNL4 variation on the HCV proteome is indeed a clear indicator of the importance of innate immunity in viral control and of the remarkable capacity of HCV to evolve escape strategies.

## Materials and methods

## Clinical samples

Across 82 studies involving >100 sites in many countries, appropriate informed consent was obtained from study participants allowing the current analysis to be performed (Welzel et al., 2017). The studies were run by Gilead Sciences (Foster City, CA) and Pharmasset (formerly Princeton, NJ). Study protocols followed the ethical guidelines set in place by the 1975 Declaration of Helsinki and were approved by the relevant institutional review board committees. All samples included in this analysis are baseline samples collected from treatment naive and experienced patients from >25 countries in North America, Europe, Asia, Oceania, and Africa between years 2010 and 2015.

## NS3, NS5A, and NS5B sequencing

The genotype assignment from Siemens VERSANT HCV Genotype INNO-LiPA 2.0 Assay (Innogenetics, Ghent, Belgium) was used to select genotype-specific primers located outside of the gene target(s) that amplify the entire NS3/4A, NS5A, or NS5B regions of HCV. Standard reverse transcription polymerase chain reaction (RT-PCR) was performed on patient plasma with HCV RNA >1000 IU/mL at DDL Diagnostic Laboratory (Rijswijk, The Netherlands). For deep sequencing, amplicons encoding the subject-derived NS3/4A, NS5A and NS5B were run using Illumina MiSeq v2 150 paired-end deep sequencing at DDL or WuXi AppTec (Shanghai, China). FASTQ files were split based on 100% matched barcodes. Contigs were generated from paired-end FASTQ files using VICUNA (Yang et al., 2012) and merged to create a de novo assembly sequence. All paired-end reads were merged using PEAR (Zhang et al., 2014), chopped at the 3’ end when MAPQ <15, and filtered to remove reads <50 bases. The filtered reads were aligned to the de novo assembly sequence using MOSAIK (Lee et al., 2014) (v1.1.0017) to create a final assembly sequence. The average coverage of >5000 reads per position was obtained for most of the samples. The aligned reads were translated in-frame and the resulting tabulated summary of variants from the final assembly was utilized to generate a consensus sequence. Mixtures were reported when present in ≥15% of the viral population. NS3/4A, NS5A and NS5B consensus nucleotide and amino acid sequences were compared by the NCBI alignment tool BLAST to a set of reference sequences to assign HCV genotype and subtype. Amino acid variation between the samples that were assigned to genotype 1a, 1b, 2a, 2b, 3a and 4a were tabulated and analyzed. The raw HCV sequences are available in the zenodo repository, https://doi.org/10.5281/zenodo.1476713.

## Host genotyping

Human genotype was determined by PCR amplification and sequencing of the rs12979860 SNP region. Possible genotypes were CC, CT or TT.

## Association analyses

To run the integrated association analysis between genotyped host SNP and viral amino acids, we used logistic regression where the traits of interest were the presence or absence of each amino acid at the variable sites of the virus proteome. We assumed an additive model and corrected for host population stratification by adding sex, country of origin, self-reported ethnicity, cirrhosis status and prior treatment experience as covariates. To account for residual viral stratification within each HCV genotype, the first five phylogenetic principal components (Revell, 2009), calculated per HCV gene to account for recombination, were also added as covariates.

For the viral load GWAS analysis, we used linear regression where the trait of interest was Box-Cox transformed pre-treatment viral load. We used Box-Cox transformation to transform the positively skewed viral load distribution into a normally distributed dependent variable. We corrected for host and viral population stratification by adding sex, country of origin, self-reported ethnicity, cirrhosis status and prior treatment experience, as well as the first five viral phylogenetic principal components as covariates.

To correct for multiple testing we calculated the Bonferroni threshold as 0.05nA, where nA represents the number of tests performed. For the analyses described in the paper, we performed a total of 10,681 tests. Given the heterogeneity of the dataset with multiple genotypes and ethnicities, we performed the integrated association analysis as well as viral load GWAS analyses on different sample subsets, created per genotype as well as per ethnic group.

## Software used

We used muscle (Edgar, 2004) to align the pathogen sequences, RaXML (Stamatakis, 2014) to obtain the phylogenetic trees and R (R Development Core Team, 2013) for all other analyses.
