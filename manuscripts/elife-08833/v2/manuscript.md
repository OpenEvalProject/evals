# Suppression of transcriptional drift extends C. elegans lifespan by postponing the onset of mortality

## Authors

- Sunitha Rangaraju<sup>1</sup>
- Gregory M Solis<sup>1</sup>
- Ryan C Thompson<sup>2</sup> ([ORCID: 0000-0002-0450-8181](https://orcid.org/0000-0002-0450-8181))
- Rafael L Gomez-Amaro<sup>1</sup>
- Leo Kurian<sup>5</sup>
- Sandra E Encalada<sup>2</sup>
- Alexander B Niculescu<sup>6</sup>
- Daniel R Salomon<sup>2</sup>
- Michael Petrascheck<sup>1</sup> †

### Affiliations

1. Department of Chemical Physiology The Scripps Research Institute La Jolla United States
2. Department of Molecular and Experimental Medicine The Scripps Research Institute La Jolla United States
3. Dorris Neuroscience Center The Scripps Research Institute La Jolla United States
4. Department of Molecular and Cellular Neuroscience The Scripps Research Institute La Jolla United States
5. Center for Molecular Medicine University of Cologne Cologne Germany
6. Department of Psychiatry Indiana University School of Medicine Indianapolis United States

† Corresponding author

## Abstract

Longevity mechanisms increase lifespan by counteracting the effects of aging. However, whether longevity mechanisms counteract the effects of aging continually throughout life, or whether they act during specific periods of life, preventing changes that precede mortality is unclear. Here, we uncover transcriptional drift, a phenomenon that describes how aging causes genes within functional groups to change expression in opposing directions. These changes cause a transcriptome-wide loss in mRNA stoichiometry and loss of co-expression patterns in aging animals, as compared to young adults. Using Caenorhabditis elegans as a model, we show that extending lifespan by inhibiting serotonergic signals by the antidepressant mianserin attenuates transcriptional drift, allowing the preservation of a younger transcriptome into an older age. Our data are consistent with a model in which inhibition of serotonergic signals slows age-dependent physiological decline and the associated rise in mortality levels exclusively in young adults, thereby postponing the onset of major mortality.

## Introduction

The most widely used standard to measure aging of an organism is the quantification of lifespan (Partridge and Gems, 2007). Lifespan relates to aging, as the latter causes the degeneration of tissues and organs, thereby increasing mortality due to systemic functional tissue failure (Balch et al., 2008; Bishop et al., 2010; David et al., 2010; Haigis and Sweet-Cordero, 2011; Taylor and Dillin, 2011; Gladyshev, 2013; Burkewitz et al., 2015; Currais, 2015). Several genetic and pharmacological strategies have been shown to prolong the lifespan of various organisms, including C. elegans (Kenyon et al., 1993; Kaeberlein et al., 1999; Curran and Ruvkun, 2007; Evason et al., 2008; Onken and Driscoll, 2010; Alavez et al., 2011; Chin et al., 2014; Ye et al., 2014; Tatum et al., 2015). Mutations in age-1 or daf-2, for example, slow degenerative processes occurring throughout life, thereby constantly lowering mortality rates (Johnson, 1990; Kenyon et al., 1993; Taylor et al., 2014). Age-associated degenerative processes such as a decline in proteostatic capacity are not necessarily restricted to older organisms but can also be observed in young adults (Labbadia and Morimoto, 2015a; 2015b). This raises the possibility of degenerative processes that occur only in young adults and thus specifically contribute to the rise of mortality during young adulthood. Any longevity mechanisms preventing such a degenerative process would specifically slow mortality rates during the period of young adulthood, effectively prolonging its duration to postpone the onset of major age-associated mortality around midlife (Bartke, 2015). However, to identify such mechanisms would require mortality-independent metrics of age-associated change, as age-associated mortality rates during young adulthood are difficult to determine by demographic analysis against the back drop of non-aging-related death events (Partridge and Gems, 2007; Beltran-Sancheza et al., 2012).

In C. elegans, mortality-independent metrics of aging include age-associated decline of various behaviors or physiological parameters such as movement or stress resistance (Huang et al., 2004; Bansal et al., 2015). Molecular markers of aging include sets of genes whose expression change with age, such as micro-RNAs, electron transport chain (ETC) components, or genes involved in posttranslational modifications such as methylation (Budovskaya et al., 2008; de Magalhaes et al., 2009; Pincus et al., 2011; Horvath et al., 2015). However, aging also increases DNA damage, affects nuclear architecture, chromatin complexes, chromatin modifications, and the transcriptional machinery (Mostoslavsky et al., 2006; Scaffidi and Misteli, 2006; Feser et al., 2010; Greer et al., 2011; Maures et al., 2011; Fushan et al., 2015). Therefore, an emerging alternative approach to measure specific gene expression changes with age is to quantify the progressive imbalance in gene expression patterns as a function of age. Two such approaches, one measuring transcriptional noise, the cell-to-cell variation in gene expression, and the other measuring decreasing correlation in the expression of genetic modules, showed a loss of co-expression patterns with age (Bahar et al., 2006; Southworth et al., 2009). These studies suggest that age-associated changes can be measured independently from mortality by tracking the loss of gene expression patterns that are observed in young animals.

In the present study, we set out to investigate the mechanisms by which the atypical antidepressant mianserin extends lifespan by recording the transcriptional dynamics of mianserin-treated and untreated C. elegans across different ages. These studies revealed that aging causes transcriptional drift, an evolutionarily conserved phenomenon in which the expression of genes change in opposing directions within functional groups. These changes cause a transcriptome-wide loss in mRNA stoichiometry and loss of co-expression patterns in aging animals, as compared to young adults. Mianserin treatment reduced age-associated transcriptional drift across ~80% of the transcriptome, preserving many characteristics of transcriptomes of younger animals. We used transcriptional drift along with mortality analysis as metrics to monitor aging and find that mianserin treatment extended lifespan by exclusively slowing age-associated changes in young adults, thereby postponing the onset of mortality.

## Results

### Aging causes a loss of co-expression patterns observed in young adults

To better understand how aging changes gene expression patterns in a eukaryotic organism, and how these changes are affected by longevity, we measured gene expression changes in mianserin-treated or untreated C. elegans by RNA-sequencing (RNA-seq; Figure 1a). Cohort #1 was a time series to study how gene expression patterns change over time in control (water) animals or in animals treated with mianserin on day 1 of adulthood (24 hr after L4 stage). Cohort #2 was designed to study dosage effects of increasing concentrations of mianserin with aging, and cohort #3 was designed to study the effects of delayed mianserin-treatment of worms treated at day 3 or 5 of adulthood (Figure 1a). Lifespan of a sub-population of each cohort was simultaneously assessed to ensure the effect of mianserin.

![Figure 1.](https://cdn.elifesciences.org/articles/08833/elife-08833-fig1-v2.jpg)

**Figure 1.:** (a) Schematic of RNA-seq experiment. In cohort #1, water or mianserin was added on day 1 of adulthood and RNA samples were harvested on day 1 (water only), day 3 (d3), day 5 (d5) and day 10 (d10). In cohort #2, animals were treated with water or increasing concentrations of mianserin (2, 10 or 50 µM) on day 1 (d1) and RNA was harvested on day 5 (d5) for RNA-seq. In cohort #3, water or 50 µM mianserin was added on day 1, day 3, and day 5, and RNA was harvested on day 10 (d10) for RNA-seq. (b) Venn diagrams of the number of GOs enriched for genes that decrease expression with mianserin (down, dark blue circle) increase expression with mianserin (up, light blue circle) or are enriched for both (intersection). (c) Venn diagrams of the number of GOs enriched for genes that decrease expression with age (down, gray circle) increase expression with age (up, white circle) or are enriched for both (intersection). (d) Heat map depicting log2 changes in gene expression for oxidative stress genes elicited by increasing concentrations of mianserin (yellow, increased expression; blue, decreased expression) (e) Mianserin decreases expression of redox genes that increase with age and increases expression of genes that decrease with age. (f) Mianserin reverts age-associated changes on the level of GOs. Venn diagrams of the number of GOs enriched for genes that decrease expression with mianserin (down, dark blue circle) and increase with age (up, white circle) or vice versa (down with age, gray circle; up with mianserin, light blue circle). (g) Mianserin reverts age-associated changes on the level of individual genes. Volcano plot shows the negative log10 of P-values as a function of log2 fold changes of 3,367 genes that significantly change expression from day 1 to day 3 in samples of water-treated control animals (black) or samples from age-matched mianserin-treated animals (50 µM, blue). As animals age, gene expression levels change (“drift”) away from levels observed in young adults (yellow line). Mianserin treatment attenuates age-associated gene expression changes preserving expression levels as seen in young adults. (h) Drift-plot shows log fold change (old/young) as a function of age for each gene involved in oxidative phosphorylation (gray lines. KEGG: cel 04142). Superimposed are Tukey-style box-plots to graph the increases in drift-variance across the entire pathway. Gene expression changes are classified into type I, which describes activation or repression of the entire pathway and into type II, which describes changes among genes relative to each other (drift-variances), see red arrows. (i) Drift-plot for lysosomal genes (KEGG: cel 00190). See Figure 1—source data 1–5, Figure 1—figure supplement 1 and Table 1 for additional information on data-sets. Also see Methods section for transcriptional drift calculation in each figure panel.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/08833/elife-08833-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** Expression patterns of GO annotations are disrupted with age. Representative pie charts show a cross-section of 50 out of 249 GO annotations enriched for genes that change in opposing direction as animals age (day 3, 5, and 10). The fraction of genes whose expression increase with age (yellow), the fraction of genes whose expression decrease with age (black), and the fraction of genes that maintain the expression seen in young day 1 adults (white) are shown. GOs are sorted and represented in the figure, starting with GOs that show the least disruption in the upper left, and the GO’s with the most extreme changes in the lower right. As animals’ age progresses from day 3, 5 to 10, more and more genes change expression in opposing directions disrupting the transcriptional stoichiometry observed in young day 1 animals. None of these 50 pie charts, as is, allows any statements on how the functional states of the physiological processes they represent change with age. The GO names and number of genes (n) belonging to each GO are shown.

Comparison of gene expression profiles of age-matched mianserin-treated and untreated controls, showed that approximately 3,000–6,000 genes changed with age in response to mianserin treatment (FDR<0.1, Figure 1—source data 1) (Robinson and Oshlack, 2010; Kim et al., 2013; Lawrence et al., 2013). We separated genes into sets that showed increased or decreased expression in response to mianserin, to conduct gene-set enrichment analysis. This revealed hundreds of gene ontologies (GO) that changed in response to mianserin (Figure 1—source data 2) (Ashburner et al., 2000; Mi et al., 2005). We observed that many GOs were enriched for both, genes that increased as well as decreased as a consequence of aging. This observation complicated any interpretation on whether pathways were activated or inhibited in response to mianserin, and how the associated function (GO) relates to mianserin-induced lifespan extension (Figure 1b).

We observed a similar scenario by conducting gene-set enrichment analysis for gene expression changes in response to age in untreated animals. As seen with mianserin, many GO annotations were enriched for both up- as well as downregulated genes at any given age (Figure 1c; Figure 1—source data 3, 4), making it difficult to interpret whether those pathways are being activated or inhibited with age. We generated 50 representative pie charts out of the 249 GO annotations that contained genes that increased or decreased in expression by day 10 due to aging. These charts suggested that as animals age and become older, genes change expression in opposing directions, disrupting relative mRNA ratios within the GO, when compared to young adults (Figure 1—figure supplement 1). Thus, aging changed the stoichiometric relationship between mRNAs belonging to the same functional group (GO). In many cases, the fractions of genes that increased, decreased or did not change in expression showed no consistent pattern, nor provided any insight into the pathway activity (Figure 1—figure supplement 1).

Because the expression patterns observed in many GOs were difficult to interpret in terms of functional change, we turned to investigate expression changes in the superoxide detoxification pathway, a well-defined cellular function that declines with age (Ashburner et al., 2000; Mi et al., 2005; Kumsta et al., 2011; Bansal et al., 2015; Rangaraju et al., 2015a). As expected from our previous studies (Rangaraju et al., 2015a), the expression levels of some superoxide detoxification genes were higher in mianserin-treated animals compared to age-matched controls (Figure 1d). Exceptions were the expression levels of sod-4 and sod-5, which were lowered upon mianserin treatment (Figure 1d). However, plotting expression changes of superoxide detoxification genes as a function of age (Figure 1e, left panel) revealed again a scenario in which genes changed in opposing directions as seen in the pie charts for many GOs before (Figure 1—figure supplement 1). Some mRNAs including those of sod-4, -5 increased with age, while some decreased (sod-1, -2, prdx-2, 3, 6) and some did not change (ctl-1, 2, 3), leading to an overall 5-10-fold change in stoichiometric balance among superoxide detoxification-associated mRNAs by day 5 (Figure 1e, left panel). More interestingly, if the expression of an sod increased with age, mianserin treatment prevented the increase and if the expression of an sod decreased with age, mianserin prevented the decrease (Figure 1e, right panel). Thus, when we took the mRNA expression levels of young animals into account, the emerging picture suggested that mianserin treatment attenuated age-associated gene expression changes.

We therefore asked whether the complex gene-set enrichment patterns observed comparing mianserin-treated and untreated samples (Figure 1b,c) could be explained by mianserin preventing expression changes due to age. Indeed, many GO annotations that increased expression with age were decreased by mianserin treatment and vice versa (Figure 1f). This attenuation of age-associated changes by mianserin treatment was even more pronounced for individual genes (Figure 1g). Analyzing cohort #1 showed a significant change in expression levels of 3,367 genes, as the animals aged from day 1 to day 3, and a change in 5,947 genes from day 1 to day 10 (FDR < 0.1) (Figure 1g, significant genes only). Mianserin treatment reduced these age-associated expression changes in over 90% of cases. Including all age-associated expression changes for the 19,196 different transcripts present in our data-set, we found that mianserin treatment attenuated age-associated changes in transcription in 15,095 out of 19,169 genes (80%, binomial P < 10–100). Thus, most of the changes observed between mianserin-treated and untreated animals are due to mianserin preventing transcriptional changes with age.

When we excluded all genes that changed due to age and were attenuated by mianserin, we obtained a much smaller gene-set consisting of mianserin-induced changes that was enriched for GOs related to stress, xenobiotic and immune-responses, as well as genes associated with aging and the determination of lifespan (Table 1, Figure 1—source data 5). These GOs have been previously shown to be regulated by serotonin in C. elegans with the exception of the xenobiotic response (Zhang et al., 2005; Petrascheck et al., 2007; Rangaraju et al., 2015a). Thus, accounting for age-associated transcriptional changes dramatically simplified a seemingly very complex gene-expression pattern (Figure 1b,c). It revealed that mianserin affected expression of a small set of physiological functions that are known to be regulated by serotonin and have been shown to be required for mianserin-induced lifespan extension or for aging in general (Garsin et al., 2003; Rangaraju, et al., 2015; Petrascheck, et al., 2007) (Table 1; Figure 1f; Figure 1—source data 5).

**Table 1.**
 GO annotations enriched for genes upregulated by mianserin during all ages, assessed by RNA-seq (day 3, 5 and 10).


<table>
  <thead>
    <tr>
      <th>GO</th>
      <th>Enriched P-value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>response to stimulus</td>
      <td>4.47E-08</td>
    </tr>
    <tr>
      <td>response to stress</td>
      <td>5.83E-05</td>
    </tr>
    <tr>
      <td>response to xenobiotic stimulus</td>
      <td>3.25E-07</td>
    </tr>
    <tr>
      <td>defense response</td>
      <td>4.66E-05</td>
    </tr>
    <tr>
      <td>innate immune response</td>
      <td>1.56E-02</td>
    </tr>
    <tr>
      <td>immune response</td>
      <td>1.62E-02</td>
    </tr>
    <tr>
      <td>immune system process</td>
      <td>1.62E-02</td>
    </tr>
    <tr>
      <td>aging</td>
      <td>6.63E-05</td>
    </tr>
    <tr>
      <td>multicellular organismal aging</td>
      <td>6.63E-05</td>
    </tr>
    <tr>
      <td>determination of adult lifespan</td>
      <td>6.63E-05</td>
    </tr>
  </tbody>
</table>

_Note: No process was specifically downregulated for all three ages._

Based on these observations, we classified gene expression changes for groups of genes into two types. Type I changes describe whether the overall expression across an entire functional group/pathway increases or decreases i.e. whether the pathway is up or down regulated with age. Type II changes describe the relative changes in gene expression among genes within functional groups with respect to each other. We named the type II change transcriptional drift. As animals age, genes within functional groups change expression levels in opposing directions resulting in the disruption of the co-expression patterns seen in young adults.

To analyze the effects of aging on transcriptional drift (type II), we designed graphs that plot the log-fold changes (log [old/young reference day1]) in gene expression as a function of age. Such a plot can be constructed for whole transcriptomes as well as for any functional subset of genes, for example, genes involved in oxidative phosphorylation or lysosome biology (Figure 1h,i). In young adults, the log-fold change is 0 and values close to 0 therefore suggest gene expression as seen in young adults (Figure 1h,i). To quantify transcriptional drift changes with age (type II), we calculated the variance of the log-fold change for genes involved in each pathway. For the purpose of this study, we will refer to this variance as drift-variance (see Materials and methods). If gene expression ratios within a pathway stay constant with age, drift-variance will stay small. If a majority of genes within a pathway change expression in opposing directions or if the rates by which they change differ dramatically, drift-variance will increase. Note that “transcriptional drift” is different from “transcriptional noise” in that the former analyzes variance among genes within the same biological replicates, whereas the latter analyzes variance of the same genes among biological replicates. Hence, how far the aging transcriptome deviates away from the transcriptome seen in young adults can be graphed in a Tukey-style box plot, which plots the drift-variance as a function of age (Figure 1h,i). We will refer to these plots as drift-plots (Figure 1h; Figure 2—figure supplement 1a–d).

### Longevity mechanisms attenuate transcriptional drift-variance

We constructed drift-plots for all 19,196 genes in the data of cohort #1, which revealed a dramatic increase in drift-variance with age, showing a progressive loss of mRNA stoichiometries and co-expression patterns observed in young-adults (Figure 2a, shaded region encompassing the whiskers of Tukey-plot). This effect was also seen in other publicly available data-sets of aging C. elegans transcriptomes and drift-variance continued to increase with age at least until day 20 (Figure 2—figure supplement 1e). Mianserin treatment attenuated the effect of aging across the whole transcriptome and preserved the co-expression patterns observed in young-adults into later age. To test whether transcriptional drift is driven by a small subset of mRNAs or a transcriptome-wide phenomenon, we randomly divided the transcriptome into subsamples of ~1,000 genes. Each subsample showed identical increases in drift-variance with age, confirming a transcriptome-wide effect (Figure 2—figure supplement 1f).

![Figure 2.](https://cdn.elifesciences.org/articles/08833/elife-08833-fig2-v2.jpg)

**Figure 2.:** (a) Drift-plots show that mianserin attenuates increasing drift-variance with age. Note that drift-variance in 10-day-old mianserin-treated animals is the same as in untreated 3-day-old control animals (dotted red line). (b) Drift-plots show that increasing concentrations of mianserin cause drift-variance to decrease. Drift-variance was measured on day 5 by RNA-seq. (c) Corresponding to b, lifespan curves show that increasing concentrations of mianserin leads to a dose-dependent increase in survival. (d) Drift-plots show that initiating mianserin treatment at later ages reduces (d3) or abolishes (d5) its effect on transcriptional drift. Drift-variance was measured on day 10 by RNA-seq. (e) Corresponding to d, lifespan curves show initiating mianserin treatment at later ages reduces (d3) or abolishes (d5) its effect on lifespan. (f) Log-fold change of xenobiotic gene expression on day 10 when mianserin was added on day 1 or day 5, compared to control animals treated with water on day 1. Adding mianserin on day 1 or day 5 leads to comparable changes. (g) Drift-plots show daf-2 RNAi attenuates increasing drift-variance with age in a manner dependent on daf-16. Left: vector control, middle: daf-2 RNAi, right: daf-16/daf-2 RNAi. P-values for transcriptional drift plots are calculated by robust Levene’s test, which compare variances and not mean values. ***P<0.001. All error bars show drift-variance. See Figure 2—figure supplement 1–2 for additional information on calculating drift-variance and Table 2. Also, see Methods section for transcriptional drift calculation in each figure panel.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/08833/elife-08833-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (a) Relationship of (a) fold-changes in gene expression as measured by qRT-PCR to b) RNA-seq counts to (c) transcriptional drift and (d) drift-variance plots. Fold-changes in gene expression in older (day 5) animals by mianserin are mostly caused by mianserin preserving the expression levels seen in young animals, thus leading to small drift-variances for groups of genes. (e) Additional transcriptional drift plots for aging C. elegans based on GEO data-sets GSE21784 and GSE46051. Transcriptional drift increases continuously up until at least day 20 towards the end of the lifespan. (f) Transcriptional drift is observed across the entire transcriptome. Random sub-sampling generating ten sets of ~1,000 genes and plotting their drift-variance shows that transcriptional drift is a phenomenon present across the entire transcriptome and is not driven by small subsets of genes.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/08833/elife-08833-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** (a) DIC photomicrograph of eggs obtained from FUDR (120 µM final) treated animals. Eggs are terminally arrested around the ventral closure (“bean stage”, 400–500 nuclei) and show a shrunken cell mass. Birefringent gut granules are observed in the middle of the eggs. Images were taken ~48 hr after FUDR treatment. (Scale bar = 20 µm). (b) Number of adult worms that produce eggs 24 hr after FUDR treatment. Of the 298 worms evaluated, all of the animals developed germline with eggs inside. (c) Treatment with FUDR dramatically reduces the RNA content in eggs. Total RNA was extracted from FUDR-treated whole wt (N2) worms, from eggs isolated from FUDR-treated N2 worms after ~28 hr of FUDR treatment and from eggs from non-FUDR-treated N2 worms (the same time point as the RNA-seq young reference),. ***P<0.001, comparison between whole worms and eggs treated with FUDR, unpaired t-test, n=3, Error bars S.E.M; ##P<0.01, comparison between eggs treated with FUDR and no FUDR, unpaired t-test, n=3, Error bars S.E.M. (d) Electrophoresis of RNA extracted from whole worms or eggs isolated from FUDR treated animals. Same number of animals used for each sample. Comparison of equal volumes (10 µl) of total RNA loaded from FUDR-treated whole worms and eggs isolated from FUDR-treated animals, resolved in an agarose gel. (e) Original drift plot from Figure 2a is shown again for comparison. Note that box in the middle of the drift plot, which is a Tukey-pl﻿ot, represents the interquartile mean, or 50% of the transcriptome that changes less with age. As drift is also observed in the interquartile mean, drift is not driven by extreme outliers, but by the majority of the genes across the entire transcriptome. (f) Drift plot generated from our data-set only including genes that were also detected in the CF512 sterile strain data-set from (Murphy et al., 2003). (g) Drift plot generated after removing 7,292 genes involved in egg-related functions detected from an eggs-only RNA-seq data-set (Osborne Nishimura et al., 2015). (h) DIC photomicrograph of eggs obtained from untreated and FUDR-treated animals carrying the Pgcy-8::GFP reporter for AFD neurons. (i) Fluorescence microscopy images show AFD neurons in eggs derived from untreated adults (left panel, white arrows) but not in eggs obtained from FUDR-treated adults (middle panel), confirming that FUDR treated eggs do not progress past the “bean stage”. FUDR does not inhibit Pgcy-8::GFP expression in adults (right panel). (j) Overlay of h and i. (k) Drift plots using our data-set including only the genes that are highly enriched in AFD, ASE or NSM neurons (Etchberger et al., 2007; Spencer et al., 2014). As FUDR arrests embryonic development before the birth of these neurons, the drift-plots cannot be influenced by RNA derived from eggs. Explanations for Figure 2—figure supplement 2 In the experiments presented in the main manuscript, we used FUDR to sterilize the animals from which we subsequently extracted RNA for RNA-seq. Thus, our samples contained fractions of egg RNA. The following control experiments and analysis show that the fraction of RNA in our samples coming from eggs is small and does not influence the phenomenon of transcriptional drift and its attenuation by mianserin. We first isolated eggs from FUDR-treated and untreated animals. FUDR treatment causes the cell mass inside the eggs to shrink and to terminally arrest at around bean stage (400–500 nuclei) (Figure 2—figure supplement 2a). FUDR-treated animals all contained similar numbers of eggs 24 hr after FUDR treatement (n=298) (Figure 2—figure supplement 2b) Note that many of the reported FUDR side-effects such as a lack of germline are not observed in 96-well liquid culture (Gomez-Amaro et al., 2015). Extracting RNA from whole worms or eggs isolated from whole worms showed that FUDR-treated eggs contained 5 times less RNA compared to untreated eggs. The fraction of RNA originating from the eggs in FUDR-treated worms was roughly ~5% (Figure 2—figure supplement 2c,d). We next asked whether this fraction could in anyway influence the phenomenon of transcriptional drift. The original plots (Figure 2a, or Figure 2—figure supplement 2e) of the entire transcriptome show that drift-variance increases in the interquartile mean (boxes) showing that it is not driven by a set of outlier genes, making it unlikely that the 5% fraction would influence drift-variance (Krzywinski and Altman, 2014). Nevertheless, to test possible interference, we calculated drift plots for various subsets of our data excluding transcrips expressed in eggs. The Murphy data were derived from CF512 (sterile) animals and thus any genes detected do not originate from eggs. We therefore excluded all genes not detected by Murphy et al from our data-set and recalculated drift. The resulting drift plot still shows a dramatic increase in drift-variance and attenuation by mianserin (Figure 2—figure supplement 2f). A potential problem with the approach used in Figure 2—figure supplement 2f is that it only removed eggs/germline genes that are specific for eggs but that it did not remove genes that are present in both eggs and soma. We therefore removed all genes that were identified in C. elegans eggs by RNA-seq from our data-set to plot Figure 2—figure supplement 2g (Osborne Nishimura et al., 2015). Of the 7,700 transcripts identified in eggs, 7,200 were present in our data-set. Note that this approach removes all ubiquitously expressed genes like ribosomal, mitochondrial and similar housekeeping genes that are present in both embryos and soma. Even though this operation removes only 7,200 out of 19,196 individual genes present in the data-set, these 7,200 genes account for 73% of total mRNA counts. Despite this dramatic reduction in overall mRNA transcripts, the drift plot combining the remaining 11, 904 genes (mostly low expressing genes) confirms an increase in drift-variance with age that is suppressed by mianserin (Figure 2—figure supplement 2g). To identify gene-sets that cannot possibly originate from the FUDR-treated eggs we exploited the specific arrest in embryonic development caused by FUDR. The DIC images suggested that FUDR arrests embryonic development before the birth of AFD, ASE and NSM neurons. If so, genes in our data-set that are specifically expressed in these neurons have to originate from the adult somatic tissue. To test that FUDR treatment prevents the birth of these neurons, we imaged eggs of C. elegans carrying a Pgcy-8::GFP transgene (AFD marker) (Figure 2—figure supplement 2h, i, j). Eggs from untreated animals showed a clear expression of the marker while FUDR-treated eggs did not (Figure 2—figure supplement 2i, j (n>100)). FUDR did not repress the expression of the Pgcy-8::GFP transgene in adults, showing that the lack of a Pgcy-8::GFP signal in FUDR-treated eggs is due to an arrest before the neurons are born and not due to inhibition of the reporter expression by FUDR. As AFD neurons are born before ASE and NSM neurons, these results suggested that none of these three neurons are present in FUDR-treated eggs (Sulston et al., 1983). After having established the absence of AFD, ASE and NSM neurons in eggs derived from FUDR treated animals, we then used the published gene-sets that are highly enriched in these three neuron types (AFD, ASE, NSM) to construct drift-plots (Etchberger et al., 2007; Spencer et al., 2014). Even for these highly restricted sets of genes, drift-variance dramatically increased with age and was repressed by mianserin. Taken together, these results show that the RNA contamination from FUDR-treated eggs is minimal and that this residual amount does not influence our results.

We previously showed, that the effect of mianserin to extend lifespan is dose-dependent (Petrascheck et al., 2007). To explore a possible quantitative relationship between longevity and drift-variance, we generated drift-plots for transcriptomes of animals treated with increasing doses of mianserin (Figure 1a, cohort #2). Increasing doses of mianserin progressively increased longevity and decreased drift-variance as measured in 5-day-old animals (Figure 2b,c; Table 2). Thus, remarkably, by varying the dose of a single molecule, it was possible to control the degree to which aging drives the loss of transcriptional co-expression away from patterns observed in young adults. These results suggested a quantitative relationship between mianserin-induced longevity and its effect on drift-variance.

**Table 2.**
 Survival data for lifespan of RNA-seq experimental cohorts.


<table>
  <thead>
    <tr>
      <th>Strain</th>
      <th>Treatment</th>
      <th>Treatment added on [day]</th>
      <th>Conc. [µM]</th>
      <th>Change in lifespan [%] Expt.1/ Expt.2/ Expt.3</th>
      <th>P-value Expt.1/ Expt.2/ Expt.3</th>
      <th>Mean Lifespan [days] Expt.1/ Expt.2/ Expt.3</th>
      <th>Number of animals Expt.1/ Expt.2/ Expt.3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>N2</td>
      <td>Water</td>
      <td>d1</td>
      <td>0</td>
      <td></td>
      <td></td>
      <td>19.33/ 17.2/ 20.45</td>
      <td>132/ 149/ 130</td>
    </tr>
    <tr>
      <td>N2</td>
      <td>Mia</td>
      <td>d1</td>
      <td>2</td>
      <td>+7/ +12/ -4</td>
      <td>0.20/ 0.04/ 0.25</td>
      <td>20.64/ 19.23/ 19.67</td>
      <td>125/ 133/ 151</td>
    </tr>
    <tr>
      <td>N2</td>
      <td>Mia</td>
      <td>d1</td>
      <td>10</td>
      <td>+30/ +16/ +6</td>
      <td>2.5E-07/ 3.7E-03/ 0.55</td>
      <td>25.09/ 19.92/ 21.74</td>
      <td>94/ 138/ 136</td>
    </tr>
    <tr>
      <td>N2</td>
      <td>Mia</td>
      <td>d1</td>
      <td>50</td>
      <td>+46/ +39/ +25</td>
      <td>1.1E-19/ 1.9E-15/ 2.8E-08</td>
      <td>28.25/ 23.92/ 25.63</td>
      <td>95/ 131/ 125</td>
    </tr>
    <tr>
      <td>N2</td>
      <td>Mia</td>
      <td>d3</td>
      <td>50</td>
      <td>+15/ +14/ +1</td>
      <td>2.0E-03/ 9.3E-04/ 0.29</td>
      <td>22.23/ 19.69/ 20.75</td>
      <td>121/ 134/ 152</td>
    </tr>
    <tr>
      <td>N2</td>
      <td>Mia</td>
      <td>d5</td>
      <td>50</td>
      <td>-8/ +8/ -2</td>
      <td>0.18/ 0.06/ 0.84</td>
      <td>17.79/ 18.52/ 20.13</td>
      <td>123/ 151/ 139</td>
    </tr>
  </tbody>
</table>

_Summary of all lifespan experiments performed in parallel for cohorts 1 and 2 of the RNA-seq studies in Figure 2c,e. The treatments, water or mianserin, at the indicated concentrations (conc.) were added on indicated day (D) of adulthood and lifespan (days) was scored until 95% of animals were dead in all tested conditions. All values (Change in lifespan [%], P-values) were calculated for the pairwise comparison between mianserin-treated and water-treated animals of the same condition, in 3 independent experiments (expts.). Statistical analysis was performed using the Mantel–Haenszel version of the log-rank test. Mean lifespan [days] and number of animals in each experiment are indicated._

Our previous studies had also shown that mianserin does not extend lifespan when added to 5-day-old post-reproductive adult animals (Petrascheck et al., 2007). Thus, we next tested whether mianserin attenuates transcriptional drift-variance independently of longevity by treating older animals. Mianserin did not attenuate transcriptional drift-variance when added on day 5 (Figure 2d). Adding mianserin on day 3 of adulthood caused a small extension of lifespan and a corresponding small attenuation of drift-variance, further supporting a quantitative relationship between suppression of drift-variance and extension of lifespan (Figure 1a, cohort #3, Figure 2d,e; Table 2). However, mianserin fully induced the xenobiotic response by up to 1,000-fold irrespective of whether added on day 1 or day 5 (Figure 2f). Therefore, the lack of an effect of mianserin when added to day 5 adults cannot be attributed to reduced drug uptake. Taken together, these results show that mianserin does not attenuate drift-variance when it does not extend lifespan.

We next asked whether the attenuation of drift-variance is unique to mianserin or whether it is observed in other lifespan-extension paradigms (Figure 2g). We asked whether reduced insulin signaling also attenuates drift-variance by analyzing the previously published gene expression data-sets of long-lived C. elegans daf-2 RNAi-treated and vector control animals (Murphy et al., 2003). Analyses of drift-variance for these data-sets showed that treatment with daf-2 RNAi attenuated drift-variance (Figure 2g). Moreover, mianserin and daf-2 RNAi attenuated age-associated drift of overlapping sets of genes. Of the 6,958 genes for which expression levels were detected at all ages in both data-sets, 58% (4,078 genes, binomial P= 6.3e-47) were attenuated by both longevity-extending mechanisms. This overlap is consistent with experiments showing that these two longevity mechanisms partially overlap, potentially explaining why mianserin only causes a +11% lifespan extension in daf-2(e1370) mutant animals instead of 31% seen in the parallel wild-type experiments (Petrascheck et al., 2007). Thus, lifespan extension by mianserin or daf-2 RNAi attenuates transcriptional drift in overlapping sets of genes.

Conversely, suppressing longevity by daf-16(RNAi) prevented the attenuation of drift-variance by daf-2(RNAi) and increased it beyond what was seen in control animals (Figure 2g). Thus, the activation of DAF-16 target genes leads to the attenuation of transcriptional drift in thousands of genes across the transcriptome. Taken together, these results show that drift-variances increase with age in C. elegans and are attenuated in two different longevity paradigms (Figure 2a,g).

From a technical perspective, the comparison between the mianserin data and the Murphy data (Murphy et al., 2003) also shows that the phenomenon of transcriptional drift is robust enough not to be influenced by the presence of eggs in the animals or the method of sterilization, as our study used FUDR and the Murphy et al. (2003) study used sterile mutants (Figure 2a,g; Figure 2—figure supplement 2).

### Attenuating drift-variances in redox-pathways preserves homeostatic capacity

The results above suggested that preserving low drift-variance in transcriptomes preserves longevity. We therefore asked whether attenuating drift-variance in specific pathways preserves homeostatic capacity, the ability of pathways to appropriately respond to a stimulus or stress. Throughout life, organisms respond to stimuli by activating or repressing transcriptional programs, an ability that is lost with age. We hypothesized that one way by which regulatory ability may be lost could be due to a failure to return to their precise steady-state transcriptional levels after stimulation. This would give rise to increases in drift-variance (Figure 3a), as seen in the drift plots for oxidative phosphorylation or lysosome biology (Figure 1h,i). In this model, slight initial deviations in gene expression levels would be compounded over time resulting in imbalanced stoichiometries between pathway components resulting in functional decline with age (Figure 3a).

![Figure 3.](https://cdn.elifesciences.org/articles/08833/elife-08833-fig3-v2.jpg)

**Figure 3.:** (a) Model for the occurrence of transcriptional drift with age. Genes belonging to the same pathway appropriately respond to a stimulus but subsequently fail to return to steady-state levels. Repeated stimuli compound this effect leading to increases in transcriptional drift. If multiple genes within a pathway have propensity to drift in one or the other direction drift-variance increases with age. (b) Drift-plots show increases in drift-variance in multiple KEGG or GO annotations associated with redox processes. P-values compare variance, not mean, n: No. of genes in each category. *P<0.05, **P<0.01, ***P<0.001, Levene’s test. Error bars; drift-variance (c) Fold increase in survival of N2 wild-type (wt) mianserin treated vs. untreated animals when challenged with paraquat at different ages. The protective effect of mianserin increases with age. *P<0.05, t-test, Error bars: S.E.M. (d) Fold increase in survival of wt (N2) treated vs. untreated animals when challenged with paraquat on day 10. Delaying mianserin treatment into later life reduces its protective effect. *P<0.05, t-test, Error bars: S.E.M. (e) Linear regression of log fold-changes in gene expression with age for genes previously shown to change upon oxidative stress. Genes upregulated in response to oxidative stress (n=252) increase with age, and genes downregulated in response to oxidative stress decrease (n=88) with age. Mianserin attenuates age-associated expression changes in oxidative stress genes in the direction indicated by blue arrows. Shading: 95% confidence interval. ***P<0.001, Wilcoxon rank-sum test. See Tables 3–5 for detailed statistics and Methods section for transcriptional drift calculation in each figure panel.

![Figure 4.](https://cdn.elifesciences.org/articles/08833/elife-08833-fig4-v2.jpg)

**Figure 4.:** (a) Survival of wt (dotted lines) or serotonin receptor mutants and serotonin synthesis mutant (bold lines) treated with water (black) or mianserin (blue) on day 1, followed by increasing concentrations of paraquat on day 5. (b) Bar graph shows fold protection as a ratio of survival of mianserin-treated vs. water-treated GPCR mutant animals ((Mia/water)-1). *P<0.05, **P<0.01, ***P<0.001, n.s., not significant, t-test; Error bars: S.E.M. See Figure 4—figure supplement 1, and Tables 6 and 7 for detailed statistics.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/08833/elife-08833-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (a) Survival of wt and two independent alleles of ser-5 mutants, ser-5(tm2647) or ser-5(tm2654), treated with water or mianserin on day 1, followed by increasing concentrations of paraquat on day 5 of adulthood. (b) Hierarchical clustering of fold change [serotonin antagonist/DMSO] in protection of wt (N2) and ser-5 mutant animals, when treated with DMSO or serotonin antagonists on day 1 followed by paraquat on day 5, shows the degree of similarity in protection between 8 structurally different serotonin antagonists (left) and the requirement of ser-5 for these antagonists to protect from oxidative stress. (c) Bar graphs quantifying transcriptional drift by qRT-PCR (log fold-changes in gene expression) in 5-day-old N2 and ser-3(ad1774) animals (left panel), and N2 and ser-4(ok512) animals (right panel) treated with mianserin, relative to water-treated N2, determined by qRT-PCR. Mianserin treatment of ser-3(ad1774) and ser-4(ok512) strains result in a drift pattern, similar to those seen in N2. Thus, these receptors are neither required for drift-attenuation in redox genes, nor for the age-associated increase in oxidative stress resistance (Figure 4). Error bars: S.E.M. For detailed statistics, see Tables 6 and 7.

![Figure 5.](https://cdn.elifesciences.org/articles/08833/elife-08833-fig5-v2.jpg)

**Figure 5.:** (a) Bar graphs quantifying transcriptional drift (log fold-changes in gene expression) as measured by qRT-PCR in 5-day-old N2 and ser-5(ok3087) animals treated with mianserin, relative to water-treated N2. Mianserin treatment increases expression of genes drifting down with age and decreases expression of genes drifting up with age in N2, but not in ser-5(ok3087) mutants. (See 5b). *P<0.05, **P<0.01, ***P<0.001,t-test; Error bars: S.E.M. (b) Log fold-change in gene expression as a function of age for stress response genes shown in a. Blue arrows indicate how mianserin treatment corrects age-associated changes in gene expression toward an expression pattern as seen in young adults. (c) Bar graphs quantifying log fold-changes in gene expression in 1-day-old N2 and ser-5(ok3087) animals treated with paraquat, relative to water-treated N2 animals. N2 and ser-5(ok3087) show an identical response to paraquat. (d) Mianserin treatment on day 1 of adulthood enhances transcription of sod and hsp-16.x genes in response to an 8h paraquat treatment on day 5 in wt (N2) animals compared to water treated controls. In contrast, mianserin treatment of ser-5(ok3087) animals did not enhance transcription of sod and hsp-16.x genes. mRNA levels of genes were evaluated by qRT-PCR and plotted as fold induction (PQ/water) (Y-axis) for each gene. (e) Survival plot of mianserin-treated and untreated N2 and ser-5(ok3087) animals. ***P<0.001, *P<0.05, Mantel–Haenszel version of the log-rank test. f) Percent increase in lifespan as a function of mianserin concentration. Mutations in ser-5 or synaptic components rendered the animals partially or completely resistant to mianserin-induced lifespan extension. See Figure 5—figure supplement 1 for additional data, and Table 8 for detailed statistics.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/08833/elife-08833-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (a) Kaplan-Meier graphs for lifespan of wt (dotted line) and synaptic mutant animals treated with water (black) or mianserin (blue). Synaptic transmission is required for mianserin-induced lifespan extension. For detailed statistics, see Table 8. (b) Kaplan-Meier graphs for lifespan of wt (dotted lines), ser-5(ok3087), (solid lines) treated with DMSO or serotonin antagonists namely: Dihydroergotamine, Metergoline, Amperozide, Methiothepin, Ketanserin, Mirtazapine, LY-165,163/PAPP or mianserin, on day 1 of adulthood. All 8 serotonergic antagonists completely or partially depend on ser-5.

![Figure 6.](https://cdn.elifesciences.org/articles/08833/elife-08833-fig6-v2.jpg)

**Figure 6.:** (a) PCA plot of RNA-seq data. Each circle represents one RNA-seq sample with the age, in days, indicated. Mianserin-treated day 10 samples show the same transcriptional age as untreated day 3 animals, dotted red line. (b) Mortality curves (moving average) constructed using Gompertz equation for lifespan experiments from 15 independent experiments of ~100 animals each treated with water or mianserin 50 µM (n>1500 total for each condition). Mianserin treatment causes a 7–8 day parallel shift in log mortality as compared to the water-treated animals. (c) Survival of wt animals treated with mianserin for 8 hr, 1 day, 5 days or throughout life was determined and compared to water treated control animals. Removing mianserin after 8 hr or 1 day lessens its effect on lifespan, while removing mianserin on day 5 or maintaining treatment throughout life showed a comparable effect. (d) Mean survival of wt animals treated with water or mianserin for 8 hr, 1 day, 5, 10, 15 days or throughout life was plotted as a function of mianserin exposure in days. Mianserin treatment for 5 to 10 days was required and sufficient for an optimal lifespan extension. (e) Distinct modes of lifespan extension: Proportional lifespan extension leads to a proportional extension across life whereas period-specific lifespan extension leads to a reduced rate of age-associated degeneration during a specific period only. Mianserin reduces the rate of age-associated changes in early adulthood, thereby postponing mortality levels by 7–8 days causing a ‘period-specific lifespan extension’. (f) Model for how mianserin modulates age-associated mortality in early adulthood. Blocking serotonergic signaling via SER-5 decreases transcriptional drift-variance with age in redox genes, leading to preserved homeostatic capacity in redox function, which subsequently delays age-associated mortality. (g) Mianserin does not affect reproductive longevity. Wt animals were treated with water or mianserin (50 µM) on day 1 followed by counting the number of viable eggs laid by them on day 1, day 2, day 3 and day 4. h) Chymotrypsin-like 26S proteasome activity measured from wt animals treated with water or mianserin (50 µM) on day 1 followed by proteasome activity assay on day 2 (upper panel) or day 5 (lower panel). Mianserin treatment does not lead to an increase in proteasome activity, unlike long lived germline-less animals. Error bars S.E.M. See Figure 6—figure supplement 1 for additional data and detailed statistics.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/08833/elife-08833-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** (a) Mortality curves constructed using Gompertz equation for lifespan experiments of wt (N2) animals from 15 independent experiments of ~100 animals each treated with water or mianserin 50 µM (n>1500 total for each condition). The shift in log mortality as a function of time with mianserin treatment is parallel to the water-treated animals. See table below for aggregate data showing hazard/mortality for water and mianserin treatment. (b) Power of detection for 500, 1000 and 1500 animals in each cohort as used in Figure 6b (α=0.01). Monte-Carlo simulations based on a parametric model derived from our data were used to determine the power of detection. A lifespan extension of 1 day corresponds to a 5% increase in lifespan. (c) Drift-plots show changes in drift-variance in proteasome pathway (KEGG annotation: 03050) associated with 38 genes involved in proteasome activity in animals treated with water or mianserin (50 µM) on day 1 and harvested on day 3, 5 and 10. Attenuation patterns of drift-variance with mianserin treatment corresponds functionally to changes in proteasome activity on day 2 and day 5 (See panel a). Mianserin slightly increases transcriptional drift on day 5 and slightly reduces proteasome activity function. P-values compare variance, not mean, **P<0.01, Levene’s test. Error bars; drift-variance.

![Figure 7.](https://cdn.elifesciences.org/articles/08833/elife-08833-fig7-v2.jpg)

**Figure 7.:** (a) Transcriptional drift-variance in gene expression from different mouse tissues aged 13 to 130 weeks. Drift-plots show an increase in drift-variance with age in mouse brain, kidney, liver, lung and spleen (b) Drift-variance plotted as a function of age for different organs. To obtain drift-variance values for young animals, a single transcriptome was set aside and used a reference. (c) Drift-plot for gene expression from 32 human brains (frontal cortex) plotted as a function of age in years. Data binned in 20-year increments. (d) Drift-variance plotted as a function of age in years for individuals. Each dot corresponds to one brain sample (frontal cortex). Shading indicates 95% confidence interval (ρ=0.603, P=0.0014). (e) Drift plots show a higher transcriptional drift-variance in BJ fibroblasts (BJ) and fibroblasts from Hutchinson Gilford progeria syndrome (HGPS), when compared to H9 embryonic stem cells. Reprogramming the BJ and HGPS cells to induced pluripotent stem cells (iPSCs) leads to a partial reversal of the transcriptional drift-variance to a lower variance corresponding to the young phenotype of the iPSCs. See Figure 2—figure supplement 1 for additional information on transcriptional drift calculation, and Methods section for transcriptional drift calculation in each figure panel.

Our previous studies showed that mianserin protected C. elegans from oxidative stress by a neuronal mechanism that modulated peripheral stress response genes (NEUROX) (Rangaraju et al., 2015a). We therefore constructed drift plots for redox-associated pathways that showed that mianserin indeed increased the overall expression of oxidative stress response genes (type I) relative to age-matched controls but also attenuated transcriptional drift (type II) (Figure 3b; Table 3).

**Table 3.**
 Gene ontology (GO) pathways of relevance to this study that are differentially regulated by mianserin.


<table>
  <thead>
    <tr>
      <th>KEGG / GO ID</th>
      <th>KEGG / GO Term</th>
      <th>Number of Genes observed</th>
      <th>Levene’s test for variance (Difference in transcriptional drift- variance) Water D1 vs. water Dx</th>
      <th>Levene’s test for variance (Difference in transcriptional drift- variance) water Dy vs. mianserin Dy</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Transcriptome</td>
      <td></td>
      <td>19,196</td>
      <td>D3 : P &lt; 1.0E-100 D5 : P &lt; 1.0E-100 D10: P &lt; 1.0E-100</td>
      <td>D3 : P &lt; 1.0E-100 D5 : P &lt; 1.0E-100 D10: P &lt; 1.0E-100</td>
    </tr>
    <tr>
      <td>KEGG:Cel00030</td>
      <td>Pentose phosphate pathway</td>
      <td>17</td>
      <td>D3 : P = 0.0096 D10: P &lt;1.0E-5</td>
      <td>D3 : P &lt;1.0E-4 D10: P = 0.01</td>
    </tr>
    <tr>
      <td>GO: 0006979</td>
      <td>Response to oxidative stress</td>
      <td>67</td>
      <td>D3 : P &lt;1.0E-10 D10: P &lt;1.0E-16</td>
      <td>D3 : P &lt;1.0E-4 D10: P = 0.001</td>
    </tr>
    <tr>
      <td>GO: 0045454</td>
      <td>Cell redox homeostasis</td>
      <td>52</td>
      <td>D3 : P &lt;1.0E-6 D10: P &lt;1.0E-10</td>
      <td>D3 : P &lt;1.0E-4 D10: P = 0.029</td>
    </tr>
    <tr>
      <td>GO: 006749</td>
      <td>Glutathione metabolism</td>
      <td>13</td>
      <td>D3 : P &lt;1.0E-4 D10: P &lt;1.0E-7</td>
      <td>D3 : P =0.041 D10: P &lt;1.0E-4</td>
    </tr>
    <tr>
      <td>GO: 0007186</td>
      <td>G-protein coupled receptor signaling</td>
      <td>335</td>
      <td>D3 : P &lt;1.0E-24 D10: P &lt; 1.0E-100</td>
      <td>D3 : P &lt;1.0E-4 D10: P &lt;1.0E-4</td>
    </tr>
    <tr>
      <td>GO: 0016209</td>
      <td>Antioxidant activity</td>
      <td>34</td>
      <td>D3 : P &lt;1.0E-8 D10: P &lt;1.0E-10</td>
      <td>D3 : P = 0.002 D10: P = 0.06</td>
    </tr>
  </tbody>
</table>

_Summary of gene changes with RNA-seq transcriptome analysis in Figure 3b.GO ID is the Gene Ontology identification number.GO Term is the Gene Ontology term for the biological process.Dx = age in days for the animals indicated, compared with D1 water-treated animals.Dy = age in days for water- and mianserin-treated animals, compared on the same day of age indicated._

We therefore asked whether mianserin treatment increased resistance to oxidative stress by either directly activating the oxidative stress response or whether attenuating transcriptional drift would preserve homeostatic capacity into older age (Rahman et al., 2013). Animals were treated with water or mianserin on day 1 of adulthood, followed by treatment with the reactive oxygen species (ROS) generator paraquat on day 3, 5, or 10 (Figure 3c). On day 3 of adulthood, no difference in stress resistance between mianserin-treated and untreated animals was observed. As animals grew older (day 5 and day 10), mianserin treatment greatly improved stress resistance (Figure 3c; Table 4). Again, as with lifespan, delaying the start of mianserin treatment to day 3 and day 5 progressively reduced its protective effect on stress resistance, this time measured in animals subjected to paraquat on day 10 of adulthood (Figure 3d; Table 5). Thus, mianserin treatment specifically improves stress resistance in older (day 5 and day 10) but not in younger (day 3) animals consistent with a model in which it preserves the homeostatic capacity of redox function.

**Table 4.**
 Survival data for paraquat stress resistance assays.


<table>
  <thead>
    <tr>
      <th>Strain</th>
      <th>Treatment</th>
      <th>Conc.[µM]</th>
      <th>Treatment added [day]</th>
      <th>PQ 100 mM, added [day]</th>
      <th>Survival after PQ [%] (expt. 1)</th>
      <th>Survival after PQ [%] (expt. 2)</th>
      <th>Survival after PQ [%] (expt. 3)</th>
      <th>Mean, Survival after PQ [%]</th>
      <th>S.D., Survival after PQ [%]</th>
      <th>P-value</th>
      <th>No. of wells</th>
      <th>Total no. of animals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>N2</td>
      <td>Water</td>
      <td>0</td>
      <td>d1</td>
      <td>d3</td>
      <td>70.0</td>
      <td>43.1</td>
      <td>62.2</td>
      <td>58.4</td>
      <td>13.9</td>
      <td></td>
      <td>48</td>
      <td>450</td>
    </tr>
    <tr>
      <td>N2</td>
      <td>Mia</td>
      <td>50</td>
      <td>d1</td>
      <td>d3</td>
      <td>87.3</td>
      <td>47.9</td>
      <td>53.9</td>
      <td>63.0</td>
      <td>21.3</td>
      <td>7.72E-01</td>
      <td>48</td>
      <td>390</td>
    </tr>
    <tr>
      <td>N2</td>
      <td>Water</td>
      <td>0</td>
      <td>d1</td>
      <td>d5</td>
      <td>55.8</td>
      <td>56.2</td>
      <td>66.1</td>
      <td>59.3</td>
      <td>5.8</td>
      <td></td>
      <td>48</td>
      <td>436</td>
    </tr>
    <tr>
      <td>N2</td>
      <td>Mia</td>
      <td>50</td>
      <td>d1</td>
      <td>d5</td>
      <td>95.5</td>
      <td>96.1</td>
      <td>92.0</td>
      <td>94.5</td>
      <td>2.2</td>
      <td>4.24E-03</td>
      <td>48</td>
      <td>435</td>
    </tr>
    <tr>
      <td>N2</td>
      <td>Water</td>
      <td>0</td>
      <td>d1</td>
      <td>d10</td>
      <td>63.3</td>
      <td>37.4</td>
      <td>41.7</td>
      <td>47.5</td>
      <td>13.9</td>
      <td></td>
      <td>48</td>
      <td>400</td>
    </tr>
    <tr>
      <td>N2</td>
      <td>Mia</td>
      <td>50</td>
      <td>d1</td>
      <td>d10</td>
      <td>91.9</td>
      <td>82.1</td>
      <td>85.4</td>
      <td>86.4</td>
      <td>5.0</td>
      <td>2.85E-02</td>
      <td>48</td>
      <td>390</td>
    </tr>
  </tbody>
</table>

_Summary of all stress resistance assays performed in Figure 3c. The treatments, water or mianserin (Mia), at the indicated concentrations (conc.) were added on day 1 of adulthood. Paraquat (PQ) was added to a final conc. of 100 mM on day 3 (d3), day 5 (d5) or day 10 (d10) and survival after PQ [%] was calculated 24 hr after the respective PQ addition. Mean and standard deviation (S.D.) of survival after PQ [%] were calculated from 3 independent experiments (expts.). P-values were calculated between water and mianserin-treatments on the same day of PQ addition, using unpaired t-test. The total number of wells and animals from which data were collected are indicated._

**Table 5.**
 Survival data for paraquat stress resistance assays, mianserin added on different days.


<table>
  <thead>
    <tr>
      <th>Strain</th>
      <th>Treatment</th>
      <th>Conc. [µM]</th>
      <th>Treatment added day</th>
      <th>PQ 100 mM, added day</th>
      <th>Survival [%] (expt. 1)</th>
      <th>Survival [%] (expt. 2)</th>
      <th>Survival [%] (expt. 3)</th>
      <th>Mean, Survival [%]</th>
      <th>S.D., Survival [%]</th>
      <th>P-value</th>
      <th>No. of wells</th>
      <th>Total no. of animals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>N2</td>
      <td>Water</td>
      <td>0</td>
      <td>d1</td>
      <td>d10</td>
      <td>63.30</td>
      <td>37.44</td>
      <td>41.72</td>
      <td>47.48</td>
      <td>13.86</td>
      <td></td>
      <td>48</td>
      <td>400</td>
    </tr>
    <tr>
      <td>N2</td>
      <td>Mia</td>
      <td>50</td>
      <td>d1</td>
      <td>d10</td>
      <td>91.85</td>
      <td>82.05</td>
      <td>85.38</td>
      <td>86.43</td>
      <td>4.97</td>
      <td>2.85E-02</td>
      <td>48</td>
      <td>390</td>
    </tr>
    <tr>
      <td>N2</td>
      <td>Water</td>
      <td>0</td>
      <td>d3</td>
      <td>d10</td>
      <td>63.97</td>
      <td>41.25</td>
      <td>38.35</td>
      <td>47.85</td>
      <td>14.02</td>
      <td></td>
      <td>48</td>
      <td>403</td>
    </tr>
    <tr>
      <td>N2</td>
      <td>Mia</td>
      <td>50</td>
      <td>d3</td>
      <td>d10</td>
      <td>78.52</td>
      <td>66.22</td>
      <td>73.62</td>
      <td>72.79</td>
      <td>6.19</td>
      <td>0.074</td>
      <td>48</td>
      <td>378</td>
    </tr>
    <tr>
      <td>N2</td>
      <td>Water</td>
      <td>0</td>
      <td>d5</td>
      <td>d10</td>
      <td>57.31</td>
      <td>43.83</td>
      <td>42.57</td>
      <td>47.90</td>
      <td>8.16</td>
      <td></td>
      <td>48</td>
      <td>387</td>
    </tr>
    <tr>
      <td>N2</td>
      <td>Mia</td>
      <td>50</td>
      <td>d5</td>
      <td>d10</td>
      <td>68.63</td>
      <td>50.58</td>
      <td>58.62</td>
      <td>59.28</td>
      <td>9.04</td>
      <td>0.18</td>
      <td>48</td>
      <td>398</td>
    </tr>
  </tbody>
</table>

_Summary of all stress resistance assays performed in Figure 3d. The treatments, water or mianserin (Mia), at the indicated concentrations (conc.) were added on day 1 (D1), day 3 (D3) or day 5 (D5) of adulthood. 100mM Paraquat (PQ) was added on day 10 (D10) and survival [%] was calculated after 24 hr. Mean and standard deviation (S.D) of survival [%] were calculated from 3 independent experiments (expts.). P-value calculated between water and mianserin-treatments using t-test. The total number of wells and animals from which data were collected are indicated._

To further distinguish between a model in which mianserin directly activates an oxidative stress response from one that preserves the homeostatic capacity by attenuating drift-variance, we asked whether mianserin enhanced (direct activation) or attenuated (preserving capacity) genes that change in response to oxidative stress (Figure 3e). Oliveira et al. identified 252 genes that were upregulated and 88 genes that were downregulated in young C. elegans in response to oxidative stress, and can therefore be considered an experimentally determined oxidative stress signature (Oliveira et al., 2009). We hypothesized that a direct activation of the oxidative stress response by mianserin would mimic the increase in expression of the 252 genes and the decrease in the expression of the 88 genes as seen in response to oxidative stress. However, we observed an attenuation rather than an activation of the oxidative stress signatures, consistent with preserving homeostatic capacity rather than a direct activation. Genes that increased in response to oxidative stress (252) showed a lower expression while genes that decreased (88) in response to oxidative stress showed a higher expression in age-matched mianserin-treated animals (Figure 3e). Consistent with the functional data, differences in the oxidative stress signature were only observed in older animals (day 5, 10), but not in younger day 3 animals. These results are consistent with a model in which mianserin treatment preserves the redox system from age-associated decline, thus improving redox capacity in older age.

### Mianserin requires the serotonin receptor SER-5 to preserve low drift-variances

In mammals, mianserin antagonizes serotonergic signals sent by 5-HT2A/C receptors (Gillman, 2006). We next asked whether preservation of redox capacity and reducing drift-variance in redox pathways by mianserin depends on serotonergic signaling. To identify the serotonergic receptor, we treated multiple mutants, each deficient in signaling by a single G-protein coupled receptor (GPCR) with mianserin on day 1, followed by increasing concentrations of paraquat on day 5 to induce oxidative stress (Figure 4a,b; Table 6). Mianserin was unable to protect multiple ser-5 mutant alleles (ok3087, tm2647, tm2654) from oxidative stress (Figure 4a,b; Figure 4—figure supplement 1a; Table 6). In addition, seven structurally distinct serotonergic antagonists/inverse agonists also protect from oxidative stress in a ser-5 dependent manner (Figure 4—figure supplement 1b; Table 7). Furthermore, mianserin did not protect animals unable to synthesize serotonin (tph-1(mg280)) (Figure 4a; Table 6) (Sze et al., 2000).

**Table 6.**
 Survival data for paraquat stress resistance assays.


<table>
  <thead>
    <tr>
      <th>Strain</th>
      <th>Treatment</th>
      <th>Conc. [µM]</th>
      <th>PQ conc. [mM]</th>
      <th>Survival after PQ [%] (expt. 1)</th>
      <th>Survival after PQ [%] (expt. 2)</th>
      <th>Survival after PQ [%] (expt. 3)</th>
      <th>Survival after PQ [%] (expt. 4)</th>
      <th>Survival after PQ [%] (expt. 5)</th>
      <th>Survival after PQ [%] (expt. 6)</th>
      <th>Mean, Survival after PQ [%]</th>
      <th>S.D., Survival after PQ [%]</th>
      <th>P-value</th>
      <th>No. of wells</th>
      <th>Total no. of animals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="12">N2</td>
      <td>Water</td>
      <td>0</td>
      <td>0</td>
      <td>89.9</td>
      <td>98.9</td>
      <td>95.8</td>
      <td>98.2</td>
      <td>93.9</td>
      <td>93.2</td>
      <td>95.0</td>
      <td>3.4</td>
      <td></td>
      <td>48</td>
      <td>548</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>15</td>
      <td>76.4</td>
      <td>88</td>
      <td>82</td>
      <td>95.3</td>
      <td>95.5</td>
      <td>91.7</td>
      <td>88.2</td>
      <td>7.7</td>
      <td></td>
      <td>48</td>
      <td>578</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>25</td>
      <td>74.2</td>
      <td>91.3</td>
      <td>80</td>
      <td>92.9</td>
      <td>85.1</td>
      <td>80.4</td>
      <td>84.0</td>
      <td>7.2</td>
      <td></td>
      <td>48</td>
      <td>531</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>50</td>
      <td>66.2</td>
      <td>67.8</td>
      <td>63.8</td>
      <td>81.9</td>
      <td>61.6</td>
      <td>67.8</td>
      <td>68.2</td>
      <td>7.1</td>
      <td></td>
      <td>48</td>
      <td>530</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>75</td>
      <td>50.1</td>
      <td>61.1</td>
      <td>44.1</td>
      <td>64.6</td>
      <td>42.4</td>
      <td>51.8</td>
      <td>52.4</td>
      <td>8.9</td>
      <td></td>
      <td>48</td>
      <td>545</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>100</td>
      <td>36.2</td>
      <td>34.4</td>
      <td>35.5</td>
      <td>53.5</td>
      <td>23</td>
      <td>54.7</td>
      <td>39.6</td>
      <td>12.3</td>
      <td></td>
      <td>48</td>
      <td>503</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>0</td>
      <td>100</td>
      <td>100</td>
      <td>99.5</td>
      <td>100</td>
      <td>100</td>
      <td>99.2</td>
      <td>99.8</td>
      <td>0.3</td>
      <td>1.71E-02</td>
      <td>48</td>
      <td>556</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>15</td>
      <td>100</td>
      <td>98.2</td>
      <td>87.6</td>
      <td>100</td>
      <td>98.8</td>
      <td>100</td>
      <td>97.4</td>
      <td>4.9</td>
      <td>3.52E-02</td>
      <td>48</td>
      <td>523</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>25</td>
      <td>96.2</td>
      <td>98.8</td>
      <td>95</td>
      <td>98.4</td>
      <td>100</td>
      <td>98.2</td>
      <td>97.8</td>
      <td>1.8</td>
      <td>4.54E-03</td>
      <td>48</td>
      <td>529</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>50</td>
      <td>95</td>
      <td>95.9</td>
      <td>94.5</td>
      <td>95.3</td>
      <td>99</td>
      <td>98.2</td>
      <td>96.3</td>
      <td>1.8</td>
      <td>1.19E-04</td>
      <td>48</td>
      <td>536</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>75</td>
      <td>98.9</td>
      <td>89.3</td>
      <td>89.4</td>
      <td>92.6</td>
      <td>97.5</td>
      <td>98.1</td>
      <td>94.3</td>
      <td>4.4</td>
      <td>1.29E-05</td>
      <td>48</td>
      <td>516</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>100</td>
      <td>97.6</td>
      <td>90.8</td>
      <td>90.7</td>
      <td>69.8</td>
      <td>93.9</td>
      <td>95.6</td>
      <td>89.7</td>
      <td>10.1</td>
      <td>1.95E-05</td>
      <td>48</td>
      <td>539</td>
    </tr>
    <tr>
      <td rowspan="12">ser-1 (ok345)</td>
      <td>Water</td>
      <td>0</td>
      <td>0</td>
      <td>92</td>
      <td>71.3</td>
      <td>89.2</td>
      <td></td>
      <td></td>
      <td></td>
      <td>84.2</td>
      <td>11.2</td>
      <td></td>
      <td>24</td>
      <td>228</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>15</td>
      <td>73.3</td>
      <td>57.9</td>
      <td>81.8</td>
      <td></td>
      <td></td>
      <td></td>
      <td>71.0</td>
      <td>12.1</td>
      <td></td>
      <td>24</td>
      <td>187</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>25</td>
      <td>71.3</td>
      <td>55.9</td>
      <td>67.8</td>
      <td></td>
      <td></td>
      <td></td>
      <td>65.0</td>
      <td>8.1</td>
      <td></td>
      <td>24</td>
      <td>209</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>50</td>
      <td>54.8</td>
      <td>46.4</td>
      <td>42.6</td>
      <td></td>
      <td></td>
      <td></td>
      <td>47.9</td>
      <td>6.2</td>
      <td></td>
      <td>24</td>
      <td>213</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>75</td>
      <td>39.4</td>
      <td>56.3</td>
      <td>50.7</td>
      <td></td>
      <td></td>
      <td></td>
      <td>48.8</td>
      <td>8.6</td>
      <td></td>
      <td>24</td>
      <td>213</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>100</td>
      <td>24.2</td>
      <td>27.3</td>
      <td>46.6</td>
      <td></td>
      <td></td>
      <td></td>
      <td>32.7</td>
      <td>12.1</td>
      <td></td>
      <td>24</td>
      <td>224</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>0</td>
      <td>100</td>
      <td>100</td>
      <td>100</td>
      <td></td>
      <td></td>
      <td></td>
      <td>100</td>
      <td>0.0</td>
      <td>0.13</td>
      <td>24</td>
      <td>215</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>15</td>
      <td>98.8</td>
      <td>97.7</td>
      <td>97.6</td>
      <td></td>
      <td></td>
      <td></td>
      <td>98.0</td>
      <td>0.7</td>
      <td>0.06</td>
      <td>24</td>
      <td>211</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>25</td>
      <td>97.9</td>
      <td>94.2</td>
      <td>98.4</td>
      <td></td>
      <td></td>
      <td></td>
      <td>96.8</td>
      <td>2.3</td>
      <td>1.51E-02</td>
      <td>24</td>
      <td>194</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>50</td>
      <td>94.8</td>
      <td>95.4</td>
      <td>97</td>
      <td></td>
      <td></td>
      <td></td>
      <td>95.7</td>
      <td>1.1</td>
      <td>4.52E-03</td>
      <td>24</td>
      <td>224</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>75</td>
      <td>93.9</td>
      <td>89.9</td>
      <td>92.4</td>
      <td></td>
      <td></td>
      <td></td>
      <td>92.1</td>
      <td>2.0</td>
      <td>9.87E-03</td>
      <td>24</td>
      <td>232</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>100</td>
      <td>87.4</td>
      <td>89.6</td>
      <td>89.5</td>
      <td></td>
      <td></td>
      <td></td>
      <td>88.8</td>
      <td>1.2</td>
      <td>1.45E-02</td>
      <td>24</td>
      <td>234</td>
    </tr>
    <tr>
      <td rowspan="12">ser-2 (pk1357)</td>
      <td>Water</td>
      <td>0</td>
      <td>0</td>
      <td>100</td>
      <td>100</td>
      <td>95.5</td>
      <td>100</td>
      <td></td>
      <td></td>
      <td>98.9</td>
      <td>2.3</td>
      <td></td>
      <td>32</td>
      <td>278</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>15</td>
      <td>88</td>
      <td>97.5</td>
      <td>73.7</td>
      <td>92.2</td>
      <td></td>
      <td></td>
      <td>87.9</td>
      <td>10.2</td>
      <td></td>
      <td>32</td>
      <td>239</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>25</td>
      <td>90.3</td>
      <td>100</td>
      <td>83</td>
      <td>83.2</td>
      <td></td>
      <td></td>
      <td>89.1</td>
      <td>8.0</td>
      <td></td>
      <td>32</td>
      <td>206</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>50</td>
      <td>76.7</td>
      <td>87.2</td>
      <td>73.7</td>
      <td>62.7</td>
      <td></td>
      <td></td>
      <td>75.1</td>
      <td>10.1</td>
      <td></td>
      <td>32</td>
      <td>254</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>75</td>
      <td>73.9</td>
      <td>73.2</td>
      <td>65.2</td>
      <td>53</td>
      <td></td>
      <td></td>
      <td>66.3</td>
      <td>9.7</td>
      <td></td>
      <td>32</td>
      <td>220</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>100</td>
      <td>72</td>
      <td>59.6</td>
      <td>54.4</td>
      <td>47.7</td>
      <td></td>
      <td></td>
      <td>58.4</td>
      <td>10.3</td>
      <td></td>
      <td>32</td>
      <td>220</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>0</td>
      <td>98.9</td>
      <td>100</td>
      <td>100</td>
      <td>100</td>
      <td></td>
      <td></td>
      <td>99.7</td>
      <td>0.6</td>
      <td>0.51</td>
      <td>32</td>
      <td>231</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>15</td>
      <td>100</td>
      <td>100</td>
      <td>100</td>
      <td>100</td>
      <td></td>
      <td></td>
      <td>100</td>
      <td>0.0</td>
      <td>0.10</td>
      <td>32</td>
      <td>255</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>25</td>
      <td>98.9</td>
      <td>100</td>
      <td>98.9</td>
      <td>96.9</td>
      <td></td>
      <td></td>
      <td>98.7</td>
      <td>1.3</td>
      <td>0.10</td>
      <td>32</td>
      <td>228</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>50</td>
      <td>100</td>
      <td>100</td>
      <td>95.5</td>
      <td>96.9</td>
      <td></td>
      <td></td>
      <td>98.1</td>
      <td>2.3</td>
      <td>1.71E-02</td>
      <td>32</td>
      <td>243</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>75</td>
      <td>98.9</td>
      <td>95</td>
      <td>96.8</td>
      <td>91.8</td>
      <td></td>
      <td></td>
      <td>95.6</td>
      <td>3.0</td>
      <td>6.35E-03</td>
      <td>32</td>
      <td>245</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>100</td>
      <td>97</td>
      <td>88.7</td>
      <td>92.3</td>
      <td>95.4</td>
      <td></td>
      <td></td>
      <td>93.4</td>
      <td>3.7</td>
      <td>3.80E-03</td>
      <td>32</td>
      <td>210</td>
    </tr>
    <tr>
      <td rowspan="12">ser-3 (ad1774)</td>
      <td>Water</td>
      <td>0</td>
      <td>0</td>
      <td>100</td>
      <td>100</td>
      <td>92.6</td>
      <td></td>
      <td></td>
      <td></td>
      <td>97.5</td>
      <td>4.3</td>
      <td></td>
      <td>24</td>
      <td>176</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>15</td>
      <td>89</td>
      <td>88.5</td>
      <td>86.8</td>
      <td></td>
      <td></td>
      <td></td>
      <td>88.1</td>
      <td>1.2</td>
      <td></td>
      <td>24</td>
      <td>174</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>25</td>
      <td>90.5</td>
      <td>85.4</td>
      <td>85.2</td>
      <td></td>
      <td></td>
      <td></td>
      <td>87.0</td>
      <td>3.0</td>
      <td></td>
      <td>24</td>
      <td>216</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>50</td>
      <td>81.3</td>
      <td>74</td>
      <td>72.1</td>
      <td></td>
      <td></td>
      <td></td>
      <td>75.8</td>
      <td>4.9</td>
      <td></td>
      <td>24</td>
      <td>176</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>75</td>
      <td>70.8</td>
      <td>48.6</td>
      <td>58.9</td>
      <td></td>
      <td></td>
      <td></td>
      <td>59.4</td>
      <td>11.1</td>
      <td></td>
      <td>24</td>
      <td>169</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>100</td>
      <td>43.7</td>
      <td>46.5</td>
      <td>30.1</td>
      <td></td>
      <td></td>
      <td></td>
      <td>40.1</td>
      <td>8.8</td>
      <td></td>
      <td>24</td>
      <td>140</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>0</td>
      <td>98.2</td>
      <td>100</td>
      <td>95.8</td>
      <td></td>
      <td></td>
      <td></td>
      <td>98.0</td>
      <td>2.1</td>
      <td>0.88</td>
      <td>24</td>
      <td>176</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>15</td>
      <td>98.9</td>
      <td>100</td>
      <td>98.4</td>
      <td></td>
      <td></td>
      <td></td>
      <td>99.1</td>
      <td>0.8</td>
      <td>3.25E-04</td>
      <td>24</td>
      <td>228</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>25</td>
      <td>93.8</td>
      <td>100</td>
      <td>90.2</td>
      <td></td>
      <td></td>
      <td></td>
      <td>94.7</td>
      <td>5.0</td>
      <td>0.10</td>
      <td>24</td>
      <td>173</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>50</td>
      <td>98.1</td>
      <td>100</td>
      <td>93.8</td>
      <td></td>
      <td></td>
      <td></td>
      <td>97.3</td>
      <td>3.2</td>
      <td>4.97E-03</td>
      <td>24</td>
      <td>174</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>75</td>
      <td>92.4</td>
      <td>95</td>
      <td>91.8</td>
      <td></td>
      <td></td>
      <td></td>
      <td>93.1</td>
      <td>1.7</td>
      <td>3.20E-02</td>
      <td>24</td>
      <td>197</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>100</td>
      <td>93.4</td>
      <td>65.6</td>
      <td>82.8</td>
      <td></td>
      <td></td>
      <td></td>
      <td>80.6</td>
      <td>14.0</td>
      <td>1.92E-02</td>
      <td>24</td>
      <td>180</td>
    </tr>
    <tr>
      <td rowspan="12">ser-4 (ok512)water</td>
      <td></td>
      <td>0</td>
      <td>0</td>
      <td>100</td>
      <td>87.6</td>
      <td>100</td>
      <td>98.6</td>
      <td></td>
      <td></td>
      <td>96.6</td>
      <td>6.0</td>
      <td></td>
      <td>32</td>
      <td>249</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>15</td>
      <td>100</td>
      <td>72.6</td>
      <td>91.3</td>
      <td>84.4</td>
      <td></td>
      <td></td>
      <td>87.1</td>
      <td>11.6</td>
      <td></td>
      <td>32</td>
      <td>262</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>25</td>
      <td>98.2</td>
      <td>67.9</td>
      <td>72.5</td>
      <td>85.5</td>
      <td></td>
      <td></td>
      <td>81.0</td>
      <td>13.7</td>
      <td></td>
      <td>32</td>
      <td>224</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>50</td>
      <td>88</td>
      <td>67.1</td>
      <td>83.3</td>
      <td>63.5</td>
      <td></td>
      <td></td>
      <td>75.5</td>
      <td>12.0</td>
      <td></td>
      <td>32</td>
      <td>229</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>75</td>
      <td>69</td>
      <td>47.2</td>
      <td>75.8</td>
      <td>61.4</td>
      <td></td>
      <td></td>
      <td>63.4</td>
      <td>12.3</td>
      <td></td>
      <td>32</td>
      <td>225</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>100</td>
      <td>56.3</td>
      <td>48.3</td>
      <td>60</td>
      <td>43.2</td>
      <td></td>
      <td></td>
      <td>52.0</td>
      <td>7.6</td>
      <td></td>
      <td>32</td>
      <td>204</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>0</td>
      <td>100</td>
      <td>95.9</td>
      <td>100</td>
      <td>100</td>
      <td></td>
      <td></td>
      <td>99.0</td>
      <td>2.1</td>
      <td>0.49</td>
      <td>32</td>
      <td>212</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>15</td>
      <td>96.9</td>
      <td>97.2</td>
      <td>97.5</td>
      <td>97.7</td>
      <td></td>
      <td></td>
      <td>97.3</td>
      <td>0.4</td>
      <td>0.21</td>
      <td>32</td>
      <td>228</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>25</td>
      <td>97.5</td>
      <td>100</td>
      <td>91.7</td>
      <td>95.5</td>
      <td></td>
      <td></td>
      <td>96.2</td>
      <td>3.5</td>
      <td>0.11</td>
      <td>32</td>
      <td>230</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>50</td>
      <td>93.8</td>
      <td>96.8</td>
      <td>96.4</td>
      <td>95.3</td>
      <td></td>
      <td></td>
      <td>95.6</td>
      <td>1.3</td>
      <td>4.31E-02</td>
      <td>32</td>
      <td>261</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>75</td>
      <td>100</td>
      <td>91.5</td>
      <td>88.1</td>
      <td>96.5</td>
      <td></td>
      <td></td>
      <td>94.0</td>
      <td>5.3</td>
      <td>9.66E-03</td>
      <td>32</td>
      <td>227</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>100</td>
      <td>96.9</td>
      <td>86.5</td>
      <td>90.3</td>
      <td>89</td>
      <td></td>
      <td></td>
      <td>90.7</td>
      <td>4.4</td>
      <td>3.75E-04</td>
      <td>32</td>
      <td>252</td>
    </tr>
    <tr>
      <td rowspan="12">ser-5 (ok3087)</td>
      <td>Water</td>
      <td>0</td>
      <td>0</td>
      <td>98.8</td>
      <td>92.2</td>
      <td>99</td>
      <td></td>
      <td></td>
      <td></td>
      <td>96.7</td>
      <td>3.9</td>
      <td></td>
      <td>24</td>
      <td>206</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>15</td>
      <td>91.1</td>
      <td>83.6</td>
      <td>85.5</td>
      <td></td>
      <td></td>
      <td></td>
      <td>86.7</td>
      <td>3.9</td>
      <td></td>
      <td>24</td>
      <td>230</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>25</td>
      <td>86.2</td>
      <td>71.6</td>
      <td>88.2</td>
      <td></td>
      <td></td>
      <td></td>
      <td>82.0</td>
      <td>9.1</td>
      <td></td>
      <td>24</td>
      <td>222</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>50</td>
      <td>83.2</td>
      <td>67.5</td>
      <td>75.9</td>
      <td></td>
      <td></td>
      <td></td>
      <td>75.5</td>
      <td>7.9</td>
      <td></td>
      <td>24</td>
      <td>222</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>75</td>
      <td>68.4</td>
      <td>64</td>
      <td>77</td>
      <td></td>
      <td></td>
      <td></td>
      <td>69.8</td>
      <td>6.6</td>
      <td></td>
      <td>24</td>
      <td>216</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>100</td>
      <td>65.1</td>
      <td>58.2</td>
      <td>62.9</td>
      <td></td>
      <td></td>
      <td></td>
      <td>62.1</td>
      <td>3.5</td>
      <td></td>
      <td>24</td>
      <td>232</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>0</td>
      <td>98.6</td>
      <td>93.9</td>
      <td>99.2</td>
      <td></td>
      <td></td>
      <td></td>
      <td>97.2</td>
      <td>2.9</td>
      <td>0.85</td>
      <td>24</td>
      <td>248</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>15</td>
      <td>96.2</td>
      <td>92.9</td>
      <td>97.4</td>
      <td></td>
      <td></td>
      <td></td>
      <td>95.5</td>
      <td>2.3</td>
      <td>3.90E-02</td>
      <td>24</td>
      <td>221</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>25</td>
      <td>95</td>
      <td>78.4</td>
      <td>90.9</td>
      <td></td>
      <td></td>
      <td></td>
      <td>88.1</td>
      <td>8.6</td>
      <td>0.45</td>
      <td>24</td>
      <td>184</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>50</td>
      <td>89.5</td>
      <td>77.4</td>
      <td>82.9</td>
      <td></td>
      <td></td>
      <td></td>
      <td>83.3</td>
      <td>6.1</td>
      <td>0.25</td>
      <td>24</td>
      <td>219</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>75</td>
      <td>73.2</td>
      <td>55.7</td>
      <td>72.5</td>
      <td></td>
      <td></td>
      <td></td>
      <td>67.1</td>
      <td>9.9</td>
      <td>0.72</td>
      <td>24</td>
      <td>213</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>100</td>
      <td>64</td>
      <td>54.6</td>
      <td>79.4</td>
      <td></td>
      <td></td>
      <td></td>
      <td>66.0</td>
      <td>12.5</td>
      <td>0.65</td>
      <td>24</td>
      <td>200</td>
    </tr>
    <tr>
      <td rowspan="12">ser-5 (tm2647)</td>
      <td>Water</td>
      <td>0</td>
      <td>0</td>
      <td>97.2</td>
      <td>97.3</td>
      <td>96.9</td>
      <td></td>
      <td></td>
      <td></td>
      <td>97.1</td>
      <td>0.2</td>
      <td></td>
      <td>24</td>
      <td>248</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>15</td>
      <td>88.8</td>
      <td>91.2</td>
      <td>87.3</td>
      <td></td>
      <td></td>
      <td></td>
      <td>89.1</td>
      <td>2.0</td>
      <td></td>
      <td>24</td>
      <td>230</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>25</td>
      <td>94.4</td>
      <td>89.9</td>
      <td>85.8</td>
      <td></td>
      <td></td>
      <td></td>
      <td>90.0</td>
      <td>4.3</td>
      <td></td>
      <td>24</td>
      <td>227</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>50</td>
      <td>79.5</td>
      <td>84.6</td>
      <td>81.7</td>
      <td></td>
      <td></td>
      <td></td>
      <td>81.9</td>
      <td>2.6</td>
      <td></td>
      <td>24</td>
      <td>228</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>75</td>
      <td>79.9</td>
      <td>73.5</td>
      <td>60.2</td>
      <td></td>
      <td></td>
      <td></td>
      <td>71.2</td>
      <td>10.0</td>
      <td></td>
      <td>24</td>
      <td>248</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>100</td>
      <td>51.6</td>
      <td>59</td>
      <td>44.1</td>
      <td></td>
      <td></td>
      <td></td>
      <td>51.6</td>
      <td>7.5</td>
      <td></td>
      <td>24</td>
      <td>224</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>0</td>
      <td>96.7</td>
      <td>99.2</td>
      <td>94.3</td>
      <td></td>
      <td></td>
      <td></td>
      <td>96.7</td>
      <td>2.5</td>
      <td>0.80</td>
      <td>24</td>
      <td>233</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>15</td>
      <td>96.7</td>
      <td>88.4</td>
      <td>95</td>
      <td></td>
      <td></td>
      <td></td>
      <td>93.4</td>
      <td>4.4</td>
      <td>0.23</td>
      <td>24</td>
      <td>246</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>25</td>
      <td>97.2</td>
      <td>88.5</td>
      <td>92.4</td>
      <td></td>
      <td></td>
      <td></td>
      <td>92.7</td>
      <td>4.4</td>
      <td>0.49</td>
      <td>24</td>
      <td>187</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>50</td>
      <td>83.7</td>
      <td>87.8</td>
      <td>85.4</td>
      <td></td>
      <td></td>
      <td></td>
      <td>85.6</td>
      <td>2.1</td>
      <td>0.13</td>
      <td>24</td>
      <td>234</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>75</td>
      <td>69.7</td>
      <td>77.3</td>
      <td>73.5</td>
      <td></td>
      <td></td>
      <td></td>
      <td>73.5</td>
      <td>3.8</td>
      <td>0.74</td>
      <td>24</td>
      <td>203</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>100</td>
      <td>46.4</td>
      <td>75.1</td>
      <td>70.3</td>
      <td></td>
      <td></td>
      <td></td>
      <td>63.9</td>
      <td>15.4</td>
      <td>0.30</td>
      <td>24</td>
      <td>196</td>
    </tr>
    <tr>
      <td rowspan="12">ser-5 (tm2654)</td>
      <td>Water</td>
      <td>0</td>
      <td>0</td>
      <td>81.5</td>
      <td>96.3</td>
      <td>83.4</td>
      <td></td>
      <td></td>
      <td></td>
      <td>87.1</td>
      <td>8.1</td>
      <td></td>
      <td>24</td>
      <td>232</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>15</td>
      <td>68.8</td>
      <td>86.6</td>
      <td>75.9</td>
      <td></td>
      <td></td>
      <td></td>
      <td>77.1</td>
      <td>9.0</td>
      <td></td>
      <td>24</td>
      <td>223</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>25</td>
      <td>77.1</td>
      <td>89.1</td>
      <td>69.1</td>
      <td></td>
      <td></td>
      <td></td>
      <td>78.4</td>
      <td>10.1</td>
      <td></td>
      <td>24</td>
      <td>226</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>50</td>
      <td>55.2</td>
      <td>79.8</td>
      <td>78.4</td>
      <td></td>
      <td></td>
      <td></td>
      <td>71.1</td>
      <td>13.8</td>
      <td></td>
      <td>24</td>
      <td>254</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>75</td>
      <td>47.5</td>
      <td>42.5</td>
      <td>55.3</td>
      <td></td>
      <td></td>
      <td></td>
      <td>48.4</td>
      <td>6.5</td>
      <td></td>
      <td>24</td>
      <td>209</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>100</td>
      <td>41.2</td>
      <td>36</td>
      <td>45.8</td>
      <td></td>
      <td></td>
      <td></td>
      <td>41.0</td>
      <td>4.9</td>
      <td></td>
      <td>24</td>
      <td>215</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>0</td>
      <td>83.7</td>
      <td>96.3</td>
      <td>90.4</td>
      <td></td>
      <td></td>
      <td></td>
      <td>90.1</td>
      <td>6.3</td>
      <td>0.63</td>
      <td>24</td>
      <td>232</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>15</td>
      <td>73.7</td>
      <td>70.3</td>
      <td>82.6</td>
      <td></td>
      <td></td>
      <td></td>
      <td>75.5</td>
      <td>6.4</td>
      <td>0.82</td>
      <td>24</td>
      <td>232</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>25</td>
      <td>66.9</td>
      <td>73.7</td>
      <td>88.2</td>
      <td></td>
      <td></td>
      <td></td>
      <td>76.3</td>
      <td>10.9</td>
      <td>0.81</td>
      <td>24</td>
      <td>184</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>50</td>
      <td>54.5</td>
      <td>68.8</td>
      <td>54.6</td>
      <td></td>
      <td></td>
      <td></td>
      <td>59.3</td>
      <td>8.2</td>
      <td>0.29</td>
      <td>24</td>
      <td>200</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>75</td>
      <td>34.9</td>
      <td>41.9</td>
      <td>66.5</td>
      <td></td>
      <td></td>
      <td></td>
      <td>47.8</td>
      <td>16.6</td>
      <td>0.95</td>
      <td>24</td>
      <td>227</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>100</td>
      <td>18.2</td>
      <td>30.6</td>
      <td>40.7</td>
      <td></td>
      <td></td>
      <td></td>
      <td>29.8</td>
      <td>11.3</td>
      <td>0.22</td>
      <td>24</td>
      <td>187</td>
    </tr>
    <tr>
      <td rowspan="12">ser-6 (tm2146)</td>
      <td>Water</td>
      <td>0</td>
      <td>0</td>
      <td>98.9</td>
      <td>96.9</td>
      <td>98.6</td>
      <td>100</td>
      <td></td>
      <td></td>
      <td>98.6</td>
      <td>1.3</td>
      <td></td>
      <td>32</td>
      <td>230</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>15</td>
      <td>95.1</td>
      <td></td>
      <td>89.6</td>
      <td>96.5</td>
      <td></td>
      <td></td>
      <td>93.7</td>
      <td>3.6</td>
      <td></td>
      <td>32</td>
      <td>260</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>25</td>
      <td>97.7</td>
      <td>87.5</td>
      <td>90.3</td>
      <td>84.8</td>
      <td></td>
      <td></td>
      <td>90.1</td>
      <td>5.6</td>
      <td></td>
      <td>32</td>
      <td>221</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>50</td>
      <td>95.3</td>
      <td>97.5</td>
      <td>84.8</td>
      <td>78.1</td>
      <td></td>
      <td></td>
      <td>88.9</td>
      <td>9.1</td>
      <td></td>
      <td>32</td>
      <td>256</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>75</td>
      <td>84.8</td>
      <td>87.1</td>
      <td>77</td>
      <td>63.5</td>
      <td></td>
      <td></td>
      <td>78.1</td>
      <td>10.6</td>
      <td></td>
      <td>32</td>
      <td>265</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>100</td>
      <td>82.4</td>
      <td>78.1</td>
      <td>77.9</td>
      <td>53</td>
      <td></td>
      <td></td>
      <td>72.9</td>
      <td>13.4</td>
      <td></td>
      <td>32</td>
      <td>253</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>0</td>
      <td>100</td>
      <td>93.3</td>
      <td>100</td>
      <td>96.9</td>
      <td></td>
      <td></td>
      <td>97.6</td>
      <td>3.2</td>
      <td>0.57</td>
      <td>32</td>
      <td>278</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>15</td>
      <td>98.8</td>
      <td></td>
      <td>96.4</td>
      <td>92.4</td>
      <td></td>
      <td></td>
      <td>95.9</td>
      <td>3.2</td>
      <td>0.49</td>
      <td>32</td>
      <td>230</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>25</td>
      <td>97.9</td>
      <td>97.5</td>
      <td>96.4</td>
      <td>91.3</td>
      <td></td>
      <td></td>
      <td>95.8</td>
      <td>3.0</td>
      <td>0.14</td>
      <td>32</td>
      <td>190</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>50</td>
      <td>100</td>
      <td>100</td>
      <td>88.6</td>
      <td>92.5</td>
      <td></td>
      <td></td>
      <td>95.3</td>
      <td>5.7</td>
      <td>0.29</td>
      <td>32</td>
      <td>252</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>75</td>
      <td>92.2</td>
      <td>100</td>
      <td>88.5</td>
      <td>88.9</td>
      <td></td>
      <td></td>
      <td>92.4</td>
      <td>5.3</td>
      <td>0.07</td>
      <td>32</td>
      <td>242</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>100</td>
      <td>95.6</td>
      <td>91.3</td>
      <td>93.4</td>
      <td>95.7</td>
      <td></td>
      <td></td>
      <td>94.0</td>
      <td>2.1</td>
      <td>4.92E-02</td>
      <td>32</td>
      <td>221</td>
    </tr>
    <tr>
      <td rowspan="12">ser-7 (tm1325)</td>
      <td>Water</td>
      <td>0</td>
      <td>0</td>
      <td>68.1</td>
      <td>73.3</td>
      <td>94.5</td>
      <td></td>
      <td></td>
      <td></td>
      <td>78.6</td>
      <td>14.0</td>
      <td></td>
      <td>24</td>
      <td>200</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>15</td>
      <td>48.1</td>
      <td>49.6</td>
      <td>32.4</td>
      <td></td>
      <td></td>
      <td></td>
      <td>43.4</td>
      <td>9.5</td>
      <td></td>
      <td>24</td>
      <td>142</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>25</td>
      <td>45.7</td>
      <td>42.9</td>
      <td>30.9</td>
      <td></td>
      <td></td>
      <td></td>
      <td>39.8</td>
      <td>7.9</td>
      <td></td>
      <td>24</td>
      <td>152</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>50</td>
      <td>38</td>
      <td>37.8</td>
      <td>36.5</td>
      <td></td>
      <td></td>
      <td></td>
      <td>37.4</td>
      <td>0.8</td>
      <td></td>
      <td>24</td>
      <td>152</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>75</td>
      <td>16.4</td>
      <td>20.2</td>
      <td>41.8</td>
      <td></td>
      <td></td>
      <td></td>
      <td>26.1</td>
      <td>13.7</td>
      <td></td>
      <td>24</td>
      <td>160</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>100</td>
      <td>25.1</td>
      <td>23.2</td>
      <td>31.6</td>
      <td></td>
      <td></td>
      <td></td>
      <td>26.6</td>
      <td>4.4</td>
      <td></td>
      <td>24</td>
      <td>134</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>0</td>
      <td>98.8</td>
      <td>98.9</td>
      <td>100</td>
      <td></td>
      <td></td>
      <td></td>
      <td>99.2</td>
      <td>0.7</td>
      <td>0.13</td>
      <td>24</td>
      <td>217</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>15</td>
      <td>95.8</td>
      <td>93.8</td>
      <td>97.2</td>
      <td></td>
      <td></td>
      <td></td>
      <td>95.6</td>
      <td>1.7</td>
      <td>9.18E-03</td>
      <td>24</td>
      <td>212</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>25</td>
      <td>100</td>
      <td>93.4</td>
      <td>97.4</td>
      <td></td>
      <td></td>
      <td></td>
      <td>96.9</td>
      <td>3.3</td>
      <td>2.25E-03</td>
      <td>24</td>
      <td>193</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>50</td>
      <td>88.5</td>
      <td>92</td>
      <td>94.6</td>
      <td></td>
      <td></td>
      <td></td>
      <td>91.7</td>
      <td>3.1</td>
      <td>5.30E-04</td>
      <td>24</td>
      <td>179</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>75</td>
      <td>91.3</td>
      <td>92.4</td>
      <td>89.4</td>
      <td></td>
      <td></td>
      <td></td>
      <td>91.0</td>
      <td>1.5</td>
      <td>1.37E-02</td>
      <td>24</td>
      <td>189</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>100</td>
      <td>96.9</td>
      <td>91.7</td>
      <td>81.6</td>
      <td></td>
      <td></td>
      <td></td>
      <td>90.1</td>
      <td>7.8</td>
      <td>8.94E-04</td>
      <td>24</td>
      <td>186</td>
    </tr>
    <tr>
      <td rowspan="10">tph-1 (mg280)</td>
      <td>Water</td>
      <td>0</td>
      <td>0</td>
      <td>97.2</td>
      <td>96.1</td>
      <td>98.2</td>
      <td></td>
      <td></td>
      <td></td>
      <td>97.2</td>
      <td>1.1</td>
      <td></td>
      <td>24</td>
      <td>148</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>25</td>
      <td>66.9</td>
      <td>67.8</td>
      <td>76</td>
      <td></td>
      <td></td>
      <td></td>
      <td>70.2</td>
      <td>5.0</td>
      <td></td>
      <td>24</td>
      <td>156</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>50</td>
      <td>52</td>
      <td>47.1</td>
      <td>56.9</td>
      <td></td>
      <td></td>
      <td></td>
      <td>52.0</td>
      <td>4.9</td>
      <td></td>
      <td>24</td>
      <td>164</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>75</td>
      <td>32.2</td>
      <td>34.6</td>
      <td>48</td>
      <td></td>
      <td></td>
      <td></td>
      <td>38.3</td>
      <td>8.5</td>
      <td></td>
      <td>24</td>
      <td>148</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>0</td>
      <td>100</td>
      <td>12.2</td>
      <td>6.7</td>
      <td>42.3</td>
      <td></td>
      <td></td>
      <td></td>
      <td>20.4</td>
      <td>19.2</td>
      <td></td>
      <td>24</td>
      <td>169</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>0</td>
      <td>94.3</td>
      <td>100</td>
      <td>96.9</td>
      <td></td>
      <td></td>
      <td></td>
      <td>97.1</td>
      <td>2.9</td>
      <td>0.96</td>
      <td>24</td>
      <td>161</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>25</td>
      <td>90.4</td>
      <td>58.7</td>
      <td>78.6</td>
      <td></td>
      <td></td>
      <td></td>
      <td>75.9</td>
      <td>16.0</td>
      <td>0.61</td>
      <td>24</td>
      <td>159</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>50</td>
      <td>64.8</td>
      <td>61.7</td>
      <td>69</td>
      <td></td>
      <td></td>
      <td></td>
      <td>65.2</td>
      <td>3.7</td>
      <td>2.33E-02</td>
      <td>24</td>
      <td>158</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>75</td>
      <td>52.9</td>
      <td>28.9</td>
      <td>57.9</td>
      <td></td>
      <td></td>
      <td></td>
      <td>46.6</td>
      <td>15.5</td>
      <td>0.47</td>
      <td>24</td>
      <td>143</td>
    </tr>
    <tr>
      <td>Mia</td>
      <td>50</td>
      <td>100</td>
      <td>8.7</td>
      <td>1.8</td>
      <td>40.6</td>
      <td></td>
      <td></td>
      <td></td>
      <td>17.0</td>
      <td>20.7</td>
      <td>0.85</td>
      <td>24</td>
      <td>150</td>
    </tr>
  </tbody>
</table>

_Summary of all stress resistance assays performed in Figure 4a. The treatments, water or mianserin (50 µM), with their indicated concentrations (conc.) were added on day 1 of adulthood. Paraquat (PQ) was added in the concentration range of 0 to 100 mM on day 5 and survival after PQ [%] was calculated 24 hr later. Mean and standard deviation (S.D.) of survival after PQ [%] were calculated from 3 to 6 independent experiments (expts.). P-values were calculated between water and mianserin-treatments at the same PQ conc., using t-test. The total number of wells and animals from which data were collected are indicated._

**Table 7.**
 Summary of oxidative stress protection by serotonin antagonists.


<table>
  <thead>
    <tr>
      <th>Strain name</th>
      <th>Fold change in survival after PQ [(Drug/DMSO) -1] Expt.1</th>
      <th>Fold change in survival after PQ [(Drug/DMSO) -1] Expt.2</th>
      <th>Fold change in survival after PQ [(Drug/DMSO) -1] Expt.3</th>
      <th>Fold change in survival after PQ [(Drug/DMSO) -1] Expt.4</th>
      <th>Fold change in survival after PQ [(Drug/DMSO) -1] Expt.5</th>
      <th>Fold change in survival after PQ [(Drug/DMSO) -1] Expt.6</th>
      <th>Fold change in survival after PQ [(Drug/DMSO) -1] Expt.7</th>
      <th>Mean, Fold change in survival after PQ</th>
      <th>S.D., Fold change in survival after PQ</th>
      <th>P-value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="11">Dihydroergotamine 88 µM</td>
    </tr>
    <tr>
      <td>N2</td>
      <td>0.62</td>
      <td>0.70</td>
      <td>0.79</td>
      <td>0.19</td>
      <td>1.75</td>
      <td>1.43</td>
      <td></td>
      <td>0.91</td>
      <td>0.57</td>
      <td></td>
    </tr>
    <tr>
      <td>ser-5(ok3087)</td>
      <td>0.45</td>
      <td>0.15</td>
      <td></td>
      <td>0.10</td>
      <td></td>
      <td></td>
      <td></td>
      <td>0.23</td>
      <td>0.19</td>
      <td>3.49E-02</td>
    </tr>
    <tr>
      <td colspan="11">Metergoline 33 µM</td>
    </tr>
    <tr>
      <td>N2</td>
      <td>0.54</td>
      <td>0.57</td>
      <td>0.68</td>
      <td>0.94</td>
      <td>1.24</td>
      <td>1.67</td>
      <td></td>
      <td>0.94</td>
      <td>0.44</td>
      <td></td>
    </tr>
    <tr>
      <td>ser-5(ok3087)</td>
      <td>-0.05</td>
      <td>-0.27</td>
      <td>-0.11</td>
      <td></td>
      <td>-0.12</td>
      <td></td>
      <td></td>
      <td>-0.13</td>
      <td>0.09</td>
      <td>1.50E-03</td>
    </tr>
    <tr>
      <td colspan="11">Amperozide 13 µM</td>
    </tr>
    <tr>
      <td>N2</td>
      <td>0.93</td>
      <td>0.74</td>
      <td>0.99</td>
      <td>0.92</td>
      <td>2.49</td>
      <td>0.89</td>
      <td></td>
      <td>1.16</td>
      <td>0.66</td>
      <td></td>
    </tr>
    <tr>
      <td>ser-5(ok3087)</td>
      <td>0.30</td>
      <td>0.03</td>
      <td></td>
      <td>-0.58</td>
      <td></td>
      <td></td>
      <td></td>
      <td>-0.09</td>
      <td>0.45</td>
      <td>1.63E-02</td>
    </tr>
    <tr>
      <td colspan="11">Methiothepin 10 µM</td>
    </tr>
    <tr>
      <td>N2</td>
      <td>0.80</td>
      <td>1.08</td>
      <td>0.95</td>
      <td>0.36</td>
      <td>0.77</td>
      <td>2.94</td>
      <td>1.39</td>
      <td>1.19</td>
      <td>0.89</td>
      <td></td>
    </tr>
    <tr>
      <td>ser-5(ok3087)</td>
      <td>0.07</td>
      <td>0.10</td>
      <td></td>
      <td>0.16</td>
      <td>-0.01</td>
      <td></td>
      <td></td>
      <td>0.08</td>
      <td>0.08</td>
      <td>1.24E-02</td>
    </tr>
    <tr>
      <td colspan="11">Ketanserin 176 µM</td>
    </tr>
    <tr>
      <td>N2</td>
      <td>0.63</td>
      <td>0.59</td>
      <td>1.13</td>
      <td>1.38</td>
      <td>0.42</td>
      <td>1.71</td>
      <td></td>
      <td>0.98</td>
      <td>0.51</td>
      <td></td>
    </tr>
    <tr>
      <td>ser-5(ok3087)</td>
      <td>-0.41</td>
      <td>-0.14</td>
      <td>0.01</td>
      <td></td>
      <td>-0.07</td>
      <td></td>
      <td></td>
      <td>-0.15</td>
      <td>0.18</td>
      <td>1.91E-03</td>
    </tr>
    <tr>
      <td colspan="11">Mirtazapine 50 µM</td>
    </tr>
    <tr>
      <td>N2</td>
      <td>0.8</td>
      <td>0.7</td>
      <td>1.1</td>
      <td>0.4</td>
      <td>1.0</td>
      <td>0.8</td>
      <td>1.5</td>
      <td>0.89</td>
      <td>0.35</td>
      <td></td>
    </tr>
    <tr>
      <td>ser-5(ok3087)</td>
      <td>0.0</td>
      <td>-0.1</td>
      <td></td>
      <td>-0.1</td>
      <td>-0.2</td>
      <td></td>
      <td></td>
      <td>-0.11</td>
      <td>0.07</td>
      <td>1.92E-04</td>
    </tr>
    <tr>
      <td colspan="11">LY-165,163 33/PAPP µM</td>
    </tr>
    <tr>
      <td>N2</td>
      <td>0.48</td>
      <td>0.49</td>
      <td>1.00</td>
      <td>0.94</td>
      <td>0.53</td>
      <td>1.40</td>
      <td></td>
      <td>0.81</td>
      <td>0.37</td>
      <td></td>
    </tr>
    <tr>
      <td>ser-5(ok3087)</td>
      <td>-0.03</td>
      <td>0.35</td>
      <td>-0.07</td>
      <td></td>
      <td>-0.16</td>
      <td></td>
      <td></td>
      <td>0.02</td>
      <td>0.23</td>
      <td>3.19E-03</td>
    </tr>
    <tr>
      <td colspan="11">Mianserin 50 µM</td>
    </tr>
    <tr>
      <td>N2</td>
      <td>1.10</td>
      <td>1.11</td>
      <td>1.18</td>
      <td>0.53</td>
      <td>3.24</td>
      <td>1.60</td>
      <td></td>
      <td>1.46</td>
      <td>0.94</td>
      <td></td>
    </tr>
    <tr>
      <td>ser-5(ok3087)</td>
      <td>0.14</td>
      <td>-0.18</td>
      <td></td>
      <td>-0.26</td>
      <td></td>
      <td></td>
      <td></td>
      <td>-0.10</td>
      <td>0.21</td>
      <td>4.49E-02</td>
    </tr>
  </tbody>
</table>

_Summary of all stress resistance assays performed in Figure 4—figure supplement 1b. The treatments, DMSO or serotonin antagonists, with their indicated concentrations (conc.) were added on day 1 of adulthood. Paraquat (PQ) (100 mM) was added on day 5 and survival after PQ [%] was calculated 24 hr later. Mean and standard deviation (S.D.) of survival after PQ [%] were calculated from 3 to 7 independent experiments (expts.). P-values were calculated between N2 and mutant strains for fold change values with indicated small molecule treatments using t-test._

We next asked whether SER-5 was also required for mianserin to preserve low transcriptional drift-variances in redox-related genes. We measured redox gene expression levels by qRT-PCR in wild-type 5-day-old N2 and ser-5(ok3087) animals that were treated with mianserin or water on day 1 (Figure 5a,b; Figure 1—figure supplement 1a). In N2 samples, mianserin increased the expression of stress response genes that drift down with age (sod-1, sod-2, prdx-2, -3, -6) and decreased the expression of stress response genes that drift up with age (sod-4, sod-5, all hsp-16s), an effect that was not observed in ser-5(ok3087) mutants. In contrast, SER-3 and SER-4, two receptors we previously showed to be required for lifespan extension by mianserin, were dispensable for stress protection (Figure 4a,b) (Petrascheck et al., 2007), as well as for the attenuation of drift-variance in redox-associated genes (Figure 4—figure supplement 1c). Thus, in wild-type animals, mianserin treatment preserved low drift-variances in redox-related genes into older age (day 5), in a ser-5 dependent manner (Figure 5a,b).

Importantly, ser-5 mutants were specifically defective in their response to mianserin, but showed no defect in their response to oxidative stress. Young (day 1) wild-type N2 animals and ser-5(ok3087) mutants showed a nearly identical response to oxidative stress (Figure 5c). The age-specific effects of ser-5 could not be attributed to expression changes, as ser-5 expression remained constant from day 1 to day 10 in our RNA-seq experiment.

To test the hypothesis that mianserin preserved the homeostatic capacity of the redox system, as suggested by Figure 3e, we asked whether the treatment with mianserin on day 1 of adulthood led to an enhanced redox gene expression in response to the stressor paraquat in older animals (day 5). We therefore challenged older mianserin-treated or control animals (day 5) with paraquat for 8 hr and measured redox-gene expression by qRT-PCR (Figure 5d). Mianserin treatment led to an enhanced transcription of redox genes in response to paraquat as compared to age-matched control animals. The enhanced response was ser-5 dependent (Figure 5d). Thus, SER-5 is required for mianserin to attenuate age-associated increases in drift-variance in redox genes, and to preserve the homeostatic capacity of the redox system into older age.

Furthermore, lifespan-extension by mianserin was strongly reduced or abrogated in ser-5, snt-1 and unc-26 mutant animals (Figure 5e, f; Figure 5—figure supplement 1a; Table 8). Seven additional serotonergic antagonists/inverse agonists also extended lifespan in a manner that was partially or fully dependent on ser-5 (Figure 5—figure supplement 1b). Thus, these results show that inhibiting serotonergic signals via SER-5 extends lifespan, attenuates age-associated drift-variance in the redox system and preserves the homeostatic capacity of the redox system.

**Table 8.**
 Summary of all lifespan data for mianserin.


<table>
  <thead>
    <tr>
      <th colspan="7">Cumulative statistics</th>
      <th colspan="4">Statistics of individual expts.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Strain</td>
      <td>Small molecule</td>
      <td>No. of expts.</td>
      <td>Mean lifespan [days] (+Mia/+water)</td>
      <td>change in lifespan [%]</td>
      <td>S.E.M.</td>
      <td>No. of animals (+Mia/+water)</td>
      <td>Mean lifespan (days) (+Mia/+water)</td>
      <td>change in lifespan [%]</td>
      <td>P-value</td>
      <td>No. of animals (+Mia/+water)</td>
    </tr>
    <tr>
      <td rowspan="6">N2</td>
      <td rowspan="6">Mia</td>
      <td>12</td>
      <td>26.7/19.8</td>
      <td>+35</td>
      <td>± 7</td>
      <td>642/577</td>
      <td>26.4/19.8</td>
      <td>+34</td>
      <td>1.67E-08</td>
      <td>77/59</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>25.5/21.5</td>
      <td>+19</td>
      <td>6.85E-07</td>
      <td>113/94</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>28.1/20.1</td>
      <td>+40</td>
      <td>3.71E-14</td>
      <td>95/104</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>30.6/19.0</td>
      <td>+64</td>
      <td>3.17E-15</td>
      <td>57/50</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>26.8/21.5</td>
      <td>+25</td>
      <td>1.87E-11</td>
      <td>149/145</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>22.6/16.6</td>
      <td>+27</td>
      <td>1.61E-23</td>
      <td>151/125</td>
    </tr>
    <tr>
      <td rowspan="3">snt-1 (md290)</td>
      <td rowspan="3">Mia</td>
      <td>3</td>
      <td>20.9/18.2</td>
      <td>+15</td>
      <td>± 2</td>
      <td>236/231</td>
      <td>23.3/19.9</td>
      <td>+17</td>
      <td>1.84E-05</td>
      <td>86/90</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>17.3/15.4</td>
      <td>+12</td>
      <td>1.18E-02</td>
      <td>79/80</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>22.1/19.3</td>
      <td>+15</td>
      <td>2.4E-03</td>
      <td>71/61</td>
    </tr>
    <tr>
      <td rowspan="3">unc-26 (e205)</td>
      <td rowspan="3">Mia</td>
      <td>3</td>
      <td>25.0/26.7</td>
      <td>-7</td>
      <td>± 7</td>
      <td>135/165</td>
      <td>27.8/26.9</td>
      <td>+3</td>
      <td>0.53</td>
      <td>54/68</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>22.2/26.5</td>
      <td>-16</td>
      <td>4.52E-02</td>
      <td>14/24</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>26.5/25.3</td>
      <td>+5</td>
      <td>0.52</td>
      <td>67/73</td>
    </tr>
    <tr>
      <td rowspan="3">ser-5 (ok3087)</td>
      <td rowspan="3">Mia</td>
      <td>3</td>
      <td>23.4/22.2</td>
      <td>+5</td>
      <td>± 5</td>
      <td>496/458</td>
      <td>23.6/20.6</td>
      <td>+15</td>
      <td>4.19E-02</td>
      <td>152/144</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>26.4/26.2</td>
      <td>+1</td>
      <td>0.85</td>
      <td>174/144</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>20.1/19.8</td>
      <td>-1</td>
      <td>0.25</td>
      <td>170/170</td>
    </tr>
  </tbody>
</table>

_Summary of all lifespan experiments performed in Figure 5e,f and Figure 5—figure supplement 1a. N2 and mutant strains were treated with 50 µM mianserin (Mia) on day 1 and lifespan [days] was scored until 95% of animals were dead in all tested conditions. Cumulative statistics and statistics of individual experiments are shown. Mean lifespan [days], change in lifespan [%] and S.E.M. for mianserin-treated (+Mia) and water-treated (+water) animals from multiple, independent experiments (expts.) are shown. Change in lifespan [%] and P-values for individual experiments were calculated using the Mantel–Haenszel version of the log-rank test. Number of animals in individual experiments and all experiments combined are shown._

### Mianserin prolongs lifespan by slowing age-associated change in young adults

We next asked whether drift-variance could be used as a metric to monitor age-associated change in young adults. Comparing drift-variances between mianserin-treated and untreated animals, we noticed that by day 10, mianserin-treated animals exhibited a drift-variance slightly lower than that of 3-day-old control animal (P=0.37). This suggested that mianserin-treated animals showed a ~7–8 day delay in age-associated transcriptional change compared to age-matched controls (Figure 2a).

Principle component analysis (PCA), a different statistical method to analyze differences between transcriptomes, confirmed this observation (Figure 6a). PCA showed that control samples aligned on the x-axis (dimension 1) according to age and that 10 day-old mianserin-treated animals aligned closer to 3-day-old than to 10-day-old control animals. These results suggested that the physiological shift that results in the 7–8 day lifespan extension observed in mianserin-treated animals at the end of a lifespan assay was already observable by day 10.

We therefore asked whether mianserin slowed age-associated physiological change specifically in early adulthood causing a 7–8 day delay by day 10. If so, mianserin would be expected to specifically lower the mortality rate in young but not in old adults. However, the number of age-associated death events in young adults is too low to directly determine changes in age-associated mortality rates before the age of day 10. As we are comparing mortality in animals either treated with water or mianserin that is added to the same population of worms on day 1 of adulthood, we can confidently state that mortality levels are identical between mianserin-treated and untreated adults at the start of the experiment. Any difference in mortality levels observed from day 1 onwards must therefore be the result of a change in mortality rate by mianserin.

Plotting a mortality curve for over 3,000 mianserin-treated or untreated animals showed a significantly lower mortality level for mianserin-treated animals by day 12 (Figure 6b, Figure 6—figure supplement 1a). Therefore, mianserin treatment decelerated the rise in mortality levels between day 1 and 12 of adulthood. From then on, the mortality curves were parallel showing a 7–8 day shift in mortality across the remaining lifespan. The parallel nature suggested that mianserin did not affect mortality rates past day 12 and that its effect on lifespan was restricted to the period of early adulthood (Figure 6b, Figure 6—figure supplement 1a) (Mair et al., 2003; Vaupel, 2010). Power calculations confirmed that these mortality curves were sufficiently powered to detect a one day difference in lifespan in over 90% of the experiments (α=0.01) (Figure 6—figure supplement 1b) (Ye et al., 2014). These results further supported a model in which mianserin treatment specifically lowered age-associated change in early adulthood, causing a shift in physiology and mortality that can be observed in transcriptomes by day 10.

We reasoned that if the effect of mianserin on lifespan precedes the onset of mortality and is completed by day 10, mianserin treatment beyond day 10 should be dispensable. Alternatively, if mianserin still influenced mortality later in life, shorter exposures would lead to a shorter lifespan extension compared to a lifelong exposure. We therefore limited mianserin exposure to 8 hr, 1, 5, 10 and 15 days and compared their lifespan with animals treated for the entire life (Figure 6c,d). Exposing the animals for 5 or 10 days was sufficient to extend lifespan to the same extent as lifelong exposure (Figure 6c,d). Shorter exposures (8 hr, 1 day) also extended lifespan, but not by as much, showing that removing mianserin from the culture is an effective means to restrict its action (Figure 6c,d). Taken together, these results are most consistent with a model in which mianserin specifically lowers the rate of age-associated change during the first few days of adulthood, thereby extending their longevity (Figure 6e) and postponing the onset of mortality. While the change in age-associated mortality rate during early adulthood is too small to be accuratly determined, when we measured drift-variance, it allowed us to monitor the age-associated change in the transcriptome during early adulthood (Figure 6e,f).

Since the effect of mianserin in early adulthood overlapped with the reproductive period (first 5 days of adulthood), we asked whether mianserin treatment increased reproductive lifespan as has been observed in tph-1(mg280) mutants (Sze et al., 2000). Mianserin treatment blocks serotonin-induced egg-laying (Petrascheck et al., 2007), but had a minor effect on amount or timing of spontaneous egg-laying and brood size (Figure 6g). Most importantly, mianserin did not increase reproductive longevity (Figure 6g).

We further considered the possibility that mianserin acted by a mechanism similar to lifespan extension by germline ablation (Figure 6h). Two previous findings suggested otherwise: i) Lifespan extension by germline ablation depends on daf-16, while mianserin does not (Arantes-Oliveira et al., 2002; Petrascheck et al., 2007); ii) germline ablation increases lifespan of eat-2(ad1116) mutants while mianserin does not (Crawford et al., 2007). We measured whether mianserin treatment mimicked the increased proteasome activity observed in glp-1 mutants (Vilchez et al., 2012) (Figure 6h). A 24 hr mianserin treatment did not increase the proteasome activity, as measured by a fluorescence-based assay for chymotrypsin-like activity. On day 5, mianserin slightly decreased proteasome activity, consistent with a slight increase in drift-variance in proteasome-related genes (Figure 6h; Figure 6—figure supplement 1c). We concluded that mianserin specifically lowers the rate of age-associated change in somatic tissues and does not involve a mechanism directly related to the germline.

### Transcriptional drift-variance increases with age in mice and humans

Our data demonstrate that changes in drift-variance provide a metric for aging that correlates with mortality in C. elegans. To test whether drift-variance also increases with age in mammals, we re-analyzed published gene expression data-sets obtained from aging mouse tissues, aging human brains, and from fibroblasts derived from Hutchinson-Gilford progeria syndrome patients (Figure 7) (Lu et al., 2004; Liu et al., 2011; Jonker et al., 2013). We calculated drift-variances from brain, kidney, liver, lung, and spleen based on gene expression data-sets from mice aged 13, 26, 52, 78, 104 and 130 weeks. We calculated drift-variances using 13-week-old mice as a young reference (see Methods) and pooled mice into age-bins of 30, 60 and 100 weeks to reduce variability. Drift-variance increased in all tissues with age (Figure 7a). Compared to the drift-variance changes observed in C. elegans (Figure 2a), these changes however were small.

Because the 13-week-old mice were used as reference for young age (see methods), the drift-variance in the 30-week-old group including the 13-week-old sample is artificially low (Figure 6a, see material and methods). To better reflect the actual variance of the 30-week-old group, we set aside the data of one 13-week-old mouse to use as a young reference and recalculated drift-variances for all samples (Figure 7b). This strategy has the advantage that we can observe the real drift-variance for the 30-week-old group by excluding the reference data-set, but has the disadvantage that the results are less robust as they all depend on a single reference sample. Plotting drift-variance for each organ as a function of age confirmed that as mice age, drift-variance increases in all organs (Figure 7b). It will be interesting to learn if the different rates by which drift-variance increases in different organs will also be observed in other data-sets.

We re-analyzed the data from Lu et al. that recorded gene expression profiles from 32 human brains aged 26 to 106 years of age (frontal cortex) (Figure 7c) (Lu et al., 2004). For the first plot, we binned the data into 20-year bins and calculated the overall drift-variance for each 20-year bin. As a young age reference, we used the mean gene expression of adults below 30 (26, 26, 27, and 29) (see Materials and methods). This analysis shows that over the entire population, drift-variance remains relatively stable until the age of sixty, and then starts to rise (Figure 6c). We also plotted the drift-variance of each individual as a function of age. This revealed a significant correlation (Spearman, rho=0.6, P=0.0014) between age and drift-variance in the human brain.

Irrespective of the age of the mother, the aging process starts afresh for each new generation. We therefore hypothesized that aging must be reversed with each new generation and asked whether it is possible to reverse increases in drift-variances. To address this question, we re-analyzed the data-set generated by Liu et al. who derived induced pluripotent stem cells (iPSCs) from fibroblasts of healthy controls (BJ) and patients suffering from Hutchinson-Gilford progeria syndrome (HPGS), an accelerated aging syndrome (Figure 7e) (Liu et al., 2011). As a young-reference to calculate drift-variance, we used human H9 embryonic stem cells (ESC). As expected for a premature aging syndrome, fibroblasts from HGPS patients showed increased drift-variance relative to BJ control fibroblasts (Figure 7e). Furthermore, nuclear reprogramming reduced drift-variance in iPSCs to levels closer to those seen in H9 embryonic stem cells. Thus, increases in drift-variance are reversed by nuclear reprogramming in vitro

## Discussion

In this study, we have analyzed the dynamics of aging C. elegans transcriptomes and how these dynamics are affected by mianserin treatment. We separate transcriptional changes across groups into those that characterize activation or inhibition of entire pathways (type I) and those that characterize the relative expression levels among genes (type II, transcriptional drift, Figure 1h,i). In C. elegans, transcriptional drift continuously increases with age across the transcriptome, substantially altering stoichiometric balances observed in young animals (Figure 2a). Longevity mechanisms induced by either pharmacologically blocking serotonergic signaling or by blocking insulin signaling by daf-2 RNAi attenuate transcriptional drift (Figure 2a,g). Abolishing lifespan extension by these mechanisms by either blocking serotonergic signaling too late (mianserin, day 5) or by addition of daf-16 RNAi (daf-2) abolished the attenuation of drift-variance (Figure 2).

Detailed analysis of redox-related pathways showed that mianserin-reduced drift-variances are associated with improved stress resistance in older age (Figure 3). Mutations in the serotonin receptor SER-5 that abolish the effect of mianserin on drift-variance also abolished its effect on stress resistance and lifespan (Figure 4, 5).

Using transcriptome-wide drift-variance values as a metric for age showed that mianserin treatment attenuated the age-associated increase of drift-variance, thereby preserving the characteristics of a much younger (~3 days-old) transcriptome up to chronological day 10 (Figure 2a, 6a). These results showed that mianserin caused a 7–8 days delay in age-associated transcriptional change and suggested that the physiological changes leading to a lifespan extension were already completed by day 10.

Measuring mortality levels supported this conclusion. By day 12, the entire mortality curve was shifted parallel by 7–8 days (Figure 6b) showing that the physiological delay leading to a lifespan extension was already completed. Experiments in which animals were exposed to mianserin for limited periods of time confirmed that mianserin exposure for the first 5–10 days of adulthood was necessary and sufficient to fully extend lifespan (Figure 6c,d). The most parsimonious explanation that accounts for all these results is that mianserin treatment slows degenerative processes specifically between day 1 and 10, extending the duration of the period of young adulthood thereby postponing the onset of major mortality around mid-life (Figure 6e,f).

### Biological interpretation of transcriptional drift-variance

Aging has been shown to cause DNA damage, degeneration of the nuclear architecture, loss of histones, loss of histone modification (Kaeberlein et al., 1999; Scaffidi and Misteli, 2006; Burgess et al., 2012). These changes contribute to the degenerative phenotypes observed with aging (Mostoslavsky et al., 2006; Feser et al., 2010; Peleg et al., 2010). In the present study, we used expression patterns of young adults as a reference to monitor the aging process across the transcriptome. We found that aging causes the expression of genes within functional groups to drift apart, causing a loss of co-expression patterns as observed in young adults. We quantified this phenomenon using drift-variance, defined as the variance in gene expression among genes. It is important to distinguish transcriptional noise, which measures the variance of the same genes among samples (Bahar et al., 2006), from transcriptional drift, which measures variance among genes within the same samples. At present it is unclear whether transcriptional drift is the consequence of a regulated program or of degenerative changes in the nucleus that lead to a loss of transcriptional control. Consistent with a regulated program are recent findings that the germline actively represses the activation of heat shock promoters via histone methylation, causing a decline in heat shock capacity (Labbadia and Morimoto, 2015b). Consistent with degenerative changes are recent findings that show the loss of histone methylation to cause aberrant gene expression that increases with age leading to a transcriptional drift-like effect (Somel et al., 2006; Mercken et al., 2013; Pu et al., 2015; Sen et al., 2015).

Irrespective of whether transcriptional drift is the consequence of a regulated program or a degenerative change, its effect on pathway function is likely to be detrimental. Many physiological processes depend on appropriate stoichiometry of their components. Large and persistent deviations in mRNA balance as measured by drift-variance are likely to result in stoichiometric imbalances in protein complexes, negatively affecting proteostasis as has been recently observed (Houtkooper et al., 2013; Walther et al., 2015). Our results modulating drift-variance for redox genes via mianserin and SER-5 certainly suggest that the age-associated increases in drift-variance are associated with regulatory decline (Figures 3, 5). Attenuation of transcriptional drift in the redox system was associated with an improved homoestatic capacity, i.e. an improved ability of the redox system to appropriately respond to outward stimuli.

Transcriptional drift also provided a useful concept to analyze aging transcriptomes. Accounting for its effects dramatically simplified what was an initially excessively complex expression pattern (Figure 1). Excluding gene expression changes due to drift left a set of genes that changed expression in response to mianserin treatment that was enriched for genes related to stress, innate immunity, aging and the xenobiotic response. With the exception of the xenobiotic response, which is expected to be triggered by addition of a foreign substance such as mianserin (Figure 2f), all other functions have been linked to serotonin signaling (Table 1) (Zahn et al., 2006; Petrascheck et al., 2007; Rangaraju et al., 2015a).

Further, in accordance with the hypothesis that increases in drift-variance are a signature of aging in the transcriptome, we find that drift-variance is attenuated by two longevity mechanisms (mianserin and daf-2 RNAi) across large sections of the transcriptome. Many of the age-associated changes that were reversed by mianserin were also reversed by daf-2 RNAi (58%). This overlap is consistent with chemical epistasis experiments. Treating daf-2(e1370) mutants with mianserin causes only a partial extension of lifespan (11% instead of 31%) (Petrascheck et al., 2007) consistent with the idea that many of the genes attenuated by mianserin treatment are already attenuated in daf-2(e1370) mutants and thus do not further contribute to a lifespan extension. It should be noted that age-associated increases in drift-variance do not contradict the idea that transcription factors regulate longevity. Activation of DAF-16 target genes by daf-2RNAi prevent age-associated drift of thousands of genes, thus resulting in a net decrease of drift, even though a transcriptional program has been induced (Figure 2g). Our experiment did not address the questions whether increasing drift-variance beyond what occurs naturally with age accelerates aging and whether attenuation of transcriptional drift-variance is universal to all longevity mechanisms.

At this point, it is prudent to mention possible pitfalls associated with transcriptional drift analysis. Drift-variance calculations require data-sets that include multiple ages (3 or more) as direct statistical comparisons to the young-reference are not permissible. Furthermore, in the context of GO annotations, it is important to realize that if a given GO annotation contains significant numbers of mis-annotated genes, these genes may change expression in a different direction giving the erroneous impression of transcriptional drift. To account for these effects in our study, we i) used the experimentally determined oxidative stress signature derived from Olivera et al (Figure 3e), and ii) used a robust Levene’s test to determine statistical differences. The robust Levene’s test uses a 10% trimmed mean, which removes large outliers such as those that would be expected by mis-annotation. These safeguards, however, are only effective if the number of mis-annotated genes is small relative to the total number of genes.

Conceptually, transcriptional drift is not a biomarker for aging. It is a metric for aging similar to lifespan measurements that can be used to monitor age-associated physiological changes on the molecular level within groups of genes. Lifespan measurements record the fraction of organisms alive in different cohorts at any given time to compare rates of aging, while drift-variance allows a similar comparison based on transcriptional drift-variance. What made drift-variance measures essential for the present study was that it allowed us to monitor age-associated physiological changes in young animals, at a time when age-associated mortality levels are too low to be accurately determined (see below).

### Period-specific lifespan extension

Measuring lifespan of mianserin-treated and untreated C. elegans revealed a mean lifespan extension of 7–8 days (Figure 2). Lifespan measurements detect differences after the majority of the animals have died and make no statements about the period during which the relevant physiological events that lead to an increase in lifespan occur (Figure 2c,e) (Mair et al., 2003; Partridge and Gems, 2007). The finding that transcriptional drift values in mianserin-treated animals already showed a 7–8 day delay in physiological change as early as day 10 suggested a model in which the physiological events responsible for the 7–8 days lifespan extension take place (and conclude) prior to day 10 (Figure 2a, 6a,e).

Determining mortality levels at different ages confirmed this model. Mianserin or water is added on day 1 of adulthood to the same preparation of N2 animals. The mortality levels of both cohorts (water, mianserin) are therefore identical at the start of the experiment. Thus, the lower mortality level observed on day 12 in mianserin-treated animals is the result of a lower mortality rate prior to day 12 (Figure 6b). Furthermore, mianserin ceases to affect mortality rates past day 12 as evident by highly parallel mortality curves (Figure 6b). As with the results obtained with drift measurements, the most plausible explanation is that mianserin treatment specifically decelerates the rise in mortality in young adults leading to a lower mortality level sometime between day 10 to day 12 that persists throughout life, ultimately revealing itself in a 7–8 day lifespan extension (~30–40% increase in lifespan) (Figure 6b).

Analysis of drift-variance, PCA, mortality and survivorship independently arrive at the same 7–8 days delay in physiology, either measured as a feature of transcriptomes or by recording death times. All methods suggest that the delay is completed before day 10 or 12 and therefore occurs during early adulthood. We further experimentally confirmed this suggestion by showing that treatment for the first five or ten days of life was necessary and sufficient to achieve the same lifespan extension observed with lifelong treatment (Figure 6c,d).

Even though this period exactly overlaps with the reproductive period, the effect of mianserin appears to be specific to somatic tissue (Figure 6g,h). In contrast to germline ablation, mianserin extends lifespan of daf-16 mutants but not of eat-2 mutants (Crawford et al., 2007; Petrascheck et al., 2007; Vilchez et al., 2012) and does not increase proteasome activity as observed in glp-1 mutants (Figure 6h). It is still possible that the mianserin-induced lifespan extension interacts or depends on the germline, but if it does, the connection is more indirect potentially similar to what has been observed for dietary restriction (Crawford et al., 2007).

Lifespan extension mechanisms that decelerate the rate of mortality are generally interpreted as slowing the aging process, while a parallel shift as the one we observe with mianserin is interpreted as a constant risk factor that causes a proportional shift in the overall risk of death (Mair et al., 2003; Harrison et al., 2009; Vaupel, 2010; Kirkwood, 2015). Our data do not challenge any of these prior interpretations, but add a further possibility. Parallel shifts may also be brought about by a period extension in which the rate of age-associated physiological change is specifically lowered in young adults. Age-associated mortality in young adults is very low compared to extrinsic mortality factors and thus changes in age-associated mortality rates are difficult to reliably determine (Partridge and Gems, 2007; Beltran-Sancheza et al., 2012). Specific changes in mortality rates during early adulthood therefore can go unnoticed but manifest themselves later as parallel shifts at the time when age-associated mortality levels are sufficiently high to be reliably determined. Whether the attenuation of physiological changes specific to young adults that affects later mortality, as seen for mianserin, is the equivalent of slowing aging in young adults is a debate for the general aging community.

In summary, this work describes the phenomenon of transcriptional drift and how it can be used as a metric for aging. Using this metric, we show that blocking serotonergic signals by mianserin delays age-associated physiological changes such as transcriptional drift and mortality exclusively during early adulthood, thus extending the duration of this period and postponing the onset of age-associated mortality.

## Materials and methods

### Measurement of transcriptional drift and drift-variance

Analyzing the RNA-seq data in aging C. elegans, we observed dramatic changes in the transcriptome with age. We simply termed these changes ‘transcriptional drift’, to emphasize the ambiguity of these changes. These changes could either be the result of regulated changes as part of a biological program, or caused by a progressive loss of transcriptional control with age. Note that a progressive loss of transcriptional control does not necessarily have to result in random changes. A gene that is continuously activated in young animals may be less activated in older animals due to a progressive functional decline in the transcriptional machinery. Thus, a gradual loss of transcriptional control would cause an age-associated decline in expression of that gene in a non-random fashion. Conversely, repressive chromatin is lost with age leading to increases in transcription that are repressed in young animals. As most physiological processes depend at least to some degree on transcriptional regulation, we propose that expression changes of genes within the same pathway that go into opposing directions (drift-variance increases) are detrimental for the functionality of the pathway (as seen for redox pathways in Figure 3b). These changes may also allow us to indirectly track the functional decline by measuring transcriptional drift.

### Calculating transcriptional drift and drift-variance

Transcriptional drift (td) is the change in transcript level of a gene at a given age from its level in young animals (“young reference”). As all the subsequent calculations depend on the age chosen for “young reference” we made sure to indicate the age used as a “young reference” for each plot (see below). For all the C. elegans work, the “young reference” age was day 1, at the onset of reproductive maturity in adulthood.

For any gene x, transcriptional drift (td) is defined as (Equation 1).

$$
td_{gene x} = ( \frac{No.of transcripts_{age[t]}}{No.of transcripts_{young reference}})
$$

or, which is the same as

$$
td_{gene x}=(\frac{cpm_{age[t]}}{cpm_{young reference}})
$$

where, ‘cpm’ stands for counts per million; ‘t’ stands for time in days, weeks or years, dependent on the organism.

Equation 1 normalizes the level of transcription for all genes to 0 for a young animal. Note: If several biological replicates are available for the age of the young reference, a variance for the young age can be calculated (see the section below titled ‘Variance for “the young reference”’).

To evaluate changes in co-expression, we calculated the drift-variance (dv) (Equation 3) over a group of n genes with transcriptional drift-values ranging from tdi=1 to tdn.

$$
drift variance=\frac{1}{n−1}\sum_{i=1}^{n}(td_{i}−td¯)^{2}
$$

Thus, if genes maintain a youthful co-expression pattern, drift-variance stays relatively small. If large fractions of genes within a GO or an entire transcriptome change expression in opposing directions, the drift-variance increases, suggesting a loss of youthful co-expression patterns as shown in Figure 1h,i.

### Variance for the “young reference”

If multiple replicate data-sets for the “young reference” age are available, it is possible to plot drift-variance for the young reference as well. There are two ways to incorporate multiple “young reference” data-sets, each of which has its advantages or disadvantages.

Method #1 uses all “young reference” samples to calculate a mean gene expression level for each individual gene to generate the “young reference” values for Equation 1. Method #1 will result in a drift-variance for the “young reference” age as well, but this drift-variance is too small and should not be used for statistical comparisons due to circular referencing. The advantage of method #1 is that the results for all subsequent ages are more robust as the inclusion of several “young reference” samples thereby reducing the overall noise (used in Figures 2a,g, 3b, 7a,c,e).

Method #2 allows calculating a real drift-variance value for young animals by setting aside one or several samples as the “young reference.” These samples are only used as references and therefore do not contribute to the drift-variance in each plot. For the remaining experimental replicates of the same age, transcriptional drift is then calculated using Equation 1 without including any of the “young reference” samples.” This will result in a drift-variance greater than 0 for the youngest age and show how much drift varies between young animals. Method #2 has the disadvantage that if there are only few young reference samples are available, and only one is used as a young reference, all values of the graph depend on a single reference sample. We used this method #2 to calculate the variances for Figure 7b,d. The case of 7d was ideal as there were 4 samples less than 30 years of age which were set aside as reference and that allowed us to calculate the “young reference”-mean over all 4 samples. As drift-variances for these 4 samples are artificially low due to self referencing they were excluded from the plot. Ideally, an experiment would have 4–6 gene expression replicates for the “young reference” age, in which case, half of them could be used as references, the others as experimental samples.

How transcriptional drift and variance relate to measures like fold-changes in transcription is shown in Supplementary Figure 2a–d. To determine whether the differences in variance were statistically different, we used the Brown-Forsythe version of the Levene’s test, as implemented in STATA software.

### Calculations for drift-plots in Figures

Figure: 1g: Volcano plot used mean cpm values from all three biological replicates.

The 0 line (young reference, day 1 expression, yellow line) indicates the expected expression level for young day 1 adult animals.

Black: Each dot represents one of for the 3,367 genes that significantly change expression with age between day 1 and day 3. The -log10(P-value) of the P-value comparing day3 water vs day 1 water is shown as a function of the the log2(cmp day 3 water / cpm day1 water).

Blue: Same 3,367 genes as above. However the -log10(P-value) comparing day3 mianserin vs day 1water is shown as a function of the the log2(cmps day 3 mianserin / cpm day1 water). Note: both data-sets (black and blue) use identical y- coordinates to demonstrate the reduction in age-associated changes upon mianserin-treatment. (cpm stands for: counts per million).

Young Reference: To obtain a ‘young reference’ value for each individual gene the mean expression level across all three biological replicates of young day 1 old water-treated C. elegans animals was calculated.

Figure 1h, i: Drift plots for genes involved in oxidative phosphorylation (KEGG pathway: cel 00190) and the lysosome (KEGG pathway: cel 04142). Only one out of three replicates was used to generate these plots. Transcriptional drift for oxidative phosphorylation and lysosomal genes (line graphs) was calculated using Equation 1 and plotted as a function of C. elegans age (gray lines). At each age, the transcriptional drift-variance across all genes within the pathway was calculated using Equation 2 and plotted as Tukey-style box plots omitting outliers. Tukey plots were superimposed over the line graphs. See Equation 1, 3. Outliers were only omitted for graphical purposes but not for statistical testing (robust Levene’s test). The lines for each gene were included in these two plots, superimposed on the Tukey-style box plot to illustrate the significance and utility of the box plots in visualizing transcriptional drift.

Young reference: As a “young reference” value for each individual gene, the expression level of young day 1 old water-treated C. elegans animals was used. Only replicate #1 of our data-set was used.

Figure 2a: Drift plots for all 19,196 genes in our data-set of water-treated control and mianserin-treated animals. Tukey plots show drift-variance calculated for the entire transcriptome (Equation 3). See Equation 1, 3. Outliers were only omitted for graphical purposes, but not for statistical testing (robust Levene’s test).

Young reference: To obtain a “young reference” value for each individual gene, the mean expression level across all three biological replicates of young day 1 old water-treated C. elegans animals was calculated.

Figure 2b: Drift plots show transcriptional drift on day 5 for 19,196 genes as a function of mianserin concentration. For each concentration, drift-variances were calculated for 5-day-old animals that were treated with increasing concentrations of mianserin on day 1, and plotted as Tukey-style box plots as a function of mianserin concentrations, excluding outliers. Outliers were only removed for graphical purposes but not for statistical testing (robust Levene’s test).

Young reference: To obtain a “young reference” value for each individual gene, the mean expression level across all three biological replicates of young day 1 old water-treated C. elegans animals was calculated.

Figure 2d: Drift plots show transcriptional drift on day 10 of adulthood for 19,196 genes as a function of age when mianserin-treatment was started. Tukey plots show drift-variance calculated for the entire transcriptome on day 10 (Equation 3) as a function of age at which mianserin-treatment was initiated.

Young reference: To obtain a “young reference” value for each individual gene, the mean expression levels across all three biological replicates of young day 1 old water-treated C. elegans animals was calculated.

Figure 2f: Log2 fold changes in expression for each gene shown in the y-axis were calculated by the formula: y = log2(cpm treatment day 10/cpm water day 1).

Figure 2g: The data from Murphy et al. were dowloaded from the Princeton Puma database. Expression values were calculated using the following variables in the data-set: expression value = ch1netmean/ch2normalizednetmean. Drift plots for control- RNAi, daf-2(RNAi) treated and daf-16(RNAi); daf-2(RNAi) treated animals were plotted as transcriptional drift-variance as a function of C. elegans age. To plot drift-variance for the entire transcriptome as function of age in days, we binned the data as follows. Day 0 (8 hr), day 1 (24 hr), day 2 (28 hr, 40 hr, 52 hr), day 4 (72 hr, 96 hr), day 6 (144 hr, 196 hr).

Young reference: As a “young reference” value for each individual gene we used the expression level at 8 hr of age. The young reference was determined for each RNAi treatement specifically (control RNAi, daf-16(RNAi); daf-2(RNAi), daf-2(RNAi).

Figure 3e: The log fold gene expression with age was calculated for each of the 252 genes that are known to be upregulated in response to oxidative stress and for each of the 88 genes known to be downregulated in response to oxidative stress. We then performed a linear fit for each set of genes for water-treated (gray) and mianserin-treated (blue) samples. Shaded region shows the 95% confidence interval.

Figure 7a, b: 7a) Drift plots showing transcriptional drift and drift-variance in different tissues across different mouse ages. For each age, the drift-variance was calculated across the entire transcriptome (Equation 3) and plotted as Tukey-style box plots omitting outliers. As only three mice were available for each age, we pooled two ages for each age bin.

7b) Drift-variance for each tissue as a function of age.

Young Reference: 7a: To obtain a “young reference” value for each individual gene, the mean expression level across all three biological replicates of young 13-week-old mice was calculated for each tissue.

Young Reference 7b: To obtain “young reference” values for each individual gene, we used one single 13-week-old replicate as a “young reference” from each tissue. The data from the “young reference” did not contribute to the graph and thus show a real transcriptional drift-variance.

Figure 7c, d: 7c). Drift plots showing transcriptional drift-variance in human gene expression data from frontal cortices as a function of age. For 7c, the data were pooled into 20 year bins.

7d) Plots drift-variance calculated based on Equation 3 as a function of age for each sample individually.

Young Reference: To obtain “young reference” values for each individual gene, the mean gene expression levels was calculated averaging expression levels from 4 samples aged 25 to 29 years and used as the “young reference” value in Equation 1.

Figure 2—figure supplement 1: e) The transcriptional drift plots were constructed by using the GEO data-sets GSE21784 and GSE46051, which are independent publicly available data-sets for aging C. elegans.

