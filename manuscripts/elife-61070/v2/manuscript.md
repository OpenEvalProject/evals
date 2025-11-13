# EKLF/KLF1 expression defines a unique macrophage subset during mouse erythropoiesis

## Authors

- Kaustav Mukherjee<sup>1</sup> ([ORCID: 0000-0002-7057-0880](https://orcid.org/0000-0002-7057-0880))
- Li Xue<sup>1</sup>
- Antanas Planutis<sup>1</sup>
- Merlin Nithya Gnanapragasam<sup>1</sup>
- Andrew Chess<sup>1</sup>
- James J Bieker<sup>1</sup> ([ORCID: 0000-0001-5128-7476](https://orcid.org/0000-0001-5128-7476)) †

### Affiliations

1. Department of Cell, Developmental, and Regenerative Biology, Mount Sinai School of Medicine New York, NY United States
2. Black Family Stem Cell Institute New York, NY United States
3. Tisch Cancer Institute New York, NY United States
4. Mindich Child Health and Development Institute, Mount Sinai School of Medicine New York, NY United States

† Corresponding author

## Abstract

Erythroblastic islands are a specialized niche that contain a central macrophage surrounded by erythroid cells at various stages of maturation. However, identifying the precise genetic and transcriptional control mechanisms in the island macrophage remains difficult due to macrophage heterogeneity. Using unbiased global sequencing and directed genetic approaches focused on early mammalian development, we find that fetal liver macrophages exhibit a unique expression signature that differentiates them from erythroid and adult macrophage cells. The importance of erythroid Krüppel-like factor (EKLF)/KLF1 in this identity is shown by expression analyses in EKLF-/- and in EKLF-marked macrophage cells. Single-cell sequence analysis simplifies heterogeneity and identifies clusters of genes important for EKLF-dependent macrophage function and novel cell surface biomarkers. Remarkably, this singular set of macrophage island cells appears transiently during embryogenesis. Together, these studies provide a detailed perspective on the importance of EKLF in the establishment of the dynamic gene expression network within erythroblastic islands in the developing embryo and provide the means for their efficient isolation.

## Introduction

Maturation of red blood cells in vivo occurs within specialized niches called ‘erythroblastic islands’ that consist of a central macrophage surrounded by erythroid cells at various stages of differentiation (Chasis and Mohandas, 2008; Hom et al., 2015; Klei et al., 2017; Manwani and Bieker, 2008; Yeo et al., 2019). Macrophages aid in providing cytokines for erythroid growth and differentiation, iron for the demands of hemoglobinization, and ultimately phagocytic and DNase functions that consume the extruded, condensed red cell nuclei during enucleation. The island is held together by specifically paired erythroid/macrophage cell surface protein interactions that, in some cases, are cell-type specific (Chasis and Mohandas, 2008; de Back et al., 2014; Hampton-O'Neil et al., 2020; Manwani and Bieker, 2008; Seu et al., 2017). The ultimate result is a highly effective and efficient means of reticulocyte formation and release.

Recovery from erythropoietic stress is impaired when macrophages are defective (Chow et al., 2013; Jacobsen et al., 2015; Liao et al., 2018; May and Forrester, 2020; Ramos et al., 2013; Sadahira et al., 2000), supporting a physiological role for island macrophages in erythroid biology. Altered islands are associated with poor prognosis of myelodysplastic patients (Buesche et al., 2016). Although studies suggest that even an 80% decrease in mouse resident macrophage levels still enables a normal recovery from stress (Ulyanova et al., 2016), this response is effectively aided by differentiation of monocytes to macrophages after recruitment to the splenic red pulp (Liao et al., 2018). As steady-state erythropoiesis appears normal in mice with impaired macrophages, the precise role of macrophage in all aspects of erythropoiesis is not fully resolved (Korolnek and Hamza, 2015).

Erythroid Krüppel-like factor (EKLF; KLF1 [Miller and Bieker, 1993]) is a zinc finger hematopoietic transcription factor that plays a global role in the activation of genes critical for genetic control within the erythroid lineage (reviewed in Gnanapragasam and Bieker, 2017; Siatecka and Bieker, 2011; Tallack and Perkins, 2010; Yien and Bieker, 2013). Genetic ablation studies in the mouse show that EKLF is absolutely required for completion of the erythroid program as EKLF-/- embryos are embryonic lethal at E15 due to a profound ß-thalassemia and the low to virtually nonexistent expression of erythroid genes of all categories. At E13.5, they are anemic and their pale fetal liver (FL) is already distinct in EKLF-/- compared to their EKLF+/+ and EKLF+/- littermates. However, EKLF also plays a crucial role in a subset of macrophage cell function, particularly within the erythroblastic island (Porcu et al., 2011; Xue et al., 2014). Within the island progeny, it directly activates Icam4 in the erythroid compartment and activates Vcam1 in the macrophage compartment (Xue et al., 2014). Together, Icam4 and Vcam1 enable a two-pronged adhesive intercellular interaction to occur with their respective integrin partners on the opposite cell type. In the absence of EKLF, these interactions decrease and the integrity of the island is compromised, contributing to the abundance of nucleated, unprocessed cells seen in circulation (Gnanapragasam et al., 2016). In addition, loss of Dnase2 expression in the macrophage yields a cell engorged with undigested nuclei that triggers IFNß induction (Kawane et al., 2001; Manchinu et al., 2018; Nagata, 2007; Porcu et al., 2011; Yoshida et al., 2005).

Independent evidence for EKLF expression in erythroblastic island macrophage has been attained recently by two sets of studies. One study analyzed EpoR+F4/80+ macrophage, which are present in erythroblastic islands and are negative for Ter119, showing that these cells are highly enriched for EKLF (Li et al., 2019). In the second study, a pure population of macrophages (Lopez-Yrigoyen et al., 2018) derived from a human induced pluripotent stem cell (iPSC) line carrying an inducible KLF1-ERT2 transgene (Yang et al., 2017) was used to demonstrate that activation of KLF1 in these macrophages altered them to an island-like phenotype as assessed by an increase in expression of erythroblastic island-associated genes and cell surface markers, an increase in phagocytic activity, and an increase in ability to support the maturation and enucleation of umbilical cord blood-derived cells (Lopez-Yrigoyen et al., 2019).

The strongest evidence for a specific macrophage subtype in the erythroblastic island comes from the mouse, where F4/80 antigen and Forssman glycosphingolipid expression, but not Mac1 expression, are enriched in these cells (reviewed in Manwani and Bieker, 2008). Island macrophages are also larger than peritoneal macrophages and exhibit a high level of phagocytic activity. Although molecular expression differences between macrophage subsets have been observed (Ginhoux et al., 2016; Hom et al., 2015; Lavin et al., 2014; Seu et al., 2017), this has not been addressed in the context of early erythroblastic island development in the FL. Given the compelling observations implicating EKLF in island macrophage biology, we characterized the molecular expression of the F4/80+ island macrophages in the developing mouse FL, determined the EKLF-dependent gene expression program in island macrophages using two independent approaches, and then established its role in specifying a unique cellular identity for this cell type by a single-cell analysis approach.

## Results

### Global gene expression in E13.5 FL macrophages reflects both erythroid and macrophage properties

We dissected E13.5 FLs and fluorescence activated cell (FACS)-sorted F4/80+ cells to obtain a pure population of FL macrophages (Figure 1—figure supplement 1). Approximately 9% of the total cells in a wild-type FL are F4/80+ (Figure 1—figure supplement 1A). The sorted singlets were monitored after cytospin to determine whether they were free of contaminating erythroid cells (Figure 1—figure supplement 1B). We found that >95% of the sorted F4/80+ population are single cells and free of any attached or engulfed erythroid cells or nuclei (Figure 1—figure supplement 1C). We then used this pure population of F4/80+ FL macrophages to determine their global gene expression profile using RNA-Seq of biological triplicates.

We compared the global gene expression of E13.5 FL F4/80+ macrophages with two sets of gene expression data. One was from primary long-term cultures of extensively self-renewing erythroblasts (ESREs) isolated from FL that can be differentiated to form mature erythroid cells (England et al., 2011; Gnanapragasam et al., 2016). The second was from adult spleen F4/80+ macrophage (Lavin et al., 2014), which is also an in vivo site of erythroblastic islands (Chow et al., 2013; Jacobsen et al., 2015; Ramos et al., 2013). Hierarchical clustering of the gene expression profile from these cell types shows that the FL macrophages cluster closer to differentiating ESREs than to splenic red pulp macrophages (Figure 1A), suggesting that the FL macrophages have an early erythroid-like gene expression profile rather than a mature macrophage-like profile. Yet at the same time we find using principal component analysis (PCA) that these cell types cluster separately, indicating that each has a unique identity (Figure 1B). Further, we find that for a list of macrophage and erythroid markers (Figure 1—source data 1, Murray and Wynn, 2011; Ng and Wood, 2014), FL macrophages have intermediate expression of both sets of markers compared to ESREs or spleen macrophages (Figure 1C). Together, these data suggest that FL F4/80+ macrophages essentially have dual characteristics of erythroid and macrophage-like cell populations in terms of marker expression but still form their own unique subset.

![Figure 1.](https://cdn.elifesciences.org/articles/61070/elife-61070-fig1-v2.jpg)

**Figure 1.:** (A) Hierarchical clustering dendrogram using scaled Z-scores based on the expression of the top 10,000 highly expressed genes is shown for individual RNA-Seq biological replicates from each cell type (source data: Figure 1—source data 1). (B) Principal component analysis of the cell types is plotted showing principal components 1 and 2 for each biological replicate (source data: Figure 1—source data 1). (C) Macrophage-specific or erythroid-specific marker expression in the cell types is shown, with replicates averaged together (source data: Figure 1—source data 3). (D) k-means clustering of individual RNA-Seq biological replicates of the different cell types (ESREs, Erythr; fetal liver, FL; spleen, Spl) by log2 FPKM displayed as a heatmap (source data: Figure 1—source data 4). Flower bracket indicates the gene cluster with enriched expression in F4/80+ FL macrophages. (E) Heatmap of only the uniquely expressed genes in F4/80+ FL macrophages that define the signature genes of this cell type (source data: Figure 1—source data 2). A few representative signature gene names are displayed.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/61070/elife-61070-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) Gating strategy used to stringently sort singlets that are F4/80+ is shown from unstained (no antibody [Ab]) or treated (anti-F4/80 Ab) fetal liver cells from EKLF+/+ E13.5 fetal livers. (The same approach was used for EKLF-/- cell sorting in Figure 3A.) (B) FACS-sorted cells using the strategy above were cytospun on a slide and observed after May-Grunwald-Giemsa staining for singlets, doublets, or >3 cells. 25 µm scale bars are indicated. (C) Quantification of data from (B) (source data: Figure 1—figure supplement 1—source data 1 ).

### Cell-type-specific expression of a subset of genes in FL macrophages provides them with a distinct cellular identity

Since our PCA analysis showed that FL macrophages have unique characteristics compared to ESREs and spleen macrophages, we performed k-means clustering of the RNA-Seq datasets of the three cell types (Figure 1D). We find a cluster that contains a set of 1291 genes that are almost exclusively expressed in FL macrophages (Figure 1D – indicated by flower bracket). Neither ESREs nor spleen macrophages have a similar set of cell-type-specific gene expression as evident from the lack of clusters showing genes only expressed in these cell types (Figure 1D). This again suggests that FL macrophages may have a distinct cellular identity and likely possess unique functions compared to other macrophage types. We selected a set of 304 genes that were only expressed in FL macrophages and not in ESREs or spleen macrophages, and refer to them as ‘signature genes’ (Figure 1E, Figure 1—source data 2).

To determine whether signature genes are a random subset of genes or whether they indeed have biological significance with respect to FL macrophage function, we performed gene ontology (GO) analysis and filtered the results down to the unique GO terms using REVIGO (Supek et al., 2011; Supplementary file 1). We find that the signature genes are involved in four major biological processes: circulatory system development, tube development (vasculature development), locomotion and motility, negative regulation of blood coagulation, and cell adhesion (Supplementary file 1). Of these, cell adhesion between erythroblast island macrophages and developing erythroblasts during erythropoiesis is known to be an important function of a subset of FL macrophages (Xue et al., 2014). The additional GO categories point to novel biological or developmental roles for FL macrophages.

### Loss of EKLF leads to significantly altered gene expression in F4/80+ FL macrophages

As a prelude to analyzing the effects of EKLF on F4/80+ macrophage, we directly verified EKLF protein expression and find that it is expressed in the F4/80+ macrophage as judged by immunofluorescence (Figure 2A). Consistent with our previous data, not all F4/80+ cells are EKLF+, and vice versa (Figure 2A, B). Additional support for macrophage specificity of EKLF expression comes from a published RNA-Seq analyses of an extensive series of staged, sorted cells in the FL (Mass et al., 2016). Mature macrophage cells (ckit-/CD45+/F480+/AA4.1-/CD11b+) do not exhibit EKLF expression in FL at E10.25; however, EKLF expression 6 hr later in the FL is apparent (E10.5) and robust by E12.5, where it remains high until E18.5, dropping off considerably until it is not detectable at postnatal stages in the liver (Figure 2C). As a positive control, Adgre1 (F4/80) is expressed in all samples (Figure 2D). As a negative control, EKLF is not expressed in any other tissue macrophage cell in the same study (all samples from skin, brain, kidney, and lung; Mass et al., 2016).

![Figure 2.](https://cdn.elifesciences.org/articles/61070/elife-61070-fig2-v2.jpg)

**Figure 2.:** (A) Immunofluorescence tests with anti-EKLF (white), 4′,6-diamidino-2-phenylindole (DAPI) (blue), and anti-F4/80 (red) antibodies in E13.5 fetal liver cells. (A) White arrowheads show coexpression of EKLF and F4/80 proteins in single cells (representative of over 20 EKLF+/F4/80+ cells in this field of 300 cells); red arrow shows that not all F4/80+ cells are EKLF+. (B) White arrow shows that not all EKLF+ cells are F4/80+ , as expected from the FACS data (cytoplasmic EKLF signal is expected [Quadrini et al., 2008; Schoenfelder et al., 2010]). (C) Collated RNA-Seq data (Mass et al., 2016) of sorted macrophage cells from multiple staged embryonic (E) day 10.25–16.5 fetal livers or postnatal (P) day 2–21 livers (ckit-/CD45+/F480+/AA4.1-/CD11b+; n = 24 samples) show transient and abundant Klf1 reads (UCSC Genome Browser). (D) Same analysis as (C) showing RNA-Seq reads of the gene encoding F4/80 (Adgre1) as a positive control across all samples.

As a result, we used FACS-sorted F4/80+ FL macrophage from an EKLF-/- mouse and compared its gene expression with wild-type (WT) FL F4/80+ macrophage by RNA-Seq to determine which genes are affected by the loss of EKLF. We observe that there are about half as many F4/80+ FL macrophages in EKLF-/- FL as in WT, suggesting a vital role for EKLF in FL macrophage development (Figure 3A; compare to Figure 1—figure supplement 1A). Using k-means clustering of the RNA-Seq data, we find the predominant effect is that genes are downregulated in the EKLF-/- FL macrophages (Figure 3B). This is consistent with the role of EKLF as a transcriptional activator (Miller and Bieker, 1993). We performed differential gene expression analysis using DESeq2 and found that a set of 1210 genes are significantly downregulated in the EKLF-/- FL macrophages (Figure 3C, Supplementary file 2). Using REVIGO analysis, we find that among others many of the downregulated genes are involved in cell–cell adhesion (Table 1).

![Figure 3.](https://cdn.elifesciences.org/articles/61070/elife-61070-fig3-v2.jpg)

**Figure 3.:** (A) A representative yield of cells from EKLF-/- FL sorted by F4/80 expression, used for RNA-Seq analysis, is shown (compare to WT yield in Figure 1—figure supplement 1A). (B) k-means clustering of absolute log2 FPKM of F4/80+ EKLF+/+ and F4/80+ EKLF-/-, and log2 FKPM ratio EKLF-/-(KO)/WT is displayed as a heatmap. Flower bracket indicates downregulated genes. (C) Differentially expressed genes in EKLF-/- (KO) compared to WT shown as a volcano plot (source data: Figure 3—source data 1).

**Table 1.**
 Summary of significant GO terms for the subset of genes significantly downregulated in EKLF-/- vs WT.


<table>
  <thead>
    <tr>
      <th>Term_ID</th>
      <th>Description</th>
      <th>Frequency (%)</th>
      <th>log10 p-value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>GO:0006464</td>
      <td>Cellular protein modification process</td>
      <td>16.80</td>
      <td>−6.8427</td>
    </tr>
    <tr>
      <td>GO:0032502</td>
      <td>Developmental process</td>
      <td>27.72</td>
      <td>−6.6535</td>
    </tr>
    <tr>
      <td>GO:0051179</td>
      <td>Localization</td>
      <td>26.83</td>
      <td>−5.5895</td>
    </tr>
    <tr>
      <td>GO:0030097</td>
      <td>Hemopoiesis</td>
      <td>3.96</td>
      <td>−5.5005</td>
    </tr>
    <tr>
      <td>GO:0048518</td>
      <td>Positive regulation of biological process</td>
      <td>24.84</td>
      <td>−4.1355</td>
    </tr>
    <tr>
      <td>GO:0044699</td>
      <td>Single-organism process</td>
      <td>65.98</td>
      <td>−3.6956</td>
    </tr>
    <tr>
      <td>GO:0022610</td>
      <td>Biological adhesion</td>
      <td>6.66</td>
      <td>−3.5792</td>
    </tr>
    <tr>
      <td>GO:0016043</td>
      <td>Cellular component organization</td>
      <td>27.23</td>
      <td>−3.3699</td>
    </tr>
    <tr>
      <td>GO:0008152</td>
      <td>Metabolic process</td>
      <td>51.22</td>
      <td>−3.3045</td>
    </tr>
    <tr>
      <td>GO:0071840</td>
      <td>Cellular component organization or biogenesis</td>
      <td>27.98</td>
      <td>−3.2058</td>
    </tr>
    <tr>
      <td>GO:0065007</td>
      <td>Biological regulation</td>
      <td>57.48</td>
      <td>−3.1341</td>
    </tr>
    <tr>
      <td>GO:0065008</td>
      <td>Regulation of biological quality</td>
      <td>15.62</td>
      <td>−2.4455</td>
    </tr>
    <tr>
      <td>GO:0044763</td>
      <td>Single-organism cellular process</td>
      <td>47.39</td>
      <td>−2.4259</td>
    </tr>
    <tr>
      <td>GO:0007169</td>
      <td>Transmembrane receptor protein tyrosine kinase signaling pathway</td>
      <td>2.62</td>
      <td>−2.028</td>
    </tr>
    <tr>
      <td>GO:0009791</td>
      <td>Post-embryonic development</td>
      <td>0.60</td>
      <td>−1.8994</td>
    </tr>
    <tr>
      <td>GO:0098609</td>
      <td>Cell–cell adhesion</td>
      <td>4.30</td>
      <td>−1.7231</td>
    </tr>
    <tr>
      <td>GO:0008219</td>
      <td>Cell death</td>
      <td>8.78</td>
      <td>−1.5167</td>
    </tr>
    <tr>
      <td>GO:0002376</td>
      <td>Immune system process</td>
      <td>11.16</td>
      <td>−1.4235</td>
    </tr>
    <tr>
      <td>GO:0009987</td>
      <td>Cellular process</td>
      <td>75.10</td>
      <td>−1.408</td>
    </tr>
  </tbody>
</table>

### EKLF-expressing F4/80+ FL cells are a functionally distinct population from EKLF- F4/80+ cells based on their gene expression program

In our previous study, we had used a mouse strain derived from embryonic stem cells that contain a single copy of the EKLF promoter directly upstream of a green fluorescent protein (GFP) reporter (pEKLF/GFP) to address whether EKLF might be expressed in both the erythroid cell and macrophage (Lohmann and Bieker, 2008). This promoter/enhancer construct is sufficient to generate tissue-specific and developmentally correct expression in vitro and in vivo (Chen et al., 1998; Lohmann et al., 2015; Xue et al., 2004; Zhou et al., 2010); thus GFP onset faithfully mirrors EKLF onset (Lohmann and Bieker, 2008). Using this surrogate marker, we had found that ~36% of F4/80+ macrophage singlet cells express EKLF (Xue et al., 2014).

Presently, we used FACS to isolate both F4/80+GFP+ (EKLF+) and F4/80+GFP- (EKLF-) subsets and assayed gene expression using RNA-Seq. PCA (Figure 4A) and correlation analysis (Figure 4—figure supplement 1A) show that the two populations have widely distinct gene expression profiles. Differential expression analysis shows that 2330 genes are enriched in F4/80+EKLF/GFP+ (Figure 4—figure supplement 1B, Supplementary file 3), with EKLF and Vcam1 among the enriched mRNAs consistent with prior work (Xue et al., 2014, Figure 4B, C). In addition, we find that Epor mRNA is also enriched in F4/80+EKLF/GFP+ (Figure 4B, D). Since Epor+/F4/80+ macrophages form erythroblast islands in bone marrow (Li et al., 2019), our data indicates that the same is true for EKLF+ F4/80+ FL macrophages. When we analyze the functional categories of genes significantly enriched in each of the subsets (Figure 4—figure supplement 1B), we find that the EKLF/GFP+F4/80+ subset is enriched for genes involved in heme synthesis, iron transport and homeostasis, and myeloid/erythroid differentiation (Table 2), functions consistent with those performed by erythroblast island macrophages. In contrast, the genes enriched in EKLF- F4/80+ macrophages are mostly involved in innate and cellular immune responses (Table 3), indicating that these are inherently distinct from the EKLF-expressing macrophages in mouse FL.

![Figure 4.](https://cdn.elifesciences.org/articles/61070/elife-61070-fig4-v2.jpg)

**Figure 4.:** (A) Principal component analysis using scaled Z-score based on the expression level of the top 10,000 highly expressed genes from RNA-Seq replicates of F4/80+ EKLF/GFP+ and F4/80+ EKLF/GFP- is plotted with each axis depicting the two major principal components (source data: Figure 4—source data 1). (B) Scatterplot showing the significantly enriched genes in the F4/80+ EKLF/GFP+ population compared to F4/80+ EKLF/GFP-. Vcam1, Klf1, and Epor are highlighted in blue (source data: Figure 4—source data 2). Fragments per kilobase million (FPKM) values of (C) EKLF/Klf1 and Vcam1 and (D) Epor in the two populations.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/61070/elife-61070-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A) Correlation analysis of Z-score transformed gene expression data for each replicate in RNA-Seq showing high correlation between EKLF/GFP+ and EKLF/GFP- replicates, respectively (source data: Figure 4—figure supplement 1—source data 1). (B) Volcano plot showing genes enriched in EKLF/GFP+ and EKLF/GFP- (source data: Figure 4—source data 2).

**Table 2.**
 Summary of GO terms for genes significantly enriched in EKLF/GFP+ F4/80+ fetal liver macrophages.


<table>
  <thead>
    <tr>
      <th>Term_ID</th>
      <th>Description</th>
      <th>Frequency (%)</th>
      <th>log10 p-valueue</th>
      <th>Uniqueness</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>GO:0006778</td>
      <td>Porphyrin-containing compound metabolic process</td>
      <td>0.18</td>
      <td>−12.8484</td>
      <td>0.777</td>
    </tr>
    <tr>
      <td>GO:0051186</td>
      <td>Cofactor metabolic process</td>
      <td>1.60</td>
      <td>−12.2111</td>
      <td>0.915</td>
    </tr>
    <tr>
      <td>GO:0033013</td>
      <td>Tetrapyrrole metabolic process</td>
      <td>0.20</td>
      <td>−11.1538</td>
      <td>0.869</td>
    </tr>
    <tr>
      <td>GO:0051179</td>
      <td>Localization</td>
      <td>26.83</td>
      <td>−8.8728</td>
      <td>0.994</td>
    </tr>
    <tr>
      <td>GO:0034101</td>
      <td>Erythrocyte homeostasis</td>
      <td>0.58</td>
      <td>−8.3027</td>
      <td>0.786</td>
    </tr>
    <tr>
      <td>GO:0006810</td>
      <td>Transport</td>
      <td>20.74</td>
      <td>−8.0986</td>
      <td>0.952</td>
    </tr>
    <tr>
      <td>GO:0051234</td>
      <td>Establishment of localization</td>
      <td>21.48</td>
      <td>−7.6831</td>
      <td>0.957</td>
    </tr>
    <tr>
      <td>GO:0065008</td>
      <td>Regulation of biological quality</td>
      <td>15.62</td>
      <td>−6.8115</td>
      <td>0.959</td>
    </tr>
    <tr>
      <td>GO:0055085</td>
      <td>Transmembrane transport</td>
      <td>5.98</td>
      <td>−6.4975</td>
      <td>0.945</td>
    </tr>
    <tr>
      <td>GO:0042592</td>
      <td>Homeostatic process</td>
      <td>7.64</td>
      <td>−6.1826</td>
      <td>0.886</td>
    </tr>
    <tr>
      <td>GO:0061515</td>
      <td>Myeloid cell development</td>
      <td>0.32</td>
      <td>−5.6997</td>
      <td>0.83</td>
    </tr>
    <tr>
      <td>GO:0048731</td>
      <td>System development</td>
      <td>21.00</td>
      <td>−5.4423</td>
      <td>0.93</td>
    </tr>
    <tr>
      <td>GO:1901564</td>
      <td>Organonitrogen compound metabolic process</td>
      <td>9.12</td>
      <td>−5.1438</td>
      <td>0.923</td>
    </tr>
    <tr>
      <td>GO:0042744</td>
      <td>Hydrogen peroxide catabolic process</td>
      <td>0.07</td>
      <td>−5.0001</td>
      <td>0.868</td>
    </tr>
    <tr>
      <td>GO:0006811</td>
      <td>Ion transport</td>
      <td>7.05</td>
      <td>−4.9442</td>
      <td>0.946</td>
    </tr>
    <tr>
      <td>GO:0048513</td>
      <td>Animal organ development</td>
      <td>15.85</td>
      <td>−4.7331</td>
      <td>0.926</td>
    </tr>
    <tr>
      <td>GO:0008152</td>
      <td>Metabolic process</td>
      <td>51.22</td>
      <td>−4.3756</td>
      <td>0.997</td>
    </tr>
    <tr>
      <td>GO:0044237</td>
      <td>Cellular metabolic process</td>
      <td>45.64</td>
      <td>−4.3162</td>
      <td>0.937</td>
    </tr>
    <tr>
      <td>GO:0055076</td>
      <td>Transition metal ion homeostasis</td>
      <td>0.58</td>
      <td>−4.2923</td>
      <td>0.831</td>
    </tr>
    <tr>
      <td>GO:0007275</td>
      <td>Multicellular organism development</td>
      <td>23.55</td>
      <td>−4.161</td>
      <td>0.933</td>
    </tr>
    <tr>
      <td>GO:0032502</td>
      <td>Developmental process</td>
      <td>27.72</td>
      <td>−4.1078</td>
      <td>0.994</td>
    </tr>
    <tr>
      <td>GO:0048872</td>
      <td>Homeostasis of number of cells</td>
      <td>1.37</td>
      <td>−4.0386</td>
      <td>0.845</td>
    </tr>
    <tr>
      <td>GO:0008643</td>
      <td>Carbohydrate transport</td>
      <td>0.71</td>
      <td>−3.9826</td>
      <td>0.911</td>
    </tr>
    <tr>
      <td>GO:0048878</td>
      <td>Chemical homeostasis</td>
      <td>4.85</td>
      <td>−3.8372</td>
      <td>0.85</td>
    </tr>
    <tr>
      <td>GO:0006796</td>
      <td>Phosphate-containing compound metabolic process</td>
      <td>13.70</td>
      <td>−3.7212</td>
      <td>0.925</td>
    </tr>
    <tr>
      <td>GO:0006793</td>
      <td>Phosphorus metabolic process</td>
      <td>14.00</td>
      <td>−3.5364</td>
      <td>0.925</td>
    </tr>
    <tr>
      <td>GO:0055072</td>
      <td>Iron ion homeostasis</td>
      <td>0.38</td>
      <td>−3.5032</td>
      <td>0.829</td>
    </tr>
    <tr>
      <td>GO:0030099</td>
      <td>Myeloid cell differentiation</td>
      <td>1.70</td>
      <td>−3.3938</td>
      <td>0.848</td>
    </tr>
    <tr>
      <td>GO:0042440</td>
      <td>Pigment metabolic process</td>
      <td>0.30</td>
      <td>−3.2046</td>
      <td>0.893</td>
    </tr>
    <tr>
      <td>GO:0050801</td>
      <td>Ion homeostasis</td>
      <td>3.30</td>
      <td>−3.1372</td>
      <td>0.843</td>
    </tr>
    <tr>
      <td>GO:0048856</td>
      <td>Anatomical structure development</td>
      <td>25.70</td>
      <td>−2.9598</td>
      <td>0.947</td>
    </tr>
    <tr>
      <td>GO:0006820</td>
      <td>Anion transport</td>
      <td>2.43</td>
      <td>−2.8403</td>
      <td>0.941</td>
    </tr>
    <tr>
      <td>GO:0017001</td>
      <td>Antibiotic catabolic process</td>
      <td>0.52</td>
      <td>−2.6912</td>
      <td>0.876</td>
    </tr>
    <tr>
      <td>GO:0098771</td>
      <td>Inorganic ion homeostasis</td>
      <td>3.02</td>
      <td>−2.6573</td>
      <td>0.839</td>
    </tr>
    <tr>
      <td>GO:0019755</td>
      <td>One-carbon compound transport</td>
      <td>0.06</td>
      <td>−2.4416</td>
      <td>0.9</td>
    </tr>
    <tr>
      <td>GO:0019725</td>
      <td>Cellular homeostasis</td>
      <td>3.80</td>
      <td>−2.1148</td>
      <td>0.81</td>
    </tr>
    <tr>
      <td>GO:0071704</td>
      <td>Organic substance metabolic process</td>
      <td>49.01</td>
      <td>−2.0066</td>
      <td>0.945</td>
    </tr>
  </tbody>
</table>

**Table 3.**
 Summary of GO terms for genes significantly enriched in EKLF/GFP- F4/80+ fetal liver macrophages.


<table>
  <thead>
    <tr>
      <th>Term_ID</th>
      <th>Description</th>
      <th>Frequency (%)</th>
      <th>log10 p-valueue</th>
      <th>Uniqueness</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>GO:0002376</td>
      <td>Immune system process</td>
      <td>11.16</td>
      <td>−90.8785</td>
      <td>0.492</td>
    </tr>
    <tr>
      <td>GO:0001775</td>
      <td>Cell activation</td>
      <td>4.73</td>
      <td>−58.5949</td>
      <td>0.502</td>
    </tr>
    <tr>
      <td>GO:0045321</td>
      <td>Leukocyte activation</td>
      <td>4.17</td>
      <td>−57.3276</td>
      <td>0.435</td>
    </tr>
    <tr>
      <td>GO:0001816</td>
      <td>Cytokine production</td>
      <td>2.93</td>
      <td>−56.1898</td>
      <td>0.522</td>
    </tr>
    <tr>
      <td>GO:0040011</td>
      <td>Locomotion</td>
      <td>7.21</td>
      <td>−51.1415</td>
      <td>0.515</td>
    </tr>
    <tr>
      <td>GO:0001817</td>
      <td>Regulation of cytokine production</td>
      <td>2.62</td>
      <td>−48.8035</td>
      <td>0.477</td>
    </tr>
    <tr>
      <td>GO:0006928</td>
      <td>Movement of cell or subcellular component</td>
      <td>7.93</td>
      <td>−47.6096</td>
      <td>0.474</td>
    </tr>
    <tr>
      <td>GO:0006954</td>
      <td>Inflammatory response</td>
      <td>2.89</td>
      <td>−45.4918</td>
      <td>0.524</td>
    </tr>
    <tr>
      <td>GO:0022610</td>
      <td>Biological adhesion</td>
      <td>6.66</td>
      <td>−45.4019</td>
      <td>0.519</td>
    </tr>
    <tr>
      <td>GO:0030334</td>
      <td>Regulation of cell migration</td>
      <td>3.21</td>
      <td>−37.8661</td>
      <td>0.468</td>
    </tr>
    <tr>
      <td>GO:0051707</td>
      <td>Response to other organism</td>
      <td>4.45</td>
      <td>−34.3509</td>
      <td>0.498</td>
    </tr>
    <tr>
      <td>GO:0009607</td>
      <td>Response to biotic stimulus</td>
      <td>4.67</td>
      <td>−34.2713</td>
      <td>0.514</td>
    </tr>
    <tr>
      <td>GO:0030155</td>
      <td>Regulation of cell adhesion</td>
      <td>2.92</td>
      <td>−34.1483</td>
      <td>0.502</td>
    </tr>
    <tr>
      <td>GO:0022603</td>
      <td>Regulation of anatomical structure morphogenesis</td>
      <td>4.20</td>
      <td>−33.7719</td>
      <td>0.47</td>
    </tr>
    <tr>
      <td>GO:0008283</td>
      <td>Cell proliferation</td>
      <td>8.83</td>
      <td>−29.2539</td>
      <td>0.482</td>
    </tr>
    <tr>
      <td>GO:0030036</td>
      <td>Actin cytoskeleton organization</td>
      <td>2.80</td>
      <td>−28.0214</td>
      <td>0.516</td>
    </tr>
    <tr>
      <td>GO:0030029</td>
      <td>Actin filament-based process</td>
      <td>3.14</td>
      <td>−27.3893</td>
      <td>0.523</td>
    </tr>
    <tr>
      <td>GO:0035295</td>
      <td>Tube development</td>
      <td>3.20</td>
      <td>−25.1916</td>
      <td>0.507</td>
    </tr>
    <tr>
      <td>GO:0008219</td>
      <td>Cell death</td>
      <td>8.78</td>
      <td>−24.5897</td>
      <td>0.468</td>
    </tr>
    <tr>
      <td>GO:0070661</td>
      <td>Leukocyte proliferation</td>
      <td>1.41</td>
      <td>−23.5623</td>
      <td>0.563</td>
    </tr>
    <tr>
      <td>GO:0072358</td>
      <td>Cardiovascular system development</td>
      <td>3.13</td>
      <td>−23.0994</td>
      <td>0.498</td>
    </tr>
    <tr>
      <td>GO:0006793</td>
      <td>Phosphorus metabolic process</td>
      <td>14.00</td>
      <td>−22.2385</td>
      <td>0.449</td>
    </tr>
    <tr>
      <td>GO:0044093</td>
      <td>Positive regulation of molecular function</td>
      <td>7.70</td>
      <td>−22.1855</td>
      <td>0.47</td>
    </tr>
    <tr>
      <td>GO:0006897</td>
      <td>Endocytosis</td>
      <td>3.19</td>
      <td>−19.725</td>
      <td>0.532</td>
    </tr>
    <tr>
      <td>GO:0098657</td>
      <td>Import into cell</td>
      <td>0.29</td>
      <td>−19.1913</td>
      <td>0.625</td>
    </tr>
    <tr>
      <td>GO:0050764</td>
      <td>Regulation of phagocytosis</td>
      <td>0.36</td>
      <td>−18.9505</td>
      <td>0.578</td>
    </tr>
    <tr>
      <td>GO:1902533</td>
      <td>Positive regulation of intracellular signal transduction</td>
      <td>4.07</td>
      <td>−18.4109</td>
      <td>0.439</td>
    </tr>
    <tr>
      <td>GO:0051704</td>
      <td>Multiorganism process</td>
      <td>6.53</td>
      <td>−17.9065</td>
      <td>0.52</td>
    </tr>
    <tr>
      <td>GO:0034097</td>
      <td>Response to cytokine</td>
      <td>3.34</td>
      <td>−17.0337</td>
      <td>0.525</td>
    </tr>
    <tr>
      <td>GO:0032940</td>
      <td>secretion by cell</td>
      <td>4.11</td>
      <td>−16.2249</td>
      <td>0.486</td>
    </tr>
    <tr>
      <td>GO:0002699</td>
      <td>Positive regulation of immune effector process</td>
      <td>0.86</td>
      <td>−14.2444</td>
      <td>0.51</td>
    </tr>
    <tr>
      <td>GO:0007167</td>
      <td>Enzyme-linked receptor protein signaling pathway</td>
      <td>4.02</td>
      <td>−14.1906</td>
      <td>0.48</td>
    </tr>
    <tr>
      <td>GO:0001774</td>
      <td>Microglial cell activation</td>
      <td>0.07</td>
      <td>−12.1713</td>
      <td>0.623</td>
    </tr>
    <tr>
      <td>GO:0010942</td>
      <td>Positive regulation of cell death</td>
      <td>2.72</td>
      <td>−11.1617</td>
      <td>0.486</td>
    </tr>
    <tr>
      <td>GO:0097435</td>
      <td>Supramolecular fiber organization</td>
      <td>2.73</td>
      <td>−11.1108</td>
      <td>0.525</td>
    </tr>
    <tr>
      <td>GO:0042592</td>
      <td>Homeostatic process</td>
      <td>7.64</td>
      <td>−10.9553</td>
      <td>0.477</td>
    </tr>
    <tr>
      <td>GO:0035456</td>
      <td>Response to interferon-beta</td>
      <td>0.22</td>
      <td>−10.2302</td>
      <td>0.627</td>
    </tr>
    <tr>
      <td>GO:0008360</td>
      <td>Regulation of cell shape</td>
      <td>0.65</td>
      <td>−10.1463</td>
      <td>0.547</td>
    </tr>
    <tr>
      <td>GO:0042107</td>
      <td>Cytokine metabolic process</td>
      <td>0.55</td>
      <td>−9.76</td>
      <td>0.605</td>
    </tr>
    <tr>
      <td>GO:0050777</td>
      <td>Negative regulation of immune response</td>
      <td>0.61</td>
      <td>−9.7184</td>
      <td>0.523</td>
    </tr>
    <tr>
      <td>GO:0002444</td>
      <td>Myeloid leukocyte-mediated immunity</td>
      <td>0.38</td>
      <td>−9.7099</td>
      <td>0.588</td>
    </tr>
    <tr>
      <td>GO:0090130</td>
      <td>Tissue migration</td>
      <td>1.14</td>
      <td>−9.6676</td>
      <td>0.563</td>
    </tr>
    <tr>
      <td>GO:0051129</td>
      <td>Negative regulation of cellular component organization</td>
      <td>2.94</td>
      <td>−9.0279</td>
      <td>0.504</td>
    </tr>
  </tbody>
</table>

### EKLF specifies expression of a substantial number of genes including important transcription factors in FL macrophages

Both the above datasets provide us with unique information. The first dataset (Figure 3) identifies EKLF-dependent macrophage genes but does not distinguish between EKLF-expressing and EKLF-deficient macrophages in a genetically unaltered state. The second dataset (Figure 4) identifies genes with enriched expression in F4/80+ cells where EKLF is also expressed but does not identify EKLF-dependent genes. By comparing the datasets, we can determine which genes have enriched expression in EKLF-expressing macrophages and are also significantly downregulated in EKLF-/-, and therefore truly EKLF-dependent (Figure 5A, red box). Overlapping these two independent datasets is an extremely powerful way to parse down the potential direct/indirect genes whose expression is dependent on the presence of EKLF. We find that 504 genes are EKLF-dependent in F4/80+EKLF+ macrophages, a highly significant number given the size of the datasets (Figure 5B, Figure 5—figure supplement 1A).

![Figure 5.](https://cdn.elifesciences.org/articles/61070/elife-61070-fig5-v2.jpg)

**Figure 5.:** (A) Scatterplot of log2-fold changes in EKLF/GFP+ plotted against EKLF-/-. Red box shows the genes that are common and of interest from both datasets, that is, enriched in EKLF/GFP+ and downregulated in EKLF-/- F4/80+ FL macrophages (source data: Figure 5—source data 1). (B) Venn diagram showing the number of genes in each category from (A). Centrimo analysis of promoters of EKLF-dependent genes showing differential motif enrichment of (C) EKLF/Klf1 and (D) Klf3, Sp4, E2f1, and E2f4 motifs (source data: Figure 5—source data 2, 3). Dotted line depicts the expected probability of occurrence of the respective motif in the background dataset (see 'Materials and methods'). (E) Heatmap showing log2-fold change of expression in EKLF-/- and EKLF/GFP+ of the above EKLF-dependent transcription factors in F4/80+ FL macrophages.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/61070/elife-61070-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (A) Heatmap showing log2-fold change expression in EKLF-/- over WT and EKLF/GFP+ over EKLF/GFP- of all the 504 EKLF-dependent genes in F4/80+ FL macrophages (source data: Figure 5—figure supplement 1—source data 1). One in every six genes’ name is displayed for visibility. (B) Centrimo analysis of E2f2 promoter of EKLF-dependent genes showing differential motif enrichment of E2f2 motifs (source data: Figure 5—source data 2, 3). Dotted line depicts the expected probability of occurrence of the E2f2 motif in the background dataset (see 'Materials and methods'). (C) Heatmap showing log2-fold change expression of potential EKLF-dependent transcription factors (source data: Figure 5—figure supplement 1—source data 1). Red boxes highlight the lineage Klf transcription factors and the cell-cycle E2f transcription factors.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/61070/elife-61070-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** (A) Heatmap of log2 FPKM values of F4/80+ FL signature genes (Figure 1E) that are also enriched in F4/80+ EKLF/GFP+ cells (source data: Figure 5—figure supplement 2—source data 1). (B) Heatmap of log2 FPKM and fold changes of FL signature genes that are significantly downregulated in EKLF-/- (source data: Figure 5—figure supplement 2—source data 2). Red boxes depict the EKLF-dependent signature genes that are common to both (A) and (B). (C) Density plot of flow cytometry analysis of E13.5 FLs stained with F4/80 and Adra2b antibodies. Gating scheme for F4/80-hi and Adra2b+ cells is shown in blue. The percentage of double-positive Adra2b+ and F4/80-hi cells, compared to total Adra2b+ cells, is indicated. (D) Representative pictures of erythroblastic islands from E13.5 FLs are shown after immunostaining with anti-F4/80 (red) or anti-Adra2b (green) antibodies. DNA stain was with DAPI (blue).

To determine whether these genes may be under EKLF transcription control, we used Centrimo (MEME suite) to analyze the promoters of these 504 genes for TF motifs that are differentially enriched over a background set comprising promoter sequences of the rest of the transcriptome (Supplementary file 4). Indeed, we find that Klf1 motifs are overrepresented in these promoters, consistent with the idea that they are EKLF-dependent (Figure 5C). In addition, we find that the motifs of transcription factors Klf3, E2f1, E2f4, and Sp4 are significantly enriched (Figure 5D) and these TFs are also among the 504 EKLF-dependent genes (Figure 5E). This strongly suggests that EKLF, together with Klf3, E2f1, E2f4, and Sp4, may constitute a transcriptional network regulating the distinct gene expression program of FL island macrophages. E2f2 is also EKLF-dependent in F4/80+ macrophages (Figure 5E), but its motif is not significantly enriched (Figure 5—figure supplement 1B, E-value=0.17), suggesting that E2f2 may not be a critical part of the EKLF transcription network in island macrophages.

The overlap of the datasets (Figure 5A, B) suggests that EKLF may regulate the expression of a significant number of other transcription factors in FL macrophages, including Foxo3, Ikzf1, MafK, Nr3c1; cell-cycle E2f factors; and other members of the Klf family (Figure 5—figure supplement 1C). This will ultimately be verified by a search of consensus target sequences in putative target genes and by EKLF ChIP. Thus, along with the known transcriptional role of EKLF in erythroid cells, our data is consistent with a global regulatory role for EKLF in the proliferation and development of FL island macrophages.

### Novel EKLF-dependent markers of EKLF+ F4/80+ FL macrophages

Our data has shown that FL macrophages have a distinct cellular identity, with a unique gene expression signature, and that the EKLF+ subset is functionally distinct. We next wished to develop a strategy to isolate the EKLF+ macrophages by finding a novel specific cell surface marker for sorting these cells. We find that of the 304 F4/80+ signature genes (Figure 1E), 16 are enriched in F4/80+EKLF/GFP+ macrophages (Figure 5—figure supplement 2A) and 32 are downregulated in F4/80+ EKLF-/- macrophages (Figure 5—figure supplement 2B). Among these, Adra2b codes for a cell surface adrenergic receptor α2B (Weinshank et al., 1990), is highly enriched in F4/80+EKLF/GFP+, and significantly downregulated approximately eightfold in F4/80+EKLF-/- (Figure 5—figure supplement 2A, B). We reasoned that Adra2b, along with F4/80+, could be used as an additional marker for EKLF+F4/80+ macrophages. Thus, we determined the proportion of Adra2b and F4/80 expressing cells in E13.5 FLs from EKLF+/+ and EKLF-/- mice using flow cytometry.

Using antibodies against Adra2b and F4/80, we find that whereas only a fraction of Adra2b+ cells are also F4/80+, most F4/80+ FL cells are Adra2b+; however, we also note that the Adra2b+F4/80+ population has a F4/80-hi subpopulation (Figure 5—figure supplement 2C, top). This F4/80-hi/Adra2b+ subset is significantly smaller in EKLF-/- (Figure 5—figure supplement 2C, bottom), consistent with our RNA-Seq observations. This data demonstrates that the F4/80-hi/Adra2b+ population in the FL correlates with EKLF expression in F4/80+ FL cells, suggesting that EKLF+ FL macrophages could be isolated using this strategy.

We used immunofluorescence to directly demonstrate that Adra2b protein is expressed in erythroblastic islands (Figure 5—figure supplement 2D). The localization of Adra2b at the surface of the central macrophage cell readily distinguishes it from the more diffuse staining exhibited by F4/80.

### Resolving the cellular heterogeneity in F4/80+ FL macrophages

One critical issue is that FL macrophages are a heterogeneous population of cells, a notion readily apparent from the published literature (Lee et al., 2018; Seu et al., 2017) and from our own observation that not all F4/80+ cells express EKLF (Figure 4). To segregate FL F4/80+ subpopulations and illuminate the role of EKLF in this process, we performed single-cell RNA-Seq on purified F4/80+ FL cells. We used a magnetic bead purification strategy in the presence of Icam4/αv inhibitor peptide (Xue et al., 2014) to isolate and maintain healthy F4/80+ cells for single-cell barcoding and library preparation using the Chromium V3 platform (see 'Materials and methods'). Using flow cytometry, we find that about 83% of our purified population is F4/80+ after two rounds of selection (Figure 6—figure supplement 1).

Single-cell RNA-Seq confirmed the cellular heterogeneity in the F4/80+ population, with 13 separate clusters of cells after unsupervised dimensionality reduction using the Seurat package (Butler et al., 2018; Stuart et al., 2019; Figure 6A). F4/80+ mRNA (encoded by the Adgre1 gene) is present in all the clusters, although some clusters have higher levels (Figure 6B). Additional macrophage markers such as Marco and Vcam1 mRNAs are also present in all clusters, whereas the macrophage transcription factor PU.1 (encoded by Spic) is enriched in clusters 0, 1, 2, and 8 (Figure 6C). Differential enrichment analysis reveals the mRNAs that are enriched in each cluster (Figure 6D, Figure 6—source data 1), and we find certain genes with almost exclusive expression in a particular cluster that serve as markers for that cluster (Figure 6—figure supplement 2).

![Figure 6.](https://cdn.elifesciences.org/articles/61070/elife-61070-fig6-v2.jpg)

**Figure 6.:** (A) Unsupervised clustering using principal component analysis and subsequent U-MAP projections computed and plotted using the R Seurat package for single-cell RNA-Seq of purified E13.5 FL F4/80+ cells. Cluster numbers are indicated on the clusters. (B) Violin plot showing the distribution of F4/80 (Adgre1) mRNA expression in the clusters identified in (A). (C) Feature plots (left panel) showing individual cellular expression superimposed on the cluster, and Violin plots (right) showing the distribution of expression in each cluster of macrophage markers Vcam1 and Marco, and the macrophage-specific transcription factor PU.1 (Spic). (D) Differential mRNA enrichment in each cluster plotted as a heatmap, showing putative unique markers of each cluster (source data: Figure 6—source data 1). Relative expression levels are indicated by color: yellow=high, black=mid, and purple=low.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/61070/elife-61070-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** F4/80-PE cells isolated from E13.5 fetal livers using the EZSep (Cell Signaling Technologies) magnetic bead method in the presence of Icam4/αv inhibitor peptide (Xue et al., 2014) and analyzed by flow cytometry to determine purity of the F4/80+ population for single-cell sequencing.

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/61070/elife-61070-fig6-figsupp2-v2.jpg)

**Figure 6—figure supplement 2.:** Cluster number and marker names are indicated.

![Figure 6—figure supplement 3.](https://cdn.elifesciences.org/articles/61070/elife-61070-fig6-figsupp3-v2.jpg)

**Figure 6—figure supplement 3.:** Violin plot showing the distribution (left) and feature plot showing individual cell expression (right) of (A) Csf1r, Dnase2a, and Il4rα genes associated with activated macrophages; (B) Gypa, Snca, and Spta1 genes, which are markers for erythro-myeloid characteristics; (C) Gapdh; and (D) Tfrc (CD71), which are uniformly expressed in most clusters.

It is apparent from these analyses that clusters 0 and 1 have a high overlap in cluster markers (Figure 6D), and due to the high expression of macrophage-specific genes (Figure 6B, C), these clusters likely are comprised of macrophages. This is also confirmed by GO analysis of the top 100 markers for these clusters (Supplementary file 5). Further, GO analysis of markers for clusters 2 and 3 yields terms compatible with activated macrophage functions (Supplementary file 5), and indeed these clusters express genes correlated with activated macrophages such as Csf1r, Dnase2a, and Il4ra (Figure 6—figure supplement 3A). In contrast, GO analysis of the top enriched genes for clusters 4, 5, 7, and 8 relate to erythro-myeloid characteristics and heme metabolism (Supplementary file 6), with highly enriched markers for these clusters being glycophorin A, α-synuclein, and α-spectrin (Figure 6—figure supplement 3B). A search for the terminal erythroid marker Ter119 (Ly76) yields no results in our single-cell sequencing dataset, indicating that perhaps its mRNA is undetectable and that our F4/80+ purification is largely devoid of terminally differentiating erythroid cells. To further support the heterogeneity of expression in these populations, in contrast we find that the mRNA for the constitutively active gene, Gapdh, is uniformly highly expressed in all clusters (Figure 6—figure supplement 3C), whereas CD71 (Tfrc) mRNA was expressed at moderate levels in most clusters (Figure 6—figure supplement 3D).

### Cellular heterogeneity in EKLF+ F4/80+ FL macrophages and an improved strategy to isolate this population

Our earlier observations from the pEKLF/GFP mice indicated that about 36% of the F4/80+ FL cells express EKLF (Xue et al., 2014). EKLF+ expression is detected exclusively in clusters 4, 5, and 7 (Figure 7A), and these clusters comprise about 23% of the cells in our dataset. We also find that most of the EKLF+ cells express Epor (Figure 7B), consistent with our earlier observations as well as others (Li et al., 2019). To further test our previous observations that Adra2b expression correlates with EKLF expression and is found in erythroblast island macrophages (Figure 5—figure supplement 2D), we looked for Adra2b expression in single cells. We find specific Adra2b enrichment in cluster 4, thus correlating with some EKLF+ as well as Epor+ cells, albeit the remaining EKLF-expressing clusters 5 and 7 have little Adra2b expression (Figure 7C). This indicates high amounts of heterogeneity even within EKLF+F4/80+ macrophages and suggests that Adra2b alone as a marker is not sufficient to enable efficient isolation of EKLF+F4/80+ cells.

![Figure 7.](https://cdn.elifesciences.org/articles/61070/elife-61070-fig7-v2.jpg)

**Figure 7.:** Violin plots showing distribution (left) and feature plots (right) showing individual cellular mRNA expression of (A) Klf1, (B) Epor, and (C) Adra2b superimposed on the clusters.

This led us to devise an improved strategy to isolate EKLF+F4/80+ FL cells based on cell surface marker expression by searching for mRNAs enriched in EKLF+ clusters 4, 5, and 7 taken together. We find that Add2 (adducin2), Hemgn (hemogen), Nxpe2 (neurexophilin and PC-esterase domain family, member 2), and Sptb (spectrinβ) are specifically enriched in the EKLF+ clusters (Figure 8A). Of these, Add2, Nxpe2, and Sptb encode membrane-associated proteins, which would be preferred for antibody-based isolation strategies such as FACS or magnetic bead separation, and thus are attractive candidates for marker-based separation of EKLF+ F4/80+ cells. Although Add2 and Sptb are known to be highly expressed in erythroid cells (Chen et al., 2009; Franco and Low, 2010; Gardner and Bennett, 1987), RNA-Seq data of ckit-/CD45+/F480+/AA4.1-/CD11b+ macrophages derived from staged mice embryos (Mass et al., 2016) shows that Add2 and Sptb mRNAs are indeed expressed in mice FL macrophages from E12.5–E18.5 (Figure 8B), with a similar developmental onset to that of EKLF (Figure 2C). Additionally, when we search for their expression in our F4/80+ EKLF/GFP+ bulk RNA-Seq dataset, all four markers are significantly enriched in F4/80+ EKLF/GFP+ (Figure 8C), thus confirming that their mRNA expression correlates with EKLF mRNA expression in F4/80+ macrophages. Finally, optimal levels of Add2 and Hemgn expression are also EKLF-dependent since we find that they are significantly downregulated in F4/80+ EKLF-/- cells (Figure 8D).

![Figure 8.](https://cdn.elifesciences.org/articles/61070/elife-61070-fig8-v2.jpg)

**Figure 8.:** Using differential enrichment analysis of EKLF clusters 4, 5, and 7 compared with the rest of the cells, putative markers for F4/80+ EKLF+ cells were identified. (A) Violin and feature plots for the identified markers Add2 (adducinβ), Hemgn (hemogen), Nxpe2 (neurexophilin and PC-esterase domain family, member2), and Sptb (spectrinβ). (B) Data (as in Figure 2C, Mass et al., 2016) showing RNA-Seq reads of F4/80+ EKLF+ cell markers from staged and sorted fetal or postnatal liver macrophages. (C) FPKM expression levels of EKLF markers in F4/80+ EKLF/GFP+ and F4/80+ EKLF/GFP- fetal liver macrophage. (D) FPKM expression levels of EKLF markers Add2 and Hemgn in F4/80+ EKLF+/+ and F4/80+ EKLF-/- fetal liver macrophage.

Upon staining E13.5 FL cells with both F4/80 and adducin2, or F4/80 and spectrinβ antibodies, we find that the majority (~88%) of the Add2+ or Sptb+ cells are F4/80- (and presumably erythroid). However, about 25% of all F4/80+ cells are Add2+ or Sptb+ in each case (Figure 9A), aligning with our single-cell RNA-Seq observations (Figure 8A). We repeated the F4/80+ purification and stained the purified F4/80+ cells for Add2 or Sptb to find that in each case about 24% of the F4/80+ cells are Add2+ or Sptb+ (Figure 9B), a proportion resembling the 23% of cells in clusters 4, 5, and 7 where these mRNAs are expressed. To test the possibility that any Add2 and Sptb expression seen in F4/80+ cells was due to residual erythroid contamination in our F4/80+ population, we performed Imagestream analysis. Using the pEKLF/GFP mouse, we stained for F4/80 and Add2, and we find single cells expressing F4/80 and Add2 that are also EKLF/GFP+ (Figure 9C). This not only confirms that the Add2 signal is coming from single cells, it also demonstrates visually that Add2 expression in a subset of F4/80+ macrophages correlates with EKLF expression in those macrophages.

![Figure 9.](https://cdn.elifesciences.org/articles/61070/elife-61070-fig9-v2.jpg)

**Figure 9.:** (A) Flow cytometry analysis of E13.5 fetal liver cells stained with anti-F4/80-PE and anti-adducinβ (top) or anti-spectrinβ (below) antibodies conjugated to AlexaFluor 647. Gates are drawn based on unstained and single-color compensation controls for PE and AlexaFluor 647. Population percentages within each gate are indicated. (B) F4/80+ cells purified from E13.5 fetal livers using magnetic bead selection stained for anti-adducinβ (top) or anti-spectrinβ (below). Gates are the same as (A) and population percentages are indicated. (C) Imaging flow cytometry analysis of E13.5 fetal liver cells from the pEKLF/GFP mouse stained for F4/80-PE and Add2-TxRed. Single cells positive for F4/80, Add2, and GFP are shown. (D, E) Isolated erythroblast islands stained for DAPI, F4/80-PE, and (D) Sptb-Alexa647 or (E) Add2-Alexa647 and examined by fluorescent microscopy. Scale bars are indicated.

Finally, since earlier studies from our group (Xue et al., 2014; Li et al., 2019) showed that EKLF expression is enriched in macrophages forming erythroblast islands, we isolated erythroblast islands and tested for Add2 and Sptb protein expression by immunofluorescence. We find high Sptb and Add2 staining in the central macrophage as well as few surrounding erythroid cells (Figure 9D, E), indicating that these markers are expressed in erythroblast island macrophages. Thus, Add2 or Sptb can be used as reliable markers to isolate F4/80+ EKLF+ FL island macrophage population for further characterization of their unique properties.

## Discussion

### Identification of a novel cell type in FL macrophage

Although there is overlap among the cell populations, we have shown that E13.5 murine FL F4/80+ macrophages exhibit a distinct expression pattern when compared to adult spleen F4/80+ macrophage, one that is also divergent from that of FL erythroid cells, thus providing them with a discrete cellular identity. Our data suggests the existence of a unique macrophage cell type with novel markers that defines erythroblastic island-associated macrophage. This is perhaps not surprising as there is extensive macrophage heterogeneity (Lee et al., 2018; Paulson, 2019; Seu et al., 2017), and it has been long noted that island macrophage may have a distinctive surface marker expression (Manwani and Bieker, 2008).

The unique expression signature exhibited by these cells includes over 300 genes that are functionally involved in positive regulation of developmental processes, particularly cell movement, localization, and adhesion. Our data suggests that establishing a macrophage cell dedicated to maintaining such a unique expression profile makes developmental sense given its role in efficiently aiding the huge demand for red blood cells during early development, specifically within the expanding FL site (Chasis and Mohandas, 2008; Hom et al., 2015; Klei et al., 2017; Manwani and Bieker, 2008; Yeo et al., 2019).

### Transient nature of a singular, EKLF-dependent FL macrophage population that coincides with the onset of definitive erythropoiesis during mouse embryonic development

The idea of a dedicated island macrophage cell is further supported by the overlap in the single-cell seq and the developmental RNA-Seq expression datasets. These show there is a specific onset of many of the markers of interest that coincide with the peak of EKLF expression in macrophage at E12.5, at the same time as definitive erythropoiesis is occurring in the mouse FL. Strikingly, expression of many of these also dissipates coordinately at later embryonic stages. This may follow from either transient EKLF expression in the macrophage or the transient presence of a population of EKLF-expressing macrophage. Such dynamic regulation has been observed with IL7Rα (Leung et al., 2019), but the remarkable coherence of the erythroblastic island macrophage subset in clusters 4, 5, and 7 suggests the existence of a cross-regulatory mechanism that leads to the establishment of a network of genes critical for proper island niche function. Consistent with this, KLF binding motifs are enriched in active macrophage genes (Gosselin et al., 2014; Lavin et al., 2014) and correlate with binding by other macrophage factors such as CJUN and P65 (Link et al., 2018). Our comparative analysis of EKLF-/- and EKLF/GFP+ strongly supports the idea, postulated previously from other studies (Li et al., 2019; Porcu et al., 2011; Xue et al., 2014), that EKLF is a central player in establishing this network at the right time and place in development. Given our studies, the cause of the embryonic lethality in the absence of EKLF could be a combination of impaired erythropoiesis due to the loss of EKLF in developing erythroid progenitors as well as impaired island macrophage function supporting definitive erythropoiesis.

### EKLF regulation of island macrophage signature genes

By combining both EKLF-/- and EKLF/GFP+ RNA-Seq data, and then further parsed by the single-cell seq data, we find that loss of EKLF expression alters expression of many macrophage genes. We also find that the EKLF-expressing macrophages are functionally different from those not expressing EKLF, with high enrichment of genes performing functions consistent with erythroblast islands. Thus, the subset that are specific to the F4/80+ macrophage and whose expression is EKLF-dependent provides a novel expression signature that identifies targets that may be unique to the erythroblastic island. We have identified three in particular, Adra2b, Add2, and Sptb, that are enriched in EKLF WT macrophage and in the erythroblastic island. As a result, we suggest that these are additional novel markers that, in conjunction with F4/80, provide a further specification to island-associated macrophage identity. Heterogeneity remains an issue; however, from our single-cell seq data, it is likely that combining select markers, in particular F4/80+, Add2+, and Sptb+, will distinguish a discrete subpopulation that is highly enriched for island-associated macrophage. We are in the process of establishing such a protocol based on the robust cell surface expression of these three markers and will include Nxpe2 in the mix if a suitable selection antibody becomes available.

Identification and molecular knowledge of unique island macrophage expression and receptors may be functionally relevant to studies that utilize these cells to help expand in vitro erythropoiesis more efficiently (Hom et al., 2015; Rhodes et al., 2008). These could be used in combination with cytokines known to enhance island macrophage such as erythropoietin (Li et al., 2019), dexamethasone (Falchi et al., 2015; Heideveld et al., 2018), or the KLF1-stimulated combo of ANGPTL7/IL33/SERPINB2 (Lopez-Yrigoyen et al., 2019). Efficient growth and maintenance become important when designing strategies to improve macrophage responses in the context of myelodysplastic syndromes (Buesche et al., 2016) or in the anemia of inflammation (Hom et al., 2015).

### Resolution of macrophage heterogeneity

Not surprisingly, we find that the FL F480+ population is heterogeneous, with our single-cell analysis suggesting 13 different clusters. Within this mixture we discovered a subset of clusters that express EKLF and its network of genes important for island macrophage. It is of interest that this subset does not express CD11b (Itgam), consistent with studies suggesting it is not an island macrophage marker (Seu et al., 2017; Tay et al., 2020; Ulyanova et al., 2016). Of additional interest, the granulocyte Ly6G marker did not appear in any of our clusters, consistent with an efficient removal of granulocytes during our enrichment procedure.

In this context, it is perhaps surprising that other markers historically suggested to be critical for island function such as Vcam1 are expressed at lower levels in the EKLF clusters than in others. Three explanations can be suggested. (1) EKLF+/Vcam1+ cells may be the relevant functional subset of total Vcam1-expressing cells, a different subset of which may have a separate, non-EKLF-dependent function (e.g., homing [(Li et al., 2018)]). (2) We are not suggesting that EKLF-expressing clusters are the sole source of macrophage islands; there may be others that arise following pathological conditions (e.g., ß-thalassemia or polycythemia vera [Chow et al., 2013; Ramos et al., 2013]), or when comparing steady-state versus stress/anemia (Paulson et al., 2020). (3) Erythroblastic islands are also found in bone marrow and spleen, and these arise within a significantly different niche than what we have focused on here during prenatal development. Such directive effects of the environment on macrophage identity have been noted before (Gosselin et al., 2014; Lavin et al., 2014). With respect to our present observations, given the importance of neural signaling in the bone marrow (Méndez-Ferrer et al., 2020), it is possible that a molecule such as Adra2b may be more highly expressed and play a more important role in bone marrow macrophage than in FL macrophage.

### Human island macrophage

Collectively, our study shows that EKLF plays a critical role within the specific subset of unique macrophage cells that are transiently required for proper establishment of erythroblastic islands in the developing embryo. Of relevance to human biology (May and Forrester, 2020), although the positive effects of EKLF expression on island macrophage function have been previously noted (Lopez-Yrigoyen et al., 2019), it is also relevant that a recent single-cell analysis of human FL hematopoiesis shows that EKLF and many of its target genes identified in the present study are also expressed in the ‘Vcam1+ erythroblastic island macrophage’ cluster (Popescu et al., 2019).

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
      <td>Genetic reagent (Mus musculus)</td>
      <td>Klf-/- (Klf1tm1Sho)</td>
      <td>10.1038/375318a0</td>
      <td>MGI:1857162</td>
      <td>EKLF-null mouse in 129S4/SvJae background</td>
    </tr>
    <tr>
      <td>Genetic reagent (Mus musculus)</td>
      <td>pEKLF/GFP</td>
      <td>10.1242/dev.018200</td>
      <td>Peklf-GFP</td>
      <td>eGFP expressed from the EKLF promoter</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-F4/80-PE (rabbit polyclonal)</td>
      <td>eBiosciences</td>
      <td>#12-4801-80</td>
      <td>(1:100)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Adra2b (rabbit polyclonal)</td>
      <td>Alomone Labs</td>
      <td>#AAR-021</td>
      <td>(1:100)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-adducinβ (mouse monoclonal)</td>
      <td>Santa Cruz Biotechnologies</td>
      <td># sc-376063</td>
      <td>(1:100)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-spectrinβ1 (mouse monoclonal)</td>
      <td>Santa Cruz Biotechnologies</td>
      <td># sc-374309</td>
      <td>(1:100)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Donkey anti-rabbit IgG – AlexaFluor 647 (donkey polyclonal)</td>
      <td>Invitrogen</td>
      <td># A-31573</td>
      <td>(1:200)</td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>FWV peptide (GenScript custom)</td>
      <td>10.1242/dev.103960</td>
      <td># SC1848</td>
      <td>2 mM</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>EasySep mouse PE positive selection kit</td>
      <td>Cell Signaling Technologies</td>
      <td># 17656</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Zip AlexaFluor 647 antibody labeling kit</td>
      <td>Invitrogen</td>
      <td># Z11235</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Lightning link Texas red conjugation kit</td>
      <td>Abcam</td>
      <td># ab195225</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>RNA Nanoprep kit</td>
      <td>Agilent</td>
      <td>#400753</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Chromium Single Cell 3ʹ Library Kit v3</td>
      <td>10X Genomics</td>
      <td># PN-1000095</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>TRIzol reagent</td>
      <td>Invitrogen</td>
      <td>#15596026</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>STAR</td>
      <td>10.1093/bioinformatics/bts635</td>
      <td>RRID:SCR_015899</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Salmon</td>
      <td>10.1038/nmeth.4197</td>
      <td>RRID:SCR_017036</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>HTSeq</td>
      <td>10.1093/bioinformatics/btu638</td>
      <td>RRID:SCR_005514</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>tximport</td>
      <td>https://github.com/mikelove/tximport</td>
      <td>RRID:SCR_016752</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>DESeq2</td>
      <td>10.1186/s13059-014-0550-8</td>
      <td>RRID:SCR_015687</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Alevin</td>
      <td>10.1186/s13059-019-1670-y</td>
      <td>https://salmon.readthedocs.io</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Seurat</td>
      <td>https://doi.org/10.1038/nbt.4096</td>
      <td>http://satijalab.org/seurat/</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>ggplot2</td>
      <td>https://github.com/tidyverse/ggplot2</td>
      <td>RRID:SCR_014601</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Pandas</td>
      <td>https://pandas.pydata.org</td>
      <td>RRID:SCR_018214</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Scikit-learn</td>
      <td>http://scikit-learn.org/</td>
      <td>RRID:SCR_002577</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Python Seaborn</td>
      <td>https://seaborn.pydata.org/</td>
      <td>RRID:SCR_018132</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Java Treeview</td>
      <td>10.1093/bioinformatics/bth349</td>
      <td>RRID:SCR_016916</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Cluster 3.0</td>
      <td>10.1093/bioinformatics/bth078</td>
      <td>RRID:SCR_013505</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>REViGO</td>
      <td>http://revigo.irb.hr/</td>
      <td>RRID:SCR_005825</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Generic GO Term Finder</td>
      <td>10.1093/bioinformatics/bth456</td>
      <td>RRID:SCR_008870</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MEME-suite</td>
      <td>http://meme-suite.org/</td>
      <td>RRID:SCR_001783</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>FCS Express 7</td>
      <td>https://www.denovosoftware.com</td>
      <td>RRID:SCR_016431</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Cell isolation

FLs were dissected from embryonic day E13.5 embryos and mechanically dispersed into single cells for fluorescence activated cell sorting (FACS) or RNA isolation. The heterozygous EKLF mouse strain was as described (Perkins et al., 1995). Photos were taken with a Nikon Microphot-FX fluorescence microscope equipped with a Q-Imaging camera or with a Zeiss Axio Observer Z1 equipped with a Hamamatsu C11440 camera. For single-cell sequencing, wild-type E13.5 FL cells were isolated from two littermate embryos from one donor mother, stained with anti-F4/80-PE antibody (eBiosciences #12-4801-80) and isolated using an EasySep mouse PE positive selection kit that uses a magnetic bead-based purification strategy (Cell Signaling Technologies #17656) and in the presence of 2 mM Icam4/αv inhibitor peptide (Xue et al., 2014) to eliminate macrophage–erythroid interactions. The cells were selected by repeating the magnetic bead binding step to increase purity. For immunofluorescence, erythroblastic island clusters were enriched from dispersed E13.5 FLs using a serum gradient as previously described (Xue et al., 2014).

### Flow cytometry

Suspended cells from FLs were stained for FACS with the following antibodies: anti-mouse F4/80-PE (eBiosciences #12-4801-80), anti-Adra2b (Alomone Labs #AAR-021), anti-adducinβ (Santa Cruz # sc-376063), and anti-spectrinβ1 (Santa Cruz # sc-374309). For anti-Adra2b staining, we used an Alexa 647 conjugated Donkey anti-rabbit secondary antibody (Life Technologies). For adducinβ and spectrinβ1 staining, primary unconjugated antibodies were conjugated to AlexaFluor 647 using a primary antibody conjugation kit (Invitrogen # Z11235). Flow cytometry data was analyzed by FCS Express software, and gates were drawn based on unstained and single-color compensation controls from the same samples, using the same dyes and within the same experiment.

### Imagestream analysis

Cells from intact E13.5 FLs were isolated from the pEKLF/GFP mouse and stained with the same antibodies for F4/80 and adducinβ as above, except the primary unconjugated antibody was labeled with a Texas Red labeling kit (Abcam #ab195225). Data was acquired using a Luminex Amnis Imagestream MkII Imaging Flow Cytometer and analyzed using the Amnis Ideas Software.

### Immunofluorescence

Erythroblastic island clusters were stained for F4/80 along with Add2 and Sptb using antibodies labeled as described above for flow cytometry. Photography was performed with a Nikon Microphot-FX fluorescence microscope equipped with a Q-Imaging camera.

### RNA isolation and RNA-Seq

FACS sorted cells were directly suspended in Trizol, and total RNA was extracted (Rio et al., 2010). RIN values for all EKLF+/+ and EKLF-/- samples were between 9.1 and 9.8. Poly-A library preparations of biological triplicate samples were analyzed by 100 nt single reads on an Illumina HiSeq 2500 or Illumina Novaseq, 60–90 million reads per sample. For F4/80+ EKLF/GFP+ population, the low cell numbers led us to use an Agilent RNA Nanoprep kit (#400753) for isolating reasonably good-quality RNA (RIN ~7). RNA-Seq data has been submitted to the Gene Expression Omnibus.

### Single-cell RNA-Seq

Libraries were generated from purified F4/80-PE+ using Chromium Single Cell 3′ Reagent Kit V3 (10X Genomics) to generate cDNA and barcoded indexes for 25,000 individual cells. Paired-end sequencing was performed using a Novaseq instrument.

### Bioinformatics and computational analysis

RNA-Seq reads were aligned using STAR (Dobin et al., 2013) to the mouse genome (mm10) or mapped using Salmon (Patro et al., 2017) to the mouse transcriptome (Ensembl GRCm38). Htseq-count (Anders et al., 2015) was used to generate gene-specific raw counts from the STAR-aligned reads. Raw counts from these programs were imported using tximport package, and count normalization and differential gene expression analysis was performed using DESeq2 (Love et al., 2014). Hierarchical clustering and PCA (Figure 1A, B) were performed using R (http://www.R-project.org/) or Python Pandas (https://pandas.pydata.org) and Scikit-learn (https://scikit-learn.org, Figure 3D). All plots were generated using either R ggplot2 (https://ggplot2.tidyverse.org) or Python Seaborn (https://seaborn.pydata.org) and Plotnine (https://plotnine.readthedocs.io) libraries. k-means clustering was performed using Cluster 3.0 software (de Hoon et al., 2004), and heatmaps were generated using Java Treeview (Saldanha, 2004, Figures 1D and 3B) and Python Seaborn (all others). R and Python code used in the analysis is deposited in github (https://github.com/mkaustav84/biekerlab-f480_macrophage; copy archived at swh:1:rev:907b15e74d998c5dd2a3106bce30af812c2b60b4.

Single-cell sequencing reads were aligned to the mouse transcriptome build GRCm38.p6vM24 using the software Alevin (Srivastava et al., 2019), and subsequent analysis was performed using the Seurat package (R-based) with built-in functions for plotting, clustering, PCA, and U-MAP analysis. After filtering, 3066 cells were retained, and for each cell 4000 variable genes were considered for analysis.

Motif analysis was performed using the Centrimo program (http://www.meme-suite.org/). Promoter sequences from −300 to +100 were extracted using a specific Perl script of Homer for the target EKLF-dependent gene set, and the promoters of the rest of the coding genes in the genome were used as background. GO analysis (go.princeton.edu) was performed using GO::TermFinder (Boyle et al., 2004), and GO terms were distilled using REVIGO (Jiang and Conrad similarity).
