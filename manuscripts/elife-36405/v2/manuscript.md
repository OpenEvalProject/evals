# Quantification of gene expression patterns to reveal the origins of abnormal morphogenesis

## Authors

- Neus Martínez-Abadías<sup>1</sup> ([ORCID: 0000-0003-3061-2123](https://orcid.org/0000-0003-3061-2123)) †
- Roger Mateu Estivill<sup>4</sup> ([ORCID: 0000-0003-4728-2239](https://orcid.org/0000-0003-4728-2239))
- Jaume Sastre Tomas<sup>5</sup> ([ORCID: 0000-0001-9053-2390](https://orcid.org/0000-0001-9053-2390))
- Susan Motch Perrine<sup>6</sup>
- Melissa Yoon<sup>6</sup>
- Alexandre Robert-Moreno<sup>1</sup> ([ORCID: 0000-0001-9042-1316](https://orcid.org/0000-0001-9042-1316))
- Jim Swoger<sup>1</sup> ([ORCID: 0000-0003-3805-0073](https://orcid.org/0000-0003-3805-0073))
- Lucia Russo<sup>1</sup>
- Kazuhiko Kawasaki<sup>6</sup>
- Joan Richtsmeier<sup>6</sup>
- James Sharpe<sup>1</sup> ([ORCID: 0000-0002-1434-9743](https://orcid.org/0000-0002-1434-9743)) †

### Affiliations

1. Centre for Genomic Regulation The Barcelona Institute for Science and Technology Barcelona Spain
2. Universitat Pompeu Fabra Barcelona Spain
3. EMBL Barcelona European Molecular Biology Laboratory Barcelona Spain
4. Universitat de Barcelona Barcelona Spain
5. Universitat de les Illes Balears (UIB) Palma de Mallorca Spain
6. Pennsylvania State University Pennsylvania United States
7. Institució Catalana de Recerca i Estudis Avançats Barcelona Spain

† Corresponding author

## Abstract

The earliest developmental origins of dysmorphologies are poorly understood in many congenital diseases. They often remain elusive because the first signs of genetic misregulation may initiate as subtle changes in gene expression, which are hard to detect and can be obscured later in development by secondary effects. Here, we develop a method to trace back the origins of phenotypic abnormalities by accurately quantifying the 3D spatial distribution of gene expression domains in developing organs. By applying Geometric Morphometrics to 3D gene expression data obtained by Optical Projection Tomography, we determined that our approach is sensitive enough to find regulatory abnormalities that have never been detected previously. We identified subtle but significant differences in the gene expression of a downstream target of a Fgfr2 mutation associated with Apert syndrome, demonstrating that these mouse models can further our understanding of limb defects in the human condition. Our method can be applied to different organ systems and models to investigate the etiology of malformations.

## Introduction

Morphogenesis is guided by dynamic spatio-temporal regulation of gene expression patterns (Chan et al., 2017; Andrey and Mundlos, 2017), the zones within tissues where genes are expressed during specific periods in development. Critical changes in the space, time or intensity of gene expression patterns can result in organ malformation, with reduced or even loss of function. These errors of morphogenesis, which occur in approximately 3% of live births (Toxicology NRC C on D, 2000), are induced by environmental and/or genetic insults that alter the normal process of development. The common approach to revealing the origin of these alterations is to look for phenotypic abnormalities in animal models and to visually assess the overall patterns of gene expression. This qualitative approach has not, however, been able to identify the earliest signs of dysmorphogenesis in many diseases because the first changes in the gene expression patterns may be subtle, limited in time, and later abnormalities may obscure the original genetic cause. To reveal the primary etiology of congenital malformations, more rigorous methods are needed to quantify the three-dimensional (3D) phenotypes of gene expression patterns. A useful tool for tracing back development should be able to perform a quantitative statistical comparison of normal and disease-altered embryogenesis and to detect the earliest signs of genetic misregulation leading to organ malformation.

The shape of developing organs is regulated by gene activity in space and time (Andrey and Mundlos, 2017). Cascades of gene regulatory networks provide the detailed instructions necessary to organize cell behavior and to orchestrate tissue growth and differentiation. Gene expression patterns can be readily mapped within tissues in a true 3D framework combining whole-mount-in-situ hybridization (WMISH) (Rosen and Beddington, 1993) with Optical Projection tomography (OPT) (Sharpe et al., 2002). WMISH is a standard molecular technique for detecting the expression of a specific gene using a labeled complementary RNA probe (de la Pompa et al., 1997; Correia and Conlon, 2001), and OPT is a mesoscopic imaging procedure that can produce high-resolution 3D reconstructions of whole developing embryos processed by WMISH (Sharpe, 2003; Boot et al., 2008). These technologies represented breakthroughs in developmental biology and have provided invaluable qualitative insights into gene function and development (Sharpe, 2003). However, methods for quantifying the 3D distributions of gene expression in a systematic, objective manner are still lacking.

Expanding the potential of OPT from qualitative to quantitative analysis of gene expression patterns is challenging. Gene expression is characterized by highly dynamic patterns, with fast rates of change and fuzzy boundaries that usually do not correspond to well-defined anatomical structures but rather to tissue regions where cells have dynamically up- and downregulated genes. Gene expression patterns have rarely been quantified (Jernvall et al., 2000; Airey et al., 2006; Salazar-Ciudad and Jernvall, 2010; Mayer et al., 2014; Hu et al., 2015; Xu et al., 2015; Martínez-Abadías et al., 2016). We propose to quantify the shape of developing organs in association with their underlying gene expression patterns by applying Geometric Morphometrics (GM), a set of statistical tools for measuring and comparing shapes with increased precision and efficiency (James Rohlf and Marcus, 1993; Klingenberg, 2002; Klingenberg, 2010; Adams et al., 2013; Hallgrimsson et al., 2015). Previous attempts had analyzed the phenotypic and gene expression patterns of variation independently (Jernvall et al., 2000), using different morphometric methods (Hu et al., 2015; Xu et al., 2015) or were restricted to two-dimensional analyses (Martínez-Abadías et al., 2016). Therefore, the current study is the first to combine OPT and GM to characterize the shape of gene expression patterns quantitatively in 3D and to associate these changes to phenotypic changes. Thus, this approach provides the ability to replace qualitative observations with the quantification of subtle yet significant biological differences that underlie the processes through which morphogenesis is altered by disease.

Here, we illustrate how our method can reveal the genetic origin of developmental defects by investigating limb malformations in Apert syndrome [OMIM 101200]. Apert syndrome is a rare congenital disease, with a disease prevalence of 15–16 per million live births, that is characterized by cranial, neural, limb, and visceral malformations (Cohen and MacLean, 2000). Over 99% of Apert cases are associated with one of two missense mutations, S252W or P253R, in the Fibroblast Growth Factor Receptor 2 (FGFR2) (Wilkie et al., 1995; Park et al., 1995). The mutations occur on neighboring amino acids on the linker region between the second and third extracellular immunoglobulin domains of FGFR2, and alter the ligand-binding specificity of the receptors (Yu et al., 2000; Yu and Ornitz, 2001). Thus, the FGF receptors are activated inappropriately, altering the entire FGF/FGFR signaling pathway and causing dysmorphologies of different organs and systems (McIntosh et al., 2000). Apert syndrome shares craniofacial dysmorphologies with other craniosynostosis syndromes but is differentiated on the basis of limb defects of the fore- and hindlimb digits. The craniofacial dysmorphology of Apert syndrome (i.e. premature closure of cranial sutures and patent anterior fontanelle associated with atypical head shape, midfacial retrusion and palatal defects) (Cohen and MacLean, 2000) has been intensively investigated, especially because mouse models show cranial phenotypes that correspond with the human condition (Holmes et al., 2009; Martínez-Abadías et al., 2010; Holmes and Basilico, 2012; Hill et al., 2013; Heuzé et al., 2014). The associated limb defects are less well studied, however, in part because mouse models for Apert syndrome present only subtle limb anomalies (Chen et al., 2003; Wang et al., 2005; Wang et al., 2010), even in mice carrying the P253R mutation (Wang et al., 2010) which is associated with the more severe limb malformations in Apert syndrome (Slaney et al., 1996; von Gernet et al., 2000).

Here, we present precise phenotyping of the limbs of newborn and embryonic specimens of the Fgfr2+/P253R Apert syndrome mouse model, and reveal significant differences that can be traced to as early as one day after the initiation of limb development. To explore the molecular basis of these initial signs of limb dysmorphology, we applied our method combining OPT and GM to assess the expression pattern of a downstream target of Fgf signaling, Dusp6. We chose to assess Dusp6 because it is well-documented as a direct target of Fgf signaling (Kawakami et al., 2003; Li et al., 2007; Ekerot et al., 2008), and because, in addition to being a relevant gene for limb morphogenesis, it is also important for facial, brain and heart development (Kawakami et al., 2003; Li et al., 2007; Maillet et al., 2008). Therefore, Dusp6 was an ideal candidate for our proof-of-concept study. Our quantitative analyses demonstrate that the Apert syndrome Fgfr2 P253R mutation induces changes in the expression pattern of Dusp6 and that these genetic changes are associated with significant phenotypic alterations. These results provide insight into the origins of limb malformations in Apert syndrome.

## Results

### Apert syndrome mice present limb malformations at birth

Previous studies have reported that most Apert syndrome mice do not show obvious abnormalities of the limbs (Chen et al., 2003), and thus focused their molecular analyses on the skull (Wang et al., 2010). Histopathological analyses in Apert syndrome mice revealed overall limb shortening resulting from abnormal osteogenic differentiation, but no signs of limb disproportion or syndactyly (Wang et al., 2005; Wang et al., 2010). Syndactyly has only been reported in three specimens of an outbred knock-in Fgfr2+/P253R model (Yin et al., 2008), but no experimental analyses were performed to further explain why the FGFR2 mutation did not affect limb development in all the specimens within the sample.

As a further test of whether or not the Fgfr2 P253R mutation affects limb development in mice, we first performed an extensive quantitative analysis of the size and shape of individual forelimb bones using data from high resolution microCT images of newborn (P0) mutant and unaffected littermates (Figure 1A–F). Our results revealed many more significant differences between P0 unaffected and Fgfr2+/P253R mutant littermates than previously reported. We found that the humerus, radius and ulna were statistically significantly shorter in length but had increased bone volumes in Fgfr2+/P253R mutant mice in comparison to unaffected littermates (Table 1 and Figure 1G). More localized size differences were detected in the bones derived from the autopod that give rise to the hands. The distal phalanx of digit I, the proximal phalanx of digit V, and metacarpals II, III and IV were significantly longer in Fgfr2+/P253R mutant mice (Table 1 and Figure 1G). In contrast, the proximal phalanx of digit III was shorter and lower in bone volume in Fgfr2+/P253R Apert syndrome mice relative to unaffected littermates (Table 1 and Figure 1G). The scapula and the clavicle, the bones that form the shoulder girdle, were also significantly affected: the scapula was longer, the clavicle was shorter and both bones showed increased bone volumes in Fgfr2+/P253R Apert syndrome mice (Table 1 and Figure 1G) compared to unaffected littermates.

![Figure 1.](https://cdn.elifesciences.org/articles/36405/elife-36405-fig1-v2.jpg)

**Figure 1.:** (A) Mouse skeleton at P0. 3D isosurface reconstruction of the skeleton of an unaffected littermate obtained from a high-resolution µCT scan. (B–F) Anatomical landmarks recorded on microCT scans of Apert syndrome mice at P0. (B) Autopod (hand). Landmarks were recorded at the midpoint of the proximal and distal tips of the distal, mid and proximal phalanges (P1–P28) and the metacarpals (P29–P38). Proximal phalanx I, middle phalanx V, and metacarpal I are not displayed because these bones have not yet mineralized at P0 and could not be visualized in many specimens. (C) Zeugopod. Landmarks were recorded at the midpoint of the proximal and distal tips of the radius (R1–R2) and ulna (U1–U2). (D) Stylopod. Landmarks were recorded at the midpoint of the proximal and distal tips of the humerus (H1–H2), as well as at the tip of the deltoid process (H3) (Figure 1—source data 1). (E) Scapula. Landmarks were recorded at the most superior and inferior lateral points of the scapula (S1–S2), the most posterior point of the spine (S3), the most antero-medial point of the acromion process (S4) and the medial, superior and inferior points of the glenoid cavity (S5–S7) (Figure 1—source data 2). (F) Clavicle. Landmarks were recorded at the medial point of the sternal and the acromial ends (C1–C2). (G) Length and volume differences in the forelimbs of Apert syndrome mouse models. Schematic representation of the forelimb of a P0 mouse showing, in different colors, statistically significant differences in bone length and volume (as measured by two-tailed one-way ANOVA or Mann-Whitney U-test) in Fgfr2+/P253R mice and unaffected littermates, as specified in Table 1. Longer/shorter refers to length, whereas larger/smaller refers to volume. (H, I) Shape differences in the forelimbs of Apert syndrome mouse models. Scatterplots of PC1 and PC2 scores based on Procrustes analysis of anatomical landmark locations representing the shape of the left humerus (H) and the left scapula (I) of unaffected (N = 10) and mutant (N = 12) littermates of Apert syndrome mouse models (Figure 1—source data 1 and Figure 1—source data 2). Convex hulls represent the range of variation within each group of mice.

**Table 1.**
 Quantitative comparison of mean bone lengths and volumes.Means were computed as the average lengths or volumes of the right and the left bones for Fgfr2+/P253R mutant (N = 12) and Fgfr2+/+ unaffected (N = 10) mice. Data for proximal phalanx I, middle phalanx V, and metacarpal I are not listed because these bones were not present in all of the specimens, as they may not yet be developed at P0. Statistically significant differences as determined by two-tailed one-way ANOVA or Mann-Whitney U-tests are marked with * (P-value<0.05). Statistically significant differences after Bonferroni correction are indicated with **.


<table>
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th colspan="2">Mean bone length (mm ± SD)</th>
      <th></th>
      <th colspan="2">Mean bone volume (mm3 ± SD)</th>
      <th></th>
    </tr>
    <tr>
      <th></th>
      <th>Bone</th>
      <th>Fgfr2+/+</th>
      <th>Fgfr2+/P253R</th>
      <th>P-value</th>
      <th>Fgfr2+/+</th>
      <th>Fgfr2+/P253R</th>
      <th>P-value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="16">Autopod</td>
      <td>Distal phalanx I</td>
      <td>0.11 ± 0.03</td>
      <td>0.13 ± 0.02</td>
      <td>0.004**</td>
      <td>0.0015 ± 0.0008</td>
      <td>0.0015 ± 0.0008</td>
      <td>0.86</td>
    </tr>
    <tr>
      <td>Distal phalanx II</td>
      <td>0.22 ± 0.03</td>
      <td>0.21 ± 0.03</td>
      <td>0.128</td>
      <td>0.0021 ± 0.0007</td>
      <td>0.0022 ± 0.0008</td>
      <td>0.659</td>
    </tr>
    <tr>
      <td>Middle phalanx II</td>
      <td>0.004 ± 0.003</td>
      <td>0.01 ± 0.004</td>
      <td>0.336</td>
      <td>0.00002 ± 0.00002</td>
      <td>0.00003 ± 0.00002</td>
      <td>0.759</td>
    </tr>
    <tr>
      <td>Proximal phalanx II</td>
      <td>0.15 ± 0.01</td>
      <td>0.14 ± 0.01</td>
      <td>0.057</td>
      <td>0.0054 ± 0.0011</td>
      <td>0.0053 ± 0.0014</td>
      <td>0.82</td>
    </tr>
    <tr>
      <td>Distal phalanx III</td>
      <td>0.26 ± 0.006</td>
      <td>0.24 ± 0.01</td>
      <td>0.068</td>
      <td>0.0034 ± 0.0008</td>
      <td>0.0033 ± 0.0017</td>
      <td>0.796</td>
    </tr>
    <tr>
      <td>Middle phalanx III</td>
      <td>0.10 ± 0.006</td>
      <td>0.10 ± 0.006</td>
      <td>0.243</td>
      <td>0.0019 ± 0.0009</td>
      <td>0.0022 ± 0.0013</td>
      <td>0.436</td>
    </tr>
    <tr>
      <td>Proximal phalanx III</td>
      <td>0.204 ± 0.02</td>
      <td>0.18 ± 0.03</td>
      <td>0.001**</td>
      <td>0.0087 ± 0.0003</td>
      <td>0.0073 ± 0.0004</td>
      <td>0.016*</td>
    </tr>
    <tr>
      <td>Distal phalanx IV</td>
      <td>0.24 ± 0.006</td>
      <td>0.19 ± 0.02</td>
      <td>0.061</td>
      <td>0.0024 ± 0.0009</td>
      <td>0.0024 ± 0.0014</td>
      <td>0.923</td>
    </tr>
    <tr>
      <td>Middle phalanx IV</td>
      <td>0.06 ± 0.009</td>
      <td>0.07 ± 0.01</td>
      <td>0.338</td>
      <td>0.0009 ± 0.0002</td>
      <td>0.0014 ± 0.0002</td>
      <td>0.24</td>
    </tr>
    <tr>
      <td>Proximal phalanx IV</td>
      <td>0.20 ± 0.01</td>
      <td>0.20 ± 0.02</td>
      <td>0.412</td>
      <td>0.0080 ± 0.0016</td>
      <td>0.0075 ± 0.0021</td>
      <td>0.358</td>
    </tr>
    <tr>
      <td>Distal phalanx V</td>
      <td>0.09 ± 0.01</td>
      <td>0.08 ± 0.01</td>
      <td>0.832</td>
      <td>0.0005 ± 0.00007</td>
      <td>0.0006 ± 0.0001</td>
      <td>0.769</td>
    </tr>
    <tr>
      <td>Proximal phalanx V</td>
      <td>0.14 ± 0.01</td>
      <td>0.15 ± 0.02</td>
      <td>0.027*</td>
      <td>0.0031 ± 0.0007</td>
      <td>0.0036 ± 0.0012</td>
      <td>0.089</td>
    </tr>
    <tr>
      <td>Metacarpal II</td>
      <td>0.39 ± 0.02</td>
      <td>0.41 ± 0.02</td>
      <td>0.034*</td>
      <td>0.0270 ± 0.0028</td>
      <td>0.0265 ± 0.0034</td>
      <td>0.586</td>
    </tr>
    <tr>
      <td>Metacarpal III</td>
      <td>0.49 ± 0.03</td>
      <td>0.52 ± 0.03</td>
      <td>0.004*</td>
      <td>0.0398 ± 0.0043</td>
      <td>0.0382 ± 0.0062</td>
      <td>0.342</td>
    </tr>
    <tr>
      <td>Metacarpal IV</td>
      <td>0.43 ± 0.02</td>
      <td>0.45 ± 0.03</td>
      <td>0.011*</td>
      <td>0.0312 ± 0.0033</td>
      <td>0.0291 ± 0.0048</td>
      <td>0.114</td>
    </tr>
    <tr>
      <td>Metacarpal V</td>
      <td>0.22 ± 0.01</td>
      <td>0.22 ± 0.02</td>
      <td>0.571</td>
      <td>0.0120 ± 0.0019</td>
      <td>0.0124 ± 0.0023</td>
      <td>0.458</td>
    </tr>
    <tr>
      <td rowspan="2">Zeugopod</td>
      <td>Radius</td>
      <td>2.29 ± 0.02</td>
      <td>2.22 ± 0.01</td>
      <td>0.003*</td>
      <td>0.3187 ± 0.0292</td>
      <td>0.3558 ± 0.0334</td>
      <td>0.001**</td>
    </tr>
    <tr>
      <td>Ulna</td>
      <td>2.76 ± 0.08</td>
      <td>2.64 ± 0.07</td>
      <td>0.000**</td>
      <td>0.4999 ± 0.0417</td>
      <td>0.5366 ± 0.0766</td>
      <td>0.010*</td>
    </tr>
    <tr>
      <td>Stylopod</td>
      <td>Humerus</td>
      <td>1.65 ± 0.01</td>
      <td>1.62 ± 0.007</td>
      <td>0.007*</td>
      <td>0.9950 ± 0.0764</td>
      <td>1.1444 ± 0.0649</td>
      <td>0.001**</td>
    </tr>
    <tr>
      <td rowspan="2">Not derived from limb bud</td>
      <td>Scapula</td>
      <td>2.69 ± 0.08</td>
      <td>2.75 ± 0.06</td>
      <td>0.013*</td>
      <td>1.0757 ± 0.0733</td>
      <td>1.2184 ± 0.0777</td>
      <td>0.001**</td>
    </tr>
    <tr>
      <td>Clavicle</td>
      <td>2.47 ± 0.06</td>
      <td>2.34 ± 0.09</td>
      <td>0.001**</td>
      <td>0.2214 ± 0.0147</td>
      <td>0.2811 ± 0.0232</td>
      <td>0.001**</td>
    </tr>
  </tbody>
</table>

The Principal Components Analysis (PCA) based on the shape of the humerus did not show marked shape differences between unaffected and Fgfr2+/P253R Apert syndrome mice (Figure 1H). However, the PCA of the scapula indicated a clear morphological differentiation between these two groups (Figure 1I). The scapula of Fgfr2+/P253R Apert syndrome mice presented a more robust phenotype, with wider and longer scapulae, in comparison to that of their unaffected littermates.

Overall, these size and shape differences demonstrate that Fgfr2+/P253R Apert syndrome mice present widespread and significant limb dysmorphologies at P0 that were not previously reported and would not have been revealed without microCT scanning and quantitative statistical testing. Some defects, such as shoulder anomalies and short humeri, have a direct correspondence with the human phenotype (Park et al., 1995). In newborn mice, however, we did not detect any clear sign of syndactyly, which is the most prominent limb defect in people with Apert syndrome (Cohen and Kreiborg, 1995; Holten et al., 1997). As the forelimb of mice is not yet completely ossified at P0 and because Fgfr2+/P253R mutant littermates die shortly after birth, we could not assess whether other limb abnormalities might appear later in development.

### A quantitative morphometric method to assess embryonic gene expression patterns

To determine the earliest developmental basis of the limb anomalies quantified in newborn mice, we developed a quantitative method to explore early embryonic limb development. First, to visualize the expression pattern of a downstream target of Fgfr2, we obtained OPT scans of Fgfr2+/P253R Apert syndrome mouse embryos that had been analyzed with WMISH to reveal Dusp6 expression (Figure 2). Qualitative assessment of the 3D reconstructions showed that Dusp6 was widely expressed throughout the embryo from embryonic day (E)10.5 to E11.5, with highest intensity in the limbs, the head and the somites (Figure 2). Dusp6 was also expressed in the heart with moderate intensity. By comparing the distribution of the Dusp6 gene expression pattern visually, it was possible to distinguish between embryos at the E10.5 and the E11.5 stages of development. At E10.5, Dusp6 was prominently expressed in the facial prominences and in the forming somites along most of the craniocaudal segment, whereas at E11.5, the expression of Dusp6 was more widespread in the brain and restricted to the caudal somites. Focusing on the limbs, the expression of Dusp6 at the two different stages was also readily distinguishable, with Dusp6 expression domains thinning into a more extended domain along the limb outline as the limb buds grow from E10.5 to E11.5 (Figure 2). The limb bud expression patterns of Fgfr2+/P253R mutant and unaffected littermates were not distinguishable because of the large amount of developmental variation within litters (Figure 2).

![Figure 2.](https://cdn.elifesciences.org/articles/36405/elife-36405-fig2-v2.jpg)

**Figure 2.:** OPT scans of embryos WMISH stained for Dusp6 revealed the anatomical location of Dusp6 gene expression (shown in yellow). For each stage, the main expression domains are highlighted on the left for anatomical reference on a lateral view of a 3D reconstruction of a Fgfr2+/+ unaffected embryo (fb, forebrain; fl, forelimb; hb, hindbrain; hl, hindlimb; ht, heart; is, isthmus; lnp, lateral nasal process; md, mandibular prominence; mnp, medial nasal process; mx, maxillary prominence; so, somites). On the right, 3D reconstructions of three unaffected and three Fgfr2+/P253R mutant embryos from the same litter are displayed to represent the high degree of variation in developmental age within litters. Embryos are not to scale. Original 2D images of the Dusp6 WMISH experiments are available in Figure 2—source data 1.

Quantitative testing was thus required to allow the more accurate evaluation of limb alterations that are potentially associated with Apert syndrome but visually undetectable. We developed a method for 3D shape analysis of the limb and the associated gene expression pattern of Dusp6 (Figure 3). This protocol enabled us to determine differences in limb size and shape between genotype groups and to assess whether these phenotypic differences are associated with altered gene expression patterns (Figure 3). Our approach uses GM methods to measure directly the limb anatomy and gene expression domains segmented from the 3D reconstructions of the embryo OPT scans. As expression of Dusp6 showed a fuzzy spatial gradient, multiple thresholding was used to define a consistently high gene expression pattern (Figure 3, steps from 1 to 5). After manual and semiautomatic recording of the 3D coordinates of landmarks on the surfaces of the limb and the gene expression domains blinded to group allocation (Figure 3, step 6; Video 1), multivariate statistical analyses were performed to explore shape and size variation and covariation patterns for the limb morphology and the Dusp6 domain (Figure 3, steps 7 and 8).

![Figure 3.](https://cdn.elifesciences.org/articles/36405/elife-36405-fig3-v2.jpg)

**Figure 3.:** Mouse embryos between E10.5 and E11.5 were analyzed with WMISH to reveal the expression of Dusp6 (1), and then cleared with BABB, and OPT scanned using both fluorescence and transmission light (2). The external surface of the embryo was obtained from the 3D reconstruction of the fluorescence scan (2). Multiple thresholding of the transmission scan by choosing different levels of grey values as shown by the histogram allowed the visualization of gene expression patterns at different intensities (3). Moderate gene expression (shown in green) was displayed as the isosurface obtained using a threshold of the grey value computed as 2/3 of the last grey value showing the Dusp6 expression domain (3). High gene expression (shown in yellow) was displayed as the isosurface obtained using a threshold of the grey value computed as 1/3 of the last grey value showing the Dusp6 expression domain (3). From the whole mouse embryo isosurfaces, all four limb buds were segmented (5A). From the high gene expression isosurface, the Dusp6 domains from all of the available limbs were segmented (5B). Maximum curvature patterns were displayed to optimize landmark recording (5). For each limb, we captured the shape and size of the limb bud (6A) and the underlying high Dusp6 gene expression pattern (6B), recording the 3D coordinates of anatomical landmarks (yellow dots), curve semi-landmarks (red dots) and surface semi-landmarks (pink dots). Anatomical and curve landmarks were recorded manually on each limb. Surface landmarks were recorded on one template limb and interpolated onto target limbs (Video 1). Landmark coordinates were the input for Geometric Morphometric (GM) quantitative shape analysis (7, 8) that was used to superimpose the landmark data (GPA, Generalized Procrustes Analysis), to compute limb size (centroid size), and to explore both shape variation within limbs and gene expression domains within litters by Principal Component Analysis (PCA). Finally, the covariation patterns for the shape of the limb and the shape of the gene expression domain were also explored using the Partial Least Squares (PLS) method.

![Video 1.](https://cdn.elifesciences.org/articles/36405/elife-36405-video1.mp4.jpg)

**Video 1.:** In this video, we show a superimposed view of a fluorescent and a transmission OPT scan of the same E11.5 mouse embryo, which was analyzed with WMISH to reveal the gene expression of Dusp6, a downstream target of Fgf signaling. The surface of the mouse embryo rotating around its central axis was obtained from the 3D reconstruction of an OPT scan based on fluorescence light. The expression pattern of the Dusp6 gene was segmented from the transmission OPT scan using multiple thresholding. The imaging revealed the anatomical location of regions of high Dusp6 gene expression (shown in purple). To compare unaffected and Fgfr2+/P253R mouse embryos and to detect statistically significant differences between them, we collected landmarks along the surface of the gene expression domain (yellow dots) and the limb bud (green dots), which capture the size and shape of the limb and the underlying gene expression domain to a highly accurate level of detail. Further quantitative analyses provided insight into the origins of limb malformations in Apert syndrome.

### The first signs of limb dysmorphology in Apert syndrome

As gene expression patterns are highly dynamic and rapidly change in size, shape and position within a few hours as development progresses (Martínez-Abadías et al., 2016), individual limb buds from Fgfr2+/P253R mutant embryos and their unaffected littermates aged between E10.5 and E11.5 were staged using a fine-resolution staging system (https://limbstaging.embl.es) (Musy et al., 2018). The staging results showed that the analyzed limbs represent a temporal continuum throughout development, with no significant differences between the staging of unaffected and mutant littermates of the same litter (Figure 4). We partitioned the time span from E10 to E11.5 into four periods, each one approximately representing 12 hr of development (see Table 2 and 'Materials and methods' for further details on sample composition).

![Figure 4.](https://cdn.elifesciences.org/articles/36405/elife-36405-fig4-v2.jpg)

**Figure 4.:** All of the limbs were individually staged using our publicly available web-based staging system (https://limbstaging.embl.es). The stage of the limb bud was estimated after alignment and shape comparison of the spline with an existing dataset with a reproducibility of ±2 hr. As both Litter 1 and Litter 2 comprised limbs between E10 and E10.5, we pooled these limbs into the 'Early' period. Litter 3, comprising limbs between E10 and E11, represented the 'Mid' developmental period. And finally, Litter 4, which included limbs between E11 and E11.5, was considered as the 'Late' period. In subsequent analyses, forelimbs and hindlimbs were analyzed separately, as specified in Table 2. Increasing color intensities in dots represent an increasing number of limbs with the same staging result. Individual scores are available in Figure 4—source data 1.

**Table 2.**
 Sample composition by genotype and period.Fgfr2+/+: unaffected littermates; Fgfr2+/P253R: Apert syndrome mutant littermates. Developmental periods were defined according to limb staging, as shown in Figure 4. Hindlimbs and forelimbs were analyzed separately because, in the same embryo, hindlimbs are delayed in development in comparison to forelimbs by about 6–8 hr. We thus presented in the main text the results from groupings highlighted in color, including those for the hindlimbs from the early and mid groups, as well as those for the forelimbs from the mid and the late groups. This represents a continuous time span of limb development, from E10 to E11.5, divided into four periods of 12 hr each. Results from the complete dataset that considers hindlimbs and forelimbs from each litter separately are available in Figures 5 and 6 (Figure 5—figure supplement 2, Figure 5—figure supplement 3, Figure 6—figure supplement 1 and Figure 6—figure supplement 2).


<table>
  <thead>
    <tr>
      <th rowspan="2">Genotype</th>
      <th rowspan="2">Period</th>
      <th rowspan="2">N limb</th>
      <th rowspan="2">N gene</th>
      <th colspan="4">LIMB</th>
    </tr>
    <tr>
      <th colspan="2">Hindlimb (N = 34)</th>
      <th colspan="2">Forelimb (N = 46)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td colspan="2">Early (~E10)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>Limb</td>
      <td>Gene</td>
      <td>Limb</td>
      <td>Gene</td>
    </tr>
    <tr>
      <td>Fgfr2+/+</td>
      <td rowspan="3">EARLY: E10-E10.5</td>
      <td>30</td>
      <td>24</td>
      <td>13</td>
      <td>9</td>
      <td>17</td>
      <td>15</td>
    </tr>
    <tr>
      <td>Fgfr2+/P253R</td>
      <td>16</td>
      <td>15</td>
      <td>11</td>
      <td>9</td>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <td>Subtotal</td>
      <td>46</td>
      <td>39</td>
      <td>24</td>
      <td>18</td>
      <td>22</td>
      <td>21</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td colspan="2">Mid early (~E10.5)</td>
      <td colspan="2">Mid late (~E11)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>Limb</td>
      <td>Gene</td>
      <td>Limb</td>
      <td>Gene</td>
    </tr>
    <tr>
      <td>Fgfr2+/+</td>
      <td rowspan="3">MID: E10.5-E11</td>
      <td>15</td>
      <td>10</td>
      <td>7</td>
      <td>3</td>
      <td>8</td>
      <td>7</td>
    </tr>
    <tr>
      <td>Fgfr2+/P253R</td>
      <td>16</td>
      <td>9</td>
      <td>8</td>
      <td>3</td>
      <td>8</td>
      <td>6</td>
    </tr>
    <tr>
      <td>Subtotal</td>
      <td>31</td>
      <td>19</td>
      <td>15</td>
      <td>6</td>
      <td>16</td>
      <td>13</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td colspan="2">Late (~E11.5)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>Limb</td>
      <td>Gene</td>
      <td>Limb</td>
      <td>Gene</td>
    </tr>
    <tr>
      <td>Fgfr2+/+</td>
      <td rowspan="3">LATE: E11-E11.5</td>
      <td>8</td>
      <td>8</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <td>Fgfr2+/P253R</td>
      <td>15</td>
      <td>14</td>
      <td>7</td>
      <td>6</td>
      <td>8</td>
      <td>8</td>
    </tr>
    <tr>
      <td>Subtotal</td>
      <td>23</td>
      <td>22</td>
      <td>11</td>
      <td>10</td>
      <td>12</td>
      <td>12</td>
    </tr>
    <tr>
      <td>Total</td>
      <td></td>
      <td>100</td>
      <td>80</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

We first focused on analyzing limb dysmorphology, aiming to determine the youngest stage at which there were morphological differences between mutant and unaffected limbs. To find the earliest moment when differences arise, we traced limb development backwards in time using Geometric Morphometric methods, starting first with embryos from the oldest period (as the differences would be easier to find) and from there proceeding towards the earlier (younger) periods. In this way, we should be able to identify confidently the initiation of limb dysmorphogenesis associated with the Fgfr2 P253R mutation.

During the 'Late' period, we detected that Fgfr2+/P253R limb buds were already clearly separated from those of their unaffected littermates in the morphospace defined by the Principal Component Analysis (PCA) (Figure 5A, Figure 5—figure supplement 1). Relative to those of their unaffected littermates, the limbs of Fgfr2+/P253R mice presented subtle phenotypic limb differences: limbs were shorter and thicker, with limited development of the wrist (Figure 5A). Quantitative comparison of limb size showed that the limbs of mutant mice were also significantly smaller than those of their unaffected littermates (Table 3 and Figure 6A). Interestingly, in this 'Late' period the limbs of mutant mice were smaller than unaffected littermates (although this was not the case in earlier periods). Overall, these results confirmed that the Fgfr2 P253R Apert syndrome mutation has an effect on limb development, altering both the size and shape of the limbs. These subtle but significant phenotypic differences would most probably have remained undetected by a qualitative approach. Our quantitative approach revealed their statistical significance and pointed to the origin of the Apert syndrome limb malformation prior to E11.5, before the 'Late' period.

![Figure 5.](https://cdn.elifesciences.org/articles/36405/elife-36405-fig5-v2.jpg)

**Figure 5.:** Principal Component Analysis based on the Procrustes-based semi-landmark analysis was used to assess the shape of the limbs and the corresponding Dusp6 expression domains for each developmental period (Figure 5—figure supplement 1). Each period was analyzed separately for the shape of the limb (A–D) and the Dusp6 expression domain (E–H), as specified in the 'Materials and methods' and in Table 2. Scatterplots of PC1 and PC2 axes with the corresponding percentages of total morphological variation explained are displayed for each analysis, along with the morphings associated with the negative, mid and positive values of the PC axis that separates mutant and unaffected littermates (PC1 or PC2, as highlighted in bold black letters in the corresponding axis). Morphings are displayed in grey tones when the analysis showed no differentiation between mutant and unaffected littermates. Morphings are displayed in color when the analysis revealed differentiation between mouse groups (blue: unaffected littermates; pink: mutant littermates). Limb buds and Dusp6 domains are not to scale and are oriented with the distal aspect to the left, the proximal aspect to the right, the anterior aspect at the top and the posterior aspect at the bottom of all images. Convex hulls represent the ranges of variation within each group of mice. Individual scores are available in Figure 5—source data 1. Results from the complete dataset analyzing hindlimbs (Figure 5—figure supplement 2, Figure 5—figure supplement 2—source data 1) and forelimbs (Figure 5—figure supplement 3, Figure 5—figure supplement 3—source data 1) from each litter separately are also available.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/36405/elife-36405-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** In the limb, we manually recorded the 3D coordinates of five anatomical landmarks (A): L1–L2, the most medial points on the anterior and the posterior sides of wrist, collected along the curve that divides the limb on the dorsal and ventral sides; L3, the most distal point of the limb, collected along the curve that divides the limb on the dorsal and ventral sides; and L4–L5, the most superior and inferior points on the dorsal and ventral sides of the limb. We also recorded between 25 and 60 points along the curve that divides the limb on the dorsal and ventral sides to define an outline spline of the limb. Using Viewbox 4, we obtained the 3D coordinates of 19 equidistant points along the outline spline that were considered in further comparative shape analyses to be curve semi-landmarks (LC1–LC19) (B). Finally, we recorded 52 surface semi-landmarks on the dorsal and ventral sides of the limb interpolating the points from a reference limb to each target limb, using the five anatomical landmarks manually recorded as matching points and by minimizing the bending energy (LS1–LS52) (C). In the gene, we manually recorded the 3D coordinates of four anatomical landmarks (D): G1–G2, the points at the most anterior and posterior tips of the gene expression domain; G3-G4, the points at the maximum curvature of the proximal side of the gene expression domain, on the dorsal and the ventral sides (D). (We also recorded 10–30 points along the distal and proximal curves of the gene expression domain at the sagittal plane, and 30–60 points along the outline of the gene expression domain, on its proximal side.) Using Viewbox 4, we obtained the 3D coordinates of eleven equidistant points along the spline of the distal and proximal curves of the gene expression domain (GCd1–GCd11 and GCp1–GCp11) (E and F), and 19 equidistant points along outline of the gene expression domain, on its proximal side (GCo1–GCo19) (G) that were considered in further comparative shape analyses as curve semi-landmarks, and are displayed simultaneously in (H).

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/36405/elife-36405-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** Scatterplots of PC1 and PC2 axes with the corresponding percentage of total morphological variation explained are displayed for each analysis, along with morphings associated with the negative, mid and positive values of the PC axis that separates mutant and unaffected littermates (PC1 or PC2, as highlighted in bold black letters in the corresponding axis). Morphings are displayed in grey tones when the analysis shows no differentiation between unaffected and mutant littermates. Morphings are displayed in color when the analysis reveals differentiation between the mouse groups (blue: unaffected littermates; pink: mutant littermates). Limb buds and Dusp6 domains are not to scale and are oriented distally to the left, proximally to the right, anteriorly to the top and posteriorly to the bottom. Convex hulls represent the ranges of variation within each group of mice, as defined in Table 2 and Figure 4. Individual scores are available in Figure 5—figure supplement 2—source data 1.

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/36405/elife-36405-fig5-figsupp3-v2.jpg)

**Figure 5—figure supplement 3.:** Scatterplots of PC1 and PC2 axes with the corresponding percentage of total morphological variation explained are displayed for each analysis, along with morphings associated with the negative, mid and positive values of the PC axis that separates mutant and unaffected littermates (PC1 or PC2, as highlighted in bold black letters in the corresponding axis). Morphings are displayed in grey tones when the analysis shows no differentiation between unaffected and mutant littermates. Morphings are displayed in color when the analysis reveals differentiation between the mouse groups (blue: unaffected littermates; pink: mutant littermates). Limb buds and Dusp6 domains are not to scale and are oriented distally to the left, proximally to the right, anteriorly to the top and posteriorly to the bottom. Convex hulls represent the ranges of variation within each group of mice, as defined in Table 2 and Figure 4. Individual scores are available in Figure 5—figure supplement 3—source data 1.

![Figure 6.](https://cdn.elifesciences.org/articles/36405/elife-36405-fig6-v2.jpg)

**Figure 6.:** (A–D) Comparison of limb bud size and Dusp6 volume in unaffected and Fgfr2+/P253R mutant littermates across development (Table 3). Limb size was measured as limb centroid size (A), whereas the size of the Dusp6 expression was measured as the volume of the gene domain (B), as specified in the 'Materials and methods' and in Table 2. Statistically significant differences as revealed by two-tailed t-tests are marked with asterisks, representing the degree of significance: *P-value=0.03, **P-value=0.01. Results from hindlimbs and forelimbs are separately available in Figure 6—figure supplement 1. The association between the size of the limbs and the volume of the Dusp6 domain was assessed separately for forelimbs (C) and hindlimbs (D). Individual scores for all of these analyses are available in Figure 6—source data 1. (E) Time course assessing the morphological integration pattern between the limb phenotype and the shape of the gene expression pattern using partial least squares analyses. Associated shape changes from late to early limb development are shown from morphings associated with the negative, mid and positive values of PLS1, which accounted for almost all of the covariation (97.6% in forelimbs and 99.5% in hindlimbs) between the limb buds and the Dusp6 gene expression domains (Figure 6—figure supplement 2). Limb buds and Dusp6 domains are not shown to scale and are oriented distally to the left, proximally to the right, anteriorly to the top and posteriorly to the bottom. On the right, representing the positive extreme of PLS1 axis, typical early limb buds showed a protruding shape (i.e. short in the proximo-distal axis and symmetrical in the antero-posterior axis) associated with a flat-bean shaped Dusp6 expression zone localized in the distal limb region, underlying the apical ectodermal ridge and spreading proximally towards the dorsal and ventral sides of the limb. On the left, representing the negative extreme of the PLS1 axis, limb buds were elongated in the proximal axis and asymmetric on the antero-posterior axis, with an expansion of the distal limb region and a contraction of the proximal region, at the wrist level. This limb shape, which is typical of more developed limbs, was associated with a Dusp6 expression that was extended underneath the apical ectodermal ridge towards the anterior and the posterior ends of the gene expression zone, but reduced on the dorsal and ventral sides of the limb. Individual scores for all of these analyses are available in Figure 6—figure supplement 2—source data 1. Legends for supplementary figures.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/36405/elife-36405-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** Comparison in hindlimbs (A, C) and forelimbs (B, D) at each developmental period, as defined in Table 2 and Figure 4. Limb size was measured in terms of limb centroid size (μm), whereas the size of the Dusp6 expression zone was measured as the volume of the gene expression domain (μm3). Statistical significant differences as revealed by two-tailed t-tests are marked with asterisks: *P-value<0.05. Individual scores are available in Figure 6—source data 1.

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/36405/elife-36405-fig6-figsupp2-v2.jpg)

**Figure 6—figure supplement 2.:** Results display the morphings associated with the negative, mid and positive values of PLS1 for hindlimbs (A) and forelimbs (B), which accounted for more than 95% of the covariation between the limb buds and the Dusp6 gene expression domains. Separate PLS analyses for hindlimbs (C) and forelimbs (D) for each developmental group, as defined in Table 2 and Figure 4, are also shown. Formal testing of differences in the intensity of the integration patterns in unaffected and Fgfr2+/P253R mutant mice at each stage was not possible because of sample size limitations, as specified in 'Materials and methods' and in Table 2. Individual scores are available in Figure 6—figure supplement 2—source data 1. Rich media.

**Table 3.**
 Quantitative comparison of limb size (μm) and Dusp6 volume (μm3) in Fgfr2+/P253R mutant and Fgfr2+/+ unaffected mice.Results from two-sided t-tests are provided separately for forelimbs and hindlimbs and for each developmental group, as defined in Table 2 and Figure 4. Statistically significant differences are marked with * (P-value<0.05).


<table>
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th colspan="5">EARLY</th>
      <th colspan="5">MID</th>
      <th colspan="5">LATE</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th>Fgfr2+/+</th>
      <th>Fgfr2+/P253R</th>
      <th>t</th>
      <th>df</th>
      <th>P-value</th>
      <th>Fgfr2+/+</th>
      <th>Fgfr2+/P253R</th>
      <th>t</th>
      <th>df</th>
      <th>P-value</th>
      <th>Fgfr2+/+</th>
      <th>Fgfr2+/P253R</th>
      <th>t</th>
      <th>df</th>
      <th>P-value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">Forelimb</td>
      <td>Limb size</td>
      <td>2041.63</td>
      <td>2274.15</td>
      <td>6.99</td>
      <td>18.98</td>
      <td>&lt;0.0001</td>
      <td>2728.24</td>
      <td>2579.69</td>
      <td>−1.70</td>
      <td>7.74</td>
      <td>0.13</td>
      <td>3311.66</td>
      <td>3097.72</td>
      <td>−3.57</td>
      <td>5.39</td>
      <td>0.01</td>
    </tr>
    <tr>
      <td>Dusp6 volume</td>
      <td>18160720</td>
      <td>18387239</td>
      <td>0.13</td>
      <td>13.03</td>
      <td>0.89</td>
      <td>23002206</td>
      <td>27432909</td>
      <td>1.78</td>
      <td>9.64</td>
      <td>0.11</td>
      <td>24792568</td>
      <td>29875554</td>
      <td>2.47</td>
      <td>9.72</td>
      <td>0.03</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td colspan="5">EARLY</td>
      <td colspan="5">MID</td>
      <td colspan="5">LATE</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Fgfr2+/+</td>
      <td>Fgfr2+/P253R</td>
      <td>t</td>
      <td>df</td>
      <td>P-value</td>
      <td>Fgfr2+/+</td>
      <td>Fgfr2+/P253R</td>
      <td>t</td>
      <td>df</td>
      <td>P-value</td>
      <td>Fgfr2+/+</td>
      <td>Fgfr2+/P253R</td>
      <td>t</td>
      <td>df</td>
      <td>P-value</td>
    </tr>
    <tr>
      <td rowspan="2">Hindlimb</td>
      <td>Limb size</td>
      <td>2280.36</td>
      <td>2489.62</td>
      <td>2.68</td>
      <td>15.76</td>
      <td>0.02</td>
      <td>2769.51</td>
      <td>2589.95</td>
      <td>−1.74</td>
      <td>3.03</td>
      <td>0.18</td>
      <td>3191.12</td>
      <td>2955.91</td>
      <td>−3.44</td>
      <td>6.73</td>
      <td>0.01</td>
    </tr>
    <tr>
      <td>Dusp6 volume</td>
      <td>16294103</td>
      <td>16277958</td>
      <td>−0.01</td>
      <td>15.36</td>
      <td>0.99</td>
      <td>23920390</td>
      <td>23131303</td>
      <td>−0.19</td>
      <td>2.45</td>
      <td>0.86</td>
      <td>41802827</td>
      <td>45608477</td>
      <td>0.52</td>
      <td>4.14</td>
      <td>0.63</td>
    </tr>
  </tbody>
</table>

During the 'Mid late' period, the limbs of Fgfr2+/P253R mutant mice were still distinguishable from those of unaffected mice in the morphospace of the PCA (Figure 5B). At this period, the limbs of Fgfr2+/P253R mice lacked the antero-posterior asymmetry and the narrowing of the wrist region more typical of unaffected littermates. Instead, Fgfr2+/P253R mice showed a limb phenotype that was elongated in the proximo-distal axis and thickened in the dorso-ventral axis (Figure 5B), resembling the limb shape of younger unaffected embryos. This shape difference coincided with reduced growth in Fgfr2+/P253R mice, as the limbs of Fgfr2+/P253R mice tended to be smaller than unaffected limbs (Table 3 and Figure 6A). Therefore, significant differences between unaffected and mutant limbs could still be detected during the 'Mid late' period of development and the origins of limb defects associated with Apert syndrome should be sought earlier in development.

The first period during which no significant differences could be detected between unaffected and Fgfr2+/P253R Apert syndrome mice was at the 'Mid early' period (Figure 5C). Despite internal variation in limb shape, with Fgfr2+/P253R mice spreading throughout the morphospace and unaffected littermates concentrated on one region, mutant and unaffected littermates completely overlapped. Therefore, limb shape differences could no longer be detected between groups. Limb size differences were not significant either (Table 3 and Figure 6A). Therefore, our results suggest that the critical time point of limb dysmorphogenesis associated with Apert syndrome occurred between the 'Mid late' and 'Mid early' periods, corresponding to the transition period from E10.5 to E11 (Figure 5B–C).

Consistent with the above, no further sign of limb shape dysmorphology was detected during the 'Early' period of development (Figure 5D). During this period, there was a great range of developmental variation, with unaffected and Fgfr2+/P253R mutant mice completely overlapping in the morphospace and with all limbs displaying similar incipient bud shapes (Figure 5D). The limbs of Fgfr2+/P253R mice were significantly larger than the limbs of their unaffected littermates (Table 3 and Figure 6A), suggesting that at this early time point, there is a significant effect of the Fgfr2 P253R mutation on limb size but not on limb shape (Figure 6A).

### Fgfr2 Apert syndrome mutation leads to aberrant overexpression of Dusp6 domains

We next sought to obtain direct evidence of altered genetic regulation that could explain the observed limb phenotype by analyzing the shape dynamics of the expression of Dusp6, a direct target gene of Fgf signaling. As in the limb shape analysis described above, we chose to work backwards in developmental time, first examining the gene expression of Dusp6 in the embryos from the latest period. We found that in the 'Late' period, Dusp6 expression was already different in Fgfr2+/P253R mutant mice and unaffected littermates. The differences were significant both in shape (Figure 5E) and size (Table 3 and Figure 6B). In the limbs of unaffected mice, the Dusp6 expression domain appeared as a thin domain underlying the apical ectodermal ridge, whereas in Fgfr2+/P253R mutant mice, the shape of the Dusp6 domain was expanded in all directions (Figure 5E). Accordingly, the volume of the Dusp6 expression domain was significantly larger in Apert syndrome mice (Table 3 and Figure 6B), even when these mice had significantly smaller limbs (Figure 6A). The Dusp6 expression domain thus grew disproportionately in the limbs of Fgfr2+/P253R mutant mice in the latest period of development (Figure 5E), which is consistent with reports of whole-body size reduction in Fgfr2+/P253R Apert mice and of the over-activation of Fgfr2 signaling by the Apert syndrome mutation (Yu and Ornitz, 2001; Ibrahimi et al., 2001).

During the 'Mid late' period, the shapes of expression patterns were still distinct — the expanded Dusp6 expression domain persisted on the dorsal and ventral sides of mutant limbs, but was reduced on the anterior and posterior sides (Figure 5F). The overall volume of the Dusp6 expression domains remained larger in Fgfr2+/P253R mutant mice, but the difference was no longer statistically significant (Table 3 and Figure 6B).

During the 'Mid early' period, the separation between unaffected and Fgfr2+/P253R mutant mice was maintained in the PCA analysis (Figure 5G). Unaffected mice showed a Dusp6 expression domain that was expanded towards the anterior and posterior edges of the expression domain (Figure 5G). By contrast, Fgfr2+/P253R mutant mice did not show the extension and the posterior asymmetry of the Dusp6 expression domain typical of normal limb development, suggesting a lack of differentiation in the Dusp6 expression of mutant limbs (Figure 5G).

The 'Early' period was the only time point when we did not detect a significant difference between unaffected and Fgfr2+/P253R mice (Figure 5H). The PCA showed variation in the expression domains of Dusp6, with similar gene expression patterns in terms of both shape (Figure 5H) and size (Table 3 and Figure 6B) across all mice. Therefore, the first observation of an alteration in the gene expression pattern (Figure 5G) occurred earlier than the change in the limb shape (Figure 5B). Our analyses provide evidence that differences in the Dusp6 gene expression pattern first occurred during the 'Mid early period', preceding the phenotypic limb differentiation, which occurred a few hours later during the 'Mid late period'. Overall, the time courses showing the dynamics of limb shape and gene expression pattern changes throughout development (Figure 5 and Figure 6) confirmed that the Fgfr2 Apert syndrome mutation causes an aberrant overexpression of Dusp6 early in development, which could later lead to significant limb malformations.

### Altered Dusp6 expression and limb dysmorphology are highly associated

Finally, we explored the patterns of correlation between the limb phenotype and gene expression to further explore how altered Fgf signaling relates to the limb malformations induced by the Apert syndrome Fgfr2 P253R mutation. First, we assessed the relationship between the size of the limbs and the volume of the Dusp6 expression domain, pooling all the forelimbs and hindlimbs and assessing the correlation between these two traits (Figure 6C,D). The trend line showed that for the same limb size, Fgfr2+/P253R mutant mice showed larger Dusp6 expression domains, both in forelimbs (R2 = 0.4) and hindlimbs (R2 = 0.6). If the extension of the Dusp6 expression depended only on limb growth, and the gene domain passively became larger by just following limb tissue growth, a higher correlation between the size of the limb and the gene expression would be expected. However, the moderate correlation found here suggests that the size of the Dusp6 gene expression zone is not solely dependent on limb growth but might be controlled by further genetic regulatory factors.

Second, we assessed the morphological integration between the shape of the limbs and the shape of the Dusp6 expression domain. The statistical analysis of the covariance pattern between these shapes can reflect the interaction of the phenotype and the gene expression pattern during limb development. As shown by analysis of additional genes expressed during limb development (Martínez-Abadías et al., 2016), even when a gene is expressed within the limb, the shape of the limb and the shape of the gene expression domain are not correlated by definition, and the integration pattern can change from a strong association to no significant correlation within few hours as the limb develops (Martínez-Abadías et al., 2016). The dynamics of the integration pattern can identify the key periods during which the expression of a gene is relevant for determining the shape of the limb. If the morphological integration is low, the expression of the gene will not be as relevant for determining the shape of the limb as it would be when the integration is high and the impact of the altered gene expression on the phenotype is minimal. If the morphological integration is high, the impact of the genetic mutation will be maximized (i.e. changes in the gene expression pattern will produce changes in the limb shape). Our results showed that the shape of the limb and the shape of the Dusp6 expression domain were indeed highly correlated (RV = 0.88 in forelimbs; RV = 0.91 in hindlimbs). This is evidence that altered Fgf signaling, induced by the Fgfr2 P253R Apert syndrome mutation, can be associated with limb dysmorphology.

By comparing the morphological integration patterns in mutant and unaffected littermates during different periods, we can test whether this interaction is maintained or disrupted by the disease during development. If the pattern or magnitude of morphological integration is different in mutant mice, it should reveal further mechanisms underlying the etiology of the disease. Our analyses showed that the pattern of morphological integration of the shape of the limbs and the shape of the Dusp6 expression domains was similar in unaffected and Fgfr2+/P253R mutant mice (Figure 6E, Figure 6—figure supplement 2). Our results confirmed that the Fgfr2 P253R mutation does not disrupt the strong association between limb shape and the Dusp6 expression domain. Therefore, the alteration of the Dusp6 expression pattern between E10 and E11.5, caused by the Fgfr2 mutation, will correlate with the limb dysmorphologies associated with Apert syndrome. Overall, the high correlation between the shape of the limb and the Dusp6 expression domain provides further evidence that altered Fgf expression resulting from the Fgfr2 mutation is strongly associated with limb defects in Apert syndrome.

## Discussion

By definition, revealing the primary etiology of an abnormality requires going back in time to the earliest moment when abnormal development can be found. Typically, the earliest changes will be the most subtle, and so the most statistically sensitive techniques are necessary to reveal these changes. The methods that are currently used to assess gene expression patterns are mainly qualitative and focus only on shape and size differences that can be simply detected by eye. Therefore, slight changes in gene expression domains, even if they have large effects on the phenotype (Honeycutt, 2008), can remain undetected. To reveal these subtle changes, we have developed a precise method combining OPT and GM to quantify embryo morphology and the underlying 3D gene expression patterns in a systematic, objective manner. This enables the visualization and quantification of how the genotype translates into the phenotype during embryonic development, the comparison of normal and disease-altered patterns of genetic and phenotypic variation and, eventually, the identification of the origins of abnormal morphogenesis. This approach can further our understanding of the etiology of genetic diseases in research using animal models (Spradling et al., 2006; Rosenthal and Brown, 2007), even in models that do not seem to recapitulate the human disease faithfully (Guénet, 2011).

Our study of the Fgfr2 P253R mouse model for Apert syndrome is an exemplary case demonstrating how quantitative assessment can overcome the shortcomings of traditional qualitative morphological assessment and lead to new discoveries. To date, the molecular and developmental mechanisms underlying the limb defects associated with Apert syndrome have remained obscure, even when these limb abnormalities clinically differentiate Apert syndrome from other craniosynostosis syndromes (such as Pfeiffer, Crouzon and Saethre-Chotzen syndromes) (Park et al., 1995; Holten et al., 1997; Cohen and MacLean, 2000). Most Apert syndrome research has focused on premature fusion of cranial sutures and craniofacial malformations (Cohen and MacLean, 2000; Holmes et al., 2009; Martínez-Abadías et al., 2010; Holmes and Basilico, 2012; Hill et al., 2013; Heuzé et al., 2014), clinical traits that are consistently phenocopied in mouse models. However, little research has been carried out on the limb defects in Apert syndrome using the same animal models, mainly because most previous research reported that malformations of the limbs are subtle or absent in the different mouse models for Apert syndrome (Chen et al., 2003; Wang et al., 2005; Wang et al., 2010). Contrary to these previous results, our quantitative morphometric analyses demonstrate that the limbs of Fgfr2+/P253R Apert syndrome mice have significant defects that are detectable in newborn mice and that can be traced back to early embryogenesis (Figure 1, Figure 5 and Figure 6).

Our analyses provide insight into the genetic origins of these limb defects, showing that altered expression patterns of genes in the Fgf signaling pathway precede and contribute to limb dysmorphogenesis in Fgfr2+/P253R Apert syndrome mice. In fact, we detected that Dusp6 expression patterns were different in unaffected and mutant littermates a few hours before the first limb dysmorphologies appeared (Figure 5), and confirmed that limb shape and Dusp6 expression patterns were highly correlated (Figure 6E, Figure 6—figure supplement 2). The altered Fgf signaling that was observed was due to the Fgfr2 P253R Apert syndrome mutation, which causes loss of ligand specificity of the receptor and increased affinity of ligands for Fgfr2. As the Apert syndrome mutation is located in the linker region between the second and the third Ig-like domains of the receptor, and as alternative splicing of the protein occurs in the carboxy-terminal half of IgIII domain, the mutation affects both isoforms of the receptor, Fgfr2IIIb and Fgfr2IIIc (Ibrahimi et al., 2001). Fgfr2IIIb is the isoform that is predominantly expressed in epithelial cells which normally binds to ligands produced in mesenchymal cells, whereas Fgfr2IIIc is expressed in mesenchymal cells and binds to ligands produced in epithelial cells. The available evidence indicates that Apert mutations alter this ligand specificity and thus raise the level of Fgfr2 signaling — either through the aberrant interaction of mutant receptors with inappropriate ligands or through the upregulation of Fgfr2 (Hajihosseini, 2008) and unpublished data). Our analyses showed that over-activation of the Fgf signaling pathway results in more expanded (Figure 5E–G) and larger (Figure 6B) expression domains for Dusp6, a gene that acts as a negative-feedback control of Fgf signaling (Ekerot et al., 2008). A delay in misregulation of the expression of Dusp6 may explain the lack of antero-posterior asymmetry and the shape deficiencies observed in Fgfr2+/P253R mutant mice (Figure 5). We found evidence that limb shape and Dusp6 expression were highly associated (Figure 6C–E), but it is likely that other downstream genes of the Fgf signaling pathway also contribute to the limb shape malformations associated with Apert syndrome.

Our analyses also demonstrated that the embryonic limb defects persisted until birth (Figure 1) and thus did not disappear during development. For instance, we found that Fgfr2+/P253R Apert syndrome mice presented postnatal limb malformations involving the shape, length and volume of many bones of the forelimb, including the scapula, humerus, ulna, radius, metacarpals and phalanges (Table 1 and Figure 1). It is not possible, however, to correlate early changes in limb bud shape directly to the defects in chondrogenesis and long bone length that appear later in development. The skeletal defects associated with Apert syndrome are the result of continuous altered Fgf signaling throughout growth and development. Overall, activated Fgf signaling may lead to decreased bone growth (Li et al., 2007). Our results demonstrate that Dusp6 participates in this process, beginning very early in development, as do many other downstream targets of Fgf signaling that have different functions and spatio-temporal patterns, all of which are involved in the complex process that regulates limb morphogenesis. Although subtle, the first malformations detected in this study suggest that further research into the origins and causes of limb dysmorphologies in Apert syndrome using these and other mouse models is warranted.

Our quantitative approach could be similarly applied to investigate other developmental defects and dysmorphologies (Winter and Baraitser, 1987). This is relevant as major developmental defects represent a leading cause of infant mortality and affect a small but relevant percentage of the population, severely compromising their quality of life (Toxicology NRC C on D, 2000). OPT and GM can potentially be used to analyze any organ and animal model that can be visualized during development using light microscopy, and any gene whose gene expression pattern can be detected by WMISH and shows a continuous expression domain over development (Martínez-Abadías et al., 2016). Our study is a proof of concept that demonstrates that this approach is feasible and develops a protocol that could be adjusted for the study of different genes and organs. With the current pipeline, the implementation of the approach should be straightforward and no more time- or resource-consuming than other cellular or molecular experiments. WMISH labeling is a standard technique in most molecular and developmental laboratories. OPT imaging is increasingly accessible and software for performing GM is freely available.

We exemplified the method by analyzing limb defects in mouse models, but it could be applied to malformations affecting the face, the brain, the tail, or any other organ that involves complex 3D shapes that are quantifiable with GM. Organs with morphologies that are devoid of reliable anatomical landmarks, such as the developing heart, should be analyzed with alternative non-landmark-based methods, such as spherical harmonics (Shen et al., 2009). Moreover, the OPT-GM approach could be applied to other vertebrate animal models, such as zebrafish, chicken and Xenopus. Finally, our approach could also be extended to analyze protein expression patterns. Immunostaining labeling with a secondary antibody coupled to a BAAB-resistant fluorophore, such as Alexa, will reveal the expression pattern of proteins and this information can be precisely captured and quantified in 3D using the OPT-GM approach.

The limitation of the approach is the requirement to generate large samples of wildtype and mutant mice per gene and time point, since several WMISH labeling and OPT scanning activities cannot be performed within the same embryos. For high-throughput analyses assessing the expression of multiple genes, such as transcriptomic and microarray assays (Yeh et al., 2013), our OPT-GM approach is a complementary technique that could confirm whether the differences in the level of gene expression of candidate genes are associated with changes in the patterns of this expression (i.e. the regions within a tissue where the genes are expressed) and further phenotypic malformations. This type of quantitative analyses will lead to a deeper understanding of how development translates genetic into phenotypic variation.

Through its increased quantitative sensitivity, our method has allowed us to reveal that the mouse model for Apert syndrome does indeed show very early abnormalities in limb development. We detected that dysregulation of an Fgfr2 target gene precedes measurable changes in limb bud morphology, thus identifying a relevant component of its genetic etiology. Quantitative evaluation of size and shape should thus be performed before discarding any animal models as useful for investigating human congenital malformations (Zuniga et al., 2012). Our method has the potential to become a useful tool for biomedical research, providing insight into the processes that cause malformations and lead to malfunction, which is essential for understanding diseases and discovering potential therapies.

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
      <td>Genetic reagent (M. musculus)</td>
      <td>Fgfr2+/P253R</td>
      <td>Wang et al., 2010; doi: 10.1186/1471 -213X-10–22</td>
      <td></td>
      <td>Laboratory of Dr. Richtsmeier (Pennsylvania State University); inbred mouse model on a C57BL/6J background</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>PBST</td>
      <td>Sigma-Aldrich</td>
      <td>P3563</td>
      <td>Phosphate-buffered saline, 0.1% tween 20</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>paraformaldehyde</td>
      <td>Sigma-Aldrich</td>
      <td>P6148</td>
      <td>4% in PBS</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>methanol</td>
      <td>Sigma-Aldrich</td>
      <td>494437–2L-D</td>
      <td>Methanol for protein sequencing, bioReagent,99.93%</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>digoxigenin-UTP</td>
      <td>Sigma-Aldrich</td>
      <td>11277073910</td>
      <td>DIG RNA Labeling Mix (Roche)</td>
    </tr>
    <tr>
      <td>Sequence -based reagent</td>
      <td>Dusp6</td>
      <td>Dickinson et al. (2002) doi:10.1016/S0925 -4773 (02)00024–2</td>
      <td></td>
      <td>m Mkp3-pCVM.sport6</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-DIG-AP (sheep polyclonal)</td>
      <td>Sigma-Aldrich</td>
      <td>11093274910</td>
      <td>(1:2000)</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>NBT</td>
      <td>Sigma-Aldrich</td>
      <td>11585029001</td>
      <td>4-nitro blue tetrazolium chloride, crystals (Roche)</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>BCIP</td>
      <td>Sigma-Aldrich</td>
      <td>11383221001</td>
      <td>4-toluidine salt (Roche)</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>BABB</td>
      <td>Sigma-Aldrich</td>
      <td>402834; W213802</td>
      <td>(one benzyl alcohol:two benzyl benzoate)</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>agarose</td>
      <td>Sigma-Aldrich</td>
      <td>A9414</td>
      <td>Agarose low gelling temperature</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Matlab</td>
      <td>The MathWorks, Inc</td>
      <td>RRID:SCR_001622</td>
      <td>https://es.mathworks.com/products/matlab.html</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>R, CRAN</td>
      <td>R Development Core Team, 2014</td>
      <td>RRID:SCR_003005</td>
      <td>http://www.R-project.org/</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Amira 6.3</td>
      <td>FEI</td>
      <td>RRID:SCR_014305</td>
      <td>https://www.fei.com/software/amira-3d-for-life-sciences/</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Viewbox</td>
      <td>dHAL software, Kifissia, Greece</td>
      <td>RRID:SCR_016481</td>
      <td>http://www.dhal.com/</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Geomorph</td>
      <td>Adams and Otárola-Castillo, 2013; doi: 10.1111/2041-210X.12035</td>
      <td>RRID:SCR_016482</td>
      <td>https://cran.r-project.org/web/packages/geomorph/index.html</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MorphoJ</td>
      <td>Klingenberg (2011): doi: 10.1111/j.1755 –0998.2010.02924.x</td>
      <td>RRID:SCR_016483</td>
      <td>http://www.flywings.org.uk/morphoj_page.htm</td>
    </tr>
  </tbody>
</table>

### Mouse model

We analyzed the Fgfr2+/P253R Apert syndrome mouse model, an inbred model backcrossed on the C57BL/6J genetic background for more than ten generations, which carries a mutation that in humans with Apert syndrome is associated with more severe syndactyly. This gain-of-function mutation, which is embryonically lethal in homozygosis, involves a proline to arginine amino acid change at position 253 of the Fgfr2 protein, which alters the ligand-binding specificity of the receptor and causes stronger receptor signaling. Further details of the mouse model and on the generation of targeting construct can be found elsewhere (Wang et al., 2010). All the experiments were performed in compliance with the animal welfare guidelines approved by the Pennsylvania State University Animal Care and Use Committees (IACUC46558, IBC46590).

### Micro-CT imaging

High-resolution micro-computed tomography (μCT) scans were acquired by the Center for Quantitative Imaging at the Pennsylvania State University (www.cqi.psu.edu) using the HD-600 OMNI-X high-resolution X-ray computed tomography system (Varian Medical Systems, Palo Alto, CA). Pixel sizes ranged from 0.01487 to 0.01503 mm, and all slice thicknesses were 0.016 mm. Image data were reconstructed on a 1024 × 1024 pixel grid as a 16-bit TIFF. To reconstruct forelimb morphology from the μCT images, isosurfaces were produced with median image filter using the software package Avizo 6.3 (Visualization Sciences Group, VSG) (Figure 1A–F).

### Morphometrics in P0 mice

We assessed forelimb morphology at P0 using unaffected (N = 10) and mutant (N = 12) littermates of Apert syndrome mouse models. A selection of 54 landmarks was collected on the left forelimb of all P0 mice, as shown in Figure 1B–F, following anatomical criteria selected to best describe the size and shape of forelimb bones in a reliable and reproducible manner. Landmarks at the proximal and distal tips of the phalanges, metacarpals, radius, ulna and clavicle were collected to represent the simple tubular shape of these bones. Additional landmarks were collected in anatomical structures of the humerus and scapula to better represent their complex 3D shapes (Figure 1B–F). To minimize measurement error, each landmark was collected twice by the same observer, restricting the deviations between the two trials to 0.05 mm.

At P0, we estimated the dimensions of the long bones of the forelimbs using the 3D coordinates of the landmarks located at the proximal and distal ends of the bones (Figure 1B–F). We also estimated the bone volumes from volume data collected from the microCT scans. To assess size differences in bone length and bone volume between mutant and unaffected P0 mice of the Fgfr2+/P253R Apert syndrome mouse model, we performed a two-tailed one-way ANOVA on those variables showing a normal distribution, and the non-parametric Mann-Whitney U-Test on those variables that deviated from a normal distribution. The shape of the humerus and the scapula was comparatively assessed in unaffected and Fgfr2+/P253R Apert syndrome littermates using Geometric Morphometrics.

Shape information was extracted using a Generalized Procrustes Analysis (GPA) (Rohlf and Slice, 1990), in which configurations of landmarks are superimposed by shifting them to a common position, rotating and scaling them to a standard size until a best fit of corresponding landmarks is achieved (Dryden and Mardia, 1998). The resulting Procrustes coordinates from the GPA were the input for further statistical analysis to compare the shape of the bones in unaffected and Fgfr2+/P253R mice. A Principal Component Analysis (PCA) was used to explore the morphological variation within each bone. PCA performs an orthogonal decomposition of the data and transforms variance covariance matrices into a smaller number of uncorrelated variables called Principal Components (PCs), which successively account for the largest amount of variation in the data (Hallgrimsson et al., 2015). Each specimen is scored for every Principal Component and the specimens can be plotted using these scores along the morphospace defined by the principal axes.

### WMISH and OPT scanning

To examine early embryonic mouse limb development in Apert syndrome mice, we bred four litters of the Fgfr2+/P253R Apert syndrome mouse model and collected them between E10.5 and E11.5. In total, 32 mouse embryos were harvested and classified by PCR genotyping into unaffected (N = 16) and mutant (N = 16) littermates (see Table 2 and Figure 4 for further details on sample size and composition). We analyzed the maximum number of samples that we could process simultaneously within the same WMISH batch, as explained next.

Dusp6 gene expression was assessed by whole-mount-in-situ hybridization (WMISH). Mouse embryos were dissected in cold phosphate-buffered saline, 0.1% tween 20 (PBST), fixed overnight in 4% paraformaldehyde (Sigma), dehydrated in a graded PBST/methanol series and stored at –20°C in methanol. The mouse embryos recovered their original size after rehydration in decreasing series of methanol/PBST. WMISH was carried out using Dusp6 antisense RNA probes labeled with digoxigenin-UTP (Roche), following standard protocols (de la Pompa et al., 1997). Alkaline phosphatase coupled anti-digoxigenin (anti-DIG-AP, Roche) and NBT/BCIP staining (Roche) were used to reveal the expression pattern for Dusp6. To minimize variations during experimental procedures, all embryos were processed systematically within the same batch, processing unaffected and mutant littermates from different litters in separate tubes, but simultaneously using the same probe, timings and concentration reagents.

After embedding in agarose, dehydrating in methanol and chemically clearing the samples with benzyl alcohol and benzyl benzoate (BABB), the stained whole embryos were scanned with both fluorescence and transmission light with a cyan fluorescent protein (CFP) filter using our home-built OPT imaging system mounted on a Leica MZ 16 FA microscope (Sharpe et al., 2002). The embryos were 3D-reconstructed from the resulting 2D images using Matlab (The MathWorks, Inc.) and visualized using Amira 6.3 (Visualization Sciences Group, FEI). From the OPT fluorescence scans, we produced 3D reconstructions of the embryo surface and we dissected the available right and left fore- and hindlimbs of each specimen, resulting in a sample of 100 embryonic limbs (Table 2). From the OPT transmission scans, we recovered the Dusp6 expression domain. As Dusp6 is expressed in a fuzzy spatial gradient, as already shown by other genes (Martínez-Abadías et al., 2016), we used 3D multiple thresholding to visualize the gene expression domain at different intensities (Figure 3). To analyze the gene expression domains comparatively across the samples, we inspected the whole range of threshold values under which the gene expression could be visualized for each limb, from the threshold showing its first appearance to the threshold under which it disappeared and was no longer detectable. We analyzed the 3D reconstruction on the basis of a threshold computed as 1/3 that of the last grey value showing the Dusp6 expression domain, which displayed a Dusp6 domain at high gene expression (Figure 3, step 3). Finally, we obtained 80 limbs (46 forelimbs and 34 hindlimbs) with associated gene expression patterns for Dusp6. Limbs or gene expression domains that were damaged during experimental manipulation or which showed obvious artifacts resulting from altered staining or imaging were discarded from the analyses. Outlier points were detected following standard protocols in GM that are based on squared Procrustes distance, and landmark misplacements were fixed whenever possible.

### Embryo staging

To account for breeding and developmental variation, individual limb buds were staged using our publicly available web-based staging system (https://limbstaging.embl.es) (Musy et al., 2018). Considering the spline curve along the outline of the limb, this tool provides a stage estimate with a reproducibility of ±2 hr. According to the staging results, the different mouse litters were ordered following a continuous temporal sequence from E10 to E11.5 (Table 2 and Figure 4). To minimize high developmental variation within and among litters of mice, hindlimbs and forelimbs from each litter were analyzed separately, except for those from two litters from the earliest stage that were pooled into the same group because their temporal distribution completely overlapped, as shown in Figure 4.

### Morphometrics from E10 to E11.5

To capture the size and shape of the limbs and the expression domains of Dusp6, we collected a set of anatomical landmarks as well as curve and surface semi-landmarks (Figure 5—figure supplement 1), as recommended in structures devoid of homologous landmarks. Semi-landmarks are mathematical points located along a curve (Bookstein, 1997) or a surface (Gunz et al., 2005) within the same object that can be slid to corresponding equally spaced locations across the sample. Only five anatomical landmarks were discernible in the limb, and four in the Dusp6 expression pattern (Figure 5—figure supplement 1). We defined several curves and surfaces over the limb as well as gene expression structures with a relatively low number of semi-landmarks in order to minimize the high dimensionality of the data while providing an adequate shape coverage that precisely captured the subtle morphological changes associated with the Apert syndrome mutation. We used Amira 6.3 (Visualization Sciences Group, FEI) to record the anatomical landmarks and Viewbox 4 (dHAL software, Kifissia, Greece) to construct a limb template of surface and curve semi-landmarks and to interpolate them onto each target shape (Figure 5—figure supplement 1).

The 3D landmark coordinates defining the shape of the limb and the Dusp6 expression domain were analyzed using Procrustes-based landmark analysis (Bookstein, 1997). Semi-landmarks were allowed to slide in the GPA by minimizing the bending energy (Bookstein, 1997; Gunz et al., 2005; Mitteroecker and Gunz, 2009). Quantitative shape analyses based on PCA were performed as explained above.

We estimated the size of the limb as the centroid size, calculated as the square root of the summed squared distances between each landmark coordinate and the centroid of the limb configuration of landmarks (Dryden and Mardia, 1998). The volumes of the Dusp6 domains were estimated from the 3D reconstructions of the OPT scans. Differences in limb size and gene expression volume between mutant and unaffected embryonic mice were tested for statistical significance using a two-tailed Welch Two Sample t-test.

We quantified the integration between the limb and the Dusp6 expression pattern and produced visualizations of the patterns of associated shape changes between them using two-block Partial Least Squares analysis (PLS) (Rohlf and Corti, 2000). This method performs a singular value decomposition of the covariance matrix between the two blocks of shape data (i.e., the limb and the Dusp6 expression domain). Uncorrelated pairs of new axes are derived as linear combinations of the original variables, with the first pair accounting for the largest amount of inter-block covariation, the second pair for the next largest amount and so on. The amount of covariation is measured by the RV coefficient, which is a multivariate analogue of the squared correlation (Klingenberg, 2009). Statistical significance was tested using permutation tests under the null hypothesis of complete independence between the two blocks of variables. Separate analyses for each developmental period, as well as for forelimbs and hindlimbs of all stages, were computed.

All of the analyses were performed using R (R Development Core Team, 2014; http://www.R-project.org); the R package geomorph (Adams and Otárola-Castillo, 2013; http://cran.r-project.org/web/packages/geomorph), SPSS Statistics 22 (IMB, 2013) and MorphoJ (Klingenberg, 2011).