f) The transcriptional drift plots were constructed by sub-sampling the data from our RNA-seq. We randomly assigned half of all genes (out of 19,196) to one of 10 gene-sets each containing ~1000 genes (5%) and plotted the drift-variance for each set. All 10 sets look nearly indistinguishable to Figure 2a.

Figure 2—figure supplement 2: f) The drift plot was constructed by removing all the genes from our data-set that were not detected in the sterile CF512 strain, thereby removing genes likely resulting from eggs and germline.

g) The drift plot was constructed by removing all genes from our data-set that were detected by RNA-seq in isolated C. elegans eggs.

k) Gene-sets enriched in AFD neurons (left plot), ASE neurons (middle plot) and NSM neurons (right plot) were used to construct drift plots based on their expression in our data-set.

### Principle component analysis

Principal components analysis plot (Figure 6a) was generated from the counts table using multidimensional scaling as implemented by the plotMDS function in the edgeR package, which computes inter-sample distances as the root-mean-square of the 500 genes with the largest log2 fold-changes between each pair of sample (the 'leading log fold-change").

### Chemicals

Solvents used to prepare stock solutions: Paraquat was dissolved in water; mianserin was dissolved either in water or DMSO as mentioned; Mirtazapine, Dihydroergotamine, LY-165,163/PAPP, Mirtazapine, Metergoline, Ketanserin, Methiothepin, and Amperozide were dissolved in DMSO; FUDR was dissolved in S-complete (Table 9).

**Table 9.**
 List of small molecules and chemicals used in this study with information


<table>
  <thead>
    <tr>
      <th>Molecule name</th>
      <th>CAS number</th>
      <th>Catalog number</th>
      <th>Manufacturer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Mianserin HCl</td>
      <td>21535-47-7</td>
      <td>0997</td>
      <td>Tocris</td>
    </tr>
    <tr>
      <td>Mirtazapine</td>
      <td>85650-52-8</td>
      <td>M3368</td>
      <td>LKT Laboratories</td>
    </tr>
    <tr>
      <td>Dihydroergotamine mesylate</td>
      <td>6190-39-2</td>
      <td>0475</td>
      <td>Tocris/R&amp;D systems</td>
    </tr>
    <tr>
      <td>LY-165,163/PAPP</td>
      <td>1814-64-8</td>
      <td>S009</td>
      <td>Sigma</td>
    </tr>
    <tr>
      <td>Mirtazapine</td>
      <td>61337-67-5</td>
      <td>M3368</td>
      <td>LKT labs</td>
    </tr>
    <tr>
      <td>Metergoline</td>
      <td>17692-51-2</td>
      <td>M3668</td>
      <td>Sigma</td>
    </tr>
    <tr>
      <td>Ketanserin tartarate</td>
      <td>83846-83-7</td>
      <td>S006</td>
      <td>Sigma</td>
    </tr>
    <tr>
      <td>Methiothepin mesylate</td>
      <td>74611-28-2</td>
      <td>M149</td>
      <td>Sigma</td>
    </tr>
    <tr>
      <td>Amperozide HCl</td>
      <td>86725-37-3</td>
      <td>2746</td>
      <td>Tocris/R&amp;D systems</td>
    </tr>
    <tr>
      <td>Paraquat (Methyl viologen)</td>
      <td>1910-42-5</td>
      <td>AC227320010</td>
      <td>Acros Organics</td>
    </tr>
    <tr>
      <td>FUDR</td>
      <td>50-91-9</td>
      <td>F0503</td>
      <td>Sigma-Aldrich</td>
    </tr>
    <tr>
      <td>DMSO</td>
      <td>67-68-5</td>
      <td>472301</td>
      <td>Sigma-Aldrich</td>
    </tr>
  </tbody>
</table>

### Strains

Detailed descriptions of all strains used in this study are tabulated below. All strains were backcrossed at least 4 times with the N2 Bristol strain. All strains were maintained as described in (Brenner, 1974). The strains with name starting with VV were generated by outcrossing to N2 Bristol strain in our lab (Table 10).

**Table 10.**
 List of mutant and fluorescent strains outcrossed and used in this study.


<table>
  <thead>
    <tr>
      <th>Strain name</th>
      <th>Genotype</th>
      <th>No.of times outcrossed</th>
      <th>Gene name</th>
      <th>Transgene</th>
      <th>Allele</th>
      <th>Parent strain(s)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>VV78</td>
      <td>unc-26 (e205) IV</td>
      <td>4</td>
      <td>unc-26</td>
      <td></td>
      <td>e205</td>
      <td>CB205</td>
    </tr>
    <tr>
      <td>VV80</td>
      <td>snt-1 (md290) II</td>
      <td>4</td>
      <td>snt-1</td>
      <td></td>
      <td>md290</td>
      <td>NM204</td>
    </tr>
    <tr>
      <td>MT15434</td>
      <td>tph-1 (mg280) II</td>
      <td>4</td>
      <td>tph-1</td>
      <td></td>
      <td>mg280</td>
      <td>MT15434</td>
    </tr>
    <tr>
      <td>DA1814</td>
      <td>ser-1 (ok345) X</td>
      <td>10</td>
      <td>ser-1</td>
      <td></td>
      <td>ok345</td>
      <td>DA1814</td>
    </tr>
    <tr>
      <td>OH313</td>
      <td>ser-2 (pk1357) X</td>
      <td>4</td>
      <td>ser-2</td>
      <td></td>
      <td>pk1357</td>
      <td>OH313</td>
    </tr>
    <tr>
      <td>DA1774</td>
      <td>ser-3 (ad1774) I</td>
      <td>3</td>
      <td>ser-3</td>
      <td></td>
      <td>ad1774</td>
      <td>DA1774</td>
    </tr>
    <tr>
      <td>AQ866</td>
      <td>ser-4 (ok512) III</td>
      <td>5</td>
      <td>ser-4</td>
      <td></td>
      <td>ok512</td>
      <td>AQ866</td>
    </tr>
    <tr>
      <td>VV130</td>
      <td>ser-5(ok3087) I</td>
      <td>4</td>
      <td>ser-5</td>
      <td></td>
      <td>ok3087</td>
      <td>RB2277</td>
    </tr>
    <tr>
      <td>FX2647</td>
      <td>ser-5 (tm2647) I</td>
      <td>0</td>
      <td>ser-5</td>
      <td></td>
      <td>tm2647</td>
      <td>FX2647</td>
    </tr>
    <tr>
      <td>FX2654</td>
      <td>ser-5 (tm2654) I</td>
      <td>0</td>
      <td>ser-5</td>
      <td></td>
      <td>tm2654</td>
      <td>FX2654</td>
    </tr>
    <tr>
      <td>FX2146</td>
      <td>ser-6 (tm2146) IV</td>
      <td>0</td>
      <td>ser-6</td>
      <td></td>
      <td>tm2146</td>
      <td>FX2146</td>
    </tr>
    <tr>
      <td>DA2100</td>
      <td>ser-7 (tm1325) X</td>
      <td>10</td>
      <td>ser-7</td>
      <td></td>
      <td>tm1325</td>
      <td>DA2100</td>
    </tr>
  </tbody>
</table>

### Lifespan assay and analysis

Lifespan assays were conducted in 96-well plates as described in (Solis and Petrascheck, 2011; Rangaraju et al., 2015b). Briefly, age-synchronized animals were cultured in S-complete media containing E. coli OP50 as feeding bacteria (~2 × 109 bacteria mL−1) in 96-well plates, such that 5–15 worms are in each well. At the L4 stage, FUDR was added to prevent animals from producing offspring. Solvent (water or DMSO) or small molecules were added on day 1 of adulthood, exposing the worms to control or compound treatment until the end of the assay. When used, DMSO was kept to a final concentration of 0.33% v/v. Live animals were scored visually, based on movement induced by shaking and application of light to each well. Animals were scored three times a week, until 95% of animals were dead in all the tested conditions. Statistical analysis was performed using the Mantel–Haenszel version of the log-rank test.

### Stress resistance assays

Resistance to oxidative stress was determined by measuring survival of mianserin-treated and untreated worms after a 24 hr exposure to the ROS-generator paraquat (Methyl viologen). Experimental worm cultures were set up as described in Lifespan assays. For dose response assays, paraquat was added to a final concentration of 0, 25, 50, 75, 100 mM on day 5 of adulthood. For paraquat time-course experiment (Figure 3c), paraquat was added 3 days, 5 days, or 10 days after addition of mianserin on day 1 of adulthood. For mianserin time-course experiment (Figure 3d), 50 µM mianserin was added on day 1, day 3 or 5 of adulthood, followed by 100 mM paraquat on day 10. For all experiments, survival of worms was assessed 24 hr after paraquat addition and expressed as the percentage of live versus total animals.

### RNA-sequencing (RNA-seq) transcriptional studies and data analysis

Mianserin-induced changes in transcription were determined by RNA-seq. A total of 12 conditions were tested each run in three biological replicates. N2 worms were cultured in 96-well plates as described in (Solis and Petrascheck, 2011). Animals in cohort #1 were treated on day 1 with water (solvent) or 50 µM mianserin, and harvested on day 3, 5, and 10 of adulthood. Animals in cohort #2 were treated with water (solvent control) or mianserin (2, 10, or 50 µM) on day 1 of adulthood and harvested on day 5. Animals in cohort #3 were treated with water (solvent) or 50 µM mianserin on day 1, day 3 and day 5 and harvested on day 10 (See Figure 1a). RNA was also harvested from untreated day 1 adults, to obtain the “young reference”. Harvested animals were washed three times in ice cold Dulbecco’s phosphate buffer saline and frozen in liquid nitrogen. A parallel lifespan assay was conducted for all cohorts to ensure mianserin action. Three biological replicates were harvested for every cohort. To extract RNA, frozen worms were re-suspended in ice-cold Trizol, zirconium beads, and glass beads (cat # 03961-1-103 and cat # 03961-1-104) in the ratio of 5:1:1 respectively, and disrupted in Precellys lysing system (6500 rpm, 3 x 10 s cycles) followed by chloroform extraction. For RNA-seq, the extracted RNA was precipitated and purified further using Qiagen RNAeasy Mini kit columns (cat # 74104). RNA was precipitated using isopropanol and washed once with 75% ethanol. Integrity of the RNA was confirmed with a Bioanalyzer (Agilent Technologies, Santa Clara, CA, USA). To prepare the library, 100 ng of total RNA per sample was processed using NuGEN Encore Complete DR RNA-seq Prep Kit (NuGEN; San Carlos; CA, USA), as per manufacturer’s instructions. The libraries were sequenced using v2 sequencing chemistry in a HiSeq2000 platform (Illumina, San Diego, CA, USA). A single-read sequencing approach was used with 100 cycles, resulting in reads with a length of 100 nucleotides each. Libraries containing their own index sequences were sequenced in a multiplex manner by pooling six libraries per lane. Resulting sequences were obtained after 20–30 million reads per sample. Sequence data were extracted in FASTQ format and used for data analysis.

### RNA-seq data analysis

RNA-seq data were analyzed by aligning the reads to the C. elegans reference genome and transcriptome from WormBase using Tophat 2 (Kim et al., 2013), and unambiguously mapped reads were counted for each annotated gene in each sample (Lawrence et al., 2013). Data were normalized for sequencing depths (counts per million, cpm) but not for gene length as no comparisons between genes within the same sample were made. The quasi-likelihood F-test from the edgeR package (Robinson and Oshlack, 2010; Lund et al., 2012) was used to test these counts for statistically significant differential gene expression between water- and mianserin-treated samples, while controlling for expression differences between the 3 biological replicates. We performed multiple testing correction by using the Benjamini-Hochberg procedure to compute a false discovery rate (FDR) value for each gene, and we considered an FDR less than 10% to be significant (Benjamini and Hochberg, 1995; Zhang et al., 2009).

### Quantitative real-time PCR (qRT-PCR) and data analysis

All qRT-PCR experiments were conducted according to the MIQE guidelines (Bustin et al., 2009), except that samples were not tested in a bio-analyzer, but photometrically quantified using a Nanodrop. All strains were cultured in 96-well plates as described in (Solis and Petrascheck, 2011). Water (solvent) or mianserin were added on day 1 of adulthood and worms were harvested on day 5. RNA was extracted as described above, followed by DNAse (Sigma, cat # AMPD1-1KT) treatment and reverse transcription using iScript RT-Supermix (BIO-RAD, cat # 170–8841) at 42ºC for 30 min. Quantitative PCR reactions were set up in 384-well plates (BIO-RAD, cat # HSP3901), which included 2.5 µl Bio-Rad SsoAdvanced SYBR Green Supermix (cat # 172–5264) or Kapa SYBR Fast master mix (cat # KK4602), 1 µl cDNA template (2.5 ng/µl, to final of 0.5 ng/µl in 5 µl PCR reaction), 1 µl water, and 0.5 µl of forward and reverse primers (150 nM final concentration for BIO-RAD SYBR mix and 75 nM final for Kapa SYBR mix) (see Table below for oligo pairs used for qRT-PCR of genes tested). Quantitative PCR was carried out using a BIO-RAD CFX384 Real-Time thermocycler (95ºC, 3 min; 40 cycles of 95ºC 10 s, 60ºC 30 s; Melting curve: 95ºC 5 s, 60ºC- 95ºC at 0.5ºC increment, 10 s). Gene expression was normalized to three reference genes, rcq-5, crn-3 and rpl-6, using the BIO-RAD CFX Manager software. Statistical significance was determined using Student’s t-test (Table 11).

**Table 11.**
 List of oligos used for qRT-PCR


<table>
  <thead>
    <tr>
      <th>Gene name</th>
      <th>qRT-PCR forward primer (5’-3’)</th>
      <th>qRT-PCR reverse primer (5’-3’)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>sod-1</td>
      <td>CGTAGGCGATCTAGGAAATGTG</td>
      <td>AACAACCATAGATCGGCCAACG</td>
    </tr>
    <tr>
      <td>sod-2</td>
      <td>TTCAACCGATCACAGGAGTC</td>
      <td>GCTCCAAATCAGCATAGTCG</td>
    </tr>
    <tr>
      <td>sod-3</td>
      <td>ATGGACACTATTAAGCGCGA</td>
      <td>GCCTTGAACCGCAATAGTG</td>
    </tr>
    <tr>
      <td>sod-4</td>
      <td>ATGTGGAACTATCGGAATTGTG</td>
      <td>GGTTGAGATTGTGTAACTGGA</td>
    </tr>
    <tr>
      <td>sod-5</td>
      <td>ATGGAGACTCAACCGATGG</td>
      <td>GACCACGGAATCTCTTCCT</td>
    </tr>
    <tr>
      <td>ctl-1</td>
      <td>AATGGATACGGAGCGCATAC</td>
      <td>AACCTTGAGCAGGCTTGAAA</td>
    </tr>
    <tr>
      <td>ctl-2</td>
      <td>TGATTACCCACTGATCGAGG</td>
      <td>GCGGATTGTTCAACCTCAG</td>
    </tr>
    <tr>
      <td>ctl-3</td>
      <td>CAATCTAACGGTCAACGACAC</td>
      <td>CATTGGATGTGGTGAGCAG</td>
    </tr>
    <tr>
      <td>prdx-2</td>
      <td>CATTCCAGTTCTCGCTGAC</td>
      <td>ATGATGAAGAGTCCACGGA</td>
    </tr>
    <tr>
      <td>prdx-3</td>
      <td>GTTCCGTTCTCTTGGAGCTG</td>
      <td>CTTGTTGAAATCAGCGAGCA</td>
    </tr>
    <tr>
      <td>prdx-6</td>
      <td>GGAGAACAATGGCTGATGC</td>
      <td>ATCTGAACATGGCGTTTGC</td>
    </tr>
    <tr>
      <td>hsp-16.1</td>
      <td>ACCACTATTTCCGTCCAGCT</td>
      <td>TGACGTTCCATCTGAGCCAT</td>
    </tr>
    <tr>
      <td>hsp-16.11</td>
      <td>ACCACTATTTCCGTCCAGCT</td>
      <td>TGACGTTCCATCTGAGCCAT</td>
    </tr>
    <tr>
      <td>hsp-16.2</td>
      <td>TCGATTGAAGCGCCAAAGAA</td>
      <td>TCTCTTCGACGATTGCCTGT</td>
    </tr>
    <tr>
      <td>hsp-16.41</td>
      <td>TCTTGGACGAACTCACTGGA</td>
      <td>TCTTGGACGAACTCACTGGA</td>
    </tr>
    <tr>
      <td>hsp-16.48</td>
      <td>CTCATGCTCCGTTCTCCATT</td>
      <td>GAGTTGTGATCAGCATTTCTCCA</td>
    </tr>
    <tr>
      <td>hsp-16.49</td>
      <td>CTCATGCTCCGTTCTCCATT</td>
      <td>GAGTTGTGATCAGCATTTCTCCA</td>
    </tr>
    <tr>
      <td>crn-3</td>
      <td>GAATGCACTCATGAACAAAGTC</td>
      <td>TAATGTTCGACTGATGAACCG</td>
    </tr>
    <tr>
      <td>rcq-5</td>
      <td>GATGTTAGAGCTGTAATTCACTGG</td>
      <td>ATCTCTTCCAGCTCTTCCG</td>
    </tr>
    <tr>
      <td>rpl-6</td>
      <td>TTCACCAAGGACACTAGCG</td>
      <td>GACAGTCTTGGAATGTCCGA</td>
    </tr>
  </tbody>
</table>

### Measurement of 26S proteasome activity

Wild-type N2 worms were cultured as described (Solis and Petrascheck, 2011). Water or Mianserin 50 µM were added on day 1 and 26S proteasome activity was assayed on day 2 and day 5 using the Millipore Proteasome activity kit (cat# APT280), following manufacturer’s protocol. Equal number of worms per condition were washed off culture media using ice cold Dulbecco’s phosphate buffer saline and freshly lysed using Precellys system (6500 rpm, 3 x 10 s cycles) in assay buffer (25 mM HEPES, pH 7.5, 0.5mM EDTA, 0.05% NP-40, and 0.001% SDS (w/v)). Chymotrypsin-like proteasome activity in the lysates were assessed using the Suc-LLVY-AMC substrate and fluorogenic AMC substrate cleavage was measured in 20 min intervals for 120 min. A subset of lysates were pre-incubated with Lactacystin (12.5 µM final) to ensure specificity of AMC cleavage by 26S proteasome. The amount of cleaved AMC fragments were quantified using TECAN xfluor safire II system at excitation of 360 nm and emission of 480 nm. The resulting readings were normalized to the total protein content in the samples measured using Bradford assay.

### Mortality curve and probability of detection

Mortality curves were generated based on the life table provided in Figure 6—figure supplement 1, tabulating death times of 15 independent experiments performed over 5 years. Each experiment consisted of 2 cohorts (water or 50 µM mianserin) and each cohort consisted of ~100 worms each amounting to ~1500 worms per condition. Power of detection was determined by Monte-Carlo simulations using a parametric model with parameters derived from our survival data of a cohort of over 5,026 N2 animals. The power of detection plot (Figure 6—figure supplement 1) shows the probability to detect a true lifespan extension with a significance level α=0.01 as a function of percent increase in lifespan for an experiment consisting of n animals. An accuracy of 1 day is the equivalent of a 5% increase in lifespan.
