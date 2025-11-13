# Limitations of principal components in quantitative genetic association models for human studies

## Authors

- Yiqi Yao<sup>1</sup>
- Alejandro Ochoa<sup>1</sup> ([ORCID: 0000-0003-4928-3403](https://orcid.org/0000-0003-4928-3403)) †

### Affiliations

1. Department of Biostatistics and Bioinformatics, Duke University Durham United States ([ROR:00py81415](https://ror.org/00py81415))
2. Duke Center for Statistical Genetics and Genomics, Duke University Durham United States ([ROR:00py81415](https://ror.org/00py81415))

† Corresponding author

## Abstract

Principal Component Analysis (PCA) and the Linear Mixed-effects Model (LMM), sometimes in combination, are the most common genetic association models. Previous PCA-LMM comparisons give mixed results, unclear guidance, and have several limitations, including not varying the number of principal components (PCs), simulating simple population structures, and inconsistent use of real data and power evaluations. We evaluate PCA and LMM both varying number of PCs in realistic genotype and complex trait simulations including admixed families, subpopulation trees, and real multiethnic human datasets with simulated traits. We find that LMM without PCs usually performs best, with the largest effects in family simulations and real human datasets and traits without environment effects. Poor PCA performance on human datasets is driven by large numbers of distant relatives more than the smaller number of closer relatives. While PCA was known to fail on family data, we report strong effects of family relatedness in genetically diverse human datasets, not avoided by pruning close relatives. Environment effects driven by geography and ethnicity are better modeled with LMM including those labels instead of PCs. This work better characterizes the severe limitations of PCA compared to LMM in modeling the complex relatedness structures of multiethnic human data for association studies.

## Introduction

The goal of a genetic association study is to identify loci whose genotype variation is significantly correlated to given trait. Naive association tests assume that genotypes are drawn independently from a common allele frequency. This assumption does not hold for structured populations, which includes multiethnic cohorts and admixed individuals (ancient relatedness), and for family data (recent relatedness; Astle and Balding, 2009). Association studies of admixed and multiethnic cohorts, the focus of this work, are becoming more common, are believed to be more powerful, and are necessary to bring more equity to genetic medicine (Rosenberg et al., 2010; Hoffman and Dubé, 2013; Coram et al., 2013; Medina-Gomez et al., 2015; Conomos et al., 2016a; Hodonsky et al., 2017; Martin et al., 2017a; Martin et al., 2017b; Hindorff et al., 2018; Hoffmann et al., 2018; Mogil et al., 2018; Roselli et al., 2018; Wojcik et al., 2019; Peterson et al., 2019; Zhong et al., 2019; Hu et al., 2020; Simonin-Wilmer et al., 2021; Kamariza et al., 2021; Lin et al., 2021; Mahajan et al., 2022; Hou et al., 2023a). When insufficient approaches are applied to data with relatedness, their association statistics are miscalibrated, resulting in excess false positives and loss of power (Devlin and Roeder, 1999; Voight and Pritchard, 2005; Astle and Balding, 2009). Therefore, many specialized approaches have been developed for genetic association under relatedness, of which PCA and LMM are the most popular.

Genetic association with PCA consists of including the top eigenvectors of the population kinship matrix as covariates in a generalized linear model (Zhang et al., 2003; Price et al., 2006; Bouaziz et al., 2011). These top eigenvectors are a new set of coordinates for individuals that are commonly referred to as PCs in genetics (Patterson et al., 2006), the convention adopted here, but in other fields PCs instead denote what in genetics would be the projections of loci onto eigenvectors, which are new independent coordinates for loci (Jolliffe, 2002). The direct ancestor of PCA association is structured association, in which inferred ancestry (genetic cluster membership, often corresponding with labels such as “European”, “African”, “Asian”, etc.) or admixture proportions of these ancestries are used as regression covariates (Pritchard et al., 2000). These models are deeply connected because PCs map to ancestry empirically (Alexander et al., 2009; Zhou et al., 2016) and theoretically (McVean, 2009; Zheng and Weir, 2016; Cabreros and Storey, 2019; Chiu et al., 2022), and they work as well as global ancestry in association studies but are estimated more easily (Patterson et al., 2006; Zhao et al., 2007; Alexander et al., 2009; Bouaziz et al., 2011). Another approach closely related to PCA is nonmetric multidimensional scaling (Zhu and Yu, 2009). PCs are also proposed for modeling environment effects that are correlated to ancestry, for example, through geography (Novembre et al., 2008; Zhang and Pan, 2015; Lin et al., 2021). The strength of PCA is its simplicity, which as covariates can be readily included in more complex models, such as haplotype association (Xu and Guan, 2014) and polygenic models (Qian et al., 2020). However, PCA assumes that the underlying relatedness space is low dimensional (or low rank), so it can be well modeled with a small number of PCs, which may limit its applicability. PCA is known to be inadequate for family data (Patterson et al., 2006; Zhu and Yu, 2009; Thornton and McPeek, 2010; Price et al., 2010), which is called ‘cryptic relatedness’ when it is unknown to the researchers, but no other troublesome cases have been confidently identified. Recent work has focused on developing more scalable versions of the PCA algorithm (Lee et al., 2012; Abraham and Inouye, 2014; Galinsky et al., 2016; Abraham et al., 2017; Agrawal et al., 2020). PCA remains a popular and powerful approach for association studies.

The other dominant association model under relatedness is the LMM, which includes a random effect parameterized by the kinship matrix. Unlike PCA, LMM does not assume that relatedness is low-dimensional, and explicitly models families via the kinship matrix. Early LMMs used kinship matrices estimated from known pedigrees or using methods that captured recent relatedness only, and modeled population structure (ancestry) as fixed effects (Yu et al., 2006; Zhao et al., 2007; Zhu and Yu, 2009). Modern LMMs estimate kinship from genotypes using a non-parametric estimator, often referred to as a genetic relationship matrix, that captures the combined covariance due to family relatedness and ancestry (Kang et al., 2008; Astle and Balding, 2009; Ochoa and Storey, 2021). Like PCA, LMM has also been proposed for modeling environment correlated to genetics (Vilhjálmsson and Nordborg, 2013; Wang et al., 2022). The classic LMM assumes a quantitative (continuous) complex trait, the focus of our work. Although case-control (binary) traits and their underlying ascertainment are theoretically a challenge (Yang et al., 2014), LMMs have been applied successfully to balanced case-control studies (Astle and Balding, 2009; Kang et al., 2010) and simulations (Price et al., 2010; Wu et al., 2011; Sul and Eskin, 2013), and have been adapted for unbalanced case-control studies (Zhou et al., 2018). However, LMMs tend to be considerably slower than PCA and other models, so much effort has focused on improving their runtime and scalability (Aulchenko et al., 2007; Kang et al., 2008; Kang et al., 2010; Zhang et al., 2010; Lippert et al., 2011; Yang et al., 2011; Listgarten et al., 2012; Zhou and Stephens, 2012; Svishcheva et al., 2012; Loh et al., 2015; Zhou et al., 2018).

An LMM variant that incorporates PCs as fixed covariates is tested thoroughly in our work. Since PCs are the top eigenvectors of the same kinship matrix estimate used in modern LMMs (Astle and Balding, 2009; Janss et al., 2012; Hoffman and Dubé, 2013; Zhang and Pan, 2015), then population structure is modeled twice in an LMM with PCs. However, some previous work has found the apparent redundancy of an LMM with PCs beneficial (Price et al., 2010; Tucker et al., 2014; Zhang and Pan, 2015), while others did not (Liu et al., 2011; Janss et al., 2012), and the approach continues to be used (Zeng et al., 2018; Mbatchou et al., 2021), although not always (Matoba et al., 2020). Recall that early LMMs used kinship to model family relatedness only, so population structure had to be modeled separately in those models, in practice as admixture fractions instead of PCs (Yu et al., 2006; Zhao et al., 2007; Zhu and Yu, 2009). The LMM with PCs (vs no PCs) is also believed to help better model loci that have experienced selection (Price et al., 2010; Vilhjálmsson and Nordborg, 2013) and environment effects correlated with genetics (Zhang and Pan, 2015).

LMM and PCA are closely related models (Astle and Balding, 2009; Janss et al., 2012; Hoffman and Dubé, 2013; Zhang and Pan, 2015), so similar performance is expected particularly under low-dimensional relatedness. Direct comparisons have yielded mixed results, with several studies finding superior performance for LMM, notably from papers promoting advances in LMMs, while many others report comparable performance (Table 1). No papers find that PCA outperforms LMM decisively, although PCA occasionally performs better in isolated and artificial cases or individual measures, often with unknown significance. Previous studies generally used either only simulated or only real genotypes, with only two studies using both. The simulated genotype studies, which tended to have low model dimensions and $F_{ST}$, were more likely to report ties or mixed results (6/8), whereas real genotypes tended to clearly favor LMMs (9/11). Similarly, 10/12 papers with quantitative traits favor LMMs, whereas 6/9 papers with case-control traits gave ties or mixed results—the only factor we do not explore in this work. Additionally, although all previous evaluations measured type I error (or proxies such as genomic inflation factors Devlin and Roeder, 1999 or QQ plots), a large fraction (6/17) did not measure power (or proxies such as ROC curves), and only four used more than one number of PCs for PCA. Lastly, no consensus has emerged as to why LMM might outperform PCA or vice versa (Price et al., 2010; Sul and Eskin, 2013; Price et al., 2013; Hoffman and Dubé, 2013), or which features of the real datasets are critical for the LMM advantage other than family relatedness, resulting in unclear guidance for using PCA. Hence, our work includes real and simulated genotypes with higher model dimensions and $F_{ST}$ matching that of multiethnic human cohorts (Ochoa and Storey, 2021; Ochoa and Storey, 2019), we vary the number of PCs, and measure robust proxies for type I error control and calibrated power.

**Table 1.**
 Previous PCA-LMM evaluations in the literature.


<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="3">Sim. Genotypes</th>
      <th>General</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
    <tr>
      <th>Publication</th>
      <th>Type*</th>
      <th>K†</th>
      <th>FST‡</th>
      <th>Real §</th>
      <th>Trait ¶</th>
      <th>Power</th>
      <th>PCs(r)</th>
      <th>Best</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Zhao et al., 2007</td>
      <td></td>
      <td></td>
      <td></td>
      <td>✓</td>
      <td>Q</td>
      <td>✓</td>
      <td>8</td>
      <td>LMM</td>
    </tr>
    <tr>
      <td>Zhu and Yu, 2009</td>
      <td>I, A, F</td>
      <td>3, 8</td>
      <td>≤0.15</td>
      <td>✓</td>
      <td>Q</td>
      <td>✓</td>
      <td>1–22</td>
      <td>LMM</td>
    </tr>
    <tr>
      <td>Astle and Balding, 2009</td>
      <td>I</td>
      <td>3</td>
      <td>0.10</td>
      <td></td>
      <td>CC</td>
      <td>✓</td>
      <td>10</td>
      <td>Tie</td>
    </tr>
    <tr>
      <td>Kang et al., 2010</td>
      <td></td>
      <td></td>
      <td></td>
      <td>✓</td>
      <td>Both</td>
      <td></td>
      <td>2–100</td>
      <td>LMM</td>
    </tr>
    <tr>
      <td>Price et al., 2010</td>
      <td>I, F</td>
      <td>2</td>
      <td>0.01</td>
      <td></td>
      <td>CC</td>
      <td></td>
      <td>1</td>
      <td>Mixed</td>
    </tr>
    <tr>
      <td>Wu et al., 2011</td>
      <td>I, A</td>
      <td>2–4</td>
      <td>0.01</td>
      <td></td>
      <td>CC</td>
      <td>✓</td>
      <td>10</td>
      <td>Mixed</td>
    </tr>
    <tr>
      <td>Liu et al., 2011</td>
      <td>S, A</td>
      <td>2–3</td>
      <td>R</td>
      <td></td>
      <td>Q</td>
      <td>✓</td>
      <td>10</td>
      <td>Tie</td>
    </tr>
    <tr>
      <td>Sul and Eskin, 2013</td>
      <td>I</td>
      <td>2</td>
      <td>0.01</td>
      <td></td>
      <td>CC</td>
      <td></td>
      <td>1</td>
      <td>Tie</td>
    </tr>
    <tr>
      <td>Tucker et al., 2014</td>
      <td>I</td>
      <td>2</td>
      <td>0.05</td>
      <td>✓</td>
      <td>Both</td>
      <td>✓</td>
      <td>5</td>
      <td>Tie</td>
    </tr>
    <tr>
      <td>Yang et al., 2014</td>
      <td></td>
      <td></td>
      <td></td>
      <td>✓</td>
      <td>CC</td>
      <td>✓</td>
      <td>5</td>
      <td>Tie</td>
    </tr>
    <tr>
      <td>Song et al., 2015</td>
      <td>S, A</td>
      <td>2–3</td>
      <td>R</td>
      <td></td>
      <td>Q</td>
      <td></td>
      <td>3</td>
      <td>LMM</td>
    </tr>
    <tr>
      <td>Loh et al., 2015</td>
      <td></td>
      <td></td>
      <td></td>
      <td>✓</td>
      <td>Q</td>
      <td>✓</td>
      <td>10</td>
      <td>LMM</td>
    </tr>
    <tr>
      <td>Zhang and Pan, 2015</td>
      <td></td>
      <td></td>
      <td></td>
      <td>✓</td>
      <td>Q</td>
      <td>✓</td>
      <td>20–100</td>
      <td>LMM</td>
    </tr>
    <tr>
      <td>Liu et al., 2016</td>
      <td></td>
      <td></td>
      <td></td>
      <td>✓</td>
      <td>Q</td>
      <td>✓</td>
      <td>3–6</td>
      <td>LMM</td>
    </tr>
    <tr>
      <td>Sul et al., 2018</td>
      <td></td>
      <td></td>
      <td></td>
      <td>✓</td>
      <td>Q</td>
      <td></td>
      <td>100</td>
      <td>LMM</td>
    </tr>
    <tr>
      <td>Loh et al., 2018</td>
      <td></td>
      <td></td>
      <td></td>
      <td>✓</td>
      <td>Both</td>
      <td>✓</td>
      <td>20</td>
      <td>LMM</td>
    </tr>
    <tr>
      <td>Mbatchou et al., 2021</td>
      <td></td>
      <td></td>
      <td></td>
      <td>✓</td>
      <td>Both</td>
      <td></td>
      <td>1</td>
      <td>LMM</td>
    </tr>
    <tr>
      <td>This work</td>
      <td>A, T, F</td>
      <td>10–243</td>
      <td>≤0.25</td>
      <td>✓</td>
      <td>Q</td>
      <td>✓</td>
      <td>0–90</td>
      <td>LMM</td>
    </tr>
  </tbody>
</table>

_*Genotype simulation types. I: Independent subpopulations; S: subpopulations (with parameters drawn from real data); A: Admixture; T: Subpopulation Tree; F: Family.†Model dimension (number of subpopulations or ancestries).‡R: simulated parameters based on real data, FST not reported.§Evaluations using unmodified real genotypes.¶Q: quantitative; CC: case-control._

In this work, we evaluate the PCA and LMM association models under various numbers of PCs, which are included in LMMs too. We use genotype simulations (admixture, family, and subpopulation tree models) and three real datasets: the 1000 Genomes Project (Abecasis et al., 2010; Abecasis et al., 2012), the Human Genome Diversity Panel (HGDP) (Cann et al., 2002; Rosenberg et al., 2002; Bergström et al., 2020), and Human Origins (Patterson et al., 2012; Lazaridis et al., 2014; Lazaridis et al., 2016; Skoglund et al., 2016). We simulate quantitative traits from two models: fixed effect sizes (FES) construct coefficients inverse to allele frequency, which matches real data (Park et al., 2011; Zeng et al., 2018; O’Connor et al., 2019) and corresponds to high pleiotropy and strong balancing selection (Simons et al., 2018) and strong negative selection (Zeng et al., 2018; O’Connor et al., 2019), which are appropriate assumptions for diseases; and random coefficients (RC), which are drawn independent of allele frequency, and corresponds to neutral traits (Zeng et al., 2018; Simons et al., 2018). LMM without PCs consistently performs best in simulations without environment, and greatly outperforms PCA in the family simulation and in all real datasets. The tree simulations, which model subpopulations with the tree but exclude family structure, do not recapitulate the real data results, suggesting that family relatedness in real data is the reason for poor PCA performance. Lastly, removing up to 4th degree relatives in the real datasets recapitulates poor PCA performance, showing that the more numerous distant relatives explain the result, and suggesting that PCA is generally not an appropriate model for real data. We find that both LMM and PCA are able to model environment effects correlated with genetics, and LMM with PCs gains a small advantage in this setting only, but direct modeling of environment performs much better. All together, we find that LMMs without PCs are generally a preferable association model, and present novel simulation and evaluation approaches to measure the performance of these and other genetic association approaches.

## Results

### Overview of evaluations

We use three real genotype datasets and simulated genotypes from six population structure scenarios to cover various features of interest (Table 2). We introduce them in sets of three, as they appear in the rest of our results. Population kinship matrices, which combine population and family relatedness, are estimated without bias using popkin (Ochoa and Storey, 2021; Figure 1). The first set of three simulated genotypes are based on an admixture model with 10 ancestries (Figure 1A; Ochoa and Storey, 2021; Gopalan et al., 2016; Cabreros and Storey, 2019). The ‘large’ version (1000 individuals) illustrates asymptotic performance, while the ‘small’ simulation (100 individuals) illustrates model overfitting. The ‘family’ simulation has admixed founders and draws a 20-generation random pedigree with assortative mating, resulting in a complex joint family and ancestry structure in the last generation (Figure 1B). The second set of three are the real human datasets representing global human diversity: Human Origins (Figure 1D), HGDP (Figure 1G), and 1000 Genomes (Figure 1J), which are enriched for small minor allele frequencies even after MAF <1% filter (Figure 1C). Last are subpopulation tree simulations (Figure 1F, I, L) fit to the kinship (Figure 1E, H and K) and MAF (Figure 1C) of each real human dataset, which by design do not have family structure.

**Table 2.**
 Features of simulated and real human genotype datasets.


<table>
  <thead>
    <tr>
      <th>Dataset</th>
      <th>Type</th>
      <th>Loci(m)</th>
      <th>Ind. (n)</th>
      <th>Subpops.* (K)</th>
      <th>Causal loci† (m1)</th>
      <th>FST‡</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Admix. Large sim.</td>
      <td>Admix.</td>
      <td>100 000</td>
      <td>1000</td>
      <td>10</td>
      <td>100</td>
      <td>0.1</td>
    </tr>
    <tr>
      <td>Admix. Small sim.</td>
      <td>Admix.</td>
      <td>100 000</td>
      <td>100</td>
      <td>10</td>
      <td>10</td>
      <td>0.1</td>
    </tr>
    <tr>
      <td>Admix. Family sim.</td>
      <td>Admix.+Pedig.</td>
      <td>100 000</td>
      <td>1000</td>
      <td>10</td>
      <td>100</td>
      <td>0.1</td>
    </tr>
    <tr>
      <td>Human Origins</td>
      <td>Real</td>
      <td>190 394</td>
      <td>2922</td>
      <td>11–243</td>
      <td>292</td>
      <td>0.28</td>
    </tr>
    <tr>
      <td>HGDP</td>
      <td>Real</td>
      <td>771 322</td>
      <td>929</td>
      <td>7–54</td>
      <td>93</td>
      <td>0.28</td>
    </tr>
    <tr>
      <td>1000 Genomes</td>
      <td>Real</td>
      <td>1 111 266</td>
      <td>2504</td>
      <td>5–26</td>
      <td>250</td>
      <td>0.22</td>
    </tr>
    <tr>
      <td>Human Origins sim.</td>
      <td>Tree</td>
      <td>190 394</td>
      <td>2922</td>
      <td>243</td>
      <td>292</td>
      <td>0.23</td>
    </tr>
    <tr>
      <td>HGDP sim.</td>
      <td>Tree</td>
      <td>771 322</td>
      <td>929</td>
      <td>54</td>
      <td>93</td>
      <td>0.25</td>
    </tr>
    <tr>
      <td>1000 Genomes sim.</td>
      <td>Tree</td>
      <td>1 111 266</td>
      <td>2504</td>
      <td>26</td>
      <td>250</td>
      <td>0.21</td>
    </tr>
  </tbody>
</table>

_*For admixed family, ignores additional model dimension of 20 generation pedigree structure. For real datasets, lower range is continental subpopulations, upper range is number of fine-grained subpopulations.†m1=round⁡(n⁢h2/8) to balance power across datasets, shown for h2=0.8 only.‡Model parameter for simulations, estimated value on real datasets._

![Figure 1.](https://cdn.elifesciences.org/articles/79238/elife-79238-fig1-v2.jpg)

**Figure 1.:** First two columns are population kinship matrices as heatmaps: individuals along x- and y-axis, kinship as color. Diagonal shows inbreeding values. (A) Admixture scenario for both Large and Small simulations. (B) Last generation of 20-generation admixed family, shows larger kinship values near diagonal corresponding to siblings, first cousins, etc. (C) Minor allele frequency (MAF) distributions. Real datasets and subpopulation tree simulations had $MAF\geq0.01$ filter. (D) Human Origins is an array dataset of a large diversity of global populations. (G) Human Genome Diversity Panel (HGDP) is a WGS dataset from global native populations. (J) 1000 Genomes Project is a WGS dataset of global cosmopolitan populations. (F, I, L) Trees between subpopulations fit to real data. (E, H, K). Simulations from trees fit to the real data recapitulate subpopulation structure.

All traits in this work are simulated. We repeated all evaluations on two additive quantitative trait models, fixed effect sizes (FES) and random coefficients (RC), which differ in how causal coefficients are constructed. The FES model captures the rough inverse relationship between coefficient and minor allele frequency that arises under strong negative and balancing selection and has been observed in numerous diseases and other traits (Park et al., 2011; Zeng et al., 2018; Simons et al., 2018; O’Connor et al., 2019), so it is the focus of our results. The RC model draws coefficients independent of allele frequency, corresponding to neutral traits (Zeng et al., 2018; Simons et al., 2018), which results in a wider effect size distribution that reduces association power and effective polygenicity compared to FES.

We evaluate using two complementary measures: (1) $SRMSD_{p}$ (p-value signed root mean square deviation) measures p-value calibration (closer to zero is better), and (2) $AUC_{PR}$ (precision-recall area under the curve) measures causal locus classification performance (higher is better; Figure 2). $SRMSD_{p}$ is a more robust alternative to the common inflation factor $\lambda$ and type I error control measures; there is a correspondence between $\lambda$ and $SRMSD_{p}$, with $SRMSD_{p}>0.01$ giving $\lambda>1.06$ (Figure 2—figure supplement 1) and thus evidence of miscalibration close to the rule of thumb of $\lambda>1.05$ (Price et al., 2010). There is also a monotonic correspondence between $SRMSD_{p}$ and type I error rate (Figure 2—figure supplement 2). $AUC_{PR}$ has been used to evaluate association models (Rakitsch et al., 2013), and reflects calibrated statistical power (Figure 2—figure supplement 3) while being robust to miscalibrated models (Appendix 2).

![Figure 2.](https://cdn.elifesciences.org/articles/79238/elife-79238-fig2-v2.jpg)

**Figure 2.:** Three archetypal models illustrate our complementary measures: M1 is ideal, M2 overfits slightly, M3 is naive. (A) QQ plot of p-values of “null” (non-causal) loci. M1 has desired uniform p-values, M2/M3 are miscalibrated. (B)$SRMSD_{p}$ (p-value Signed Root Mean Square Deviation) measures signed distance between observed and expected null p-values (closer to zero is better). (C) Precision and Recall (PR) measure causal locus classification performance (higher is better). (D) $AUC_{PR}$ (Area Under the PR Curve) reflects power (higher is better).

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/79238/elife-79238-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Comparison between $SRMSD_{p}$ and inflation factor.Each point is a pair of statistics for one replicate, one association model (PCA or LMM with some number of PCs $r$), one trait model (FES vs RC, all heritability/environments tested), and one dataset (color coded by dataset). Note log y-axis. The sigmoidal curve in Equation 10 is fit to the data.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/79238/elife-79238-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** Comparison between $SRMSD_{p}$ and type I error rate.Type I error rate calculated at a p-value threshold of 1e-2 (horizontal dashed gray line). Thus, a calibrated model has a type I error rate of 1e-2 and $SRMSD_{p}=0$ (where the dashed lines meet). As expected, increased type I error rates correspond to $SRMSD_{p}>0$, while reduced type I error rates correspond to $SRMSD_{p}<0$. Each point is a pair of statistics for one replicate, one association model (PCA or LMM with some number of PCs $r$), one trait model (FES vs RC, all heritability/environments tested), and one dataset (color coded by dataset). Note log y-axis.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/79238/elife-79238-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** Comparison between $AUC_{PR}$ and calibrated power.Calibrated power is power calculated at an empirical type I error threshold of 1e-4. Each point is a pair of statistics for one replicate, one association model (PCA or LMM with some number of PCs $r$), one trait model (FES vs RC, all heritability/environments tested), and one dataset (color coded by dataset). Gray dashed line is $y=x$ line.

Both PCA and LMM are evaluated in each replicate dataset including a number of PCs $r$ between 0 and 90 as fixed covariates. In terms of p-value calibration, for PCA the best number of PCs $r$ (minimizing mean $|SRMSD_{p}|$ over replicates) is typically large across all datasets (Table 3), although much smaller $r$ values often performed as well (shown in following sections). Most cases have a mean $|SRMSD_{p}|<0.01$, whose p-values are effectively calibrated. However, PCA is often miscalibrated on the family simulation and real datasets (Table 3). In contrast, for LMM, $r=0$ (no PCs) is always best, and is always calibrated. Comparing LMM with $r=0$ to PCA with its best $r$, LMM always has significantly smaller $|SRMSD_{p}|$ than PCA or is statistically tied. For $AUC_{PR}$ and PCA, the best $r$ is always smaller than the best $r$ for $|SRMSD_{p}|$, so there is often a tradeoff between calibrated p-values versus classification performance. For LMM, there is no tradeoff, as $r=0$ often has the best mean $AUC_{PR}$, and otherwise is not significantly different from the best $r$. Lastly, LMM with $r=0$ always has significantly greater or statistically tied $AUC_{PR}$ than PCA with its best $r$.

**Table 3.**
 Overview of PCA and LMM evaluations for high heritability simulations.


<table>
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th colspan="3">LMM r=0 vs best r</th>
      <th colspan="4">PCA vs LMM r=0</th>
    </tr>
    <tr>
      <th>Dataset</th>
      <th>Metric</th>
      <th>Trait*</th>
      <th>Cal.†</th>
      <th>Best r‡</th>
      <th>P-value §</th>
      <th>Best r‡</th>
      <th>Cal.†</th>
      <th>P-value §</th>
      <th>Best model ¶</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Admix. Large sim.</td>
      <td>|SRMSDp|</td>
      <td>FES</td>
      <td>True</td>
      <td>0</td>
      <td>1</td>
      <td>12</td>
      <td>True</td>
      <td>0.036</td>
      <td>Tie</td>
    </tr>
    <tr>
      <td>Admix. Small sim.</td>
      <td>|SRMSDp|</td>
      <td>FES</td>
      <td>True</td>
      <td>0</td>
      <td>1</td>
      <td>4</td>
      <td>True</td>
      <td>0.055</td>
      <td>Tie</td>
    </tr>
    <tr>
      <td>Admix. Family sim.</td>
      <td>|SRMSDp|</td>
      <td>FES</td>
      <td>True</td>
      <td>0</td>
      <td>1</td>
      <td>90</td>
      <td>False</td>
      <td>3.9e-10*</td>
      <td>LMM</td>
    </tr>
    <tr>
      <td>Human Origins</td>
      <td>|SRMSDp|</td>
      <td>FES</td>
      <td>True</td>
      <td>0</td>
      <td>1</td>
      <td>89</td>
      <td>False</td>
      <td>3.9e-10*</td>
      <td>LMM</td>
    </tr>
    <tr>
      <td>HGDP</td>
      <td>|SRMSDp|</td>
      <td>FES</td>
      <td>True</td>
      <td>0</td>
      <td>1</td>
      <td>87</td>
      <td>True</td>
      <td>4.4e-10*</td>
      <td>LMM</td>
    </tr>
    <tr>
      <td>1000 Genomes</td>
      <td>|SRMSDp|</td>
      <td>FES</td>
      <td>True</td>
      <td>0</td>
      <td>1</td>
      <td>90</td>
      <td>False</td>
      <td>3.9e-10*</td>
      <td>LMM</td>
    </tr>
    <tr>
      <td>Human Origins sim.</td>
      <td>|SRMSDp|</td>
      <td>FES</td>
      <td>True</td>
      <td>0</td>
      <td>1</td>
      <td>88</td>
      <td>True</td>
      <td>0.017</td>
      <td>Tie</td>
    </tr>
    <tr>
      <td>HGDP sim.</td>
      <td>|SRMSDp|</td>
      <td>FES</td>
      <td>True</td>
      <td>0</td>
      <td>1</td>
      <td>47</td>
      <td>True</td>
      <td>0.046</td>
      <td>Tie</td>
    </tr>
    <tr>
      <td>1000 Genomes sim.</td>
      <td>|SRMSDp|</td>
      <td>FES</td>
      <td>True</td>
      <td>0</td>
      <td>1</td>
      <td>78</td>
      <td>True</td>
      <td>9.6e-10*</td>
      <td>LMM</td>
    </tr>
    <tr>
      <td>Admix. Large sim.</td>
      <td>|SRMSDp|</td>
      <td>RC</td>
      <td>True</td>
      <td>0</td>
      <td>1</td>
      <td>26</td>
      <td>True</td>
      <td>0.11</td>
      <td>Tie</td>
    </tr>
    <tr>
      <td>Admix. Small sim.</td>
      <td>|SRMSDp|</td>
      <td>RC</td>
      <td>True</td>
      <td>0</td>
      <td>1</td>
      <td>4</td>
      <td>True</td>
      <td>0.00097</td>
      <td>Tie</td>
    </tr>
    <tr>
      <td>Admix. Family sim.</td>
      <td>|SRMSDp|</td>
      <td>RC</td>
      <td>True</td>
      <td>0</td>
      <td>1</td>
      <td>90</td>
      <td>False</td>
      <td>3.9e-10*</td>
      <td>LMM</td>
    </tr>
    <tr>
      <td>Human Origins</td>
      <td>|SRMSDp|</td>
      <td>RC</td>
      <td>True</td>
      <td>0</td>
      <td>1</td>
      <td>90</td>
      <td>True</td>
      <td>0.00065</td>
      <td>Tie</td>
    </tr>
    <tr>
      <td>HGDP</td>
      <td>|SRMSDp|</td>
      <td>RC</td>
      <td>True</td>
      <td>0</td>
      <td>1</td>
      <td>37</td>
      <td>True</td>
      <td>1.5e-05*</td>
      <td>LMM</td>
    </tr>
    <tr>
      <td>1000 Genomes</td>
      <td>|SRMSDp|</td>
      <td>RC</td>
      <td>True</td>
      <td>0</td>
      <td>1</td>
      <td>76</td>
      <td>True</td>
      <td>3.9e-10*</td>
      <td>LMM</td>
    </tr>
    <tr>
      <td>Human Origins sim.</td>
      <td>|SRMSDp|</td>
      <td>RC</td>
      <td>True</td>
      <td>0</td>
      <td>1</td>
      <td>85</td>
      <td>True</td>
      <td>0.14</td>
      <td>Tie</td>
    </tr>
    <tr>
      <td>HGDP sim.</td>
      <td>|SRMSDp|</td>
      <td>RC</td>
      <td>True</td>
      <td>0</td>
      <td>1</td>
      <td>44</td>
      <td>True</td>
      <td>8.8e-07*</td>
      <td>LMM</td>
    </tr>
    <tr>
      <td>1000 Genomes sim.</td>
      <td>|SRMSDp|</td>
      <td>RC</td>
      <td>True</td>
      <td>0</td>
      <td>1</td>
      <td>90</td>
      <td>True</td>
      <td>3.9e-10*</td>
      <td>LMM</td>
    </tr>
    <tr>
      <td>Admix. Large sim.</td>
      <td>AUCPR</td>
      <td>FES</td>
      <td></td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
      <td></td>
      <td>5.9e-06*</td>
      <td>LMM</td>
    </tr>
    <tr>
      <td>Admix. Small sim.</td>
      <td>AUCPR</td>
      <td>FES</td>
      <td></td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td></td>
      <td>0.025</td>
      <td>Tie</td>
    </tr>
    <tr>
      <td>Admix. Family sim.</td>
      <td>AUCPR</td>
      <td>FES</td>
      <td></td>
      <td>1</td>
      <td>0.35</td>
      <td>22</td>
      <td></td>
      <td>3.9e-10*</td>
      <td>LMM</td>
    </tr>
    <tr>
      <td>Human Origins</td>
      <td>AUCPR</td>
      <td>FES</td>
      <td></td>
      <td>0</td>
      <td>1</td>
      <td>34</td>
      <td></td>
      <td>3.9e-10*</td>
      <td>LMM</td>
    </tr>
    <tr>
      <td>HGDP</td>
      <td>AUCPR</td>
      <td>FES</td>
      <td></td>
      <td>1</td>
      <td>0.33</td>
      <td>16</td>
      <td></td>
      <td>4.4e-10*</td>
      <td>LMM</td>
    </tr>
    <tr>
      <td>1000 Genomes</td>
      <td>AUCPR</td>
      <td>FES</td>
      <td></td>
      <td>1</td>
      <td>0.11</td>
      <td>8</td>
      <td></td>
      <td>3.9e-10*</td>
      <td>LMM</td>
    </tr>
    <tr>
      <td>Human Origins sim.</td>
      <td>AUCPR</td>
      <td>FES</td>
      <td></td>
      <td>0</td>
      <td>1</td>
      <td>36</td>
      <td></td>
      <td>3.9e-10*</td>
      <td>LMM</td>
    </tr>
    <tr>
      <td>HGDP sim.</td>
      <td>AUCPR</td>
      <td>FES</td>
      <td></td>
      <td>0</td>
      <td>1</td>
      <td>17</td>
      <td></td>
      <td>1.7e-05*</td>
      <td>LMM</td>
    </tr>
    <tr>
      <td>1000 Genomes sim.</td>
      <td>AUCPR</td>
      <td>FES</td>
      <td></td>
      <td>0</td>
      <td>1</td>
      <td>10</td>
      <td></td>
      <td>5e-10*</td>
      <td>LMM</td>
    </tr>
    <tr>
      <td>Admix. Large sim.</td>
      <td>AUCPR</td>
      <td>RC</td>
      <td></td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
      <td></td>
      <td>1.4e-05*</td>
      <td>LMM</td>
    </tr>
    <tr>
      <td>Admix. Small sim.</td>
      <td>AUCPR</td>
      <td>RC</td>
      <td></td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td></td>
      <td>0.095</td>
      <td>Tie</td>
    </tr>
    <tr>
      <td>Admix. Family sim.</td>
      <td>AUCPR</td>
      <td>RC</td>
      <td></td>
      <td>0</td>
      <td>1</td>
      <td>34</td>
      <td></td>
      <td>3.9e-10*</td>
      <td>LMM</td>
    </tr>
    <tr>
      <td>Human Origins</td>
      <td>AUCPR</td>
      <td>RC</td>
      <td></td>
      <td>3</td>
      <td>0.4</td>
      <td>36</td>
      <td></td>
      <td>9.6e-10*</td>
      <td>LMM</td>
    </tr>
    <tr>
      <td>HGDP</td>
      <td>AUCPR</td>
      <td>RC</td>
      <td></td>
      <td>4</td>
      <td>0.21</td>
      <td>16</td>
      <td></td>
      <td>0.013</td>
      <td>Tie</td>
    </tr>
    <tr>
      <td>1000 Genomes</td>
      <td>AUCPR</td>
      <td>RC</td>
      <td></td>
      <td>5</td>
      <td>0.004</td>
      <td>9</td>
      <td></td>
      <td>0.00043</td>
      <td>Tie</td>
    </tr>
    <tr>
      <td>Human Origins sim.</td>
      <td>AUCPR</td>
      <td>RC</td>
      <td></td>
      <td>0</td>
      <td>1</td>
      <td>37</td>
      <td></td>
      <td>4.1e-10*</td>
      <td>LMM</td>
    </tr>
    <tr>
      <td>HGDP sim.</td>
      <td>AUCPR</td>
      <td>RC</td>
      <td></td>
      <td>3</td>
      <td>0.087</td>
      <td>17</td>
      <td></td>
      <td>0.0014</td>
      <td>Tie</td>
    </tr>
    <tr>
      <td>1000 Genomes sim.</td>
      <td>AUCPR</td>
      <td>RC</td>
      <td></td>
      <td>3</td>
      <td>0.37</td>
      <td>10</td>
      <td></td>
      <td>8.5e-10*</td>
      <td>LMM</td>
    </tr>
  </tbody>
</table>

_*FES: Fixed Effect Sizes, RC: Random Coefficients.†Calibrated: whether mean |SRMSDp|<0.01 over 50 replicates.‡Value of r (number of PCs) with minimum mean |SRMSDp| or maximum mean AUCPR.§Wilcoxon paired 1-tailed test of distributions (|SRMSDp| or AUCPR) between models in header. Asterisk marks significant value using Bonferroni threshold (p<α/ntests with α=0.01 and ntests=72 is the number of tests in this table).¶Tie if no significant difference using Bonferroni threshold._

### Evaluations in admixture simulations

Now we look more closely at results per dataset. The complete $SRMSD_{p}$ and $AUC_{PR}$ distributions for the admixture simulations and FES traits are in Figure 3. RC traits gave qualitatively similar results (Figure 3—figure supplement 1).

![Figure 3.](https://cdn.elifesciences.org/articles/79238/elife-79238-fig3-v2.jpg)

**Figure 3.:** PCA and LMM models have varying number of PCs ($r\in{0,…,90}$ on x-axis), with the distributions (y-axis) of $SRMSD_{p}$ (top subpanel) and $AUC_{PR}$ (bottom subpanel) for 50 replicates. Best performance is zero $SRMSD_{p}$ and large $AUC_{PR}$. Zero and maximum median $AUC_{PR}$ values are marked with horizontal gray dashed lines, and $|SRMSD_{p}|<0.01$ is marked with a light gray area. LMM performs best with $r=0$, PCA with various $r$. (A) Large simulation ($n=1,000$ individuals). (B) Small simulation ($n=100$) shows overfitting for large $r$. (C) Family simulation ($n=1,000$) has admixed founders and large numbers of close relatives from a realistic random 20-generation pedigree. PCA performs poorly compared to LMM: $SRMSD_{p}>0$ for all $r$ and large $AUC_{PR}$ gap.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/79238/elife-79238-fig3-figsupp1-v2.jpg)

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/79238/elife-79238-fig3-figsupp2-v2.jpg)

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/79238/elife-79238-fig3-figsupp3-v2.jpg)

![Figure 3—figure supplement 4.](https://cdn.elifesciences.org/articles/79238/elife-79238-fig3-figsupp4-v2.jpg)

**Figure 3—figure supplement 4.:** ‘LMM lab.’ was only tested with $r=0$.

![Figure 3—figure supplement 5.](https://cdn.elifesciences.org/articles/79238/elife-79238-fig3-figsupp5-v2.jpg)

**Figure 3—figure supplement 5.:** ‘LMM lab.’ was only tested with $r=0$.

In the large admixture simulation, the $SRMSD_{p}$ of PCA is largest when $r=0$ (no PCs) and decreases rapidly to near zero at $r=3$, where it stays for up to $r=90$ (Figure 3A). Thus, PCA has calibrated p-values for $r\geq3$, smaller than the theoretical optimum for this simulation of $r=K-1=9$. In contrast, the $SRMSD_{p}$ for LMM starts near zero for $r=0$, but becomes negative as $r$ increases (p-values are conservative). The $AUC_{PR}$ distribution of PCA is similarly worst at $r=0$, increases rapidly and peaks at $r=3$, then decreases slowly for $r>3$, while the $AUC_{PR}$ distribution for LMM starts near its maximum at $r=0$ and decreases with $r$. Although the $AUC_{PR}$ distributions for LMM and PCA overlap considerably at each $r$, LMM with $r=0$ has significantly greater $AUC_{PR}$ values than PCA with $r=3$ (Table 3). However, qualitatively PCA performs nearly as well as LMM in this simulation.

The observed robustness to large $r$ led us to consider smaller sample sizes. A model with large numbers of parameters $r$ should overfit more as $r$ approaches the sample size $n$. Rather than increase $r$ beyond 90, we reduce individuals to $n=100$, which is small for typical association studies but may occur in studies of rare diseases, pilot studies, or other constraints. To compensate for the loss of power due to reducing $n$, we also reduce the number of causal loci (see Trait Simulation), which increases per-locus effect sizes. We found a large decrease in performance for both models as $r$ increases, and best performance for $r=1$ for PCA and $r=0$ for LMM (Figure 3B). Remarkably, LMM attains much larger negative $SRMSD_{p}$ values than in our other evaluations. LMM with $r=0$ is significantly better than PCA ($r=1$ to 4) in both measures (Table 3), but qualitatively the difference is negligible.

The family simulation adds a 20-generation random family to our large admixture simulation. Only the last generation is studied for association, which contains numerous siblings, first cousins, etc., with the initial admixture structure preserved by geographically biased mating. Our evaluation reveals a sizable gap in both measures between LMM and PCA across all $r$ (Figure 3C). LMM again performs best with $r=0$ and achieves mean $|SRMSD_{p}|<0.01$. However, PCA does not achieve mean $|SRMSD_{p}|<0.01$ at any $r$, and its best mean $AUC_{PR}$ is considerably worse than that of LMM. Thus, LMM is conclusively superior to PCA, and the only calibrated model, when there is family structure.

### Evaluations in real human genotype datasets

Next, we repeat our evaluations with real human genotype data, which differs from our simulations in allele frequency distributions and more complex population structures with greater $F_{ST}$, numerous correlated subpopulations, and potential cryptic family relatedness.

Human Origins has the greatest number and diversity of subpopulations. The $SRMSD_{p}$ and $AUC_{PR}$ distributions in this dataset and FES traits (Figure 4A) most resemble those from the family simulation (Figure 3C). In particular, while LMM with $r=0$ performed optimally (both measures) and satisfies mean $|SRMSD_{p}|<0.01$, PCA maintained $SRMSD_{p}>0.01$ for all $r$ and its $AUC_{PR}$ were all considerably smaller than the best $AUC_{PR}$ of LMM.

![Figure 4.](https://cdn.elifesciences.org/articles/79238/elife-79238-fig4-v2.jpg)

**Figure 4.:** Same setup as Figure 3, see that for details. These datasets strongly favor LMM with no PCs over PCA, with distributions that most resemble the family simulation. (A) Human Origins. (B) Human Genome Diversity Panel (HGDP). (C) 1000 Genomes Project.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/79238/elife-79238-fig4-figsupp1-v2.jpg)

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/79238/elife-79238-fig4-figsupp2-v2.jpg)

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/79238/elife-79238-fig4-figsupp3-v2.jpg)

![Figure 4—figure supplement 4.](https://cdn.elifesciences.org/articles/79238/elife-79238-fig4-figsupp4-v2.jpg)

**Figure 4—figure supplement 4.:** ‘LMM lab.’ was only tested with $r=0$.

![Figure 4—figure supplement 5.](https://cdn.elifesciences.org/articles/79238/elife-79238-fig4-figsupp5-v2.jpg)

**Figure 4—figure supplement 5.:** ‘LMM lab.’ was only tested with $r=0$.

HGDP has the fewest individuals among real datasets, but compared to Human Origins contains more loci and low-frequency variants. Performance (Figure 4B) again most resembled the family simulations. In particular, LMM with $r=0$ achieves mean $|SRMSD_{p}|<0.01$ (p-values are calibrated), while PCA does not, and there is a sizable $AUC_{PR}$ gap between LMM and PCA. Maximum $AUC_{PR}$ values were lowest in HGDP compared to the two other real datasets.

1000 Genomes has the fewest subpopulations but largest number of individuals per subpopulation. Thus, although this dataset has the simplest subpopulation structure among the real datasets, we find $SRMSD_{p}$ and $AUC_{PR}$ distributions (Figure 4C) that again most resemble our earlier family simulation, with mean $|SRMSD_{p}|<0.01$ for LMM only and large $AUC_{PR}$ gaps between LMM and PCA.

Our results are qualitatively different for RC traits, which had smaller $AUC_{PR}$ gaps between LMM and PCA (Figure 4—figure supplement 1). Maximum $AUC_{PR}$ were smaller in RC compared to FES in Human Origins and 1000 Genomes, suggesting lower power for RC traits across association models. Nevertheless, LMM with $r=0$ was significantly better than PCA for all measures in the real datasets and RC traits (Table 3).

### Evaluations in subpopulation tree simulations fit to human data

To better understand which features of the real datasets lead to the large differences in performance between LMM and PCA, we carried out subpopulation tree simulations. Human subpopulations are related roughly by trees, which induce the strongest correlations, so we fit trees to each real dataset and tested if data simulated from these complex tree structures could recapitulate our previous results (Figure 1). These tree simulations also feature non-uniform ancestral allele frequency distributions, which recapitulated some of the skew for smaller minor allele frequencies of the real datasets (Figure 1C). The $SRMSD_{p}$ and $AUC_{PR}$ distributions for these tree simulations (Figure 5) resembled our admixture simulation more than either the family simulation (Figure 3) or real data results (Figure 4). Both LMM with $r=0$ and PCA (various $r$) achieve mean $|SRMSD_{p}|<0.01$ (Table 3). The $AUC_{PR}$ distributions of both LMM and PCA track closely as $r$ is varied, although there is a small gap resulting in LMM ($r=0$) besting PCA in all three simulations. The results are qualitatively similar for RC traits (Figure 5—figure supplement 1, Table 3). Overall, these subpopulation tree simulations do not recapitulate the large LMM advantage over PCA observed on the real data.

![Figure 5.](https://cdn.elifesciences.org/articles/79238/elife-79238-fig5-v2.jpg)

**Figure 5.:** Same setup as Figure 3, see that for details. These tree simulations, which exclude family structure by design, do not explain the large gaps in LMM-PCA performance observed in the real data. (A) Human Origins tree simulation. (B) Human Genome Diversity Panel (HGDP) tree simulation. (C) 1000 Genomes Project tree simulation.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/79238/elife-79238-fig5-figsupp1-v2.jpg)

### Numerous distant relatives explain poor PCA performance in real data

In principle, PCA performance should be determined by the dimension of relatedness, or kinship matrix rank, since PCA is a low-dimensional model whereas LMM can model high-dimensional relatedness without overfitting. We used the Tracy-Widom test (Patterson et al., 2006) with $p<0.01$ to estimate kinship matrix rank as the number of significant PCs (Figure 6—figure supplement 1A). The true rank of our simulations is slightly underestimated (Table 2), but we confirm that the family simulation has the greatest rank, and real datasets have greater estimates than their respective subpopulation tree simulations, which confirms our hypothesis to some extent. However, estimated ranks do not separate real datasets from tree simulations, as required to predict the observed PCA performance. Moreover, the HGDP and 1000 Genomes rank estimates are 45 and 61, respectively, yet PCA performed poorly for all $r\leq90$ numbers of PCs (Figure 4). The top eigenvalue explained a proportion of variance proportional to $F_{ST}$ (Table 2), but the rest of the top 10 eigenvalues show no clear differences between datasets, except the small simulation had larger variances explained per eigenvalue (expected since it has fewer eigenvalues; Figure 6—figure supplement 1). Comparing cumulative variance explained versus rank fraction across all eigenvalues, all datasets increase from their starting point almost linearly until they reach 1, except the family simulation has much greater variance explained by mid-rank eigenvalues (Figure 6—figure supplement 1). We also calculated the number of PCs that are significantly associated with the trait, and observed similar results, namely that while the family simulation has more significant PCs than the non-family admixture simulations, the real datasets and their tree simulated counterparts have similar numbers of significant PCs (Figure 6—figure supplement 2). Overall, there is no separation between real datasets (where PCA performed poorly) and subpopulation tree simulations (where PCA performed relatively well) in terms of their eigenvalues or kinship matrix rank estimates.

Local kinship, which is recent relatedness due to family structure excluding population structure, is the presumed cause of the LMM to PCA performance gap observed in real datasets but not their subpopulation tree simulation counterparts. Instead of inferring local kinship through increased kinship matrix rank, as attempted in the last paragraph, now we measure it directly using the KING-robust estimator (Manichaikul et al., 2010). We observe more large local kinship in the real datasets and the family simulation compared to the other simulations (Figure 6). However, for real data this distribution depends on the subpopulation structure, since locally related pairs are most likely in the same subpopulation. Therefore, the only comparable curve to each real dataset is their corresponding subpopulation tree simulation, which matches subpopulation structure. In all real datasets, we identified highly related individual pairs with kinship above the 4th degree relative threshold of 0.022 (Manichaikul et al., 2010; Conomos et al., 2016b). However, these highly related pairs are vastly outnumbered by more distant pairs with evident non-zero local kinship as compared to the extreme tree simulation values.

![Figure 6.](https://cdn.elifesciences.org/articles/79238/elife-79238-fig6-v2.jpg)

**Figure 6.:** Curves are complementary cumulative distribution of lower triangular kinship matrix (self kinship excluded) from KING-robust estimator. Note log x-axis; negative estimates are counted but not shown. Most values are below 4th degree relative threshold. Each real dataset has a greater cumulative than its subpopulation tree simulations.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/79238/elife-79238-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** (A) Kinship matrix rank estimated with the Tracy-Widom test with $p<0.01$. (B) Cumulative variance explained versus eigenvalue rank fraction. (C) Variance explained by first 10 eigenvalues.

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/79238/elife-79238-fig6-figsupp2-v2.jpg)

**Figure 6—figure supplement 2.:** PCs are tested using an ordinary linear regression sequentially, with the th PC tested conditionally on the previous $k−1$ PCs and the intercept. Q-values are estimated from the 90 p-values (one for each PC in a given dataset and replicate) using the R package qvalue assuming $\pi_{0}=1$ (necessary since the default $\pi_{0}$ estimates were unreliable for such small numbers of p-values and occasionally produced errors), and an FDR threshold of 0.05 is used to determine the number of significant PCs. Distribution per dataset is over its 50 replicates. Shown are results for FES traits with $h^{2}=0.8$ (the results for RC were very similar, not shown).

To try to improve PCA performance, we followed the standard practice of removing 4th degree relatives, which reduced sample sizes between 5% and 10% (Table 4). Only $r=0$ for LMM and $r=20$ for PCA were tested, as these performed well in our earlier evaluation, and only FES traits were tested because they previously displayed the large PCA-LMM performance gap. LMM significantly outperforms PCA in all these cases (Wilcoxon paired 1-tailed $p<0.01$; Figure 7). Notably, PCA still had miscalibrated p-values two of the three real datasets ($|SRMSD_{p}|>0.01$), the only marginally calibrated case being HGDP which is also the smallest of these datasets. Otherwise, $AUC_{PR}$ and $SRMSD_{p}$ ranges were similar here as in our earlier evaluation. Therefore, the removal of the small number of highly related individual pairs had a negligible effect in PCA performance, so the larger number of more distantly related pairs explain the poor PCA performance in the real datasets.

![Figure 7.](https://cdn.elifesciences.org/articles/79238/elife-79238-fig7-v2.jpg)

**Figure 7.:** Each dataset is a column, rows are measures. Boxplot whiskers are extrema over 50 replicates. First row has $|SRMSD_{p}|<0.01$ band marked as gray area.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/79238/elife-79238-fig7-figsupp1-v2.jpg)

**Table 4.**
 Dataset sizes after 4th degree relative filter.


<table>
  <thead>
    <tr>
      <th>Dataset</th>
      <th>Loci (m)</th>
      <th>Ind. (n)</th>
      <th>Ind. removed (%)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Human Origins</td>
      <td>189 722</td>
      <td>2636</td>
      <td>9.8</td>
    </tr>
    <tr>
      <td>HGDP</td>
      <td>758 009</td>
      <td>847</td>
      <td>8.8</td>
    </tr>
    <tr>
      <td>1000 Genomes</td>
      <td>1 097 415</td>
      <td>2390</td>
      <td>4.6</td>
    </tr>
  </tbody>
</table>

### Low heritability and environment simulations

Our main evaluations were repeated with traits simulated under a lower heritability value of $h^{2}=0.3$. We reduced the number of causal loci in response to this change in heritability, to result in equal average effect size per locus compared to the previous high heritability evaluations (see Trait Simulation). Despite that, these low heritability evaluations measured lower $AUC_{PR}$ values than their high heritability counterparts (Figure 3—figure supplement 2, Figure 3—figure supplement 3, Figure 4—figure supplement 2, Figure 4—figure supplement 3, Figure 7—figure supplement 1). The gap between LMM and PCA was reduced in these evaluations, but the main conclusion of the high heritability evaluation holds for low heritability as well, namely that LMM with $r=0$ significantly outperforms or ties LMM with $r>0$ and PCA in all cases (Table 5).

**Table 5.**
 Overview of PCA and LMM evaluations for low heritability simulations.


<table>
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th colspan="3">LMM r=0 vs best r</th>
      <th colspan="4">PCA vs LMM r=0</th>
    </tr>
    <tr>
      <th>Dataset</th>
      <th>Metric</th>
      <th>Trait*</th>
      <th>Cal.†</th>
      <th>Best r‡</th>
      <th>p-value §</th>
      <th>Best r‡</th>
      <th>Cal.†</th>
      <th>p-value §</th>
      <th>Best model ¶</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Admix. Large sim.</td>
      <td>|SRMSDp|</td>
      <td>FES</td>
      <td>True</td>
      <td>0</td>
      <td>1</td>
      <td>62</td>
      <td>True</td>
      <td>0.00012*</td>
      <td>LMM</td>
    </tr>
    <tr>
      <td>Admix. Small sim.</td>
      <td>|SRMSDp|</td>
      <td>FES</td>
      <td>True</td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
      <td>True</td>
      <td>0.27</td>
      <td>Tie</td>
    </tr>
    <tr>
      <td>Admix. Family sim.</td>
      <td>|SRMSDp|</td>
      <td>FES</td>
      <td>True</td>
      <td>0</td>
      <td>1</td>
      <td>90</td>
      <td>False</td>
      <td>3.9e-10*</td>
      <td>LMM</td>
    </tr>
    <tr>
      <td>Human Origins</td>
      <td>|SRMSDp|</td>
      <td>FES</td>
      <td>True</td>
      <td>0</td>
      <td>1</td>
      <td>81</td>
      <td>True</td>
      <td>3.9e-10*</td>
      <td>LMM</td>
    </tr>
    <tr>
      <td>HGDP</td>
      <td>|SRMSDp|</td>
      <td>FES</td>
      <td>True</td>
      <td>0</td>
      <td>1</td>
      <td>37</td>
      <td>True</td>
      <td>6.2e-09*</td>
      <td>LMM</td>
    </tr>
    <tr>
      <td>1000 Genomes</td>
      <td>|SRMSDp|</td>
      <td>FES</td>
      <td>True</td>
      <td>0</td>
      <td>1</td>
      <td>84</td>
      <td>True</td>
      <td>3.9e-10*</td>
      <td>LMM</td>
    </tr>
    <tr>
      <td>Admix. Large sim.</td>
      <td>|SRMSDp|</td>
      <td>RC</td>
      <td>True</td>
      <td>0</td>
      <td>1</td>
      <td>35</td>
      <td>True</td>
      <td>0.00094</td>
      <td>Tie</td>
    </tr>
    <tr>
      <td>Admix. Small sim.</td>
      <td>|SRMSDp|</td>
      <td>RC</td>
      <td>True</td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
      <td>True</td>
      <td>0.087</td>
      <td>Tie</td>
    </tr>
    <tr>
      <td>Admix. Family sim.</td>
      <td>|SRMSDp|</td>
      <td>RC</td>
      <td>True</td>
      <td>0</td>
      <td>1</td>
      <td>90</td>
      <td>False</td>
      <td>4.1e-10*</td>
      <td>LMM</td>
    </tr>
    <tr>
      <td>Human Origins</td>
      <td>|SRMSDp|</td>
      <td>RC</td>
      <td>True</td>
      <td>0</td>
      <td>1</td>
      <td>75</td>
      <td>True</td>
      <td>0.00016*</td>
      <td>LMM</td>
    </tr>
    <tr>
      <td>HGDP</td>
      <td>|SRMSDp|</td>
      <td>RC</td>
      <td>True</td>
      <td>0</td>
      <td>1</td>
      <td>23</td>
      <td>True</td>
      <td>1.7e-05*</td>
      <td>LMM</td>
    </tr>
    <tr>
      <td>1000 Genomes</td>
      <td>|SRMSDp|</td>
      <td>RC</td>
      <td>True</td>
      <td>0</td>
      <td>1</td>
      <td>41</td>
      <td>True</td>
      <td>6.7e-10*</td>
      <td>LMM</td>
    </tr>
    <tr>
      <td>Admix. Large sim.</td>
      <td>AUCPR</td>
      <td>FES</td>
      <td></td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
      <td></td>
      <td>0.11</td>
      <td>Tie</td>
    </tr>
    <tr>
      <td>Admix. Small sim.</td>
      <td>AUCPR</td>
      <td>FES</td>
      <td></td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td></td>
      <td>0.58</td>
      <td>Tie</td>
    </tr>
    <tr>
      <td>Admix. Family sim.</td>
      <td>AUCPR</td>
      <td>FES</td>
      <td></td>
      <td>0</td>
      <td>1</td>
      <td>7</td>
      <td></td>
      <td>2.2e-06*</td>
      <td>LMM</td>
    </tr>
    <tr>
      <td>Human Origins</td>
      <td>AUCPR</td>
      <td>FES</td>
      <td></td>
      <td>0</td>
      <td>1</td>
      <td>16</td>
      <td></td>
      <td>8e-10*</td>
      <td>LMM</td>
    </tr>
    <tr>
      <td>HGDP</td>
      <td>AUCPR</td>
      <td>FES</td>
      <td></td>
      <td>11</td>
      <td>0.68</td>
      <td>6</td>
      <td></td>
      <td>0.0043</td>
      <td>Tie</td>
    </tr>
    <tr>
      <td>1000 Genomes</td>
      <td>AUCPR</td>
      <td>FES</td>
      <td></td>
      <td>6</td>
      <td>0.34</td>
      <td>4</td>
      <td></td>
      <td>2.3e-07*</td>
      <td>LMM</td>
    </tr>
    <tr>
      <td>Admix. Large sim.</td>
      <td>AUCPR</td>
      <td>RC</td>
      <td></td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
      <td></td>
      <td>0.14</td>
      <td>Tie</td>
    </tr>
    <tr>
      <td>Admix. Small sim.</td>
      <td>AUCPR</td>
      <td>RC</td>
      <td></td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td></td>
      <td>0.1</td>
      <td>Tie</td>
    </tr>
    <tr>
      <td>Admix. Family sim.</td>
      <td>AUCPR</td>
      <td>RC</td>
      <td></td>
      <td>0</td>
      <td>1</td>
      <td>5</td>
      <td></td>
      <td>1.9e-06*</td>
      <td>LMM</td>
    </tr>
    <tr>
      <td>Human Origins</td>
      <td>AUCPR</td>
      <td>RC</td>
      <td></td>
      <td>4</td>
      <td>0.16</td>
      <td>12</td>
      <td></td>
      <td>0.003</td>
      <td>Tie</td>
    </tr>
    <tr>
      <td>HGDP</td>
      <td>AUCPR</td>
      <td>RC</td>
      <td></td>
      <td>2</td>
      <td>0.14</td>
      <td>5</td>
      <td></td>
      <td>0.14</td>
      <td>Tie</td>
    </tr>
    <tr>
      <td>1000 Genomes</td>
      <td>AUCPR</td>
      <td>RC</td>
      <td></td>
      <td>0</td>
      <td>1</td>
      <td>4</td>
      <td></td>
      <td>0.078</td>
      <td>Tie</td>
    </tr>
  </tbody>
</table>

_*FES: Fixed Effect Sizes, RC: Random Coefficients.†Calibrated: whether mean |SRMSDp|<0.01 over 50 replicates.‡Value of r (number of PCs) with minimum mean |SRMSDp| or maximum mean AUCPR.§Wilcoxon paired 1-tailed test of distributions (|SRMSDp| or AUCPR) between models in header. Asterisk marks significant value using Bonferroni threshold (p<α/ntests with α=0.01 and ntests=48 is the number of tests in this table).¶Tie if no significant difference using Bonferroni threshold._

Lastly, we simulated traits with both low heritability and large environment effects determined by geography and subpopulation labels, so they are strongly correlated to the low-dimensional population structure. For that reason, PCs may be expected to perform better in this setting (in either PCA or LMM). However, we find that both PCA and LMM (even without PCs) increase their $AUC_{PR}$ values compared to the low-heritability evaluations (Figure 8—figure supplement 1; Figure 8 also shows representative numbers of PCs, which performed optimally or nearly so in individual simulations shown in Figure 3—figure supplement 4, Figure 3—figure supplement 5, Figure 4—figure supplement 4, Figure 4—figure supplement 5). p-Value calibration is comparable with or without environment effects, for LMM for all $r$ and for PCA once $r$ is large enough (Figure 8—figure supplement 1). These simulations are the only where we occasionally observed for both metrics a significant, though small, advantage of LMM with PCs versus LMM without PCs (Table 6). Additionally, on RC traits only, PCA significantly outperforms LMM in the three real human datasets (Table 6), the only cases in all of our evaluations where this is observed. For comparison, we also evaluate an ‘oracle’ LMM without PCs but with the finest group labels, the same used to simulate environment, as fixed categorical covariates (‘LMM lab.’), and see much larger $AUC_{PR}$ values than either LMM with PCs or PCA (Figure 8, Figure 3—figure supplement 4, Figure 3—figure supplement 5, Figure 4—figure supplement 4, Figure 4—figure supplement 5, Table 6). However, LMM with labels is often more poorly calibrated than LMM or PCA without labels, which may be since these numerous labels are inappropriately modeled as fixed rather than random effects. Overall, we find that association studies with correlated environment and genetic effects remain a challenge for PCA and LMM, that addition of PCs to an LMM improves performance only marginally, and that if the environment effect is driven by geography or ethnicity then use of those labels greatly improves performance compared to using PCs.

![Figure 8.](https://cdn.elifesciences.org/articles/79238/elife-79238-fig8-v2.jpg)

**Figure 8.:** Traits simulated with environment effects, otherwise the same as Figure 7. ‘LMM lab.’ includes as fixed effects true groups from which environment was simulated.

![Figure 8—figure supplement 1.](https://cdn.elifesciences.org/articles/79238/elife-79238-fig8-figsupp1-v2.jpg)

**Figure 8—figure supplement 1.:** Each curve traces as the number of PCs $r$ is increased from $r=0$ (marked with an “x”) until $r=90$ (unmarked end), on one axis is the mean value over replicates of either $SRMSD_{p}$ or $AUC_{PR}$, for low heritability simulations on the x-axis and environment simulations on the y-axis. Each curve corresponds to one dataset (color) and association model (solid or dashed line type). Columns: (A) FES and (B) RC traits show similar results. First row shows that for PCA curves (dashed), $SRMSD_{p}$ is higher (worse) in environment simulations for low $r$, but becomes equal in both simulations once $r$ is sufficiently large; for LMM curves (solid), $SRMSD_{p}$ is equal in both simulations for all $r$, all datasets. Second row shows that for PCA, $AUC_{PR}$ is higher (better) in low heritability simulations for low $r$, but becomes higher in environment simulations once $r$ is sufficiently large; for LMM, performance is better in environment simulations for all $r$, all datasets.

**Table 6.**
 Overview of PCA and LMM evaluations for environment simulations.


<table>
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th colspan="3">LMM r=0 vs best r</th>
      <th colspan="4">PCA vs LMM r=0</th>
      <th colspan="3">LMM lab. r=0 vs PCA/LMM</th>
    </tr>
    <tr>
      <th>Dataset</th>
      <th>Metric</th>
      <th>Trait*</th>
      <th>Cal.†</th>
      <th>r‡</th>
      <th>p-value §</th>
      <th>r‡</th>
      <th>Cal.†</th>
      <th>p-value §</th>
      <th>Best ¶</th>
      <th>Cal.†</th>
      <th>p-value §</th>
      <th>Best ¶</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Admix. Large sim.</td>
      <td>|SRMSDp|</td>
      <td>FES</td>
      <td>True</td>
      <td>0</td>
      <td>1</td>
      <td>83</td>
      <td>True</td>
      <td>0.38</td>
      <td>Tie</td>
      <td>True</td>
      <td>1.8e-14*</td>
      <td>PCA/LMM</td>
    </tr>
    <tr>
      <td>Admix. Small sim.</td>
      <td>|SRMSDp|</td>
      <td>FES</td>
      <td>True</td>
      <td>0</td>
      <td>1</td>
      <td>90</td>
      <td>True</td>
      <td>0.001</td>
      <td>Tie</td>
      <td>False</td>
      <td>1.4e-14*</td>
      <td>PCA/LMM</td>
    </tr>
    <tr>
      <td>Admix. Family sim.</td>
      <td>|SRMSDp|</td>
      <td>FES</td>
      <td>True</td>
      <td>4</td>
      <td>0.18</td>
      <td>90</td>
      <td>False</td>
      <td>3.9e-10*</td>
      <td>LMM</td>
      <td>True</td>
      <td>0.066</td>
      <td>LMM/LMM lab.</td>
    </tr>
    <tr>
      <td>Human Origins</td>
      <td>|SRMSDp|</td>
      <td>FES</td>
      <td>True</td>
      <td>9</td>
      <td>3.9e-05*</td>
      <td>90</td>
      <td>False</td>
      <td>1.4e-08*</td>
      <td>LMM</td>
      <td>False</td>
      <td>3.9e-10*</td>
      <td>LMM</td>
    </tr>
    <tr>
      <td>HGDP</td>
      <td>|SRMSDp|</td>
      <td>FES</td>
      <td>True</td>
      <td>0</td>
      <td>1</td>
      <td>90</td>
      <td>True</td>
      <td>0.0037</td>
      <td>Tie</td>
      <td>False</td>
      <td>2.1e-09*</td>
      <td>PCA/LMM</td>
    </tr>
    <tr>
      <td>1000 Genomes</td>
      <td>|SRMSDp|</td>
      <td>FES</td>
      <td>False</td>
      <td>8</td>
      <td>8.8e-08*</td>
      <td>85</td>
      <td>True</td>
      <td>0.053</td>
      <td>Tie</td>
      <td>True</td>
      <td>3.9e-10*</td>
      <td>LMM lab.</td>
    </tr>
    <tr>
      <td>Admix. Large sim.</td>
      <td>|SRMSDp|</td>
      <td>RC</td>
      <td>True</td>
      <td>0</td>
      <td>1</td>
      <td>60</td>
      <td>True</td>
      <td>0.033</td>
      <td>Tie</td>
      <td>True</td>
      <td>6.3e-10*</td>
      <td>PCA/LMM</td>
    </tr>
    <tr>
      <td>Admix. Small sim.</td>
      <td>|SRMSDp|</td>
      <td>RC</td>
      <td>True</td>
      <td>0</td>
      <td>1</td>
      <td>9</td>
      <td>True</td>
      <td>0.85</td>
      <td>Tie</td>
      <td>False</td>
      <td>1.4e-14*</td>
      <td>PCA/LMM</td>
    </tr>
    <tr>
      <td>Admix. Family sim.</td>
      <td>|SRMSDp|</td>
      <td>RC</td>
      <td>True</td>
      <td>5</td>
      <td>0.14</td>
      <td>90</td>
      <td>False</td>
      <td>3.9e-10*</td>
      <td>LMM</td>
      <td>True</td>
      <td>0.011</td>
      <td>LMM/LMM lab.</td>
    </tr>
    <tr>
      <td>Human Origins</td>
      <td>|SRMSDp|</td>
      <td>RC</td>
      <td>False</td>
      <td>9</td>
      <td>1.1e-08*</td>
      <td>90</td>
      <td>True</td>
      <td>2.3e-07*</td>
      <td>PCA</td>
      <td>False</td>
      <td>3.9e-10*</td>
      <td>PCA</td>
    </tr>
    <tr>
      <td>HGDP</td>
      <td>|SRMSDp|</td>
      <td>RC</td>
      <td>True</td>
      <td>0</td>
      <td>1</td>
      <td>89</td>
      <td>True</td>
      <td>6.5e-09*</td>
      <td>PCA</td>
      <td>False</td>
      <td>3.9e-10*</td>
      <td>PCA</td>
    </tr>
    <tr>
      <td>1000 Genomes</td>
      <td>|SRMSDp|</td>
      <td>RC</td>
      <td>False</td>
      <td>8</td>
      <td>1.6e-08*</td>
      <td>88</td>
      <td>True</td>
      <td>4.9e-09*</td>
      <td>PCA</td>
      <td>True</td>
      <td>0.09</td>
      <td>PCA/LMM lab.</td>
    </tr>
    <tr>
      <td>Admix. Large sim.</td>
      <td>AUCPR</td>
      <td>FES</td>
      <td></td>
      <td>4</td>
      <td>2.4e-06*</td>
      <td>6</td>
      <td></td>
      <td>0.0021</td>
      <td>Tie</td>
      <td></td>
      <td>1.8e-15*</td>
      <td>LMM lab.</td>
    </tr>
    <tr>
      <td>Admix. Small sim.</td>
      <td>AUCPR</td>
      <td>FES</td>
      <td></td>
      <td>3</td>
      <td>0.055</td>
      <td>4</td>
      <td></td>
      <td>0.033</td>
      <td>Tie</td>
      <td></td>
      <td>0.28</td>
      <td>Tie</td>
    </tr>
    <tr>
      <td>Admix. Family sim.</td>
      <td>AUCPR</td>
      <td>FES</td>
      <td></td>
      <td>12</td>
      <td>7e-04</td>
      <td>63</td>
      <td></td>
      <td>3.9e-10*</td>
      <td>LMM</td>
      <td></td>
      <td>3.9e-10*</td>
      <td>LMM lab.</td>
    </tr>
    <tr>
      <td>Human Origins</td>
      <td>AUCPR</td>
      <td>FES</td>
      <td></td>
      <td>20</td>
      <td>3.7e-06*</td>
      <td>90</td>
      <td></td>
      <td>1.4e-05*</td>
      <td>LMM</td>
      <td></td>
      <td>3.9e-10*</td>
      <td>LMM lab.</td>
    </tr>
    <tr>
      <td>HGDP</td>
      <td>AUCPR</td>
      <td>FES</td>
      <td></td>
      <td>12</td>
      <td>4.3e-06*</td>
      <td>45</td>
      <td></td>
      <td>0.0044</td>
      <td>Tie</td>
      <td></td>
      <td>3.9e-10*</td>
      <td>LMM lab.</td>
    </tr>
    <tr>
      <td>1000 Genomes</td>
      <td>AUCPR</td>
      <td>FES</td>
      <td></td>
      <td>9</td>
      <td>1.9e-08*</td>
      <td>55</td>
      <td></td>
      <td>0.028</td>
      <td>Tie</td>
      <td></td>
      <td>3.9e-10*</td>
      <td>LMM lab.</td>
    </tr>
    <tr>
      <td>Admix. Large sim.</td>
      <td>AUCPR</td>
      <td>RC</td>
      <td></td>
      <td>4</td>
      <td>0.00085</td>
      <td>5</td>
      <td></td>
      <td>0.0018</td>
      <td>Tie</td>
      <td></td>
      <td>5e-10*</td>
      <td>LMM lab.</td>
    </tr>
    <tr>
      <td>Admix. Small sim.</td>
      <td>AUCPR</td>
      <td>RC</td>
      <td></td>
      <td>2</td>
      <td>0.13</td>
      <td>5</td>
      <td></td>
      <td>0.093</td>
      <td>Tie</td>
      <td></td>
      <td>0.0028</td>
      <td>Tie</td>
    </tr>
    <tr>
      <td>Admix. Family sim.</td>
      <td>AUCPR</td>
      <td>RC</td>
      <td></td>
      <td>9</td>
      <td>0.01</td>
      <td>86</td>
      <td></td>
      <td>1.7e-09*</td>
      <td>LMM</td>
      <td></td>
      <td>3.9e-10*</td>
      <td>LMM lab.</td>
    </tr>
    <tr>
      <td>Human Origins</td>
      <td>AUCPR</td>
      <td>RC</td>
      <td></td>
      <td>22</td>
      <td>0.0039</td>
      <td>90</td>
      <td></td>
      <td>1e-06*</td>
      <td>PCA</td>
      <td></td>
      <td>3.9e-10*</td>
      <td>LMM lab.</td>
    </tr>
    <tr>
      <td>HGDP</td>
      <td>AUCPR</td>
      <td>RC</td>
      <td></td>
      <td>19</td>
      <td>0.0057</td>
      <td>64</td>
      <td></td>
      <td>2.8e-05*</td>
      <td>PCA</td>
      <td></td>
      <td>3e-07*</td>
      <td>LMM lab.</td>
    </tr>
    <tr>
      <td>1000 Genomes</td>
      <td>AUCPR</td>
      <td>RC</td>
      <td></td>
      <td>9</td>
      <td>8.7e-05*</td>
      <td>87</td>
      <td></td>
      <td>1.2e-09*</td>
      <td>PCA</td>
      <td></td>
      <td>4.4e-10*</td>
      <td>LMM lab.</td>
    </tr>
  </tbody>
</table>

_*FES: Fixed Effect Sizes, RC: Random Coefficients.†Calibrated: whether mean |SRMSDp|<0.01 over 50 replicates.‡Value of r (number of PCs) with minimum mean |SRMSDp| or maximum mean AUCPR.§Wilcoxon paired 1-tailed test of distributions (|SRMSDp| or AUCPR) between models in header. Asterisk marks significant value using Bonferroni threshold (p<α/ntests with α=0.01 and ntests=72 is the number of tests in this table).¶Tie if no significant difference using Bonferroni threshold; in last column, pairwise ties are specified and “Tie” is three-way tie._

## Discussion

Our evaluations conclusively determined that LMM without PCs performs better than PCA (for any number of PCs) across all scenarios without environment effects, including all real and simulated genotypes and two trait simulation models. Although the addition of a few PCs to LMM does not greatly hurt its performance (except for small sample sizes), they generally did not improve it either (Table 3, Table 5), which agrees with previous observations (Liu et al., 2011; Janss et al., 2012) but contradicts others (Zhao et al., 2007; Price et al., 2010). Our findings make sense since PCs are the eigenvectors of the same kinship matrix that parameterized random effects, so including both is redundant.

The presence of environment effects that are correlated to relatedness presents the only scenario where occasionally PCA and LMM with PCs outperform LMM without PCs (Table 6). It is commonly believed that PCs model such environment effects well (Novembre et al., 2008; Zhang and Pan, 2015; Lin et al., 2021). However, we observe that LMM without PCs models environment effects nearly as well as with PCs (Figure 8), consistent with previous findings (Vilhjálmsson and Nordborg, 2013; Wang et al., 2022) and with environment inflating heritability estimates using LMM (Heckerman et al., 2016). Moreover, modeling the true environment groups as fixed categorical effects always substantially improved $AUC_{PR}$ compared to modeling them with PCs (Figure 8, Table 6). Modeling numerous environment groups as fixed effects does result in deflated p-values (Figure 8, Table 6), which we expect would be avoided by modeling them as random effects, a strategy we chose not to pursue here as it is both a circular evaluation (the true effects were drawn from that model) and out of scope. Overall, including PCs to model environment effects yields limited power gains if at all, even in an LMM, and is no replacement for more adequate modeling of environment whenever possible.

Previous studies found that PCA was better calibrated than LMM for unusually differentiated markers (Price et al., 2010; Wu et al., 2011; Yang et al., 2014), which as simulated were an artificial scenario not based on a population genetics model, and are otherwise believed to be unusual (Sul and Eskin, 2013; Price et al., 2013). Our evaluations on real human data, which contain such loci in relevant proportions if they exist, do not replicate that result. Family relatedness strongly favors LMM, an advantage that probably outweighs this potential PCA benefit in real data.

Relative to LMM, the behavior of PCA fell between two extremes. When PCA performed well, there was a small number of PCs with both calibrated p-values and $AUC_{PR}$ near that of LMM without PCs. Conversely, PCA performed poorly when no number of PCs had either calibrated p-values or acceptably large $AUC_{PR}$. There were no cases where high numbers of PCs optimized an acceptable $AUC_{PR}$, or cases with miscalibrated p-values but high $AUC_{PR}$. PCA performed well in the admixture simulations (without families, both trait models), real human genotypes with RC traits, and the subpopulation tree simulations (both trait models). Conversely, PCA performed poorly in the admixed family simulation (both trait models) and the real human genotypes with FES traits.

PCA assumes that genetic relatedness is restricted to a low-dimensional subspace, whereas LMM can handle high-dimensional relatedness. Thus, PCA performs well in the admixture simulation, which is explicitly low-dimensional (see Genotype simulation from the admixture model), and our subpopulation tree simulations, which are likely well approximated by a few dimensions despite the large number of subpopulations because there are few long branches. Conversely, PCA performs poorly under family structure because its kinship matrix is high-dimensional (Figure 6—figure supplement 1). However, estimating the latent space dimensions of real datasets is challenging because estimated eigenvalues have biased distributions (Hayashi et al., 2018). Kinship matrix rank estimated using the Tracy-Widom test (Patterson et al., 2006) did not fully predict the datasets that PCA performs well on. In contrast, estimated local kinship finds considerable cryptic family relatedness in all real human datasets and better explains why PCA performs poorly there. The trait model also influences the relative performance of PCA, so genotype-only parameters (eigenvalues or local kinship) alone cannot tell the full story. There are related tests for numbers of dimensions that consider the trait which we did not consider, including the Bayesian information criterion for the regression with PCs against the trait (Zhu and Yu, 2009). Additionally, PCA and LMM goodness of fit could be compared using the coefficient of determination generalized for LMMs (Sun et al., 2010).

PCA is at best underpowered relative to LMMs, and at worst miscalibrated regardless of the numbers of PCs included, in real human genotype tests. Among our simulations, such poor performance occurred only in the admixed family. Local kinship estimates reveal considerable family relatedness in the real datasets absent in the corresponding subpopulation tree simulations. Admixture is also absent in our tree simulations, but our simulations and theory show that admixture is well handled by PCA. Hundreds of close relative pairs have been identified in 1000 Genomes (Gazal et al., 2015; Al Khudhair et al., 2015; Fedorova et al., 2016; Schlauch et al., 2017), but their removal does not improve PCA performance sufficiently in our tests, so the larger number of more distantly related pairs are PCA’s most serious obstacle in practice. Distant relatives are expected to be numerous in any large human dataset (Henn et al., 2012; Shchur and Nielsen, 2018; Loh et al., 2018). Our FES trait tests show that family relatedness is more challenging when rarer variants have larger coefficients. Overall, the high relatedness dimensions induced by family relatedness is the key challenge for PCA association in modern datasets that is readily overcome by LMM.

Our tests also found PCA robust to large numbers of PCs, far beyond the optimal choice, agreeing with previous anecdotal observations (Price et al., 2006; Kang et al., 2010), in contrast to using too few PCs for which there is a large performance penalty. The exception was the small sample size simulation, where only small numbers of PCs performed well. In contrast, LMM is simpler since there is no need to choose the number of PCs. However, an LMM with a large number of covariates may have conservative p-values, as observed for LMM with large numbers of PCs, which is a weakness of the score test used by the LMM we evaluated that may be overcome with other statistical tests. Simulations or post hoc evaluations remain crucial for ensuring that statistics are calibrated.

There are several variants of the PCA and LMM analyses, most designed for better modeling linkage disequilibrium (LD), that we did not evaluate directly, in which PCs are no longer exactly the top eigenvectors of the kinship matrix (if estimated with different approaches), although this is not a crucial aspect of our arguments. We do not consider the case where samples are projected onto PCs estimated from an external sample (Privé et al., 2020), which is uncommon in association studies, and whose primary effect is shrinkage, so if all samples are projected then they are all equally affected and larger regression coefficients compensate for the shrinkage, although this will no longer be the case if only a portion of the sample is projected onto the PCs of the rest of the sample. Another approach tests PCs for association against every locus in the genome in order to identify and exclude PCs that capture LD structure (which is localized) instead of ancestry (which should be present across the genome; Privé et al., 2020); a previous proposal removes LD using an autocorrelation model prior to estimating PCs (Patterson et al., 2006). These improved PCs remain inadequate models of family relatedness, so an LMM will continue to outperform them in that setting. Similarly, the leave-one-chromosome-out (LOCO) approach for estimating kinship matrices for LMMs prevents the test locus and loci in LD with it from being modeled by the random effect as well, which is called ‘proximal contamination’ (Lippert et al., 2011; Yang et al., 2014). While LOCO kinship estimates vary for each chromosome, they continue to model family relatedness, thus maintaining their key advantage over PCA. The LDAK model estimates kinship instead by weighing loci taking LD into account (Speed et al., 2012). LD effects must be adjusted for, if present, so in unfiltered data we advise the previous methods be applied. However, in this work, simulated genotypes do not have LD, and the real datasets were filtered to remove LD, so here there is no proximal contamination and LD confounding is minimized if present at all, so these evaluations may be considered the ideal situation where LD effects have been adjusted successfully, and in this setting LMM outperforms PCA. Overall, these alternative PCs or kinship matrices differ from their basic counterparts by either the extent to which LD influences the estimates (which may be a confounder in a small portion of the genome, by definition) or by sampling noise, neither of which are expected to change our key conclusion.

One of the limitations of this work include relatively small sample sizes compared to modern association studies. However, our conclusions are not expected to change with larger sample sizes, as cryptic family relatedness will continue to be abundant in such data, if not increase in abundance, and thus give LMMs an advantage over PCA (Henn et al., 2012; Shchur and Nielsen, 2018; Loh et al., 2018). One reason PCA has been favored over classic LMMs is because PCA’s runtime scales much better with increasing sample size. However, recent approaches not tested in this work have made LMMs more scalable and applicable to biobank-scale data (Loh et al., 2015; Zhou et al., 2018; Mbatchou et al., 2021), so one clear next step is carefully evaluating these approaches in simulations with larger sample sizes. A different benefit for including PCs were recently reported for BOLT-LMM, which does not result in greater power but rather in reduced runtime, a property that may be specific to its use of scalable algorithms such as conjugate gradient and variational Bayes (Loh et al., 2018). Many of these newer LMMs also no longer follow the infinitesimal model of the basic LMM (Loh et al., 2015; Mbatchou et al., 2021), and employ novel approximations, which are features not evaluated in this work and worthy of future study.

Another limitation of this work is ignoring rare variants, a necessity given our smaller sample sizes, where rare variant association is miscalibrated and underpowered. Using simulations mimicking the UK Biobank, recent work has found that rare variants can have a more pronounced structure than common variants, and that modeling this rare variant structure (with either PCA and LMM) may better model environment confounding, reduce inflation in association studies, and ameliorate stratification in polygenic risk scores (Zaidi and Mathieson, 2020). Better modeling rare variants and their structure is a key next step in association studies.

The largest limitation of our work is that we only considered quantitative traits. Previous evaluations involving case-control traits tended to report PCA-LMM ties or mixed results, an observation potentially confounded by the use of low-dimensional simulations without family relatedness (Table 1). An additional concern is case-control ascertainment bias and imbalance, which appears to affect LMMs more severely, although recent work appears to solve this problem (Yang et al., 2014; Zhou et al., 2018). Future evaluations should aim to include our simulations and real datasets, to ensure that previous results were not biased in favor of PCA by not simulating family structure or larger coefficients for rare variants that are expected for diseases by various selection models.

Overall, our results lead us to recommend LMM over PCA for association studies in general. Although PCA offer flexibility and speed compared to LMM, additional work is required to ensure that PCA is adequate, including removal of close relatives (lowering sample size and wasting resources) followed by simulations or other evaluations of statistics, and even then PCA may perform poorly in terms of both type I error control and power. The large numbers of distant relatives expected of any real dataset all but ensures that PCA will perform poorly compared to LMM (Henn et al., 2012; Shchur and Nielsen, 2018; Loh et al., 2018). Our findings also suggest that related applications such as polygenic models may enjoy gains in power and accuracy by employing an LMM instead of PCA to model relatedness (Rakitsch et al., 2013; Qian et al., 2020). PCA remains indispensable across population genetics, from visualizing population structure and performing quality control to its deep connection to admixture models, but the time has come to limit its use in association testing in favor of LMM or other, richer models capable of modeling all forms of relatedness.

## Materials and methods

### The complex trait model and PCA and LMM approximations

Let $x_{i⁢j}\in{0,1,2}$ be the genotype at the biallelic locus $i$ for individual $j$, which counts the number of reference alleles. Suppose there are $n$ individuals and $m$ loci, $X=(x_{i⁢j})$ is their $m\timesn$ genotype matrix, and $y$ is the length-$n$ column vector of individual trait values. The additive linear model for a quantitative (continuous) trait is:

$$
y=1⁢\alpha+X^{′}⁢\beta+Z^{′}⁢η+ϵ,
$$

where 1 is a length-$n$ vector of ones, $\alpha$ is the scalar intercept coefficient, $\beta$ is the length-$m$ vector of locus coefficients, $Z$ is a design matrix of environment effects and other covariates, $η$ is the vector of environment coefficients, $ϵ$ is a length-$n$ vector of residuals, and the superscript prime symbol ($′$) denotes matrix transposition. The residuals follow $ϵ_{j}∼Normal⁢(0,\sigma_{ϵ}^{2})$ independently per individual $j$, for some $\sigma_{ϵ}^{2}$.

The full model of Equation 1, which has a coefficient for each of the $m$ loci, is underdetermined in current datasets where $m≫n$. The PCA and LMM models, respectively, approximate the full model fit at a single locus $i$:

$$
PCA: y=1⁢\alpha+x_{i}⁢\beta_{i}+U_{r}⁢\gamma_{r}+Z^{′}⁢η+ϵ,
$$



$$
LMM:y=1\alpha+x_{i}\beta_{i}+s+Z^{′}η+ϵ,s∼Normal(0,2\sigma_{s}^{2}Φ^{T}),
$$

where $x_{i}$ is the length-$n$ vector of genotypes at locus $i$ only, $\beta_{i}$ is the locus coefficient, $U_{r}$ is an $n\timesr$ matrix of PCs, $\gamma_{r}$ is the length-$r$ vector of PC coefficients, $s$ is a length-$n$ vector of random effects, $Φ^{T}=(\phi_{j⁢k}^{T})$ is the $n\timesn$ kinship matrix conditioned on the ancestral population $T$, and $\sigma_{s}^{2}$ is a variance factor. Both models condition the regression of the focal locus $i$ on an approximation of the total polygenic effect $X^{′}⁢\beta$ with the same covariance structure, which is parameterized by the kinship matrix. Under the kinship model, genotypes are random variables obeying

$$
E⁡[x_{i}|T]=2⁢p_{i}^{T}⁢1,Cov⁡(x_{i}|T)=4⁢p_{i}^{T}⁢(1-p_{i}^{T})⁢Φ^{T},
$$

where $p_{i}^{T}$ is the ancestral allele frequency of locus $i$ (Malécot, 1948; Wright, 1949; Jacquard, 1970; Astle and Balding, 2009). Assuming independent loci, the covariance of the polygenic effect is

$$
Cov⁡(X^{′}\beta)=2\sigma_{s}^{2}Φ^{T},\sigma_{s}^{2}=\sumi=1m2p_{i}^{T}(1−p_{i}^{T})\beta_{i}^{2},
$$

which is readily modeled by the LMM random effect $s$, where the difference in mean is absorbed by the intercept. Alternatively, consider the eigendecomposition of the kinship matrix $Φ^{T}=U⁢Λ⁢U^{′}$ where $U$ is the $n\timesn$ eigenvector matrix and $Λ$ is the $n\timesn$ diagonal matrix of eigenvalues. The random effect can be written as

$$
s=U\gamma_{LMM},\gamma_{LMM}∼Normal(0,2\sigma_{s}^{2}Λ),
$$

which follows from the affine transformation property of multivariate normal distributions. Therefore, the PCA term $U_{r}⁢\gamma_{r}$ can be derived from the above equation under the additional assumption that the kinship matrix has approximate rank $r$ and the coefficients $\gamma_{r}$ are fit without constraints. In contrast, the LMM uses all eigenvectors, while effectively shrinking their coefficients $\gamma_{LMM}$ as all random effects models do, although these parameters are marginalized (Astle and Balding, 2009; Janss et al., 2012; Hoffman and Dubé, 2013; Zhang and Pan, 2015). PCA has more parameters than LMM, so it may overfit more: ignoring the shared terms in Equation 2 and Equation 3, PCA fits $r$ parameters (length of $\gamma$), whereas LMMs fit only one ($\sigma_{s}^{2}$).

In practice, the kinship matrix used for PCA and LMM is estimated with variations of a method-of-moments formula applied to standardized genotypes $X_{S}$, which is derived from Equation 4:

$$
X_{S}=(\frac{x_{ij}−2p^_{i}^{T}}{\sqrt{4p^_{i}^{T}(1−p^_{i}^{T})}}),Φ^^{T}=\frac{1}{m}X_{S}^{′}X_{S},
$$

where the unknown $p_{i}^{T}$ is estimated by $p^_{i}^{T}=\frac{1}{2⁢n}⁢\sum_{j=1}^{n}x_{i⁢j}$ (Price et al., 2006; Kang et al., 2008; Kang et al., 2010; Yang et al., 2011; Zhou and Stephens, 2012; Yang et al., 2014; Loh et al., 2015; Sul et al., 2018; Zhou et al., 2018). However, this kinship estimator has a complex bias that differs for every individual pair, which arises due to the use of this estimated $p^_{i}^{T}$(Ochoa and Storey, 2021; Ochoa and Storey, 2019). Nevertheless, in PCA and LMM these biased estimates perform as well as unbiased ones (Hou et al., 2023b).

We selected fast and robust software implementing the basic PCA and LMM models. PCA association was performed with plink2 (Chang et al., 2015). The quantitative trait association model is a linear regression with covariates, evaluated using the t-test. PCs were calculated with plink2, which equal the top eigenvectors of Equation 5 after removing loci with minor allele frequency $MAF<0.1$.

LMM association was performed using GCTA (Yang et al., 2011; Yang et al., 2014). Its kinship estimator equals Equation 5. PCs were calculated using GCTA from its kinship estimate. Association significance is evaluated with a score test. In the small simulation only, GCTA with large numbers of PCs had convergence and singularity errors in some replicates, which were treated as missing data.

### Simulations

Every simulation was replicated 50 times, drawing anew all genotypes (except for real datasets) and traits. Below we use the notation $f_{A}^{B}$ for the inbreeding coefficient of a subpopulation $A$ from another subpopulation $B$ ancestral to $A$. In the special case of the total inbreeding of $A$, $f_{A}^{T}$, $T$ is an overall ancestral population, which is ancestral to every individual under consideration, such as the most recent common ancestor (MRCA) population.

#### Genotype simulation from the admixture model

The basic admixture model is as described previously (Ochoa and Storey, 2021) and is implemented in the R package bnpsd. Both Large and Family simulations have $n=1,000$ individuals, while Small has $n=100$. The number of loci is $m=100,000$. Individuals are admixed from $K=10$ intermediate subpopulations, or ancestries. Each subpopulation $S_{u}$ ($u\in{1,…,K}$) is at coordinate $u$ and has an inbreeding coefficient $f_{S_{u}}^{T}=u⁢\tau$ for some $\tau$. Ancestry proportions $q_{j⁢u}$ for individual $j$ and $S_{u}$ arise from a random walk with spread $\sigma$ on the 1D geography, and $\tau$ and $\sigma$ are fit to give $F_{ST}=0.1$ and mean kinship $\theta¯^{T}=0.5⁢F_{ST}$ for the admixed individuals (Ochoa and Storey, 2021). Random ancestral allele frequencies $p_{i}^{T}$, subpopulation allele frequencies $p_{i}^{S_{u}}$, individual-specific allele frequencies $\pi_{i⁢j}$, and genotypes $x_{i⁢j}$ are drawn from this hierarchical model:

$$
p_{i}^{T}∼Uniform(0.01,0.5),p_{i}^{S_{u}}|p_{i}^{T}∼Beta(p_{i}^{T}(\frac{1}{f_{S_{u}}^{T}}−1),(1−p_{i}^{T})(\frac{1}{f_{S_{u}}^{T}}−1)),\pi_{ij}=\sumu=1Kq_{ju}p_{i}^{S_{u}},x_{ij}|\pi_{ij}∼Binomial(2,\pi_{ij}),
$$

where this Beta is the Balding-Nichols distribution (Balding and Nichols, 1995) with mean $p_{i}^{T}$ and variance $p_{i}^{T}⁢(1-p_{i}^{T})⁢f_{S_{u}}^{T}$. Fixed loci ($i$ where $x_{i⁢j}=0$ for all $j$, or $x_{i⁢j}=2$ for all $j$) are drawn again from the model, starting from $p_{i}^{T}$, iterating until no loci are fixed. Each replicate draws a genotypes starting from $p_{i}^{T}$.

As a brief aside, we prove that global ancestry proportions as covariates is equivalent in expectation to using PCs under the admixture model. Note that the latent space of $X$, which is the subspace to which the data is constrained by the admixture model, is given by $(\pi_{i⁢j})$, which has $K$ dimensions (number of columns of $Q=(q_{j⁢u})$), so the top $K$ PCs span this space. Since associations include an intercept term ($1⁢\alpha$ in Equation 2), estimated PCs are orthogonal to 1  (note $Φ^^{T}1=0$ because $X_{S}⁢1=0$), and the sum of rows of $Q$ sums to one, then only $K-1$ PCs plus the intercept are needed to span the latent space of this admixture model.

#### Genotype simulation from random admixed families

We simulated a pedigree with admixed founders, no close relative pairings, assortative mating based on a 1D geography (to preserve admixture structure), random family sizes, and arbitrary numbers of generations (20 here). This simulation is implemented in the R package simfam. Generations are drawn iteratively. Generation 1 has $n=1000$ individuals from the above admixture simulation ordered by their 1D geography. Local kinship measures pedigree relatedness; in the first generation, everybody is locally unrelated and outbred. Individuals are randomly assigned sex. In the next generation, individuals are paired iteratively, removing random males from the pool of available males and pairing them with the nearest available female with local kinship $<1/4^{3}$ (stay unpaired if there are no matches), until there are no more available males or females. Let $n=1000$ be the desired population size, $n_{m}=1$ the minimum number of children per family and nf the number of families (paired parents) in the current generation, then the number of additional children (beyond the minimum) is drawn from $Poisson⁢(n/n_{f}-n_{m})$. Let $\delta$ be the difference between desired and current population sizes. If $\delta>0$, then $\delta$ random families are incremented by 1. If $\delta<0$, then $|\delta|$ random families with at least $n_{m}+1$ children are decremented by 1. If $|\delta|$ exceeds the number of families, all families are incremented or decremented as needed and the process is iterated. Children are assigned sex randomly, and are reordered by the average coordinate of their parents. Children draw alleles from their parents independently per locus. A new random pedigree is drawn for each replicate, as well as new founder genotypes from the admixture model.

#### Genotype simulation from a subpopulation tree model

This model draws subpopulations allele frequencies from a hierarchical model parameterized by a tree, which is also implemented in bnpsd and relies on the R package ape for general tree data structures and methods (Paradis and Schliep, 2019). The ancestral population $T$ is the root, and each node is a subpopulation $S_{w}$ indexed arbitrarily. Each edge between $S_{w}$ and its parent population $P_{w}$ has an inbreeding coefficient $f_{S_{w}}^{P_{w}}$. $P_{i}^{T}$ are drawn from a given distribution, which is constructed to mimic each real dataset in Appendix 1. Given the allele frequencies $p_{i}^{P_{w}}$ of the parent population, $S_{w}$’s allele frequencies are drawn from:

$$
p_{i}^{S_{w}}|p_{i}^{P_{w}}∼Beta(p_{i}^{P_{w}}(\frac{1}{f_{S_{w}}^{P_{w}}}−1),(1−p_{i}^{P_{w}})(\frac{1}{f_{S_{w}}^{P_{w}}}−1)).
$$

Individuals $j$ in $S_{w}$ draw genotypes from its allele frequency: $x_{ij}|p_{i}^{S_{w}}∼Binomial(2,p_{i}^{S_{w}}).$ Loci with $MAF<0.01$ are drawn again starting from the $p_{i}^{T}$ distribution, iterating until no such loci remain.

#### Fitting subpopulation tree to real data

We developed new methods to fit trees to real data based on unbiased kinship estimates from popkin, implemented in bnpsd. A tree with given inbreeding coefficients $f_{S_{w}}^{P_{w}}$ for its edges (between subpopulation $S_{w}$ and its parent $P_{w}$) gives rise to a coancestry matrix $ϑ_{u⁢v}^{T}$ for a subpopulation pair ($S_{u},S_{v}$), and the goal is to recover these edge inbreeding coefficients from coancestry estimates. Coancestry values are total inbreeding coefficients of the MRCA population of each subpopulation pair. Therefore, we calculate $f_{S_{w}}^{T}$ for every $S_{w}$ recursively from the root as follows. Nodes with parent $P_{w}=T$ are already as desired. Given $f_{P_{w}}^{T}$, the desired $f_{S_{w}}^{T}$ is calculated via the ‘additive edge’ $\delta_{w}$ (Ochoa and Storey, 2021):

$$
f_{S_{w}}^{T}=f_{P_{w}}^{T}+\delta_{w},\delta_{w}=f_{S_{w}}^{P_{w}}(1−f_{P_{w}}^{T}).
$$

These $\delta_{w}\geq0$ because $0\leqf_{S_{w}}^{P_{w}},f_{P_{w}}^{T}\leq1$ for every $w$. Edge inbreeding coefficients can be recovered from additive edges: $f_{S_{w}}^{P_{w}}=\delta_{w}/(1-f_{P_{w}}^{T})$. Overall, coancestry values are sums of $\delta_{w}$ over common ancestor nodes,

$$
ϑ_{uv}^{T}=\sumw\delta_{w}I_{w}(u,v),
$$

where the sum includes all $w$, and $I_{w}⁢(u,v)$ equals 1 if $S_{w}$ is a common ancestor of $S_{u},S_{v}$, 0 otherwise. Note that $I_{w}⁢(u,v)$ reflects tree topology and $\delta_{w}$ edge values.

To estimate population-level coancestry, first kinship ($\phi^_{j⁢k}^{T}$) is estimated using popkin (Ochoa and Storey, 2021). Individual coancestry ($\theta^_{j⁢k}^{T}$) is estimated from kinship using

$$
\theta^_{jk}^{T}={\phi^_{jk}^{T}ifk\neqj,f^_{j}^{T}=2\phi^_{jj}^{T}−1ifk=j.
$$

Lastly, coancestry $ϑ^_{u⁢v}^{T}$ between subpopulations are averages of individual coancestry values:

$$
ϑ^_{uv}^{T}=\frac{1}{|S_{u}||S_{v}|}\sumj\inS_{u}\sumk\inS_{v}\theta^_{jk}^{T}.
$$

Topology is estimated with hierarchical clustering using the weighted pair group method with arithmetic mean (Sokal and Michener, 1958), with distance function $d⁢(S_{u},S_{v})=max⁢{ϑ^_{u⁢v}^{T}}-ϑ^_{u⁢v}^{T},$ which succeeds due to the monotonic relationship between node depth and coancestry (Equation 7). This algorithm recovers the true topology from the true coancestry values, and performs well for estimates from genotypes.

To estimate tree edge lengths, first $\delta_{w}$ are estimated from $ϑ^_{u⁢v}^{T}$ and the topology using Equation 7 and non-negative least squares linear regression (Lawson and Hanson, 1974) (implemented in nnls; Mullen, 2012) to yield non-negative $\delta_{w}$, and $f_{S_{w}}^{P_{w}}$ are calculated from $\delta_{w}$ by reversing Equation 5. To account for small biases in coancestry estimation, an intercept term $\delta_{0}$ is included ($I_{0}⁢(u,v)=1$ for all $u,v$), and when converting $\delta_{w}$ to $f_{S_{w}}^{P_{w}}$, $\delta_{0}$ is treated as an additional edge to the root, but is ignored when drawing allele frequencies from the tree.

#### Trait simulation

Traits are simulated from the quantitative trait model of Equation 1, with novel bias corrections for simulating the desired heritability from real data relying on the unbiased kinship estimator popkin (Ochoa and Storey, 2021). This simulation is implemented in the R package simtrait. All simulations have a fixed narrow-sense heritability of $h^{2}$, a variance proportion due to environment effects $\sigma_{η}^{2}$, and residuals are drawn from $ϵ_{j}∼Normal⁢(0,\sigma_{ϵ}^{2})$ with $\sigma_{ϵ}^{2}=1-h^{2}-\sigma_{η}^{2}$. The number of causal loci m1, which determines the average coefficient size, is chosen with the heuristic formula $m_{1}=round⁡(n⁢h^{2}/8)$, which empirically balances power well with varying $n$ and $h^{2}$. The set of causal loci $C$ is drawn anew for each replicate, from loci with $MAF\geq0.01$ to avoid rare causal variants, which are not discoverable by PCA or LMM at the sample sizes we considered. Letting $v_{i}^{T}=p_{i}^{T}⁢(1-p_{i}^{T})$, the effect size of locus $i$ equals $2⁢v_{i}^{T}⁢\beta_{i}^{2}$, its contribution of the trait variance (Park et al., 2010). Under the fixed effect sizes (FES) model, initial causal coefficients are

$$
\beta_{i}=\frac{1}{\sqrt{2v_{i}^{T}}}
$$

for known $p_{i}^{T}$; otherwise $v_{i}^{T}$ is replaced by the unbiased estimator (Ochoa and Storey, 2021) $v^_{i}^{T}=p^_{i}^{T}⁢(1-p^_{i}^{T})/(1-\phi¯^{T}),$ where $\phi¯^{T}$ is the mean kinship estimated with popkin. Each causal locus is multiplied by –1 with probability 0.5. Alternatively, under the random coefficients (RC) model, initial causal coefficients are drawn independently from $\beta_{i}∼Normal⁢(0,1)$. For both models, the initial genetic variance is $\sigma_{0}^{2}=\sum_{i\inC}2⁢v_{i}^{T}⁢\beta_{i}^{2},$ replacing $v_{i}^{T}$ with $v^_{i}^{T}$ for unknown $p_{i}^{T}$ (so $\sigma_{0}^{2}$ is an unbiased estimate), so we multiply every initial $\beta_{i}$ by $\frac{h}{\sigma_{0}}$ to have the desired heritability. Lastly, for known $p_{i}^{T}$, the intercept coefficient is $\alpha=-\sum_{i\inC}2⁢p_{i}^{T}⁢\beta_{i}.$ When $p_{i}^{T}$ are unknown, $p^_{i}^{T}$ should not replace $p_{i}^{T}$ since that distorts the trait covariance (for the same reason the standard kinship estimator in Equation 5 is biased), which is avoided with

$$
\alpha=−\frac{2}{m_{1}}(\sumi\inCp^_{i}^{T})(\sumi\inC\beta_{i}).
$$

Simulations optionally included multiple environment group effects, similarly to previous models (Zhang and Pan, 2015; Wang et al., 2022), as follows. Each independent environment $i$ has predefined groups, and each group $g$ has random coefficients drawn independent from $η_{g⁢i}∼Normal⁢(0,\sigma_{η⁢i}^{2})$ where $\sigma_{η⁢i}^{2}$ is a specified variance proportion for environment $i$. $Z$ has individuals along columns and environment-groups along rows, and it contains indicator variables: 1 if the individual belongs to the environment-group, 0 otherwise.

We performed trait simulations with the following variance parameters (Table 7): high heritability used $h^{2}=0.8$ and no environment effects; low heritability used $h^{2}=0.3$ and no environment effects; lastly, environment used $h^{2}=0.3,\sigma_{η⁢1}^{2}=0.3,\sigma_{η⁢2}^{2}=0.2$ (total $\sigma_{η}^{2}=\sigma_{η⁢1}^{2}+\sigma_{η⁢2}^{2}=0.5$). For real genotype datasets, the groups are the continental (environment 1) and fine-grained (environment 2) subpopulation labels given (see next subsection). For simulated genotypes, we created these labels by grouping by the index $j$ (geographical coordinate) of each simulated individual, assigning group $g=ceiling⁢(j⁢k_{i}/n)$ where ki is the number of groups in environment $i$, and we selected $k_{1}=5$ and $k_{2}=25$ to mimic the number of groups in each level of 1000 Genomes (Table 2).

**Table 7.**
 Variance parameters of trait simulations.


<table>
  <thead>
    <tr>
      <th>Trait variance type</th>
      <th>h2</th>
      <th>ση2</th>
      <th>σϵ2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>High heritability</td>
      <td>0.8</td>
      <td>0.0</td>
      <td>0.2</td>
    </tr>
    <tr>
      <td>Low heritability</td>
      <td>0.3</td>
      <td>0.0</td>
      <td>0.7</td>
    </tr>
    <tr>
      <td>Environment</td>
      <td>0.3</td>
      <td>0.5</td>
      <td>0.2</td>
    </tr>
  </tbody>
</table>

### Real human genotype datasets

The three datasets were processed as before (Ochoa and Storey, 2019; summarized below), except with an additional filter so loci are in approximate linkage equilibrium and rare variants are removed. All processing was performed with plink2 (Chang et al., 2015), and analysis was uniquely enabled by the R packages BEDMatrix (Grueneberg and de Los Campos, 2019) and genio. Each dataset groups individuals in a two-level hierarchy: continental and fine-grained subpopulations. Final dataset sizes are in Table 2.

We obtained the full (including non-public) Human Origins by contacting the authors and agreeing to their usage restrictions. The Pacific data (Skoglund et al., 2016) was obtained separately from the rest (Lazaridis et al., 2014; Lazaridis et al., 2016), and datasets were merged using the intersection of loci. We removed ancient individuals, and individuals from singleton and non-native subpopulations. Non-autosomal loci were removed. Our analysis of both the whole-genome sequencing (WGS) version of HGDP (Bergström et al., 2020) and the high-coverage NYGC version of 1000 Genomes (Fairley et al., 2020) was restricted to autosomal biallelic SNP loci with filter “PASS”.

Since our evaluations assume uncorrelated loci, we filtered each real dataset with plink2 using parameters “--indep-pairwise 1000kb 0.3”, which iteratively removes loci that have a greater than 0.3 squared correlation coefficient with another locus that is within 1000 kb, stopping until no such loci remain. Since all real datasets have numerous rare variants, while PCA and LMM are not able to detect associations involving rare variants, we removed all loci with $MAF<0.01$. Lastly, only HGDP had loci with over 10% missingness removed, as they were otherwise 17% of remaining loci (for Human Origins and 1000 Genomes they were under 1% of loci so they were not removed). Kinship matrix rank and eigenvalues were calculated from popkin kinship estimates. Eigenvalues were assigned p-values with twstats of the Eigensoft package (Patterson et al., 2006), and kinship matrix rank was estimated as the largest number of consecutive eigenvalue from the start that all satisfy $p<0.01$ (p-values did not increase monotonically). For the evaluation with close relatives removed, each dataset was filtered with plink2 with option “--king-cutoff” with cutoff 0.02209709 ($=2^{-11/2}$) for removing up to 4th degree relatives using KING-robust (Manichaikul et al., 2010), and $MAF<0.01$ filter is reapplied (Table 4).

### Evaluation of performance

All approaches are evaluated using two complementary metrics: $SRMSD_{p}$ quantifies p-value uniformity, and $AUC_{PR}$ measures causal locus classification performance and reflects power while ranking miscalibrated models fairly. These measures are more robust alternatives to previous measures from the literature (Appendix 2), and are implemented in simtrait.

P-values for continuous test statistics have a uniform distribution when the null hypothesis holds, a crucial assumption for type I error and FDR control (Storey, 2003; Storey and Tibshirani, 2003). We use the Signed Root Mean Square Deviation ($SRMSD_{p}$) to measure the difference between the observed null p-value quantiles and the expected uniform quantiles:

$$
SRMSD_{p}=sgn(u_{median}−p_{median})\sqrt{\frac{1}{m_{0}}\sumi=1m_{0}(u_{i}−p_{(i)})^{2}},
$$

where $m_{0}=m-m_{1}$ is the number of null (non-causal) loci, here $i$ indexes null loci only, $p_{(i)}$ is the $i$ th ordered null p-value, $u_{i}=(i-0.5)/m_{0}$ is its expectation, $p_{median}$ is the median observed null p-value, $u_{median}=\frac{1}{2}$ is its expectation, and sgn is the sign function (1 if $u_{median}\geqp_{median}$, –1 otherwise). Thus, $SRMSD_{p}=0$ corresponds to calibrated p-values, $SRMSD_{p}>0$ indicate anti-conservative p-values, and $SRMSD_{p}<0$ are conservative p-values. The maximum $SRMSD_{p}$ is achieved when all p-values are zero (the limit of anti-conservative p-values), which for infinite loci approaches

$$
SRMSD_{p}→\sqrt{\int_{0}^{1}u^{2}du}=\frac{1}{\sqrt{3}}≈0.577.
$$

The same value with a negative sign occurs for all p-values of 1.

Precision and recall are standard performance measures for binary classifiers that do not require calibrated p-values (Grau et al., 2015). Given the total numbers of true positives (TP), false positives (FP) and false negatives (FN) at some threshold or parameter $t$, precision and recall are

$$
Precision(t)=\frac{TP(t)}{TP(t)+FP(t)},Recall(t)=\frac{TP(t)}{TP(t)+FN(t)}.
$$

Precision and Recall trace a curve as $t$ is varied, and the area under this curve is $AUC_{PR}$. We use the R package PRROC to integrate the correct non-linear piecewise function when interpolating between points. A model obtains the maximum $AUC_{PR}=1$ if there is a $t$ that classifies all loci perfectly. In contrast, the worst models, which classify at random, have an expected precision ($=AUC_{PR}$) equal to the overall proportion of causal loci: $m_{1}/m$.

### Data and code availability

The data and code generated during this study are available on GitHub at https://github.com/OchoaLab/pca-assoc-paper (copy archived at Ochoa, 2023). The public subset of Human Origins is available on the Reich Lab website at https://reich.hms.harvard.edu/datasets; non-public samples have to be requested from David Reich. The WGS version of HGDP was downloaded from the Wellcome Sanger Institute FTP site at ftp://ngs.sanger.ac.uk/production/hgdp/hgdp_wgs.20190516/. The high-coverage version of the 1000 Genomes Project was downloaded from ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/data_collections/1000G_2504_high_coverage/working/20190425_NYGC_GATK/.

### Web resources

plink2, https://www.cog-genomics.org/plink/2.0/ ; GCTA, https://yanglab.westlake.edu.cn/software/gcta/ ; Eigensoft, https://github.com/DReichLab/EIG ; bnpsd, https://cran.r-project.org/package=bnpsd ; simfam, https://cran.r-project.org/package=simfam ; simtrait, https://cran.r-project.org/package=simtrait ; genio, https://cran.r-project.org/package=genio ; popkin, https://cran.r-project.org/package=popkin ; ape, https://cran.r-project.org/package=ape ; nnls, https://cran.r-project.org/package=nnls ; PRROC, https://cran.r-project.org/package=PRROC ; BEDMatrix, https://cran.r-project.org/package=BEDMatrix.
