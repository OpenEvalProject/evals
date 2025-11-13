# Differential regulation by CD47 and thrombospondin-1 of extramedullary erythropoiesis in mouse spleen

## Authors

- Rajdeep Banerjee<sup>1</sup> ([ORCID: 0009-0007-0878-2034](https://orcid.org/0009-0007-0878-2034))
- Thomas J Meyer<sup>2</sup> ([ORCID: 0000-0002-7185-5597](https://orcid.org/0000-0002-7185-5597))
- Margaret C Cam<sup>2</sup> ([ORCID: 0000-0001-8190-9766](https://orcid.org/0000-0001-8190-9766))
- Sukhbir Kaur<sup>1</sup>
- David D Roberts<sup>1</sup> ([ORCID: 0000-0002-2481-2981](https://orcid.org/0000-0002-2481-2981)) †

### Affiliations

1. Laboratory of Pathology, Center for Cancer Research, National Cancer Institute, National Institutes of Health Bethesda United States ([ROR:040gcmg81](https://ror.org/040gcmg81))
2. CCR Collaborative Bioinformatics Resource, Office of Science and Technology Resources, National Cancer Institute, National Institutes of Health Bethesda United States ([ROR:040gcmg81](https://ror.org/040gcmg81))

† Corresponding author

## Abstract

Extramedullary erythropoiesis is not expected in healthy adult mice, but erythropoietic gene expression was elevated in lineage-depleted spleen cells from Cd47−/− mice. Expression of several genes associated with early stages of erythropoiesis was elevated in mice lacking CD47 or its signaling ligand thrombospondin-1, consistent with previous evidence that this signaling pathway inhibits expression of multipotent stem cell transcription factors in spleen. In contrast, cells expressing markers of committed erythroid progenitors were more abundant in Cd47−/− spleens but significantly depleted in Thbs1−/− spleens. Single-cell transcriptome and flow cytometry analyses indicated that loss of CD47 is associated with accumulation and increased proliferation in spleen of Ter119−CD34+ progenitors and Ter119+CD34− committed erythroid progenitors with elevated mRNA expression of Kit, Ermap, and Tfrc. Induction of committed erythroid precursors is consistent with the known function of CD47 to limit the phagocytic removal of aged erythrocytes. Conversely, loss of thrombospondin-1 delays the turnover of aged red blood cells, which may account for the suppression of committed erythroid precursors in Thbs1−/− spleens relative to basal levels in wild-type mice. In addition to defining a role for CD47 to limit extramedullary erythropoiesis, these studies reveal a thrombospondin-1-dependent basal level of extramedullary erythropoiesis in adult mouse spleen.

## Introduction

CD47 is a counter-receptor for signal-regulatory protein-α (SIRPα; Matozaki et al., 2009) and a component of a supramolecular membrane signaling complex for thrombospondin-1 that contains specific integrins, heterotrimeric G proteins, tyrosine kinase receptors, exportin-1, and ubiquilins (Gao et al., 1996; Isenberg et al., 2009; Kaur et al., 2022; Soto-Pantoja et al., 2015). CD47 binding to SIRPα on macrophages induces inhibitory signaling mediated by its cytoplasmic immunoreceptor tyrosine-based inhibition motifs that recruit and activate the tyrosine phosphatases SHP-1 and SHP-2 (Matozaki et al., 2009). Loss of this inhibitory signaling results in rapid splenic clearance of Cd47−/− mouse red blood cells (RBC) when transfused into a wild type (WT) recipient (Oldenborg et al., 2000). The species-specificity of CD47/SIRPα binding constitutes a barrier to interspecies blood transfusion and hematopoietic reconstitution (Strowig et al., 2011; Wang et al., 2007).

CD47 forms nanoclusters on young RBC with limited binding to thrombospondin-1 (Wang et al., 2020). CD47 abundance decreases on aged RBCs, but CD47 on aging RBC forms larger and more dense clusters with increased ability to bind thrombospondin-1. CD47 on aging RBC also adopts an altered conformation (Burger et al., 2012). Exposure of aged RBC to thrombospondin-1 further increases the size of CD47 clusters via a lipid-raft-dependent mechanism. Conversely, CD47 cluster formation was limited on Thbs1−/− mouse RBC and associated with significantly increased RBC lifespan (Wang et al., 2020).

Liver and spleen are the main hematopoietic organs during embryonic development, whereas bone marrow assumes that responsibility after birth (Kim, 2010). Induction of extramedullary hematopoiesis in adult spleen can compensate for pathological conditions that compromise hematopoiesis in bone marrow (Cenariu et al., 2021). CD47 is highly expressed on proliferating erythroblasts during stress-induced erythropoiesis, and antibodies blocking either CD47 or SIRPα inhibited the required transfer of mitochondria from macrophages to developing erythroblasts in erythroblastic islands (Yang et al., 2022). Notably, treatment with a CD47 antibody enhanced splenomegaly in the anemic stress model. Consistent with the absence of inhibitory SIRPα signaling that limits clearance of aged RBC (Fossati-Jimack et al., 2002; Lutz and Bogdanova, 2013), Cd47−/− mice derived using CRISPR/Cas9 exhibited hemolytic anemia and splenomegaly (Kim et al., 2018). Conversely, CD47-dependent thrombospondin-1 signaling regulates the differentiation of multipotent stem cells in a stage-specific manner (Kaur et al., 2013; Nath et al., 2018; Porpiglia et al., 2022). and both Thbs1−/− and Cd47−/− mouse spleens have more abundant Sox2+ stem cells and higher mRNA expression of the multipotent stem cell transcription factors Myc, Sox2, Oct4, and Klf4 (Kaur et al., 2013). Therefore, both thrombospondin-1- and SIRPα-dependent CD47 signaling could alter erythropoiesis and contribute to spleen enlargement. Here, we utilized flow cytometry combined with bulk and single-cell transcriptomics to examine extramedullary hematopoiesis in Cd47−/− and Thbs1−/− mice, which revealed cooperative and opposing roles for CD47 and thrombospondin-1 to limit extramedullary erythropoiesis in spleen.

## Results

### Upregulation of erythroid precursors in Cd47−/− mouse spleen

We confirmed the previously reported spleen enlargement in Cd47−/− mice (Bian et al., 2016; Nath et al., 2018), but we did not observe significant spleen enlargement in Thbs1−/− mice (Figure 1—figure supplement 1A). Enlargement of Cd47−/− spleens could result from increased phagocytic clearance of RBC, as reported in Cd47−/− and Sirpa−/− mice treated with CpG (Kidder et al., 2020) and aging Cd47−/− mice (Kim et al., 2018). Alternatively, increased cell numbers could result from the increased stem cell abundance in Cd47−/− spleens (Kaur et al., 2013). The spleen enlargement was associated with a significantly higher total spleen cell number in a single cell suspension after RBC lysis in Cd47−/− mice compared to WT and Thbs1−/− mice (Figure 1A).

![Figure 1.](https://cdn.elifesciences.org/articles/92679/elife-92679-fig1-v1.jpg)

**Figure 1.:** (A) Total spleen cell numbers in WT, Cd47−/− and Thbs1−/− C57BL/6 mice determined after lysis of RBC (mean ± SEM, n=3). Flow cytometry was performed to analyze gated singlet spleen cells stained with Ter119 antibody (B), CD34 antibody (C), Sca1 antibody (D), Ki67 antibody with the indicated gating for high and low expression (E), cKit antibody (F), Epor antibody (G), Ermap antibody (H), Gypa antibody (I), or Aqp1 antibody (J). Further analysis of Epor (K, O), Ermap (L, P), Gypa (M, Q), and Aqp1 expression (N, R) was performed after gating for Ter119 expression. The percentages of cells positive for the indicated surface markers are presented (n=3 or 4 mice of each genotype). p-values were determined using a two-tailed t test for two-samples assuming equal variances in GraphPad Prism. *=p < 0.05, **=p < 0.01, ***=p < 0.001.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/92679/elife-92679-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** (A) Representative images of spleens from WT, Cd47−/−, and Thbs1−/− mice. (B) Volcano plot for differentially expressed genes between lineage-depleted Naive Cd47−/− vs WT CD8+-enriched spleen cells. Red dots represent significant genes with >2 fold change and p<0.001, and the top 30 genes were labelled. (C) GSEA plot showing RBC Heme Metabolism gene set enrichment. (D) Heat map visualization of the top differentially expressed genes in the RBC Heme Metabolism gene set.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/92679/elife-92679-fig1-figsupp2-v1.jpg)

**Figure 1—figure supplement 2.:** The sequential flow cytometry gating strategy is illustrated.

Our previous analysis of lineage-negative cells from WT and Cd47−/− spleens identified an increased abundance of NK cell precursors in Cd47−/− spleens (Nath et al., 2018). Analysis of bulk RNAseq data of naïve WT and Cd47−/− spleen cells depleted for proerythroblasts through mature erythrocytes using the antibody Ter-119 (Kina et al., 2000) and for cells bearing CD4, CD11b, CD11c, CD19, CD45R, CD49b, CD105, MHC Class II, and TCRγ/δ (Lin−CD8+) unexpectedly showed strong enrichment of a heme metabolism gene signature (Figure 1—figure supplement 1C), markers of stress-induced erythropoiesis (Delic et al., 2020; Thompson et al., 2010) and adult definitive erythropoiesis (Kingsley et al., 2013) in the lineage-depleted Cd47−/− relative to the corresponding cells from WT spleens (Table 1, Figure 1—figure supplement 1B and D). Trim10 mRNA, which encodes an erythroid-specific RING finger protein required for terminal erythroid differentiation (Harada et al., 1999), was elevated 50-fold. Higher Mki67 mRNA expression suggested increased proliferation among Lin− Cd47−/− spleen cells, which also expressed elevated mRNA levels of the major erythroid transcription factor Gata1 (Gutiérrez et al., 2020). Apart from increased Kit mRNA expression, however, mRNA expression of markers for multipotent erythroid progenitors including Anpep (CD13), Cd33, Sca1 and Gata2 was not elevated in the absence of CD47. These data suggested preferential accumulation of committed erythroid progenitors rather than multipotent erythroid progenitors in the Cd47−/− spleens. CD47 regulates activities of the nuclear transport protein exportin-1 (Kaur et al., 2022), and Xpo1 mRNA was also increased in Cd47−/− cells (Table 1). Exportin-1 is a Gata1 transcriptional target and promotes terminal erythroid differentiation by maintaining Gata1 in the nucleus (Guillem et al., 2020), which suggested a potential mechanism by which loss of CD47 could increase erythropoiesis.

**Table 1.**
 Expression of erythropoiesis-associated genes in lineage-depleted Cd47−/− versus WT spleen cells.


<table>
  <thead>
    <tr>
      <th>Gene</th>
      <th>Erythropoiesis expression/function</th>
      <th>Fold change Cd47-/-/WT*</th>
      <th>T statistic</th>
      <th>p-value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Ermap</td>
      <td>extramedullary erythropoiesis marker†</td>
      <td>21.5</td>
      <td>6.04</td>
      <td>9.35x10–5</td>
    </tr>
    <tr>
      <td>Tal1</td>
      <td>extramedullary erythropoiesis marker†</td>
      <td>13.9</td>
      <td>5.13</td>
      <td>3.55x10–4</td>
    </tr>
    <tr>
      <td>Gypa</td>
      <td>extramedullary erythropoiesis marker†</td>
      <td>89.3</td>
      <td>3.67</td>
      <td>3.86x10–3</td>
    </tr>
    <tr>
      <td>Gata1</td>
      <td>extramedullary erythropoiesis marker†</td>
      <td>7.69</td>
      <td>4.86</td>
      <td>5.38x10–4</td>
    </tr>
    <tr>
      <td>Kel</td>
      <td>extramedullary erythropoiesis marker†</td>
      <td>29.0</td>
      <td>4.61</td>
      <td>8.04x10–4</td>
    </tr>
    <tr>
      <td>Slc4a1</td>
      <td>extramedullary erythropoiesis marker†</td>
      <td>151.4</td>
      <td>4.90</td>
      <td>5.05x10–4</td>
    </tr>
    <tr>
      <td>Klf1</td>
      <td>extramedullary erythropoiesis marker†</td>
      <td>20.6</td>
      <td>5.06</td>
      <td>3.95x10–4</td>
    </tr>
    <tr>
      <td>Cldn13</td>
      <td>extramedullary erythropoiesis marker†</td>
      <td>49.2</td>
      <td>4.42</td>
      <td>1.09x10–3</td>
    </tr>
    <tr>
      <td>Trim10</td>
      <td>extramedullary erythropoiesis marker†</td>
      <td>49.7</td>
      <td>4.11</td>
      <td>1.83x10–3</td>
    </tr>
    <tr>
      <td>Epor</td>
      <td>extramedullary erythropoiesis marker†</td>
      <td>12.3</td>
      <td>4.91</td>
      <td>5.01x10–4</td>
    </tr>
    <tr>
      <td>Sptb</td>
      <td>extramedullary erythropoiesis marker†</td>
      <td>36.5</td>
      <td>5.21</td>
      <td>3.16x10–4</td>
    </tr>
    <tr>
      <td>Rhag</td>
      <td>extramedullary erythropoiesis marker†</td>
      <td>33.0</td>
      <td>4.64</td>
      <td>7.68x10–4</td>
    </tr>
    <tr>
      <td>Hba-a1</td>
      <td>erythroblasts</td>
      <td>63.8</td>
      <td>6.46</td>
      <td>5.23x10–5</td>
    </tr>
    <tr>
      <td>Hbb-bs</td>
      <td>erythroblasts</td>
      <td>59.2</td>
      <td>6.60</td>
      <td>4.34x10–5</td>
    </tr>
    <tr>
      <td>Gata1</td>
      <td>BFU-E through erythroblasts</td>
      <td>7.69</td>
      <td>4.86</td>
      <td>5.38x10–4</td>
    </tr>
    <tr>
      <td>Tfrc (CD71)</td>
      <td>CFU-E through erythroblasts</td>
      <td>3.12</td>
      <td>6.19</td>
      <td>7.58x10–5</td>
    </tr>
    <tr>
      <td>Kit</td>
      <td>Progenitors through CFU-E</td>
      <td>1.72</td>
      <td>6.24</td>
      <td>7.02x10–5</td>
    </tr>
    <tr>
      <td>Sox6</td>
      <td>Adult definitive erythropoiesis</td>
      <td>35.5</td>
      <td>3.56</td>
      <td>0.0046</td>
    </tr>
    <tr>
      <td>Aqp1</td>
      <td>Adult definitive erythropoiesis</td>
      <td>26.9</td>
      <td>6.51</td>
      <td>4.91x10–5</td>
    </tr>
    <tr>
      <td>Nr3c1</td>
      <td>Adult definitive erythropoiesis</td>
      <td>1.12</td>
      <td>2.80</td>
      <td>0.018</td>
    </tr>
    <tr>
      <td>Mki67</td>
      <td>Proliferation marker</td>
      <td>4.43</td>
      <td>7.65</td>
      <td>1.14x10–5</td>
    </tr>
    <tr>
      <td>Cd34</td>
      <td>Multipotent progenitors through CFU-E</td>
      <td>1.60</td>
      <td>1.59</td>
      <td>0.141</td>
    </tr>
    <tr>
      <td>Ly6a (Sca1)</td>
      <td>Multipotent progenitors</td>
      <td>1.17</td>
      <td>1.02</td>
      <td>0.331</td>
    </tr>
    <tr>
      <td>Anpep (CD13)</td>
      <td>Multipotent progenitors</td>
      <td>1.16</td>
      <td>1.14</td>
      <td>0.28</td>
    </tr>
    <tr>
      <td>Cd33</td>
      <td>Multipotent progenitors</td>
      <td>–1.06</td>
      <td>–0.37</td>
      <td>0.71</td>
    </tr>
    <tr>
      <td>Gata2</td>
      <td>Multipotent progenitors</td>
      <td>1.08</td>
      <td>0.66</td>
      <td>0.52</td>
    </tr>
    <tr>
      <td>Xpo1</td>
      <td>Stability of nuclear Gata1</td>
      <td>1.23</td>
      <td>3.86</td>
      <td>2.7x10–3</td>
    </tr>
  </tbody>
</table>

_*Gene enrichment in naïve Cd47−/− vs WT spleen cells depleted for CD4, CD11b, CD11c, CD19, CD45R (B220), CD49b (DX5), CD105, MHC Class II, Ter-119, and TCRγ/δ.†Reported markers of stress-induced extramedullary erythropoiesis (Delic et al., 2020; Thompson et al., 2010)._

To further characterize CD47-dependent spleen cells and the relevance of thrombospondin-1, single cell suspensions of depleted of mature RBC were analyzed using flow cytometry for expression of erythropoiesis-related cell surface and proliferation markers (Figure 1B–J, Figure 1—figure supplement 2). The percentages of Ter119+ cells in singlet cells from Cd47−/− spleens was significantly higher than in WT or Thbs1−/− spleens (p=0.0061 and 0.0322 respectively, Figure 1B). CD34 is expressed on multipotent through the CFU-E erythroid progenitors and was expressed a significantly higher percentage on Cd47−/− versus WT or Thbs1−/− cells (p=0.0008 and 0.0001 respectively, Figure 1C), whereas the multipotent progenitor marker Sca1 was expressed in a smaller percentage of Cd47−/− versus WT or Thbs1−/− spleen cells (p=0.0001 and 0.0009 respectively, Figure 1D).

A higher percentage of Cd47−/− cells expressed the proliferation marker Ki67 at low but not high levels compared to WT or Thbs1−/− spleen cells (p=0.0024 and 0.0003 respectively, Figure 1E). c-Kit signaling is crucial for normal hematopoiesis and is expressed in multipotent progenitors through CFU-E (Lennartsson and Rönnstrand, 2012; Swaminathan et al., 2022), but the percentage of cKit positive cells was higher only in Thbs1−/− spleen cells (Figure 1F).

Erythrocyte lineage markers including Ermap, glycophorin A (Gypa), Epor and Aqp1 are established markers of stress-induced extramedullary erythropoiesis (Delic et al., 2020). The erythropoietin receptor (Epor), which is expressed in CFU-E through proerythroblasts, was expressed in significantly more Cd47−/− versus WT spleen cells (p=0.0077) but in significantly fewer Thbs1−/− spleen cells (p=0.0017 Figure 1G). Cells expressing the major RBC membrane glycoprotein Gypa, which accumulates in erythroblasts, Ermap, and Aqp1 showed similar significant increases in Cd47−/− spleen cells, whereas only Gypa+ and Aqp1+ cells were significantly decreased in Thbs1−/− spleen cells (Figure 1H, I and J). Consistent with their known induction kinetics, most of the cells expressing these markers were Ter119+, and the alterations in their abundance observed in Cd47−/− and Thbs1−/− spleens were restricted to Ter119+ cells (Figure 1K–R). These results indicate an increased abundance of committed erythroid progenitors spanning CD34+ progenitors through reticulocytes in the Cd47−/− spleen but depletion of the earlier Sca1+ multipotent progenitors. Consistent with the decreased turnover of Thbs1−/− RBC (Wang et al., 2020), cells expressing the committed erythroid markers Gypa, Epor, and Aqp1 were depleted in Thbs1−/− spleens.

Erythropoietin binding to Epor on early erythroid precursor cells stimulates their survival, proliferation, and differentiation by inducing the master transcriptional regulators Tal1, Gata1, and Klf1 (Perreault and Venters, 2018). Tal1, Gata1, and Klf1, and Epor mRNAs were strongly up-regulated in Cd47−/− relative to WT spleens (Table 1). The increased proliferative response in the Cd47−/− cells is consistent with a significant increase in Epor+ Ter119+ Cd47−/− cells, contrasting with a significant decrease in their abundance in Ter119+ Thbs1−/− cells (Figure 1K). Epor expression was minimal and unchanged in the Ter119− population (Figure 1O), indicating that the Ter119 antigen is expressed in erythroid precursors that are responsive to erythropoietin. These data are consistent with increased extramedullary erythropoiesis in Cd47−/− and suppressed extramedullary erythropoiesis relative to WT in Thbs1−/− spleens.

### CD47-dependence of erythropoietic markers in Ter119+ and Ter119− cells

The Ter119 antibody recognizes an antigen highly expressed in mouse proerythroblasts through mature erythrocytes (Kina et al., 2000). Although Ter119 is a widely used erythroid lineage marker, its epitope does not map to a specific protein (Kina et al., 2000) and requires 9-O-acetylation of sialic acids that are present on several RBC glycoproteins (Mahajan et al., 2019). Although no effect of CD47 on the abundance of cKit+ cells was detected (Figure 1F), Kit mRNA was significantly enriched in lineage-negative Cd47−/− spleen cells (Table 1). To resolve this discrepancy, the percentage of cKit+ cells was assessed in Ter119+ and Ter119− populations (Figure 2A, Figure 2—figure supplement 1). A higher percentage of the Cd47−/− cells were Ter119+cKit+. Consistent with Figure 1F and the elevation of multipotent stem cells in Thbs1−/− spleen (Kaur et al., 2013), Ter119−cKit+ cells were elevated in Thbs1−/− spleens. Consistent with the bulk RNA sequencing data, Sca1+ cells in spleen did not differ in the Ter119+ cells and were less abundant in Ter119− cells from Cd47−/− spleens relative to the same subset from WT (Figure 2B). Consistent with the negative regulation of stem cell transcription factors in spleen by CD47-dependent thrombospondin-1 signaling (Kaur et al., 2013), these results support prior evidence that that loss of Thbs1 or Cd47 results in accumulation of early hematopoietic precursors that are Ter119− and demonstrates a Cd47−/−-specific enrichment of cKit+Ter119+ committed erythroid precursors. Proliferating cells with low Ki67 expression were more abundant in the Ter119+ and Ter119− populations of Cd47−/− cells relative to WT and Thbs1−/− cells, suggesting that loss of Cd47 but not Thbs1 increases the proliferation of committed erythroid precursors (Figure 2C and D).

![Figure 2.](https://cdn.elifesciences.org/articles/92679/elife-92679-fig2-v1.jpg)

**Figure 2.:** Spleen cells isolated from WT, Cd47−/− and Thbs1−/− mice (2 male and 2 female of each genotype) were costained with Ter119 antibody along with cKit, Ki67, Sca1 Ermap, Gypa, Epor, or Aqp1 antibodies and acquired on an LSRFortessa SORP. After gating for singlet cells, the percentages of Ter119+ and Ter119− cells positive for stem cell markers cKit (A) and Sca1 (B), high or low levels of the proliferation marker Ki67 (C, D), were compared among WT, Cd47−/− and Thbs1−/− mouse spleens (n=3–4). The proliferation of CD34+ and CD34− populations of Ter119+ spleen cells from WT, Cd47−/−, Thbs1−/− mice was evaluated by staining with CD34, Ter119 and Ki67 antibodies. Ter119+CD34+ cells (E), Ter119+CD34− cells (F), and Ter119−CD34+ cells (G) were also quantified (left panels) and analyzed for the proliferation marker Ki67 (center and right panels). p-values were determined using a two-tailed t test for two-samples assuming equal variances in GraphPad Prism. *=p < 0.05, **=p < 0.01, ***=p < 0.001.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/92679/elife-92679-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** The sequential flow cytometry gating strategy is illustrated.

### CD47 limits proliferation of Ter119+CD34− and Ter119−CD34+ spleen cells

Although Figure 1 demonstrated increased numbers of Ter119+ and CD34+ cells in Cd47−/− spleens, further analysis revealed that more CD34+ cells are Ter119− than Ter119+ (Figure 2E and G, left panels). Therefore, loss of CD47 upregulates both early Ter119−CD34+ progenitors and more mature Ter119+ progenitors, most of which have lost CD34 expression (Figure 2F). Most of the increased proliferation of Cd47−/− spleen cells, indicated by Ki67 expression, was in the Ter119+CD34− subset (Figure 2F, center and right panels), but proliferating Cd47−/− cells were also enriched in the Ter119−CD34+ population (Figure 2G). These data indicate roles for more differentiated Ter119+CD34− erythroid progenitors as well as earlier Ter119−CD34+ erythroid progenitors in mediating the increased extramedullary erythropoiesis in Cd47−/− spleens.

### Identification of CD47-dependent erythroid precursor populations

Single cell RNA sequencing (scRNAseq) was used to further define effects of CD47 and thrombospondin-1 on erythroid precursors in spleen (Figure 3, Figure 3—figure supplement 1). Spleen cells from WT, Cd47−/− and Thbs1−/− mice were treated with immobilized antibodies to deplete monocytic, T, B, and NK cell lineages and mature RBC and subjected to scRNAseq analysis. Following alignment, the mRNA expression data were clustered in two dimensions using the t-distributed stochastic neighbor embedding (tSNE) method in NIDAP. Using a resolution of 0.4, the spleen cells clustered in 18 groups (Figure 3A).

![Figure 3.](https://cdn.elifesciences.org/articles/92679/elife-92679-fig3-v1.jpg)

**Figure 3.:** (A) tSNE clustering analysis of lineage-depleted spleen cells from WT, Cd47−/− and Thbs1−/−mice (n = 3). The encircled area contains erythroid cells (clusters 12) and stem cells (cluster 14). (B) Cell type analysis using Immgen and Mouse RNAseq and SingleR (v.1.0) databases. (C) Distribution of WT, Cd47−/− and Thbs1−/− spleen cells in each cluster of the tSNE plot. (D) Enlarged plots of clusters 12 and 14 and cells in these clusters colored by genotype.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/92679/elife-92679-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** The scatter plots, histograms and violin plots of three samples lineage-depleted of WT, Cd47−/− and Thbs1−/− spleen cells are shown. The number of UMI per cell filter was set to exclude cells with <2000 UMI in nCount RNA. The Feature RNA plot shows the number of genes with non-zero expression detected per cell. Filtering was set to exclude cells having <15% mitochondrial gene expression as presented in the percent mt plot. The log10Genes per UMI plot represents the scores for complexity of the RNA library found in each cell. No filter was set in this row.

Cell type analysis using SingleR with Immgen and mouse RNAseq databases identified the main cell types in each cluster (Figure 3B). Immgen main cell type annotation identified cluster 12 and a subset of cluster 14 as stem cells, and mouse RNA seq annotation identified erythrocyte signatures mostly in cluster 12. WT, Cd47−/−, and Thbs1−/− cells clustered by genotype in the major residual T cell clusters 0 through 5 but had similar distributions within clusters 12 and 14 (Figure 3C and D).

Erythroid lineage markers were found mainly in cluster 12, which contained 440 cells (Figure 4 and Figure 4—figure supplements 1 and 2). Consistent with the flow data in Figures 1 and 2, Cd47−/− cells were more abundant in cluster 12 (65%), and Thbs1−/− cells were less abundant (15%) than WT cells (21%). CD34 was expressed mostly in cluster 14 and to lower parts of cluster 12, whereas Ly6a (Sca1) was restricted to isolated cells in both clusters. Kit and Gata2, which are expressed by multipotent progenitors through CFU-E, were expressed in lower and middle areas of cluster 12 and to a limited degree in cluster 14 (Figure 4). The extramedullary erythropoiesis markers Epor, Gata1, Klf1, and Ermap, the definitive erythropoiesis marker Aqp1 and the proliferation marker Ki67 had similar distributions in cluster 12 (Figure 4). Trim10 and the late erythroid markers Gypa, Tmem56, Epb42, Spta1, and Sptb were restricted to the upper regions of cluster 12 (Figure 4). Therefore, erythroid differentiation within cluster 12 correlates with increasing TSNE-2 scores.

![Figure 4.](https://cdn.elifesciences.org/articles/92679/elife-92679-fig4-v1.jpg)

**Figure 4.:** High resolution tSNE plots showing the distribution of mRNAs encoding the multipotent stem cell markers CD34 and Ly6a (Sca1) and Gata2, the erythropoietic markers Kit and Epor, the proliferation marker Mki67, erythroid differentiation transcription factors Klf1 and Gata1, and erythroid differentiation and extramedullary erythropoiesis markers Ermap, Aqp1, Tmem56, Trim10, Gypa1, Spta1, Sptb, Ebp42, Xpo1, and RanBP2 in clusters 12 and 14. Expression levels were normalized to maximum expression of each mRNA in these clusters.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/92679/elife-92679-fig4-figsupp1-v1.jpg)

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/92679/elife-92679-fig4-figsupp2-v1.jpg)

**Figure 4—figure supplement 2.:** Data are from two female and one male mouse of each genotype.

Similar high percentages of WT and Cd47−/− cells within cluster 12 expressed the erythroid lineage markers Klf1, Aqp1, Epor, Ermap, and Gata1, but percentages for Klf1, Epor, and Gata1 were lower in Thbs1−/− cells (Figure 4—source data 1). Expression of the erythroid genes Klf1, Aqp1, Epor, Ermap, and Gata1 was not detected in the stem cell cluster 14 (Figure 4—source data 1). The average mRNA/cell for Tfrc and Ermap was significantly higher in Cd47−/− cells, whereas mRNAs encoding Klf1, Aqp1, Epor, and Gata1 were significantly lower in Thbs1−/− cells compared to WT (Figure 5A, Table 2). Violin plots indicated that cells with the highest Mki67 mRNA expression were more abundant in Cd47−/− cells in cluster 12, and the average expression was higher (p=9.2 × 10–6), but cells with high and low Mki67 had similar distributions in Thbs1−/− and WT cells (Figure 5A). Mki67 expression levels were lower in cluster 14, and Cd47−/− cells had higher mean expression that WT, but Thbs1−/− cells had lower Mki67 expression than WT (Table 2). Expression of Kit was also higher in Cd47−/− versus WT cells in cluster 12 (p=0.0015). Although more Cd47−/− cells expressed Gata1 (Figure 4—source data 1), its mean expression was not higher than in WT cells.

![Figure 5.](https://cdn.elifesciences.org/articles/92679/elife-92679-fig5-v1.jpg)

**Figure 5.:** (A) Violin plots comparing mRNA expression levels of the indicated genes in Cd47−/−(red), Thbs1−/−(blue) and WT spleen cells (green) in cluster 12. (B) Violin plots comparing mRNA expression levels of the indicated genes in Cd47−/−, Thbs1−/−, and WT spleen cells in cluster 14. *=p < 0.05 relative to WT cells in the respective cluster. n = 2 female and 1 male mice of each genotype; *=p < 0.05.

**Table 2.**
 Differential mRNA expression of erythropoietic, stem cell, and proliferation associated markers in WT, Cd47−/−, and Thbs1−/− cells in clusters 12 and 14.


<table>
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th colspan="2">Cd47−/− vs WT</th>
      <th colspan="2">Thbs1−/− vs WT</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Cluster</td>
      <td>Gene</td>
      <td>p-value</td>
      <td>Avg log2 FC</td>
      <td>p-value</td>
      <td>Avg log2 FC</td>
    </tr>
    <tr>
      <td>12</td>
      <td>Klf1</td>
      <td>0.463</td>
      <td>–0.115</td>
      <td>0.0023</td>
      <td>–0.510</td>
    </tr>
    <tr>
      <td>12</td>
      <td>Aqp1</td>
      <td>0.331</td>
      <td>–0.130</td>
      <td>0.0011</td>
      <td>–0.472</td>
    </tr>
    <tr>
      <td>12</td>
      <td>Tfrc</td>
      <td>0.017</td>
      <td>0.531</td>
      <td>0.93</td>
      <td>0.009</td>
    </tr>
    <tr>
      <td>14</td>
      <td>Tfrc</td>
      <td>0.64</td>
      <td>0.071</td>
      <td>0.922</td>
      <td>0.016</td>
    </tr>
    <tr>
      <td>12</td>
      <td>Epor</td>
      <td>0.506</td>
      <td>–0.078</td>
      <td>4.75x10–5</td>
      <td>–0.576</td>
    </tr>
    <tr>
      <td>12</td>
      <td>Ermap</td>
      <td>5.1x10–3</td>
      <td>0.309</td>
      <td>0.65</td>
      <td>–0.073</td>
    </tr>
    <tr>
      <td>12</td>
      <td>Gata1</td>
      <td>0.57</td>
      <td>0.007</td>
      <td>0.0011</td>
      <td>–0.377</td>
    </tr>
    <tr>
      <td>12</td>
      <td>Mki67</td>
      <td>9.16x10–6</td>
      <td>0.997</td>
      <td>0.22</td>
      <td>0.456</td>
    </tr>
    <tr>
      <td>14</td>
      <td>Mki67</td>
      <td>0.0089</td>
      <td>0.798</td>
      <td>0.0017</td>
      <td>–0.062</td>
    </tr>
    <tr>
      <td>12</td>
      <td>Kit</td>
      <td>0.0015</td>
      <td>0.331</td>
      <td>0.057</td>
      <td>0.264</td>
    </tr>
    <tr>
      <td>14</td>
      <td>Kit</td>
      <td>0.020</td>
      <td>0.409</td>
      <td>0.58</td>
      <td>0.222</td>
    </tr>
    <tr>
      <td>12</td>
      <td>Xpo1</td>
      <td>3.31x10–8</td>
      <td>0.472</td>
      <td>0.0069</td>
      <td>0.323</td>
    </tr>
    <tr>
      <td>14</td>
      <td>Xpo1</td>
      <td>0.079</td>
      <td>0.211</td>
      <td>0.19</td>
      <td>0.148</td>
    </tr>
    <tr>
      <td>12</td>
      <td>Ranbp1</td>
      <td>0.24</td>
      <td>0.108</td>
      <td>0.13</td>
      <td>0.079</td>
    </tr>
    <tr>
      <td>14</td>
      <td>Ranbp1</td>
      <td>0.91</td>
      <td>0.069</td>
      <td>0.076</td>
      <td>–0.486</td>
    </tr>
    <tr>
      <td>12</td>
      <td>Ranbp2</td>
      <td>1.98x10–14</td>
      <td>0.754</td>
      <td>0.092</td>
      <td>0.269</td>
    </tr>
    <tr>
      <td>14</td>
      <td>Ranbp2</td>
      <td>0.0056</td>
      <td>0.365</td>
      <td>0.88</td>
      <td>0.042</td>
    </tr>
    <tr>
      <td>12</td>
      <td>Nr3c1</td>
      <td>8.5x10–4</td>
      <td>0.320</td>
      <td>8.8x10–4</td>
      <td>0.430</td>
    </tr>
    <tr>
      <td>14</td>
      <td>Nr3c1</td>
      <td>0.012</td>
      <td>0.153</td>
      <td>8.6x10–5</td>
      <td>0.428</td>
    </tr>
    <tr>
      <td>12</td>
      <td>Ddx46</td>
      <td>3.04x10–8</td>
      <td>0.530</td>
      <td>2.68x10–10</td>
      <td>0.779</td>
    </tr>
    <tr>
      <td>14</td>
      <td>Ddx46</td>
      <td>0.0014</td>
      <td>0.385</td>
      <td>0.0023</td>
      <td>0.490</td>
    </tr>
  </tbody>
</table>

Expression of Xpo1 and Ranbp2, which regulates activity of the Xpo1/Ran complex that stabilizes Gata1 (Ritterhoff et al., 2016), was higher in cluster 12 than in cluster 14, and within cluster 12 the distribution of positive cells was similar to that for other markers of committed erythroid precursors (Figure 4). Xpo1 and RanBP2 mRNAs were expressed in higher percentages of cluster 12 Cd47−/− and Thbs1−/− cells compared to WT (Figure 4—source data 1). The average Xpo1 expression/cell in cluster 12 was significantly higher in Cd47−/− and Thbs1−/− cells compared to WT, whereas expression was not Cd47- or Thbs1-dependent in cluster 14 (Figure 5A and B, Table 2).

Resolution of cluster 12 into CD34+ and CD34− cells revealed that the CD47-dependent expression of Xpo1 and Ranbp2 was restricted to the CD34− population (Figure 4—source data 2). Xpo1 was also Thbs1-dependent in the CD34− cells but could not be evaluated in CD34+ due to lack of an adequate Thbs1−/− cell number. In contrast, expression of mRNA for RanBP1, which regulates the physical interaction of Xpo1 with CD47 (Kaur et al., 2022), did not differ in Cd47−/− or Thbs1−/− cells in clusters 12 (Table 2).

Nr3c1, a marker of adult definitive erythropoiesis (Kingsley et al., 2013), and Ddx46, which is required for hematopoietic stem cell differentiation (Hirabayashi et al., 2013), were among the genes with increased percentages of positive cells and significantly increased average expression in both Cd47−/− and Thbs1−/− cells in cluster 12 (Figure 4—source data 1, Table 2). These genes also showed CD47-dependent expression in cluster 14, but with less significant p-values for expression per cell (Table 2).

The co-expression of mRNAs for erythropoietic genes was compared in cluster 12 cells from Cd47−/−, WT, and Thbs1−/− spleens (Table 3). Small fractions of the WT CD34+ cells expressed Gata1 and Klf1 mRNAs, 2.2% expressed Mki67, and none expressed Ermap. Consistent with the flow cytometry data in Figure 2, coexpression of the respective genes with CD34 was more frequent in Cd47−/− cells in cluster 12, but generally less in Thbs1−/− cells. Notably, CD34+ Thbs1−/− cells showed no Mki67 coexpression. In contrast, WT cells that expressed committed erythroid differential markers were highly proliferative. Coexpression of all these genes with Mik67 was more frequent in Cd47−/− cells compared to WT cells, but only for Kit and Ly6a in Thbs1−/− cells. Coexpression of the erythroid transcription factors Gata1 and Klf1 was similarly increased in Cd47−/− cells but decreased in Thbs1−/− cells compared to the WT cells in cluster 12. The latter is consistent with the extended life span of Thbs1−/− RBC (Wang et al., 2020). Kit coexpression with the erythroid lineage markers Ermap and Klf1 was moderately dependent on genotype, and Ly6a coexpression with these markers was decreased for Cd47−/− cells in cluster 12.

**Table 3.**
 Co-expression of the indicated erythropoiesis related genes in WT, Cd47−/− and Thbs1−/− spleen cells in cluster 12 was quantified and expressed as a percentage of the total cell number of each genotype in cluster 12.


<table>
  <thead>
    <tr>
      <th>Cluster 12 gene coexpression</th>
      <th>WT</th>
      <th>Cd47−/−</th>
      <th>Thbs1−/−</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Cd34_Ermap</td>
      <td>0.0%</td>
      <td>1.8%</td>
      <td>1.6%</td>
    </tr>
    <tr>
      <td>Cd34_Klf1</td>
      <td>6.5%</td>
      <td>8.1%</td>
      <td>3.1%</td>
    </tr>
    <tr>
      <td>Cd34_Gata1</td>
      <td>6.5%</td>
      <td>8.4%</td>
      <td>0.0%</td>
    </tr>
    <tr>
      <td>Mki67_Cd34</td>
      <td>2.2%</td>
      <td>6.3%</td>
      <td>0.0%</td>
    </tr>
    <tr>
      <td>Mki67_Ermap</td>
      <td>55.4%</td>
      <td>63.0%</td>
      <td>54.7%</td>
    </tr>
    <tr>
      <td>Mki67_Kit</td>
      <td>48.9%</td>
      <td>67.2%</td>
      <td>57.8%</td>
    </tr>
    <tr>
      <td>Mki67_Ly6a</td>
      <td>37.0%</td>
      <td>48.2%</td>
      <td>43.8%</td>
    </tr>
    <tr>
      <td>Mki67_Klf1</td>
      <td>62.0%</td>
      <td>74.6%</td>
      <td>57.8%</td>
    </tr>
    <tr>
      <td>Mki67_Epor</td>
      <td>54.4%</td>
      <td>62.7%</td>
      <td>53.1%</td>
    </tr>
    <tr>
      <td>Klf1_Ermap</td>
      <td>67.4%</td>
      <td>68.0%</td>
      <td>62.5%</td>
    </tr>
    <tr>
      <td>Klf1_Gata1</td>
      <td>78.3%</td>
      <td>82.4%</td>
      <td>59.4%</td>
    </tr>
    <tr>
      <td>Ermap_Gata1</td>
      <td>62.0%</td>
      <td>65.1%</td>
      <td>56.2%</td>
    </tr>
    <tr>
      <td>Kit_Ermap</td>
      <td>54.4%</td>
      <td>56.7%</td>
      <td>59.4%</td>
    </tr>
    <tr>
      <td>Kit_Klf1</td>
      <td>71.7%</td>
      <td>77.1%</td>
      <td>78.1%</td>
    </tr>
    <tr>
      <td>Ly6a_Ermap</td>
      <td>42.4%</td>
      <td>37.7%</td>
      <td>46.9%</td>
    </tr>
    <tr>
      <td>Ly6a_Klf1</td>
      <td>64.1%</td>
      <td>59.2%</td>
      <td>67.2%</td>
    </tr>
  </tbody>
</table>

A report that CD47 mediates transfer of mitochondria from macrophages to early erythroblasts during stress-induced erythropoiesis suggested that erythroid precursors in Cd47−/−mice would have lower expression of mitochondrial chromosome-encoded genes (Yang et al., 2022). However, Mt-Atp8, Mt-Nd3, Mt-Nd4l, Mt-Nd5, and Mt-Nd6 were among the most significantly up-regulated genes in Cd47−/− cells in cluster 12 (Table 4). Consistent with CD47 and TSP1 regulation of mitochondrial homeostasis in other cell types (Frazier et al., 2011; Kelm et al., 2020; Miller et al., 2015; Norman-Burgdolf et al., 2020), expression of mt-Atp8, Mt-Nd4l, Mt-Nd5, and Mt-Nd6 was also increased in Thbs1−/− cells in cluster 12. However, expression of other mitochondrial-encoded genes was significantly decreased in Thbs1−/− cells in cluster 12.

**Table 4.**
 Differential expression of mitochondrial encoded genes in cluster 12 cells from WT, Cd47−/−, and Thbs1−/− spleens.


<table>
  <thead>
    <tr>
      <th>Gene</th>
      <th>p-val Cd47−/−vs WT</th>
      <th>Avg log2FC Cd47−/−vs_WT</th>
      <th>p-val Thbs1-/- vs_WT</th>
      <th>Avg log2FC Thbs1-/- vs_WT</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Mt-Atp6</td>
      <td>0.887</td>
      <td>–0.027</td>
      <td>5.43x10–11</td>
      <td>–0.812</td>
    </tr>
    <tr>
      <td>Mt-Atp8</td>
      <td>7.23x10–20</td>
      <td>0.98</td>
      <td>0.0168</td>
      <td>0.377</td>
    </tr>
    <tr>
      <td>Mt-Co1</td>
      <td>0.028</td>
      <td>0.135</td>
      <td>2.60x10–7</td>
      <td>–0.532</td>
    </tr>
    <tr>
      <td>Mt-Co2</td>
      <td>0.226</td>
      <td>0.068</td>
      <td>3.37x10–10</td>
      <td>–0.693</td>
    </tr>
    <tr>
      <td>Mt-Co3</td>
      <td>0.207</td>
      <td>0.097</td>
      <td>1.02x10–8</td>
      <td>–0.671</td>
    </tr>
    <tr>
      <td>Mt-Cytb</td>
      <td>0.338</td>
      <td>–0.006</td>
      <td>9.35x10–10</td>
      <td>–0.790</td>
    </tr>
    <tr>
      <td>Mt-Nd1</td>
      <td>0.074</td>
      <td>0.15</td>
      <td>6.78x10–6</td>
      <td>–0.636</td>
    </tr>
    <tr>
      <td>Mt-Nd2</td>
      <td>0.135</td>
      <td>0.113</td>
      <td>1.00x10–7</td>
      <td>–0.748</td>
    </tr>
    <tr>
      <td>Mt-Nd3</td>
      <td>7.67x10–9</td>
      <td>0.531</td>
      <td>1.36x10–7</td>
      <td>–0.813</td>
    </tr>
    <tr>
      <td>Mt-Nd4</td>
      <td>0.152</td>
      <td>0.093</td>
      <td>5.84x10–6</td>
      <td>–0.558</td>
    </tr>
    <tr>
      <td>Mt-Nd4l</td>
      <td>3.50x10–10</td>
      <td>0.658</td>
      <td>6.49x10–8</td>
      <td>0.787</td>
    </tr>
    <tr>
      <td>Mt-Nd5</td>
      <td>4.63x10–8</td>
      <td>0.612</td>
      <td>0.0154</td>
      <td>0.375</td>
    </tr>
    <tr>
      <td>Mt-Nd6</td>
      <td>1.65x10–7</td>
      <td>0.416</td>
      <td>4.39x10–6</td>
      <td>0.524</td>
    </tr>
  </tbody>
</table>

### Reclustering and analysis of cells expressing erythroid signature genes

Erythrocyte progenitor markers were expressed mainly within cluster 12, but some positive cells were scattered across the T cell clusters 0 through 5 (Figure 6A, Figure 6—figure supplement 1A). To determine whether the latter positive cells include relevant erythroid lineages that were missed in the initial clustering, five lineage markers Gypa, Ermap, Klf1, Gata1, and Aqp1 that predominately localized in cluster 12 (Figure 6—figure supplement 1A) were selected as an erythroid signature to calculate module scores (Figure 6—figure supplement 1A and B). The 1007 cells that express this signature based on module scores (Figure 6A) were then reclustered, yielding five clusters within two major clusters in a UMAP projection (Figure 6B). Immgen annotations predicted that the major clusters represent T cells (548 cells) and stem cells (419 cells, Figure 6C). Mouse RNAseq annotation confirmed the T cell cluster and predicted the stem cell cluster to be of erythrocyte lineage (Figure 6C). WT, Cd47−/− and Thbs1−/− cells were uniformly distributed throughout the erythroid cluster but segregated within the T cell cluster (Figure 6D). Cd47−/− cells were more abundant in the erythroid cluster (271 cells) and Thbs1−/− cells were less abundant (58 cells) relative to WT cells (90 cells).

![Figure 6.](https://cdn.elifesciences.org/articles/92679/elife-92679-fig6-v1.jpg)

**Figure 6.:** (A) tSNE plot showing the distribution of cells selected for expressing threshold levels of Gypa, Ermap, Klf1, Gata1, and/or Aqp1. (B) Re-clustered cells expressing the erythroid progenitor signature are displayed in an UMAP projection. (C) Immgen and mouse RNAseq main cell type annotation of reclustered cells expressing the erythroid gene signature. (D) Distribution of WT (purple), Cd47−/− (green), and Thbs1−/− cells (orange) in the erythroid precursor and T cell clusters. Data are from two female and one male mouse of each genotype.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/92679/elife-92679-fig6-figsupp1-v1.jpg)

**Figure 6—figure supplement 1.:** (A) The left panels show the distribution of cells expressing threshold levels of the 5 gene signature in the original TSNE projection. (B) The RBC progenitor module scoring was performed, as module Scores (a.k.a. Signature Scores) calculated for each cell using expression of five genes (Gypa, Ermap, Klf1, Gata1, and Aqp1). The threshold was set manually (red dashed line on subplots) to separate high-scoring cells from low-scoring cells and expressed by the color on the TSNE plot (top left, high score cells are dark red and low scores cells are represented as light red). RBC Progenitor Module Scoring Plots show the distributions of module scores in lineage-depleted spleen cells from each mouse, with the threshold score indicated by the dotted red lines. (C) The volcano plot presents differentially expressed genes contrasting the reclustered erythropoietic progenitor cell clusters and the T cell cluster.

A volcano plot indicated major differences in the transcriptomes of the two main clusters consistent with their respective erythroid and T cell lineages (Figure 6—figure supplement 1C). The expression of Ermap, Klf1, and Aqp1 mRNAs in 20–30% of cells in the T cell cluster is consistent with previous reports of their expression in minor subsets of T cells (Moon et al., 2004; Su et al., 2021; Teruya et al., 2018; Figure 7).

![Figure 7.](https://cdn.elifesciences.org/articles/92679/elife-92679-fig7-v1.jpg)

**Figure 7.:** Distribution of the multipotent stem cell markers CD34 and Ly6a (Sca1), erythropoietic markers Gata2, Kit, and Epor, the erythroid differentiation transcription factors Klf1 and Gata1, and erythroid differentiation and extramedullary erythropoiesis marker the proliferation marker Mik67, and the erythroid markers Ermap, Tfrc, Aqp1, Tfrc, Tmem56, Trim10, Gypa1, Ebp42, Spta1, Sptb, Xpo1, and Ranbp2 in the erythroid lineage cluster (left) and T cell cluster (right). Expression levels were normalized to maximum expression of each mRNA in these clusters. Data are from two female and one male mouse of each genotype.

The distribution of erythroid markers throughout the reclustered erythroid population was consistent with the results for cluster 12 (Figure 7). CD34+ cells were concentrated in the lower region of the erythroid cell cluster. Consistent with the selection of cells based on expression of committed erythroid lineage genes, the cluster lacked Ly6a+ cells. Kit was expressed by the CD34+ cells and extended upward through the cluster. The upper cells showed increased expression of Epor, Klf1, Gata1, and Aqp1. Expression of the proliferation marker Mki67 was strongest in the upper region of the erythroid cell cluster and extended to cells that cells that expressed markers of more mature precursors including Ermap, Tfrc (transferrin receptor), and Tmem56. Trim10 mediates terminal erythroid differentiation and colocalized with mRNAs encoding glycophorin A, spectrin A, spectrin B, and band 4.2. The upregulation of erythrocyte lineage markers coincided with more abundant Cd47−/− cells in this cluster, which supports the initial unsupervised clustering and confirms increased extramedullary erythropoiesis in Cd47−/− mice.

Differential gene expression analysis contrasting Cd47−/− and Thbs1−/− with WT cells in the erythroid cluster (Table 5) reproduced all of the results found in cluster 12 (Table 2). Mki67, Tfrc, and Ermap mRNAs were significantly higher in Cd47−/− cells compared to WT, whereas Klf1, Aqp1, Epor, and Gata1 mRNAs were significantly lower in Thbs1−/− cells (Table 5). Differences in the percentages of cells expressing these genes seen in cluster 12 were also reproduced in the reclustered erythroid cells (Figure 7—source data 1). The altered expression of Xpo1 and RanBP2 were also confirmed in the erythroid cluster, but Xpo1 mRNA expression was not CD47-dependent in the T cell cluster (Table 5). Notably, the increased expression of Nr3c1, and Ddx46 mRNAs in Cd47−/− and Thbs1−/− cells in the erythroid cell cluster was also found in the reclustered T cells (Table 5). However, the T cell cluster completely lacked expression of the proliferation-associated markers Mki67 and Tfrc (Figure 7—source data 1). Aqp1 and Gata1were also expressed by a subset of the T cells (Figure 7—source data 1), but their decreased mRNA expression in Thbs1−/− cells was not seen in the T cell cluster (Table 5).

**Table 5.**
 Differential mRNA expression of erythropoietic, stem cell, and proliferation associated markers in reclustered WT, Cd47−/−, and Thbs1−/− erythroid and T cell clusters.


<table>
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th colspan="2">Cd47−/− vs WT</th>
      <th colspan="2">Thbs1−/− vs WT</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Cluster</td>
      <td>Gene</td>
      <td>p-value</td>
      <td>Avg log2 FC</td>
      <td>p-value</td>
      <td>Avg log2 FC</td>
    </tr>
    <tr>
      <td>Erythroid</td>
      <td>Klf1</td>
      <td>0.507</td>
      <td>–0.095</td>
      <td>0.0016</td>
      <td>–0.526</td>
    </tr>
    <tr>
      <td>Erythroid</td>
      <td>Aqp1</td>
      <td>0.196</td>
      <td>–0.088</td>
      <td>8.1x10–4</td>
      <td>–0.390</td>
    </tr>
    <tr>
      <td>T cells</td>
      <td>Aqp1</td>
      <td>0.662</td>
      <td>0.027</td>
      <td>0.350</td>
      <td>–0.092</td>
    </tr>
    <tr>
      <td>Erythroid</td>
      <td>Tfrc</td>
      <td>0.015</td>
      <td>0.549</td>
      <td>0.936</td>
      <td>0.054</td>
    </tr>
    <tr>
      <td>T cells</td>
      <td>Tfrc</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Erythroid</td>
      <td>Epor</td>
      <td>0.767</td>
      <td>–0.046</td>
      <td>0.026</td>
      <td>–0.219</td>
    </tr>
    <tr>
      <td>Erythroid</td>
      <td>Ermap</td>
      <td>0.0064</td>
      <td>0.326</td>
      <td>0.496</td>
      <td>–0.010</td>
    </tr>
    <tr>
      <td>T cells</td>
      <td>Ermap</td>
      <td>0.335</td>
      <td>0.076</td>
      <td>0.697</td>
      <td>0.063</td>
    </tr>
    <tr>
      <td>Erythroid</td>
      <td>Gata1</td>
      <td>0.38</td>
      <td>0.009</td>
      <td>0.0040</td>
      <td>–0.337</td>
    </tr>
    <tr>
      <td>T cells</td>
      <td>Gata1</td>
      <td>0.0044</td>
      <td>–.0.162</td>
      <td>0.302</td>
      <td>0.093</td>
    </tr>
    <tr>
      <td>Erythroid</td>
      <td>Mki67</td>
      <td>4.6x10–6</td>
      <td>1.015</td>
      <td>0.118</td>
      <td>0.545</td>
    </tr>
    <tr>
      <td>T cells</td>
      <td>Mki67</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Erythroid</td>
      <td>Kit</td>
      <td>0.0066</td>
      <td>0.293</td>
      <td>0.059</td>
      <td>0.275</td>
    </tr>
    <tr>
      <td>T cells</td>
      <td>Kit</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Erythroid</td>
      <td>Xpo1</td>
      <td>2.65x10–9</td>
      <td>0.514</td>
      <td>0.0025</td>
      <td>0.373</td>
    </tr>
    <tr>
      <td>T cells</td>
      <td>Xpo1</td>
      <td>0.238</td>
      <td>0.047</td>
      <td>0.137</td>
      <td>0.066</td>
    </tr>
    <tr>
      <td>Erythroid</td>
      <td>Ranbp1</td>
      <td>0.099</td>
      <td>0.133</td>
      <td>0.41</td>
      <td>0.078</td>
    </tr>
    <tr>
      <td>T cells</td>
      <td>Ranbp1</td>
      <td>0.278</td>
      <td>–0.124</td>
      <td>0.970</td>
      <td>0.019</td>
    </tr>
    <tr>
      <td>Erythroid</td>
      <td>Ranbp2</td>
      <td>3.2x10–14</td>
      <td>0.755</td>
      <td>0.058</td>
      <td>0.298</td>
    </tr>
    <tr>
      <td>T cells</td>
      <td>Ranbp2</td>
      <td>4.5x10–4</td>
      <td>0.275</td>
      <td>0.210</td>
      <td>0.094</td>
    </tr>
    <tr>
      <td>Erythroid</td>
      <td>Nr3c1</td>
      <td>6.5x10–4</td>
      <td>0.319</td>
      <td>0.0011</td>
      <td>0.447</td>
    </tr>
    <tr>
      <td>T cells</td>
      <td>Nr3c1</td>
      <td>0.0018</td>
      <td>0.274</td>
      <td>0.0018</td>
      <td>0.233</td>
    </tr>
    <tr>
      <td>Erythroid</td>
      <td>Ddx46</td>
      <td>1.65x10–9</td>
      <td>0.530</td>
      <td>2.98x10–9</td>
      <td>0.775</td>
    </tr>
    <tr>
      <td>T cells</td>
      <td>Ddx46</td>
      <td>2.3x10–5</td>
      <td>0.348</td>
      <td>7.5x10–6</td>
      <td>0.446</td>
    </tr>
    <tr>
      <td>Erythroid</td>
      <td>Hba-a1</td>
      <td>0.906</td>
      <td>0.034</td>
      <td>0.0088</td>
      <td>–2.168</td>
    </tr>
  </tbody>
</table>

## Discussion

Our data supports a role for thrombospondin-1-stimulated CD47 signaling to limit early stages of erythropoiesis in WT mouse spleen and opposing roles for thrombospondin-1 and CD47 to regulate SIRPα-dependent turnover of RBC. The increased anemic stress in Cd47−/− spleen increases extramedullary erythropoiesis, whereas extramedullary erythropoiesis is suppressed by the decreased RBC turnover in Thbs1−/− spleen. These studies are consistent with the reported increased red cell turnover in Cd47−/− mice and decreased RBC turnover in Thbs1−/− mice compared to WT mice (Wang et al., 2020). Increased RBC clearance in Cd47−/− mice is mediated by loss of the ‘don’t eat me’ function of CD47 on red cells (Kim et al., 2018; Oldenborg et al., 2000). In wildtype mice, clearance is augmented by thrombospondin-1 binding to the clustered CD47 on aging red cells (Wang et al., 2020). Thus, anemic stress in the mouse strains studied here and the abundance of committed erythroid progenitors in their spleens decrease in the order Cd47−/−>WT > Thbs1−/−.

Independent of CD47 protecting erythropoietic cells from phagocytosis, we previously found that bone marrow from Cd47−/− mice subjected to the stress of ionizing radiation exhibited more colony forming units for erythroid (CFU-E) and burst-forming unit-erythroid (BFU-E) progenitors compared to bone marrow from irradiated wildtype mice (Maxhimer et al., 2009). Loss of CD47 results in an intrinsic protection of hematopoietic stem cells in bone marrow from genotoxic stress, which may be mediated by an increased protective autophagy response (Soto-Pantoja et al., 2012). The same mechanism may contribute to regulating extramedullary erythropoiesis in spleen.

The properties of erythroid precursors that accumulate in Cd47−/− spleens are consistent with previous studies of stress induced extramedullary erythropoiesis associated with malaria or trypanosome infections (Delic et al., 2020; Thompson et al., 2010). In addition to containing elevated NK precursors (Nath et al., 2018), the present data demonstrate that Cd47−/− spleen contains more abundant erythroid precursors that are Ter119+ by flow cytometry but presumably lack sufficient Ter119 for antibody bead depletion. These cells are present but less abundant in WT spleen, indicating that a low basal level of extramedullary erythropoiesis occurs in healthy mouse spleen. The Ter119+CD34− cells that accumulate in Cd47−/− spleens are more proliferative and express multiple markers of committed erythroid precursors. In contrast, the same cells are depleted in Thbs1−/− spleen, consistent with the function of thrombospondin-1 to facilitate the CD47/SIRPα-mediated turnover of aging RBC (Wang et al., 2020). These data also indicate that physiological levels of thrombospondin-1 are necessary to support a basal level of erythropoiesis in WT spleen.

Notably, Thbs1−/− and Cd47−/− spleens contain more early erythroid precursors than are maintained basally in a WT spleen, consistent with the role of thrombospondin-1 signaling via CD47 to limit the expression of multipotent stem cell transcription factors in spleen (Kaur et al., 2013). Earlier erythroid precursors that are Ter119−Kit+ accumulate in Thbs1−/− spleen. Thbs1−/− and Cd47−/− cells express more Ddx46, which is required for differentiation of hematopoietic stem cells (Hirabayashi et al., 2013), and Xpo1, which supports the erythropoietic function of Gata1 (Guillem et al., 2020). Although Ter119+ cells expressing markers of committed erythroid progenitors were depleted in Thbs1−/− compared to WT spleens, mRNAs for some markers of committed erythroid cells including Nr3c1 mRNA were elevated in Thbs1−/− and Cd47−/− cluster 12 cells. However, early progenitors express CD45R, and inclusion of this antibody in the negative selection cocktail should deplete early progenitors from the populations used for both RNAseq analyses. This may account for the relative lack of CD47-dependent CD34+ cells in cluster 12.

One caveat in interpreting the CD47- and thrombospondin-1-dependence of the extramedullary erythropoiesis markers Ermap and Aqp1 in total spleen cells and the Ter119-depleted cells used for scRNAseq is that both are also expressed in minor subsets of T cells (Moon et al., 2004). The reclustering analysis confirmed that these erythropoietic markers are expressed in minor T cell populations, which notably also showed CD47-dependent gene expression changes. This may also account for the differences in CD47-dependence of erythropoietic marker expression observed by flow cytometry in Ter119+ cells but not in total spleen cells or Ter119− spleen cells.

In addition to utility for assessing extramedullary erythropoiesis, the CD47-dependent erythropoiesis genes identified here may have translational utility. Therapeutic CD47 antibodies and decoys designed to inhibit the function of CD47 have entered multiple clinical trials for treating cancers, but anemia associated with loss of CD47-dependent inhibitory SIRPα signaling in macrophages has been a frequent side effect observed for the first generation of these therapeutics (Kaur et al., 2020). These therapeutic antibodies also recognize CD47 on RBC and thereby sensitize them to removal by phagocytes. The resulting anemia would be expected to induce erythropoiesis in bone marrow and possibly at extramedullary sites. Human spleen cells are not accessible to directly evaluate extramedullary erythropoiesis in cancer patients receiving CD47-targeted therapeutics, but analysis of circulating erythroid precursors or liquid biopsy methods could be useful to detect induction of extramedullary erythropoiesis by these therapeutics. Therefore, the CD47-dependent erythroid markers identified in this study may be useful biomarkers for assessing hematologic side effects of CD47-targeted therapeutics.

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
      <td>Commercial assay or kit</td>
      <td>CD8a+T Cell Isolation Kit</td>
      <td>Miltenyi Biotec</td>
      <td>Cat#: 130–104–075</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>CD8a (Ly-2) MicroBeads mouse</td>
      <td>Miltenyi Biotec</td>
      <td>Cat#: 130-117-044</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>EDTA solution</td>
      <td>Sigma-Aldrich</td>
      <td>Cat#: E8008</td>
      <td>2 mM</td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>bovine serum albumin (BSA)</td>
      <td>Sigma-Aldrich</td>
      <td>Cat#: A7906</td>
      <td>0.5%</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>ACK Lysing Buffer, 100 mL</td>
      <td>Quality Biologicals</td>
      <td>Cat#: 118-156-721</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (Mus musculus, C57BL/6)</td>
      <td>WT mice</td>
      <td>Jackson Laboratories</td>
      <td>WT C57BL/6</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (M. musculus, C57BL/6)</td>
      <td>Cd47-/- mice</td>
      <td>Jackson Laboratories</td>
      <td>B6.129S7-Cd47tm1Fpl/J; Strain:003173</td>
      <td>Lindberg et al., 1996;PMID:8864123</td>
    </tr>
    <tr>
      <td>Strain, strain background (M. musculus, C57BL/6)</td>
      <td>Thbs1-/- mice</td>
      <td>Jackson Laboratories</td>
      <td>B6.129S2-Thbs1tm1Hyn/J; Strain:006141</td>
      <td>Lawler et al., 1998;PMID:9486968</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-mouse Ter119-APC (Rat monoclonal)</td>
      <td>Biolegend</td>
      <td>Cat#: 116212;RRID:AB_313713</td>
      <td>IgG2bFACS (1 μg/100 μl/1 million cells)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-mouse CD34-Percp/Cy5.5 (Rat monoclonal)</td>
      <td>Biolegend</td>
      <td>Cat#: 119327;RRID:AB_2728136</td>
      <td>IgG2aFACS (1 μg/100 μl/1 million cells)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti mouse Sca1 PE/Cy7 (Rat monoclonal)</td>
      <td>Biolegend</td>
      <td>Cat#: 108114;RRID:AB_493596</td>
      <td>IgG2aFACS (0.5 μg/100 μl/1 million cells)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-mouse cKit PE (Rat monoclonal)</td>
      <td>Biolegend</td>
      <td>Cat#: 105808;RRID:AB_313217</td>
      <td>IgG2bFACS (0.1 μg/100 μl/1 million cells)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-mouse Ki67- PE/Cy7 (Rat monoclonal)</td>
      <td>Biolegend</td>
      <td>Cat#: 652425;RRID:AB_2632693</td>
      <td>IgG2aFACS (0.5 μg/100 μl/1 million cells)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>IgG2b, κ APC Isotype Control Antibody (Rat monoclonal)</td>
      <td>Biolegend</td>
      <td>Cat#: 400611;RRID:AB_326555</td>
      <td>IgG2bFACS (1 μg/100 μl/1 million cells)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>IgG2a, κ PerCP/Cyanine5.5 Isotype Control Antibody (Rat monoclonal)</td>
      <td>Biolegend</td>
      <td>Cat#: 400531;RRID:AB_2864286</td>
      <td>FACS (1 μg/100 μl/1 million cells)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>IgG2a, κ PE/Cyanine7 Isotype Control Antibody (Rat monoclonal)</td>
      <td>Biolegend</td>
      <td>Cat#: 400521;RRID:AB_326542</td>
      <td>FACS (0.25 μg/100 μl/1 million cells)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>IgG2b, κ PE Isotype Control Antibody (Rat monoclonal)</td>
      <td>Biolegend</td>
      <td>Cat#: 400608;RRID:AB_326552</td>
      <td>FACS (0.1 μg/100 μl/1 million cells)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>IgG2a, κ Alexa Fluor 488 Isotype Control Antibody (Rat monoclonal)</td>
      <td>Biolegend</td>
      <td>Cat#: 400525;RRID:AB_2864283</td>
      <td>FACS (0.25 μg/100 μl/1 million cells)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-Rabbit IgG (H+L) Cross-Adsorbed, Alexa Fluor 594 (Goat polyclonal)</td>
      <td>Thermo Fisher</td>
      <td>Cat#: A-11012</td>
      <td>FACS (0.2 μg/100 μl/1 million cells)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-ERMAP (Rabbit polyclonal)</td>
      <td>Thermo Fisher</td>
      <td>Cat#: BS-12333R</td>
      <td>FACS (1:100 dilution)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-GYPA (Rabbit polyclonal)</td>
      <td>Thermo Fisher</td>
      <td>Cat#: BS-2575R</td>
      <td>FACS (1:100 dilution)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Aquaporin 1 (Rabbit polyclonal)</td>
      <td>Thermo Fisher</td>
      <td>Cat#: PA5-78806</td>
      <td>FACS (1 μg/100 μl/1 million cells)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-EPOR (Rabbit polyclonal)</td>
      <td>Bioss; Thermo Fisher</td>
      <td>Cat#: BS-1424R</td>
      <td>FACS (1 μg/100 μl/1 million cells)</td>
    </tr>
  </tbody>
</table>

### Mice and cells

WT, Cd47−/− (B6.129S7-Cd47tm1Fpl/J, Lindberg et al., 1996), and Thbs1−/− (B6.129S2-Thbs1tm1Hyn/J, Lawler et al., 1998) mice were obtained from The Jackson Laboratory, backcrossed on the C57BL/6 background, and maintained under specific pathogen free conditions. All animal experiments were carried out in strict accordance with the Recommendations for the Care and Use of Laboratory Animals of the National Institutes of Health under a protocol approved by the NCI Animal Care and Use Committee (LP-012). Age and gender matched 8- to 12-week-old mice were used for experiments except where noted. For the bulk RNA sequencing four male Cd47−/− mice and four male wildtype mice were used per CCBR guidance. For single-cell RNA sequencing, two female and one male of each genotype were used per CCBR guidance. For flow cytometry, two female and two males of each genotype were used.

Spleens were removed from the mice and homogenized in HBSS and passed through a 70 µm mesh (Sigma, CLS431751) to remove debris. The cell suspension was treated with ACK lysis buffer for 4 min to lyse the RBC. The suspensions were centrifuged and washed twice with cold HBSS. Aliquots of single-cell suspensions were stained using trypan blue and counted to assess viability.

### Flow cytometry

Spleens were obtained from two male and two female mice of each genotype. Single-cell suspensions from spleens were stained by incubation for 30 min at 4 °C using optimized concentrations of antibodies: CD34-Percp/Cy5.5 and Ter119-APC, cKit-PE and PE/Cy7, Sca1- AF488, Ki67- PE-Cy7 and Percp/Cy5.5 (Biolegend). Non-tagged Ermap, Gypa, Aqp1 (Thermo Fisher) and Epor (Bios Inc) antibodies were detected using secondary goat anti-rabbit AF594 antibodies. Stained single-cell suspensions were acquired on an LSRFortessa SORP (BD Biosciences), and data were analyzed using FlowJo software (Tree Star). A total of 2×105 gated live events were acquired for each analysis. Isotype and unstained controls were used to gate the desired positive populations.

### Single-cell RNA sequencing (scRNAseq)

Because bulk RNA sequencing analysis identified elevated expression of erythropoietic genes in CD8+ spleen cells from Cd47−/− mice that were obtained using magnetic bead depletion of all other lineages, the same method was used as the first step to enrich erythroid precursors. Single cell suspensions from WT, Thbs1−/− and Cd47−/− spleens were depleted of all mature hematopoietic cell lineages including erythroblasts and mature RBC using the CD8a+T Cell Isolation Kit, mouse (Miltenyi Biotec). Single-cell suspensions were incubated with the supplied antibody cocktail of the CD8+ T cell isolation kit for 15 min on ice and then passed through the column as per manufacturer’s instructions. The flow through combined with three washes was centrifuged, and the cells were then incubated with CD8a (Ly-2) microbeads and passed through magnetic columns to obtain lineage-depleted cell populations. Capture & Library Preparation for single cell end-counting gene expression using the 10 X Genomics platform was performed by the Single Cell Analysis Facility (CCR).

Single-cell RNA-sequencing (scRNA-seq) data were generated using the Chromium Single Cell 3’ Solution (10 x Genomics). Raw sequencing data were processed using the CellRanger software suite (version 4.0.0, 10 x Genomics). CellRanger’s mkfastq and count functions were utilized to demultiplex raw base call (BCL) files into sample-specific FASTQ files, perform barcode processing, and align cDNA reads to the reference genome (mm10) to generate feature-barcode matrices.

Downstream analysis and visualization were performed within the NIH Integrated Analysis Platform (NIDAP) using R programs developed by a team of NCI bioinformaticians on the Foundry platform (Palantir Technologies). The Single Cell workflow on NIDAP executes the SCWorkflow package (https://github.com/NIDAP-Community/SCWorkflow; copy archived at NIDAP-Community, 2024), which is based on the Seurat workflow (v. 4.1.1; Hao et al., 2021). Quality control metrics were assessed to remove low-quality cells, defined as cells with fewer than 200 detected genes or a high percentage (>15%) of mitochondrial gene expression, indicative of cellular stress or apoptosis. After filtering, the dataset consisted of 13,933 single cells with an average of 7523 unique molecular identifiers (UMIs) per cell and an average gene detection of 2114 genes per cell. The dataset underwent normalization via log-transformation, and RunPCA applied to the scaled data of the variable features to compute the principal components. After performing SCTransform (Hafemeister and Satija, 2019) on the merged dataset, an unsupervised clustering methodology was employed to categorize cells exhibiting analogous expression patterns. The FindClusters function was used with a clustering resolution of 0.4 for all cells and a reclustered resolution of 0.2 for the RBC progenitor cell subset. Each cellular cluster was annotated with the expression of established cell-type-specific marker genes and dimensionality reduction plots (t-distributed stochastic neighbor embedding [t-SNE] and uniform manifold approximation and projection [UMAP]), were utilized for the visual representation of clusters. Cell types were called using SingleR (v.1.0) (Aran et al., 2019) and Immgen and Mouse RNAseq databases.

Differential expression analysis among the identified cell clusters was conducted utilizing the FindMarkers function, which implements a Wilcoxon Rank Sum test. Genes were deemed differentially expressed with an adjusted p-value <0.05 following correction for multiple testing via the Benjamini-Hochberg procedure.

### Bulk RNAseq

Naïve CD8-enriched lineage-depleted spleen cells from four male 4–6 week-old Cd47−/− and four male WT mice were prepared using CD8a+T Cell Isolation Kit, subjected to RNAseq analysis (Nath et al., 2022). Downstream analysis and visualization were performed within the NIH Integrated Analysis Platform (NIDAP) using R programs developed by a team of NCI bioinformaticians on the Foundry platform (Palantir Technologies). Briefly, RNA-seq FASTQ files were aligned to the reference genome (mm10) using STAR (Dobin et al., 2013) and raw counts data produced using RSEM (Li and Dewey, 2011). The gene counts matrix was imported into the NIDAP platform, where genes were filtered for low counts (<1 cpm) and normalized by quantile normalization using the limma package (Ritchie et al., 2015). Differentially expressed genes were calculated using limma-Voom (Law et al., 2016) and GSEA was performed using the fgsea package (Korotkevich et al., 2019). Preranked gene set enrichment analysis of the Hallmark collection was performed using the t-statistic as ranking variable. (Figure 1—figure supplement 1).
