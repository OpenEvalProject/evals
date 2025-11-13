# Pancreatic progenitor epigenome maps prioritize type 2 diabetes risk genes with roles in development

## Authors

- Ryan J Geusz<sup>1</sup> ([ORCID: 0000-0002-4897-9305](https://orcid.org/0000-0002-4897-9305))
- Allen Wang<sup>1</sup> ([ORCID: 0000-0001-9870-7888](https://orcid.org/0000-0001-9870-7888))
- Joshua Chiou<sup>1</sup> ([ORCID: 0000-0002-4618-0647](https://orcid.org/0000-0002-4618-0647))
- Joseph J Lancman<sup>5</sup> ([ORCID: 0000-0003-1238-4446](https://orcid.org/0000-0003-1238-4446))
- Nichole Wetton<sup>1</sup>
- Samy Kefalopoulou<sup>1</sup>
- Jinzhao Wang<sup>1</sup>
- Yunjiang Qui<sup>2</sup> ([ORCID: 0000-0002-0539-9714](https://orcid.org/0000-0002-0539-9714))
- Jian Yan<sup>2</sup> ([ORCID: 0000-0002-1267-2870](https://orcid.org/0000-0002-1267-2870))
- Anthony Aylward<sup>1</sup> ([ORCID: 0000-0003-3524-856X](https://orcid.org/0000-0003-3524-856X))
- Bing Ren<sup>2</sup>
- P Duc Si Dong<sup>5</sup>
- Kyle J Gaulton<sup>1</sup> ([ORCID: 0000-0003-1318-7161](https://orcid.org/0000-0003-1318-7161)) †
- Maike Sander<sup>1</sup> ([ORCID: 0000-0001-5308-7785](https://orcid.org/0000-0001-5308-7785)) †

### Affiliations

1. Department of Pediatrics, Pediatric Diabetes Research Center, University of California, San Diego San Diego United States
2. Department of Cellular & Molecular Medicine, University of California, San Diego San Diego United States
3. Sanford Consortium for Regenerative Medicine San Diego United States
4. Biomedical Graduate Studies Program, University of California, San Diego San Diego United States
5. Human Genetics Program, Sanford Burnham Prebys Medical Discovery Institute San Diego United States
6. Graduate School of Biomedical Sciences, Sanford Burnham Prebys Medical Discovery Institute San Diego United States
7. Ludwig Institute for Cancer Research San Diego United States

† Corresponding author

## Abstract

Genetic variants associated with type 2 diabetes (T2D) risk affect gene regulation in metabolically relevant tissues, such as pancreatic islets. Here, we investigated contributions of regulatory programs active during pancreatic development to T2D risk. Generation of chromatin maps from developmental precursors throughout pancreatic differentiation of human embryonic stem cells (hESCs) identifies enrichment of T2D variants in pancreatic progenitor-specific stretch enhancers that are not active in islets. Genes associated with progenitor-specific stretch enhancers are predicted to regulate developmental processes, most notably tissue morphogenesis. Through gene editing in hESCs, we demonstrate that progenitor-specific enhancers harboring T2D-associated variants regulate cell polarity genes LAMA1 and CRB2. Knockdown of lama1 or crb2 in zebrafish embryos causes a defect in pancreas morphogenesis and impairs islet cell development. Together, our findings reveal that a subset of T2D risk variants specifically affects pancreatic developmental programs, suggesting that dysregulation of developmental processes can predispose to T2D.

## Introduction

Type 2 diabetes (T2D) is a multifactorial metabolic disorder characterized by insulin insensitivity and insufficient insulin secretion by pancreatic beta cells (Halban et al., 2014). Genetic association studies have identified hundreds of loci influencing risk of T2D (Mahajan et al., 2018). However, disease-relevant target genes of T2D risk variants, the mechanisms by which these genes cause disease, and the tissues in which the genes mediate their effects remain poorly understood.

The majority of T2D risk variants map to non-coding sequence, suggesting that genetic risk of T2D is largely mediated through variants affecting transcriptional regulatory activity. Intersection of T2D risk variants with epigenomic data has uncovered enrichment of T2D risk variants in regulatory sites active in specific cell types, predominantly in pancreatic beta cells, including risk variants that affect regulatory activity directly (Chiou et al., 2019; Fuchsberger et al., 2016; Gaulton et al., 2015; Gaulton et al., 2010; Greenwald et al., 2019; Mahajan et al., 2018; Parker et al., 2013; Pasquali et al., 2014; Thurner et al., 2018; Varshney et al., 2017). T2D risk-associated variants are further enriched within large, contiguous regions of islet active chromatin, referred to as stretch or super-enhancers (Parker et al., 2013). These regions of active chromatin preferentially bind islet-cell-restricted transcription factors and drive islet-specific gene expression (Parker et al., 2013; Pasquali et al., 2014).

Many genes associated with T2D risk in islets are not uniquely expressed in differentiated islet endocrine cells, but also in pancreatic progenitor cells during embryonic development. For example, T2D risk variants map to HNF1A, HNF1B, HNF4A, MNX1, NEUROG3, PAX4, and PDX1 (Flannick et al., 2019; Mahajan et al., 2018; Steinthorsdottir et al., 2014), which are all transcription factors also expressed in pancreatic developmental precursors. Studies in model organisms and hESC-based models of pancreatic endocrine cell differentiation have shown that inactivation of these transcription factors causes defects in endocrine cell development, resulting in reduced beta cell numbers (Gaertner et al., 2019). Furthermore, heterozygous mutations for HNF1A, HNF1B, HNF4A, PAX4, and PDX1 are associated with maturity onset diabetes of the young (MODY), which is an autosomal dominant form of diabetes with features similar to T2D (Urakami, 2019). Thus, there is evidence that reduced activity of developmentally expressed transcription factors can cause diabetes later in life.

The role of these transcription factors in T2D and MODY could be explained by their functions in regulating gene expression in mature islet cells. However, it is also possible that their function during endocrine cell development could predispose to diabetes instead of, or in addition to, endocrine cell gene regulation. One conceivable mechanism is that individuals with reduced activity of these transcription factors are born with either fewer beta cells or beta cells more prone to fail under conditions of increased insulin demand. Observations showing that disturbed intrauterine metabolic conditions, such as maternal malnutrition, can lead to reduced beta cell mass and T2D predisposition in the offspring (Lumey et al., 2015; Nielsen et al., 2014; Portha et al., 2011) support the concept that compromised beta cell development could predispose to T2D. However, whether there is T2D genetic risk relevant to the regulation of endocrine cell development independent of gene regulation in mature islet cells has not been explored.

In this study, we investigated the contribution of gene regulatory programs specifically active during pancreatic development to T2D risk. First, we employed a hESC-based differentiation system to generate chromatin maps of hESCs during their stepwise differentiation into pancreatic progenitor cells. We then identified T2D-associated variants localized in active enhancers in developmental precursors but not in mature islets, used genome editing in hESCs to define target genes of pancreatic progenitor-specific enhancers harboring T2D variants, and employed zebrafish genetic models to study the role of two target genes in pancreatic and endocrine cell development.

## Results

### Pancreatic progenitor stretch enhancers are enriched for T2D risk variants

To determine whether there is a development-specific genetic contribution to T2D risk, we generated genome-wide chromatin maps of hESCs during their stepwise differentiation into pancreatic progenitors through four distinct developmental stages: definitive endoderm (DE), gut tube (GT), early pancreatic progenitors (PP1), and late pancreatic progenitors (PP2) (Figure 1A). We then used ChromHMM (Ernst and Kellis, 2012) to annotate chromatin states, such as active promoters and enhancers, at all stages of hESC differentiation as well as in primary islets (Figure 1—figure supplement 1A,B).

![Figure 1.](https://cdn.elifesciences.org/articles/59067/elife-59067-fig1-v1.jpg)

**Figure 1.:** (A) Schematic illustrating the stepwise differentiation of human embryonic stem cells (hES) into pancreatic progenitors (solid arrows) and lineage relationship to islets (dotted arrow). Developmental intermediates include definitive endoderm (DE), gut tube (GT), early pancreatic progenitor (PP1), and late pancreatic progenitor (PP2) cells. (B) Box plots depicting length of typical enhancers (TE) and stretch enhancers (SE) at each developmental stage and in primary human islets. Plots are centered on median, with box encompassing 25–75th percentile and whiskers extending up to 1.5 interquartile range. Total numbers of enhancers are shown above each box plot. (C) Examples of stretch enhancers (denoted with red boxes) near the genes encoding the pancreatic lineage-determining transcription factors NKX6.1 and PDX1, respectively. Chromatin states are based on ChromHMM classifications: TssA, active promoter; TssFlnk, flanking transcription start site; TssBiv, bivalent promoter; Repr, repressed; EnhA, active enhancer; EnhP, poised enhancer. (D) Percentage of TE and SE overlapping with at least one ATAC-seq peak at PP2 or in islets. Enrichment analysis comparing observed and expected overlap based on random genomic regions of the same size and located on the same chromosome averaged over 10,000 iterations (***p<1 × 10−4; permutation test). ATAC-seq peaks were merged from two independent differentiations for PP2 stage cells and four donors for primary islets. (E) Genome-wide enrichment of T2D-associated variants (minor allele frequency >0.0025) in stretch enhancers, ATAC-seq peaks, and ATAC-seq peaks within stretch enhancers for all developmental stages when modeling each annotation separately. Points and lines represent log-scaled enrichment estimates and 95% confidence intervals from functional genome wide association analysis (fgwas), respectively. ATAC-seq peaks were merged from two independent differentiations for ES, DE, GT, PP1, and PP2 stage cells and from four donors for primary islets. (F) Genome-wide enrichment of T2D-associated variants (minor allele frequency >0.0025) in ATAC-seq peaks within stretch enhancers for all developmental stages and coding exons when considering all annotations in a joint model. Points and lines represent log-scaled enrichment estimates and 95% confidence intervals from fgwas, respectively. ATAC-seq peaks were merged from two independent differentiations for ES, DE, GT, PP1, and PP2 stage cells and from four donors for primary islets. See also Figure 1—figure supplement 1.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/59067/elife-59067-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** (A) Diagram illustrating incorporation of histone modification and CTCF ChIP-seq data to generate chromatin state calls via ChromHMM. (B) Percentage of the genome covered by defined chromatin states at each developmental stage and in primary human islets. Chromatin states are based on ChromHMM classifications: TssA, active promoter; TssFlnk, flanking transcription start site; TssBiv, bivalent promoter; Repr, repressed; EnhA, active enhancer; EnhP, poised enhancer. (C) Percentage of typical (TE) and stretch enhancers (SE) relative to all enhancers at each developmental stage and in islets. (D) Box plots showing mRNA levels based on RNA-seq of nearest expressed genes (fragments per kilobase per million fragments mapped (FPKM) ≥1) for TE and SE at each developmental stage and in islets (***p=4.68 × 10−7, 4.64 × 10−11, 1.31 × 10−5, 8.85 × 10−9, 5.34 × 10−6, and <2.2 × 10−16 for TE vs SE comparisons in ES, DE, GT, PP1, PP2, and islets, respectively; Wilcoxon rank sum test, two sided). Plots are centered on median, with box encompassing 25-75th percentile and whiskers extending up to 1.5 interquartile range. n = 3 replicates from independent differentiations at ES, DE, GT, PP1, and PP2, respectively; n = 3 islet replicates. (E) Percentage of TE and SE overlapping with at least one ATAC-seq peak in ES, DE, GT, or PP1. Enrichment analysis comparing observed and expected overlap based on random genomic regions of the same size and located on the same chromosome averaged over 10,000 iterations (***p<1 × 10−4; permutation test). ATAC-seq peaks were merged from two independent differentiations. (F) Percentage of TE and SE overlapping 0, 1, 2, 3, or 4+ ATAC-seq peaks at each developmental stage and in islets. ATAC-seq peaks were merged from two independent differentiations for ES, DE, GT, PP1, and PP2 stage cells and from four donors for primary islets.

Large and contiguous regions of active enhancer chromatin, which have been termed stretch- or super-enhancers (Parker et al., 2013; Whyte et al., 2013), are highly enriched for T2D risk variants in islets (Parker et al., 2013; Pasquali et al., 2014). We therefore partitioned active enhancers from each hESC developmental stage and islets into stretch enhancers (SE) and traditional (non-stretch) enhancers (TE) (Figure 1B). Consistent with prior observations of SE features (Parker et al., 2013; Whyte et al., 2013), SE comprised a small subset of all active enhancers (7.7%, 7.8%, 8.8%, 8.1%, 8.1%, and 10.4% of active enhancers in ES, DE, GT, PP1, PP2, and islets, respectively; Figure 1B and Figure 1—figure supplement 1C) and genes proximal to SE were more highly expressed than genes proximal to TE (p=4.68 × 10−7, 4.64 × 10−11, 1.31 × 10−5, 8.85 × 10−9, 5.34 × 10−6, and <2.2 × 10−16 for expression of genes near TE vs SE in ES, DE, GT, PP1, PP2, and islets, respectively; Figure 1—figure supplement 1D). Genes near SE in pancreatic progenitors included transcription factors involved in the regulation of pancreatic cell identity, such as NKX6.1 and PDX1 (Figure 1C). Since disease-associated variants are preferentially enriched in narrow peaks of accessible chromatin within broader regions of active chromatin (Greenwald et al., 2019; Thurner et al., 2018; Varshney et al., 2017), we next used ATAC-seq to generate genome-wide maps of chromatin accessibility across all time points of differentiation. Nearly all identified SE contained at least one ATAC-seq peak (Figure 1D and Figure 1—figure supplement 1E,F). At the PP2 stage, 62.3% of SE harbored one, 32.2% two or three, and 0.7% four or more ATAC-seq peaks (Figure 1—figure supplement 1F). Similar percentages were observed in earlier developmental precursors and islets.

Having annotated accessible chromatin sites within SE, we next tested for enrichment of T2D-associated variants in SE active in mature islets and in pancreatic developmental stages. We observed strongest enrichment of T2D-associated variants in islet SE (log enrichment = 2.18, 95% CI = 1.80, 2.54) and late pancreatic progenitor SE (log enrichment = 2.17, 95% CI = 1.40, 2.74), which was more pronounced when only considering variants in accessible chromatin sites within these elements (islet log enrichment = 3.20, 95% CI = 2.74, 3.60; PP2 log enrichment = 3.18, 95% CI = 2.35, 3.79; Figure 1E). Given that a subset of pancreatic progenitor SE is also active in islets, we next determined whether pancreatic progenitor SE contribute to T2D risk independently of islet SE. Variants in accessible chromatin sites of late pancreatic progenitor SE were enriched for T2D association in a joint model including islet SE (islet log enrichment = 2.94, 95% CI = 2.47, 3.35; PP2 log enrichment = 1.27, 95% CI = 0.24, 2.00; Figure 1F). We also observed enrichment of variants in accessible chromatin sites of pancreatic progenitor SE after conditioning on islet SE (log enrichment = 0.60, 95% CI = −0.87, 1.48), as well as when excluding pancreatic progenitor SE active in islets (log enrichment = 1.62, 95% CI = <-20, 3.14). Examples of known T2D loci with T2D-associated variants in SE active in pancreatic progenitors but not in islets included LAMA1 and PROX1. These results suggest that a subset of T2D variants may affect disease risk by altering regulatory programs specifically active in pancreatic progenitors.

### Pancreatic progenitor-specific stretch enhancers are near genes that regulate tissue morphogenesis

Having observed enrichment of T2D risk variants in pancreatic progenitor SE independent of islet SE, we next sought to further characterize the regulatory programs of SE with specific function in pancreatic progenitors. We therefore defined a set of pancreatic progenitor-specific stretch enhancers (PSSE) based on the following criteria: (i) annotation as a SE at the PP2 stage, (ii) no classification as a SE at the ES, DE, and GT stages, and (iii) no classification as a TE or SE in islets. Applying these criteria, we identified a total of 492 PSSE genome-wide (Figure 2A and Figure 2—source data 1).

![Figure 2.](https://cdn.elifesciences.org/articles/59067/elife-59067-fig2-v1.jpg)

**Figure 2.:** (A) Schematic illustrating identification of pancreatic progenitor-specific stretch enhancers (PSSE). (B) Heatmap showing density of H3K27ac ChIP-seq and ATAC-seq reads at PSSE, centered on overlapping H3K27ac and ATAC-seq peaks, respectively, and spanning 5 kb in ES, DE, GT, PP1, PP2, and islets. PSSE coordinates in Figure 2—source data 1. (C) Percentage of PSSE exhibiting indicated chromatin states at defined developmental stages and in islets. (D) Percentage of PSSE overlapping with at least one ChIP-seq peak at PP2 for the indicated transcription factors. Enrichment analysis comparing observed and expected overlap based on random genomic regions of the same size and located on the same chromosome averaged over 10,000 iterations (***p<1×10−4; permutation test). (E) Gene ontology analysis for nearest expressed genes (fragments per kilobase per million fragments mapped (FPKM) ≥1 at PP2) to the 492 PSSE. See also Figure 2—source data 2. (F) Enrichment (LD score regression coefficient z-scores) of T2D, developmental, and metabolic GWAS trait-associated variants at accessible chromatin sites in PSSE as compared with PP2 and islet stretch enhancers. Significant enrichment was identified within accessible chromatin at PP2 stretch enhancers for lean type 2 diabetes (Z = 2.06, *p=3.94 × 10−2), at PP2 stretch enhancers for type 2 diabetes (Z = 3.57, ***p=3.52 × 10−4), at islet stretch enhancers for type 2 diabetes (Z = 2.78, **p=5.46 × 10−3), at islet stretch enhancers for fasting proinsulin levels (Z = 2.83, **p=4.61 × 10−3), at islet stretch enhancers for HOMA-B (Z = 2.58, **p=9.85 × 10−3), at PP2 stretch enhancers for disposition index (Z = 2.18, *p=2.94 × 10−2), at islet stretch enhancers for acute insulin response (Z = 2.24, *p=2.51 × 10−2), at islet stretch enhancers for HbA1c (Z = 1.98, *p=4.72 × 10−2), and at islet stretch enhancers for fasting glucose levels (Z = 2.64, **p=8.31 × 10−3). See also Figure 2—source data 3 and Figure 2—figure supplement 1.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/59067/elife-59067-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** (A) Percentage of PSSE overlapping with at least one ATAC-seq peak at PP2. Enrichment analysis comparing observed and expected overlap based on random genomic regions of the same size and located on the same chromosome averaged over 10,000 iterations (***p<1 × 10−4; permutation test). (B) Percentage of PSSE overlapping 0, 1, 2, 3, or 4+ ATAC-seq peaks at PP2. (C) Enriched transcription factor (TF) binding motifs with associated p-values at ATAC-seq peaks at PP2 intersecting PSSE. Fisher’s exact test, two sided, corrected for multiple comparisons. (D) Box plots showing mRNA levels based on RNA-seq of nearest expressed genes (fragments per kilobase per million fragments mapped (FPKM) ≥1 at PP2) for PSSE at each developmental stage and in islets (*p=1.10 × 10−2 for GT vs PP1; ***p=1.80 × 10−8 for GT vs PP2, p<2.2 × 10−16 for PP2 vs islet; Wilcoxon rank sum test, two sided). Plots are centered on median, with box encompassing 25-75th percentile and whiskers extending up to 1.5 interquartile range. n = 3 replicates from independent differentiations at ES, DE, GT, PP1, and PP2, respectively; n = 3 islet replicates. (E) Box plots showing H3K27ac signal at PSSE in tissues and cell lines from the ENCODE and Epigenome Roadmap projects as well as in developmental intermediates and islets (ISL). Plots are centered on median, with box encompassing 25-75th percentile and whiskers extending up to 1.5 interquartile range. See also Figure 2—source data 4. (F) Number of PSSE overlapping defined chromatin states in human adipose stromal cells from preadipose (hASC1) to mature adipose state (hASC4) (from Varshney et al., 2017). ChromHMM classifications: Quiescent; ReprPCWk, Weak Repressed PolyComb; TxWk, Weak Transcription; Tx, Strong Transcription; EnhWk, Weak Enhancer; ReprPC, Repressed Polycomb; EnhA1, Active Enhancer 1; EnhG, Genic Enhancer; EnhA2, Active Enhancer 2.

As expected based on their chromatin state classification, PSSE acquired broad deposition of the active enhancer mark H3K27ac at the PP1 and PP2 stages (Figure 2B,C). Coincident with an increase in H3K27ac signal, chromatin accessibility at PSSE also increased (Figure 2B), and 93.5% of PSSE contained at least one accessible chromatin site at the PP2 stage (Figure 2—figure supplement 1A,B). Further investigation of PSSE chromatin state dynamics at earlier stages of pancreatic differentiation revealed that PSSE were often poised (defined by H3K4me1 in the absence of H3K27ac) prior to activation (42%, 48%, 63%, and 17% of PSSE in ES, DE, GT, and PP1, respectively; Figure 2C), consistent with earlier observations that a poised enhancer state frequently precedes enhancer activation during development (Rada-Iglesias et al., 2011; Wang et al., 2015). Intriguingly, a subset of PSSE was classified as TE earlier in development (13%, 23%, 29%, and 46% of PSSE in ES, DE, GT, and PP1, respectively; Figure 2C), suggesting that SE emerge from smaller regions of active chromatin seeded at prior stages of development. During differentiation into mature islet cells, PSSE lost H3K27ac but largely retained H3K4me1 signal (62% of PSSE) (Figure 2C), persisting in a poised state in terminally differentiated islet cells.

To gain insight into the transcription factors that regulate PSSE, we conducted motif enrichment analysis of accessible chromatin sites within PSSE (Figure 2—figure supplement 1C). Consistent with the activation of PSSE upon pancreas induction, motifs associated with transcription factors known to regulate pancreatic development (Conrad et al., 2014; Masui et al., 2007) were enriched, including FOXA (p=1 × 10−34), PDX1 (p=1 × 10−30), GATA (p=1 × 10−25), ONECUT (p=1 × 10−17), and RBPJ (p=1 × 10−14), suggesting that pancreatic lineage-determining transcription factors activate PSSE. Analysis of the extent of PSSE overlap with ChIP-seq binding sites for FOXA1, FOXA2, GATA4, GATA6, PDX1, HNF6, and SOX9 at the PP2 stage substantiated this prediction (p<1 × 10−4 for all transcription factors; permutation test; Figure 2D).

Annotation of biological functions of predicted target genes for PSSE (nearest gene with FPKM ≥1 at PP2 stage) revealed gene ontology terms related to developmental processes, such as tissue morphogenesis (p=1 × 10−7) and vascular development (p=1 × 10−8), as well as developmental signaling pathways, including BMP (p=1 × 10−5), NOTCH (p=1 × 10−4), and canonical Wnt signaling (p=1 × 10−4; Figure 2E and Figure 2—source data 2), which have demonstrated roles in pancreas morphogenesis and cell lineage allocation (Ahnfelt-Rønne et al., 2010; Li et al., 2015; Murtaugh, 2008; Sharon et al., 2019; Sui et al., 2013). Consistent with the temporal pattern of H3K27ac deposition at PSSE, transcript levels of PSSE-associated genes increased upon pancreatic lineage induction and peaked at the PP2 stage (p=1.8 × 10−8; Figure 2—figure supplement 1D). Notably, expression of these genes sharply decreased in islets (p<2.2 × 10−16), underscoring the likely role of these genes in regulating pancreatic development but not mature islet function.

### Pancreatic progenitor-specific stretch enhancers are highly specific across T2D-relevant tissues and cell types

We next sought to understand the phenotypic consequences of PSSE activity in the context of T2D pathophysiology. Variants in accessible chromatin sites of PSSE genome-wide were enriched for T2D association (log enrichment = 2.85, 95% CI = <-20, 4.09). We determined enrichment of genetic variants for T2D-related quantitative endophenotypes within accessible chromatin sites of PSSE, as well as all pancreatic progenitor SE (not just progenitor-specific) and islet SE, using LD score regression (Bulik-Sullivan et al., 2015; Finucane et al., 2015). As expected based on prior observations (Parker et al., 2013; Pasquali et al., 2014), we observed enrichment (Z > 1.96) of variants associated with quantitative traits related to insulin secretion and beta cell function within islet SE, exemplified by fasting proinsulin levels, HOMA-B, and acute insulin response (Z = 2.8, Z = 2.6, and Z = 2.2, respectively; Figure 2F). Conversely, PSSE showed a trend toward depletion for these traits, although the estimates were not significant. We further tested for enrichment in the proportion of variants in PSSE and islet SE nominally associated (p<0.05) with beta cell function traits compared to background variants. There was significant enrichment of beta cell trait association among islet SE variants (χ2 test; p<0.05 for all beta cell functional traits except for insulin secretion rate), but no corresponding enrichment for PSSE (Figure 2—source data 3).

A prior study found that variants at the LAMA1 locus had stronger effects on T2D risk among lean relative to obese cases (Perry et al., 2012). Since we identified a PSSE at the LAMA1 locus, we postulated that variants in PSSE collectively might have differing impact on T2D risk in cases segregated by BMI. We therefore tested PSSE, as well as pancreatic progenitor SE and islet SE, for enrichment of T2D association using GWAS of lean and obese T2D (Perry et al., 2012), using LD score regression (Bulik-Sullivan et al., 2015; Finucane et al., 2015). We observed nominally significant enrichment of variants in pancreatic progenitor SE for T2D among lean cases (Z = 2.1). Variants in PSSE were mildly enriched for T2D among lean (Z = 1.1) and depleted among obese (Z = −0.70) cases, although neither estimate was significant. By comparison, islet SE showed positive enrichment for T2D among both lean (Z = 1.9) and obese cases (Z = 1.3; Figure 2F). Together, these results suggest that PSSE may affect T2D risk in a manner distinct from islet SE function.

Having observed little evidence for enrichment of PSSE variants for traits related to beta cell function, we asked whether the enrichment of PSSE for T2D-associated variants could be explained by PSSE activity in T2D-relevant tissues and cell types outside the pancreas. We assessed PSSE activity by measuring H3K27ac signal in 95 representative tissues and cell lines from the ENCODE and Epigenome Roadmap projects (Kundaje et al., 2015). Interestingly, there was group-wide specificity of PSSE to pancreatic progenitors relative to other cells and tissues including those relevant to T2D, such as adipose tissue, skeletal muscle, and liver (Figure 2—figure supplement 1E and Figure 2—source data 4). Since gene regulation in adipocyte precursors also contributes to T2D risk (Claussnitzer et al., 2014), we further examined PSSE specificity with respect to chromatin states during adipogenesis, using data from human adipose stromal cell differentiation stages (hASC1-4) (Mikkelsen et al., 2010; Varshney et al., 2017). PSSE exhibited virtually no active chromatin during adipogenesis (9, 8, 6, and 8 out of the 492 PSSE were active enhancers in hACS-1, hASC-2, hASC-3, and hASC-4, respectively; Figure 2—figure supplement 1F). These findings identify PSSE as highly pancreatic progenitor-specific across T2D-relevant tissues and cell types.

### Identification of pancreatic progenitor-specific stretch enhancers harboring T2D-associated variants

Given the relative specificity of PSSE to pancreatic progenitors, we next sought to identify T2D-associated variants in PSSE at specific loci which may affect pancreatic development. We therefore identified variants in PSSE with evidence of T2D association (at p=4.7 × 10−6) after correcting for the total number of variants in PSSE genome-wide (n = 10,738). In total there were 49 variants in PSSE with T2D association exceeding this threshold mapping to 11 loci (Figure 3A). This included variants at nine loci with known genome-wide significant T2D association (PROX1, ST6GAL1, SMARCAD1, XKR6, INS-IGF2, HMGA2, SMEK1, HMG20A, and LAMA1), as well as at two previously unreported loci with sub-genome-wide significant association, CRB2 and PGM1. To identify candidate target genes of the T2D-associated PSSE in pancreatic progenitors, we analyzed the expression of all genes within the same topologically associated domain (TAD) as the PSSE in PP2 cells and in primary human embryonic pancreas tissue (Figure 3B and Figure 3—figure supplement 1A). These expressed genes are candidate effector transcripts of T2D-associated variants in pancreatic progenitors.

![Figure 3.](https://cdn.elifesciences.org/articles/59067/elife-59067-fig3-v1.jpg)

**Figure 3.:** (A) Manhattan plot showing T2D association p-values (from Mahajan et al., 2018) for 10,738 variants mapping within PSSE. The dotted line shows the threshold for Bonferroni correction (p=4.66 × 10−6). Novel loci identified with this threshold and mapping at least 500 kb away from a known locus are highlighted in blue. Chromosomal coordinates of T2D-associated PSSE are indicated. (B) mRNA levels (measured in fragments per kilobase per million fragments mapped [FPKM]) at PP2 (blue) and in human embryonic pancreas (54 and 58 days gestation, gold) of nearest expressed (FPMK ≥1) gene at PP2 for PSSE harboring T2D variants identified in A. (C) PP2 specificity of H3K27ac signal at PSSE harboring T2D variants identified in A. Z-score comparing H3K27ac signal at PP2 to H3K27ac signal in tissues and cell lines from the ENCODE and Epigenome Roadmap projects. See also Figure 3—figure supplement 1.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/59067/elife-59067-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** (A) mRNA levels (measured in fragments per kilobase per million fragments mapped [FPKM]) at PP2 and in human embryonic pancreas (54 and 58 days gestation, Emb Pan) of all genes expressed (FPKM ≥1) at PP2 and located within topologically associated domains (TADs) containing indicated PSSE harboring T2D variants identified in Figure 3A. (B) Heatmap showing H3K27ac signal at PSSE harboring T2D variants identified in Figure 3A. Quantification in tissues and cell lines from the ENCODE and Epigenome Roadmap projects (tissues) as well as in developmental intermediates and islets (ISL) is shown. (C) H3K27ac signal at LAMA1-associated PSSE in tissues and cell lines from the ENCODE and Epigenome Roadmap projects as well as in developmental intermediates and islets.

As many pancreatic progenitor SE remain poised in mature islets (Figure 2C), we considered whether T2D-associated variants in PSSE could have gene regulatory function in islets that is re-activated in the disease state. We therefore assessed overlap of PSSE variants with accessible chromatin of islets from T2D donors (Khetan et al., 2018). None of the strongly T2D-associated variants in PSSE (p=4.7 × 10−6) overlapped an islet accessible chromatin site in T2D islets, arguing against the relevance of PSSE in broadly regulating islet gene activity during T2D.

### A pancreatic progenitor-specific stretch enhancer at LAMA1 harbors T2D risk variants and regulates LAMA1 expression selectively in pancreatic progenitors

Variants in a PSSE at the LAMA1 locus were associated with T2D at genome-wide significance (Figure 3A), and LAMA1 was highly expressed in the human embryonic pancreas (Figure 3B). Furthermore, the activity of the PSSE at the LAMA1 locus was almost exclusively restricted to pancreatic progenitors (Figure 3—figure supplement 1B,C), and was further among the most progenitor-specific across all PSSE harboring T2D risk variants (Figure 3C). In addition, reporter gene assays in zebrafish embryos have shown that this enhancer drives gene expression specific to pancreatic progenitors in vivo (Cebola et al., 2015). We therefore postulated that the activity of T2D-associated variants within the LAMA1 PSSE is relevant for gene regulation in pancreatic progenitors, and we sought to characterize the LAMA1 PSSE in greater depth.

Multiple T2D-associated variants mapped within the LAMA1 PSSE, and these variants were further in the 99% credible set in fine-mapping data from the DIAMANTE consortium (Mahajan et al., 2018; Figure 4A). No other variants in the 99% credible set mapped in an accessible chromatin site active in islets from either non-diabetic or T2D samples. The PSSE is intronic to the LAMA1 gene and contains regions of poised chromatin and TE at prior developmental stages (Figure 4A). Consistent with its stepwise genesis as a SE throughout development, regions of open chromatin within the LAMA1 PSSE were already present at the DE and GT stages. Furthermore, pancreatic lineage-determining transcription factors, such as FOXA1, FOXA2, GATA4, GATA6, HNF6, SOX9, and PDX1, were all bound to the PSSE at the PP2 stage (Figure 4B). Among credible set variants in the LAMA1 PSSE, rs10502347 overlapped an ATAC-seq peak as well as ChIP-seq sites for multiple pancreatic lineage-determining transcription factors. Additionally, rs10502347 directly coincided with a SOX9 footprint identified in ATAC-seq data from PP2 cells, and the T2D risk allele C is predicted to disrupt SOX9 binding (Figure 4B). Consistent with the collective endophenotype association patterns of PSSE (Figure 2F), rs10502347 showed no association with beta cell function (p=0.81, 0.23, 0.46 for fasting proinsulin levels, HOMA-B, and acute insulin response, respectively; Figure 4—figure supplement 1A). Thus, T2D variant rs10502347 is predicted to affect the binding of pancreatic transcription factors and does not appear to affect beta cell function.

![Figure 4.](https://cdn.elifesciences.org/articles/59067/elife-59067-fig4-v1.jpg)

**Figure 4.:** (A) (Top) Locus plots showing T2D association p-values for variants in a 35 kb window (hg19 chr18:7,050,000–7,085,000) at the LAMA1 locus and LAMA1 PSSE (red box). Fine mapped variants within the 99% credible set for the LAMA1 locus are colored black. All other variants are colored light gray. (Bottom) Chromatin states and ATAC-seq signal in ES, DE, GT, PP1, and PP2. TssA, active promoter; TssFlnk, flanking transcription start site; TssBiv, bivalent promoter; Repr, repressed; EnhA, active enhancer; EnhP, poised enhancer. (B) FOXA1, FOXA2, GATA4, GATA6, HNF6, SOX9, and PDX1 ChIP-seq profiles at the LAMA1 PSSE in PP2. The variant rs10502347 (red) overlaps transcription factor binding sites and a predicted ATAC-seq footprint for the SOX9 sequence motif. Purple dotted lines indicate the core binding profile of the average SOX9 footprint genome-wide and the blue dotted line indicates the position of rs10502347 within the SOX9 motif. (C) LAMA1 mRNA expression at each developmental stage determined by RNA-seq, measured in fragments per kilobase per million fragments mapped (FPKM). Data shown as mean ± S.E.M. (n = 3 replicates from independent differentiations). Light blue and purple indicate classification of the LAMA1 PSSE as typical enhancer (TE) and stretch enhancer (SE), respectively. (D) LAMA1 mRNA expression at each developmental stage determined by qPCR in control and ∆LAMA1Enh cells. Data are shown as mean ± S.E.M. (n = 3 replicates from independent differentiations for control cells. ∆LAMA1Enh cells represent combined data from two clonal lines with three replicates for each line from independent differentiations. n = 3 technical replicates for each sample; p=0.319, 0.594, 0.945, 0.290, and <1 × 10−6 for comparisons in ES, DE, GT, PP1, and PP2, respectively; student’s t-test, two sided; ***p<0.001, n.s., not significant). Light blue and purple indicate classification of the LAMA1 PSSE as TE and SE, respectively. Each plotted point represents the average of technical replicates for each differentiation. (E) mRNA expression determined by RNA-seq at PP2 of genes expressed in either control or ∆LAMA1Enh cells (FPKM ≥ 1 at PP2) and located within the same topologically associated domain as LAMA1. Data are shown as mean FPKM ± S.E.M. (n = 2 replicates from independent differentiations for control cells. ∆LAMA1Enh cells represent combined data from two clonal lines with two replicates for each line from independent differentiations. p adj. = 0.389 and 8.11 × 10−3 for ARHGAP28 and LAMA1, respectively; DESeq2). See also Figure 4—figure supplements 1 and 2.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/59067/elife-59067-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** (A) Odds ratio estimates (points) and 95% CIs (lines) for rs10502347 association with T2D and metabolic GWAS traits. Significant associations are colored black, non-significant are colored light grey. (B) Schematic illustrating CRISPR-Cas9-mediated deletion strategy of LAMA1-associated PSSE to generate independent ∆LAMA1Enh hESC clones with different DNA cleavage products. (C) Flow cytometry analysis for NKX6.1 and PDX1 comparing control and ∆LAMA1Enh PP2 cells. Isotype control (ISO) for each antibody is shown in red and target protein staining in green. Percentage of cells expressing each protein is indicated (representative experiment, n = 3 independent differentiations). (D) Immunofluorescent staining for NKX6.1 and PDX1 in control and ∆LAMA1Enh PP2 cells (representative images, n = 2 slides). Scale bar, 50 μm. (E) mRNA expression of pancreatic transcription factors determined by RNA-seq in control and ∆LAMA1Enh PP2 cells. Data are shown as mean of fragments per kilobase per million fragments mapped (FPKM) ± S.E.M. (n = 2 replicates from independent differentiations for control cells. ∆LAMA1Enh cells represent combined data from two clonal lines with two replicates for each line from independent differentiations. p adj. = 3.56 × 10−2, 0.224, 0.829, 8.14 × 10−2, and 0.142, for comparisons of PDX1, NKX6.1, PROX1, PTF1A, and SOX9, respectively; DESeq2; * p adj. <0.05, n.s., not significant). (F) Similarity matrix showing Pearson correlations for normalized transcriptomes (log transformed expression for genes with FPKM ≥1 in ≥1 replicates) in control and ∆LAMA1Enh PP2 cells (n = 2 independent differentiations for control cells and for each ∆LAMA1Enh clone). See also Figure 4—source datas 1 and 2.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/59067/elife-59067-fig4-figsupp2-v1.jpg)

**Figure 4—figure supplement 2.:** (A) Schematic illustrating CRISPR-Cas9-mediated deletion strategy of LAMA1 to generate ∆LAMA1 hESC clonal line. (B) Immunofluorescent staining for Laminin in control and ∆LAMA1 PP2 cells (representative images, n = 2 independent slides). Scale bar, 50 μm. (C) Flow cytometry analysis for NKX6.1 and PDX1 comparing control and ∆LAMA1 PP2 cells. Isotype control (ISO) for each antibody is shown in red and target protein staining in green. Percentage of cells expressing each protein is indicated. (D) Immunofluorescent staining for NKX6.1 and PDX1 in control and ∆LAMA1 PP2 cells (representative images, n = 2 independent slides). Scale bar, 50 μm. (E) mRNA expression of pancreatic transcription factors determined by qPCR in control and ∆LAMA1 PP2 cells. Data are shown as mean ± S.E.M. (n = 3 replicates from independent differentiations. n = 3 technical replicates for each sample; p=2.19 × 10−2, 0.360, 6.25 × 10−2, 0.710, and 0.122 for comparisons of PDX1, NKX6.1, PROX1, PTF1A, and SOX9 expression in control compared to ∆LAMA1 PP2 cells, respectively; student’s t-test, two sided; n.s., not significant, *p<0.01). Each plotted point represents the average of technical replicates for each differentiation.

Enhancers can control gene expression over large genomic distances, and therefore their target genes cannot be predicted based on proximity alone. To directly assess the function of the LAMA1 PSSE in regulating gene activity, we utilized CRIPSR-Cas9-mediated genome editing to generate two independent clonal human hESC lines harboring homozygous deletions of the LAMA1 PSSE (hereafter referred to as ∆LAMA1Enh; Figure 4—figure supplement 1B). We examined LAMA1 expression in ∆LAMA1Enh compared to control cells throughout stages of pancreatic differentiation. Consistent with the broad expression of LAMA1 across developmental and mature tissues, control cells expressed LAMA1 at all stages (Figure 4C). LAMA1 was expressed at similar levels in ∆LAMA1Enh and control cells at early developmental stages, but was significantly reduced in PP2 cells derived from ∆LAMA1Enh clones (p=0.319, 0.594, 0.945, 0.290, and <1 × 10−6 for comparisons in ES, DE, GT, PP1, and PP2, respectively; Figure 4D). To next investigate whether the LAMA1 PSSE regulates other genes at this locus, we utilized Hi-C datasets from PP2 cells to identify topologically associated domains (TADs). We then examined expression of genes mapping in the same TAD as the LAMA1 PSSE. ARHGAP28 was the only other expressed gene within the TAD, and albeit not significantly different from controls (p.adj >0.05), showed a trend toward lower expression in ∆LAMA1Enh PP2 cells (Figure 4E), raising the possibility that ARHGAP28 is an additional target gene of the LAMA1 PSSE. Together, these results demonstrate that while LAMA1 itself is broadly expressed across developmental stages, the T2D-associated PSSE regulates LAMA1 expression specifically in pancreatic progenitors.

To determine whether deletion of the LAMA1 PSSE affects pancreatic development, we generated PP2 stage cells from ∆LAMA1Enh and control hESC lines and analyzed pancreatic cell fate commitment by flow cytometry and immunofluorescence staining for PDX1 and NKX6.1 (Figure 4—figure supplement 1C,D). At the PP2 stage, ∆LAMA1Enh and control cultures contained similar percentages of PDX1- and NKX6.1-positive cells. Furthermore, mRNA expression of PDX1, NKX6.1, PROX1, PTF1A, and SOX9 was either unaffected or only minimally reduced (p adj. = 3.56 × 10−2, 0.224, 0.829, 8.14 × 10−2, and 0.142, for comparisons of PDX1, NKX6.1, PROX1, PTF1A, and SOX9 expression, respectively; Figure 4—figure supplement 1E), and the overall gene expression profiles as determined by RNA-seq were similar in ∆LAMA1Enh and control PP2 cells (Figure 4—figure supplement 1F and Figure 4—source datas 1 and 2). To examine effects of complete LAMA1 loss-of-function, we additionally generated a hESC line harboring a deletion of the LAMA1 coding sequences (hereafter referred to as ∆LAMA1; Figure 4—figure supplement 2A,B), and produced PP2 stage cells. Similar to ∆LAMA1Enh cultures, ∆LAMA1 and control PP2 stage cultures contained similar numbers of PDX1- and NKX6.1-positive cells (Figure 4—figure supplement 2C,D). Likewise, mRNA expression of PDX1, NKX6.1, PROX1, PTF1A, and SOX9 was similar in ∆LAMA1 and control PP2 cells (p=4.3 × 10−2, 0.19, 0.16, 0.17, and 8.7 × 10−2, respectively; Figure 4—figure supplement 2E). These findings indicate that in vitro pancreatic lineage induction is unperturbed in both ∆LAMA1Enh cells exhibiting reduced LAMA1 expression, as well as ∆LAMA1 cells where LAMA1 coding sequences are disrupted.

### Pancreatic progenitor-specific stretch enhancers at the CRB2 and PGM1 loci harbor T2D-associated variants

Multiple variants with evidence for T2D association in PSSE mapped outside of known risk loci, such as those mapping to CRB2 and PGM1 (Figure 3A). As with the LAMA1 PSSE, PSSE harboring variants at CRB2 and PGM1 were intronic to their respective genes, contained ATAC-seq peaks, and bound pancreatic lineage-determining transcription factors FOXA1, FOXA2, GATA4, GATA6, HNF6, SOX9, and PDX1 (Figure 5A,B and Figure 5—figure supplement 1A,B). Compared to the LAMA1 PSSE, CRB2 and PGM1 PSSE were less specific to pancreatic progenitors and exhibited significant H3K27ac signal in several other tissues and cell types, most notably brain, liver, and the digestive tract (Figure 5—figure supplement 1C,D).

![Figure 5.](https://cdn.elifesciences.org/articles/59067/elife-59067-fig5-v1.jpg)

**Figure 5.:** (A) (Top) Locus plots showing T2D association p-values for variants in a 35 kb window (hg19 chr9:126,112,000–126,147,000) at the CRB2 locus and CRB2 PSSE (red box). Fine mapped variants within the 99% credible set for the novel CRB2 locus are colored black. All other variants are colored light gray. (Bottom) Chromatin states and ATAC-seq signal in ES, DE, GT, PP1, and PP2. TssA, active promoter; TssFlnk, flanking transcription start site; TssBiv, bivalent promoter; Repr, repressed; EnhA, active enhancer; EnhP, poised enhancer. (B) FOXA1, FOXA2, GATA4, GATA6, HNF6, SOX9, and PDX1 ChIP-seq profiles at the CRB2 PSSE in PP2. The variant rs2491353 (black) overlaps with transcription factor binding sites. (C) CRB2 mRNA expression at each developmental stage determined by RNA-seq, measured in fragments per kilobase per million fragments mapped (FPKM). Data shown as mean ± S.E.M. (n = 3 replicates from independent differentiations). Light blue and purple indicate classification of the CRB2 PSSE as typical enhancer (TE) and stretch enhancer (SE), respectively. Plotted points represent average of technical replicates for each differentiation. (D) CRB2 mRNA expression at each developmental stage determined by qPCR in control and ∆CRB2Enh cells. Data are shown as mean ± S.E.M. (n = 3 replicates from independent differentiations for control cells. ∆CRB2Enh cells represent combined data from two clonal lines with three replicates for each line from independent differentiations. n = 3 technical replicates for each sample; p=7.03 × 10−4,<1 × 10−6,<1 × 10−6, 1.46 × 10−2, and <1 × 10−6 for comparisons in ES, DE, GT, PP1, and PP2, respectively; student’s t-test, two sided; ***p<0.001 **p<0.01). Light blue and purple indicate classification of the CRB2 PSSE as TE and SE, respectively. Each plotted point represents the average of technical replicates for each differentiation. (E) mRNA expression determined by RNA-seq at PP2 of genes expressed in either control or ∆CRB2Enh cells (FPKM ≥ 1 at PP2) and located within the same topologically associated domain as CRB2. Data are shown as mean FPKM ± S.E.M. (n = 2 replicates from independent differentiations for control cells. ∆CRB2Enh cells represent combined data from two clonal lines with two replicates for each line from independent differentiations. p adj. = 0.158, 1.00, and 3.51 × 10−3, for MIR600HG, STRBP, and CRB2, respectively; DESeq2; **p<0.01, n.s., not significant). See also Figure 5—figure supplements 1–3.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/59067/elife-59067-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** (A) (Top) Locus plots showing T2D association p-values for variants in a 43 kb window (hg19 chr1:64,084,000–64,127,000) at the PGM1 locus and PGM1 PSSE (red box). Fine mapped variants within the 99% credible set for the novel PGM1 locus are colored black. All other variants are colored light gray. (Bottom) Chromatin states and ATAC-seq signal in ES, DE, GT, PP1, and PP2. TssA, active promoter; TssFlnk, flanking transcription start site; TssBiv, bivalent promoter; Repr, repressed; EnhA, active enhancer; EnhP, poised enhancer. (B) FOXA1, FOXA2, GATA4, GATA6, HNF6, SOX9, and PDX1 ChIP-seq profiles at the PGM1 PSSE in PP2 cells. The variants rs2269247, rs2301055, rs2301054, and rs2269246 (black) overlap with transcription factor binding sites. (C) H3K27ac signal at CRB2-associated PSSE in tissues and cell lines from the ENCODE and Epigenome Roadmap projects as well as in developmental intermediates and islets (ISL). (D) H3K27ac signal at PGM1-associated PSSE in tissues and cell lines from the ENCODE and Epigenome Roadmap projects as well as in developmental intermediates and islets.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/59067/elife-59067-fig5-figsupp2-v1.jpg)

**Figure 5—figure supplement 2.:** (A) Schematic illustrating CRISPR-Cas9-mediated deletion strategy of CRB2-associated PSSE to generate independent ∆CRB2Enh hESC clones with different DNA cleavage products. (B) Flow cytometry analysis for NKX6.1 and PDX1 comparing control and ∆CRB2Enh PP2 cells. Isotype control (ISO) for each antibody is shown in red and target protein staining in green. Percentage of cells expressing each protein is indicated (representative experiment, n = 3 independent differentiations). (C) Immunofluorescent staining for NKX6.1 and PDX1 in control and ∆CRB2Enh PP2 cells (representative images, n = 2 independent slides). Scale bar, 50 μm. (D) mRNA expression of pancreatic transcription factors determined by RNA-seq in control and ∆CRB2Enh PP2 cells. Data are shown as mean of fragments per kilobase per million fragments mapped (FPKM) ± S.E.M. (n = 2 replicates from independent differentiations for control cells ∆CRB2Enh cells represent combined data from two clonal lines with two replicates for each line from independent differentiations. p adj. = 1.00, 1.00, 1.00, 1.00, and 1.00, for comparisons of PDX1, NKX6.1, PROX1, PTF1A, and SOX9, respectively; DESeq2; n.s., not significant). (E) Similarity matrix showing Pearson correlations for normalized transcriptomes (log transformed expression for genes with FPKM ≥1 in ≥1 replicates) in control and ∆CRB2Enh PP2 cells (n = 2 independent differentiations for control cells and for each ∆CRB2Enh clone). See also Figure 5—source data 1.

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/59067/elife-59067-fig5-figsupp3-v1.jpg)

**Figure 5—figure supplement 3.:** (A) Schematic illustrating CRISPR-Cas9-mediated deletion strategy of CRB2 to generate ∆CRB2 hESC clonal line. (B) Immunofluorescent staining for CRB2 in control and ∆CRB2 PP2 cells (representative images, n = 2 independent slides). Scale bar, 50 μm. (C) Flow cytometry analysis for NKX6.1 and PDX1 comparing control and ∆CRB2 PP2 cells. Isotype control (ISO) for each antibody is shown in red and target protein staining in green. Percentage of cells expressing each protein is indicated. (D) Immunofluorescent staining for NKX6.1 and PDX1 in control and ∆CRB2 PP2 cells (representative images, n = 2 independent slides). Scale bar, 50 μm. (E) mRNA expression of pancreatic transcription factors determined by qPCR in control and ∆CRB2 PP2 cells. Data are shown as mean ± S.E.M. (n = 3 replicates from independent differentiations. n = 3 technical replicates for each sample; p=0.241, 0.971, 0.397, 0.374, and 0.311 for comparisons of PDX1, NKX6.1, PROX1, PTF1A, and SOX9 expression in control compared to ∆CRB2 PP2 cells, respectively; student’s t-test, two sided; n.s., not significant). Each plotted point represents the average of technical replicates for each differentiation.

CRB2 is a component of the Crumbs protein complex involved in the regulation of cell polarity and neuronal, heart, retinal, and kidney development (Alves et al., 2013; Bulgakova and Knust, 2009; Dudok et al., 2016; Jiménez-Amilburu and Stainier, 2019; Slavotinek et al., 2015). However, its role in pancreatic development is unknown. To determine whether the CRB2 PSSE regulates CRB2 expression in pancreatic progenitors, we generated two independent hESC clones with homozygous deletions of the CRB2 PSSE (hereafter referred to as ∆CRB2Enh; Figure 5—figure supplement 2A) and performed pancreatic differentiation of ∆CRB2Enh and control hESC lines. In control cells, CRB2 was first expressed at the GT stage and increased markedly at the PP1 stage (Figure 5C). This pattern of CRB2 expression is consistent with H3K27ac deposition at the CRB2 PSSE in GT stage cells and classification as a SE at the PP1 and PP2 stages (Figure 5A and Figure 5—figure supplement 1C). In ∆CRB2Enh cells, we observed upregulation of CRB2 expression at earlier developmental stages, in particular at the DE and GT stages (p<1 × 10−6 at both stages; Figure 5D), suggesting that the CRB2 PSSE may be associated with repressive transcriptional complexes prior to pancreas induction. At the PP2 stage, CRB2 expression was significantly reduced in ∆CRB2Enh cells (p adj. = 3.51 × 10−3; Figure 5D), whereas the expression of other genes in the same TAD was not affected (p adj. ≥0.05; Figure 5E). Thus, the CRB2 PSSE specifically regulates CRB2 and is required for CRB2 expression in pancreatic progenitors.

Phenotypic characterization of PP2 stage ∆CRB2Enh cultures revealed similar percentages of PDX1- and NKX6.1-positive cells as in control cultures (Figure 5—figure supplement 2B,C). The expression of pancreatic transcription factors and global gene expression profiles were also similar in ∆CRB2Enh and control PP2 cells (Figure 5—figure supplement 2D,E and Figure 5—source data 1). Likewise, CRB2 deletion hESCs (∆CRB2) differentiated to the PP2 stage (Figure 5—figure supplement 3A,B) produced similar numbers of PDX1- and NKX6.1-positive cells and expressed pancreatic transcription factors at levels similar to control cells (Figure 5—figure supplement 3C–E). Thus, neither deletion of the CRB2 PSSE nor the CRB2 gene overtly impairs pancreatic lineage induction in the in vitro hESC differentiation system.

### lama1 and crb2 zebrafish morphants display annular pancreas and decreased beta cell mass

Based on their classification as extracellular matrix and cell polarity proteins, respectively, Laminin (encoded by LAMA1) and CRB2 are predicted to regulate processes related to tissue morphogenesis, such as cell migration, tissue growth, and cell allocation within the developing organ. Furthermore, PSSE in general were enriched for proximity to genes involved in tissue morphogenesis (Figure 2E), suggesting that T2D risk variants acting within PSSE could have roles in pancreas morphogenesis. Since cell migratory processes and niche-specific signaling events are not fully modeled during hESC differentiation, we reasoned that the in vitro pancreatic differentiation system might not be suitable for studying Laminin and CRB2 function in pancreatic development.

To circumvent these limitations, we employed zebrafish as an in vivo vertebrate model to study the effects of reduced lama1 and crb2 levels on pancreatic development. The basic organization and cell types in the pancreas as well as the genes regulating endocrine and exocrine pancreas development are highly conserved between zebrafish and mammals (Dong et al., 2008; Field et al., 2003; Kimmel et al., 2015). To analyze pancreatic expression of Laminin and Crb proteins, we used Tg(ptf1a:eGFP)jh1 embryos to visualize pancreatic progenitor cells and the acinar pancreas by eGFP expression. At 48 hr post-fertilization (hpf), both Laminin and Crb proteins were detected in the eGFP and Nkx6.1 co-positive pancreatic progenitor cell domain (Figure 6—figure supplement 1A,B).

To determine the respective functions of lama1 and crb2 in pancreatic development, we performed knockdown experiments using anti-sense morpholinos directed against lama1 and the two zebrafish crb2 genes, crb2a and crb2b (Omori and Malicki, 2006; Pollard et al., 2006). Knockdown efficiency of each morpholino was validated using whole-mount immunohistochemistry. We observed significant reduction of Laminin staining throughout the pancreatic progenitor cell domain in embryos treated with morpholinos targeting lama1 (Figure 6—figure supplement 2A–D). In embryos treated with morpholinos targeting crb2a or crb2a and crb2b, we observed loss of staining in the pancreatic progenitor cell domain using antibodies specific to Crb2a or antibodies detecting all Crb proteins, respectively (Figure 6—figure supplement 3A–H) Residual panCrb protein signal was observed in the dorsal pancreas, which may be the result of expression of Crb proteins other than Crb2a and Crb2b in this region.

Consistent with prior studies (Pollard et al., 2006), lama1 morphants exhibited reduced body size and other gross anatomical defects at 78 hpf, whereas crb2a/b morphants appeared grossly normal. Both lama1 and crb2a/b morphants displayed an annular pancreas (15 out of 34 lama1 and 27 out of 69 crb2a/b morphants) characterized by pancreatic tissue partially or completely encircling the duodenum (Figure 6A–D), a phenotype indicative of impaired migration of pancreatic progenitors during pancreas formation. These findings suggest that both lama1 and crb2a/b control cell migratory processes during early pancreatic development and that reduced levels of lama1 or crb2a/b impair pancreas morphogenesis.

![Figure 6.](https://cdn.elifesciences.org/articles/59067/elife-59067-fig6-v1.jpg)

**Figure 6.:** (A,B) Representative 3D renderings of Tg(ptf1a:eGFP)jh1 control zebrafish embryos (A,A’) and lama1 morphants (B,B’) stained with DAPI (nuclei, blue) and antibody against insulin (red); n ≥ 15 embryos per condition. To account for reduced acinar pancreas size in lama1 morphants, control embryos were imaged at 50 hr post fertilization (hpf) and lama1 morphants at 78 hpf. 15 out of 34 lama1 morphants displayed an annular pancreas with two acinar pancreas domains (green) connected behind the presumptive intestine (B’, white arrow). Scale bar, 40 µM. (C,D) Representative 3D renderings of 78 hpf Tg(ptf1a:eGFP)jh1 control zebrafish embryos (C,C’) and crb2a/b morphants (D,D’) stained with DAPI (nuclei, blue) and antibodies against insulin (red); n ≥ 15 embryos per condition. Twenty-seven out of 69 crb2a/b morphants displayed an annular pancreas with the acinar pancreas (green) completely surrounding the presumptive intestine. Scale bar, 40 µM. (E) Representative 3D renderings of Tg(ptf1a:eGFP)jh1 control zebrafish embryos and crb2a/b, lama1, or crb2a/b + lama1 morphants stained with DAPI (nuclei, blue) and antibody against insulin (red). All embryos were imaged at 78 hpf except for controls to lama1 and crb2a/b + lama1 morphants, which were imaged at 50 hpf to account for reduced acinar pancreas size of lama1 morphants. Scale bar, 20 µM. (F) Quantification of beta (insulin+) cell nuclei per embryo from experiment in (E). p adj. = 4.0 × 10−3, 8.0 × 10−3, and 2.0 × 10−4 for comparison of hfp 78 control (n = 7 embryos) to hfp 78 crb2a/b (n = 8), hpf 50 control (n = 12) to hpf 78 lama1 (n = 10), or crb2a/b + lama1 (n = 12) morphants, respectively; ANOVA-Dunnett’s multiple comparison test; ***p<0.001 **p<0.01. 5 out of 8 crb2a/b, 3 out of 10 lama1, and 9 out of 12 crb2a/b + lama1 morphants displayed an annular pancreas. MO, morpholino; Control, standard control morpholino. See also Figure 6—figure supplements 1–4.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/59067/elife-59067-fig6-figsupp1-v1.jpg)

**Figure 6—figure supplement 1.:** (A,B) Confocal images of 36 hr post fertilization (hpf) Tg(ptf1a:eGFP)jh1 zebrafish foregut endoderm labeled with DAPI (nuclei, grey) and antibodies against Nkx6.1 (blue; pancreatic progenitors) and Laminin (A, red) or panCrb (B, red); n = 10 embryos stained. (A–A”’’) Z-focal plane image showing pancreatic progenitor cells marked by Nkx6.1 (blue) and low level ptf1a:eGFP, labeled with anti-Laminin antibodies (red). (B–B”’’) Pancreatic progenitors labeled with anti-panCrb antibodies (red). Scale bar, 20 µM.

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/59067/elife-59067-fig6-figsupp2-v1.jpg)

**Figure 6—figure supplement 2.:** Confocal images (3D rendered) of 32–34 hpf Tg(ptf1a:eGFP)jh1 zebrafish foregut endoderm labeled with DAPI (nuclei, grey) and anti-Laminin antibodies (red). (A–A’’) Z-focal plane image of pancreatic progenitors marked by ptf1a:eGFP (green) and labeled with anti-Laminin antibodies (red) from embryos injected with non-targeting standard control morpholinos (n = 6). (B–B’’) Z-focal plane image showing loss of Laminin staining (red) in pancreatic progenitors marked by ptf1a:eGFP (green) from embryos injected with morpholinos targeting lama1 (n = 5/6). (C,D) 3D renderings of 45 hpf Tg(ptf1a:eGFP)jh1 zebrafish foregut endoderm labeled with antibodies against Nkx6.1 (blue) and Laminin (red). (C–C’’) Z-focal plane image of pancreatic progenitors marked by ptf1a:eGFP (green) and labeled with anti-Nkx6.1 (blue) and anti-Laminin (red) antibodies from embryos injected with standard control morpholinos (n = 4/4). (D–D’’) Z-focal plane image showing loss of Laminin staining (red) in pancreatic progenitors marked by ptf1:eGFP and labeled with anti-Nkx6.1 antibodies (blue) from embryos injected with morpholinos targeting lama1 (n = 3/4). Scale bar, 20 µM. Arrows highlight pancreatic progenitors marked by Laminin (red), Nkx6.1 (blue) and ptf1a:eGFP. MO, morpholino.

![Figure 6—figure supplement 3.](https://cdn.elifesciences.org/articles/59067/elife-59067-fig6-figsupp3-v1.jpg)

**Figure 6—figure supplement 3.:** (A,B) 3D renderings of 32–34 hpf Tg(ptf1a:eGFP)jh1 zebrafish foregut endoderm labeled with DAPI (nuclei, grey) and anti-Crb2a antibodies (red). (A–A’’) Z-focal plane image showing Crb2a labeled (red) foregut endoderm from embryos injected with standard control morpholinos (n = 6). (B–B’’) Z-focal plane image showing loss of Crb2a staining (red) in the foregut endoderm from embryos injected with morpholinos targeting crb2a (n = 6/6). (C,D) 3D renderings of 45 hpf Tg(ptf1a:eGFP)jh1 zebrafish foregut endoderm labeled with DAPI (nuclei, grey) and anti-Crb2a antibodies (red). (C–C’) Z-focal plane image showing Crb2a-labeled (red) embryos injected with standard control morpholinos (n = 3). (D–D’) Z-focal plane image showing loss of Crb2a staining (red) in embryos injected with morpholinos targeting crb2a (n = 3/3).(E,F) 3D renderings of 32–34 hpf Tg(ptf1a:eGFP)jh1 zebrafish foregut endoderm labeled with DAPI (nuclei, grey) and anti-panCrb antibodies (red). (E–E’’) Z-focal plane image showing pancreatic progenitors marked by ptf1a:eGFP (green) and labeled with anti-panCrb antibodies (red; white arrows) from embryos injected with standard control morpholinos (n = 8). (F–F’’) Z-focal plane image showing reduced panCrb (red) staining in pancreatic progenitors marked by ptf1a:eGFP (green) from embryos injected with morpholinos targeting both crb2a and crb2b (n = 4/5). (G,H) 3D renderings of 45 hpf Tg(ptf1a:eGFP)jh1 zebrafish foregut endoderm labeled with anti-Nkx6.1 (blue) and anti-panCrb (red) antibodies. (G–G’’) Z-focal plane image showing pancreatic progenitors marked by ptf1a:eGFP (green) and labeled with anti-Nkx6.1 (blue) and anti-panCrb (red; white arrows) antibodies from embryos injected with standard control morpholinos (n = 4). (H–H’’) Z-focal plane image showing reduced panCrb (red) staining in pancreatic progenitors marked by ptf1a:eGFP and labeled with anti-Nkx6.1 antibodies (blue) from embryos injected with morpholinos targeting both crb2a and crb2b (n = 3/4). Yellow arrows denote dorsal pancreas where panCrb labeling remains in control injected embryos, possibly due to expression of alternate Crb proteins present within the dorsal pancreas. Scale bar, 20 µM. MO, morpholino.

![Figure 6—figure supplement 4.](https://cdn.elifesciences.org/articles/59067/elife-59067-fig6-figsupp4-v1.jpg)

**Figure 6—figure supplement 4.:** Quantification of beta (insulin+) cell nuclei per embryo in Tg(ptf1a:eGFP)jh1 control zebrafish embryos and crb2a or crb2b morphants at 78 hr post fertilization (hpf). p adj. = 0.91 and 4.4 × 10−2 for comparison of control (n = 7 embryos) to crb2a (n = 8) or crb2b (n = 8) morphants, respectively; ANOVA-Dunnett’s multiple comparison test; **p<0.01, n.s., not significant. 0 out of 8 crb2a, 0 out of 8 crb2b morphants displayed an annular pancreas. MO, morpholino; Control, standard control morpholino.

To gain insight into the effects of lama1 and crb2a/b knockdown on pancreatic endocrine cell development, we examined beta cell numbers (insulin+ cells) at 78 hpf. We also evaluated potential synergistic effects of combined lama1 and crb2a/b knockdown. To account for the reduction in body and pancreas size in lama1 morphants, we compared cell numbers in 78 hpf lama1 morphants with 50 hpf control embryos, which have a similarly sized acinar compartment as 78 hpf lama1 morphants. Beta cell numbers were significantly reduced in both lama1 and crb2a/b morphants (p=8.0 × 10−3 and 4.0 × 10−3 for comparisons of lama1 and crb2a/b morphants, respectively; Figure 6E,F), as well as in morphants with a combined knockdown of lama1 and crb2a/b (p=2.0 × 10−4; Figure 6F), showing that reduced lama1 and crb2a/b levels, both individually and in combination, impair beta cell development. Furthermore, we found that nearly all lama1, crb2a/b, and combined lama1 and crb2a/b morphants without an annular pancreas had reduced beta cell numbers, indicating independent roles of lama1 and crb2 in pancreas morphogenesis and beta cell differentiation. Finally, to investigate the contributions of individual crb2 genes to the observed phenotype, we performed knockdown experiments using morpholinos against crb2a and crb2b alone. Only crb2b morphants showed a significant reduction in beta cell numbers (p=4.4 × 10−2; Figure 6—figure supplement 4), suggesting that crb2b is the predominant crb2 gene required for beta cell development. Combined, these findings demonstrate that lama1 and crb2 are regulators of pancreas morphogenesis and beta cell development in vivo.

## Discussion

In this study, we identify T2D-associated variants localized within chromatin active in pancreatic progenitors but not islets or other T2D-relevant tissues, suggesting a novel mechanism whereby a subset of T2D risk variants specifically alters pancreatic developmental processes. We link T2D-associated enhancers active in pancreatic progenitors to the regulation of LAMA1 and CRB2 and demonstrate a functional requirement in zebrafish for lama1 and crb2 in pancreas morphogenesis and endocrine cell formation. Furthermore, we provide a curated list of T2D risk-associated enhancers and candidate effector genes for further exploration of how the regulation of developmental processes in the pancreas can predispose to T2D.

Our analysis identified 11 loci where T2D-associated variants mapped in SE specifically active in pancreatic progenitors. Among these loci was LAMA1, which has stronger effects on T2D risk in lean compared to obese individuals (Perry et al., 2012). We also found evidence that variants in PSSE collectively have stronger enrichment for T2D in lean individuals, although the small number of PSSE and limited sample size of the BMI-stratified T2D genetic data prohibits a more robust comparison. There was also a notable lack of enrichment among PSSE variants for association with traits related to insulin secretion and beta cell function. If T2D-associated variants in PSSE indeed confer diabetes susceptibility by affecting beta cell development, the question arises as to why variants associated with traits related to beta cell function are not enriched within PSSE. As genetic association studies of endophenotypes are based on data from non-diabetic subjects, a possible explanation is that variants affecting beta cell developmental processes have no overt phenotypic effect under physiological conditions and contribute to T2D pathogenesis only during the disease process.

Since the genomic position of enhancers and transcription factor binding sites is not well conserved between species (Villar et al., 2015), a human cell model is necessary to identify target genes of enhancers associated with disease risk. By employing enhancer deletion in hESCs, we demonstrate that T2D-associated PSSE at the LAMA1 and CRB2 loci regulate LAMA1 and CRB2, respectively, and establish LAMA1 and CRB2 as the predominant target gene of their corresponding PSSE within TAD boundaries. By analyzing LAMA1 and CRB2 expression throughout the pancreatic differentiation time course, we show that the identified PSSE control LAMA1 and CRB2 expression in a temporal manner consistent with the activation pattern of their associated PSSE. While the specific T2D-relevant target genes of the majority of T2D-associated PSSE remain to be identified, it is notable that several are localized within TADs containing genes encoding transcriptional regulators. These include PROX1 and GATA4, which are known to regulate pancreatic development (Shi et al., 2017; Tiyaboonchai et al., 2017; Westmoreland et al., 2012), as well as HMGA2 and BCL6 with unknown functions in the pancreas. Our catalogue of T2D-associated PSSE provides a resource to fully characterize the gene regulatory program associated with developmentally mediated T2D risk in the pancreas. Our finding that predicted target genes of PSSE are similarly expressed in hESC-derived pancreatic progenitors and primary human embryonic pancreas (Figure 3B and Figure 3—figure supplement 1A) further underscores the utility of the hESC-based system for these studies.

In the embryo, endocrine cells differentiate by delaminating from a polarized epithelium of progenitors governed by local cell-cell and cell-matrix signaling events (Mamidi et al., 2018). These processes are not well-recapitulated in the hESC-based pancreatic differentiation system, highlighting a limitation of this system for studying the function of Laminin and CRB2, which are mediators of mechanical signals within an epithelium. Therefore, we analyzed their function in zebrafish as an in vivo model. We show that lama1 or crb2 knockdown leads to an annular pancreas and reduced beta cell numbers. The beta cell differentiation defect was also evident in embryos not displaying an annular pancreas, suggesting independent mechanisms.

Consistent with our findings in lama1 morphants, culture of pancreatic progenitors on Laminin-based substrates promotes endocrine cell differentiation (Mamidi et al., 2018). During in vivo pancreatic development, endothelial cells are an important albeit not the only source of Laminin in the pancreas (Heymans et al., 2019; Mamidi et al., 2018; Nikolova et al., 2006). While we do not know the respective contributions of endothelial cell- and pancreatic progenitor cell-derived Laminin to the phenotype of lama1 morphants, the T2D-associated LAMA1 PSSE is not active in endothelial cells (Figure 3—figure supplement 1C). Furthermore, we found no other T2D-associated variants at the LAMA1 locus mapping in endothelial cell enhancers or accessible chromatin sites in islets, suggesting that T2D risk is linked to LAMA1 regulation in pancreatic progenitors.

Similar to Laminin, CRB2 has been shown to regulate mechanosignaling (Varelas et al., 2010). Our observation that pancreatic progenitor cells express Crb proteins is consistent with the phenotype of crb2 morphants reflecting a progenitor-autonomous role of Crb2. Furthermore, the similarity in pancreatic phenotype between lama1 or crb2 morphants raises the possibility that signals from Laminin and Crb2 could converge on the same intracellular pathways in pancreatic progenitors.

Our findings suggest that variation in gene regulation during pancreatic development can predispose to T2D later in life. Several lines of evidence support the concept of a developmental impact on T2D risk. First, human genetic studies have shown a strong correlation between birth weight and adult cardiometabolic traits and disease (Horikoshi et al., 2016). Second, epidemiological studies provide evidence that offspring of mothers who were pregnant during a famine have a higher prevalence of T2D (Lumey et al., 2015). This phenomenon has been experimentally reproduced in rodents, where maternal malnutrition has been shown to cause reduced beta cell mass at birth and to render beta cells more prone to failure under stress (Nielsen et al., 2014). Together, our results provide a strong rationale for further exploration of how genetic variants affecting developmental gene regulation in the pancreas contribute to T2D risk.

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
      <td>Antibody</td>
      <td>APC Mouse monoclonal IgG1, κ Isotype Control</td>
      <td>BD Pharmingen</td>
      <td>Cat# 555751, RRID:AB_398613</td>
      <td>Flow cytometry (1:100)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Chicken polyclonal anti-GFP</td>
      <td>Aves Labs</td>
      <td>Cat# GFP-1020, RRID:AB_10000240</td>
      <td>Immunohistochemistry (1:200)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Cy3-conjugated donkey polyclonal anti-mouse</td>
      <td>Jackson ImmunoResearch Labs</td>
      <td>Cat# 715-165-150, RRID:AB_2340813</td>
      <td>Immunofluorescence (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>DyLight 488-conjugated donkey polyconal anti-goat</td>
      <td>Jackson ImmunoResearch Labs</td>
      <td>Cat# 705-545-003, RRID:AB_2340428</td>
      <td>Immunofluorescence (1:500)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Goat polyclonal anti-CTCF</td>
      <td>Santa Cruz Biotechnology</td>
      <td>Cat# SC-15914X, RRID:AB_2086899</td>
      <td>ChIP-seq (4 ug)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Goat polyclonal anti-FOXA1</td>
      <td>Abcam</td>
      <td>Cat# ab5089, RRID:AB_304744</td>
      <td>ChIP-seq (4 ug)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Goat polyclonal anti-FOXA2</td>
      <td>Santa Cruz Biotechnology</td>
      <td>Cat# sc-6554, RRID:AB_2262810</td>
      <td>ChIP-seq (4 ug)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Goat polyclonal anti-GATA4</td>
      <td>Santa Cruz Biotechnology</td>
      <td>Cat# sc-1237, RRID:AB_2108747</td>
      <td>ChIP-seq (4 ug)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Goat polyclonal anti-PDX1</td>
      <td>Abcam</td>
      <td>Cat# ab47383, RRID:AB_2162359</td>
      <td>Immunofluorescence (1:500)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Guinea pig polyclonal anti-Insulin</td>
      <td>Biomeda</td>
      <td>Cat# v2024</td>
      <td>Immunohistochemistry (1:200)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse monoclonal anti-Crb2a</td>
      <td>ZIRC</td>
      <td>Cat# Zs-4</td>
      <td>Immunohistochemistry (1:100)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse polyclonal anti-GATA6</td>
      <td>Santa Cruz Biotechnology</td>
      <td>Cat# sc-9055, RRID:AB_2108768</td>
      <td>ChIP-seq (4 ug)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse monoclonal anti-NKX6.1</td>
      <td>Developmental Studies Hybridoma Bank</td>
      <td>Cat# F64A6B4, RRID:AB_532380</td>
      <td>Immunofluorescence (1:300)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse monoclonal anti-NKX6.1-Alexa Fluor 647</td>
      <td>BD Biosciences</td>
      <td>Cat# 563338, RRID:AB_2738144</td>
      <td>Flow cytometry (1:5)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse monoclonal anti-NKX6.1</td>
      <td>Developmental Studies Hybridoma Bank</td>
      <td>Cat# F55A10, RRID:AB_532378</td>
      <td>Immunohistochemistry (1:10)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse monoclonal anti-PDX1-PE</td>
      <td>BD Biosciences</td>
      <td>Cat# 562161, RRID:AB_10893589</td>
      <td>Flow cytometry (1:10)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>PE Mouse monoclonal IgG1, κ Isotype Control</td>
      <td>BD Pharmingen</td>
      <td>Cat# 555749, RRID:AB_396091</td>
      <td>Flow cytometry (1:100)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit polyclonal anti-CRB2</td>
      <td>Sigma</td>
      <td>Cat # SAB1301340</td>
      <td>Immunofluorescence (1:500)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit polyclonal anti-H3K27ac</td>
      <td>Active Motif</td>
      <td>Cat# 39133, RRID:AB_2561016</td>
      <td>ChIP-seq (4 ug)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit polyclonal anti-H3K4me1</td>
      <td>Abcam</td>
      <td>Cat# ab8895, RRID:AB_306847</td>
      <td>ChIP-seq (4 ug)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit polyclonal anti-HNF6</td>
      <td>Santa Cruz Biotechnology</td>
      <td>Cat# sc-13050, RRID:AB_2251852</td>
      <td>ChIP-seq (4 ug)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit polyclonal anti-laminin</td>
      <td>Sigma</td>
      <td>Cat# L9393, RRID:AB_477163</td>
      <td>Immunohistochemistry (1:100) Immunofluorescence (1:30)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit monoclonal anti-panCrb</td>
      <td>Jensen Laboratory, University of Massachusetts, Amherst</td>
      <td>N/A</td>
      <td>Immunohistochemistry (1:100)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit polyclonal anti-PDX1</td>
      <td>Beta Cell Biology Consortium</td>
      <td>AB1068</td>
      <td>ChIP-seq (4 ug)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit polyclonal anti-SOX9</td>
      <td>Chemicon</td>
      <td>Cat# 5535, RRID:AB_2239761</td>
      <td>ChIP-seq (4 ug)</td>
    </tr>
    <tr>
      <td>Cell line (Homo-sapiens)</td>
      <td>CyT49</td>
      <td>ViaCyte, Inc</td>
      <td>NIHhESC-10–0041, RRID:CVCL_B850</td>
      <td>Male</td>
    </tr>
    <tr>
      <td>Cell line (Homo-sapiens)</td>
      <td>H1</td>
      <td>WiCell Research Institute</td>
      <td>NIHhESC-10–0043, RRID:CVCL_9771</td>
      <td>Male</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>2-Mercaptoethanol</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat# 21985023</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Accutase</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat# 00-4555-56</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>B-27 supplement</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat# 17504044</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Bovine Albumin Fraction V</td>
      <td>Life Technologies</td>
      <td>Cat# 15260037</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>D-(+)-Glucose Solution, 45%</td>
      <td>Sigma-Aldrich</td>
      <td>Cat# G8769</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>DAPI</td>
      <td>Invitrogen</td>
      <td>Cat# D1306</td>
      <td>Immunohistochemistry (1:200)</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>DMEM High Glucose</td>
      <td>VWR</td>
      <td>Cat# 16750–082</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>DMEM/F12 [-] L-glutamine</td>
      <td>VWR</td>
      <td>Cat# 15–090-CV</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>DMEM/F12 with L-Glutamine, HEPES</td>
      <td>Corning</td>
      <td>Cat# 45000–350</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>DMF</td>
      <td>EMD Millipore</td>
      <td>Cat# DX1730</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>DPBS</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat# 21–031-CV</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>DTT</td>
      <td>Sigma</td>
      <td>Cat# D9779</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Fetal Bovine Serum</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat# MT35011CV</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Glutamax</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat# 35050–079</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>GlutaMAX</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat# 35050061</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Hoechst 33342</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat# H3570</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>HyClone Dulbecco’s Modified Eagles Medium</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat# SH30081.FS</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>IGEPAL-CA630</td>
      <td>Sigma</td>
      <td>Cat# I8896</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Illumina tagmentation enzyme</td>
      <td>Illumina</td>
      <td>Cat# FC-121–1030</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Insulin-Transferrin-Selenium (ITS)</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat# 41400045</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Insulin-Transferrin-Selenium-Ethanolamine (ITS-X)</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat# 51500–056</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>KAAD-Cyclopamine</td>
      <td>Toronto Research Chemicals</td>
      <td>Cat# K171000</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>K-acetate</td>
      <td>Sigma</td>
      <td>Cat# P5708</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>KnockOut SR XenoFree</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat# A1099202</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>LDN-193189</td>
      <td>Stemgent</td>
      <td>Cat# 04–0074</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Matrigel</td>
      <td>Corning</td>
      <td>Cat# 356231</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>MCDB 131</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat# 10372–019</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Mg-acetate</td>
      <td>Sigma</td>
      <td>Cat# M2545</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>mTeSR1 Complete Kit - GMP</td>
      <td>STEMCELL Technologies</td>
      <td>Cat# 85850</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>NEBNext High-Fidelity 2X PCR Master Mix</td>
      <td>NEB</td>
      <td>Cat# M0541</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Non-Essential Amino Acids</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat# 11140050</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>O.C.T. Compound</td>
      <td>Sakura Finetek USA</td>
      <td>Cat# 25608–930</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Penicillin-Streptomycin</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat# 15140122</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Polyethylenimine (PEI)</td>
      <td>Polysciences</td>
      <td>Cat# 23966–1</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Protease inhibitor</td>
      <td>Roche</td>
      <td>Cat# 05056489001</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Retinoic acid</td>
      <td>Sigma-Aldrich</td>
      <td>Cat# R2625</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>RNA ScreenTape Sample Buffer</td>
      <td>Agilent Technologies</td>
      <td>Cat# 5067–5577</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>ROCK Inhibitor Y-27632</td>
      <td>STEMCELL Technologies</td>
      <td>Cat# 72305</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>RPMI 1640 [-] L-glutamine</td>
      <td>VWR</td>
      <td>Cat# 15–040-CV</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>SANT-1</td>
      <td>Sigma-Aldrich</td>
      <td>Cat# S4572</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Sodium Bicarbonate</td>
      <td>Sigma-Aldrich</td>
      <td>Cat# NC0564699</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Tamoxifen</td>
      <td>Sigma</td>
      <td>Cat# T5648</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>TGF-β RI Kinase Inhibitor IV</td>
      <td>Calbiochem</td>
      <td>Cat# 616454</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>TPB</td>
      <td>Calbiochem</td>
      <td>Cat# 565740</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Tranylcypromine</td>
      <td>Cayman Chemical</td>
      <td>Cat# 10010494</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Tris-acetate</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat# BP-152</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>TTNPB</td>
      <td>Enzo Life Sciences</td>
      <td>Cat# BML-GR105</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Vectashield Antifade Mounting Medium</td>
      <td>Vector Laboratories</td>
      <td>Cat# H-1000</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>XtremeGene 9</td>
      <td>Roche</td>
      <td>Cat# 6365787001</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay</td>
      <td>High Sensitivity D1000 ScreenTape</td>
      <td>Agilent Technologies</td>
      <td>Cat# 5067–5584</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>RNA ScreenTape</td>
      <td>Agilent Technologies</td>
      <td>Cat# 5067–5576</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>RNA ScreenTape Ladder</td>
      <td>Agilent Technologies</td>
      <td>Cat# 5067–5578</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>BD Cytofix/Cytoperm Plus Fixation/Permeabilization Solution Kit</td>
      <td>BD Biosciences</td>
      <td>Cat# 554715</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>ChIP-IT High Sensitivity Kit</td>
      <td>Active Motif</td>
      <td>Cat# 53040</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>iQ SYBR Green Supermix</td>
      <td>Bio-Rad</td>
      <td>Cat# 1708884</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>iScript cDNA Synthesis Kit</td>
      <td>Bio-Rad</td>
      <td>Cat# 1708891</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>KAPA Library Preparation Kit (Illumina)</td>
      <td>Kapa Biosystems</td>
      <td>Cat# KK8234</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>KAPA Stranded mRNA-Seq Kits</td>
      <td>Kapa Biosystems</td>
      <td>Cat# KK8401</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>MinElute PCR purification kit</td>
      <td>QIAGEN</td>
      <td>Cat# 28004</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>Qubit ssDNA assay kit</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat# Q10212</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>RNeasy Micro Kit</td>
      <td>QIAGEN</td>
      <td>Cat# 74004</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. rerio)</td>
      <td>Tg(ptf1a:eGFP)jh1</td>
      <td>PMID:16258076</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>SPRIselect bead</td>
      <td>Beckman Coulter</td>
      <td>Cat# B23317</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant protein</td>
      <td>Activin A</td>
      <td>R and D Systems</td>
      <td>Cat# 338-AC/CF</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant protein</td>
      <td>Human AB Serum</td>
      <td>Valley Biomedical</td>
      <td>Cat# HP1022</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant protein</td>
      <td>Recombinant EGF</td>
      <td>R and D Systems</td>
      <td>Cat# 236-EG</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant protein</td>
      <td>Recombinant Heregulinβ−1</td>
      <td>Peprotech</td>
      <td>Cat# 100–03</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant protein</td>
      <td>Recombinant KGF/FGF7</td>
      <td>R and D Systems</td>
      <td>Cat# 251 KG</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant protein</td>
      <td>Recombinant Mouse Wnt3A</td>
      <td>R and D Systems</td>
      <td>Cat# 1324-WN/CF</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant protein</td>
      <td>Recombinant Noggin</td>
      <td>R and D Systems</td>
      <td>Cat# 3344 NG</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Px333 Plasmid</td>
      <td>http://www.addgene.org/64073/</td>
      <td>RRID:Addgene_64073</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>LAMA1 Forward</td>
      <td>This paper</td>
      <td>qPCR primers</td>
      <td>GTG ATG GCA ACA GCG CAA A</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>LAMA1 Reverse</td>
      <td>This paper</td>
      <td>qPCR primers</td>
      <td>GAC CCA GTG ATA TTC TCT CCC A</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>CRB2 Forward</td>
      <td>This paper</td>
      <td>qPCR primers</td>
      <td>ACC ACT GTG CTT GTC CTG AG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>CRB2 Reverse</td>
      <td>This paper</td>
      <td>qPCR primers</td>
      <td>TCC AGG GTC GCT AGA TGG AG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>TBP Forward</td>
      <td>This paper</td>
      <td>qPCR primers</td>
      <td>TGT GCA CAG GAG CCA AGA GT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>TBP Reverse</td>
      <td>This paper</td>
      <td>qPCR primers</td>
      <td>ATT TTC TTG CTG CCA GTC TGG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>LAMA1Enh Upstream Guide</td>
      <td>This paper</td>
      <td>CRISPR sgRNA</td>
      <td>GTC AAA TTG CTA TAA CAC GG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>LAMA1Enh Downstream Guide</td>
      <td>This paper</td>
      <td>CRISPR sgRNA</td>
      <td>CCA CTT TAA GTA TCT CAG CA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>CRB2Enh Upstream Guide</td>
      <td>This paper</td>
      <td>CRISPR sgRNA</td>
      <td>ATA CAA AGC ACG TGA GA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>CRB2Enh Downstream Guide</td>
      <td>This paper</td>
      <td>CRISPR sgRNA</td>
      <td>GAA TGC GGA TGA CGC CTG AG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>lama1-ATG</td>
      <td>PMID:16321372</td>
      <td>Morpholino</td>
      <td>TCA TCC TCA TCT CCA TCA TCG CTC A Obtained from GeneTools, LLC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>crb2a-SP</td>
      <td>PMID:16713951</td>
      <td>Morpholino</td>
      <td>ACG TTG CCA GTA CCT GTG TAT CCT G Obtained from GeneTools, LLC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>crb2b-SP</td>
      <td>PMID:16713951</td>
      <td>Morpholino</td>
      <td>TAA AGA TGT CCT ACC CAG CTT GAA C Obtained from GeneTools, LLC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>standard control MO</td>
      <td>N/A</td>
      <td>Morpholino</td>
      <td>CCT CTT ACC TCA GTT ACA ATT TAT A Obtained from GeneTools, LLC</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Adobe Illustrator v 5.1</td>
      <td>http://www.adobe.com/products/illustrator.html</td>
      <td>RRID:SCR_014198</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Adobe Photoshop v 5.1</td>
      <td>http://www.adobe.com/products/photoshop.html</td>
      <td>RRID:SCR_014199</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>BEDtools v 2.26.0</td>
      <td>https://github.com/arq5x/bedtools2</td>
      <td>RRID:SCR_006646</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Bioconductor</td>
      <td>https://www.bioconductor.org/</td>
      <td>RRID: SCR_006442</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Burrows-Wheeler Aligner v 0.7.13</td>
      <td>http://bio-bwa.sourceforge.net/</td>
      <td>RRID:SCR_010910</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>CENTIPEDE v 1.2</td>
      <td>http://centipede.uchicago.edu/</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Cufflinks v 2.2.1</td>
      <td>http://cole-trapnell-lab.github.io/cufflinks/</td>
      <td>RRID:SCR_014597</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>deepTools2 v 3.1.3</td>
      <td>https://deeptools.readthedocs.io/en/develop/content/installation.html</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>DESeq2 v 3.10</td>
      <td>https://bioconductor.org/packages/release/bioc/html/DESeq2.html</td>
      <td>RRID:SCR_015687</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>FlowJo v10 software</td>
      <td>https://www.flowjo.com/solutions/flowjo</td>
      <td>RRID: SCR_008520</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>GraphPad Prism v 8.1.2</td>
      <td>https://www.graphpad.com/scientific-software/prism/</td>
      <td>RRID: SCR_002798</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>HOMER v 4.10.4</td>
      <td>http://homer.ucsd.edu/homer/</td>
      <td>RRID: SCR_010881</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Juicebox Tools v 1.4</td>
      <td>https://github.com/aidenlab/Juicebox/wiki/Juicebox-Assembly-Tools</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MACS2 v 2.1.4</td>
      <td>http://liulab.dfci.harvard.edu/MACS/</td>
      <td>RRID:SCR_013291</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MEME suite v 5.1.1</td>
      <td>http://meme-suite.org/</td>
      <td>RRID:SCR_001783</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Metascape</td>
      <td>http://metscape.ncibi.org</td>
      <td>RRID:SCR_014687</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Picard Tools v 1.131</td>
      <td>http://broadinstitute.github.io/picard/</td>
      <td>RRID:SCR_006525</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>R Project for Statistical Computing v 3.6.1</td>
      <td>http://www.r-project.org/</td>
      <td>RRID:SCR_001905</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>SAMtools v 1.5</td>
      <td>http://samtools.sourceforge.net</td>
      <td>RRID:SCR_002105</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>STAR v 2.4</td>
      <td>https://github.com/alexdobin/STAR</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>UCSC Genome Browser</td>
      <td>http://genome.ucsc.edu/</td>
      <td>RRID:SCR_005780</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>vcf2diploid v 0.2.6a</td>
      <td>https://github.com/abyzovlab/vcf2diploid</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>ZEISS ZEN Digital Imaging for Light Microscopy</td>
      <td>http://www.zeiss.com/microscopy/en_us/products/microscope-software/zen.html#introduction</td>
      <td>RRID:SCR_013672</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Maintenance and differentiation of CyT49 hESCs

Genomic and gene expression analyses (ChIP-seq, ATAC-seq, RNA-seq) for generation of chromatin maps and target gene identification were performed in CyT49 hESCs (male). Propagation of CyT49 hESCs was carried out by passing cells every 3 to 4 days using Accutase (eBioscience) for enzymatic cell dissociation, and with 10% (v/v) human AB serum (Valley Biomedical) included in the hESC media the day of passage. hESCs were seeded into tissue culture flasks at a density of 50,000 cells/cm2. hESC research was approved by the University of California, San Diego, Institutional Review Board and Embryonic Stem Cell Research oversight committee.

Pancreatic differentiation was performed as previously described (Schulz et al., 2012; Wang et al., 2015; Xie et al., 2013). Briefly, a suspension-based culture format was used to differentiate cells in aggregate form. Undifferentiated aggregates of hESCs were formed by re-suspending dissociated cells in hESC maintenance medium at a concentration of 1 × 106 cells/mL and plating 5.5 mL per well of the cell suspension in 6-well ultra-low attachment plates (Costar). The cells were cultured overnight on an orbital rotator (Innova2000, New Brunswick Scientific) at 95 rpm. After 24 hr the undifferentiated aggregates were washed once with RPMI medium and supplied with 5.5 mL of day 0 differentiation medium. Thereafter, cells were supplied with the fresh medium for the appropriate day of differentiation (see below). Cells were continually rotated at 95 rpm, or 105 rpm on days 4 through 8, and no media change was performed on day 10. Both RPMI (Mediatech) and DMEM High Glucose (HyClone) medium were supplemented with 1X GlutaMAX and 1% penicillin/streptomycin. Human activin A, mouse Wnt3a, human KGF, human noggin, and human EGF were purchased from R and D systems. Other added components included FBS (HyClone), B-27 supplement (Life Technologies), Insulin-Transferrin-Selenium (ITS; Life Technologies), TGFβ R1 kinase inhibitor IV (EMD Bioscience), KAAD-Cyclopamine (KC; Toronto Research Chemicals), and the retinoic receptor agonist TTNPB (RA; Sigma Aldrich). Day-specific differentiation media formulations were as follows:

Cells at D0 correspond to the embryonic stem cell (ES) stage, cells at D2 correspond to the definitive endoderm (DE) stage, cells at D5 correspond to the gut tube (GT) stage, cells at D7 correspond to the early pancreatic progenitor (PP1) stage, and cells at D10 correspond to the late pancreatic progenitor (PP2) stage.

### Maintenance and differentiation of H1 hESCs

∆LAMA1Enh and ∆CRB2Enh clonal lines were derived by targeting H1 hESCs (male). Cells were maintained and differentiated as described with some modifications (Jin et al., 2019; Rezania et al., 2014). In brief, hESCs were cultured in mTeSR1 media (Stem Cell Technologies) and propagated by passaging cells every 3–4 days using Accutase (eBioscience) for enzymatic cell dissociation. hESC research was approved by the University of California, San Diego, Institutional Review Board and Embryonic Stem Cell Research Oversight Committee.

For differentiation, cells were dissociated using Accutase for 10 min, then reaggregated by plating the cells at a concentration of ~5.5 e6 cells/well in a low attachment six-well plate on an orbital shaker (100 rpm) in a 37°C incubator. The following day, undifferentiated cells were washed in base media (see below) and then differentiated using a multi-step protocol with stage-specific media and daily media changes.

All stage-specific base media were comprised of MCDB 131 medium (Thermo Fisher Scientific) supplemented with NaHCO3, GlutaMAX, D-Glucose, and BSA using the following concentrations:

Media compositions for each stage were as follows:

Cells at D0 correspond to the embryonic stem cell (ES) stage, cells at D3 correspond to the definitive endoderm (DE) stage, cells at D6 correspond to the gut tube (GT) stage, cells at D8 correspond to the early pancreatic progenitor (PP1) stage, and cells at D11 correspond to the late pancreatic progenitor (PP2) stage.

### Generation of ∆LAMA1Enh, ∆CRB2Enh, ∆LAMA1, and ∆CRB2 hESC lines

To generate clonal homozygous LAMA1Enh and CRB2Enh deletion hESC lines, sgRNAs targeting each relevant enhancer were designed and cloned into Px333-GFP, a modified version of Px333 (Addgene, #64073). To generate clonal homozygous LAMA1 and CRB2 deletion hESC lines, sgRNAs targeting the second exon of each gene were designed and cloned into Px458 (Addgene, #48138). Plasmids expressing the sgRNAs were transfected into H1 hESCs with XtremeGene 9 (Roche). Twenty-four hr later, 8000 GFP+ cells were sorted into a well of six-well plate. Individual colonies that emerged within 5–7 days after transfection were subsequently transferred manually into 48-well plates for expansion, genomic DNA extraction, PCR genotyping, and Sanger sequencing. sgRNA oligos are listed below.

### Human tissue

Human embryonic pancreas tissue was obtained from the Birth Defects Research Laboratory of the University of Washington. Studies for use of embryonic human tissue were approved by the Institutional Review Board of the University of California, San Diego. A pancreas from a 54- and 58-day gestation embryo each were pooled for RNA-seq analysis.

### Zebrafish husbandry

Adult zebrafish and embryos were cared for and maintained under standard conditions. All research activity involving zebrafish was reviewed and approved by SBP Medical Discovery Institute Institutional Animal Care and Use Committee. The following transgenic lines were used: Tg(ptf1a:eGFP)jh1 (Godinho et al., 2005).

### Morpholino injections in zebrafish

The following previously validated morpholinos were injected into the yolk at the one-cell stage in a final volume of either 0.5 or 1 nl: 0.75 ng lama1-ATG (5’- TCATCCT CATCTCCATCATCGCTCA −3’); 3 ng crb2a-SP, (5’-ACGTTGCCAGTACCTGTGTATCCTG-3’) (Omori and Malicki, 2006; Watanabe et al., 2010); 3 ng crb2b-SP, (5’-TAAAGATGTCCTACCCAGCTTGAAC-3’) (Omori and Malicki, 2006); 6.75 ng standard control MO (5’- CCTCTTACCTCAGTTACAATTTATA −3’). All morpholinos were obtained from GeneTools, LLC.

### Chromatin immunoprecipitation sequencing (ChIP-seq)

ChIP-seq was performed using the ChIP-IT High-Sensitivity kit (Active Motif) according to the manufacturer’s instructions. Briefly, for each cell stage and condition analyzed, 5–10 × 106 cells were harvested and fixed for 15 min in an 11.1% formaldehyde solution. Cells were lysed and homogenized using a Dounce homogenizer and the lysate was sonicated in a Bioruptor Plus (Diagenode), on high for 3 × 5 min (30 s on, 30 s off). Between 10 and 30 µg of the resulting sheared chromatin was used for each immunoprecipitation. Equal quantities of sheared chromatin from each sample were used for immunoprecipitations carried out at the same time. A total of 4 µg of antibody were used for each ChIP-seq assay. Chromatin was incubated with primary antibodies overnight at 4°C on a rotator followed by incubation with Protein G agarose beads for 3 hr at 4°C on a rotator. Antibodies used were rabbit anti-H3K27ac (Active Motif 39133), rabbit anti-H3K4me1 (Abcam ab8895), rabbit anti-H3K4me3 (Millipore 04–745), rabbit anti-H3K27me3 (Millipore 07–499), goat anti-CTCF (Santa Cruz Biotechnology SC-15914X), goat anti-GATA4 (Santa Cruz SC-1237), rabbit anti-GATA6 (Santa Cruz SC-9055), goat anti-FOXA1 (Abcam Ab5089), goat-anti-FOXA2 (Santa Cruz SC-6554), rabbit anti-PDX1 (BCBC AB1068), rabbit anti-HNF6 (Santa Cruz SC-13050), and rabbit anti-SOX9 (Chemicon AB5535). Reversal of crosslinks and DNA purification were performed according to the ChIP-IT High-Sensitivity instructions, with the modification of incubation at 65°C for 2–3 hr, rather than at 80°C for 2 hr. Sequencing libraries were constructed using KAPA DNA Library Preparation Kits for Illumina (Kapa Biosystems) and library sequencing was performed on either a HiSeq 4000 System (Illumina) or NovaSeq 6000 System (Illumina) with single-end reads of either 50 or 75 base pairs (bp). Sequencing was performed by the Institute for Genomic Medicine (IGM) core research facility at the University of California at San Diego (UCSD). Two replicates from independent hESC differentiations were generated for each ChIP-seq experiment.

### ChIP-seq data analysis

ChIP-seq reads were mapped to the human genome consensus build (hg19/GRCh37) and visualized using the UCSC Genome Browser (Kent et al., 2002). Burrows-Wheeler Aligner (BWA) (Li and Durbin, 2009) version 0.7.13 was used to map data to the genome. Unmapped and low-quality (q < 15) reads were discarded. SAMtools (Li et al., 2009) was used to remove duplicate sequences and HOMER (Heinz et al., 2010) was used to call peaks using default parameters and to generate tag density plots. Stage- and condition-matched input DNA controls were used as background when calling peaks. The BEDtools suite of programs (Quinlan and Hall, 2010) was used to perform genomic algebra operations. For all ChIP-seq experiments, replicates from two independent hESC differentiations were generated. Tag directories were created for each replicate using HOMER. Directories from each replicate were then combined, and peaks were called from the combined replicates. For histone modifications and CTCF peaks, pearson correlations between each pair of replicates were calculated over the called peaks using the command multiBamSummary from the deepTools2 package (Ramírez et al., 2016). For pancreatic lineage-determining transcription factors (GATA4, GATA6, FOXA1, FOXA2, HNF6, PDX1, SOX9), correlations were calculated for peaks overlapping PSSE. Calculated Pearson correlations are as follow:

<table>
  <thead>
    <tr>
      <th></th>
      <th>H3K4me1</th>
      <th>H3K27ac</th>
      <th>CTCF</th>
      <th>H3K4me3</th>
      <th>H3K27me3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ES</td>
      <td>0.90</td>
      <td>0.91</td>
      <td>0.87</td>
      <td>0.81</td>
      <td>1.00</td>
    </tr>
    <tr>
      <td>DE</td>
      <td>0.97</td>
      <td>0.84</td>
      <td>0.86</td>
      <td>0.99</td>
      <td>0.99</td>
    </tr>
    <tr>
      <td>GT</td>
      <td>0.97</td>
      <td>0.87</td>
      <td>0.89</td>
      <td>0.97</td>
      <td>0.99</td>
    </tr>
    <tr>
      <td>PP1</td>
      <td>0.97</td>
      <td>0.85</td>
      <td>0.89</td>
      <td>0.96</td>
      <td>0.99</td>
    </tr>
    <tr>
      <td>PP2</td>
      <td>0.98</td>
      <td>0.87</td>
      <td>0.87</td>
      <td>0.97</td>
      <td>1.00</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th></th>
      <th>GATA4</th>
      <th>GATA6</th>
      <th>FOXA1</th>
      <th>FOXA2</th>
      <th>HNF6</th>
      <th>PDX1</th>
      <th>SOX9</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>PP2</td>
      <td>0.86</td>
      <td>0.82</td>
      <td>0.87</td>
      <td>0.80</td>
      <td>0.95</td>
      <td>0.64</td>
      <td>0.86</td>
    </tr>
  </tbody>
</table>

### RNA isolation and sequencing (RNA-seq) and qRT-PCR

RNA was isolated from cell samples using the RNeasy Micro Kit (Qiagen) according to the manufacturer instructions. For each cell stage and condition analyzed between 0.1 and 1 × 106 cells were collected for RNA extraction. For qRT-PCR, cDNA synthesis was first performed using the iScript cDNA Synthesis Kit (Bio-Rad) and 500 ng of isolated RNA per reaction. qRT-PCR reactions were performed in triplicate with 10 ng of template cDNA per reaction using a CFX96 Real-Time PCR Detection System and the iQ SYBR Green Supermix (Bio-Rad). PCR of the TATA binding protein (TBP) coding sequence was used as an internal control and relative expression was quantified via double delta CT analysis. For RNA-seq, stranded, single-end sequencing libraries were constructed from isolated RNA using the TruSeq Stranded mRNA Library Prep Kit (Illumina) and library sequencing was performed on either a HiSeq 4000 System (Illumina) or NovaSeq 6000 System (Illumina) with single-end reads of either 50 or 75 base pairs (bp). Sequencing was performed by the Institute for Genomic Medicine (IGM) core research facility at the University of California at San Diego. A complete list of RT-qPCR primer sequences can be found below.

<table>
  <thead>
    <tr>
      <th>LAMA1 forward</th>
      <th>GTG ATG GCA ACA GCG CAA A</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>LAMA1 reverse</td>
      <td>GAC CCA GTG ATA TTC TCT CCC A</td>
    </tr>
    <tr>
      <td>CRB2 forward</td>
      <td>ACC ACT GTG CTT GTC CTG AG</td>
    </tr>
    <tr>
      <td>CRB2 reverse</td>
      <td>TCC AGG GTC GCT AGA TGG AG</td>
    </tr>
    <tr>
      <td>PDX1 forward</td>
      <td>AAG TCT ACC AAA GCT CAC GCG</td>
    </tr>
    <tr>
      <td>PDX1 reverse</td>
      <td>GTA GGC GCC GCC TGC</td>
    </tr>
    <tr>
      <td>NKX6.1 forward</td>
      <td>CTG GCC TGT ACC CCT CAT CA</td>
    </tr>
    <tr>
      <td>NKX6.1 reverse</td>
      <td>CTT CCC GTC TTT GTC CAA CA</td>
    </tr>
    <tr>
      <td>PROX1 forward</td>
      <td>AAC ATG CAC TAC AAT AAA GCA AAT GAC</td>
    </tr>
    <tr>
      <td>PROX1 reverse</td>
      <td>CAG GAA TCT CTC TGG AAC CTC AAA</td>
    </tr>
    <tr>
      <td>PTF1A forward</td>
      <td>GAA GGT CAT CAT CTG CCA TC</td>
    </tr>
    <tr>
      <td>PTF1A reverse</td>
      <td>GGC CAT AAT CAG GGT CGC T</td>
    </tr>
    <tr>
      <td>SOX9 forward</td>
      <td>AGT ACC CGC ACT TGC ACA AC</td>
    </tr>
    <tr>
      <td>SOX9 reverse</td>
      <td>ACT TGT AAT CCG GGT GGT CCT T</td>
    </tr>
    <tr>
      <td>TBP forward</td>
      <td>TGT GCA CAG GAG CCA AGA GT</td>
    </tr>
    <tr>
      <td>TBP reverse</td>
      <td>ATT TTC TTG CTG CCA GTC TGG</td>
    </tr>
  </tbody>
</table>

### RNA-seq data analysis

Reads were mapped to the human genome consensus build (hg19/GRCh37) using the Spliced Transcripts Alignment to a Reference (STAR) aligner v2.4 (Dobin et al., 2013). Normalized gene expression (fragments per kilobase per million mapped reads; FPKM) for each sequence file was determined using Cufflinks v2.2.1 (Trapnell et al., 2010) with the parameters: --library-type fr-firststrand --max-bundle-frags 10000000. For all RNA-Seq experiments, replicates from two independent hESC differentiations were generated. Pearson correlations between bam files corresponding to each pair of replicates were calculated, and are as follow:

<table>
  <thead>
    <tr>
      <th>∆LAMA1Enh clone 1 PP2</th>
      <th>1.00</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>∆LAMA1Enh clone 2 PP2</td>
      <td>0.99</td>
    </tr>
    <tr>
      <td>∆CRB2Enh clone 1 PP2</td>
      <td>0.98</td>
    </tr>
    <tr>
      <td>∆CRB2Enh clone 2 PP2</td>
      <td>0.90</td>
    </tr>
    <tr>
      <td>∆LAMA1Enh control PP2</td>
      <td>0.92</td>
    </tr>
    <tr>
      <td>∆CRB2Enh control PP2</td>
      <td>0.99</td>
    </tr>
  </tbody>
</table>

### Assay for transposase accessible chromatin sequencing (ATAC-seq)

ATAC-seq (Buenrostro et al., 2013) was performed on approximately 50,000 nuclei. The samples were permeabilized in cold permeabilization buffer 0.2% IGEPAL-CA630 (I8896, Sigma), 1 mM DTT (D9779, Sigma), Protease inhibitor (05056489001, Roche), 5% BSA (A7906, Sigma) in PBS (10010–23, Thermo Fisher Scientific) for 10 min on the rotator in the cold room and centrifuged for 5 min at 500 × g at 4°C. The pellet was resuspended in cold tagmentation buffer (33 mM Tris-acetate (pH = 7.8) (BP-152, Thermo Fisher Scientific), 66 mM K-acetate (P5708, Sigma), 11 mM Mg-acetate (M2545, Sigma), 16% DMF (DX1730, EMD Millipore) in Molecular biology water (46000 CM, Corning)) and incubated with tagmentation enzyme (FC-121–1030; Illumina) at 37°C for 30 min with shaking at 500 rpm. The tagmented DNA was purified using MinElute PCR purification kit (28004, QIAGEN). Libraries were amplified using NEBNext High-Fidelity 2X PCR Master Mix (M0541, NEB) with primer extension at 72°C for 5 min, denaturation at 98°C for 30 s, followed by 8 cycles of denaturation at 98°C for 10 s, annealing at 63°C for 30 s and extension at 72°C for 60 s. After the purification of amplified libraries using MinElute PCR purification kit (28004, QIAGEN), double size selection was performed using SPRIselect bead (B23317, Beckman Coulter) with 0.55X beads and 1.5X to sample volume. Finally, libraries were sequenced on HiSeq4000 (Paired-end 50 cycles, Illumina).

### ATAC-seq data analysis

ATAC-seq reads were mapped to the human genome (hg19/GRCh37) using Burrows-Wheeler Aligner (BWA) version 0.7.13 (Li and Durbin, 2009), and visualized using the UCSC Genome Browser (Kent et al., 2002). SAMtools (Li et al., 2009) was used to remove unmapped, low-quality (q < 15), and duplicate reads. MACS2 (Zhang et al., 2008) was used to call peaks, with parameters ‘shift set to 100 bps, smoothing window of 200 bps’ and with ‘nolambda’ and ‘nomodel’ flags on. MACS2 was also used to call ATAC-Seq summits, using the same parameters combined with the ‘call-summits’ flag.

For all ATAC-Seq experiments, replicates from two independent hESC differentiations were generated. Bam files for each pair of replicates were merged for downstream analysis using SAMtools, and Pearson correlations between bam files for each individual replicate were calculated over a set of peaks called from the merged bam file. Correlations were performed using the command multiBamSummary from the deepTools2 package (Ramírez et al., 2016) with the ‘—removeOutliers’ flag and are as follow:

<table>
  <thead>
    <tr>
      <th>ES</th>
      <th>0.95</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>DE</td>
      <td>0.83</td>
    </tr>
    <tr>
      <td>GT</td>
      <td>1.00</td>
    </tr>
    <tr>
      <td>PP1</td>
      <td>1.00</td>
    </tr>
    <tr>
      <td>PP2</td>
      <td>1.00</td>
    </tr>
  </tbody>
</table>

For downstream analysis, ATAC-seq peaks were merged from two independent differentiations for ES, DE, GT, PP1, and PP2 stage cells and from four donors for primary islets. Primary islet ATAC-seq data was obtained from previously published datasets (Greenwald et al., 2019).

### Hi-C data analysis

Hi-C data were processed as previously described with some modifications (Dixon et al., 2015). Read pairs were aligned to the hg19 reference genome separately using BWA-MEM with default parameters (Li and Durbin, 2009). Specifically, chimeric reads were processed to keep only the 5’ position and reads with low mapping quality (<10) were filtered out. Read pairs were then paired using custom scripts. Picard tools were then used to remove PCR duplicates. Bam files with alignments were further processed into text format as required by Juicebox tools (Durand et al., 2016). Juicebox tools were then applied to generate hic files containing normalized contact matrices. All downstream analysis was based on 10 Kb resolution KR normalized matrices.

Chromatin loops were identified by comparing each pixel with its local background, as described previously (Rao et al., 2014) with some modifications. Specifically, only the donut region around the pixel was compared to model the expected count. Briefly, the KR-normalized contact matrices at 10 Kb resolution were used as input for loop calling. For each pixel, distance-corrected contact frequencies were calculated for each surrounding bin and the average of all surrounding bins. The expected counts were then transformed to raw counts by multiplying the counts with the raw-to-KR normalization factor. The probability of observing raw expected counts was calculated using Poisson distribution. All pixels with p-value<0.01 and distance less than 10 Kb were selected as candidate pixels. Candidate pixels were then filtered to remove pixels without any neighboring candidate pixels since they were likely false positives. Finally, pixels within 20 Kb of each other were collapsed and only the most significant pixel was selected. The collapsed pixels with p-value<1e-5 were used as the final list of chromatin loops.

A full set of scripts used for processing Hi-C data (Qui, 2021) is available at https://github.com/MSanderlab/Pancreatic-progenitor-epigenome-maps-prioritize-type-2-diabetes-risk-genes-with-roles-in-development/tree/master (copy archived at swh:1:rev:ba79c687523c2696ea0ef30d8476e28a0d860f18).

### Definition of chromatin states

We collected or generated H3K4me1, H3K27ac, H3K4me1, H3K4me3, H3K27me3, and CTCF ChIP-seq data at each developmental stage and in mature islets. Data corresponding to mature islets was downloaded from previously published studies (Bhandare et al., 2010; Parker et al., 2013; Pasquali et al., 2014). Sequence reads were mapped to the human genome hg19 using bwa (version 0.7.12) (Li and Durbin, 2009), and low quality and duplicate reads were filtered using samtools (version 1.3) (Li et al., 2009). Using these reads, we then called chromatin states jointly across all data using chromHMM (version 1.12) (Ernst and Kellis, 2012) and used a 10-state model and 200 bp bin size, as models with larger state numbers did not empirically resolve any additional informative states. We then assigned state names based on patterns defined by the NIH Epigenome Roadmap (Kundaje et al., 2015), which included active promoter/TssA (high H3K4me3, high H3K27ac), flanking TSS/TssFlnk1 (high H3K4me3), flanking TSS/TssFlnk 2 (high H3K4me3, high H3K27ac, high H3K4me1), bivalent Tss/TssBiv (high H3K27me3, high H3K4me3), poised enhancer/EnhP (high H3K4me1), insulator/CTCF (high CTCF), active enhancer/EnhA (high H3K27ac, high H3K4me1), repressor (high H3K27me3), and two quiescent (low signal for all assays) states. The state map with assigned names is shown in Figure 1—figure supplement 1A.

We next defined stretch enhancer elements at each developmental stage and in mature islets. For each active enhancer (EnhA) element, we determined the number of consecutive 200 bp bins covered by the enhancer. We then modeled the resulting bin counts for enhancers in each cell type using a Poisson distribution. Enhancers with a p-value less than. 001 were labeled as stretch enhancers and otherwise labeled as traditional enhancers.

### Permutation-based significance

A random sampling approach (10,000 iterations) was used to obtain null distributions for enrichment analyses, in order to obtain p-values. Null distributions for enrichments were obtained by randomly shuffling enhancer regions using BEDTools (Quinlan and Hall, 2010) and overlapping with ATAC-seq peaks. p-values<0.05 were considered significant.

### Assignment of enhancer target genes

Transcriptomes were filtered for genes expressed (FPKM ≥1) at each relevant stage, and BEDTools (Quinlan and Hall, 2010) was used to assign each enhancer to the nearest annotated TSS.

### Gene ontology

All gene ontology analyses were performed using Metascape (Zhou et al., 2019) with default parameters.

### Motif enrichment analysis

The findMotifsGenome.pl. command in HOMER (Heinz et al., 2010) was used to identify enriched transcription factor binding motifs. de novo motifs were assigned to transcription factors based on suggestions generated by HOMER.

### T2D-relevant trait enrichment analysis

GWAS summary statistics for T2D (Mahajan et al., 2018; Perry et al., 2012), metabolic traits (HOMA-B, HOMA-IR [Dupuis et al., 2010], fasting glucose, fasting insulin [Manning et al., 2012], fasting proinsulin [Strawbridge et al., 2011], 2 hr glucose adjusted for BMI [Saxena et al., 2010], HbA1c, insulin secretion rate, disposition index, acute insulin response, peak insulin response [Wood et al., 2017]), and developmental traits (head circumference [Taal et al., 2012], birth length [van der Valk et al., 2015], birth weight [Horikoshi et al., 2016]) conducted with individuals of European ancestry were obtained from various sources including the MAGIC consortium, EGG consortium, and authors of the studies. Custom LD score annotation files were created for PSSE, PP2 stretch enhancers, and islet stretch enhancers using LD score regression version 1.0.1 (Bulik-Sullivan et al., 2015). Enrichments for GWAS trait-associated variants within PSSE, PP2 stretch enhancers, and islet stretch enhancers were estimated with stratified LD score regression (Finucane et al., 2015). We next determined enrichment in the proportion of variants in accessible chromatin sites within islet SE and PSSE with nominal association to beta cell-related glycemic traits. For each trait, we calculated a 2 × 2 table of variants mapping in and outside of islet SE or PSSE and with or without nominal association and then determined significance using a chi-square test.

### Adipocyte differentiation analysis

Chromatin states for human adipose stromal cell (hASC) differentiation stages (1-4) were obtained from a published study (Varshney et al., 2017). PSSE were intersected with hASC chromatin states using BEDTools intersect (version 2.26.0) (Quinlan and Hall, 2010) with default parameters.

### Identification of T2D risk loci intersecting PSSE

T2D GWAS summary statistics were obtained from the DIAMANTE consortium (Mahajan et al., 2018). Intersection of variants and PSSE was performed using BEDTools intersect (version 2.26.0) (Quinlan and Hall, 2010) with default parameters. The adjusted significance threshold was set at p<4.66 × 10−6 (Bonferroni correction for 10,738 variants mapping in PSSE). Putative novel loci were defined as those with (1) at least one variant in a PSSE reaching the adjusted significance threshold and (2) mapping at least 500 kb away from a known T2D locus.

### ATAC-seq footprinting analysis

ATAC-seq footprinting was performed as previously described (Aylward et al., 2018). In brief, diploid genomes for CyT49 were created using vcf2diploid (version 0.2.6a) (Rozowsky et al., 2011) and genotypes called from whole genome sequencing and scanned for a compiled database of TF sequence motifs from JASPAR (Mathelier et al., 2016) and ENCODE (ENCODE Project Consortium, 2012) with FIMO (version 4.12.0) (Grant et al., 2011) using default parameters for p-value threshold and a 40.9% GC content based on the hg19 human reference genome. Footprints within ATAC-seq peaks were discovered with CENTIPEDE (version 1.2) (Pique-Regi et al., 2011) using cut-site matrices containing Tn5 integration counts within a ± 100 bp window around each motif occurrence. Footprints were defined as those with a posterior probability ≥0.99.

### Generation of similarity matrices for total transcriptomes

For each replicate, FPKM values corresponding to total transcriptome were filtered for genes expressed (FPKM ≥1) in ≥1 replicate. For expressed genes, log(FPKM+1) values were used to calculate Pearson correlations.

### Immunofluorescence analysis

Cell aggregates derived from hESCs were allowed to settle in microcentrifuge tubes and washed twice with PBS before fixation with 4% paraformaldehyde (PFA) for 30 min at room temperature. Fixed samples were washed twice with PBS and incubated overnight at 4°C in 30% (w/v) sucrose in PBS. Samples were then loaded into disposable embedding molds (VWR), covered in Tissue-Tek O.C.T. Sakura Finetek compound (VWR) and flash frozen on dry ice to prepare frozen blocks. The blocks were sectioned at 10 µm and sections were placed on Superfrost Plus (Thermo Fisher) microscope slides and washed with PBS for 10 min. Slide-mounted cell sections were permeabilized and blocked with blocking buffer, consisting of 0.15% (v/v) Triton X-100 (Sigma) and 1% (v/v) normal donkey serum (Jackson Immuno Research Laboratories) in PBS, for 1 hr at room temperature. Slides were then incubated overnight at 4°C with primary antibody solutions. The following day slides were washed five times with PBS and incubated for 1 hr at room temperature with secondary antibody solutions. Cells were washed five times with PBS before coverslips were applied.

All antibodies were diluted in blocking buffer at the ratios indicated below. Primary antibodies used were goat anti-PDX1 (1:500 dilution, Abcam ab47383), mouse anti-NKX6.1 (1:300 dilution, Developmental Studies Hybridoma Bank F64A6B4), rabbit anti-Laminin (1:30, Sigma L-9393), and rabbit anti-CRB2 (1:500, Sigma SAB1301340). Secondary antibodies against goat and mouse were Alexa488- and Cy3-conjugated donkey antibodies, respectively (Jackson Immuno Research Laboratories 705-545-003 and 715-165-150, respectively), and were used at dilutions of 1:500 (anti-goat Alexa488) or 1:1000 (anti-mouse Cy3). Cell nuclei were stained with Hoechst 33342 (1:3000, Invitrogen). Representative images were obtained with a Zeiss Axio-Observer-Z1 microscope equipped with a Zeiss ApoTome and AxioCam digital camera. Figures were prepared in Adobe Creative Suite 5.

### Flow cytometry analysis

Cell aggregates derived from hESCs were allowed to settle in microcentrifuge tubes and washed with PBS. Cell aggregates were incubated with Accutase at room temperature until a single-cell suspension was obtained. Cells were washed with 1 mL ice-cold flow buffer comprised of 0.2% BSA in PBS and centrifuged at 200 g for 5 min. BD Cytofix/Cytoperm Plus Fixation/Permeabilization Solution Kit was used to fix and stain cells for flow cytometry according to the manufacturer's instructions. Briefly, cell pellets were re-suspended in ice-cold BD Fixation/Permeabilization solution (300 µL per microcentrifuge tube). Cells were incubated for 20 min at 4°C. Cells were washed twice with 1 mL ice-cold 1 × BD Perm/Wash Buffer and centrifuged at 10°C and 200 × g for 5 min. Cells were re-suspended in 50 µL ice-cold 1 × BD Perm/Wash Buffer containing diluted antibodies, for each staining performed. Cells were incubated at 4°C in the dark for 1–3 hr. Cells were washed with 1.25 mL ice-cold 1X BD Wash Buffer and centrifuged at 200 × g for 5 min. Cell pellets were re-suspended in 300 µL ice-cold flow buffer and analyzed in a FACSCanto II (BD Biosciences). Antibodies used were PE-conjugated anti-PDX1 (1:10 dilution, BD Biosciences); and AlexaFluor 647-conjugated anti-NKX6.1 (1:5 dilution, BD Biosciences). Data were processed using FlowJo software v10.

### Whole mount immunohistochemistry

Zebrafish larvae were fixed and stained according to published protocols (Lancman et al., 2013) using the following antibodies: chicken anti-GFP (1:200; Aves Labs; GFP-1020), guinea pig anti-insulin (1:200; Biomeda; v2024), mouse anti-Crb2a (1:100; ZIRC; zs-4), rabbit anti-panCrb (1:100; provided by Dr. Abbie M. Jensen at University of Massachusetts, Amherst; Hsu and Jensen, 2010), rabbit anti-Laminin (1:100; Sigma;L9393), mouse anti-Nkx6.1 (1:10; DSHB; F55A10), and DAPI (1:200; 500 mg/ml, Invitrogen; D1306).

### Imaging and quantification of beta cell numbers in zebrafish

To quantify beta cell numbers, 50 and 78 hpf zebrafish larvae were stained for confocal imaging using DAPI and guinea pig anti-insulin antibody (1:200; Biomeda; v2024). Whole mount fluorescent confocal Z-stacks (0.9 μm steps) images were collected for the entire islet with optical slices captured at a focal depth of 1.8 μm. Samples were imaged using a Zeiss 710 confocal microscope running Zen 2010 (Black) software. Final images were generated using Adobe Photoshop CS6 and/or ImageJ64 (vs.1.48b).

### Data sources

The following datasets used in this study were downloaded from the GEO and ArrayExpress repositories:

RNA-seq: Pancreatic differentiation of CyT49 hESC line (E-MTAB-1086); primary islet data (GSE115327).

ChIP-seq: H3K27ac data in primary islets (E-MTAB-1919 and GSE51311); H3K27ac data in pancreatic differentiation of CyT49 hESC line (GSE54471); H3K4me1 data in pancreatic differentiation of CyT49 hESC line (GSE54471); H3K4me1 data in primary islets (E-MTAB-1919 and E-MTAB 189); H3K27me3 and H3K4me3 in pancreatic differentiation of CyT49 hESC line (E-MTAB-1086); H3K4me3 and H3K27me3 in primary islets (E-MTAB-189); CTCF in primary islets (E-MTAB-1919); PDX1 in CyT49 PP2 (GSE54471); samples from ROADMAP consortium: http://ncbi.nlm.nih.gov/geo/roadmap/epigenomics.

ATAC-seq: primary islet data (PRJN527099); CyT49 PP2 (GSE115327).

Hi-C datasets were generated in collaboration with the Ren laboratory at University of California, San Diego as a component of the 4D Nucleome Project (Dekker et al., 2017) under accession number 4DNES0LVRKBM.

### Quantification and statistical analyses

Statistical analyses were performed using GraphPad Prism (v8.1.2), and R (v3.6.1). Statistical parameters, such as the value of n, mean, standard deviation (SD), standard error of the mean (SEM), significance level (*p<0.05, **p<0.01, and ***p<0.001), and the statistical tests used, are reported in the figures and figure legends. The ‘n’ refers to the number of independent pancreatic differentiation experiments analyzed (biological replicates).

Statistically significant gene expression changes were determined with DESeq2 (Love et al., 2014).
