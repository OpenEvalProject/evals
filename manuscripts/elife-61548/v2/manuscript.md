# Demographic history mediates the effect of stratification on polygenic scores

## Authors

- Arslan A Zaidi<sup>1</sup> ([ORCID: 0000-0002-2155-8367](https://orcid.org/0000-0002-2155-8367)) †
- Iain Mathieson<sup>1</sup> †

### Affiliations

1. Department of Genetics, Perelman School of Medicine, University of Pennsylvania Philadelphia United States

† Corresponding author

## Abstract

Population stratification continues to bias the results of genome-wide association studies (GWAS). When these results are used to construct polygenic scores, even subtle biases can cumulatively lead to large errors. To study the effect of residual stratification, we simulated GWAS under realistic models of demographic history. We show that when population structure is recent, it cannot be corrected using principal components of common variants because they are uninformative about recent history. Consequently, polygenic scores are biased in that they recapitulate environmental structure. Principal components calculated from rare variants or identity-by-descent segments can correct this stratification for some types of environmental effects. While family-based studies are immune to stratification, the hybrid approach of ascertaining variants in GWAS but reestimating effect sizes in siblings reduces but does not eliminate stratification. We show that the effect of population stratification depends not only on allele frequencies and environmental structure but also on demographic history.

## Introduction

Population structure refers to patterns of genetic variation that arise due to non-random mating. If these patterns are correlated with environmental factors, they can lead to spurious associations and biased effect size estimates in genome-wide association studies (GWAS). Approaches such as genomic control (GC) (Devlin and Roeder, 1999), principal component analysis (PCA) (Price et al., 2006), linear mixed models (LMMs) (Kang et al., 2010; Loh et al., 2015) and linkage disequilibrium score regression (LDSC) (Bulik-Sullivan et al., 2015a) have been developed to detect and correct for this stratification. However, these approaches do not necessarily remove all stratification, particularly when multiple studies are meta-analyzed (Berg et al., 2019; Sohail et al., 2019). Large GWAS in relatively homogeneous populations, such as the UK Biobank (UKB) (Bycroft et al., 2018), should alleviate many of these concerns. However, such populations still exhibit fine-scale population structure (Leslie et al., 2015; Karakachoff et al., 2015; Kerminen et al., 2017; Haworth et al., 2019; Raveane et al., 2019; Bycroft et al., 2019; Byrne et al., 2020). The extent to which this fine structure impacts GWAS inference in practice is largely unknown, and it is not clear whether existing methods adequately correct for it. This question has become increasingly acute in light of the recent focus on polygenic scores for disease risk prediction (Torkamani et al., 2018; Knowles and Ashley, 2018). Polygenic scores for many physical and behavioral traits exhibit geographic clustering within the UK even after stringent correction for population structure (Haworth et al., 2019; Abdellaoui et al., 2019). Although some of this variation may be attributed to recent migration patterns (Abdellaoui et al., 2019), it could also reflect residual stratification in effect size estimates (Lawson et al., 2020).

To address these questions, we investigated the effect of population structure on GWAS in a simulated population with a similar degree of structure to the UK Biobank. We considered the fact that different demographic histories can give rise to the same overall degree of population structure (in terms of statistics such as $F_{S⁢T}$ and the genomic inflation factor, λ). This is relevant because the degree to which common and rare variants are impacted by, and are thus informative about, population structure depends on demographic history. It is therefore important to understand the demographic history of GWAS populations in order to assess the consequences of stratification.

## Results

### Rare variants capture recent population structure

We leveraged recent advances in our understanding of human history to simulate GWAS under different realistic demographic models. We simulated population structure using a six-by-six lattice-grid arrangement of demes with two different symmetric stepping-stone migration models (Figure 1). First, a model where the structure extends infinitely far back in time (perpetual structure model; e.g. Mathieson and McVean, 2012) and second, a model where the structure originated 100 generations ago (recent structure model). This second model is motivated by the observation from ancient DNA that Britain experienced an almost complete population replacement within the last 4,500 years (Olalde et al., 2018), providing an upper bound for the establishment of present-day geographic structure in Britain. We set the migration rates in the two models to match the degree of population structure in the UK Biobank, measured by the average $F_{S⁢T}$ between regions (Leslie et al., 2015) and the genomic inflation factor for a GWAS of birthplace in individuals with ‘White British’ ancestry from the UK Biobank (Haworth et al., 2019).

![Figure 1.](https://cdn.elifesciences.org/articles/61548/elife-61548-fig1-v2.jpg)

**Figure 1.:** Panels show the first and second principal components (PCs) of the genetic relationship matrix constructed from either common (upper row) or rare (lower row) variants. Each point is an individual (N = 9,000) and their color represents the deme in the grid (upper left) from which they were sampled. Both common (minor allele frequency >0.05) and rare (minor allele count = 2, 3, or 4) variants can be informative when population structure is ancient (left column; $\tau=∞$ represents the time in generations in the past at which structure disappears) but only rare variants are informative about recent population structure (right column; $\tau=100$ generations). Number of variants used for PCA: 200,000 (upper row), 1 million (lower left), and ≈750,000 (lower right).

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/61548/elife-61548-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) Proportion of variance in the first five rare-PCs (green) explained by 50 common-PCs (and vice versa). (B) Proportion of variance in rare-PC 1 and 2 explained by 50 common-PCs calculated using increasing number of common variants.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/61548/elife-61548-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** (A) Imputation accuracy as a function of frequency on a single chromosome. Even though imputation accuracy for rare variants is lower than that for common variants, (B) imputed rare variants still capture population structure in the ‘recent structure’ model. Alternatively, (C,D) PCA on IBD-sharing can be used to capture recent population structure.

Population structure in the two models is qualitatively different, even though $F_{S⁢T}$ is the same. When structure is recent, it is driven largely by rare variants which tend to have a more recent origin (Gravel et al., 2011; Fu et al., 2013; O'Connor et al., 2015) and are therefore less likely to be shared among demes. Common variants, because they are older and usually predate the onset of structure in our model, are more likely to be shared among demes and have not drifted enough in 100 generations to capture the spatial structure effectively. Therefore, recent structure is captured by the principal components of rare variants (rare-PCA) but not common variants (common-PCA) (Figure 1). In fact, 100 common-PCs altogether explain only 3% of the variance in rare-PC1 (Figure 1—figure supplement 1). In comparison, when population structure is perpetual, both common and rare variants carry information about spatial structure (Figure 1, Figure 1—figure supplements 1, 100 common-PCs explain 50% of the variance in rare-PC1). The two models discussed here represent somewhat extreme demographic scenarios and in reality, the degree to which common and rare variants capture independent aspects of population structure will depend on how the structure varies through time (Figure 1—figure supplement 1).

PCA with rare variants requires sequence data. When only genotype data are available, imputed rare variants can be used Figure 1—figure supplement 2. However, the practical utility of this approach would depend on the imputation accuracy which in turn depends on the population, the imputation algorithm and the reference panel (Das et al., 2018). Another alternative is to carry out PCA on haplotype or identity-by-descent (IBD) sharing, which is also informative about recent population structure (Figure 1—figure supplement 2).

### The impact of population stratification depends on demographic history

That common variants fail to capture recent population structure has important implications for GWAS. Most GWAS use PCA or LMMs, both of which rely on the genetic relatedness matrix (GRM) to describe population structure. Since rare variants are not well-represented on SNP arrays, the GRM is usually constructed from common variants. This will lead to insufficient correction if common variants do not adequately capture recent population structure. To test this, we simulated a GWAS (N = 9,000) of a non-heritable phenotype (i.e. $h^{2}=0$) with an environmental component that is either smoothly (e.g. latitude) or sharply (e.g. local effects) distributed in space (Figure 2). We calculated GRMs using either common (minor allele frequency, MAF > 0.05) or rare variants (minor allele count, MAC = 2, 3, or 4), and included the first 100 PCs in the model to correct for population structure.

![Figure 2.](https://cdn.elifesciences.org/articles/61548/elife-61548-fig2-v2.jpg)

**Figure 2.:** (A) Perpetual structure and (B) recent structure. Upper and lower rows show results for smoothly and sharply distributed environmental risk, respectively, whereas columns show different methods of correction. The simulated phenotype has no genetic contribution so any deviation from the diagonal represents inflation in the test statistic. Each panel shows QQ plots for -log10 p-value for common (orange) and rare (blue) variants. Insets show inflation ($\lambda_{p}$) in the tail (99.9th percentile) of the distribution. Results are averaged across 20 simulations of the phenotype.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/61548/elife-61548-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Models were fitted with either a genetic relatedness matrix constructed with common variants (left column) or with rare variants (right column). Insets show the 99.9% tail of the inflation factor. Orange and blue colored lines refer to common and rare variants, respectively. Results shown for a single simulation of the phenotype.

When population structure is recent, smooth environmental effects lead to an inflation in common, but not rare, variants and this inflation can only be corrected with rare- but not common-PCs (Figure 2B, top row). This is a consequence of the fact that rare variants carry more information about recent structure than common variants (Figure 1). We find similar results using LMMs instead of PCA (Figure 2—figure supplement 1). Therefore, in studies with recent structure, such as the UKB, neither PCA- nor LMM-based methods will fully correct for stratification as long as the GRM is derived from common variants. In contrast, under the perpetual structure model, both common and rare variants may be inflated due to smooth environmental effects (Figure 2A, top row), but this inflation is largely corrected with either common- or rare-PCs (Figure 2A, top row).

Local environmental effects largely impact rare variants only (Mathieson and McVean, 2012; Figure 2A, lower row) and the inflation due to local effects cannot be fully corrected using either common- or rare-PCs (Figure 2A and B, lower row). This is because local environmental effects cannot be represented by a linear combination of the first hundred principal components. Importantly, local effects only impact a small subset of variants—those clustered in the affected deme(s)—resulting in inflation only in the tails of the test statistic distribution (Figure 2). This pattern of inflation cannot be detected using standard genomic inflation, which assumes that stratification impacts enough variants to shift the median of the test statistic (Devlin and Roeder, 1999), making it difficult to distinguish between true associations and residual stratification.

### Burden tests are relatively robust to local environmental effects

In practice, single rare variant association tests are often underpowered. To circumvent this, many studies aggregate information across multiple rare variants in a gene. Because they aggregate across rare variants, such tests have the potential to be affected by rare variant stratification (Mathieson and McVean, 2012). To study this, we examined the behavior of a simple gene burden statistic—the total number of rare derived alleles (frequency < 0.001) in each gene. We find that for a gene of average size (total exon length of ≈1.3 kb, mean of 16 rare variants), burden tests are robust to local effects under both perpetual and recent structure models (Figure 3). Because the burden statistic involves averaging over many variants, it behaves more like a common variant than a rare variant in terms of its spatial distribution (Figure 3—figure supplement 1). Thus, it is still susceptible to confounding by smoothly distributed environmental effects, but this can be corrected by common-PCA in the perpetual structure model or rare-PCA in either model (Figure 3).

![Figure 3.](https://cdn.elifesciences.org/articles/61548/elife-61548-fig3-v2.jpg)

**Figure 3.:** QQ plots of expected and observed -log10p-value under the (A) perpetual and (B) recent structure models for the association of rare variant burden across a gene with total exon length of 1.3 kb (gene length of 7 kb) and non-heritable phenotype with a smooth (upper) or sharp (lower) distribution of environmental effects. Orange and green lines show results for a gene with and without recombination, respectively. Inset shows inflation in the tail (99.9%) of the test statistic distribution.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/61548/elife-61548-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) Gray curves are individual variants (1,000 sampled uniformly at random for plotting), and red lines indicate the mean curve across all 1,000 variants. The diagonal represents the case where the variant/burden is uniformly distributed over the entire grid. Common variants tend to be more widely distributed (left panel) than rare variants (right) as illustrated by the grid inset. (B) Each curve represents a single gene (10,000 sampled), and the yellow line represents the mean across genes. The color of a curve represents the number of rare variants across which burden is aggregated. As the number of variants increases, gene burden behaves more like a common variant in its spatial distribution.

More generally, the spatial distribution of gene burden depends on the number of variants and the recombination distance across which it is aggregated. Gene burden should become geographically less localized with an increase in the number of aggregated rare variants as each is likely to arise in an independent branch of the genealogy (Figure 3—figure supplement 1). As genetic distance between mutations increases, recombination decouples genealogies on which they arise, further reducing the probability of multiple mutations occurring on the same branch. Conversely, the rare variant burden aggregated across few variants in genes with little recombination behaves more like a single rare variant and is susceptible to local effects (Figure 3B lower row).

### Polygenic scores capture residual environmental stratification

Polygenic scores—constructed by summing the effects of large numbers of associated variants—offer a simple way to make genetic risk predictions. At least in European ancestry populations, they can explain a substantial proportion of the phenotypic variance in complex traits like height (Yengo et al., 2018), BMI (Yengo et al., 2018), and coronary artery disease risk (Khera et al., 2018). However, their practical utility is limited by lack of transferability between populations (Scutari et al., 2016; Martin et al., 2017; Kerminen et al., 2019; Wang et al., 2020b) and between subgroups within populations (Mostafavi et al., 2020). This may be due in part to stratification in polygenic scores. To understand the behavior of polygenic scores under the perpetual and recent structure models, we simulated GWAS (N = 9000) of a heritable phenotype with a genetic architecture similar to that of height. We used GWAS effect sizes to calculate polygenic scores in an independent sample (N = 9000) and subtracted the true genetic values for each individual to examine the spatial bias in polygenic scores due to stratification.

Under both perpetual and recent structure models, residual polygenic scores are spatially structured, recapitulating environmental effects even when 100 common-PCs are used as covariates in the GWAS (Figure 4). LMMs perform similarly (Figure 4—figure supplement 1). This is due to the fact that when population stratification is not fully corrected, the effect sizes of variants that are correlated with the environment tend to be over- or under-estimated depending on the direction and strength of correlation (Figure 4—figure supplement 2). Stratification in residual polygenic scores is minimal when the causal variants are known, but not when the score is constructed from the most significant SNPs (‘lead SNPs’) (Figure 4, Figure 4—figure supplement 3)—almost always the case in practice. Thus, picking the most significant SNPs (clumping and thresholding) tends to enrich for variants that are more structured than the causal variants, and improvements through statistical fine-mapping are marginal (Figure 4—figure supplement 3). Polygenic scores will be especially prone to residual stratification when constructed using SNPs that do not reach genome-wide significance. At such loci, the causal effects are likely to be small relative to the effect of stratification, leading to false identification of more structured variants.

![Figure 4.](https://cdn.elifesciences.org/articles/61548/elife-61548-fig4-v2.jpg)

**Figure 4.:** The simulated phenotype in the training sample has a heritability of 0.8, distributed over 2,000 causal variants. Each small square is colored with the mean residual polygenic score for that deme in the test sample, averaged over 20 independent simulations of the phenotype. In each panel, the rows represent different methods of PCA correction and columns represent two different methods of variant ascertainment. ‘Causal’ refers to causal variants with p-value < 5×10−4, and ‘Lead SNP’ refers to a set of variants, where each represents the most significantly associated SNP with a p-value < 5×10−4 in a 100 kb window around the causal variant. The simulated environment is shown on the left. For the sharp effect, the affected deme is highlighted with an asterisk.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/61548/elife-61548-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** Residual polygenic score in each deme was averaged across all individuals from that deme and over 10 simulations of the phenotype. The terms 'Causal' and 'Lead SNP' refer to polygenic scores constructed with known causal variants and topmost significant SNPs, respectively.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/61548/elife-61548-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** Each panel shows the comparison of the true (simulated) and estimated effect sizes of causal variants (M = 2000) for different modes of correction for population structure and when the environment is smoothly distributed in a North-South cline. The color of each bin represents the mean correlation of variants in that bin and latitude, averaged across 20 simulations. When there is residual stratification, the effect sizes of variants that are positively correlated with latitude are biased upwards, whereas the effect sizes of variants that are negatively correlated are biased downwards. Even though the effect size of any single variant may be biased due to stratification, the effect size across all variants is still unbiased. In this particular case, because the population structure has a recent origin, rare-PCA, but not common-PCA adequately removes the bias.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/61548/elife-61548-fig4-figsupp3-v2.jpg)

**Figure 4—figure supplement 3.:** Polygenic scores were calculated using (A) causal variants with p-value < 5e-04, (B) variants fine-mapped with SuSiE in windows where at least one variant has a p-value < 5e-04, and (C) the most significantly associated variants in windows where at least one variant has a p-value < 5e-04. Results presented here are based on the recent structure model. Bias is measured by the correlation between polygenic score and latitude (the confounding environmental effect) and prediction accuracy is measured by the proportion of variance in genetic value of an individual explained by their polygenic score. Red dashed lines represent the observed mean of the distribution.

### The effect of stratification in more complex models

In reality, genetic structure in most studies is more complex than either model discussed above. Most populations are genetically heterogeneous, and each genome is shaped by processes such as ancient and recent admixture, non-random mating, and selection, all of which vary both spatially and temporally. The present-day population of Britain, for example, is the result of a complex history of migration and admixture (Leslie et al., 2015; Olalde et al., 2018). Thus, restricting analysis even to the ‘White British’ subset of UK Biobank involves population structure on multiple time scales. To study these effects, we simulated under a model based on the demographic history of Europe and geographic structure of England and Wales, while maintaining the same degree of structure as the previous models (Figure 5, Table 1). In addition to recent geographic structure, we simulated an admixture event 100 generations ago between two populations, each of which are themselves the result of mixtures between several ancient populations (Figure 5). We varied the admixture fraction from the two source populations to create a North-South ancestry cline and sampled individuals to mimic uneven sampling in the UK Biobank (Figure 5, Materials and methods).

![Figure 5.](https://cdn.elifesciences.org/articles/61548/elife-61548-fig5-v2.jpg)

**Figure 5.:** (A) Illustration of the simulated demography. (B) Maps depicting the spatial distribution of residual polygenic scores, as in Figure 4, averaged across 20 simulations of the phenotype. Columns: ‘Smooth’ and ‘Sharp’ refer to environmental effects and ‘Causal‘ and ‘Lead SNP’ refer to sets of variants that were used to construct polygenic scores. Rows: Different methods of correction for population structure. WHG and EHG: Western and Eastern Hunter Gatherers; EF: Early Farmers.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/61548/elife-61548-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** Each region is colored with the mean residual polygenic score across 250 individuals and 20 random iterations. ‘Smooth’ refers to a North-South environmental risk and ‘Sharp’ refers to a local environmental risk (risk location indicated with *). Polygenic scores were constructed using either the true causal variants (Causal) or the topmost significant SNPs (Lead SNPs). Compare this to Figure 5 where individuals are sampled non-uniformly.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/61548/elife-61548-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** (A) Principal component analysis (PCA) on common variants shows little or no structure. PCA on (B) rare variants and (C) IBD-sharing captures population structure effectively. (D) Genomic inflation in summary statistics for GWAS on the non-heritable 'Smooth' phenotype as a function of frequency of variants used in PCA. Single genetic relatedness matrix (GRM; orange) refers to the inflation observed with PCs calculated using a single GRM constructed from variants in the given frequency bin. Multiple GRM (blue) refers to the inflation with two sets of PCs calculated separately: 50 PCs from common variants (MAF>0.05) and 50 PCs from variants in the given frequency bin. .

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/61548/elife-61548-fig5-figsupp3-v2.jpg)

**Figure 5—figure supplement 3.:** (A) Variance in longitude, latitude, and the sharply distributed phenotype explained by 100 PCs under the complex demographic model. PCs explain more variance in longitude and latitude than in the Sharp phenotype because it is difficult to express the latter as a linear combination of PCs. Note, that PCs explain more variance in latitude than in longitude. This is because under the complex structure model, there is ancestry stratification in the north-south direction in addition to recent structure due to isolation by distance. Importantly, PCs computed separately from common and rare variants explain more of the structure than PCs computed from a single GRM constructed from common and rare variants together. (B) Variance explained in the sharp phenotype.

**Table 1.**
 Mean observed FST for different migration rate under each demographic model.


<table>
  <thead>
    <tr>
      <th>Model</th>
      <th>Migration rate1</th>
      <th>Mean FST (95% C.I.)</th>
      <th>λ (Latitude)</th>
      <th>λ (Longitude)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Recent</td>
      <td>0.001</td>
      <td>3.8e-03 (3.7e-03 - 4e-03)</td>
      <td>3.5649</td>
      <td>3.7808</td>
    </tr>
    <tr>
      <td>Recent</td>
      <td>0.0025</td>
      <td>2.6e-03 (2.5e-03–2.7e-03)</td>
      <td>3.4733</td>
      <td>3.6425</td>
    </tr>
    <tr>
      <td>Recent</td>
      <td>0.005</td>
      <td>1.6e-03 (1.5e-03–1.7e-03)</td>
      <td>3.0914</td>
      <td>3.1357</td>
    </tr>
    <tr>
      <td>Recent</td>
      <td>0.0075</td>
      <td>1.5e-03 (1.4e-03–1.6e-03)</td>
      <td>3.4661</td>
      <td>3.3344</td>
    </tr>
    <tr>
      <td>Recent</td>
      <td>0.01</td>
      <td>1.1e-03 (1e-03–1.2e-03)</td>
      <td>3.0629</td>
      <td>3.0675</td>
    </tr>
    <tr>
      <td>Recent</td>
      <td>0.015</td>
      <td>7.9e-04 (7.2e-04–8.6e-04)</td>
      <td>2.8256</td>
      <td>2.5172</td>
    </tr>
    <tr>
      <td>Recent</td>
      <td>0.02</td>
      <td>7e-04 (6.3e-04–7.7e-04)</td>
      <td>2.4668</td>
      <td>2.6838</td>
    </tr>
    <tr>
      <td>Recent</td>
      <td>0.025</td>
      <td>5.1e-04 (4.4e-04–5.9e-04)</td>
      <td>2.2173</td>
      <td>2.6485</td>
    </tr>
    <tr>
      <td>Recent</td>
      <td>0.03</td>
      <td>4e-04 (3.3e-04–4.6e-04)</td>
      <td>2.4842</td>
      <td>2.2036</td>
    </tr>
    <tr>
      <td>Recent</td>
      <td>0.05*</td>
      <td>2.3e-04 (1.7e-04–2.9e-04)</td>
      <td>1.6754</td>
      <td>1.8486</td>
    </tr>
    <tr>
      <td>Perpetual</td>
      <td>0.06</td>
      <td>2.5e-04 (1.9e-04–3.1e-04)</td>
      <td>1.8101</td>
      <td>1.7606</td>
    </tr>
    <tr>
      <td>Perpetual</td>
      <td>0.07*</td>
      <td>2.0e-04 (1.4e-04–2.6e-04)</td>
      <td>1.6640</td>
      <td>1.6381</td>
    </tr>
    <tr>
      <td>Perpetual</td>
      <td>0.08</td>
      <td>1.7e-04 (1.1e-04–2.3e-04)</td>
      <td>1.5905</td>
      <td>1.6658</td>
    </tr>
    <tr>
      <td>Complex</td>
      <td>0.05</td>
      <td>3.2e-04 (2.5e-04–3.8e-04)</td>
      <td>2.6425</td>
      <td>1.7480</td>
    </tr>
    <tr>
      <td>Complex</td>
      <td>0.06</td>
      <td>2.8e-04 (2.1e-04–3.4e-04)</td>
      <td>2.1651</td>
      <td>1.8637</td>
    </tr>
    <tr>
      <td>Complex</td>
      <td>0.07</td>
      <td>2.5e-04 (1.8e-04–3.1e-04)</td>
      <td>1.9318</td>
      <td>1.7012</td>
    </tr>
    <tr>
      <td>Complex</td>
      <td>0.08*</td>
      <td>1.5e-04 (9.7e-05–2.1e-04)</td>
      <td>1.6520</td>
      <td>1.5214</td>
    </tr>
    <tr>
      <td>Complex</td>
      <td>0.09</td>
      <td>1.7e-04 (1.1e-04–2.2e-04)</td>
      <td>1.6841</td>
      <td>1.3892</td>
    </tr>
    <tr>
      <td>Complex</td>
      <td>0.1</td>
      <td>1.7e-04 (1.2e-04–2.3e-04)</td>
      <td>1.5943</td>
      <td>1.4719</td>
    </tr>
    <tr>
      <td>Complex</td>
      <td>0.12</td>
      <td>1.3e-04 (7.3e-05–1.8e-04)</td>
      <td>1.4442</td>
      <td>1.4395</td>
    </tr>
    <tr>
      <td>Complex</td>
      <td>0.15</td>
      <td>7.9e-05 (2.7e-05–1.3e-04)</td>
      <td>1.2536</td>
      <td>1.3123</td>
    </tr>
  </tbody>
</table>

_Proportion of migrants in and out of a deme per generation. Selected migration rate indicated with * for each model._

The results under this model are very similar to the recent structure model in that when the environmental effect is smoothly distributed, it cannot be corrected using common-PCA as population structure is largely recent (Figure 5). Note also that correction is not complete even with rare-PCA as seen from the biased polygenic scores of individuals from Cornwall, in the south-west of England (lower left deme in Figure 5B). This is not due to reduced migration in the region (‘edge effects’) but rather to uneven sampling (only 17 individuals sampled from Cornwall as opposed to 250 under uniform sampling). The bias disappears when individuals are sampled uniformly (Figure 5—figure supplement 1). Thus, our ability to correct for stratification and the utility of polygenic scores also depends on the sampling design of the GWAS. As with the other models, local effects cannot be corrected using either common- or rare-PCA (Figure 5).

### Polygenic scores based on effect sizes reestimated in siblings are not immune to stratification

Sibling-based studies test for association between siblings’ phenotypic and genotypic differences. These, and other family-based association tests, are robust to population stratification as any difference in siblings’ genotypes is due to Mendelian segregation and therefore uncorrelated with environmental effects. We simulated sibling pairs under the recent structure model and confirmed that polygenic scores constructed using SNPs and their effect sizes from the sibling-based tests were uncorrelated with environmental variation (Figure 6 lower row).

![Figure 6.](https://cdn.elifesciences.org/articles/61548/elife-61548-fig6-v2.jpg)

**Figure 6.:** Phenotypes simulated as in Figure 4. (A) Spatial distribution of polygenic scores generated using (top) effects of variants discovered in a standard genome-wide association study (GWAS; middle) variants ascertained in a standard GWAS but with effect sizes reestimated in sib-based design, (bottom) variants ascertained and effect sizes estimated in sib-based design. In each case, the effect is averaged over 20 simulations. (B) Bias and (C) predictive accuracy of polygenic scores for 20 simulations of the smooth environmental effect.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/61548/elife-61548-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** The polygenic scores were calculated using variants and their effect sizes in a standard genome-wide association study (GWAS; top row), variants ascertained in a standard GWAS and effects reestimated in sibling pairs (middle row), or a full sibling-based design where both variants and their effects are obtained in sibling pairs. Polygenic scores were averaged across 20 random simulations of the phenotype.

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/61548/elife-61548-fig6-figsupp2-v2.jpg)

**Figure 6—figure supplement 2.:** The bias is smallest and prediction accuracy greatest when variants are ascertained in a standard genome-wide association study (GWAS) and their effects reestimated in an independent sample of unrelated individuals (middle row). This explains the bias and prediction accuracy seen when variants were ascertained in a standard GWAS and their effects reestimated in siblings Figure 6. Shown, for comparison, is the bias and prediction accuracy of polygenic scores calculated from effects discovered in a standard GWAS of 9K (top row) and 18K individuals (bottom row), respectively. Even though a larger GWAS improves prediction accuracy slightly, it also increases the bias. Blue dashed lines represent the expected bias and red dashed lines represent the observed mean of the distribution.

In practice, however, sample sizes for sibling-based studies are much smaller than standard GWAS. A possible hybrid approach is to first ascertain significantly associated SNPs in a standard GWAS and then reestimate effect sizes in siblings. However, this approach is not completely immune to stratification. To demonstrate, we took the significant lead SNPs from a standard GWAS, reestimated their effect sizes in an independent set of 9,000 sibling pairs simulated under the same demographic model, and then generated polygenic scores in a third, independent, sample of 9,000 unrelated individuals. Polygenic scores generated this way are still correlated with the environmental effect when it is smoothly distributed, although less than when effect sizes from the discovery GWAS are used (Figure 6). Even though the sibling reestimated effects are unbiased, stratification in the polygenic score persists because the frequencies of the lead SNPs are systematically correlated with the environment. This is less pronounced for local effects because stratification is driven by variants that are rare in the discovery sample and often absent in the test sample (Figure 6—figure supplement 1).

One argument in favor of the hybrid approach is that it balances the trade-off between bias and prediction accuracy. We show that the predictive accuracy of this approach is indeed higher than if both variants and effects were discovered in either standard or sibling GWAS (Figure 6). However, this is not an effect of the hybrid approach specifically but that of reestimation in general. Reestimating effect sizes in an independent cohort of unrelated individuals produces similar improvements in bias and prediction accuracy of polygenic scores (Figure 6—figure supplement 2).

## Discussion

The effect of population structure on GWAS depends on the amount of structure, the frequency of the variants tested and the distribution of confounding environmental effects. Here, we demonstrated that it also depends on the demographic history of the population in a way that is not fully captured by the degree of structure as summarized by $F_{S⁢T}$ and genomic inflation. Consequently, to fully correct for population structure, it is necessary to know not only the degree of realized structure, but also the demographic history that generated it.

Generally, PCA (or mixed models) based on common variants will inadequately capture and correct population structure with a recent origin. This might partly explain why polygenic scores derived from studies such as the UK Biobank (Haworth et al., 2019; Abdellaoui et al., 2019) and FINNRISK (Kerminen et al., 2019) exhibit geographic clustering. In such cases, PCA based on rare variants, which are more informative about recent population history (Gravel et al., 2011; Fu et al., 2013; O'Connor et al., 2013; O'Connor et al., 2015; Mathieson and McVean, 2015), would be more effective. Haplotype sharing (Lawson et al., 2012) or identity-by-descent (IBD) segments are similarly informative about recent history (Palamara et al., 2012; Ralph and Coop, 2013; Saada et al., 2020), and provide an alternative to rare variant PCA when sequence data are not available, or when there are relatively few rare variants to adequately capture the structure, for example in exome sequence data.

This still leaves the question of exactly which frequency of variants (or length of IBD segments) to use. The structure in most studies exists on multiple time scales, even in relatively homogeneous populations (Byrne et al., 2020). In such cases, sets of PCs derived from variants in different frequency bins, or from IBD segments of different lengths, may be needed. PCs can be chosen based on visual inspection for significant axes of population structure (e.g. Figure 5—figure supplement 2A–C). However, even among the PCs that exhibit population structure, not all will contribute to the phenotype unless they are correlated with the confounding environmental effect(s), the distribution of which is a priori unknown. An empirical solution to this problem is to carry out a set of preliminary GWAS, each with different sets of PCs and use the summary statistics with the smallest inflation (Figure 5—figure supplement 2D). By letting the model learn the weights of PCs derived from different frequency bins, this approach has the added benefit of allowing for non-linearity in the contribution of stratification at different time scales. For example, under our complex model, using both common- and rare-PCs corrects for structure better than models where either rare- or common-PCs were used alone (Figure 5—figure supplement 3).

PCA- or LMM-based corrections are only effective when environmental effects are smoothly distributed with respect to ancestry or when they can be expressed as a linear function of the GRM. Sharply distributed effects (e.g. local environment or batch effects) may not be fully corrected with any method, regardless of the demographic history of the population. Such confounders are an important concern for rare variant studies. Because local effects lead to inflation in the tails of the test statistic distribution, single rare variant associations should always be treated with caution. Fortunately, burden tests are more robust to local effects than single rare variant tests, although, the degree to which burden statistics will be sensitive to local effects depends on the number of variants and the recombination distance between them—short genes with fewer variants will be more sensitive to local effects.

Even imperfect correction for population structure is probably sufficient to limit the number of genome-wide false positive associations in GWAS. But when information is aggregated across a large number of marginally associated variants, even small overestimates in effect sizes can lead to substantial bias in polygenic scores. Essentially some of the predictive power of polygenic scores will derive from predicting environmental structure rather than genetic effects. Comparison of polygenic scores derived from standard GWAS and sibling-based studies suggests that this effect can be substantial (Mostafavi et al., 2020), and it may also contribute to inflated estimates of heritability and genetic correlation (Browning and Browning, 2011). Even though family-based studies are immune to stratification, we show that the practice of discovering associations in a standard GWAS and then reestimating their effects in siblings improves prediction and reduces, but does not eliminate, bias in polygenic scores if there is inadequate correction in the original GWAS. However, this is largely because of the advantages of reestimating effect sizes in a different sample, rather than specifically because of the use of siblings.

Our study focused on population structure arising from ancient admixtures and geographic structure because these are relatively well-understood and easy to model. However, our results generalize to any type of population structure, for example due to social stratification or assortative mating. What we refer to as local environmental effects also includes socially structured factors such as cultural practices. Ultimately, no single approach can completely correct for population stratification and replication in within-family studies and populations of different ancestry will provide greater confidence. To facilitate the evaluation of any residual population stratification in summary statistics, we recommend that studies report the following: (i) Summary statistics for all methods of correction attempted (e.g. PCA or LMMs where the GRM is constructed from variants in different frequency bins); (ii) Summary statistics for association with any available demographic variables such as birthplace (e.g. Haworth et al., 2019); (iii) Summaries of the distribution of polygenic scores (for a subset of the data not used in the original GWAS) with respect to geography, ancestry, and principal components (e.g. Kerminen et al., 2019). These summaries will be helpful for downstream evaluation of the robustness of polygenic predictions.

## Materials and methods

### Simulations of population structure

We used msprime (Kelleher et al., 2016) to simulate genotypes in a 6×6 grid of demes and modeled the demographic history in three different ways: (i) where the structure extends infinitely far back in time (‘perpetual’), (ii) where all demes collapse into a single population 100 generations in the past (‘recent’), and (iii) a more complex model that is loosely based on the demographic history of Europe (Lazaridis, 2018; Figure 5; ‘complex’). We fixed the effective population size of all demes and the merged ancestral population sizes to 10,000 diploid individuals.

For the perpetual and recent models, we parameterized the degree of structure in the data with a fixed, symmetric migration rate among demes (m) chosen to match the degree of structure observed in Britain. To select an appropriate value for m, we simulated a 10 Mb genome (10 chromosomes of 1 Mb each) with mutation and recombination rates of 1× 10−8 per-base per-generation, for 9,000 individuals (250 per-deme) for a range of migration rates under each demographic model (Table 1). We estimated mean $F_{S⁢T}$ across all demes with the Weir and Cockerham estimator (Weir and Cockerham, 1984) using an LD-pruned (PLINK –indep-pairwise 100 10 0.1; Purcell et al., 2007; Chang et al., 2015) set of common variants (MAF > 0.05). We used the ratio of averages approach (Bhatia et al., 2013) to calculate $F_{S⁢T}$ and estimated genomic inflation on birthplace ($\lambda_{l⁢o⁢c⁢a⁢t⁢i⁢o⁢n}$) by carrying out GWAS on an individual’s x and y coordinates in the grid, similar to the GWAS on longitude and latitude in Haworth et al., 2019. The migration rate was chosen for each model separately to roughly match the mean $F_{S⁢T}$ observed among regions in Britain (≈ 0.0007) (Leslie et al., 2015) and $\lambda_{l⁢o⁢c⁢a⁢t⁢i⁢o⁢n}≈12$ reported for the UKB (Haworth et al., 2019). Because genomic inflation scales linearly with sample size (Bulik-Sullivan et al., 2015b), we matched the expected value given our sample size of 9K using:

$$
\lambda_{l⁢o⁢c⁢a⁢t⁢i⁢o⁢n}^{9⁢k}=\frac{9}{300}⁢(\lambda_{l⁢o⁢c⁢a⁢t⁢i⁢o⁢n}^{300⁢k}-1)+1
$$

Where $\lambda_{l⁢o⁢c⁢a⁢t⁢i⁢o⁢n}^{300⁢k}$ is the observed value ($≈12$) given a sample size of 300,000 as in Haworth et al., 2019. Plugging this in, we get an expected value of $\lambda_{l⁢o⁢c⁢a⁢t⁢i⁢o⁢n}^{9⁢k}≈$ 1.36. To match this approximately, we set the migration rate to a fixed value of 0.05 and 0.07 for the ‘recent’ and ‘perpetual’ models, respectively (Table 1).

We parameterized the ‘complex’ model with two migration rates, m1 and m2, where m1 represents the migration rate between the source populations mixing 100 generations before present (2.5kya) and m2 represents the migration rate between adjacent demes in the grid (Figure 5). We selected m1 and m2 in a step-wise manner, first setting m1 = 0.004 (representing the $F_{S⁢T}$ between the two source populations) to match the maximum $F_{S⁢T}$ between regions in Britain. We then set m2 = 0.08 (representing subsequent mixing and isolation by distance) to match the mean $F_{S⁢T}$ between regions in Britain (Leslie et al., 2015; Table 1). In all cases, after selecting the appropriate migration parameters, we re-simulated genotypes under each model for a larger genome of 200 Mb (20 chromosomes of 10 Mb each), which we used for all further analysis.

### Geographic structure in England and Wales

We downloaded the Nomenclature of Territorial Units for Statistics level 2 (NUTS2) map for 35 regions in England and Wales (version 2015) from data.gov.uk and assigned each individual of ‘White British’ ancestry in the UKB to a region based on their birthplace. We calculated the proportion of individuals sampled from each region and used these as weights in our simulations to mimic the sampling distribution in the UKB. To generate a migration matrix between regions, we generated an adjacency matrix for the NUTS2 districts using the ‘simple features’ (sf) R package (Pebesma, 2018), where an entry is one if two districts abut and zero otherwise, and multiplied this matrix by the migration parameter $m_{2}$.

### Simulation of phenotypes

To study the effect of stratification on test statistic inflation, we simulated non-heritable phenotypes $y_{i⁢j}$ of an individual $i$ from deme $j$ as $y_{i⁢j}∼N⁢(\mu_{j},\sigma)$, where $\mu_{j}$ is the mean environmental effect in deme $j$. For the smooth effect, we chose $\mu_{j}$ such that the difference between the northern and southernmost demes was 2σ. For the sharp effect, we set $\mu_{j}=2⁢\sigma$ for one affected deme and zero otherwise. To test the impact of population structure on effect size estimation and polygenic score prediction, we simulated heritable phenotypes using the model described in Schoech et al., 2019. We selected 2,000 variants across the 200 Mb genome (one variant chosen uniformly at random in each 100 kb window) and sampled their effect sizes as $\beta_{k}∼N⁢(0,\sigma_{l}^{2}⁢[p_{k}⁢(1-p_{k})]^{\alpha})$ where $\sigma_{l}^{2}$ is the frequency-independent component of genetic variance, $p_{k}$ is the allele frequency of the $k^{t⁢h}$ variant, and $\alpha$ is a scaling factor. We set $\alpha=-0.4$ based on an estimate for height (Schoech et al., 2019) and $\sigma_{l}^{2}$ such that the overall genetic variance underlying the trait, $\sigma_{g}^{2}=\sigma_{l}^{2}⁢\sum_{k=1}^{M}[2⁢p_{k}⁢(1-p_{k})]^{\alpha+1}=0.8$. We calculated the genetic value for each individual, $g_{i}=\sum_{k=1}^{M}\beta_{k}⁢x_{i⁢k}$, where $x_{i⁢k}$ is the number of derived alleles individual $i$ carries at variant $k$, and added environmental effects as described above. We generated 20 random iterations of both heritable and non-heritable phenotypes.

### GWAS

We simulated 18,000 individuals (500 from each deme) under each demographic model and split the sample into two equally sized sets, a training set on which GWAS and PCA were carried out, and a test set for polygenic score predictions. Common-PCA and rare-PCA were carried out using PLINK (Chang et al., 2015) on a set of 200,000 common (MAF > 5%) and one million rare (minor allele count = 2, 3, or 4) variants, respectively, sampled from all variants generated under each model. To carry out PCA on identity-by-descent (IBD) sharing, we called long (>10 cM) pairwise IBD segments using GERMLINE (Gusev et al., 2009) with default parameters and generated an IBD-sharing GRM, in which each entry represents the total fraction of the haploid genome (100 Mb) shared by individual pairs. We calculated eigenvectors (PCs) of the IBD-sharing GRM using GCTA (Yang et al., 2011).

We performed GWAS using –glm in PLINK 2.0 with 100 PCs as covariates (Chang et al., 2015). As indicated in the main text, we also used as a set of 50 common- and 50 rare-PCs, computed separately, as covariates in the same model to correct for structure existing on multiple time scales.

We fitted LMMs using GCTA-LOCO (Yang et al., 2011) where the GRM was based on the same common or rare variants used for PCA. GCTA’s LOCO (leave one chromosome out) algorithm fits a model where the GRM is constructed from SNPs that are not present on the same chromosome as the variant being tested to avoid proximal contamination. We also included the top 100 PCs as fixed effects in the mixed models.

We calculated genomic inflation ($\lambda_{p}$) for non-heritable phenotypes as $\frac{χ_{p}^{2}}{F_{χ^{2}}^{-1}⁢(p)}$ where $χ_{p}^{2}$ is the $p^{t⁢h}$ percentile of the observed association test statistic and $F_{χ^{2}}^{-1}⁢(p)$ is the quantile function of the $χ^{2}$ distribution with 1 degree of freedom.

### Sibling-based tests

We conducted structured matings by sampling pairs of individuals from the same deme and generated the haplotypes of each child by sampling haplotypes, with replacement, from each parent without recombination. We generated heritable phenotypes as described in the previous section for each sibling and modeled the effect of each variant as

$$
Δ⁢y_{i}=\beta_{i}⁢Δ⁢x_{i}+ϵ_{i}
$$

where $Δ⁢y$ is the difference in siblings’ phenotypic values and $Δ⁢x_{i}$ is the difference in the number of derived alleles at the $i^{t⁢h}$ variant.

### Polygenic scores

We calculated polygenic scores for each individual as $\sum_{i}\beta_{i}^⁢x_{i}$ where $\beta_{i}^$ is the estimated effect size and $x_{i}$ is the number of derived alleles for the $i^{t⁢h}$ variant (either causal or lead SNP). To study patterns of residual stratification, we subtracted individuals’ true (simulated) genetic values ($g_{i}=\sum_{i}\beta_{i}⁢x_{i}$), which themselves can be structured, from polygenic scores. We averaged residual polygenic scores across 20 random iterations of causal variant selection, effect size generation, and GWAS to minimize stochastic variation. Predictive accuracy of polygenic scores was measured as the proportion of variance in individuals’ genetic values that can be explained by their polygenic score.

### Gene burden

We simulated genes, each with eight exons of length 160 bp separated by introns of length 6,938 bp, representing an average gene in the human genome (Piovesan et al., 2019). We simulated 100,000 genes for the ‘recent’ model with and without recombination and for the ‘perpetual’ model with no recombination. For the ‘perpetual’ model with recombination, we simulated 50,000 genes. We calculated gene burden as the total count of derived alleles (frequency < 0.001) across all exons in the gene for each individual. Even though introns do not directly contribute to gene burden, they serve as spacers to allow for recombination between exons. In genes without recombination, introns only add to the computational cost and, therefore, we did not simulate them. To ensure that differences in structure in gene burden between models was driven by differences in demographic history and not differences in the number of rare variants, we first calculated the mean (16) and standard deviation (4) of the number of rare variants under the ‘recent’ model and sampled from this distribution when simulating under the ‘perpetual’ model. The geographic clustering of burden was measured using Gini curves and the Gini coefficient.

$$
G=\frac{n-y_{1}-\sum1<i\leqn(y_{i}+y_{i-1})}{n}
$$

where $y_{i}$ is the cumulative gene burden in the $i^{t⁢h}$ deme sorted in increasing order of gene-burden and $n$ is the number of demes. The Gini coefficient ranges from zero, indicating that the burden is uniformly distributed in space, to one, indicating that the burden is concentrated in a single deme (Figure 3—figure supplement 1).

### Imputation and fine-mapping

We performed imputation using Beagle 5.1 (Browning et al., 2018). We imputed the genotypes of rare variants (MAF < 0.001) in a sample of 9,000 individuals using the phased sequences of an independent 9,000 individuals as reference. Both reference and test sets were simulated under the recent structure model.

We fine-mapped variants using SuSiE (Wang et al., 2020a) separately on 100 Kb windows, each of which carried a single causal variant. We restricted fine-mapping to windows where at least one variant had a p-value $<1\times$ 10−4 and picked the variant with the highest posterior inclusion probability to construct polygenic scores.

### Code availability

We carried out all analyses with code written in Python 3.5, R 3.5.1, and shell scripts, which are all available at https://github.com/Arslan-Zaidi/popstructure; Zaidi, 2020; copy archived at swh:1:rev:1509a53ee491e3e01320c174ff55f9426da8923f.
