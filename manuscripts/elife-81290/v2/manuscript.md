# Transcriptional profiling of Hutchinson-Gilford Progeria syndrome fibroblasts reveals deficits in mesenchymal stem cell commitment to differentiation related to early events in endochondral ossification

## Authors

- Rebeca San Martin<sup>1</sup> ([ORCID: 0000-0001-7249-3922](https://orcid.org/0000-0001-7249-3922))
- Priyojit Das<sup>2</sup> ([ORCID: 0000-0002-6774-6718](https://orcid.org/0000-0002-6774-6718))
- Jacob T Sanders<sup>1</sup>
- Ashtyn M Hill<sup>1</sup>
- Rachel Patton McCord<sup>1</sup> ([ORCID: 0000-0003-0010-5323](https://orcid.org/0000-0003-0010-5323)) †

### Affiliations

1. Department of Biochemistry & Cellular and Molecular Biology, University of Tennessee at Knoxville Knoxville United States ([ROR:020f3ap87](https://ror.org/020f3ap87))
2. UT-ORNL Graduate School of Genome Science and Technology, University of Tennessee at Knoxville Knoxville United States ([ROR:020f3ap87](https://ror.org/020f3ap87))
3. Department of Pathology, University of Texas Southwestern Medical Center Dallas United States ([ROR:00t9vx427](https://ror.org/00t9vx427))

† Corresponding author

## Abstract

The expression of a mutant Lamin A, progerin, in Hutchinson-Gilford Progeria Syndrome leads to alterations in genome architecture, nuclear morphology, epigenetic states, and altered phenotypes in all cells of the mesenchymal lineage. Here, we report a comprehensive analysis of the transcriptional status of patient derived HGPS fibroblasts, including nine cell lines not previously reported, in comparison with age-matched controls, adults, and old adults. We find that Progeria fibroblasts carry abnormal transcriptional signatures, centering around several functional hubs: DNA maintenance and epigenetics, bone development and homeostasis, blood vessel maturation and development, fat deposition and lipid management, and processes related to muscle growth. Stratification of patients by age revealed misregulated expression of genes related to endochondral ossification and chondrogenic commitment in children aged 4–7 years old, where this differentiation program starts in earnest. Hi-C measurements on patient fibroblasts show weakening of genome compartmentalization strength but increases in TAD strength. While the majority of gene misregulation occurs in regions which do not change spatial chromosome organization, some expression changes in key mesenchymal lineage genes coincide with lamin associated domain misregulation and shifts in genome compartmentalization.

## Introduction

Hutchinson-Gilford progeria syndrome (HPGS) is a rare disease, characterized by a severe premature aging phenotype (Gilford and Hutchinson, 1897; Hutchinson, 1886). Patients appear normal at birth, with a disease onset around 2 years of age when they present with slow growth rate, short stature, and marked lipodystrophy with a characteristic loss of subcutaneous fat. With progression, patients experience arthritis, joint contracture, osteoporosis and stiffening of blood vessels. Average life expectancy for HPGS patients is 13.4 years, with myocardial infarction and stroke being the predominant causes of death (Foundation, 2019).

HGPS is caused by a thymidine substitution mutation at cytidine 608 (GGC >GGT), within exon 11 of the gene that encodes for Lamin A (LMNA) (De Sandre-Giovannoli et al., 2003; Eriksson et al., 2003). Lamin A is a structural protein of the nuclear envelope, playing an important role in genome structure and nuclear integrity. The mutation does not result in an amino acid substitution, frame shift or early termination. Rather, it induces the usage of a cryptic splice site and the subsequent deletion of 50 amino acids at the C terminus. In turn, this deletion impedes downstream processing of the protein and results in conservation of C terminus farnesylation (Davies et al., 2009). This abnormal protein product is called Progerin. Aggregation of Progerin leads to a disruption of the normal nuclear envelope meshwork, leading to deformed nuclei, nuclear stiffening, and defective mechanotransduction (Apte et al., 2017; Goldman et al., 2004; Lammerding et al., 2004).

Of particular interest, progeria patients present with various defects in all tissues of the mesenchymal lineage. Specifically, regarding bone physiology, patients show reduced stature, generalized osteopenia, thin calvaria, and clavicle regression with absence of medial and lateral ends, as well as resorption of the distal bony phalanges and anterior ribs (Chawla et al., 2017; Cleveland et al., 2012; Gordon et al., 2011; Nazir et al., 2017). These phenotypes are more striking when considering that at birth, bone structure appears normal. Previous observations, where fibroblasts from progeria patients showed abnormal levels of aggrecan (Lemire et al., 2006) a marker of chondrogenic differentiation, led us to hypothesize that fibroblasts derived from HGPS patients – themselves a cell of the mesenchymal lineage – could harbor vestigial transcriptional signatures to abnormal mesenchymal stem cell commitment, which would become apparent by comparing them with different normal age group controls.

In this study, we conduct a comprehensive analysis of previously published RNA-seq datasets for HPGS fibroblast cells harboring the typical C>T mutation in the LMNA gene and provide transcriptomics data for nine patient fibroblast samples that had no previously reported RNA-seq data. By comparing the transcriptional profile of HPGS fibroblasts (33 datasets, 21 patients, 1–20 years old) with fibroblasts derived from age-matched controls (21 datasets, 16 donors, 1–19 years old), healthy adults, (16 donors, 26–43 years old) and healthy old adults (15 donors, 80–96 years old), we provide insight into important defects in repair biology, metabolism (calcium, lipid), and other areas important to the mesenchymal cell lineage. Our results show that transcription of genes involved in negative regulation of chondrocyte commitment is compromised in fibroblasts from patients that are at the age of onset of postnatal endochondral ossification. We report that some genes central to differentiation commitment into the chondrogenic-osteogenic lineage and identified as misregulated in this study (PTHLH, BMP4, FZD4, and IGF1) show either abnormal genomic architecture or lamin associated domain alterations.

Our results support the hypothesis that defects in the initial steps of chondrogenesis commitment are a potential mechanism for mesenchymal stem cell depletion that later results in abnormal adipogenesis, diminished microvasculature homeostasis, and poor wound repair observed in HGPS patients.

## Results

### Batch correction is essential for comparison among patient and normal cohorts

To determine gene sets that were consistently misregulated in Progeria fibroblasts, we collected both newly generated and previously published RNA-seq data from all available Progeria patient fibroblast cell samples as well as fibroblasts from control individuals in different age groups (Appendix 1—tables 1–3; Fleischer et al., 2018; Ikegami et al., 2020; Köhler et al., 2020; Mateos et al., 2018). When the resulting transcriptomics data were analyzed by principal component analysis (PCA), datasets clustered according to laboratory of origin regardless of diagnosis, making direct comparisons impossible (Figure 1—figure supplement 1A), as has been previously observed in Progeria transcriptomics analysis (Ikegami et al., 2020) However, after batch effect correction (materials and methods Zhang et al., 2020a), the first principal component was able to segregate the samples depending on progeria/non progeria origin (Figure 1—figure supplement 1B) which enabled direct comparisons between patients and controls from different age groups which originated from different sources.

### Gene ontology analysis of transcriptional changes reveals eight clusters of biological activity affected in HGPS

To derive sets of genes differentially regulated in Progeria, we divided the patient samples into Young (0–8 years old) and Teen (>13 years old) categories based on the idea that different developmental processes take place in these age groups. We then compared each patient group to age-matched controls, middle-aged adults, and older adults and selected up and down-regulated genes (FDR adjusted P-value <0.001) for gene ontology analysis. Teenage HGPS patients showed the smallest number of genes changing expression levels when compared to age-matched controls, but the highest number of genes up/down regulated when compared to healthy middle-aged or old adults (Table 1 and Table 1—source data 1). Importantly, comparisons between the normal children cohort and the adult normal controls yield few significant changes, suggesting that HGPS is the driver of the differences observed among cohorts.

**Table 1.**
 Number of up/down-regulated genes per age comparisons.Table 1—source data 1.Metascape outputs for gene ontology analysis.Childhood and teenaged patient samples compared to middle aged and older adults.


<table>
  <thead>
    <tr>
      <th>Comparisons</th>
      <th>Upregulated genes</th>
      <th>Downregulated genes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Young patients – Age matched</td>
      <td>260</td>
      <td>63</td>
    </tr>
    <tr>
      <td>Young patients – Adult control</td>
      <td>574</td>
      <td>241</td>
    </tr>
    <tr>
      <td>Young patients – Old adult control</td>
      <td>984</td>
      <td>435</td>
    </tr>
    <tr>
      <td>Teenaged patients – Age matched</td>
      <td>237</td>
      <td>81</td>
    </tr>
    <tr>
      <td>Teenaged patients – Adult control</td>
      <td>1873</td>
      <td>1138</td>
    </tr>
    <tr>
      <td>Teenaged patients – Old adult control</td>
      <td>1872</td>
      <td>1022</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Young Control – Adult Control</td>
      <td>28</td>
      <td>25</td>
    </tr>
    <tr>
      <td>Young Control – Old Control</td>
      <td>817</td>
      <td>421</td>
    </tr>
  </tbody>
</table>

Overall, relevant gene ontology terms identified in the study pertain to eight functional clusters: DNA maintenance and Epigenetics (Figure 1), Repair and Extracellular matrix (Figure 2), Bone (Figure 3), Adipose Tissue (Figure 4), Blood Vessels (Figure 5), and Muscle (Figure 6).

![Figure 1.](https://cdn.elifesciences.org/articles/81290/elife-81290-fig1-v2.jpg)

**Figure 1.:** (A) Summary table of processes related to DNA maintenance and epigenetics, represented as transcriptional up or downregulation based on RNA-seq of young/teenager progeria patient derived fibroblasts compared to age matched, middle age or old control patients. (B) Heat map of RNA-seq transcriptome analysis for 976 selected genes related to DNA maintenance and epigenetics. The heat map shows per-gene z-score computed from batch effect corrected log2 read count values, genes in rows and 29 patient samples (progeria and young/adult/old control) organized in columns. Genes were hierarchically clustered based on Euclidean distance and average linkage. Within each cohort, columns are organized by patient age. (C) Comparison of young progeria patients versus middle age or old donor control fibroblasts. Enriched ontology clusters for upregulated genes related DNA maintenance and epigenetics, as characterized by Metascape analysis. Metascape reports p-values calculated based on the hypergeometric distribution. (D) Comparison of teen-aged progeria patient fibroblast versus old donor control fibroblasts. Enriched ontology clusters for up regulated genes related to DNA maintenance and epigenetics, as characterized by Metascape analysis.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/81290/elife-81290-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) Principal component analysis (PCA) of the datasets used in this study before batch correction. Samples segregate primarily by lab of origin (red circles). Solid color markers: Progeria, hollow markers: normal controls, triangles: female, circles: male. (B) PCA after batch correction. Samples primarily segregate by progeria/control phenotype. Dotted line denotes an arbitrary margin between cohorts. Solid color markers: Progeria, hollow markers: normal controls, triangles: female, circles: male. Purple circles denote patients that are mismatched from the rest of their respective groups.

![Figure 2.](https://cdn.elifesciences.org/articles/81290/elife-81290-fig2-v2.jpg)

**Figure 2.:** (A) Heat map of RNA-seq transcriptome analysis for 585 selected genes related to repair. Data presented as in Figure 1B. (B) Heat map of RNA-seq transcriptome analysis for 145 selected genes related to extra cellular matrix. Data presented as in Figure 1B. (C) Summary table of processes related to repair and extra cellular matrix organization, represented as up or downregulation in transcription based on RNA-seq of young/teenager progeria patient derived fibroblasts, compared to middle age or old control patients. Age comparisons that yielded no significant results in relevant categories are not shown.

![Figure 3.](https://cdn.elifesciences.org/articles/81290/elife-81290-fig3-v2.jpg)

**Figure 3.:** (A) Summary table of processes related to bone and cartilage development and homeostasis represented as up or downregulated transcription based on RNA-seq of young progeria patient derived fibroblasts compared to age matched, middle age or old control patients. (B) Heat map of RNA-seq transcriptome analysis for 165 selected genes related to bone and cartilage development. Data presented as in Figure 1B. (C) Comparison of young progeria patients versus old donor control fibroblasts. Enriched ontology clusters for upregulated genes related bone and cartilage development and homeostasis, as characterized by Metascape analysis. (D) Comparison of young progeria patients versus old donor control fibroblasts. Enriched ontology clusters for downregulated genes related to cation homeostasis, as characterized by Metascape analysis. (E) Comparison of young progeria patients versus middle age control fibroblasts. Enriched ontology clusters for downregulated genes related to bone development and homeostasis, as characterized by Metascape analysis.

![Figure 4.](https://cdn.elifesciences.org/articles/81290/elife-81290-fig4-v2.jpg)

**Figure 4.:** (A) Summary table of processes related to fat cell differentiation and lipid metabolism, represented as up or downregulation in transcription based on RNA-seq of young/teenager progeria patient derived fibroblasts, compared to age matched, middle age, or old control patients. (B) Heat map of RNA-seq transcriptome analysis for 134 selected genes related to fat cell differentiation and lipid metabolism. Data presented as in Figure 1B. (C) Comparison of young progeria patients versus middle age or old donor control fibroblasts. Enriched ontology clusters for upregulated genes related to fat and lipid metabolism, as characterized by Metascape analysis.

![Figure 5.](https://cdn.elifesciences.org/articles/81290/elife-81290-fig5-v2.jpg)

**Figure 5.:** (A) Summary table of processes related to blood vessel homeostasis, represented as up or downregulation in transcription based on RNA-seq of young/teenager progeria patient derived fibroblasts, compared to age matched, middle age, or old control patients. (B) Heat map of RNA-seq transcriptome analysis for 131 selected genes related to blood vessel homeostasis. Data presented as in Figure 1B. (C) Comparison of young progeria patients versus middle-aged donor control fibroblasts. Enriched ontology clusters for upregulated genes related to blood vessel development, as characterized by Metascape analysis. (D) Comparison of teen-aged progeria patient fibroblast versus age-matched control fibroblasts. Enriched ontology clusters for upregulated genes related to blood vessel development, as characterized by Metascape analysis.

![Figure 6.](https://cdn.elifesciences.org/articles/81290/elife-81290-fig6-v2.jpg)

**Figure 6.:** (A) Summary table of processes related to muscle and cardiac muscle development, represented as up or downregulation in transcription based on RNA-seq of young/teenager progeria patient derived fibroblasts, compared to middle age or old control patients. (B) Heat map of RNA-seq transcriptome analysis for 261 selected genes related to muscle development. Data presented as in Figure 1B. (C) Comparison of young progeria patients versus middle-aged and old donor control fibroblasts and of teen-aged progeria patients versus old donor controls. Enriched ontology clusters for upregulated genes related to muscle development, as characterized by Metascape analysis.

The largest number of differentially expressed genes (Nine hundred and seventy) were related to the biological processes of epigenetic programming and DNA maintenance (Figure 1A and Figure 1—source data 1). Gene ontology pathways included in this cohort include epigenetic regulation of gene silencing, senescence-associated heterochromatin, DNA repair, DNA recombination, and histone methylation/modifications. This is in line with extensive previous evidence of epigenetic and DNA repair misregulation in Progeria (Aguado et al., 2019; Gonzalo and Coll-Bonfill, 2019; Misteli and Scaffidi, 2005). These genes were predominantly over-expressed in young progeria patients when compared to all controls (Figure 1B,C) and between teenaged patients compared to their age matched control and adults (Figure 1B,D).

The next biological process with the most misregulated transcription among age groups was tissue repair. It bears mentioning that most of the nucleosome-associated proteins and histones identified in the DNA maintenance cluster, as previously described, overlap with the repair GO terms. In all, 585 genes are differentially expressed between cohorts (Figure 2A), with HGPS patients predominantly overexpressing targets pertaining to the organization of the extracellular matrix (145 genes, Figure 2B). Interestingly, signatures related to coagulation, Bone Morphogenic Protein signaling, and response to wound healing are all downregulated in young HGPS patients when compared to adults (Figure 2C).

In this analysis of fibroblasts, we also identified misregulation of gene targets typically associated with the biology of mesenchymal tissue. Specifically, we see misregulation of transcription of genes involved in bone (165 genes. Figure 3), fat (261 genes. Figure 4), blood vessel homeostasis (131 genes. Figure 5), and muscle (261 genes. Figure 6). All these lineages have been observed as compromised in HGPS patients, showing phenotypes like osteopenia, early atherosclerosis, and lack of subcutaneous fat deposition. (Gordon et al., 2011; Hamczyk et al., 2018; Xiong et al., 2013).

Bone biology mis-regulation appears to be stratified into two distinct hubs: downregulation of pathways related to calcium homeostasis and transport and upregulation of pathways involved in cell differentiation of chondrocytes and osteoblasts (Figure 3A,B and Figure 3—source data 1). Comparing young patients’ transcriptional profile to that of old adult normal controls shows upregulation of genes involved in late osteogenic commitment. Such is the case of ontology terms that include osteoblast differentiation, ossification, and chondrocyte differentiation (Figure 3C). In parallel, genes included in pathways related to cation homeostasis, particularly calcium, are downregulated (Figure 3D). This comparison is similar to that of young patients and normal middle-aged adult controls (Figure 3E).

Lipid homeostasis and transport pathways are downregulated in all comparisons between samples from young patients. Young HGPS samples show downregulation in pathways involving fat cell differentiation when compared to age-matched controls, in line with observed fat deposition defects in patients (Revêchon et al., 2017; Figure 4A–C).

Gene ontology terms related to blood vessels show upregulation of blood vessel morphogenesis, but a decrease of blood vessel maturation when comparing samples from young patients to either age-matched or old controls (Figure 5A–C). This phenotype persists in comparisons between teen aged patients and their age-matched controls (Figure 5D). Further, in a possible contribution to the circulatory defects observed in HGPS patients, both young and teen-aged patient samples show a marked upregulation of genes in pathways related to muscle development and cardiac muscle differentiation and development when comparing both HGPS cohorts against adult controls (Figure 6A–C).

### Age stratification of young patients highlights differences in HGPS gene misregulation across childhood

To further refine our findings related to young age patients and the mesenchymal phenotypes observed, we stratified the young HGPS patients into two age groups: early infancy (0–3 years old) and children (4–7 years old), comparing these cohorts to age matched, middle age and old controls as before. The total numbers of genes up and down regulated between comparisons are described in Table 2 and Table 2—source data 1. In this analysis, about forty percent of genes upregulated in early infant patients when compared against their age matched controls are related to epigenetic modifications as described in the previous analysis (Figure 1). Specifically, the GO term ‘HDACs deacetylate histones’ shows the highest enrichment in this group. These same genes are represented in the comparison with the middle age-old adult control groups.

**Table 2.**
 Number of up/down-regulated genes in young patient cohort comparisons.Table 2—source data 1.Metascape outputs for gene ontology analysis.Early and late childhood patient samples compared to healthy children, middle aged, and older adults.


<table>
  <thead>
    <tr>
      <th>Comparisons</th>
      <th>Upregulated genes</th>
      <th>Downregulated genes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Early Infant – Age matched</td>
      <td>113</td>
      <td>25</td>
    </tr>
    <tr>
      <td>Early Infant – Middle aged adult</td>
      <td>540</td>
      <td>172</td>
    </tr>
    <tr>
      <td>Early Infant – Old adult</td>
      <td>646</td>
      <td>388</td>
    </tr>
    <tr>
      <td>Children - Age matched</td>
      <td>203</td>
      <td>102</td>
    </tr>
    <tr>
      <td>Children - Middle aged adult</td>
      <td>173</td>
      <td>184</td>
    </tr>
    <tr>
      <td>Children - Old adult</td>
      <td>305</td>
      <td>394</td>
    </tr>
  </tbody>
</table>

In contrast, the comparison of patients aged 4–7 years to their age matched controls show an enrichment for ossification and calcium homeostasis. Out of the cohort of genes identified as downregulated in this comparison (102), about 10% are related to early chondrogenesis events. Among those, parathyroid hormone related protein (PTHLH), insulin like growth factor (IGF1), bone morphogenic protein receptor 1B (BMPR1B), and collagen 10a1 (COL10a1), are an integral part of early commitment and control necessary for the triggering of endochondral ossification (Bradley and Drissi, 2010; Green et al., 2015; Maruyama et al., 2010). Genes related to ossification and calcium homeostasis were also identified as downregulated in this cohort. Further, upregulated genes in age-matched and adult comparisons include BMP4, and several genes related to WNT5a biology which play an important role in skeletal development (Figure 7A–C).

![Figure 7.](https://cdn.elifesciences.org/articles/81290/elife-81290-fig7-v2.jpg)

**Figure 7.:** (A) Heat map of RNA-seq transcriptome analysis for 25 selected genes related to endochondral ossification. The heat map shows per-gene z-score computed from batch effect corrected log2 read count values, genes in rows and 29 patient samples (progeria and young/adult/old control) organized in columns. Genes were hierarchically clustered based on Euclidean distance and average linkage. Blue lines separate young infants (0–3 y/o) from children (4–7 y/o) and older children (8–10 y/o). Genes related to WNT5a biology highlighted (red circle). (B) Abridged signaling pathway for WNT5a, highlighting the roles of the genes whose transcription is affected in young HGPS patients compared to their aged-matched controls. (C) BMP4 expression, also identified as significantly upregulated in the analysis of all HGPS patients (Figure 3) differs between Progeria (pink) and control (blue) samples. (* indicates p<0.05 by Kruskal Wallis test; dotted lines within the violin plots indicate 25th, median, and 75th percentiles).

### Genes of interest are impacted by chromatin compartment switches or abnormal lamina associated domains (LADs)

Chromosome conformation capture was performed on skin fibroblasts from parents of HGPS patients (Mother AG03257, Father HGADFN168), from 8-year-old male and female HGPS patients (HGADFN167 and AG11513), and from an age matched (8-year-old male) healthy control (GM08398) (Appendix 1—table 4). Genome-wide contact maps for all of these cells show globally similar patterns of chromosome conformation, with the exception of a translocation between chr3 and chr11 in AG11513 cells (Figure 8A). At a whole chromosome folding level, we note that progeria fibroblasts show a decrease in telomere interactions and an apparent loss of ‘Rabl’ like structure (Figure 8B). This type of Rabl structure loss was previously observed after DNA damage in fibroblasts (Sanders et al., 2020). We find that topologically associating domain (TAD) structure is preserved in Progeria fibroblasts, with even an increase in TAD boundary strength as compared to healthy parent controls (Figure 8C). A similar increase in TAD boundary strength was previously found in senescent and progerin-expressing human mesenchymal progenitor cells (Liu et al., 2022). Increased TAD boundary strength was also previously observed in DNA damaged fibroblasts (Sanders et al., 2020), suggesting that some of these features of genome structure may relate to the increased constitutive levels of DNA damage observed in these patient fibroblasts.

![Figure 8.](https://cdn.elifesciences.org/articles/81290/elife-81290-fig8-v2.jpg)

**Figure 8.:** (A) 2.5 Mb Hi-C heatmaps for AG03257-P7 (Mother, WT), and HGPS patients (HGADFN167-P19 and AG11513-P7) Translocations between chromosomes appear as high interaction frequency regions (red) away from the diagonal. A translocation between chromosomes 3 and 11 is apparent in AG11513 cells (circle). (B) Log ratio of 2.5 Mb contact frequency in Progeria (167-P19) vs. healthy father (168-P16). Loss of telomere interactions is notable as blue patches in the corner of each chromosome. (C) TAD boundary strength boxplots calculated using the InsulationScore approach between early (left) and late (right) passage Progeria cells minus their respective controls. Boxes represent the upper and lower quartiles with the center line as the median. Upper whiskers extend 1.5×IQR beyond the upper quartile, and lower whiskers extend either 1.5×IQR below the lower quartile or to the end of the dataset. (D) Plots of the first eigenvector for a section of chromosome 12, obtained from principal component analysis (PC1) of 250 kb binned Hi-C data for control fibroblasts (Mother AG03257, Father HGADFN168) and HGPS fibroblasts (HGADFN167 and AG11513). Compartment identity remains predominantly unchanged (A compartment: Red, B compartment: Blue). (E) Graphs showing the A-A compartment interaction strength (red) and B-B compartment interaction strength (blue) within each chromosome for related father and child cell lines (HGADFN168, HGADFN167). Samples were collected a both early (left; P12) and late passages (middle; P19 for Progeria and P27 for father). Comparison between the two samples (right) shows that the HPGS cell line shows a marked decrease in A-A compartment interaction strength in late passages in the majority of chromosomes. (F) Eigen 1 values represent the compartment identity (same as plotted in D) for genes identified in this study as upregulated (left) or downregulated (right) in the 0–7 year-old age-matched comparison. While differences between groups are not significant overall (Kruskal-Wallis), a subset of downregulated genes appear to be changing conformation to a B compartment in progeria samples (box). Violin plots for the global distribution of values; median denoted by a thick dashed line, 25th and 75th percentiles highlighted as thin dashed lines. Percentages of genes in the B compartment are indicated in the box below downregulated gene graph. (G) Compartment identity for genes identified in this study as upregulated (left) or downregulated (right) in the 0–7 year-old HGPS samples compared to normal middle-aged controls. (H) Compartment identity for genes identified in this study as upregulated (left) or downregulated (right) in the 0–7 year-old HGPS samples compared to old-aged controls.

![Figure 8—figure supplement 1.](https://cdn.elifesciences.org/articles/81290/elife-81290-fig8-figsupp1-v2.jpg)

**Figure 8—figure supplement 1.:** (A) The genomic regions for downregulated genes identified in our age comparisons were compiled with the LAD identity found in father and HGPS child fibroblasts (HGADFN168 and HGADFN167, respectively). Comparisons are presented as follows, from left to right: Young HGPS (0–7 years old) compared to middle-aged controls, young HGPS patients compared to old controls, teenaged HGPS compared to middle-aged controls and teenaged HGPS compared to old controls. Differences between al groups are significant (Kruskal-Wallis p<0.001) Violin plots for the global distribution of values; median denoted by thick dashed line, 25th and 75th percentiles highlighted as thin dashed lines. (B) The genomic regions for up regulated genes identified in our age comparisons were compiled with the LAD identity found in father and HGPS child fibroblasts (HGADFN168 and HGADFN167, respectively). Comparisons are presented as follows, from left to right: Young HGPS (0–7 years old) compared to middle-aged controls, young HGPS patients compared to old controls, teenaged HGPS compared to middle-aged controls and teenaged HGPS compared to old controls. Differences between al groups are significant (Kruskal-Wallis p<0.001) Violin plots for the global distribution of values; median denoted by thick dashed line, 25th and 75th percentiles highlighted as thin dashed lines. (C) LAD distribution along chromosome 1 and 21. LAD identity remains consistent among samples, with small regional changes in LAD definition in specific areas (highlighted- rectangle). The greatest difference among samples is the strength in LAD definition, as characterized by smaller positive and negative values. (D) The genome-wide distribution of LADs, as characterized by DamID-seq shows that normal fibroblast lines HGADFN168 (belonging to a father of an HGPS patient) and HFFc6 (human foreskin fibroblast), show a characteristic bimodal distribution in LAD intensity around positive (LAD) and negative (non-LAD) values. In contrast, LAD values for the HGPS cell line HGADFN167 distribute normally, around zero.

Using principal component analysis of Hi-C data at 250 kb-resolution, we classified genomic regions into open euchromatin (A) or closed heterochromatin (B) spatial compartments according to positive and negative values of the first eigenvector, respectively. Since accelerated senescence has been previously observed in progeria fibroblasts (Bridger and Kill, 2004; Wheaton et al., 2017), we performed compartment analysis on cells belonging to a father-child pair, at early and late passages. Samples were collected for the HGADFN168 cells (Father) at passages 12 and 27, and for the HGADFN167 (Child) at passages 12 and 19. Our results show that in the parent fibroblasts there are small changes in compartment strength (the degree of preference for interactions within the same compartment vs. between different compartments). In contrast, there is a predominant loss of A compartment strength in the late passage HGPS cells (Figure 8E). Interestingly, although the compartmentalization strength appears to be altered, the genome-wide compartment identity remains consistent among cohorts, with small changes in compartment identity appearing sporadically (Figure 8D). The loss of compartment strength at later passages in Progeria cells is consistent with previous observations, though this more deeply sequenced, and less noisy dataset shows that compartments are more preserved in Progeria cells than previously observed (McCord et al., 2013).

To test whether the up or downregulation of genes identified through this study relates to compartment switching, we evaluated the compartment identity strength of all up- or down-regulated genes, based on their genomic coordinates, in the healthy and patient datasets. We found that genes that are upregulated in HGPS tend to be located in the A compartment in both HGPS and WT fibroblast samples, suggesting that many expression increases do not require chromosome compartment shifts (Figure 8F–H). In contrast, a subset of the genes that are downregulated in the 0–7 HGPS fibroblasts vs. normal age- matched or adult fibroblasts also shift toward the B compartment in HGPS samples compared to healthy adults. (Figure 8F–H).

To test whether the up or downregulation of genes identified through this study relates to abnormal distribution of lamin associated domains, we compiled the genomic coordinates of these genes with published Lamin ChIP-seq and DamID-seq data (Dekker et al., 2017; McCord et al., 2013). We observe that differences between all groups are significant, with HGPS Lamin A association values markedly higher than their control counterparts (Figure 8—figure supplement 1A and B, Kruskal-Wallis p<0.001). However, we found that this shift in Lamin association is true throughout all genomic regions, with an overall dampening of the lamin association signal in HGPS patients (Figure 8—figure supplement 1C) and small regions switching from associated to dissociated from the nuclear lamina. Comparing normal fibroblast cells HGADFN168 (belonging to the father of an HGPS patient) and HFFc6 (human foreskin fibroblast), we observe that both show a characteristic bimodal distribution in LAD intensity around markedly positive (LAD) and negative (non-LAD) values (log2 Lamin/input). In contrast, LAD values for the HGPS fibroblasts HGADFN167 show a normal distribution around zero: the intensity of both types of association is reduced in HGPS cells, consistent with an overall misregulated interaction between chromosomes and the nuclear lamina (Figure 8—figure supplement 1D).

Certain key genes of interest related to osteogenesis and chondrogenic proliferation and identified as differentially regulated by transcriptomics show notable concordant alterations in compartment identity or lamina association. For example, bone morphogenic protein 4 (BMP4), which is upregulated in Progeria (Figure 7C), also shows a marked shift toward the A compartment in patient fibroblasts compared to both adult and age matched WT fibroblasts (Figure 9). In turn, Frizzled-4 (FZD4), which is upregulated in HGPS and involved in skeletal development, does not shift compartments but shows an erosion of Lamin association (Figure 9—figure supplement 1). Similarly, the gene that encodes parathyroid hormone-like hormone (PTHLH), which is downregulated in HGPS, is in a conserved A compartment in both healthy and HGPS cells but shows an increase in Lamin association in patient cells (Figure 9—figure supplement 1). Consistent with the observation that compartment shifts were more likely to be found alongside gene downregulation, we also identified a set of key genes in the mesenchymal lineage that were both downregulated and shifted toward the B compartment in HGPS (Figure 9—figure supplement 2).

![Figure 9.](https://cdn.elifesciences.org/articles/81290/elife-81290-fig9-v2.jpg)

**Figure 9.:** The gene is located in a region that shifts toward the A compartment (red) in HGPS compared to WT parent and healthy child controls.

![Figure 9—figure supplement 1.](https://cdn.elifesciences.org/articles/81290/elife-81290-fig9-figsupp1-v2.jpg)

**Figure 9—figure supplement 1.:** The data is centered on FZD4 (le) and PTHLH (right), as shown in blue highlights. Both genes localize to the A compartment (red, positive values) even though FZD4 is upregulated in Progeria and PTHLH is downregulated (see Figure 7). FZD4 shows erosion of LAD domain (yellow/blue track) in HGPS while PTHLH shows a gain of Lamina contacts in HGPS.

![Figure 9—figure supplement 2.](https://cdn.elifesciences.org/articles/81290/elife-81290-fig9-figsupp2-v2.jpg)

**Figure 9—figure supplement 2.:** Compartments shift toward negative (more B-associated) values at the locations of these genes, shown in blue highlights. Functional categories relevant to the genes (as categorized in Figures 1—6) are listed below each gene.

## Discussion

In this study, we present a comprehensive analysis of the transcriptome of HPGS patient derived fibroblasts, stratified by age, compared to their age-matched controls. Since progeria patients present with accelerated aging, we also compared this data to that derived from middle-aged and old adults. Strikingly, HPGS expression profiles do not phenocopy gene ontology analysis from either set of adult controls, suggesting an altered aging-like paradigm.

Given the critical role that Lamin A plays in nuclear structure, formation of heterochromatin, and subsequent gene silencing (Lammerding et al., 2004; Leemans et al., 2019), it is not surprising that one of the main biological processes affected in our study, as per gene ontology analysis, is DNA maintenance and epigenetics. Upregulation of genes in the HDAC family is the largest discriminator between Progeria and age-matched normal controls in the 0- to 3-year-old cohort and 4- to 7-year-old age groups, and this upregulation persists in comparisons with the adult controls. Our data suggests an upregulation of genes belonging to ontology terms such as negative epigenetic regulation of genes, chromatin silencing, DNA repair, double strand DNA repair and DNA recombination across all age comparison with young patients. Overexpression of these genes are a potential overcompensation mechanism for defects found in DNA repair (Aguado et al., 2019; Gonzalo and Kreienkamp, 2015; Komari et al., 2020; Reviewed by Misteli and Scaffidi, 2005). In older HGPS samples, downregulation of genes related to histone methylation, histone modification, chromatin modifying enzymes, and DNA recombination was also observed.

Concomitant with changes in gene expression of epigenetic factors, Progeria fibroblasts show alterations in chromosome structure, as has been previously observed (McCord et al., 2013). The increased resolution and clarity of Hi-C data presented here enables us to describe these alterations more clearly. Spatial compartmentalization is weakened in Progeria patients with increasing passages consistent with microscopically observed loss of heterochromatin (Goldman et al., 2004). Unlike compartments, topologically associating domain (TAD) boundaries are preserved during in Progeria cells, even at higher passages. When we compare gene expression changes to chromosome structure changes, we observe that many genes consistently upregulated across Progeria patients are in the open, A compartment across all Hi-C samples, suggesting that these gene expression alterations are not associated with dramatic chromosome structural change. Downregulated genes are more likely to exhibit switching into the B compartment in Progeria patients. We find that certain genes relevant to the mesenchymal lineage show gene expression changes that are concordant with compartment switches and lamin association changes. It is possible that these changes are more directly influenced by mutant lamin and lead to downstream effects on genes without observed chromosome structure changes.

### A compromised transcriptional landscape, related to developmental milestones, points towards a compromised mesenchymal stem cell niche

We further describe up and down regulated biological function clusters that could play a detrimental role in bone, fat, joint and vascular homeostasis. It has been proposed that progerin accumulation in the nucleus results in a defect in the mesenchymal stem cell lineage which gives rise to osteoblasts, chondrocytes, adipocytes, pericytes, and myocytes (Reviewed by Andrzejewska et al., 2019). Overall, our results are in concordance with previous reports of transcriptional misregulation in mesenchymal lineages (Csoka et al., 2004), but the age group comparisons we present here further refine these observations to a temporal effect on lineage commitment.

iPSC models in which HGPS fibroblasts were reprogrammed to stem cells, and further differentiated into mesenchymal stem cells lineages were characterized by nuclear dysmorphia and increased DNA damage, but resulted in confounding results on differentiation, showing either limited differentiation potential, or no significant changes (Crasto and Di Pasquale, 2018; Xiong et al., 2013; Zhang et al., 2011). Interestingly, the most common finding in HGPS-derived iPSCs further differentiated into other lineages is premature senescence and the presence of progerin and misshapen nuclei (Reviewed by Lo Cicero and Nissan, 2015). In a more direct approach, overexpression of progerin in umbilical cord derived MSCs and other MSC systems resulted in a reduced capacity of differentiation into chondrogenic, osteogenic and adipogenic capacity in vitro (Mateos et al., 2013) and deficient proliferation and migration (Pacheco et al., 2014). In the context of these collective findings, our age-stratified gene expression comparisons in fibroblasts may shed light on whether this abnormal cell fate regulation occurs predominantly in a particular lineage.

### Failed arrest of chondrocyte hypertrophy as a potential mechanism of MSC depletion in HGPS

Transcriptional upregulation of several members of the WNT5a signaling cascade and downregulation of expression of PTHLH, in early age comparisons described in this study, point to an essential defect in early endochondral ossification control and osteogenesis. Specifically, WNT signaling has been previously implicated as a connection between progeria-like syndromes and a defective deposition of extra cellular matrix, essential in bone development (Andrade et al., 2017; Green et al., 2015; Hernandez et al., 2010). Not unlike the phenotypes observed in HGPS patients, bone defects are also present in murine models for HGPS, with young mice (4-week-old) showing decreased trabecular thickness and number, bone volume and decreased mineral density (Hernandez et al., 2010). Not surprisingly, murine pre-osteoblasts forced to express mouse progerin failed to mineralize and show decreased levels of Runx2 expression and alkaline phosphatase upon osteoblastic induction (Tsukune et al., 2019). Further, Lamin A knockdown inhibits osteoblast proliferation and impairs osteoblast differentiation in an MSC in vitro differentiation model (Rauner et al., 2009).

Unlike other MSC fates, like adipogenesis, which occurs downstream of a positive energy intake all through life, bone formation occurs in a carefully orchestrated manner, at specific timepoints during development and early life. Secondary endochondral ossification that occurs in long bones like the humerus and femur, initiate in early childhood, activate intermittently, and finalize with the fusion of the growth plate during the teenage years (Diméglio et al., 2005; Xie and Chagin, 2021; Zoetis et al., 2003). This process is tightly regulated by several signaling networks aimed at balancing longitudinal growth of the bone with maintenance of precursor cells, like MSCs and quiescent chondrocytes. The transcriptional repression of PTHLH and upregulation of WNT5a in this niche would result in early depletion of the latter, as cells continue down a pathway of chondrocyte proliferation and hypertrophy unimpeded (Bradley and Drissi, 2010; Olsen et al., 2000; Usami et al., 2016). The deficit in clavicular development in HPGS patients could provide some insight as to the spatiotemporal consequences of MSC/chondrocyte pool depletion. The clavicle is unique because while it is the first bone to start ossification during the embryonic period (Ogata and Uhthoff, 1990), it is the last to complete the process. In early events, around the fifth week of gestation, the two primary ossification centers, formed from mesenchymal tissues, fuse to form the middle of the clavicle. The complete ossification of the clavicular epiphysis occurs via endochondral ossification during the teenage years, with medial ossification beginning at the onset of puberty (Ferguson and Scott, 2016; Langley, 2016). In turn, bone deposition at the terminal ossification center, must occur in adolescents between 11 and 16 years of age, for the process to successfully proceed to epiphyseal plate ossification in early adulthood. (Schulz et al., 2008). Taken together, our observations point towards a ‘fail to arrest’ phenotype that results in over-commitment towards the hypertrophic chondrocyte lineage in very young HGPS patients. We hypothesize that this results in a premature depletion of the chondro-osteoprogenitor pool and, at later stages, of the bone marrow-derived mesenchymal stem cells that feed into this niche later in life result in the incomplete endochondral ossification of the claviculae of HGPS patients (Video 1).

![Video 1.](https://cdn.elifesciences.org/articles/81290/elife-81290-video1.mp4.jpg)

### Deficient repair responses exacerbate the depletion of tissue resident MSC pools

A secondary function of tissue resident MSCs is to aid in repair during wounding and disease.

Our data shows that dermal fibroblasts derived from HPGS patients present with abnormal repair, including downregulated signatures of wound healing, hemostasis, and BMP signaling. These observations recapitulate previous reports of HGPS patient-derived skin precursors, which can differentiate intro fibroblasts and smooth muscle cells (smooth muscle alpha actin positive – myofibroblasts). In the precursor stage, these cells express low levels of progerin in vivo and in vitro, but differentiation into the lineages increases progerin expression and deposition in the nucleus (Wenzel et al., 2012). In concordance with our findings, a progeria murine model, deficient in the downstream processing of lamin A, shows abnormal skin wound repair, with prolonged time to wound closure, poor vasculogenic signaling and angiogenesis, which includes a limited mobilization of bone-marrow derived progenitor cells (Butala et al., 2012). Related to this phenotype, the LMNAΔ9 murine progeria model for HPGS show a significant decrease in postnatal fibroblast proliferation, with accelerated senescence levels in cell lines derived from kidney, lung, skin, and skeletal muscle (Hernandez et al., 2010). Further, a decreased epidermal population of adult stem cells was observed in another murine model of HGPS (Rosengardten et al., 2011), which are also deficient for skin wound repair.

Overall, growth, development, and maintaining homeostasis place a considerable burden on the mesenchymal stem cell pool and its many lineages. Under a paradigm of biology of priority during development the organism’s structural integrity in the shape of bones and joints, the homeostasis of blood microvessels – regulated by pericytes – should take precedence to fat deposition (Figure 10A).

![Figure 10.](https://cdn.elifesciences.org/articles/81290/elife-81290-fig10-v2.jpg)

**Figure 10.:** HGPS affects differentiation commitment and subsequent biology of priority during early development, which results in premature depletion of MSC pools.

We propose that these defects in repair in Progeria patients strain the mesenchymal stem cell pools from which repair reactive stroma originates, which have been characterized as both pools of CD44/CD99-positive cells in glandular tissues and as pluripotent cells located at the pericyte position (Crisan et al., 2008; Kim et al., 2014). Interestingly, it has been reported that normal fibroblast cell lines contain a subset of pluripotent MSCs, indistinguishable from those derived from the bone marrow (Denu et al., 2016) and it is established that normal MSCs lose proliferative and differentiation potential within a few passages when cultured in vitro. This phenomenon has been correlated with a defect in lamin A maturation that leads to cellular senescence (Bellotti et al., 2016), which is similar to the terminal differentiation into wound-repair-myofibroblasts resulting from the TGF-beta induction of prostate resident MSCs (Kim et al., 2014). HPGS fibroblasts experience an increased rate in apoptosis, with subsequent cell divisions, concomitant with mutant Lamin A accumulation (Bridger and Kill, 2004), and chronic DNA damage that lead to premature senescence (Wheaton et al., 2017),which could be indirect evidence of early depletion of the MSC pool in these cell lines. (Figure 10B).

Related to later differentiation events, the depletion of microvasculature resident MSCs occurring as a result of chronic, deficient wound repair would carry a severe impact to adipogenesis. Cells at the pericyte position have been characterized as the primary source for adipocytes in vivo (Traktuev et al., 2008; Zannettino et al., 2008). These cells, which are CD44, CD90 double positive, phenocopy the pluripotency of tissue resident mesenchymal stem cells, and are able to differentiate into repair-like myofibroblasts expressing smooth muscle alpha actin (Merfeld-Clauss et al., 2017). Coupled with a preadipocyte depletion phenotype, lipodystrophy in HGPS has also been experimentally induced by the introduction of progerin expression into a subset of pre adipogenic cells in mice, which led to fibrosis, senescence, and macrophage infiltration, with the ultimate result of white fat depletion (Revêchon et al., 2017).

### The fibroblast as a sentinel of general mesenchymal lineage health

The criticism can be made that it is a stretch to make hypotheses about different mesenchymal stem cell pools based only on gene expression from dermal fibroblasts. This is indeed a limitation that must be considered, but primary samples of other mesenchymal lineage tissues from HGPS patients are not available, and there is evidence of interplay between fibroblasts and the MSC lineage. After birth, the bone marrow mesenchymal stem cell niche is in close synergy with pools of fibroblasts (LeBleu and Neilson, 2020; Soundararajan and Kannan, 2018), tissue resident mesenchymal stem cells (El Agha et al., 2017) and pericytes (Lamagna and Bergers, 2006). Since these cell pools are in flux, and can compensate for each other under duress (Di Carlo and Peduto, 2018; Direkze et al., 2004; Ozerdem et al., 2005; San Martin et al., 2014), comparing the global transcriptional status of fibroblasts between a patient cohort and its aged-matched controls can provide an insight into potential systemic deficits and compensatory mechanisms at play.

### Ideas and speculation

Overall, the cohorts of biological processes that we observe to be misregulated across different age groups of Progeria patients lead us to speculate the impact of this misregulation across a series of events in development, which will warrant further investigation:

### Conclusion

Our comprehensive analysis of previously published and newly generated RNA-seq datasets for Progeria fibroblast cells enabled careful age-stratified comparisons. Comparing young children and teenagers with Progeria to age-matched controls, middle-aged, and elderly adults, we find misregulated genes which suggest important defects in cell and tissue repair biology, epigenetics, metabolism (calcium, lipids), and other functions important to the mesenchymal cell lineage. Our comparisons show altered regulation of chondrocyte commitment genes in the fibroblasts of Progeria patients who are at the age of postnatal ossification compared to typically developing age-matched controls. Interestingly, the Progeria gene expression patterns are distinct from older adult fibroblast expression patterns, emphasizing that this disease does not simply mimic normal aging. While genome spatial compartmentalization in these patients is overall weakened, much of the gene misregulation occurs in regions that do not change their compartment status or lamin association. However, a few key misregulated genes in the osteogenic and adipogenic lineage show a clear concordant switch in spatial compartmentalization or lamin association, suggesting that some alterations in these pathways may result directly from the influence of progerin on chromosome structure.

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
      <td>Biological sample (Homo sapiens)</td>
      <td>Purified RNA</td>
      <td>Coriell Institute</td>
      <td>AG01178</td>
      <td>Male 20 y/o</td>
    </tr>
    <tr>
      <td>Biological sample (Homo sapiens)</td>
      <td>Purified RNA</td>
      <td>Coriell Institute</td>
      <td>AG03198</td>
      <td>Female 10 y/o</td>
    </tr>
    <tr>
      <td>Biological sample (Homo sapiens)</td>
      <td>Purified RNA</td>
      <td>Coriell Institute</td>
      <td>AG06917</td>
      <td>Male 3 y/o</td>
    </tr>
    <tr>
      <td>Biological sample (Homo sapiens)</td>
      <td>Purified RNA</td>
      <td>Coriell Institute</td>
      <td>AG07493</td>
      <td>Female 2 y/o</td>
    </tr>
    <tr>
      <td>Biological sample (Homo sapiens)</td>
      <td>Purified RNA</td>
      <td>Coriell Institute</td>
      <td>AG08466</td>
      <td>Female 8 y/o</td>
    </tr>
    <tr>
      <td>Biological sample (Homo sapiens)</td>
      <td>Purified RNA</td>
      <td>Coriell Institute</td>
      <td>AG10578</td>
      <td>Male 17 y/o</td>
    </tr>
    <tr>
      <td>Biological sample (Homo sapiens)</td>
      <td>Purified RNA</td>
      <td>Coriell Institute</td>
      <td>AG10677</td>
      <td>Male 4 y/o</td>
    </tr>
    <tr>
      <td>Biological sample (Homo sapiens)</td>
      <td>Purified RNA</td>
      <td>Coriell Institute</td>
      <td>AG11572</td>
      <td>Female 2 y/o</td>
    </tr>
    <tr>
      <td>Biological sample (Homo sapiens)</td>
      <td>Purified RNA</td>
      <td>Coriell Institute</td>
      <td>GM01178</td>
      <td>Male 20 y/o</td>
    </tr>
    <tr>
      <td>Biological sample (Homo sapiens)</td>
      <td>Purified RNA</td>
      <td>Coriell Institute</td>
      <td>GM01972</td>
      <td>Female 14 y/o</td>
    </tr>
    <tr>
      <td>Biological sample (Homo sapiens)</td>
      <td>Purified RNA</td>
      <td>Coriell Institute</td>
      <td>AG11513</td>
      <td>Female 8 y/o</td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>HGPS human primary dermal fibroblast</td>
      <td>Progeria Research Foundation (PRF) Cell and Tissue Bank</td>
      <td>HGADFN167</td>
      <td>8-year-old male progeria patient</td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>WT human primary dermal fibroblast</td>
      <td>Progeria Research Foundation (PRF) Cell and Tissue Bank</td>
      <td>HGADFN168</td>
      <td>Father of progeria patient</td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>HGPS human primary dermal fibroblast</td>
      <td>Coriell Institute</td>
      <td>AG11513</td>
      <td>8-year-old female progeria patient</td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>WT human primary dermal fibroblast</td>
      <td>Coriell Institute</td>
      <td>AG03257</td>
      <td>Mother of progeria patient</td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>WT human primary dermal fibroblast</td>
      <td>Coriell Institute</td>
      <td>GM08398</td>
      <td>8-year-old male healthy child</td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>HindIII</td>
      <td>New England Biolabs</td>
      <td>R0104L</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>DpnII</td>
      <td>New England Biolabs</td>
      <td>R0543L</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>T4 DNA Ligase</td>
      <td>Invitrogen</td>
      <td>15224041</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>DNA Polymerase I Klenow Fragment</td>
      <td>New England Biolabs</td>
      <td>M0210L</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>T4 DNA Polymerase</td>
      <td>New England Biolabs</td>
      <td>M0203L</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>Biotin-dATP</td>
      <td>Invitrogen</td>
      <td>19524016</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Arima-HiC +Kit</td>
      <td>Arima Genomics</td>
      <td>Mammalian Cell Lines Protocol (A160134 v01)</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>NEBNext Ultra II kit</td>
      <td>New England Biolabs</td>
      <td>E7645S</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>NEBNext Multiplex Oligos for Illumina (Index Primers Set 4)</td>
      <td>New England Biolabs</td>
      <td>E7730S</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>NEBNext Multiplex Oligos for Illumina (Index Primers Set 1)</td>
      <td>New England Biolabs</td>
      <td>E7335S</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>BBDuk</td>
      <td>https://github.com/kbaseapps/BBTools</td>
      <td></td>
      <td>RRID:SCR_016968</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>STAR aligner</td>
      <td>https://github.com/alexdobin/STAR</td>
      <td></td>
      <td>RRID:SCR_004463</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>HTSeq-Counts</td>
      <td>https://github.com/simon-anders/htseq</td>
      <td></td>
      <td>RRID:SCR_011867</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>DESeq2</td>
      <td>https://bioconductor.org/packages/release/bioc/html/DESeq2.html</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>cMapping</td>
      <td>https://github.com/dekkerlab/cMapping (Lajoie et al., 2015; Lajoie and Oomen, 2015)</td>
      <td></td>
      <td>v1.0.6; Bryan Lajoie</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>cWorld-dekker</td>
      <td>https://github.com/dekkerlab/cworld-dekker (Lajoie and Venev, 2019)</td>
      <td></td>
      <td>v0.41.1; Bryan Lajoie</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>ComBat-seq</td>
      <td>https://github.com/zhangyuqing/ComBat-seq (Zhang et al., 2020a; Zhang et al., 2020b)</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

### RNA-seq

Ten micrograms of purified RNA from several progeria cell samples were acquired from the Coriell Institute (Camden, NJ) as follows: AG06917 (HGPS. Male 3 y/o), AG10578 (HGPS. Male 17 y/o), AG11572 (HGPS. Female 2 y/o), AG10677 (HGPS. Male 4 y/o), AG08466 (HGPS. Female 8 y/o), AG03198 (HGPS. Female 10 y/o), AG07493 (HGPS. Female 2 y/o), AG01178 (HGPS. Male 20 y/o), AG11513 (HGPS. Female 8 y/o), GM01972 (HGPS. Female 14 y/o), GM01178 (HGPS. Male 20 y/o). After internal quality control upon receipt, RNA-seq library construction and sequencing of two technical replicates was carried out by Genewiz (South Plainfield, NJ). Further, previously published RNA-seq datasets from HPGS fibroblasts and normal controls were included in the study (Appendix 1—tables 1–3; Fleischer et al., 2018; Ikegami et al., 2020; Köhler et al., 2020; Mateos et al., 2018).

### RNA-seq data processing

The fastq reads were first processed with BBDuk tool (https://github.com/kbaseapps/BBTools), performing adapter trimming with parameters “ktrim = r k=23 mink = 11 hdist = 1”. Adapter trimmed reads were processed for quality trimming using the BBDuk tool to discard reads with quality score lower than 28 (parameters “qtrim = r trimq = 28”). Following the adapter and quality trimming steps, the reads were aligned to the reference genome hg19 using STAR aligner (https://github.com/alexdobin/STAR) with both ‘--outFilterScoreMinOverLread’ and ‘ --outFilterMatchNminOverLread’ parameters set to 0.2. Finally, the mapped reads were sorted based on genomic coordinates and feature count was performed with HTSeq-Counts (https://github.com/simon-anders/htseq).

### Batch effect removal

Since the RNA-seq files used in this study were generated in different laboratories, using different technologies, the raw gene counts produced by HTSeq-Counts suffer from batch effect. To mitigate that issue, the raw counts are batch effect adjusted using the ComBat-seq tool (https://github.com/zhangyuqing/ComBat-seq). For this purpose, files from the same laboratory are assigned the same batch number. In addition, the sex and status of the samples are provided as the biological covariates to the ComBat-seq tool to preserve that signal in the adjusted data.

### Differential expression analysis

Differential gene expression analysis was performed between different groups of diseased and healthy samples using DESeq2 (https://bioconductor.org/packages/release/bioc/html/DESeq2.html) tool. HGPS samples from Young (0–7 y/o) or teenage (13+y/o) patients were compared to age matched (AM), middle aged (M), and old (O) control samples (Table 1—source data 1). Further, to correlate gene expression profiles with known patient survival statistics, comparisons were further refined by stratifying early infancy progeria patients (0–3 years old) and older children (4–7 years old), comparing those populations to age matched, middle aged and old control samples, as before (Table 2—source data 1).

### Gene ontology analysis

Genes defined as up/down regulated for each of the age group comparisons, were considered for gene ontology analysis based on an FDR adjusted p-value cutoff of 0.001. These gene lists, in turn, were then analyzed using Metascape (Zhou et al., 2019). Metascape output files were manually clustered into gene ontology themes, observed throughout the analysis. Gene lists derived from this manual clustering were then visualized via heatmaps to facilitate comparisons among age groups.

### Gene expression heatmap plotting

To plot expression of specific genes across different samples as a heatmap, the batch adjusted counts for all the genes for each sample were log2 normalized with a pseudo count of 1. The expression of specific genes across specific samples was then extracted and Z-score normalization was performed for each of the genes. Finally, the Z-score normalized values were plotted using the Seaborn python package as a heatmap. (https://seaborn.pydata.org/).

### DamID-seq data processing

All the DamID-seq data was processed as previously reported (Leemans et al., 2019), with modifications in the trimming step. Briefly, the bwa mem (https://github.com/lh3/bwa, Li, 2022) tool was used to map gDNA reads starting with GATC to a combination of hg19 reference genome with a ribosomal model. For further processing, only the mapped reads having a mapping quality of at least 10 were considered as GATC fragments. Next, the reads were combined into the bins of 40 kb resolution depending on the middle of the GATC fragments and then scaled to 1 M reads. For normalization, log2-ratio of the scaled target over the scaled Dam-only bins was calculated with a pseudo count of 1.

### Cell culture

Human primary dermal fibroblast cell lines were obtained from The Progeria Research Foundation (PRF) Cell and Tissue Bank (HGPS: HGADFN167 and healthy adult: HGADFN168). Dermal fibroblasts (HGPS: AG11513, healthy adult: AG03257, and healthy child GM08398) were purchased from Coriell Institute (Camden, NJ). Cells were grown in DMEM (Gibco) supplemented with 15% FBS (Corning), 1% Pen-strep (Gibco), and 1% L-glutamine (Gibco). Cells were passaged at a density of 80%.

### Chromosome conformation capture (Hi-C)

Hi-C experiments were performed according to standard protocols (Golloshi et al., 2018). The starting material was comprised of skin fibroblasts of parents of HGPS patients (Mother AG03257, Father HGADFN168), a healthy age matched child (GM08398) and two HGPS patient fibroblast samples (HGADFN167 and AG11513). Further, HGADFN168 and HGADFN167, belonging to a parent-child matched cells were analyzed both at an early and late passage: p12-27 and p12-19, respectively.

Briefly, ~5 million cells were fixed with 1% formaldehyde, suspended in cell lysis buffer for permeabilization, and homogenized by douncing. Crosslinked chromatin was digested overnight with HindIII (HGADFN167 and HGADFN168) or DpnII (HGADFN167, HGADFN168, AG03257 and AG11513). GM08398 cells were processed using the Arima-HiC +Kit from Arima Genomics following the protocol for Mammalian Cell Lines (A160134 v01). Sticky ends were filled in with biotin-dATP (Invitrogen), and the blunt ends of interacting fragments were ligated together. DNA was purified by two phenol-chloroform extractions and ethanol precipitation. Biotin-dATP at unligated ends was removed, and the DNA was sheared to a target size of 200–400 bp by a Covaris sonicator (Covaris, M220). DNA between 100–400 bp was selected for using AMPure XP beads (Beckman Coulter). Biotinylated DNA was pulled down using streptavidin coated magnetic beads and prepared for multiplex sequencing on an Illumina platform using the NEBNext Ultra II kit (NEB, E7645S). All end preparation, adaptor ligation, and PCR amplification steps were carried out on bead bound DNA libraries. Sequencing was carried out on Illumina HiSeq 3000 or NovaSeq platforms with 75 bp or 150 bp paired end reads. All Hi-C data statistics are presented in Appendix 1—table 4.

### Analysis of Hi-C data

Sequencing reads were mapped to the reference human genome hg19, filtered, and iteratively corrected using previously published pipelines (Imakaev et al., 2012), available on github (https://github.com/dekkerlab/cMapping). Publicly available tools (https://github.com/dekkerlab/cworld-dekker) were used to produce Hi-C heatmaps at 2.5 Mb and 250 kb resolution and to perform principal component analysis (using the matrix2compartment script) to generate compartment tracks at 250 kb resolution, assigning A and B compartments to positive and negative PC1 values, respectively. Values from replicate experiments were averaged, by bin, to produce the final compartment track. TAD boundary strength analysis was carried out using the insulation score approach (Crane et al., 2015) (matrix2insulation) from this cworld package with 500 kb insulation square using 40 kb resolution contact maps.

### ChIP-seq data and processing: Lamin associated domain analysis

Raw LMNA ChIP-seq data was obtained from the NCBI Gene Expression Omnibus (GEO) under accession number GSE41764 (McCord et al., 2013). For comparison, DamID-seq for the fibroblast line HFFc6 (van Steensel Lab, Netherlands Cancer Institute) was obtained from the 4D Nucleome data portal (Dekker et al., 2017; Reiff et al., 2021), through the bio sample identifier 4DNBSR7TC87A.

The fastq reads were first processed for adapter and quality trimming with the help of BBDuk tool. The reads were then aligned to the hg19 reference genome using STAR aligner. Finally, both the target and input mapped reads were binned at 40 kb resolution and log2-ratio of the target over the input bins was calculated using the ‘bamCompare’ function of deepTools with parameters “--operation log2 -bs 40000 --ignoreDuplicates --minMappingQuality 30 --scaleFactorsMethod SES --effectiveGenomeSize 2864785220”.
