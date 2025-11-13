# Developmental hourglass and heterochronic shifts in fin and limb development

## Authors

- Koh Onimaru<sup>1</sup> ([ORCID: 0000-0002-2428-9510](https://orcid.org/0000-0002-2428-9510)) †
- Kaori Tatsumi<sup>1</sup>
- Chiharu Tanegashima<sup>1</sup>
- Mitsutaka Kadota<sup>1</sup>
- Osamu Nishimura<sup>1</sup> ([ORCID: 0000-0003-1969-2580](https://orcid.org/0000-0003-1969-2580))
- Shigehiro Kuraku<sup>1</sup> ([ORCID: 0000-0003-1464-8388](https://orcid.org/0000-0003-1464-8388)) †

### Affiliations

1. Laboratory for Phyloinformatics, RIKEN Center for Biosystems Dynamics Research (BDR) Kobe Japan
2. Laboratory for Bioinformatics Research, RIKEN BDR Wako City Japan
3. Molecular Oncology Laboratory, Graduate School of Medicine, Nagoya University Nagoya Japan

† Corresponding author

## Abstract

How genetic changes are linked to morphological novelties and developmental constraints remains elusive. Here, we investigate genetic apparatuses that distinguish fish fins from tetrapod limbs by analyzing transcriptomes and open-chromatin regions (OCRs). Specifically, we compared mouse forelimb buds with the pectoral fin buds of an elasmobranch, the brown-banded bamboo shark (Chiloscyllium punctatum). A transcriptomic comparison with an accurate orthology map revealed both a mass heterochrony and hourglass-shaped conservation of gene expression between fins and limbs. Furthermore, open-chromatin analysis suggested that access to conserved regulatory sequences is transiently increased during mid-stage limb development. During this stage, stage-specific and tissue-specific OCRs were also enriched. Together, early and late stages of fin/limb development are more permissive to mutations than middle stages, which may have contributed to major morphological changes during the fin-to-limb evolution. We hypothesize that the middle stages are constrained by regulatory complexity that results from dynamic and tissue-specific transcriptional controls.

## Introduction

The genetic mechanism of morphological diversity among multicellular organisms is of central interest in evolutionary biology. In particular, our understanding of how morphological novelties are linked to the emergence of their respective genetic apparatuses is limited (Rebeiz and Tsiantis, 2017). In addition, it is still unclear to what extent internal constraints, such as pleiotropy, affect evolvability (Wagner and Zhang, 2011). The fin-to-limb transition is a classic, yet still influential, case study that contributes to our understanding of morphological evolution. In general, tetrapod limbs are composed of three modules, the stylopod, zeugopod, and autopod, which are ordered proximally to distally (Figure 1A). In contrast, fish fins are often subdivided into different anatomical modules along the anterior−posterior axis—the propterygium, mesopterygium, and metapterygium (Figure 1A). Although it is still controversial how this different skeletal arrangement compares with the archetypal tetrapod limb, the autopod (wrist and digits) seems to be the most apparent morphological novelty during the fin-to-limb transition (Clack, 2009). Despite intensive comparative studies of developmental gene regulation, genetic machinery that differs between fins and limbs remains elusive. Instead, several studies revealed that autopod-specific regulation of Hoxa13 and Hoxd10−13, which control autopod formation, is also conserved in non-tetrapod vertebrates (Davis et al., 2007; Freitas et al., 2007; Schneider et al., 2011), except that the expression domains of Hoxa13 and Hoxa11 are mutually exclusive in mouse and chick limbs while overlapping in examined fish fin buds (note that axolotl limbs also exhibit such fish-like overlap of these expression domains; Ahn and Ho, 2008; Metscher et al., 2005; Sakamoto et al., 2009; Woltering et al., 2019). Although several gene regulatory differences have been proposed to explain the anatomical difference between fins and limbs, these proposals have been exclusively focused on Hox genes (Kherdjemil et al., 2016; Nakamura et al., 2016; Sheth et al., 2012; Woltering et al., 2014). Therefore, a genome-wide systematic study is required to identify the genetic differences between fish fins and tetrapod limbs.

![Figure 1.](https://cdn.elifesciences.org/articles/62865/elife-62865-fig1-v2.jpg)

**Figure 1.:** (A) The skeletal patterns of a mouse limb (top) and a bamboo shark pectoral fin (bottom). Anterior is to the top; distal is to the right. (B) Mouse forelimb buds and bamboo shark pectoral fin buds that were analyzed by RNA-seq. (C) Comparison of the accuracy of three orthology assignment methods. Vertical axis, the percentages of correctly assigned Hoxa and Hoxd paralogs (black bars) and Fgf paralogs (white bars). (D) Heat map visualization of the transcription profile of Hoxa and Hoxd genes in mouse limb buds (left) and bamboo shark fin buds (right) with scaled TPMs.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/62865/elife-62865-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** Red arrows, the main flow of the algorithm. Black arrows, orthology assignment for cartilaginous fish-specific genes. Gray arrows, parallel retrieving of orthologs of mouse genes from other animals. Red rectangles, best hits across other animal genes or in elephantfish genes. Green rectangles, best hits among each animal genome. Note that this schematic explains how the orthology of abstract genes ‘bamboo shark gene X’ and ‘mouse gene Y’ are assigned. First, using BLASTP, putative orthologs of bamboo shark genes are retrieved from other animal genomes, such as human, mouse, alligator, and elephantfish. Then, all BLASTP results except those from elephantfish are concatenated to find a best scored gene across species (cross-species best hit). In this schematic, the alligator gene XP001 is the best hit. In parallel, putative orthologs of mouse genes are also retrieved from the same set of animal genomes. If there is a mouse gene Y that has a best hit with alligator XP001, this mouse gene Y and bamboo shark gene X are considered to be an orthologous pair.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/62865/elife-62865-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** The tree was inferred with the maximum-likelihood method. The support values at nodes indicate bootstrap probabilities. Genes highlighted in red are bamboo shark genes (can be converted into the original gene ID by replacing ‘g’ with ‘Chipu’ and fill the digit with 0 to be seven figure number in total).

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/62865/elife-62865-fig1-figsupp3-v2.jpg)

**Figure 1—figure supplement 3.:** These trees are shown because alignment sequences used in Figure 1—figure supplement 2 are truncated or absent in these genes. The tree was inferred with the maximum-likelihood method. The support values at nodes indicate bootstrap probabilities. Genes highlighted in red are bamboo shark genes.

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/62865/elife-62865-fig1-figsupp4-v2.jpg)

**Figure 1—figure supplement 4.:** (A) Visualization of the effect of normalization by showing a housekeeping gene family, Ndufa. Left panels show TMM (trimmed mean of M) and TPM (transcripts per million) calculated by RSEM. Right panels show these values with additional normalization using several other housekeeping genes (Atp5j, Atp5h, Atp5g3, Psmc3, Psmc5, Psmd7, Mrpl54, Mrpl46, Polr2e, Polr1b, Mrpl2). Housekeeping genes are selected from a previously published list (https://www.tau.ac.il/~elieis/HKG/HK_genes.txt; Eisenberg and Levanon, 2013). All expression values are standardized by setting the maximum expression value of each gene as ‘1’. Note that because housekeeping genes do not change their expression amount over time, these expression values should be close to ‘1’ (i.e. all colors should be dark blue) with some exceptions. However, the intact TMM (top, left panel) is apparently biased, in that the majority of Ndufa genes show their strongest expression at E9.5, with sharp decreases at other stages. This bias can be corrected by normalization with other housekeeping genes (top right panel). In contrast, the intact TPM (bottom, left panel) has a weaker bias than TMM. Additional normalization (bottom, right panel) has less of an effect. Therefore, this study used the intact TPM. (B) Euclidean distances of transcriptome data between mouse samples (left) and between bamboo shark samples (right). Whereas the close relation of the replicates of mouse samples can be seen from this heat map, the replicates of bamboo shark samples show less similarity. This noisy data may be attributed to the fact that there is no established strain of the bamboo shark and/or that bamboo shark embryos were staged by morphology but not physical time. However, the average of replicates seems to mitigate the noise of the bamboo shark samples, because Hox gene expression showed a smooth temporal collinearity as seen in Figure 1D.

![Figure 1—figure supplement 5.](https://cdn.elifesciences.org/articles/62865/elife-62865-fig1-figsupp5-v2.jpg)

**Figure 1—figure supplement 5.:** (A) A simple example for comparing expression distances between two species. Species 1 and 2 are imaginery simple species that have two genes (genes 1 and 2) and three developmental time points (t1, t2, and t3). Distances in the bottom are the Euclidean distance between two species at each stage. (B, C) Housekeeping gene expressions with intact TPM values and different scaling methods in mouse limb buds (B) and bambooshark fin buds (C). Intact TPM, TPM values without any scaling methods; Max 1, TPM values were scaled by setting the highest TPM in each gene of each species to ‘1’; Z-score, the mean expression value was subtracted from each expression value and each result was then divided by the standard deviation; Unit vector, expression values were divided by the norm; Log10, log10 transformation. These housekeeping genes are listed in both a human housekeeping gene list (https://www.tau.ac.il/~elieis/HKG/HK_genes.txt) and the BUSCO data set (thus these genes are likely conserved in most vertebrates). Note that although the expression values of the housekeeping genes were almost constant during development, Z-score scaling amplifies subtle differences between stages. In addition, intact TPM values were not readily comparable between limb buds and bamboo shark fin buds (e.g. the maximum value of POLR1B in mouse limb buds was roughly twice as high as that of bamboo shark fin buds). Error bars are not displayed.

![Figure 1—figure supplement 6.](https://cdn.elifesciences.org/articles/62865/elife-62865-fig1-figsupp6-v2.jpg)

**Figure 1—figure supplement 6.:** (A, B) Heterochronic gene expressions with intact TPM values and different scaling methods in mouse limb buds (A) and bambooshark fin buds (B). See the legend of Figure 1—figure supplement 5 for scaling methods. Error bars are omitted. (C) The total Euclidean distance with respect to gene expression for the three housekeeping and the three heterochronic genes between mouse limb buds and bamboo shark fin buds. Using the housekeeping genes shown in (A, B) and the different scaling methods, the graph shows the summation of Euclidean distances between all combinations of mouse limb and bamboo shark fin stages. (D) The ratios of the Euclidean distances for housekeeping genes to those for heterochronic genes as shown in C.

![Figure 1—figure supplement 7.](https://cdn.elifesciences.org/articles/62865/elife-62865-fig1-figsupp7-v2.jpg)

**Figure 1—figure supplement 7.:** TPM values of 5ʹ Hoxd genes in mouse limb buds at E12.5 (left) and bamboo shark fin buds at st. 31 (right, orange bars) and st. 32 (right, blue bars). Error bars, SEM. Note that the genomic locus of Hoxd genes was positively correlated with their expression amount in the mouse limb bud, whereas no such correlation was found in the bamboo shark fin bud.

![Figure 1—figure supplement 8.](https://cdn.elifesciences.org/articles/62865/elife-62865-fig1-figsupp8-v2.jpg)

**Figure 1—figure supplement 8.:** (A, B) Scaled TPM values of indicated genes related to chondrogenesis (A) and myogenesis (B). Error bars, SEM.

There have been several difficulties that limit genetic comparisons between tetrapods and non-tetrapod vertebrates. For example, whereas zebrafish and medaka are ideal models for molecular studies, their rapid evolutionary speed and a teleost-specific whole-genome duplication hinder comparative analyses with tetrapods at both the morphological and genetic levels (Ravi and Venkatesh, 2008). This obstacle can be circumvented by using more slowly evolving species such as spotted gar, coelacanths, and elephantfish (also known as elephant shark, a cartilaginous fish that is not a true shark) with their genome sequences that have not experienced recent lineage-specific genome duplications and thus facilitate the tracing of the evolution of gene regulation (Amemiya et al., 2013; Braasch et al., 2016). However, the major disadvantage of these slowly evolving species is the inaccessibility of developing embryos. In contrast, although the eggs of sharks and rays (other slowly evolving species; Hara et al., 2018) are often more accessible, their genomic sequence information has not been available until recently. As a solution for these problems, this study used embryos of the brownbanded bamboo shark (referred to hereafter as the bamboo shark), because a usable genome assembly was recently published for this species (Hara et al., 2018). Importantly, its non-coding sequences seem to be more comparable with those of tetrapods than with teleosts (Hara et al., 2018). In addition, this species is common in aquariums and has a detailed developmental staging table, providing an opportunity to study embryogenesis (Onimaru et al., 2018). These unique circumstances of the bamboo shark enabled a comprehensive study to identify the genetic differences between fins and limbs.

In this study, to identify genetic differences between fins and limbs, we performed RNA sequencing (RNA-seq) analyses of developing bamboo shark fins and mouse limbs. Along with this transcriptomic comparison, we also generated an accurate orthology map between the bamboo shark and mouse. In addition, we applied an assay for transposase‐accessible chromatin with high‐throughput and chromatin accessibility analysis (ATAC-seq; Buenrostro et al., 2013) across a time series of mouse limb buds, which generated a high-quality data set the showing dynamics of open-chromatin regions (OCRs; putative enhancers) during limb development. We also analyzed the evolutionary conservation of sequences in these OCRs to gain insights into the gene regulatory changes during the fin-to-limb transition.

## Results

### Comparative transcriptome analysis

To compare the temporal dynamics of gene expression between bamboo shark fin and mouse limb development, we obtained RNA-seq data from a time series of growing fin and limb buds with three replicates (Figure 1B; Supplementary file 1 for the details of RNA-seq). We selected limb buds from embryonic day (E)9.5 to E12.5 mice because this is the period during which the major segments of the tetrapod limb—the stylopod, zeugopod, and autopod—become apparent. In particular, the presumptive autopod domain, which is a distinct structure in the tetrapod limb, is visually recognizable from E11.5. For the bamboo shark, we selected developing fin stages from as wide a time period as possible (Figure 1B). To perform fine-scale molecular-level comparison, we annotated its coding genes using BLASTP against several vertebrates (listed in the Materials and methods) and our custom algorithm. As a result, 16443 unique genes from 63898 redundant coding transcripts were annotated as orthologous to known genes of vertebrates, among which 13,005 genes were uniquely orthologous to mouse genes (Table 1 for details of the transcriptome assembly; Figure 1—figure supplement 1—3, Supplementary files 2 and 3 for gene annotations and Supplementary data for sequence information). The number of detected orthologs is reasonable when compared with other studies (e.g. Hao et al., 2020). The quality of the ortholog assignment, which was assessed by examining Hox and Fgf genes, showed that our custom algorithm is more accurate than other methods (Figure 1C; see Materials and Methods and Supplementary file 4 for details). Using this assembly for the bamboo shark and RefSeq genes for mice, the means and standard errors of the transcripts per million (TPM) values were calculated from three replicates (see Figure 1—figure supplement 4 for other normalization methods and Supplementary files 5 and 6 for the full list of TPM values). In addition, for most of the analyses, TPMs were scaled by setting the highest TPM in each gene of each species to ‘1’ (which we refer to as the Max one method) to capture temporal dynamics rather than absolute transcript amounts. Compared to using intact TPMs and other scaling methods, Max one is relatively sensitive to interspecific differences in dynamically regulated gene expression (see Materials and methods and Figure 1—figure supplements 5 and 6 for details).

**Table 1.**
 Assembly statistics of bamboo shark transcriptome.


<table>
  <thead>
    <tr>
      <th>Characteristic</th>
      <th>Bamboo shark transcriptome</th>
      <th>Bamboo shark gene model (Hara et al., 2018)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Total number of sequences</td>
      <td>222015</td>
      <td>34038</td>
    </tr>
    <tr>
      <td>Total sequence length (bp)</td>
      <td>195541367</td>
      <td>36633751</td>
    </tr>
    <tr>
      <td>Average length (bp)</td>
      <td>880</td>
      <td>1076</td>
    </tr>
    <tr>
      <td>Maximum length (bp)</td>
      <td>18451</td>
      <td>108594</td>
    </tr>
    <tr>
      <td>N count</td>
      <td>0</td>
      <td>10208</td>
    </tr>
    <tr>
      <td>L50</td>
      <td>24765</td>
      <td>5666</td>
    </tr>
    <tr>
      <td>N50 length (bp)</td>
      <td>2075</td>
      <td>1749</td>
    </tr>
    <tr>
      <td>Protein coding</td>
      <td>63898</td>
      <td>34038</td>
    </tr>
    <tr>
      <td>Orthology detected</td>
      <td>41633</td>
      <td>18180</td>
    </tr>
    <tr>
      <td>Unique orthologs</td>
      <td>14139</td>
      <td>14907</td>
    </tr>
    <tr>
      <td>Unique orthologs without gene symbols</td>
      <td>1821</td>
      <td>1780</td>
    </tr>
    <tr>
      <td>Unique orthologs only in elephantfish</td>
      <td>826</td>
      <td>552</td>
    </tr>
    <tr>
      <td>Sequences with no orthology</td>
      <td>20892</td>
      <td>15254</td>
    </tr>
    <tr>
      <td>Orthologs with mouse genes</td>
      <td>12326</td>
      <td>13005</td>
    </tr>
  </tbody>
</table>

With this transcriptome data set and gene annotation, we first validated our data by analyzing the expression profiles of Hoxa and Hoxd genes. In mouse limb development, Hoxa and Hoxd genes undergo two phases of global regulation (Deschamps and Duboule, 2017). During the first phase, Hoxd genes are regulated by an enhancer group located 3ʹ of the entire HoxD cluster, and the Hoxd genes are sequentially upregulated from 3ʹ to 5ʹ. The outcome of this first phase helps to establish the arm and the forearm. During the second phase, enhancers located 5ʹ of the HoxD cluster start to activate expression of Hoxd10 to Hoxd13 in the presumptive autopod region (Hoxa genes are regulated in a similar manner; Deschamps and Duboule, 2017). As expected, we detected the two phases of Hoxd gene regulation in mouse limb transcriptomes; the expression levels of Hoxd1 to Hoxd8 were highest at E9.5 (the first phase regulation), and Hoxd11 to Hoxd13 were gradually upregulated later (the second phase regulation; Figure 1D). Interestingly, the expression levels of Hoxd9 and Hoxd10 were highest at E10.5, which probably represents the transitional state between the first and second global regulation (Andrey et al., 2013). A similar profile was observed for Hoxa genes (Figure 1D). As with mouse limb buds, we found similar phasic regulation of Hoxa and Hoxd genes in the bamboo shark fin transcriptome (Figure 1D), suggesting that these transcriptomic data cover comparable developmental stages between the two species at least with respect to Hox gene regulation.

The overall similarity in the temporal dynamics of Hox gene expression between the mouse limb bud and the bamboo shark fin bud is an expected result because the second phase of Hoxd gene regulation has been found to be conserved in the fins of many fish (Ahn and Ho, 2008; Davis et al., 2007; Freitas et al., 2007; Schneider et al., 2011; Tulenko et al., 2017). However, there are several differences that are worth noting. For example, in mouse limb buds, Hoxd11 and Hoxd12 expression was highest at E11.5, followed by further upregulation of Hoxd13 at E12.5 (Figure 1D). In contrast, in bamboo shark fin buds, these three genes reached their peak expression simultaneously at [stage (st)]31 (Figure 1D). This led us to investigate further whether the quantitative collinearity of 5ʹ Hoxd genes, where the expression of Hoxd13 is much higher than that of its neighboring Hoxd genes, whose transcription levels decrease with increasing distance from Hoxd13 (Montavon et al., 2008), is conserved in the bamboo shark fin buds. First, as a confirmation of the previous observation, we also found quantitative collinearity of Hoxd genes in our transcriptome data of mouse limb buds at E12.5 (Figure 1—figure supplement 7). However, the bamboo shark fin buds exhibited no clear relationship between the genomic loci and the expression levels of Hoxd genes at either st31 or st32 (Figure 1—figure supplement 7): Hoxd12 expression was highest among its neighbors. Hoxd9 showed the second highest expression, followed by Hoxd10 and Hoxd11, which had roughly identical levels of transcripts. Hoxd13 expression was lowest among these 5ʹ members. Given that quantitative collinearity is considered to be a consequence of the characteristic global regulation of the HoxD cluster in the mouse limb bud (Montavon et al., 2008), this result suggests that the bamboo shark fin bud may have a different mechanism for Hoxd gene regulation. Interestingly, a recent study also showed that the presumptive autopod domains of chick limb buds express nearly a same amount of Hoxd13 and Hoxd12 transcripts (Yakushiji-Kaminatsui et al., 2018), suggesting that quantitative collinearity is not a universal feature of fins and limbs, rather varies among species. Taken together, although the overall temporal dynamics of Hox gene expression are conserved between the mouse limb bud and the bamboo shark fin bud, some differences in the regulation of Hox genes may exist between species.

To investigate to what extent our bulk transcriptome data captured the processes of cellular differentiation, we also analyzed genes related to chrondrogenesis and myogenesis. As a result, we found that the chondrogenic pathway was at least partially conserved between bambooshark fin buds and mouse limb buds; the expression level of Sox9 and Runx3 (key transcription factors of chondrogenesis; Fowler and Larsson, 2020) increased relatively early, and that of Acan (a cartilage-specific proteoglycan; Fowler and Larsson, 2020) was upregulated later (Figure 1—figure supplement 8). In contrast, although Nog is known to be expressed in cartilaginous condensations in mouse limb buds (Brunet et al., 1998), we did not detect a Nog ortholog in either the fin transcriptome or the genome assembly of the bamboo shark. As for myogenesis, our transcriptome data captured both conserved and divergent myogenetic regulation: Pax3 (a marker of myogenic precursor cells) was downregulated over developmental time, and the MyoD gene family (Myog, Myod1, Myf5) took turns for further differentiation (Chal and Pourquié, 2017). In contrast, whereas mouse limb buds showed upregulation of three myosin genes (Myh3, Myh7, Myh8) at E12.5, we detected the upregulation of only Myh7 in bamboo shark fin buds. Again, we did not find Myh3 and Myh8 in either the transcriptome or the genome assembly of the bamboo shark. These results suggest that our transcriptome data, even though based on bulk sampling of RNA, can reveal conserved and diverged cellular differentiation processes.

### Heterochronic gene expressions

Next, to find differences in gene regulation between the two species, we performed a gene-by-gene comparison of expression dynamics with hierarchical clustering (Figure 2A). To find potential candidate genes that contribute to the different morphologies between fins and limbs, we annotated genes with mouse mutant phenotypes (see Supplementary file 7 for the full list of genes, expression data, and annotation). The result showed that 6701 genes were significantly expressed in only one of these species (‘Fin-specific’ and ‘Limb-specific’ in Figure 2A; 3284 and 3417 genes, respectively). While the fin-specific gene group consisted of many uncharacterized genes, it included ones that are known to control only fish fin development (Fischer et al., 2003; Zhang et al., 2010), such as And1 (TRINITY_DN62789_c1_g1_i3 in Supplementary data; ortholog of a coelacanth gene, XP_015216565) and Fgf24 (TRINITY_DN92536_c7_g1_i2 in Supplementary data; ortholog of a coelacanth gene, XP_006012032). In the limb-specific gene group, several interesting genes were listed that exhibit abnormal phenotype in the mouse limb (e.g. Bmp2, Ihh, and Megf8). However, the number of these species-specific genes is probably unreliable and overestimated because these groups also contain genes for which their orthology was not assigned correctly. We also detected 1884 genes that were upregulated during late stages of fin/limb development for both species, including genes that are well known to be expressed later during fin/limb development, such as the autopod-related transcription factors Hoxd13 and Hoxa13 and differentiation markers Col2a1 and Mef2c (‘Conserved, late1 and Conserved, late2’ in Figure 2A). Intriguingly, 5388 genes exhibited heterochronic expression profiles; their expression levels were highest during the late stages of mouse limb bud development but were relatively stable expression throughout fin development (‘Heterochronic1’; 3178 genes) or decreased during the late stages of fin development (‘Heterochronic2’; 2223 genes; see Supplementary file 7 for the full list of genes and annotations). For validation, we examined the spatio-temporal expression pattern of three heterochronic genes that exhibit limb abnormality in mouse mutants, Aldh1a2 from Heterochronic1 and, Hand2 and Vcan from Heterochronic2. Aldh1a2 is upregulated in the interdigital web of mouse limb buds from E11.5 (Figure 2—figure supplement 1A) and known to positively regulate interdigital cell death (Kuss et al., 2009). On the other hand, in bamboo shark fin buds, Aldh1a2 expression was initially uniform and was later restricted to the distal edge of fin buds (Figure 2—figure supplement 1A). Hand2 and Vcan transcripts were upregulated in mouse forelimb buds at E12.5 and downregulated in bamboo shark fin buds at st32 (Figure 2B,C). Thus, the temporal transcriptomic profiles were consistent with spatial expression patterns.

![Figure 2.](https://cdn.elifesciences.org/articles/62865/elife-62865-fig2-v2.jpg)

**Figure 2.:** (A) Clustering analysis of gene expression dynamics. Each column represents an ortholog pair between the bamboo shark and the mouse. Each row indicates scaled gene expression at a time point indicated to the right of the heat map. Values are scaled TPMs. (B, C) Whole-mount in situ hybridization of Hand2 (B) and Vcan (C) as examples of the heterochronic genes detected in (A). Asterisks, background signals; scale bars, 200 μm. Error bars: SEM.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/62865/elife-62865-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) Left panels, whole mount in situ hybridization of Aldh1a2 (one of the genes from the cluster Heterochronic1) in bamboo shark fin buds and mouse limb buds. Right panels, TPM values of Aldh1a2. Arrowheads indicate the late-stage expression of Aldh1a2 in bamboo shark fin buds. Scale bars, 200 μm. Error bars, SEM. (B) Heatmap of genes that exhibit an inverse relation to Heterochronic2 genes in Figure 2A. Yellow empty box, genes that exhibit relatively sharp upregulation in bamboo shark fin buds and downregulation in mouse limb buds over time. (C) Comparison of Fgf gene expression. Vertical axis, TPM values; error bars, SEM; N/A, not applicable because of the absence of Fgf24 in the mouse genome.

For a comparison, we found relatively few genes that were downregulated over time in the mouse limb bud but were upregulated in the shark fin. There was a total of 241 such genes, but only 43 of them displayed a clear heterochrony (yellow empty box in Figure 2—figure supplement 1B and Supplementary file 8 for the list of the genes). Of those, Fgf8 is particularly interesting as FGF8 plays a crucial role as a growth signal from the apical ectodermal ridge (AER) in mouse and chick limb buds (Lewandoski et al., 2000). As shown in Figure 2—figure supplement 1C, Fgf8 expression was high during the early stages of limb buds and was gradually downregulated at later stages. In contrast, in bamboo shark fin buds, Fgf8 was expressed very weakly (around 0.1 TPM) at st. 27 and st. 27.5 and was upregulated at later stages. Indeed, this late upregulation of Fgf8 was also reported in the apical fin fold (roughly equivalent to the AER) of zebrafish pectoral fin buds (Nomura et al., 2006). In the zebrafish pectoral fin bud, Fgf16 and Fgf24 are upregulated earlier than Fgf8 (Draper et al., 2003; Nomura et al., 2006). In addition, Fgf4, Fgf9, and Fgf17 are expressed in the AER and have a redundant function in the mouse limb bud (Mariani et al., 2008). Therefore, we also examined these other Fgf genes and found that moderate expression of Fgf9, Fgf16, and Fgf24 were detected in the early stages of bamboo shark fin buds (Figure 2—figure supplement 1C). Although we cannot infer the ancestral state of the expression pattern, the overlapping functions of these genes may have allowed subfunctionalization of the signaling molecules of the AER during vertebrate divergence. In sum, we detected mass heterochronic shifts in gene expression between bamboo shark fin buds and mouse forelimb buds. In particular, a mechanism to maintain upregulation of the expression of genes involved in early fin development may have been either gained in the tetrapod lineages or lost in the cartilaginous fish lineages.

### Comparison of SHH signaling pathways in limb and fin buds

In tetrapod limbs, SHH controls growth and asymmetric gene expression along the anterior-posterior axis. Although previous studies have repeatedly implied a relatively delayed onset of Shh expression or a short signal duration in developing fins of several elasmobranch species (Dahn et al., 2007; Sakamoto et al., 2009; Yonei-Tamura et al., 2008), there has not been solid evidence to support such a delay due to the lack of systematic gene expression analysis and the poor staging system of these species. Because the heterochronic genes identified above include basic SHH target genes, such as Ptch1 and Gli1, we reexamined the expression dynamics of Shh and its target genes in mouse limb and bamboo shark fin buds. Because HOX genes are the upstream factors relative to Shh transcription (Zeller et al., 2009), we used them as a potential reference for developmental time. We first found that Shh transcription was present by the earliest stages examined in both bamboo shark fin and mouse limb buds, and it peaked when the transcription level of Hoxd9 and Hoxd10 was highest, suggesting that there was no apparent heterochrony in Shh transcription timing at least between these two species (red rectangles in Figure 3A and B). In contrast, SHH target genes, such as Ptch1/2, Gli1, Gremlin, and Hand2 (Vokes et al., 2008), did show a relatively extended period of expression in mouse limb buds as compared with their expression in bamboo shark fin buds. Namely, whereas the expression peak of SHH target genes was concurrent with that of Shh in the bamboo shark fin bud, these SHH target genes were highly expressed in E11.5 limb buds, which is one day later than the Shh expression peak (yellow rectangles in Figure 3A and B; see Figure 3—figure supplement 1 for intact TPM values). This timing difference is also apparent when comparing the expression peak of Hoxd11 and Hoxd12, which was concurrent with that of SHH target genes in mouse limb buds, but came after downregulation of SHH target genes in bamboo shark fin buds (green rectangles in Figure 3A and B). To confirm this observation, we performed whole-mount in situ hybridization for Ptch1 and Hoxd12 in mouse limb buds and bamboo shark fin buds. As previously reported (Lewis et al., 2001; Zákány et al., 2004), mouse limb buds showed a clear expansion of the expression domain of Ptch1 (upper panel in Figure 3C) from E10.5 to E11.5, which is accompanied by the anterior extension of the Hoxd12 expression domain (black arrowheads in Figure 3C). In contrast, Ptch1 was expressed in the posterior domain of bamboo shark fin buds at st. 29 (white arrowheads in Figure 3D), but was substantially downregulated by st. 31, whereas the Hoxd12 expression domain extended anteriorly at this stage (black arrowheads in Figure 3D). These results were roughly consistent with the RNA-seq data. We cannot completely reject the possibility that this timing difference is due to the different physical time-resolution of data sampling between these species (six time points over 20 days in the bamboo shark and four time points over 4 days in the mouse). However, given that this data set captured the similar expression dynamics of HoxA/D clusters between these species (Figure 1D; also see Figure 4C) as well as the differentiation dynamics of myocytes and chondrocytes (Figure 1—figure supplement 8), these results quite likely represent an interesting difference in the transcriptional regulation of SHH downstream genes between fins and limbs.

![Figure 3.](https://cdn.elifesciences.org/articles/62865/elife-62865-fig3-v2.jpg)

**Figure 3.:** (A, B) Scaled expression of Shh and related genes in mouse limb buds (A) and bamboo shark fin buds (B), respectively. The rectangles indicate the expression peaks of Shh, Hoxd9, and Hoxd10 (magenta), Shh target genes (yellow) and Hoxd11 and Hoxd12 (green). (C, D) Whole-mount in situ hybridization of Ptch1 and Hoxd12 in mouse limb buds (C) and bamboo shark fin buds (D); scale bars, 200 μm. White arrowheads in (D) indicate restricted expression of Ptch1 in bamboo shark fin buds. Black arrowheads in (C and D) indicate anteriorly extended expression of Hoxd12.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/62865/elife-62865-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** Red filled rectangles, the expression peak of Shh, Hoxd9, and Hoxd10; yellow filled rectangles, the expression peak of Shh target genes; green filled rectangles, the expression peak of Hoxd11 and Hoxd12.

![Figure 4.](https://cdn.elifesciences.org/articles/62865/elife-62865-fig4-v2.jpg)

**Figure 4.:** (A) Euclidean distances of the transcriptome profiles. Every combination of time points of bamboo shark fin buds and mouse limb buds is shown. The darker colors indicate a greater similarity between gene expression profiles. (B) A line plot of the Euclidean distances shown in (A). The x axis indicates the mouse limb stages, and the y axis is the Euclidean distance. (C) The same as (A) except that only Hoxd genes are included. (D, E) Scatter plots of the first and second principal components (D) and of the second and third components (e). Arrows in (E) indicate the time-order of transcriptome data. (F) Count of tissue-associated genes expressed in mouse forelimb buds. Genes with 0.65 ≤ entropy were counted.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/62865/elife-62865-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** Cross-species comparisons of transcriptome data between the two species with indicated distance methods. Note that these methods consistently show the closest distance around E10.5 and st. 27.5–30.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/62865/elife-62865-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** (A) The ratio of explained variable for each of the principal components from Figure 4D and E. (B) Euclidean distance measures using the indicated principal components. Note that individual principal components do not reproduce the hourglass-shaped conservation shown in Figure 4A, but PC1, PC2, and PC3 are sufficient for the most part to reproduce Figure 4A. (C) Percentage of stage-associated genes with [z ≤ 1.0] for mouse limb buds (left) and bamboo shark fin buds (right). Note that both species showed a low percentage of stage-associated genes during the middle stages of development. (D) Number (left) and fraction (right) of tissue-associated genes expressed in mouse limb buds. Tissue specificity was evaluated by entropy using RNA-seq data from 71 mouse tissues. A gene with entropy ≥0.65 was considered a tissue-specific gene. In the right panel, gene counts were normalized based on the number of total expressed genes. Note that the number of tissue-associated genes was lowest at E10.5.

### Hourglass-shaped conservation

Several studies have reported a temporally heterogeneous diversification of embryonic transcriptomes, such that the middle stages are more conserved than early or late stages (e.g. Irie and Kuratani, 2011; Kalinka et al., 2010; Levin et al., 2012). These observations are considered to support the notion of the developmental hourglass (or egg timer), which has been proposed to explain the morphological similarity of mid-stage embryos based on developmental constraints, such as strong interactions between tissues or Hox-dependent organization of the body axis (Duboule, 1994; Raff, 1996). In addition, a previous transcriptomic analysis reported that the late stage of mammalian limb development has experienced relatively rapid evolution (Maier et al., 2017). To examine which developmental stages of fins and limbs are conserved, we calculated the distance between the fin and limb transcriptome data. As a result, four different distance methods that we examined consistently indicated that the limb bud at E10.5 and the fin buds at st27.5–30 tended to have a relatively similar expression profile (Figure 4A for a Euclidean distance measure and Figure 4—figure supplement 1 for other types of distance measures). In addition, the transcriptomic profile of all the stages of examined fin buds showed the highest similarity to that of E10.5 limb bud (Figure 4B). Therefore, the mid-stages of limb and fin buds tend to be conserved over 400 million years of evolution.

To find factors that underlie the mid-stage conservation, we analyzed Hox genes, which were proposed to be responsible for the developmental hourglass (Duboule, 1994). We found that the comparison of only Hox gene expression did not reproduce the hourglass-shaped conservation (Figure 4C), suggesting that other mechanisms constrain the middle stage of development. We further performed principal component analysis (PCA) of gene expression profiles to identify genes responsible for the hourglass-shaped conservation. The first component, PC1, distinguished transcriptome data mostly by species differences (Figure 4D). In contrast, PC2 was correlated with the temporal order of mouse limb buds (Figure 4D). PC2 was also weakly correlated with the temporal order of bamboo shark fin buds except at st27 (Figure 4D), but PC3 showed a clearer correlation (Figure 4E). These three components were mostly sufficient to reproduce the mid-stage conservation in Figure 4A (Figure 4—figure supplement 2A for the ratio of explained variables and 2B for the Euclidean distance measure). Interestingly, the plot with PC2 and PC3 roughly mirrored the hourglass-shaped conservation because the earliest and latest stages were placed more distantly than the middle stages in this representation (Figure 4E). Indeed, the major loadings of PC2 consisted of the conserved late expressed genes (C8) and the heterochronically regulated genes (C9 and C12) identified in Figure 2A (see Table 2 for the top 25 genes of PC2). Similarly, PC3 consisted of the conserved early genes (a part of C15) and the heterochronically regulated genes (C12 and C13; see Supplementary file 9 for the loadings of PC3 and others), suggesting that the presence of heterochronically regulated genes may at least partly contribute to the mid-stage conservation and the distant relationship between the early/late stages of fins and limbs. These results indicate that the mass heterochronic shift in gene expression, at least in part, contributes to the long distances between early- and late-stage expression profiles (Figure 4E).

**Table 2.**
 PCA loadings.


<table>
  <thead>
    <tr>
      <th colspan="3">Loading axis: PC2</th>
    </tr>
    <tr>
      <th>Gene symbol</th>
      <th>Cluster name</th>
      <th>Loading</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>TRHDE</td>
      <td>C8</td>
      <td>0.31</td>
    </tr>
    <tr>
      <td>PAX9</td>
      <td>C11</td>
      <td>0.3</td>
    </tr>
    <tr>
      <td>COL9A2</td>
      <td>C8</td>
      <td>0.3</td>
    </tr>
    <tr>
      <td>RTN4R</td>
      <td>C8</td>
      <td>0.3</td>
    </tr>
    <tr>
      <td>APC2</td>
      <td>C9</td>
      <td>0.3</td>
    </tr>
    <tr>
      <td>CNMD</td>
      <td>C8</td>
      <td>0.29</td>
    </tr>
    <tr>
      <td>HOXD13</td>
      <td>C8</td>
      <td>0.29</td>
    </tr>
    <tr>
      <td>FAM69C</td>
      <td>C8</td>
      <td>0.29</td>
    </tr>
    <tr>
      <td>WFIKKN2</td>
      <td>C8</td>
      <td>0.29</td>
    </tr>
    <tr>
      <td>HOXA13</td>
      <td>C8</td>
      <td>0.29</td>
    </tr>
    <tr>
      <td>LRRN3</td>
      <td>C12</td>
      <td>0.29</td>
    </tr>
    <tr>
      <td>HPSE2</td>
      <td>C9</td>
      <td>0.29</td>
    </tr>
    <tr>
      <td>SERPINB1A</td>
      <td>C11</td>
      <td>0.29</td>
    </tr>
    <tr>
      <td>CDKN2B</td>
      <td>C8</td>
      <td>0.28</td>
    </tr>
    <tr>
      <td>LTBP1</td>
      <td>C8</td>
      <td>0.28</td>
    </tr>
    <tr>
      <td>CDH19</td>
      <td>C8</td>
      <td>0.28</td>
    </tr>
    <tr>
      <td>PDZD2</td>
      <td>C8</td>
      <td>0.28</td>
    </tr>
    <tr>
      <td>NLGN3</td>
      <td>C9</td>
      <td>0.28</td>
    </tr>
    <tr>
      <td>MATN1</td>
      <td>C8</td>
      <td>0.28</td>
    </tr>
    <tr>
      <td>MYOD1</td>
      <td>C8</td>
      <td>0.28</td>
    </tr>
    <tr>
      <td>TSPAN11</td>
      <td>C12</td>
      <td>0.28</td>
    </tr>
    <tr>
      <td>SERINC2</td>
      <td>C9</td>
      <td>0.28</td>
    </tr>
    <tr>
      <td>FYB</td>
      <td>C8</td>
      <td>0.28</td>
    </tr>
    <tr>
      <td>KIF1A</td>
      <td>C8</td>
      <td>0.28</td>
    </tr>
    <tr>
      <td>COL9A3</td>
      <td>C8</td>
      <td>0.28</td>
    </tr>
  </tbody>
</table>

Because a recent report suggests that pleiotropy of genes is related to hourglass-shaped conservation (EXPANDE Consortium et al., 2017), we counted the number of genes with stage- or tissue-specific expression. Consistent with the previous report (EXPANDE Consortium et al., 2017), we detected a relatively low number of stage-associated genes during the middle stages of mouse forelimb and bamboo shark fin development (Figure 4—figure supplement 2C). To evaluate the tissue specificity of genes, we first calculated Shannon entropy of gene expression patterns by analyzing RNA-seq data from 71 mouse tissues as released by the ENCODE project (Davis et al., 2018; Supplementary file 10 for the list of RNA-seq data). Namely, genes expressed only in a few tissues score lower with respect to entropy (thus, these genes are more specific). We counted genes with 1.0 ≥ TPM and 0.65 ≤ entropy and, again, found that the number of tissue-associated genes was relatively low at E10.5 (Figure 3F). Together, these results indicate an inverse correlation between the hourglass-shaped conservation and the number of tissue- and stage-specific genes.

### Open chromatin region (OCR) conservation

Next, we systematically identified putative gene regulatory sequences involved in mouse limb development and sought a possible cause for the hourglass-shaped conservation in gene regulatory sequences. To this end, we applied ATAC-seq, which detects OCRs (putative active regulatory sequences), to time-series of forelimb buds at E9.5–E12.5 with three replicates. First, as a positive control, we found that ATAC-seq peaks that were determined by MACS2 peak caller covered 10 of 11 known limb enhancers of the HoxA cluster (Figure 5A and Figure 5—figure supplement 1), suggesting a high coverage of true regulatory sequences. Consistently, our ATAC-seq data showed relatively high scores for a quality control index, fraction of reads in peaks (FRiP), as compared with data downloaded from the ENCODE project (Davis et al., 2018; Figure 5B). Next, to examine evolutionary conservation, we performed BLASTN (Camacho et al., 2009) for the sequences in the ATAC-seq peaks against several vertebrate genomes. Reinforcing the result of the transcriptome analysis, we found that evolutionarily conserved sequences were most accessible at E10.5 (Figure 5C). To confirm this result, we also used a different alignment algorithm, LAST (Kiełbasa et al., 2011) with the bamboo shark and the alligator (Green et al., 2014) genomes. Alignment results for both analyses consistently indicated that the OCRs of E10.5 forelimb bud more frequently contained conserved sequences relative to those of other time points (Figure 5D; see Figure 5—figure supplement 2A and B for the absolute counts of conserved sequences). Therefore, activation of conserved gene regulatory sequences may be one of the proximate causes for the hourglass-shaped conservation of fin and limb transcriptome data.

![Figure 5.](https://cdn.elifesciences.org/articles/62865/elife-62865-fig5-v2.jpg)

**Figure 5.:** (A) ATAC-seq signals in the enhancer regions of the HoxA cluster. e1 to e4, known limb enhancers. Green vertical lines below the signals, peak regions determined by MACS2. (B) Comparison of a quality index, FRiP, for ATAC-seq data. Blue bars are samples with a FRiP score >0.2. The number in the end of the label name indicates the replicate number. (C) Conservation analysis of sequences in ATAC-seq peaks with BLASTN. The values to the right of each graph indicate the fraction of conserved sequences in the total peak regions. The common name of each genome sequence is indicated above the graph. The not-conserved heatmap indicates the fraction of sequences that were not aligned to any genome sequences and thus serve as a negative control. (D) Temporal changes of sequence conservation frequency in ATAC-seq peaks with LAST. Error bars: SEM.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/62865/elife-62865-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (A) Correlation distance between samples. The numbers in the end of the sample names indicate the replicates of indicated stages. Darker color means more similar gene expressions. (B) Percentage of peak regions in the genome sequence. (C) ATAC-seq signals in BPM (blue signals), peak regions (blue rectangles) and the known limb enhancers of HoxA cluster (red rectangles, e1–e19). Note that only e5 is not covered by ATAC-seq data.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/62865/elife-62865-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** (A, B) The absolute count of OCRs that overlap with sequences conserved between the mouse and the alligator (A) and the bamboo shark (B). Error bars, SEM. (C, D) The fraction of conserved OCRs sorted by the identified clusters in Figure 6A. Sequence conservation was estimated by pairwise alignment using LAST (A–D).

### Temporal dynamics of open chromatin domains

To further characterize the ATAC-seq peaks, we next performed a clustering analysis. Using one of the three replicates for each stage, we collected the summits of peaks and the surrounding 1400 bp and carried out hierarchical clustering, which resulted in eight clusters (C1–C8; Figure 6A) that consisted of broad (C1 and C2), E11.5/E12.5-specific (C3 and C4), stable (C5 and C6), E10.5-specific (C7), and E9.5-specific (C8) peaks. The overall clustering pattern was reproducible by other combinations of replicates if its FRiP was ≥0.20 (Figure 6—figure supplement 1). Consistent with the above conservation analysis, E10.5-specific peaks frequently overlapped conserved sequences (Figure 5—figure supplement 2C and D).

![Figure 6.](https://cdn.elifesciences.org/articles/62865/elife-62865-fig6-v2.jpg)

**Figure 6.:** (A) The heatmap (left) shows whole-genome clustering of ATAC-seq peaks. Each row indicates a particular genome region with a length of 1400 bp. Columns indicate developmental stages. C1−C8 are cluster numbers. The motifs (right) show the rank of enriched motifs in the sequences of each cluster. (B) Top, volcano plots of ATAC-seq signals between indicated stages (p-values, two-sided Student’s t-test). Bottom, the counts of differential signals (black dots in the top panel). + and − are genomic regions with increased or decreased signals, respectively. (C) The fraction of limb-specific OCRs for each cluster.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/62865/elife-62865-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** DDifferent replicates were used for the same analysis as shown in Figure 6A. The number after the stage name indicates the replication number. Note that the clustering analyses with different replicates identified clusters similar to those in Figure 6A (compare the left-most panel with the second and third panels from the left). Including replicates with a low-quality score resulted in a relatively small fraction of early stage-specific peaks and a large fraction of late stage-specific peaks (right-most panel).

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/62865/elife-62865-fig6-figsupp2-v2.jpg)

**Figure 6—figure supplement 2.:** The top five motifs from clusters C5 and C6 determined while using all other peaks as the background sequence.

![Figure 6—figure supplement 3.](https://cdn.elifesciences.org/articles/62865/elife-62865-fig6-figsupp3-v2.jpg)

**Figure 6—figure supplement 3.:** The top five motifs from clusters C5 and C6 determined while using all other peaks as the background sequence.

![Figure 6—figure supplement 4.](https://cdn.elifesciences.org/articles/62865/elife-62865-fig6-figsupp4-v2.jpg)

**Figure 6—figure supplement 4.:** The top five motifs from each cluster. See Supplementary data for the full list of motifs. C1–C8 correspond to the clusters in Figure 6A.

![Figure 6—figure supplement 5.](https://cdn.elifesciences.org/articles/62865/elife-62865-fig6-figsupp5-v2.jpg)

**Figure 6—figure supplement 5.:** The average number of top-ranked motifs identified by de novo motif discovery in Figure 6—figure supplement 4 are plotted against mouse embryonic stages. The average numbers were calculated using all three replicates of ATAC-seq peaks at each stage. Rows indicate clusters identified in Figure 6A; columns indicate motif rank. Error bars, SEM. C1–C8 correspond to the clusters in Figure 6A. Note that the number of CTCF motifs (top-ranked in C5) was relatively stable over time, which is consistent with the clustering analysis shown in Figure 6A. In addition, the number of motifs enriched for C3, such as BHLHA15, HOX13, TEAD, and Tlx?, increased over time. In contrast, COUP-TFII and TCF7L2 motifs decreased over time. Interestingly, LHX and HOX9 motifs were transiently increased at E10.5.

To characterize the regulatory features of the clusters, we performed motif analysis in each cluster using HOMER (Heinz et al., 2010). First, it was convincing that stable peaks (C5 and C6) were enriched for the CTCF binding motif both in de novo motif discovery (Figure 6A) and known motif enrichment analysis (Figure 6—figure supplement 2), which is a major regulator of three-dimensional genomic structure. This result was consistent whether random genomic regions or other peak regions were used for the background (Figure 6—figure supplement 3). In addition, E11.5/E12.5-specific peak C3 was enriched for the HOX13 motif (Figure 6A), which was consistent with the increase in the expression of 5ʹ Hox genes (Figure 1D). C4 was also enriched for motifs similar to those of C3, but the HOX13 motif was detected only in known motif enrichment analysis (compare Figure 6—figure supplements 2 and 3). The enrichment of the HOX9 motif in E10.5-specific peaks (C7) was also consistent with our RNA-seq data, in which Hoxd9 and Hoxa9 expression levels peaked at E10.5 (Figure 1D). Interestingly, in E10.5-specific peaks (C7), the LHX1-binding motif was ranked at the top of the motif enrichment list the closely related transcription factors Lhx2, Lhx9, and Lmx1b are required to mediate a signaling feedback loop between ectoderm and mesenchyme in limb development (Tzchori et al., 2009). C8 was enriched for motifs similar to those in C7 (e.g. COUP-TFII), but the top-ranked transcription factor in the de novo motif discovery analysis was VSX2, which has a very similar binding sequence to the LHX motif (Figure 6—figure supplement 4). The LHX motif was top-ranked in C8 for the known motif enrichment analysis (Figure 6—figure supplement 2). For a better understanding of the dynamics of transcription factor motifs, we counted the average number of the above detected motifs within the OCRs of each stage, which revealed a transitional increase in LHX and HOX9 motifs at E10.5 and a gradual increase in the motifs detected in C3 over the developmental stages (Figure 6—figure supplement 3). In addition, Gene Ontology (GO) analysis for the peaks in each cluster revealed that the constitutively accessible peaks (C5, C6) were closely located to genes annotated with ‘cellular components’ (Supplementary file 11). Interestingly, the dynamically regulated peaks (C3, C4, C7, C8) were associated with genes with ‘developmental process’, ‘multicellular organism development’, and ‘anatomical structure morphogenesis’ (Supplementary file 11), suggesting that these dynamic OCRs regulate developmental genes. Together, these results suggest that there are E10.5-specific transient OCRs that exhibit several characteristics including their evolutionary conservation, the presence of LHX and HOX9 motifs and a close relation with developmental genes.

To confirm the results from the above clustering analysis, we also determined the genomic regions that showed a statistically significant increase or decrease in the ATAC-seq signal within a day by using all replicates. As a result, ATAC-seq signals were most increased during the transition from E9.5 to E10.5 in the mouse limb bud. From E10.5 to E11.5, the total number of decreased and increased signals was highest, indicating that the OCR landscape was most dynamically changing at E10.5 (Figure 6B). In contrast, relatively few significant changes were observed from E11.5 to E12.5. Thus, in contrast to the transcriptome analysis, stage-specific gene regulatory sequences are likely to be most accessible at E10.5. Moreover, by comparing the peaks of each cluster identified above with ATAC-seq peaks of other cells and tissues released by the ENCODE project (Davis et al., 2018; Supplementary file 10 for the full list of cells and tissues), we discovered that the C7 cluster (E10.5-specific peaks) contained more peaks that did not overlap with those of other cells and tissues. Again, in contrast to the transcriptome analysis, the data suggest that gene regulatory sequences that are accessible only at E10.5 tend to be limb-specific (Figure 6C). Taken together, these analyses revealed a unique regulatory landscape of forelimb buds at E10.5, which is enriched for evolutionarily conserved stage-specific and tissue-specific OCRs.

## Discussion

In this work, we applied transcriptomics and chromatin accessibility analysis to systematically study genetic changes that differentiate fins from limbs. Because of the slow sequence evolution and the embryo availability of the bamboo shark, we were able to compare transcriptional regulation of genes with high accuracy and found both heterochronic shifts and hourglass-shaped conservation of transcriptional regulation between fin and limb development. Here, we discuss the interpretations, limitations, and implications of these results.

Our time-series transcriptome data indicated that a remarkable number of genes that exhibit the highest expression during the late stages of mouse limb bud development are decreased during the late stages of bamboo shark fin development (Figure 2). The simplest hypothesis for this mass heterochronic shift is that the later stages of limb development gained expression of one or a few upstream transcription factor(s) or signaling molecules that collectively regulate this group of genes. Interestingly, we also observed relatively extensive expression of the downstream targets of the SHH signaling pathway in mouse limb buds, as compared with bamboo shark fin buds (Figure 3). Because SHH-independent regulation of its target genes through the GLI3-HOX complex was previously reported (Chen et al., 2004), the mismatch between the peak expression of Shh and its target genes may be caused by such SHH-independent regulatory mechanisms that are absent in bamboo shark fin development. Given that direct and genetic interactions of GLI3 and HOX have a significant impact on autopod formation, the emergence of this interaction may be a key component of the mass heterochronic shift and the acquisition of autopod-related developmental regulation in the tetrapod lineages. However, because we compared only two species, it is equally possible that the late stages of shark fin development lost this SHH-independent gene regulation. Alternatively, given that the evolutionary distance between these two species is >400 million years, it is also possible that every one of these genes independently shifted their expression to the later stages of limb development or to the early stages of shark fin development. Further taxon sampling and functional analyses will reveal the relation between the mass heterochronic shift and the emergence of the autopod.

Related to the potential changes in regulation of SHH target genes, by analyzing catshark fin buds, we previously proposed that the expression domains of genes that are positively regulated by SHH might have expanded anteriorly during the fin-to-limb transition (Onimaru et al., 2015). We speculated that this expression changes may be linked to the loss of pro- and mesopterygial elements. Recently, this hypothesis was partially supported by another group who compared the gene expression pattern of lungfish and cichlid fin development (Woltering et al., 2020), where lungfish fin buds seem to exhibit an intermediate condition between non-sarcopterygian fish fins and tetrapod limbs in terms of gene expression distribution along the anterior-posterior axis. This group particularly emphasized that the absence and presence of the dynamics of the anterior expansion of Hoxd13 expression correlate with the difference between the metapterygial morphologies of lungfish and tetrapods (also see Johanson et al., 2007 for a conflicting report). However, the significance of changes in Hoxd13 expression remains unclear because of the following two reasons: (a) Hoxd13 expression pattern seems to quite vary among species—the anterior expansion of Hoxd13 expression has been observed in the fin buds of the little skate, the small-spotted catshark, and Polyodon (Davis et al., 2007; Freitas et al., 2007; Nakamura et al., 2015), while not in those of zebrafish and cichlids (Ahn and Ho, 2008; Woltering et al., 2020) and (b) in fish fins, the expression domain of Hoxa13, whose function is mostly redundant with Hoxd13, commonly spans from anterior to posterior regions in fish fin buds like as tetrapod limbs (Davis et al., 2007; Freitas et al., 2007; Nakamura et al., 2016). Therefore, while changes in Hoxd13 expression domain are likely to contribute to some degree of anatomical diversity, their impact is questionable in the context of the fin-to-limb transition. Nevertheless, our previous study and Woltering et al. commonly suggest that the anterior expansion of gene expression domains is likely associated with the substantial anatomical changes during the fin-to-limb transition. As discussed above, we speculate that the mass heterochronic shifts that we observed in the present study may be related to the gain of SHH-independent regulation of its target genes. Therefore, whether the anterior expansion of SHH-target gene expression is related to the mass heterochronic shifts will be one of the interesting questions to address in the future.

We observed that gene expression profiles are most highly conserved between bamboo shark fin buds at st. 27.5–30 and mouse forelimb buds at E10.5 (Figure 4). Consistent with this result, our chromatin accessibility analysis reveals that OCRs at E10.5 tend to contain evolutionarily conserved sequences (Figure 5). Whereas transcriptomic conservation during the middle of embryonic development has been reported by many groups using different species (e.g. Irie and Kuratani, 2011; Kalinka et al., 2010), analysis of regulatory sequence conservation during embryonic development has been either incomplete or controversial. For example, by analyzing histone acetylation marks on several developing organs in mouse embryos, Nord et al., 2013 proposed regulatory sequences active at E11.5 are exposed by the highest evolutionary constraint. However, they used stem cell lines as the substitutes for organs at early stages. Another study showed that genes expressed at the segmentation stage of zebrafish embryos tended to be surrounded by highly conserved non-coding sequences (Piasecka et al., 2013). Although their results are in line with our present study as discussed below, they did not show that these highly conserved non-coding sequences were indeed active at the segmentation stage. In addition to these studies, there is a conflicting observation that early, instead of middle, embryonic stages tend to be regulated by conserved OCRs (Uesaka et al., 2019). Therefore, our present study is the first to convincingly show a clear correlation of conservation status between transcriptomic data and OCRs. Our results suggest that evolutionary constraints on the gene regulatory apparatus are present during the middle stage of fin and limb development. What drives the hourglass-shaped conservation is still under debate. Interestingly, we found that stage- and tissue-specific OCRs were enriched in this conserved period, during which a relatively low number of stage- and tissue-specific genes were expressed (Figure 6). These quite contrasting observations imply that the mid-stage limb development is enriched for pleiotropic genes controlled by multiple tissue-specific enhancers, including limb-specific ones, rather than by constitutive promoters that often regulate housekeeping genes. Therefore, we speculate that, at least in the case of limb development, complex regulatory sequences that execute spatiotemporally specific transcriptional controls over pleiotropic genes constrain the evolvability of this particular period of morphogenesis, probably due to the vulnerability of complex regulation to genetic mutations.

In conclusion, the present study provides insights for the evolutionary origin of gene regulation that differentiates fins from limbs. In particular, comparative transcriptional analyses prompted us to hypothesize that mass heterochronic shifts of gene expression may have occurred during the fin-to-limb evolution. In addition, both transcriptome and open chromatin data point to an evolutionary constraint during mid-stage limb development, likely owing to gene regulatory complexity. Although these hypotheses require further taxon sampling and experimental tests, this study opens up new prospects for understanding not only the genetic basis of the fin-to-limb transition but also the general nature of morphological evolution.

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
      <td>Gene (Mus musculus)</td>
      <td>Hand2</td>
      <td>ENSEMBL</td>
      <td>ENSMUST00000040104.4</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>Gene (Mus musculus)</td>
      <td>Vcan</td>
      <td>ENSEMBL</td>
      <td>ENSMUST00000109546.8</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>Gene (Mus musculus)</td>
      <td>Aldh1a2</td>
      <td>ENSEMBL</td>
      <td>ENSMUST00000034723.5</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>Gene (Mus musculus)</td>
      <td>Ptch1</td>
      <td>ENSEMBL</td>
      <td>ENSMUST00000192155.5</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>Gene (Mus musculus)</td>
      <td>Hoxd12</td>
      <td>ENSEMBL</td>
      <td>ENSMUST00000001878.5</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>Gene (Chiloscyllium punctatum)</td>
      <td>Hand2</td>
      <td>ENSEMBL</td>
      <td>Chipun0004250/g4250.t1/ TRINITY_DN85524_c0_g1_i1</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>Gene (Chiloscyllium punctatum)</td>
      <td>Vcan</td>
      <td>This paper</td>
      <td>Chipun0003941/g3941.t1/ TRINITY_DN95522_c0_g1_i8</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>Gene (Chiloscyllium punctatum)</td>
      <td>Hoxd12</td>
      <td>This paper</td>
      <td>Chipun0005654/g5654.t1/TRINITY_DN85970_c0_TRINITYg1_i1</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>Gene (Chiloscyllium punctatum)</td>
      <td>Ptch1</td>
      <td>This paper</td>
      <td>Chipun0003320/g3320.t1/TRINITY_DN92499_c0_g1_i3</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>Gene (Chiloscyllium punctatum)</td>
      <td>Aldh1a2</td>
      <td>This paper</td>
      <td>Chipun0010503/g10503.t1/TRINITY_DN81423_c0_g1_i1</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>Strain, strain background (Mus musculus)</td>
      <td>C52BL/6</td>
      <td>Laboratory for Animal Resources and Genetic Engineering RIKEN,</td>
      <td>N/A</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Digoxigenin-AP, Fab fragments (Sheep)</td>
      <td>Millipore Sigma</td>
      <td>Cat# 11093274910</td>
      <td>polyclonal (1:4000)</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Mus musculus Hand2 forward primer</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>ACCAAACTCTCCAAGATCAAGACACTG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Mus musculus Hand2 reverse primer</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>TTGAATACTTACAATGTTTACACCTTC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Mus musculus Vcan forward primer</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>TGCAAAGATGGTTTCATTCAGCGACAC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Mus musculus Vcan reverse primer</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>ACACGTGCAGAGACCTGCAAGATGCTG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Mus musculus Aldh1a2 forward primer</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>ACCGTGTTCTCCAACGTCACTGATGAC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Mus musculus Aldh1a2 reverse primer</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>TCTGTCAGTAACAGTATGGAGAGCTTG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Mus musculus Hoxd12 forward primer</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>CTCAACTTGAACATGGCAGTGCAAGTG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Mus musculus Hoxd12 reverse primer</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>AGCTCTAGCTAGGCTCCTGTTTCATGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Mus musculus Ptch1 forward primer</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>GGGAAGGCAGTTCATTGTTACTGTAACTG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Mus musculus Ptch1 reverse primer</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>TGTAATACGACTCACTATAGGTCAGAAGCTGCCACACACAGGCATGAAGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Chiloscyllium punctatum Hand2 forward primer</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>ACCAGCTACATTGCCTACCTCATGGAC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Chiloscyllium punctatum Hand2 reverse primer</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>CACTTGTTGAACGGAAGTGCACAAGTC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Chiloscyllium punctatum Vcan forward primer</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>AGCTTGGGAAGATGCAGAGAAGGAATG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Chiloscyllium punctatum Vcan reverse primer</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>AGAGCAGCTTCACAATGCAGTCTCTGG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Chiloscyllium punctatum Aldh1a2 forward primer</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>TTGAACTTGTACTAAGTGGTATCGCTG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Chiloscyllium punctatum Aldh1a2 reverse primer</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>AGGATGTGAACATTAGGCTGACCTCAC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Chiloscyllium punctatum Hoxd12 forward primer</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>GCCAGTATGCAACAGATCCTCTGATGG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Chiloscyllium punctatum Hoxd12 reverse primer</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>CTAATGACCTGTTGTACTTACATTCTC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Chiloscyllium punctatum Ptch1 forward primer</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>TTCAGCCAGATTGCAGATTACATCAACC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Chiloscyllium punctatum Ptch1 reverse primer</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>TTCTCTGTGTTTCACATTCAACGTCCTG</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Nextera DNA Sample Preparation Kit</td>
      <td>Illumina</td>
      <td>Cat# FC-121–1031</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>TruSeq Stranded mRNA LT Sample Prep Kit</td>
      <td>Illumina</td>
      <td>Cat# RS-122–2101</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Trinity</td>
      <td>https://github.com/trinityrnaseq/trinityrnaseq</td>
      <td>RRID:SCR_013048</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Bowtie2</td>
      <td>http://bowtie-bio.sourceforge.net/bowtie2/index.shtml</td>
      <td>RRID:SCR_016368</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>BWA</td>
      <td>http://bio-bwa.sourceforge.net/</td>
      <td>RRID:SCR_010910</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MACS2</td>
      <td>https://github.com/macs3-project/MACS</td>
      <td>RRID:SCR_013291</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>HOMER</td>
      <td>http://homer.ucsd.edu/homer/motif/</td>
      <td>RRID:SCR_010881</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>RSEM</td>
      <td>https://github.com/deweylab/RSEM</td>
      <td>RRID:SCR_013027</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>scikit-learn</td>
      <td>https://scikit-learn.org/stable/</td>
      <td>RRID:SCR_002577</td>
      <td>N/A</td>
    </tr>
  </tbody>
</table>

### Animals

Animal experiments were conducted in accordance with the guidelines approved by the Institutional Animal Care and Use Committee (IACUC), RIKEN Kobe Branch, and experiments involving mice were approved by IACUC (K2017-ER032). The eggs of brownbanded bamboo shark (C. punctatum) were kindly provided by Osaka Aquarium Kaiyukan and were incubated at 25°C in artificial seawater (MARINE ART Hi, Tomita Pharmaceutical Co., Ltd.) and staged according to the published staging table (Onimaru et al., 2018). For mouse embryos, C52BL/6 timed-pregnant females were supplied by the animal facility of Kobe RIKEN, LARGE and sacrificed at different days after 9.5–12.5 days of gestation. For RNA-seq, fin buds and limb buds were dissected in cold seawater and phosphate-buffered saline (PBS), respectively, and stored at −80°C. For in situ hybridization, embryos were fixed overnight in 4% paraformaldehyde in PBS, dehydrated in a graded methanol series, and stored in 100% methanol at −20°C.

### RNA-seq

We sampled mouse forelimb buds at E9.5, E10.5, E11.5 and E12.5 and bamboo shark pectoral fin buds at st27, st27.5, st29, st30, st31, and st32 and pooled several individual samples by stage to obtain enough RNA for each time point. We considered this pooled sample to represent one biological replicate (other replicates were generated using different individuals). Total RNAs from these samples were extracted with the RNeasy Micro and Mini plus kit (QIAGEN, Cat. No. 74034 and 74134) and PicoPure RNA Isolation Kit (ThermoFisher, Cat. No. KIT0214). Genomic DNA was removed with gDNA Eliminator columns included with this kit. For quality control, the Agilent 2100 Bioanalyzer system and Agilent RNA 6000 Nano Kit (Agilent, Cat. No. 5067–1511) were used to measure the RNA integrity number for each sample. Using 237 ng of each of the RNA samples, strand-specific single-end RNA-seq libraries were prepared with the TruSeq Stranded mRNA LT Sample Prep Kit (Illumina, Cat. No. RS-122–2101 and/or RS-122–2102). For purification, we applied 1.8× (after end repair) and 1.0× (after adapter ligation and PCR) volumes of Agencourt AMPure XP (Beckman Coulter, Cat. No. A63880). The optimal number of PCR cycles for library amplification was determined by a preliminary quantitative PCR using KAPA HiFi HotStart Real-Time Library Amplification Kit (KAPA, Cat. No. KK2702) and was estimated to be 11 cycles for mouse limb buds and 10 cycles for bamboo shark fin buds. The quality of the libraries was checked by Agilent 4200 TapeStation High Sensitivity D1000. The libraries were sequenced after on-board cluster generation for 80 cycles using 1× HiSeq Rapid SBS Kit v2 (Illumina, Cat. No. FC-402–4022) and HiSeq SR Rapid Cluster Kit v2 (Illumina, Cat. No. GD-402–4002) on a HiSeq 1500 (Illumina) operated by HiSeq Control Software v2.2.58 (Run type: SR80 bp). The output was processed with Illumina RTA v1.18.64 for base-calling and with bcl2fastq v1.8.4 for de-multiplexing. Quality control of the obtained fastq files for individual libraries was performed with FASTQC v0.11.5. RNA-seq was performed with three biological replicates for each stage.

### Transcriptome assembly and orthology assignment

We used the NCBI RefSeq mouse proteins (GRCm38.p5; only curated proteins were used) and two bamboo shark gene lists: a genome sequence-based gene model (Hara et al., 2018) and transcripts assembled from RNA-seq in this study (see below) for orthology assignment. The amino acid sequences of the published gene model of the bamboo shark are available from https://doi.org/10.6084/m9.fig (Supplementary file 1). For the transcriptome assembly, the short reads from the bamboo shark RNA-seq data were trimmed and filtered with Trim Galore! (https://www.bioinformatics.babraham.ac.uk/projects/trim_galore/) and assembled using Trinity v2.4.0 (Grabherr et al., 2011; options: --SS_lib_type RF --normalize_max_read_cov 200 min_kmer_cov 2). Protein coding sequences were predicted with a program that finds coding regions, TransDecoder v3.0.1 (Haas et al., 2013), according to the guide in TransDecoder (Supplementary file 2 and 3). Using these coding gene lists as queries, orthologous pairs were assigned as illustrated in Figure 1—figure supplement 1. The idea behind this algorithm is the ‘gar bridge’ (Braasch et al., 2016), an empirical observation that a comparison including intermediate and slowly evolving animals yields a better resolution for identifying homologous sequences than a direct comparison between two species. First, BLASTP v2.7.1 was performed between mouse and bamboo shark genes reciprocally, and also against the coding genes of the elephantfish (or elephant shark; Callorhinchus_milii-6.1.3), spotted gar (LepOcu1), coelacanth (LatCha1), chicken (GRCg6a), alligator (ASM28112v4), and human (GRCh38.p12; options: -outfmt 6 -evalue 1e-30 -window 0). Then, the BLASTP results of bamboo shark queries against the animals listed above (except for the elephantfish) were concatenated, and the best hit across species (cross-species best hit) was identified for each of the bamboo shark genes. If there was no cross-species best hit, then the best hit among the elephantfish genes was retrieved, which may include cartilaginous fish-specific genes. Subsequently, orthologous pairs between mouse and bamboo shark genes were assigned by checking if a cross-species best hit from the bamboo shark BLASTP results also had a best hit in the BLASTP result of mouse genes against the corresponding animal (species-wise best hit; Supplementary files 4, 5, 6).

For quality control, the orthology of Fgf family members was independently determined by generating molecular phylogenetic trees (Figure 1—figure supplements 2 and 3). Amino acid sequences were aligned with an alignment tool, MAFFT v7.419–1 (Katoh et al., 2002; options: --localpair --maxiterate 1000) and trimmed with trimAL v1.2 (Capella-Gutiérrez et al., 2009; options: -gt 0.9 -cons 60). Then, maximum-likelihood trees were constructed with RaxML v8.2.12 (Stamatakis, 2014; options: -x 12345 p 12345 m PROTGAMMAWAG -f a -# 100). The orthology of Hox genes was confirmed based on genome synteny. These independently confirmed orthologous pairs were compared with the results of the above orthology assignment algorithm. For a comparison, we also used the results from a reciprocal best hit algorithm, proteinOrtho v6.0.4 (Lechner et al., 2011) and the previously generated orthology groups (Hara et al., 2018; Figure 1B).

### Quantification and scaling

The trimmed RNA-seq short reads were aligned to the transcript contigs for the bamboo shark and curated RefSeq genes (GRCm38.p5) for the mouse using RSEM v1.3.0 (Li and Dewey, 2011) and Perl scripts (align_and_estimate_abundance.pl and abundance_estimates_to_matrix.pl) in the Trinity package. TPM (transcripts per million), but not TMM (trimmed mean of M-values), was used for all analyses, because we found some artificial biases in TMM values (see Figure 1—figure supplement 4). TPM values from the splicing variants of a single gene were summed up to generate a single value per gene. Then, the means and standard errors of TPM values from three replicates were used for the downstream analyses. Genes with a maximum TPM <1.0 were considered not expressed. For clustering and distance measures, TPM values were scaled so that the maximum value of each gene of each species was set to ‘1’ (Max 1). Whereas this scaling method loses information with respect to the absolute value of the TPMs, it has a substantial advantage when comparisons are being made between evolutionarily distant species. Indeed, previous comparative transcriptome studies have scaled gene expression values in different ways. Among those approaches, the use of Z-scores (standardization) and log transformations are relatively common strategies (e.g. Kalinka et al., 2010; Leiboff and Hake, 2019; Levin et al., 2016). Some researchers have used the intact RPKM (reads per kilobase per million) values to compare closely related species (Wang et al., 2013), but, because the RPKM is known to be inconsistent between samples even within a species (Wagner et al., 2012). Scaled transcriptional values are commonly used for clustering analyses and visualization of transcriptomic data from different samples within a single species. In this case, scaling is mainly aimed at flattening the dynamic range of transcription levels among genes. For inter-specific comparisons, scaling is also useful for being simultaneously sensitive to differentially regulated genes and also insensitive to conserved housekeeping genes. Here, we examine the effect of several scaling methods and the use of intact TPM values. We define the four relevant scaling methods as follows:

$$
M_{g,s,t}=\frac{x_{g,s,t}}{max{x_{g,s,t}:t=1..T_{s}}}
$$



$$
Z_{g,s,t}=\frac{x_{g,s,t}-x¯_{g,s}}{\sigma_{g,s}}
$$



$$
U_{g,s,t}=\frac{x_{g,s,t}}{{x_{g,s,t}:t=1..T_{s}}}
$$



$$
L_{g,s,t}=log_{10}x_{g,s,t}+1
$$

where xg,s,t is the intact TPM of gene g, species s, and time point t; Ts is the total number of time points in species s; Mg,s,t, Zg,s,t, Ug,s,t and Lg,s,t are scaled values that we refer to as the Max 1, Z-score, Unit vector and Log10 methods, respectively; and $x¯_{g,s}$ and $\sigma_{g,s}$ are the mean and standard deviation, respectively, of {xg,s,1...xg,s,Ts}.

First, we take a simple example to develop some intuition as to how these calculations transform TPM values. Let us assume that we compare two species [(species 1 and species 2)], and each species has two genes (gene 1 and gene 2) and three developmental time points (t1, t2, and t3; Figure 1—figure supplement 5A). Gene 1 is a constitutively active gene (i.e. a housekeeping gene), and gene 2 is differentially regulated between species. In this example, we want to identify t2 as the most conserved time point because gene two is expressed in both species at this time point. In addition, we want to ignore the subtle expression differences of gene one within and between species. As seen in Figure 1—figure supplement 5A, scaling by the Max 1, Unit vector, and Log10 methods effectively conserves the expression dynamics of gene two while suppressing the expression noise of gene 1. In contrast, Z-score scaling amplifies the expression dynamics of both genes to the same degree, which suggests that the Z-score method is sensitive to noise. Calculation of the Euclidean distances for each time point between species 1 and 2 (‘Distance’ in Figure 1—figure supplement 5A) shows that although all scaling methods and the use of intact TPMs indicate that t2 is the most similar time point, Max one creates a greater contrast between conserved and non-conserved time points than the other methods. Therefore, Max one is likely to be able to sensitively detect inter-specific differences. We also examined a subset of our real transcriptomic data from mouse limb buds and bamboo shark fin buds. As an example, we chose three housekeeping genes conserved in most vertebrates, Psmd5, Mrpl21, and Polr1b—these genes are listed both in a housekeeping gene list https://www.tau.ac.il/~elieis/HKG/HK_genes.txt (Eisenberg and Levanon, 2013) and in the BUSCO data set, a gene list used to assess the completeness of genome assemblies (Simão et al., 2015). As shown in Figure 1—figure supplement 5B and C, the TPM values of these genes were stable throughout developmental time in both species, suggesting that these genes also play a role in the maintenance of basic cellular function in bamboo shark fin development. However, the TPM values of Mrpl21 and Polr1b in mouse limb buds were roughly twice as high as those in bamboo shark fin buds. One explanation for this finding is that the expression of housekeeping genes is low in the bamboo shark because the relatively low temperature of the environment in which it lives slows its metabolic activity. We note, however, that there are many technical uncertainties when directly interpreting TPM values, particularly when comparing distantly related species. For example, differences in DNA sequences of transcripts (such as variations in GC content) between species probably affects the efficiency of library preparation and sequencing. The TPM values are also likely to be biased because of the incompleteness of the reference transcriptome sequence that we used for the bamboo shark (e.g. some genes lack 3ʹ untranlated regions). Therefore, the dynamics of TPM values extracted by scaling methods rather than absolute TPM values are likely to contain more biologically relevant information. Of the scaling methods, Max 1, Unit vector, and Log10 conserved the stable expression profile of the housekeeping genes, whereas the Z-score method amplified the subtle variation in TPM values as seen in the above simple example (Figure 1—figure supplement 5B). In particular, the Max one and Unit vector methods transformed the TPM values into relatively comparable values between the two species (compare Figure 1—figure supplement 5B with C). For a comparison, we also examined three genes that are heterochronically regulated between bamboo shark fin buds and mouse limb buds (Figure 1—figure supplement 6A and B). In this case, all of the scaling methods seemed to conserve the temporal dynamics of gene expression.

To obtain an objective measure, we calculated the ratio of the interspecific Euclidean distance of the three housekeeping genes to that of the three heterochronic genes with different scaling methods (Figure 1—figure supplement 6C and D). Namely, the Euclidean distance of expression values was close to zero if we used only housekeeping genes (left panel of Figure 1—figure supplement 6C), but it was larger when comparing heterochronic genes (right panel of Figure 1—figure supplement 6C). As a result, the Max1 method resulted in the highest ratio (Figure 1—figure supplement 6D), suggesting that Max1 is most sensitive to interspecific differences in dynamically regulated genes.

### Clustering analyses of transcriptome data

The scaled values of each orthologous pair were concatenated as a 10-dimensional vector (consisting of four stages for mouse limb buds and six stages for bamboo shark fin buds), and all gene expression vectors were dimensionally reduced with UMAP (hyper parameters: a = 10, b = 1.8) followed by hierarchical clustering (hyper parameters: method = 'ward', metric = 'euclidean'; the code is available at https://github.com/koonimaru/easy_heatmapper; copy archived at https://archive.softwareheritage.org/swh:1:dir:b1b8edece650ac9e8a7458354aaf69e74f437092;origin=https://github.com/koonimaru/easy_heatmapper;visit=swh:1:snp:a69e903d0efcde99cb203ec86832c5e5c56a43e5;anchor=swh:1:rev:ba1fde133621a52390b82b4c9f73711a56f252b8/). To find genes that have an opposite trend in their expression relative to 'Heterochronic2', a Pearson correlation coefficient (PCC) for TPM values and developmental stages was calculated for each gene for each species, and genes with PCC > 0.5 for bamboo shark fin buds and PCC < −0.5 for mouse limb buds were listed (Figure 2—figure supplement 1B and Supplementary file 8). For the distance measurements, four different distance methods were calculated: Euclidean distance ($\sqrt{\sumu_{i}-v_{i}^{2}}$), correlation distance ($1-\frac{u-u¯v-v¯}{u-u¯_{2}v-v¯_{2}}$), Shannon distance ($-\frac{1}{2}\sumu_{i}log\frac{u_{i}+v_{i}}{2u_{i}}+v_{i}log\frac{u_{i}+v_{i}}{2v_{i}}$), standardized Euclidean distance ($\sqrt{\sumu_{i}-v_{i}^{2}/V_{i}}$), where u and v are gene expression vectors of two samples and Vi is the variance computed over all the values of gene i. For PCA analysis, we used the PCA module in a python package, scikit-learn (https://scikit-learn.org/stable/).

For the stage-associated gene analysis in Figure 3—figure supplement 1B and C, we first calculated the z-score of each gene at each stage as $\frac{u_{k,i}-u¯_{i}}{\sigma_{i}}$, where $u_{k,i}$ is the TPM value of gene i at stage k, $u¯_{i}$ is a mean of TPM over all the stages, and $\sigma_{i}$ is the standard deviation of the TPM. Genes with TPM ≥ 1.0 and the absolute Z-score ≥1.0 were counted as stage-associated genes. For the tissue-associated gene analysis, the entropy of each gene was calculated using RNA-seq data of 71 tissues downloaded from the ENCODE web site (https://www.encodeproject.org/; see Supplementary file 10 for all list). Entropy was calculated as follows:

$$
p_{k,i}=\frac{TPM_{k,i}}{\sum_{k}TPM_{k,i}}
$$



$$
H_{i}=-\sum_{k}p_{k,i}logp_{k,i}
$$

where $TPM_{k,i}$ is the TPM value of gene i in tissue k, $p_{k,i}$ is a probability distribution and $H_{i}$ is entropy. Genes with TPM (of mouse limb buds) ≥ 1.0 and 0.65 ≤ entropy were counted as tissue-associated genes.

### Whole-mount in situ hybridization

To clone DNA sequences for RNA probes, we used primers that were based on the nucleotide sequences in the ENSEMBL database (https://www.ensembl.org) for mouse genes and in the transcriptome assembly (Supplementary file 3); bamboo shark Hand2 (Chipun0004250/g4250.t1/ TRINITY_DN85524_c0_g1_i1), 5′-ACCAGCTACATTGCCTACCTCATGGAC-3′ and 5′-CACTTGTTGAACGGAAGTGCACAAGTC-3′; bamboo shark Vcan (Chipun0003941/g3941.t1/ TRINITY_DN95522_c0_g1_i8), 5′-AGCTTGGGAAGATGCAGAGAAGGAATG-3′ and 5′-AGAGCAGCTTCACAATGCAGTCTCTGG-3′; bamboo shark Hoxd12 (Chipun0005654/g5654.t1/TRINITY_DN85970_c0_g1_i1), 5′-GCCAGTATGCAACAGATCCTCTGATGG-3′ and 5′-CTAATGACCTGTTGTACTTACATTCTC-3′; bamboo shark Ptch1 (Chipun0003320/g3320.t1/TRINITY_DN92499_c0_g1_i3), 5′-TTCAGCCAGATTGCAGATTACATCAACC-3′ and 5′-TTCTCTGTGTTTCACATTCAACGTCCTG-3′; bamboo shark Aldh1a2 (Chipun0010503/g10503.t1/TRINITY_DN81423_c0_g1_i1), 5′-TTGAACTTGTACTAAGTGGTATCGCTG-3′ and 5′-AGGATGTGAACATTAGGCTGACCTCAC-3′; mouse Hand2 (ENSMUST00000040104.4), 5′-ACCAAACTCTCCAAGATCAAGACACTG-3′ and 5′-TTGAATACTTACAATGTTTACACCTTC-3′; mouse Vcan (ENSMUST00000109546.8), 5′-TGCAAAGATGGTTTCATTCAGCGACAC-3′ and 5′-ACACGTGCAGAGACCTGCAAGATGCTG-3′; mouse Hoxd12 (ENSMUST00000109546.8), 5′-TGCAAAGATGGTTTCATTCAGCGACAC-3′ and 5′-ACACGTGCAGAGACCTGCAAGATGCTG-3′; mouse Aldh1a2 (ENSMUST00000034723.5), 5′-ACCGTGTTCTCCAACGTCACTGATGAC-3′ and 5′-TCTGTCAGTAACAGTATGGAGAGCTTG-3′; mouse Ptch1 (ENSMUST00000192155.5), 5′-GGGAAGGCAGTTCATTGTTACTGTAACTG-3′ and 5′-TGTAATACGACTCACTATAGGTCAGAAGCTGCCACACACAGGCATGAAGC-3′. Note that although we also tried bamboo shark Shh expression analysis using several RNA probes, we did not obtain specific signals. Fixed embryos were processed for in situ hybridization as described (Westerfield, 2000) with slight modifications. Briefly, embryos were re-hydrated with 50% MeOH in PBST (0.01% Tween 20 in PBS) and with PBST for 5–30 min each at room temperature (RT). Then, embryos were treated with 20 μg/ml proteinase K (Roche) in PBST (5 s for mouse E11.5 and E12.5 embryos, 5 min for st. 27 and st. 29 bamboo shark embryos, 10 min for st. 31 and st. 32 bamboo shark embryos). After the proteinase treatment, embryos were fixed in 4% paraformaldehyde/PBS for 1 hr, followed by one or two washes with PBST for 5–10 min each. Optionally, if embryos had some pigmentation, they were immersed in 2% H2O2 until they became white. Then, embryos were incubated for 1 hr in preheated hybridization buffer (50 ml formaldehyde; 25 ml 20× SSC, pH 5.0; 100 μl 50 mg/ml yeast torula RNA; 100 μl 50 mg/ml heparin; 1 ml 0.5 M EDTA; 2.5 ml 10% Tween 20; 5 g dextran sulfate; and DEPC-treated MilliQ water to a final volume of 100 ml) at 68°C. Subsequently, embryos were incubated with fresh hybridization buffer containing 0.25–4 μl/ml of RNA probes at 68°C overnight. Embryos were washed twice with preheated Wash buffer 1 (50 ml formaldehyde; 25 ml 20× SSC, pH 5.0; 2.5 ml 10% Tween 20; and DEPC-treated MilliQ water to a final volume of 100 ml) for 1 hr each at 68°C; once with preheated Wash buffer 2, which consisted of equal volumes of Wash buffer 1 and 2× SSCT (10 ml 20× SSC, pH 7.0; 1 ml 10% Tween 20; and MilliQ water to a final volume of 100 ml), for 10 min at 68°C; once with preheated 2× SSCT at 68°C for 10 min; and once with TBST at room temperature for 10 min. Embryos were then incubated with a blocking buffer (20 μl/ml 10% bovine serum albumin, 20 μl/ml heat-inactivated fetal bovine serum in TBST) for 1 hr at room temperature, followed by incubation with 1/4000 anti-digoxigenin (Roche) in fresh blocking buffer at 4°C overnight. Embryos were washed four times with TBST for 10–20 min each and were incubated at 4°C overnight. Finally, embryos were incubated with NTMT (200 μl 5 M NaCl; 1 ml 1 M Tris-HCl, pH 9.8; 500 μl 1 M MgCl2; 100 μl 10% Tween 20; and MilliQ water to a final volume of 10 ml) for 20 min and then with 15 μg/ml nitro-blue tetrazolium chloride (NBT) and 175 μg/ml 5-bromo-4-chloro-3-indolyphosphate p-toluidine salt (BCIP) in NTMT for 10 min to 2 hr until signals appeared. Pictures were taken with an Olympus microscope. For bamboo shark embryos, experiments were performed for at least two biological replicates.

### ATAC-seq

Mouse forelimb buds at E9.5, E10.5, E11.5, and E12.5 were dissected, and samples from several individuals were pooled by stage to obtain enough cells. We considered this pooled sample to represent a biological replicate (other replicates were generated using different individuals). To obtain single-cell suspensions, pooled samples were treated with collagenase for 10 min at room temperature. The tissues were then dissociated into single-cell suspensions by pipetting the mixture and passing it through a 40 μm mesh filter (Funakoshi, Cat. No. HT-AMS-14002); the cell suspension was frozen in CryoStor medium (STEMCELL Technologies, Cat. No. ST07930) with Mr. Frosty (Thermo Scientific, Cat. No. 5100–0001) at −80°C overnight, according to Milani et al., 2016. An ATAC-seq library was prepared as described (Buenrostro et al., 2013) with some minor modifications. For library preparation, stored cells were thawed in a 38°C water bath and centrifuged at 500 g for 5 min at 4°C, which was followed by a wash using 50 μl of cold PBS and a second centrifugation at 500 g for 5 min at 4°C. Ten thousand cells per sample were collected, without distinguishing dead cells, and were lysed using 50 μl of cold lysis buffer (10 mM Tris-HCl, pH 7.4; 10 mM NaCl; 3 mM MgCl2; and 0.1% IGEPAL CA-630). Immediately after lysis, cells were spun at 1000 g for 10 min at 4°C, and the supernatant was discarded. For the transposition reaction, cells were re-suspended in the transposase reaction mix (25 μl 2× TD buffer, 2.5 μl Tn5 transposase [in the Nextera DNA Sample Preparation Kit, Illumina, Cat. No. FC-121–1031], and 22.5 μl nuclease-free water) and incubated for 30 min at 37°C. The reaction mix was purified using DNA Clean and Concentrator-5 (Zymo Research, Cat. No. D4014) by adding 350 μl of DNA-binding buffer and eluting in a volume of 10 μl. After a five-cycle pre-PCR amplification, the optimal number of PCR cycles was determined by a preliminary PCR using KAPA HiFi HotStart Real-Time Library Amplification Kit and was estimated to be four cycles. The PCR products were purified using 1.8× volumes of Agencourt AMPure XP. As a control, 50 ng of mouse genomic DNA was also transposed following the standard procedure of the Nextera DNA Sample Preparation Kit. Sequencing with HiSeq X was outsourced to Macrogen, Inc, which was carried out with HiSeq Control Software 3.3.76 (Run type: PE151bp). The output was processed with Illumina RTA 2.7.6 for base-calling and with bcl2fastq 2.15.0 for de-multiplexing. Quality control of the obtained fastq files for individual libraries was performed with FASTQC v0.11.5. ATAC-seq was performed with three biological replicates for each stage.

### ATAC-seq data analysis

The short-read data from ATAC-seq were trimmed and filtered with Trim-Galore! (v0.5.0; options: --paired --phred33 -e 0.1 -q 30). We also removed reads that originated from mitochondrial genome contamination by mapping reads to the mouse mitochondrial genome using bowtie2 v2.3.4.1 (Langmead and Salzberg, 2012). The rest of the reads were mapped onto the mouse genome (mm10) using bwa v0.7.17 with the ‘mem’ option (Li and Durbin, 2010). Among the mapped reads, we removed reads with length >320 bp to reduce noise. The rest of the reads were further down-sampled to around 83.2 million reads to equalize the sequence depth of every sample. Peak calls were done with MACS2 v2.1.1 (Zhang et al., 2008; options: --nomodel --shift −100 --extsize 200 f BAMPE -g mm -B -q 0.01; the genomic reads were used as a control for all samples). For FRiP score calculation, a module, ‘countReadsPerBin.CountReadsPerBin’ in deepTools v3.2.1 (Ramírez et al., 2016), was used to count reads in peaks, and these read counts were then divided by the total number of reads. To evaluate reproducibility among the replicates, we first divided the mouse genome into 500 bp bins. Then, the ATAC-seq peaks were re-distributed into these bins with bedtools (Quinlan and Hall, 2010; options: intersect -F 0.4 f 0.4 -e -wo). Peaks of >500 bp were subdivided into 500-bp-long regions, and those of <500 bp were extended to fit within the closest 500 bp window. Subsequently, these peaks were converted into one-hot vectors, in which ‘1’ means that a 500-bp-long genomic region harbors an ATAC-seq peak. Genomic regions that lacked ATAC-seq peaks in all data were omitted. Using these one-hot vectors, Euclidean distances between the ATAC-seq data were calculated (Figure 5—figure supplement 1A).

For the conservation analysis, the significant variation in the length of ATAC-seq peaks complicated this evaluation. To deal with such variation, we the ATAC-seq peaks were re-distributed into 100 bp bins with bedtools (Quinlan and Hall, 2010; options: intersect -F 0.4 f 0.4 -e -wo) as described above. The sequences in these peaks were retrieved with BLASTN v2.7.1 against the genomes of 16 vertebrate species listed in Supplementary file 10 (BLASTN options: -task dc-megablast -max_target_seqs 1). The blast hits that scored ≥40 were considered as conserved sequences. In this way, the final figures shown in Figure 5C represent the fraction of the total conserved sequence length in the peaks of each stage rather than the number of conserved peaks. For confirmation, we also used a different alignment algorithm, LAST v961 (Kiełbasa et al., 2011) to find conserved sequences. To generate mouse genome databases for LAST, we first masked repeat sequences with N and split the genome file into multiple files, each of which contained a single chromosome sequence. Then, databases were generated using lastdb (options: -cR01). Alignments with the bamboo shark genome (Cpunctatum_v1.0; https://transcriptome.riken.jp/squalomix/resources/01.GCA_003427335.1_Cpunctatum_v1.0_genomic.rn.fna.gz) and the alligator genome (ASM28112v3) were carried out by lastal (options: -a1 -m100). Only a unique best alignment was selected using last-split. These alignment results were converted into the bed format, and regions that overlapped with the ATAC-seq peaks that were subdivided into 100 bp bins were counted.

For the clustering analysis, we converted the alignment files of the ATAC-seq reads into mapped reads in bins per million (BPM) coverage values with 200 bp resolution using bamCoverage in deepTools v3.2.1 (Ramírez et al., 2016; options: -of bedgraph --normalizeUsing BPM --effectiveGenomeSize 2652783500 -e -bs 200). Then, BPMs at the summits of ATAC-seq peaks and an additional 600 bp to the left and to the right of each summit (1400 bp in total) were collected and clustered by t-SNE (https://github.com/DmitryUlyanov/Multicore-TSNE; hyper parameters: perplexity = 30.0, n_iter = 5000) followed by hierarchical clustering (hyper parameters: method = ‘ward’, metric = ‘euclidean’). Enriched motifs were detected using a Perl script, findMotifsGenome.pl in HOMER v4.10.4 (Heinz et al., 2010; options: -size 100 -mask). To count the number of motif occurrences, ‘-find’ option of findMotifsGenome.pl was used, and sequences that scored ≥75% of the highest motif score were counted. For GO analysis, annotatePeaks.pl in HOMER was used. For the tissue-specificity analysis, we downloaded several aligned and unaligned reads of ATAC-seq experiments on 25 different tissues from the ENCODE web site (https://www.encodeproject.org/; see Supplementary file 10 for a complete list), and peaks were called as described above. Then, peaks that did not overlap with other tissues/cells were detected using bedtools.

### Data and materials availability

RNA-seq and ATAC-seq data sets generated during the current study are available in the Gene Expression Omnibus (GEO) repository under accession number GSE136445. Other sequence data and raw data are available in the figshare (DOI: 10.6084/m9.figshare.9928541). Code for clustering analysis is available at https://github.com/koonimaru/easy_heatmapper. Materials related to this paper are available upon request from the corresponding authors.
