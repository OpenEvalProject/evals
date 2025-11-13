# Discovering non-additive heritability using additive GWAS summary statistics

## Authors

- Samuel Pattillo Smith<sup>1</sup> ([ORCID: 0000-0002-6269-0276](https://orcid.org/0000-0002-6269-0276))
- Gregory Darnell<sup>1</sup> ([ORCID: 0000-0003-0425-940X](https://orcid.org/0000-0003-0425-940X))
- Dana Udwin<sup>6</sup>
- Julian Stamp<sup>1</sup>
- Arbel Harpak<sup>3</sup> ([ORCID: 0000-0002-3655-748X](https://orcid.org/0000-0002-3655-748X))
- Sohini Ramachandran<sup>1</sup>
- Lorin Crawford<sup>1</sup> ([ORCID: 0000-0003-0178-8242](https://orcid.org/0000-0003-0178-8242)) †

### Affiliations

1. Center for Computational Molecular Biology, Brown University Providence United States ([ROR:05gq02987](https://ror.org/05gq02987))
2. Department of Ecology and Evolutionary Biology, Brown University Providence United States ([ROR:05gq02987](https://ror.org/05gq02987))
3. Department of Integrative Biology, The University of Texas at Austin Austin United States ([ROR:00hj54h04](https://ror.org/00hj54h04))
4. Department of Population Health, The University of Texas at Austin Austin United States ([ROR:00hj54h04](https://ror.org/00hj54h04))
5. Institute for Computational and Experimental Research in Mathematics, Brown University Providence United States ([ROR:05gq02987](https://ror.org/05gq02987))
6. Department of Biostatistics, Brown University Providence United States ([ROR:05gq02987](https://ror.org/05gq02987))
7. Data Science Institute, Brown University Providence United States ([ROR:05gq02987](https://ror.org/05gq02987))
8. Microsoft Cambridge United States ([ROR:00d0nc645](https://ror.org/00d0nc645))

† Corresponding author

## Abstract

LD score regression (LDSC) is a method to estimate narrow-sense heritability from genome-wide association study (GWAS) summary statistics alone, making it a fast and popular approach. In this work, we present interaction-LD score (i-LDSC) regression: an extension of the original LDSC framework that accounts for interactions between genetic variants. By studying a wide range of generative models in simulations, and by re-analyzing 25 well-studied quantitative phenotypes from 349,468 individuals in the UK Biobank and up to 159,095 individuals in BioBank Japan, we show that the inclusion of a cis-interaction score (i.e. interactions between a focal variant and proximal variants) recovers genetic variance that is not captured by LDSC. For each of the 25 traits analyzed in the UK Biobank and BioBank Japan, i-LDSC detects additional variation contributed by genetic interactions. The i-LDSC software and its application to these biobanks represent a step towards resolving further genetic contributions of sources of non-additive genetic effects to complex trait variation.

## Introduction

Heritability is defined as the proportion of phenotypic trait variation that can be explained by genetic effects (Bulik-Sullivan et al., 2015b, Bulik-Sullivan et al., 2015a, Shi et al., 2016). Until recently, studies of heritability in humans have been reliant on typically small sized family studies with known relatedness structures among individuals (Zaitlen et al., 2013; Polderman et al., 2015). Due to advances in genomic sequencing and the steady development of statistical tools, it is now possible to obtain reliable heritability estimates from biobank-scale data sets of unrelated individuals (Bulik-Sullivan et al., 2015b; Shi et al., 2016; Hou et al., 2019; Pazokitoroudi et al., 2020). Computational and privacy considerations with genome-wide association studies (GWAS) in these larger cohorts have motivated a recent trend to estimate heritability using summary statistics (i.e. estimated effect sizes and their corresponding standard errors). In the GWAS framework, additive effect sizes and standard errors for individual single nucleotide polymorphisms (SNPs) are estimated by regressing phenotype measurements onto the allele counts of each SNP independently. Through the application of this approach over the last two decades, it has become clear that many traits have a complex and polygenic basis—that is, hundreds to thousands of individual genetic loci across the genome often contribute to the genetic basis of variation in a single trait (Yengo et al., 2018).

Many statistical methods have been developed to improve the estimation of heritability from GWAS summary statistics (Bulik-Sullivan et al., 2015b, Shi et al., 2016, Speed and Balding, 2019, Song et al., 2022). The most widely used of these approaches is linkage disequilibrium (LD) score regression and the corresponding LDSC software (Bulik-Sullivan et al., 2015b), which corrects for inflation in GWAS summary statistics by modeling the relationship between the variance of SNP-level effect sizes and the sum of correlation coefficients between focal SNPs and their genomic neighbors (i.e. the LD score of each variant). The formulation of the LDSC framework relies on the fact that the expected relationship between chi-square test statistics (i.e. the squared magnitude of GWAS allelic effect estimates) and LD scores holds when complex traits are generated under the infinitesimal (or polygenic) model which assumes: (i) all causal variants have the same expected contribution to phenotypic variation and (ii) causal variants are uniformly distributed along the genome. Initial simulations in Bulik-Sullivan et al. showed that violations of these assumptions can be tolerated to a point, but begin to affect the estimation of narrow-sense heritability once a certain proportion of variants have nonzero effects. Importantly, the estimand of the LDSC model is the proportion of phenotypic variance attributable to additive effects of genotyped SNPs. The main motivation behind the LDSC model is that, for polygenic traits, many marker SNPs tag nonzero effects. This may simply arise because some of these SNPS are in LD with causal variants (Bulik-Sullivan et al., 2015b) or because their statistical association is the product of a confounding factor such as population stratification.

As of late, there have been many efforts to build upon and improve the LDSC framework. For example, recent work has shown that it is possible to estimate the proportion of phenotypic variation explained by dominance effects (Palmer et al., 2023) and local ancestry (Chan et al., 2023) using extensions of the LDSC model. One limitation of LDSC is that, in practice, it only uses the diagonal elements of the squared LD matrix in its formulation which, while computationally efficient, does not account for information about trait architecture that is captured by the off-diagonal elements. This tradeoff helps LDSC to scale genome-wide, but it has also been shown to lead to heritability estimates with large standard error (Ning et al., 2020, Zhang et al., 2021, Song et al., 2022). Recently, newer approaches have attempted to reformulate the LDSC model by using the eigenvalues of the LD matrix to leverage more of the information present in the correlation structure between SNPs (Shi et al., 2016, Song et al., 2022).

In this paper, we show that the LDSC framework can be extended to estimate greater proportions of genetic variance in complex traits (i.e. beyond the variance that is attributable to additive effects) when a subset of causal variants is involved in a gene-by-gene (G×G) interaction. Indeed, recent association mapping studies have shown that G×G interactions can drive heterogeneity of causal variant effect sizes (Patel et al., 2022). Importantly, non-additive genetic effects have been proposed as one of the main factors that explains ‘missing’ heritability—the proportion of heritability not explained by the additive effects of variants (Eichler et al., 2010).

The key insight we highlight in this manuscript is that SNP-level GWAS summary statistics can provide evidence of non-additive genetic effects contributing to trait architecture if there is a nonzero correlation between individual-level genotypes and their statistical interactions. We present the ‘interaction-LD score’ regression model or i-LDSC: an extension of the LDSC framework which recovers ‘missing’ heritability by leveraging this ‘tagged’ relationship between linear and nonlinear genetic effects. To validate the performance of i-LDSC in simulation studies, we focus on synthetic trait architectures that have been generated with contributions stemming from second-order and cis-acting statistical SNP-by-SNP interaction effects; however, note that the general concept underlying i-LDSC can easily be extended to other sources of non-additive genetic effects (e.g. gene-by-environment interactions). The main difference between i-LDSC and LDSC is that the i-LDSC model includes an additional set of ‘cis-interaction’ LD scores in its regression model. These scores measure the amount of phenoytpic variation contributed by genetic interactions that can be explained by additive effects. In practice, these additional scores are efficient to compute and require nothing more than access to a representative pairwise LD map, same as the input required for LD score regression.

Through extensive simulations, we show that i-LDSC recovers substantial non-additive heritability that is not captured by LDSC when genetic interactions are indeed present in the generative model for a given complex trait. More importantly, i-LDSC has a calibrated type I error rate and does not overestimate contributions of genetic interactions to trait variation in simulated data when only additive effects are present. While analyzing 25 complex traits in the UK Biobank and BioBank Japan, we illustrate that pairwise interactions are a source of ‘missing’ heritability captured by additive GWAS summary statistics—suggesting that phenotypic variation due to non-additive genetic effects is more pervasive in human phenotypes than previously reported. Specifically, we find evidence of tagged genetic interaction effects contributing to heritability estimates in all of the 25 traits in the UK Biobank, and 23 of the 25 traits we analyzed in the BioBank Japan. We believe that i-LDSC, with our development of a new cis-interaction score, represents a significant step towards resolving the true contribution of genetic interactions.

## Results

### Overview of the interaction-LD score regression model

Interaction-LD score regression (i-LDSC) is a statistical framework for estimating heritability (i.e. the proportion of trait variance attributable to genetic variance). Here, we will give an overview of the i-LDSC method and its corresponding software, as well as detail how its underlying model differs from that of LDSC (Bulik-Sullivan et al., 2015b). We will assume that we are analyzing a GWAS dats set $𝒟={𝐗,𝐲}$ where $𝐗$ is an $N\timesJ$ matrix of genotypes with $J$ denoting the number of SNPs (each of which is encoded as {0, 1, 2} copies of a reference allele at each locus $j$) and $𝐲$ is an $N$-dimensional vector of measurements of a quantitative trait. The i-LDSC framework only requires summary statistics of individual-level data: namely, marginal effect size estimates for each SNP $𝜷^$ and a sample LD matrix $𝐑$ (which can be provided via reference panel data).

We begin by considering the following generative linear model for complex traits

$$
y=b_{0}+X\beta+W\theta+\epsilon,\epsilon∼N(0,(1−H^{2})I),
$$

where $b_{0}$ is an intercept term; $𝜷=(\beta_{1},…,\beta_{J})$ is a $J$-dimensional vector containing the true additive effect sizes for an additional copy of the reference allele at each locus on $y$; $W$ is an $N\timesM$ matrix of (pairwise) cis-acting SNP-by-SNP statistical interactions between some subset of causal SNPs, where columns of this matrix are assumed to be the Hadamard (element-wise) product between genotypic vectors of the form $𝐱_{j}∘𝐱_{k}$ for the $j$-th and $k$-th variants; $𝜽=(\theta_{1},…,\theta_{M})$ is an $M$-dimensional vector containing the interaction effect sizes; $𝜺$ is a normally distributed error term with mean zero and variance scaled according to the proportion of phenotypic variation not explained by genetic effects (Bulik-Sullivan et al., 2015b), which we will refer to as the broad-sense heritability of the trait denoted by $H^{2}$; and $𝐈$ denotes an $N\timesN$ identity matrix. For convenience, we will assume that the genotype matrix (column-wise) and the trait of interest have been mean-centered and standardized (Strandén and Christensen, 2011; de Los Campos et al., 2013; Zhou et al., 2013). Lastly, we will let the intercept term b0 be a fixed parameter and we will assume that the effect sizes are each normally distributed with variances proportional to their individual contributions to trait heritability (Yang et al., 2010; Wu et al., 2011; Zhou et al., 2013; Crawford et al., 2017)

$$
\beta_{j}∼N(0,\phi_{\beta}^{2}/J),\theta_{m}∼N(0,\phi_{\theta}^{2}/M).
$$

Effectively, we say that $𝕍⁢[𝐗⁢𝜷]=\phi_{\beta}^{2}$ is the proportion of phenotypic variation contributed by additive SNP effects under the generative model, while $𝕍⁢[𝐖⁢𝜽]=\phi_{\theta}^{2}$ makes up the proportion of phenotypic variation contributed by genetic interactions. While the appropriateness of treating genetic effects as random variables in analytical derivations has been questioned (de Los Campos et al., 2015), later, we will justify the theory presented here with simulation results showing that i-LDSC accurately recovers non-additive genetic variance in Equation 1 under a broad range of conditions.

There are two key takeaways from the generative model specified above. First, Equation 2 implies that the additive and non-additive components in Equation 1 are orthogonal to each other. In other words, $𝔼⁢[𝜷^{⊺}⁢𝐗^{⊺}⁢𝐖⁢𝜽]=𝔼⁢[𝜷^{⊺}]⁢𝐗^{⊺}⁢𝐖⁢𝔼⁢[𝜽]=𝟎$. This is important because it means that there is a unique partitioning of genetic variance when studying a trait of interest. The second key takeaway is that the genotype matrix $𝐗$ and the matrix of genetic interactions $𝐖$ themselves are correlated despite being linearly independent (see Materials and methods). This property stems from the fact that the pairwise interaction between two SNPs is encoded as the Hadamard product of two genotypic vectors in the form $𝐰_{m}=𝐱_{j}∘𝐱_{k}$ (which is a nonlinear function of the genotypes).

A central objective in GWAS studies is to infer how much phenotypic variation can be explained by genetic effects. To achieve that objective, a key consideration involves incorporating the possibility of non-additive sources of genetic variation to be explained by additive effect size estimates obtained from GWAS analyses (Hill et al., 2008). If we assume that the genotype and interaction matrices are correlated, then $X$ and $𝐖$ are not completely orthogonal (i.e. such that $X^{⊺}W\neq0$) and the following relationship between the moment matrix $X^{⊺}y$, the observed marginal GWAS summary statistics $\beta^$, and the true coefficient values $\beta$ from the generative model in Equation 1 holds in expectation (see Materials and methods)

$$
E[X^{⊺}y]=(X^{⊺}X)\beta+(X^{⊺}W)\theta⟺≈E[\beta^]=R\beta+V\theta
$$

where $𝐑$ is a sample estimate of the LD matrix, and $𝐕$ represents a sample estimate of the correlation between the individual-level genotypes $𝐗$ and the span of genetic interactions between causal SNPs in $𝐖$. Intuitively, the term $V\theta$ can be interpreted as the subset of pairwise interaction effects that are tagged by the additive effect estimates from the GWAS study. Note that, when (i) non-additive genetic effects do not contribute to the overall architecture of a trait (i.e. such that $\theta=0$) or (ii) the genotype and interaction matrices $𝐗$ and $𝐖$ are uncorrelated, the equation above simplifies to a relationship between LD and summary statistics that is assumed in many GWAS studies and methods (Hormozdiari et al., 2014; Nakka et al., 2016; Zhu and Stephens, 2017; Zhang et al., 2018; Zhu and Stephens, 2018; Cheng et al., 2020; Demetci et al., 2021).

The goal of i-LDSC is to increase estimates of genetic variance by accounting for sources of non-additive genetic effects that can be explained by additive GWAS summary statistics. To do this, we extend the LD score regression framework and the corresponding LDSC software (Bulik-Sullivan et al., 2015b). Here, according to Equation 3, we note that $\beta^∼N(R\beta+V\theta,\lambdaR)$ where $\lambda$ is a scale variance term due to uncontrolled confounding effects (Guan and Stephens, 2011; Song et al., 2022). Next, we condition on $Θ=(\beta,\theta)$ and take the expectation of chi-square statistics $χ^{2}=N\beta^\beta^^{⊺}$ to yield

$$
E[\beta^\beta^^{⊺}]=E[E[\beta^\beta^^{⊺}|Θ]]=E[V[\beta^|Θ]+E[\beta^|Θ]E[\beta^|Θ]^{⊺}]=E[\lambdaR+(R\beta+V\theta)(R\beta+V\theta)^{⊺}]=E[\lambdaR+R\beta\beta^{⊺}R+2R\beta\theta^{⊺}V^{⊺}+V\theta\theta^{⊺}V^{⊺}]=\lambdaR+(\frac{\phi_{\beta}^{2}}{J})R^{2}+(\frac{\phi_{\theta}^{2}}{M})V^{2}.
$$

We define $ℓ_{j}=\sumkr_{jk}^{2}$ as the LD score for the additive effect of the $j$-th variant (Bulik-Sullivan et al., 2015b), and $f_{j}=\summv_{jm}^{2}$ represents the ‘cis-interaction’ LD score which encodes the pairwise interaction between the $j$-th variant and all other variants within a genomic window that is a pre-specified number of SNPs wide (Crawford et al., 2017), respectively. By considering only the diagonal elements of LD matrix in the first term, similar to the original LDSC approach (Bulik-Sullivan et al., 2015b; Song et al., 2022), we get the following simplified regression model

$$
E[χ^{2}]∝1+ℓ\tau+fϑ
$$

where $χ^{2}=(χ_{1}^{2},…,χ_{J}^{2})$ is a $J$-dimensional vector of chi-square summary statistics, and $ℓ=(ℓ_{1},…,ℓ_{J})$ and $f=(f_{1},…,f_{J})$ are $J$-dimensional vectors of additive and cis-interaction LD scores, respectively. Furthermore, we define the variance components $\tau=N\phi_{\beta}^{2}/J$ and $ϑ=N\phi_{\theta}^{2}/M$ as the additive and non-additive regression coefficients of the model, and 1 is the intercept meant to model the bias factor due to uncontrolled confounding effects (e.g. cryptic relatedness structure). In practice, we efficiently compute the cis-interaction LD scores by considering only a subset of interactions between each $j$-th focal SNP and SNPs within a cis-proximal window around the $j$-th SNP. In our validation studies and applications, we base the width of this window on the observation that LD decays outside of a window of 1 centimorgan (cM); therefore, SNPs outside the 1 cM window centered on the $j$-th SNP will not significantly contribute to its LD scores. Note that the width of this window can be relaxed in the i-LDSC software when appropriate. We fit the i-LDSC model using weighted least squares to estimate regression parameters and derive p-values for identifying traits that have significant statistical evidence of tagged cis-interaction effects by testing the null hypothesis $H_{0}:ϑ=0$. Importantly, under the null model of a trait being generated by only additive effects, the i-LDSC model in Equation 5 reduces to an infinitesimal model (Fisher, 1999) or, in the case some variants have no effect on the trait, a polygenic model.

Lastly, we want to note the empirical observation that the additive ($ℓ$) and interaction $(𝒇$) LD scores are lowly correlated. This is important because it indicates that the presence of cis-interaction LD scores in the model specified in Equation 5 has little-to-no influence over the estimate for the additive coefficient $\tau$. Instead, the inclusion of $𝒇$ creates a multivariate model that can identify the proportion of variance explained by both additive and non-additive effects in summary statistics. In other words, we can interpret $ϑ^$ as an estimate of the phenotypic variation explained by tagged cis-acting interaction effects. The concept of additive genetic effects partially explaining non-additive variation has also described in various studies from quantitative genetics (Hill et al., 2008; Hivert et al., 2021; Mäki-Tanila and Hill, 2014). Under Hardy-Weinberg equilibrium, it can be shown that the additive variance explained by $J$ SNPs takes on the following form (Materials and methods) (Falconer and Mackay, 1983)

$$
\sigma_{A}^{2}=\sumj=1J2p_{j}(1−p_{j})[\beta_{j}+2\sumk\neqjJp_{k}\theta_{jk}]^{2}.
$$

The expression for the additive variance $\sigma_{A}^{2}$ in Equation 6 is important because it represents the theoretical upper bound on the proportion of total phenotypic variance that can be recovered from GWAS summary statistics using the i-LDSC framework. As a result, we use the sum of coefficient estimates $\tau^+ϑ^\leq\sigma_{A}^{2}$ to construct i-LDSC heritability estimates. A full derivation of the cis-interaction regression framework and details about its corresponding implementation in our software i-LDSC can be found in Materials and Methods.

### Detection of tagged pairwise interaction effects using i-LDSC in simulations

We illustrate the power of i-LDSC across different genetic trait architectures via extensive simulation studies (Materials and methods). We generate synthetic phenotypes using real genome-wide genotype data from individuals of self-identified European ancestry in the UK Biobank. To do so, we first assume that traits have a polygenic architecture where all SNPs have a nonzero additive effect. Next, we randomly select a set of causal cis-interaction variants and divide them into two interacting groups (Materials and methods). One may interpret the SNPs in group #1 as being the ‘hubs’ in an interaction map (Crawford et al., 2017), whereas SNPs in group #2 are selected to be variants within some kilobase (kb) window around each SNP in group #1. We assume a wide range of simulation scenarios by varying the following parameters:

We also varied the correlation between SNP effect size and minor allele frequency (MAF; as discussed in Schoech et al., 2019). All results presented in this section are based on 100 different simulated phenotypes for each parameter combination.

Figure 1 demonstrates that i-LDSC robustly detects significant tagged non-additive genetic variance, regardless of the total number of causal interactions genome-wide. Instead, the power of i-LDSC depends on the proportion of phenotypic variation that is generated by additive versus interaction effects (ρ), and its power tends to scale with the window size used to compute the cis-interaction LD scores (see Materials and methods). i-LDSC shows a similar performance for detecting tagged cis-interaction effects when the effect sizes of causal SNPs depend on their minor allele frequency and when we varied the number of SNPs assigned to be in group #2 within 10 kb and 100 kb windows, respectively (Figure 1—figure supplements 1–5).

![Figure 1.](https://cdn.elifesciences.org/articles/90459/elife-90459-fig1-v1.jpg)

**Figure 1.:** Synthetic trait architecture was simulated using real genotype data from individuals of self-identified European ancestry in the UK Biobank. All SNPs were considered to have at least an additive effect (i.e. creating a polygenic trait architecture). Next, we randomly select two groups of interacting variants and divide them into two groups. The group #1 SNPs are chosen to be 1%, 5%, and 10% of the total number of SNPs genome-wide (see the x-axis in each panel). These interact with the group #2 SNPs which are selected to be variants within a ± 10 kilobase (kb) window around each SNP in group #1. Coefficients for additive and interaction effects were simulated with no minor allele frequency dependency $\alpha=0$ (see Materials and methods). Panels (A) and (B) are results with simulations using a heritability $H^{2}=0.3$, while panels (C) and (D) were generated with $H^{2}=0.6$. We also varied the proportion of heritability contributed by additive effects to (A, C) $ρ=0.5$ and (B, D) $ρ=0.8$, respectively. Here, we are blind to the parameter settings used in generative model and run i-LDSC while computing the cis-interaction LD scores using different estimating windows of ± 5 (green), ± 10 (orange), ± 25 (purple), and ± 50 (pink) SNPs. Results are based on 100 simulations per parameter combination and the horizontal bars represent standard errors. Generally, the performance of i-LDSC increases with larger heritability and lower proportions of additive variation. Note that LDSC is not shown here because it does not search for tagged interaction effects in summary statistics.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/90459/elife-90459-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** Power calculations for the i-LDSC framework to detect tagged pairwise genetic interaction effects on simulated data using a ± 10 kilobase (kb) window to generate cis-interactions around a focal SNP with a moderate minor allele frequency dependency $\alpha=-0.5$ for effect sizes.Synthetic trait architecture was simulated using real genotype data from individuals of self-identified European ancestry in the UK Biobank. All SNPs were considered to have at least an additive effect (i.e. creating a polygenic trait architecture). Next, we randomly select two groups of interacting variants and divide them into two groups. The group #1 SNPs are chosen to be 1%, 5%, and 10% of the total number of SNPs genome-wide (see the x-axis in each panel). These interact with the group #2 SNPs which are selected to be variants within a ± 10 kilobase (kb) window around each SNP in group #1. Coefficients for additive and interaction effects were simulated with minor allele frequency dependency $\alpha=-0.5$ (see Materials and methods). Panels (A) and (B) are results of simulations where the total heritability explained by additive SNP effects and cis-interaction effects is $H^{2}=0.3$, while panels (C) and (D) were generated with $H^{2}=0.6$. We also varied the proportion of phenotypic variation explained by additive SNP effects to (A, C) $ρ=0.5$ and (B, D) $ρ=0.8$, respectively. Here, we are blind to the parameter settings used in generative model and run i-LDSC while computing the cis-interaction LD scores using different estimation windows of ± 5 (green), ± 10 (orange), ± 25 (purple), and ± 50 (pink) SNPs. Results are based on 100 simulations per parameter combination and the horizontal black bars represent standard errors.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/90459/elife-90459-fig1-figsupp2-v1.jpg)

**Figure 1—figure supplement 2.:** Power calculations for the i-LDSC framework to detect tagged pairwise genetic interaction effects on simulated data using a ± 10 kilobase (kb) window to generate cis-interactions around a focal SNP with a strong minor allele frequency dependency $\alpha=-𝟏$ for effect sizes.Synthetic trait architecture was simulated using real genotype data from individuals of self-identified European ancestry in the UK Biobank. All SNPs were considered to have at least an additive effect (i.e. creating a polygenic trait architecture). Next, we randomly select two groups of interacting variants and divide them into two groups. The group #1 SNPs are chosen to be 1%, 5%, and 10% of the total number of SNPs genome-wide (see the x-axis in each panel). These interact with the group #2 SNPs which are selected to be variants within a ± 10 kilobase (kb) window around each SNP in group #1. Coefficients for additive and interaction effects were simulated with minor allele frequency dependency $\alpha=-0.5$ (see Materials and methods). Panels (A) and (B) are results of simulations where the total heritability explained by additive SNP effects and cis-interaction effects is $H^{2}=0.3$, while panels (C) and (D) were generated with $H^{2}=0.6$. We also varied the proportion of phenotypic variation explained by additive SNP effects to (A, C) $ρ=0.5$ and (B, D) $ρ=0.8$, respectively. Here, we are blind to the parameter settings used in generative model and run i-LDSC while computing the cis-interaction LD scores using different estimation windows of ± 5 (green), ± 10 (orange), ± 25 (purple), and ± 50 (pink) SNPs. Results are based on 100 simulations per parameter combination and the horizontal black bars represent standard errors.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/90459/elife-90459-fig1-figsupp3-v1.jpg)

**Figure 1—figure supplement 3.:** Power calculations for the i-LDSC framework to detect tagged pairwise genetic interaction effects on simulated data using a ± 10 kilobase (kb) window to generate cis-interactions around a focal SNP with no minor allele frequency dependency $\alpha=𝟎$ for effect sizes.Synthetic trait architecture was simulated using real genotype data from individuals of self-identified European ancestry in the UK Biobank. All SNPs were considered to have at least an additive effect (i.e. creating a polygenic trait architecture). Next, we randomly select two groups of interacting variants and divide them into two groups. The group #1 SNPs are chosen to be 1%, 5%, and 10% of the total number of SNPs genome-wide (see the x-axis in each panel). These interact with the group #2 SNPs which are selected to be variants within a ± 10 kilobase (kb) window around each SNP in group #1. Coefficients for additive and interaction effects were simulated with minor allele frequency dependency $\alpha=-0.5$ (see Materials and methods). Panels (A) and (B) are results of simulations where the total heritability explained by additive SNP effects and cis-interaction effects is $H^{2}=0.3$, while panels (C) and (D) were generated with $H^{2}=0.6$. We also varied the proportion of phenotypic variation explained by additive SNP effects to (A, C) $ρ=0.5$ and (B, D) $ρ=0.8$, respectively. Here, we are blind to the parameter settings used in generative model and run i-LDSC while computing the cis-interaction LD scores using different estimation windows of ± 5 (green), ± 10 (orange), ± 25 (purple), and ± 50 (pink) SNPs. Results are based on 100 simulations per parameter combination and the horizontal black bars represent standard errors.

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/90459/elife-90459-fig1-figsupp4-v1.jpg)

**Figure 1—figure supplement 4.:** Power calculations for the i-LDSC framework to detect tagged pairwise genetic interaction effects on simulated data using a ± 100 kilobase (kb) window to generate cis-interactions around a focal SNP with a moderate minor allele frequency dependency $\alpha=-0.5$ for effect sizes.Synthetic trait architecture was simulated using real genotype data from individuals of self-identified European ancestry in the UK Biobank. All SNPs were considered to have at least an additive effect (i.e. creating a polygenic trait architecture). Next, we randomly select two groups of interacting variants and divide them into two groups. The group #1 SNPs are chosen to be 1%, 5%, and 10% of the total number of SNPs genome-wide (see the x-axis in each panel). These interact with the group #2 SNPs which are selected to be variants within a ± 10 kilobase (kb) window around each SNP in group #1. Coefficients for additive and interaction effects were simulated with minor allele frequency dependency $\alpha=-0.5$ (see Materials and methods). Panels (A) and (B) are results of simulations where the total heritability explained by additive SNP effects and cis-interaction effects is $H^{2}=0.3$, while panels (C) and (D) were generated with $H^{2}=0.6$. We also varied the proportion of phenotypic variation explained by additive SNP effects to (A, C) $ρ=0.5$ and (B, D) $ρ=0.8$, respectively. Here, we are blind to the parameter settings used in generative model and run i-LDSC while computing the cis-interaction LD scores using different estimation windows of ± 5 (green), ± 10 (orange), ± 25 (purple), and ± 50 (pink) SNPs. Results are based on 100 simulations per parameter combination and the horizontal black bars represent standard errors.

![Figure 1—figure supplement 5.](https://cdn.elifesciences.org/articles/90459/elife-90459-fig1-figsupp5-v1.jpg)

**Figure 1—figure supplement 5.:** Power calculations for the i-LDSC framework to detect tagged pairwise genetic interaction effects on simulated data using a ± 100 kilobase (kb) window to generate cis-interactions around a focal SNP with a strong minor allele frequency dependency $\alpha=-𝟏$ for effect sizes.Synthetic trait architecture was simulated using real genotype data from individuals of self-identified European ancestry in the UK Biobank. All SNPs were considered to have at least an additive effect (i.e. creating a polygenic trait architecture). Next, we randomly select two groups of interacting variants and divide them into two groups. The group #1 SNPs are chosen to be 1%, 5%, and 10% of the total number of SNPs genome-wide (see the x-axis in each panel). These interact with the group #2 SNPs which are selected to be variants within a ± 10 kilobase (kb) window around each SNP in group #1. Coefficients for additive and interaction effects were simulated with minor allele frequency dependency $\alpha=-0.5$ (see Materials and methods). Panels (A) and (B) are results of simulations where the total heritability explained by additive SNP effects and cis-interaction effects is $H^{2}=0.3$, while panels (C) and (D) were generated with $H^{2}=0.6$. We also varied the proportion of phenotypic variation explained by additive SNP effects to (A, C) $ρ=0.5$ and (B, D) $ρ=0.8$, respectively. Here, we are blind to the parameter settings used in generative model and run i-LDSC while computing the cis-interaction LD scores using different estimation windows of ± 5 (green), ± 10 (orange), ± 25 (purple), and ± 50 (pink) SNPs. Results are based on 100 simulations per parameter combination and the horizontal black bars represent standard errors.

Importantly, i-LDSC does not falsely identify putative non-additive genetic effects in GWAS summary statistics when the synthetic phenotype was generated by only additive effects ($ρ=1$). Figure 2 illustrates the performance of i-LDSC under the null hypothesis $H_{0}:ϑ=0$, with the type I error rates for different estimation window sizes of the cis-interaction LD scores highlighted in panel A. Here, we also show that, when no genetic interaction effects are present, i-LDSC unbiasedly estimates the cis-interaction coefficient in the regression model to be $ϑ^=0$ (Figure 2B), robustly estimates the heritability (Figure 2C), and provides well-calibrated p-values when assessed over many traits (Figure 2D). This behavior is consistent across different MAF-dependent effect size distributions, and p-value calibration is not sensitive to misspecification of the estimation windows used to generate the cis-interaction LD scores (Figure 2—figure supplements 1–2).

![Figure 2.](https://cdn.elifesciences.org/articles/90459/elife-90459-fig2-v1.jpg)

**Figure 2.:** In these simulations, synthetic trait architecture is made up of only additive genetic variation (i.e. $ρ=1$). Coefficients for additive and interaction effects were simulated with no minor allele frequency dependency $\alpha=0$ (see Materials and methods). Here, we are blind to the parameter settings used in generative model and run i-LDSC while computing the cis-interaction LD scores using different estimating windows of ± 5 (green), ± 10 (orange), ± 25 (purple), and ± 50 (pink) SNPs. (A) Mean type I error rate using the i-LDSC framework across an array of estimation window sizes for the cis-interaction LD scores. This is determined by assessing the p-value of the cis-interaction coefficient ($ϑ$) in the i-LDSC regression model and checking whether p < 0.05. (B) Estimates of the cis-interaction coefficient ($ϑ$). Since traits were simulated with only additive effects, these estimates should be centered around zero. (C) Estimates of the proportions of phenotypic variance explained (PVE) by genetic effects (i.e. estimated heritability) where the true additive variance is set to $H^{2}⁢ρ=0.6$. (D) QQ-plot of the p-values for the cis-interaction coefficient ($ϑ$) in i-LDSC. Results are based on 100 simulations per parameter combination and the horizontal bars represent standard errors.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/90459/elife-90459-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** The i-LDSC framework is well-calibrated under the null hypothesis and does not identify evidence of tagged non-additive effects when polygenic traits are generated by only additive effects and a moderate minor allele frequency dependency $\alpha=-0.5$ for effect sizes.In these simulations, synthetic trait architecture is made up of only additive genetic variation (i.e. $ρ=1$). Coefficients for additive and interaction effects were simulated with minor allele frequency dependency $\alpha=-0.5$ (see Materials and methods). Here, we are blind to the parameter settings used in generative model and run i-LDSC while computing the cis-interaction LD scores using different estimation windows of ± 5 (green), ± 10 (orange), ± 25 (purple), and ± 50 (pink) SNPs. (A) Mean type I error rate using the i-LDSC framework across an array of estimation window sizes for the cis-interaction LD scores. This is determined by assessing the p-value of the cis-interaction coefficient ($ϑ$) in the i-LDSC regression model and checking whether p < 0.05. (B) Estimates of the cis-interaction coefficient ($ϑ$). Since traits were simulated with only additive effects, these estimates should be centered around zero. (C) Estimates of the proportions of phenotypic variance explained (PVE) by genetic effects (i.e. estimated heritability) where the true additive variance is set to $H^{2}⁢ρ=0.6$. (D) QQ-plot of the p-values for the cis-interaction coefficient ($ϑ$) in i-LDSC. Results are based on 100 simulations per parameter combination and the horizontal black bars represent standard errors.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/90459/elife-90459-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** The i-LDSC framework is well-calibrated under the null hypothesis and does not identify evidence of tagged non-additive effects when polygenic traits are generated by only additive effects and a strong minor allele frequency dependency $\alpha=-𝟏$ for effect sizes.In these simulations, synthetic trait architecture is made up of only additive genetic variation (i.e. $ρ=1$). Coefficients for additive and interaction effects were simulated with minor allele frequency dependency $\alpha=-0.5$ (see Materials and methods). Here, we are blind to the parameter settings used in generative model and run i-LDSC while computing the cis-interaction LD scores using different estimation windows of ± 5 (green), ± 10 (orange), ± 25 (purple), and ± 50 (pink) SNPs. (A) Mean type I error rate using the i-LDSC framework across an array of estimation window sizes for the cis-interaction LD scores. This is determined by assessing the p-value of the cis-interaction coefficient ($ϑ$) in the i-LDSC regression model and checking whether p < 0.05. (B) Estimates of the cis-interaction coefficient ($ϑ$). Since traits were simulated with only additive effects, these estimates should be centered around zero. (C) Estimates of the proportions of phenotypic variance explained (PVE) by genetic effects (i.e. estimated heritability) where the true additive variance is set to $H^{2}⁢ρ=0.6$. (D) QQ-plot of the p-values for the cis-interaction coefficient ($ϑ$) in i-LDSC. Results are based on 100 simulations per parameter combination and the horizontal black bars represent standard errors.

One of the innovations that i-LDSC offers over the traditional LDSC framework is increased heritability estimates after the identification of non-additive genetic effects that are tagged by GWAS summary statistics. Here, we applied both methods to the same set of simulations in order to understand how LDSC behaves for traits generated with cis-interaction effects. Figure 3 depicts boxplots of the heritability estimates for each approach and shows that, across an array of different synthetic phenotype architectures, LDSC captures less of phenotypic variance explained by all genetic effects. It is important to note that i-LDSC can yield upwardly biased heritability estimates when the cis-interaction scores are computed over genomic window sizes that are too small; however, these estimates become more accurate for larger window size choices (Figure 3—figure supplement 1). In contrast to LDSC, which aims to capture phenotypic variance attributable to the additive effects of genotyped SNPs, i-LDSC accurately partitions genetic effects into additive versus cis-interacting components, which in turn generally leads the ability of i-LDSC to capture more genetic variance. The mean absolute error between the true generative heritability and heritability estimates produced by i-LDSC and LDSC are shown in Supplementary files 1 and 2, respectively. Generally, the error in heritability estimates is higher for LDSC than it is for i-LDSC across each of the scenarios that we consider.

![Figure 3.](https://cdn.elifesciences.org/articles/90459/elife-90459-fig3-v1.jpg)

**Figure 3.:** Synthetic trait architecture was simulated using real genotype data from individuals of self-identified European ancestry in the UK Biobank (Materials and Methods). All SNPs were considered to have at least an additive effect (i.e. creating a polygenic trait architecture). Next, we randomly select two groups of interacting variants and divide them into two groups. The group #1 SNPs are chosen to be 10% of the total number of SNPs genome-wide. These interact with the group #2 SNPs which are selected to be variants within a ± 100 kilobase (kb) window around each SNP in group #1. Coefficients for additive and interaction effects were simulated with no minor allele frequency dependency $\alpha=0$ (see Materials and methods). Here, we assume a heritability (A) $H^{2}=0.3$ or (B) $H^{2}=0.6$ (marked by the black dotted lines, respectively), and we vary the proportion contributed by additive effects with $ρ={0.2,0.4,0.6,0.8}$. The grey dotted lines represent the total contribution of additive effects in the generative model for the synthetic traits ($H^{2}ρ)$. i-LDSC outperforms LDSC in recovering heritability across each scenario. Results are based on 100 simulations per parameter combination.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/90459/elife-90459-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** Synthetic trait architecture was simulated using real genotype data from individuals of self-identified European ancestry in the UK Biobank. All SNPs were considered to have at least an additive effect (i.e. creating a polygenic trait architecture). Next, we randomly select two groups of interacting variants and divide them into two groups. The group #1 SNPs are chosen to be 10% of the total number of SNPs genome-wide. These interact with the group #2 SNPs which are selected to be variants within a ± 100 kilobase (kb) window around each SNP in group #1. Coefficients for additive and cis-interaction effects were simulated with no minor allele frequency dependency $\alpha=0$ (see Materials and methods). Here, we assume a total heritability explained by additive SNP and cis-interaction effects is (A) $H^{2}=0.3$ or (B) $H^{2}=0.6$ (marked by the black dotted lines, respectively), and we vary the proportion contributed by additive effects with $ρ={0.2,0.4,0.6,0.8}$. The grey dotted line represents the total contribution of additive effects in the generative model for the synthetic traits ($H^{2}ρ)$. We run i-LDSC while computing the cis-interaction LD scores using different estimating windows of ± 5, ± 10, ± 25, and ± 50 SNPs, respectively. These results help motivate the selection of scores calculated using a ± 50 SNP window in our empirical analyses. Results are based on 100 simulations per parameter combination.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/90459/elife-90459-fig3-figsupp2-v1.jpg)

**Figure 3—figure supplement 2.:** Synthetic trait architecture was simulated using real genotype data from individuals of self-identified European ancestry in the UK Biobank. All SNPs were considered to have at least an additive effect (i.e. creating a polygenic trait architecture). Next, we randomly select two groups of interacting variants and divide them into two groups. The group #1 SNPs are chosen to be 10% of the total number of SNPs genome-wide. These interact with the group #2 SNPs which are selected to be variants within a ± 100 kilobase (kb) window around each SNP in group #1. G×E effects were simulated using an amplification model (Zhu et al., 2023 ; see Materials and methods) where we split the sample population in half to emulate two subsets of individuals coming from different environments. We randomly draw variant effect sizes for the first environment from a standard Gaussian distribution. Then effect sizes for the second environment are set to be the product of the effect sizes in from with first environment with an amplifier $w=[1.1,1.2,…,2]$ (see the x-axis in each panel). Both the cis-interaction and G×E effects were set to explain a quarter of the total phenotypic variation and the remaining half was explained by additive SNP effects. Panels (A) and (B) show estimates of the proportions of phenotypic variance explained (PVE) by genetic effects (i.e. estimated heritability) from LDSC and i-LDSC, respectively. Panels (C) and (D) show i-LDSC estimates of the phenotypic variation explained by tagged non-additive genetic effects using the cis-interaction LD score (i.e. estimates of $ϑ$). We assume the total heritability explained by all genetic effects to be (A, C) $H^{2}=0.6$ and (B, D) $H^{2}=0.3$. Results are based on 100 simulations per parameter combination.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/90459/elife-90459-fig3-figsupp3-v1.jpg)

**Figure 3—figure supplement 3.:** Synthetic trait architecture was simulated using real genotype data from individuals of self-identified European ancestry in the UK Biobank. All SNPs were considered to have at least an additive effect (i.e. creating a polygenic trait architecture). Next, we randomly select two groups of interacting variants and divide them into two groups. The group #1 SNPs are chosen to be 10% of the total number of SNPs genome-wide. These interact with the group #2 SNPs which are selected to be variants within a ± 100 kilobase (kb) window around each SNP in group #1. G×Ancestry effects were simulated as the product of individual genotypes and the SNP loadings for each of the first 10 PCs (see the x-axis in each panel). Both the cis-interaction and G×Ancestry effects were set to explain a quarter of the total phenotypic variation and the remaining half was explained by additive SNP effects. The proportion of genotypic variance explained by each PC is shown in green. Panels (A) and (B) show estimates of the proportions of phenotypic variance explained (PVE) by genetic effects (i.e. estimated heritability) from LDSC and i-LDSC, respectively. Panels (C) and (D) show i-LDSC estimates of the phenotypic variation explained by tagged non-additive genetic effects using the cis-interaction LD score (i.e. estimates of $ϑ$). We assume the total heritability explained by all genetic effects to be (A, C) $H^{2}=0.6$ and (B, D) $H^{2}=0.3$. Results are based on 100 simulations per parameter combination.

![Figure 3—figure supplement 4.](https://cdn.elifesciences.org/articles/90459/elife-90459-fig3-figsupp4-v1.jpg)

**Figure 3—figure supplement 4.:** Synthetic trait architecture was simulated using real genotype data from individuals of self-identified European ancestry in the UK Biobank. All SNPs were considered to have at least an additive effect (i.e. creating a polygenic trait architecture). Next, we randomly select two groups of interacting variants and divide them into two groups. The group #1 SNPs are chosen to be 10% of the total number of SNPs genome-wide. These interact with the group #2 SNPs which are selected to be variants within a ± 100 kilobase (kb) window around each SNP in group #1. G×Ancestry effects were simulated as the product of individual genotypes and the SNP loadings for each of the first 10 PCs (see the x-axis in each panel). Both the cis-interaction and G×Ancestry effects were set to explain a quarter of the total phenotypic variation and the remaining half was explained by additive SNP effects. The proportion of genotypic variance explained by each PC is shown in green. Panels (A) and (B) show estimates of the proportions of phenotypic variance explained (PVE) by genetic effects (i.e. estimated heritability) from LDSC and i-LDSC, respectively. Panels (C) and (D) show i-LDSC estimates of the phenotypic variation explained by tagged non-additive genetic effects using the cis-interaction LD score (i.e. estimates of $ϑ$). We assume the total heritability explained by all genetic effects to be (A, C) $H^{2}=0.6$ and (B, D) $H^{2}=0.3$. Results are based on 100 simulations per parameter combination.

![Figure 3—figure supplement 5.](https://cdn.elifesciences.org/articles/90459/elife-90459-fig3-figsupp5-v1.jpg)

**Figure 3—figure supplement 5.:** Synthetic trait architecture was simulated using real genotype data from individuals of self-identified European ancestry in the UK Biobank. All SNPs were considered to have at least an additive effect (i.e. creating a polygenic trait architecture). G×E effects were simulated using an amplification model65 (see Materials and methods) where we split the sample population in half to emulate two subsets of individuals coming from different environments. We randomly draw variant effect sizes for the first environment from a standard Gaussian distribution. Then effect sizes for the second environment are set to be the product of the effect sizes in from with first environment with an amplifier $w=[1.1,1.2,…,2]$ (see the x-axis in each panel). Additive and G×E effects were set to explain half of the phenotypic variation. Note that unlike results depicted in Figure 3—figure supplement 2, there are no cis-interaction effects that affect trait architecture. Here, panels (A) and (B) show estimates of the proportions of phenotypic variance explained (PVE) by genetic effects (i.e. estimated heritability) from LDSC and i-LDSC, respectively. Panels (C) and (D) show i-LDSC estimates of the phenotypic variation explained by tagged non-additive genetic effects using the cis-interaction LD score (i.e. estimates of $ϑ$). We assume the total heritability explained by all genetic effects to be (A, C) $H^{2}=0.6$ and (B, D) $H^{2}=0.3$. Results are based on 100 simulations per parameter combination.

![Figure 3—figure supplement 6.](https://cdn.elifesciences.org/articles/90459/elife-90459-fig3-figsupp6-v1.jpg)

**Figure 3—figure supplement 6.:** Synthetic trait architecture was simulated using real genotype data from individuals of self-identified European ancestry in the UK Biobank. All SNPs were considered to have at least an additive effect (i.e. creating a polygenic trait architecture). G×Ancestry effects were simulated as the product of individual genotypes and the SNP loadings for each of the first 10 PCs (see the x-axis in each panel). Additive and G×E effects were set to explain half of the phenotypic variation. The proportion of genotypic variance explained by each PC is shown in green. Note that unlike results depicted in Figure 3—figure supplement 3, there are no cis-interaction effects that affect trait architecture. Here, panels (A) and (B) show estimates of the proportions of phenotypic variance explained (PVE) by genetic effects (i.e. estimated heritability) from LDSC and i-LDSC, respectively. Panels (C) and (D) show i-LDSC estimates of the phenotypic variation explained by tagged non-additive genetic effects using the cis-interaction LD score (i.e. estimates of $ϑ$). We assume the total heritability explained by all genetic effects to be (A, C) $H^{2}=0.6$ and (B, D) $H^{2}=0.3$. Results are based on 100 simulations per parameter combination.

![Figure 3—figure supplement 7.](https://cdn.elifesciences.org/articles/90459/elife-90459-fig3-figsupp7-v1.jpg)

**Figure 3—figure supplement 7.:** Synthetic trait architecture was simulated using real genotype data from individuals of self-identified European ancestry in the UK Biobank. All SNPs were considered to have at least an additive effect (i.e. creating a polygenic trait architecture). G×Ancestry effects were simulated as the product of individual genotypes and the SNP loadings for each of the first 10 PCs (see the x-axis in each panel). Additive and G×E effects were set to explain half of the phenotypic variation. The proportion of genotypic variance explained by each PC is shown in green. Note that unlike results depicted in Figure 3—figure supplement 4, there are no cis-interaction effects that affect trait architecture. Here, panels (A) and (B) show estimates of the proportions of phenotypic variance explained (PVE) by genetic effects (i.e. estimated heritability) from LDSC and i-LDSC, respectively. Panels (C) and (D) show i-LDSC estimates of the phenotypic variation explained by tagged non-additive genetic effects using the cis-interaction LD score (i.e., estimates of $ϑ$). We assume the total heritability explained by all genetic effects to be (A, C) $H^{2}=0.6$ and (B, D) $H^{2}=0.3$. Results are based on 100 simulations per parameter combination.

![Figure 3—figure supplement 8.](https://cdn.elifesciences.org/articles/90459/elife-90459-fig3-figsupp8-v1.jpg)

**Figure 3—figure supplement 8.:** Synthetic trait architecture was simulated using real genotype data from individuals of self-identified European ancestry in the UK Biobank. Here, traits were generated with solely additive effects where only variants with the top or bottom ${1,5,10,25,50,100}$ percentile of LD scores were given nonzero coefficients in the generative model (see the x-axis in each panel). Panels (A) and (B) show estimates of the proportions of phenotypic variance explained (PVE) by genetic effects (i.e. estimated heritability) from LDSC and i-LDSC, respectively. Panels (C) and (D) show i-LDSC estimates of the phenotypic variation explained by tagged non-additive genetic effects using the cis-interaction LD score (i.e. estimates of $ϑ$). We assume the total heritability explained by all genetic effects to be (A, C) $H^{2}=0.6$ and (B, D) $H^{2}=0.3$. Results are based on 100 simulations per parameter combination. The overall takeaway is that breaking the assumed relationship between LD scores and chi-squared test statistics (i.e. that they are generally positively correlated) led to unbounded estimates of heritability for both LDSC and i-LDSC in all but the (polygenic) scenario when 100% of SNPs contributed to phenotypic variation.

![Figure 3—figure supplement 9.](https://cdn.elifesciences.org/articles/90459/elife-90459-fig3-figsupp9-v1.jpg)

**Figure 3—figure supplement 9.:** Synthetic trait architectures are simulated such that a substantial proportion of genetic variance is explained by an additive effect that is not directly observed. The goal of these simulations was to assess how these unobserved effects influence the estimation of the non-additive variance component in the i-LDSC model. In each simulation, we generated haplotypes that each contain 5000 variants. Next, we select either (A, B) a single causal variant with only an additive effect or (C, D) a set of ten causal variants with only additive effects. In each case, the causal variants have a MAF that is randomly selected between: (i) (0.01, 0.1), (ii) (0.1, 0.2), (iii) (0.2, 0.3), (iv) (0.3, 0.4), or (v) (0.4, 0.5) as depicted on the x-axis. The corresponding additive effect size for each causal variant across the haplotypes is simulated to be inversely proportional to its MAF (Schoech et al., 2019). On the y-axis, we measure the difference (Δ) between i-LDSC coefficient estimates when every variant is included in the model versus when the haplotype causal variants are omitted for two different trait architectures with broad-sense heritability set to (A, C) $H^{2}=0.6$ and (B, D) $H^{2}=0.3$. Results are based on 100 simulations per parameter combination.

![Figure 3—figure supplement 10.](https://cdn.elifesciences.org/articles/90459/elife-90459-fig3-figsupp10-v1.jpg)

**Figure 3—figure supplement 10.:** The i-LDSC framework protects against the false discovery of non-additive genetic variance when causal interacting SNPs are unobserved and the proportion of genetic variance explained by additive effects is equal to $ρ=$ 0.5.Synthetic trait architectures are simulated such that a substantial proportion of genetic variance is explained by pairwise genetic interaction effects that are not directly observed. The goal of these simulations was to assess how these unobserved effects influence the estimation of the non-additive variance component in the i-LDSC model. In each simulation, we generated haplotypes that each contain 5000 variants. Every SNP in the genome had at least a small additive effect. The corresponding additive effect size for each variant across the haplotypes is simulated to be inversely proportional to its MAF (Schoech et al., 2019). We then set (A, C) 1% or (B, D) 5% of causal variants in each haplotype to have non-zero interaction effects. On the y-axis, we measure the difference (Δ) between i-LDSC coefficient estimates when every variant is included in the model versus when the specified percentage of variants with pairwise genetic interaction effects are omitted for two different trait architectures with broad-sense heritability set to (A, B) $H^{2}=0.6$ and (C, D) $H^{2}=0.3$. Results are based on 100 simulations per parameter combination.

![Figure 3—figure supplement 11.](https://cdn.elifesciences.org/articles/90459/elife-90459-fig3-figsupp11-v1.jpg)

**Figure 3—figure supplement 11.:** The i-LDSC framework protects against the false discovery of non-additive genetic variance when causal interacting SNPs are unobserved and the proportion of genetic variance explained by additive effects is equal to $ρ=$ 0.8.Synthetic trait architectures are simulated such that a substantial proportion of genetic variance is explained by pairwise genetic interaction effects that are not directly observed. The goal of these simulations was to assess how these unobserved effects influence the estimation of the non-additive variance component in the i-LDSC model. In each simulation, we generated haplotypes that each contain 5000 variants. Every SNP in the genome had at least a small additive effect. The corresponding additive effect size for each variant across the haplotypes is simulated to be inversely proportional to its MAF (Schoech et al., 2019). We then set (A, C) 1% or (B, D) 5% of causal variants in each haplotype to have non-zero interaction effects. On the y-axis, we measure the difference (Δ) between i-LDSC coefficient estimates when every variant is included in the model versus when the specified percentage of variants with pairwise genetic interaction effects are omitted for two different trait architectures with broad-sense heritability set to (A, B) $H^{2}=0.6$ and (C, D) $H^{2}=0.3$. Results are based on 100 simulations per parameter combination.

![Figure 3—figure supplement 12.](https://cdn.elifesciences.org/articles/90459/elife-90459-fig3-figsupp12-v1.jpg)

**Figure 3—figure supplement 12.:** To simulate synthetic trait architectures, we first simulated additive effects for each variant to be MAF-dependent (i.e., $\alpha=-1$). Here, we set the corresponding interaction effect sizes to have a correlation with the additive effect sizes equal to $r={-1,-0.8,-0.6,…,0.6,0.8,1}$ (labeled across the x-axis). On the y-axis, we measure the bias in the LDSC and i-LDSC estimates of phenotypic variance explained (PVE) by genetic effects. In each simulation, we generate traits with an equal proportion of variance explained by additive and interaction effects and a total broad-sense heritability set to (A) $H^{2}=0.6$ and (B) $H^{2}=0.3$. Results are based on 100 simulations for each parameter value.

![Figure 3—figure supplement 13.](https://cdn.elifesciences.org/articles/90459/elife-90459-fig3-figsupp13-v1.jpg)

**Figure 3—figure supplement 13.:** To simulate synthetic trait architectures, we first simulated additive effects for each variant to be MAF-dependent (i.e., $\alpha=-1$). Here, we set the corresponding interaction effect sizes to be either (A, C) a linear function or (B, D) a squared function of the additive effects with a scaling factor $q={0.1,0.2,…,0.8,1}$ (labeled across the x-axis). On the y-axis, we measure the bias in the LDSC and i-LDSC estimates of the phenotypic variance explained (PVE) by genetic effects. In each simulation, we generate traits with an equal proportion of variance explained by additive and interaction effects and a total broad-sense heritability set to (A, B) $H^{2}=0.6$ and (C, D) $H^{2}=0.3$. Results are based on 100 simulations for each parameter value.

Next, we perform an additional set of simulations where we explore other common generative models for complex trait architecture that involve non-additive genetic effects. Specifically, we compare heritability estimates from LDSC and i-LDSC in the presence of additive effects, cis-acting interactions, and a third source of genetic variance stemming from either gene-by-environment (G×E) or or gene-by-ancestry (G×Ancestry) effects. Details on how these components were generated can be found in Materials and Methods. In general, i-LDSC underestimates overall heritability when additive effects and cis-acting interactions are present alongside G×E (Figure 3—figure supplement 2) and/or G×Ancestry effects when PCs are included as covariates (Figure 3—figure supplement 3). Notably, when PCs are not included to correct for residual stratification, both LDSC and i-LDSC can yield unbounded heritability estimates greater than 1 (Figure 3—figure supplement 4). Also interestingly, when we omit cis-interactions from the generative model (i.e. the genetic architecture of simulated traits is only made up of additive and G×E or G×Ancestry effects), i-LDSC will still estimate a nonzero genetic variance component with the cis-interaction LD scores (Figure 3—figure supplements 5–7). Collectively, these results empirically show the important point that cis-interaction scores are not enough to recover missing genetic variation for all types of trait architectures; however, they are helpful in recovering phenotypic variation explained by statistical interaction effects. Recall that the linear relationship between (expected) $χ^{2}$ test statistics and LD scores proposed by the LDSC framework holds when complex traits are generated under the polygenic model where all causal variants have the same expected contribution to phenotypic variation. When cis-interactions affect genetic architecture (e.g. in our earlier simulations in Figure 3), these assumptions are violated in LDSC, but the inclusion of the additional nonlinear scores in i-LDSC help recover the relationship between the expectation of $χ^{2}$ test statistics and LD.

As a further demonstration of how i-LDSC performs when assumptions of the original LD score model are violated, we also generated synthetic phenotypes with sparse architectures using the spike-and-slab model (Zhou et al., 2013). Here, traits were simulated with solely additive effects, but this time only variants with the top or bottom ${1,5,10,25,50,100}$ percentile of LD scores were given nonzero effects (see Materials and methods). Breaking the relationship assumed under the LDSC framework between LD scores and chi-squared statistics (i.e. that they are generally positively correlated) led to unbounded estimates of heritability in all but the (polygenic) scenario when 100% of SNPs contributed to the phenotypic variation (Figure 3—figure supplement 8).

Finally, we performed a set of polygenic simulations to assess if i-LDSC estimates of non-additive genetic variance could be spuriously inflated due to either (i) unobserved additive effects (see, for example, Hemani et al., 2014), (ii) unobserved SNPs that are involved in genetic interactions, or by (iii) nonzero correlation between the additive and interaction effect sizes in the generative model (i.e. breaking the independence assumption in Equation 2). In the first setting, we observed that, across a range of both minor allele frequencies and effect sizes, the omission of causal haplotypes had a negligible effect on the estimated value of the coefficients in i-LDSC (Figure 3—figure supplement 9). We hypothesize this is due to the fact that the simulations were done for polygenic architectures where all SNPs have at least an additive effect. As a result, not observing a small subset of SNPs does not hinder the ability of i-LDSC to estimate genetic variance because the effect size of each SNP is small. If these simulations were conducted for sparse architectures, we would have likely seen a greater impact on i-LDSC; although, we have already shown the LD score regression framework to be uncalibrated for traits with sparse genetic architectures (again see Figure 3—figure supplement 8). In the second setting, we observed that the i-LDSC framework protects against the false discovery of non-additive genetic effects and underestimates the variance component $ϑ$ when causal variants involved in pairwise interactions were unobserved (Figure 3—figure supplements 10 and 11). As a direct comparison, estimates of the additive variance component $\tau$ in i-LDSC were not affected by the unobserved interacting variants. Lastly, in the third setting, we observed that the mean estimate of the genetic variance in both LDSC and i-LDSC had a slight upward bias as the correlation between additive and interaction effect sizes in the generative model increased; however, the median of these bias estimates was still near zero across all simulated scenarios and their corresponding replicates (Figure 3—figure supplements 12 and 13).

### Application of i-LDSC to the UK Biobank and BioBank Japan

To assess whether pairwise interaction genetic effects are significantly affecting estimates of heritability in empirical biobank data, we applied i-LDSC to 25 continuous quantitative traits from the UK Biobank and BioBank Japan (Supplementary file 3). Protocols for computing GWAS summary statistics for the UK Biobank are described in the Materials and methods; while pre-computed summary statistics for BioBank Japan were downloaded directly from the consortium website (https://pheweb.jp/downloads). We release the cis-acting SNP-by-SNP interaction LD scores used in our analyses on the i-LDSC GitHub repository from two reference groups in the 1000 Genomes: 489 individuals from the European superpopulation (EUR) and 504 individuals from the East Asian (EAS) superpopulation (see also Supplementary files 4 and 5).

In each of the 25 traits, we analyzed in the UK Biobank, we detected significant proportions of estimated genetic variation stemming from tagged pairwise cis-interactions (Table 1). This includes many canonical traits of interest in heritability analyses: height, cholesterol levels, urate levels, and both systolic and diastolic blood pressure. Our findings in Table 1 are supported by multiple published studies identifying evidence of non-additive effects playing a role in the architectures of different traits of interest. For example, Li et al., 2020 found evidence for genetic interactions that contributed to the pathogenesis of coronary artery disease. It was also recently shown that non-additive genetic effects plays a significant role in body mass index (Song et al., 2022). Generally, we find that the traditional LDSC produces lower estimates of trait heritability because it does not consider the additional sources of genetic signal that i-LDSC does (Table 1). In BioBank Japan, 23 of the 25 traits analyzed had a significant nonlinear component detected by i-LDSC — with HDL and triglyceride levels being the only exceptions.

**Table 1.**
 i-LDSC heritability estimates and p-values highlighting statistically significant contributions of tagged pairwise genetic interaction effects for 25 traits in the UK Biobank and BioBank Japan.Here, LDSC heritability estimates are included as a baseline. The difference between the approaches is that the i-LDSC heritability estimates include proportions of phenotypic variation that are explained by tagged non-additive variation (see columns with estimates of $ϑ$). Note that all 25 traits analyzed in the UK Biobank and 23 of the 25 traits analyzed in BioBank Japan have a statistically significant amount of tagged non-additive genetic effects as detected by the cis-interaction LD score (p < 0.05). The two traits without significant tagged non-additive genetic effects in BioBank Japan were HDL (p = 0.081) and Triglyceride (p = 0.110). These traits are indicated by *. The i-LDSC p-values are related to the estimates of the $ϑ$ coefficients which are also displayed in Figure 4.


<table>
  <thead>
    <tr>
      <th>Trait</th>
      <th>UKB (LDSC)</th>
      <th>UKB (i-LDSC)</th>
      <th>UKB ϑ^</th>
      <th>UKB p-value</th>
      <th>BBJ (LDSC)</th>
      <th>BBJ (i-LDSC)</th>
      <th>BBJ ϑ^</th>
      <th>BBJ p-value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Basophil</td>
      <td>0.0250</td>
      <td>0.0315</td>
      <td>0.0065</td>
      <td>1.572× 10−12</td>
      <td>0.0684</td>
      <td>0.1548</td>
      <td>0.0864</td>
      <td>0.025</td>
    </tr>
    <tr>
      <td>BMI</td>
      <td>0.1757</td>
      <td>0.2349</td>
      <td>0.0592</td>
      <td>3.083× 10−84</td>
      <td>0.1667</td>
      <td>0.2656</td>
      <td>0.0989</td>
      <td>2.438× 10−18</td>
    </tr>
    <tr>
      <td>Cholesterol</td>
      <td>0.0954</td>
      <td>0.0974</td>
      <td>0.0020</td>
      <td>1.821× 10−16</td>
      <td>0.0629</td>
      <td>0.1268</td>
      <td>0.0639</td>
      <td>2.740× 10−4</td>
    </tr>
    <tr>
      <td>CRP</td>
      <td>0.0354</td>
      <td>0.0414</td>
      <td>0.0060</td>
      <td>9.845× 10−12</td>
      <td>0.0202</td>
      <td>0.1625</td>
      <td>0.1423</td>
      <td>0.020</td>
    </tr>
    <tr>
      <td>DBP</td>
      <td>0.0940</td>
      <td>0.1203</td>
      <td>0.0263</td>
      <td>1.118× 10−65</td>
      <td>0.0605</td>
      <td>0.1267</td>
      <td>0.0662</td>
      <td>1.675× 10−7</td>
    </tr>
    <tr>
      <td>EGFR</td>
      <td>0.1521</td>
      <td>0.1999</td>
      <td>0.0478</td>
      <td>1.187× 10−46</td>
      <td>0.1010</td>
      <td>0.1225</td>
      <td>0.0215</td>
      <td>4.232× 10−5</td>
    </tr>
    <tr>
      <td>Eosinophil</td>
      <td>0.1055</td>
      <td>0.1375</td>
      <td>0.0320</td>
      <td>1.230× 10−18</td>
      <td>0.0785</td>
      <td>0.1973</td>
      <td>0.1188</td>
      <td>0.001</td>
    </tr>
    <tr>
      <td>HBA1C</td>
      <td>0.0906</td>
      <td>0.1083</td>
      <td>0.0177</td>
      <td>1.578× 10−26</td>
      <td>0.1057</td>
      <td>0.1308</td>
      <td>0.0251</td>
      <td>0.031</td>
    </tr>
    <tr>
      <td>HDL*</td>
      <td>0.1599</td>
      <td>0.1768</td>
      <td>0.0169</td>
      <td>9.636× 10−37</td>
      <td>0.1590</td>
      <td>0.1838</td>
      <td>0.0248</td>
      <td>0.081</td>
    </tr>
    <tr>
      <td>Height</td>
      <td>0.3675</td>
      <td>0.4815</td>
      <td>0.1140</td>
      <td>1.038× 10−64</td>
      <td>0.3941</td>
      <td>0.7336</td>
      <td>0.3395</td>
      <td>7.433× 10−33</td>
    </tr>
    <tr>
      <td>Hematocrit</td>
      <td>0.1078</td>
      <td>0.1352</td>
      <td>0.0274</td>
      <td>2.479× 10−25</td>
      <td>0.0752</td>
      <td>0.0928</td>
      <td>0.0176</td>
      <td>3.689× 10−5</td>
    </tr>
    <tr>
      <td>Hemoglobin</td>
      <td>0.1177</td>
      <td>0.1433</td>
      <td>0.0256</td>
      <td>4.284× 10−27</td>
      <td>0.0702</td>
      <td>0.0752</td>
      <td>0.0050</td>
      <td>9.037× 10−4</td>
    </tr>
    <tr>
      <td>LDL</td>
      <td>0.0802</td>
      <td>0.0859</td>
      <td>0.0057</td>
      <td>5.087× 10−13</td>
      <td>0.0745</td>
      <td>0.1438</td>
      <td>0.0693</td>
      <td>0.018</td>
    </tr>
    <tr>
      <td>Lymphocyte</td>
      <td>0.0402</td>
      <td>0.0501</td>
      <td>0.0099</td>
      <td>4.906× 10−19</td>
      <td>0.0844</td>
      <td>0.1757</td>
      <td>0.0913</td>
      <td>5.479× 10−5</td>
    </tr>
    <tr>
      <td>MCH</td>
      <td>0.1361</td>
      <td>0.1597</td>
      <td>0.0236</td>
      <td>1.785× 10−25</td>
      <td>0.1536</td>
      <td>0.2831</td>
      <td>0.1295</td>
      <td>1.042× 10−5</td>
    </tr>
    <tr>
      <td>MCHC</td>
      <td>0.0317</td>
      <td>0.0364</td>
      <td>0.0047</td>
      <td>3.730× 10−12</td>
      <td>0.0571</td>
      <td>0.0650</td>
      <td>0.0079</td>
      <td>0.027</td>
    </tr>
    <tr>
      <td>MCV</td>
      <td>0.1630</td>
      <td>0.1902</td>
      <td>0.0272</td>
      <td>1.180× 10−29</td>
      <td>0.1530</td>
      <td>0.2818</td>
      <td>0.1288</td>
      <td>1.042× 10−5</td>
    </tr>
    <tr>
      <td>Monocyte</td>
      <td>0.0788</td>
      <td>0.0955</td>
      <td>0.0167</td>
      <td>5.257× 10−18</td>
      <td>0.0888</td>
      <td>0.1549</td>
      <td>0.0661</td>
      <td>0.004</td>
    </tr>
    <tr>
      <td>Neutrophil</td>
      <td>0.1102</td>
      <td>0.1391</td>
      <td>0.0289</td>
      <td>1.777× 10−33</td>
      <td>0.1191</td>
      <td>0.2114</td>
      <td>0.0923</td>
      <td>5.050× 10−5</td>
    </tr>
    <tr>
      <td>Platelet</td>
      <td>0.1992</td>
      <td>0.2447</td>
      <td>0.0455</td>
      <td>2.303× 10−37</td>
      <td>0.1565</td>
      <td>0.2436</td>
      <td>0.0871</td>
      <td>7.724× 10−9</td>
    </tr>
    <tr>
      <td>RBC</td>
      <td>0.1574</td>
      <td>0.1933</td>
      <td>0.0359</td>
      <td>3.292× 10−31</td>
      <td>0.1203</td>
      <td>0.2068</td>
      <td>0.0865</td>
      <td>5.972× 10−8</td>
    </tr>
    <tr>
      <td>SBP</td>
      <td>0.0954</td>
      <td>0.1201</td>
      <td>0.0247</td>
      <td>8.660× 10−75</td>
      <td>0.0769</td>
      <td>0.1604</td>
      <td>0.0835</td>
      <td>9.075× 10−10</td>
    </tr>
    <tr>
      <td>Triglycerides*</td>
      <td>0.1061</td>
      <td>0.1204</td>
      <td>0.0143</td>
      <td>1.410× 10−26</td>
      <td>0.1171</td>
      <td>0.2670</td>
      <td>0.1499</td>
      <td>0.110</td>
    </tr>
    <tr>
      <td>Urate</td>
      <td>0.1217</td>
      <td>0.1550</td>
      <td>0.0333</td>
      <td>9.642× 10−38</td>
      <td>0.1395</td>
      <td>0.3462</td>
      <td>0.2067</td>
      <td>0.015</td>
    </tr>
    <tr>
      <td>WBC</td>
      <td>0.0962</td>
      <td>0.1250</td>
      <td>0.0288</td>
      <td>9.866× 10−34</td>
      <td>0.1024</td>
      <td>0.2266</td>
      <td>0.1242</td>
      <td>1.346× 10−8</td>
    </tr>
  </tbody>
</table>

For each of the 25 traits that we analyzed, we found that the i-LDSC heritability estimates are significantly correlated with corresponding estimates from LDSC in both the UK Biobank ($r^{2}=0.988$, $P=5.936\times10^{-24}$) and BioBank Japan ($r^{2}=0.849$, $P=6.061\times10^{-11}$) as shown in Figure 4A. Additionally, we found that the heritability estimates for the same traits between the two biobanks are highly correlated according to both LDSC ($r^{2}=0.848$, $P=7.166\times10^{-11}$) and i-LDSC ($r^{2}=0.666$, $P=6.551\times10^{-7}$) analyses as shown in Figure 4B. After comparing the i-LDSC heritability estimates to LDSC, we then assessed whether there was significant difference in the amount of phenotypic variation explained by the non-additive genetic effect component in the GWAS summary statistics derived from the the UK Biobank and BioBank Japan (i.e. comparing the estimates of $ϑ$; see Figure 4—figure supplement 1A). We show that, while heterogeneous between traits, the phenotypic variation explained by genetic interactions is relatively of the same magnitude for both biobanks ($r^{2}=0.372$, $P=0.0119$). Notably, the trait with the most significant evidence of tagged cis-interaction effects in GWAS summary statistics is height which is known to have a highly polygenic architecture.

![Figure 4.](https://cdn.elifesciences.org/articles/90459/elife-90459-fig4-v1.jpg)

**Figure 4.:** The i-LDSC framework recovers heritability and provides estimates of tagged cis-interactions in GWAS summary statistics ($ϑ$) for 25 quantitiative traits in the UK Biobank and BioBank Japan.(A) In both the UK Biobank (green) and BioBank Japan (purple), estimates of phenotypic variance explained (PVE) by genetic effects from i-LDSC and LDSC are highly correlated for 25 different complex traits. The Spearman correlation coefficient between heritability estimates from LDSC and i-LDSC for the UK Biobank and BioBank Japan are $r^{2}=0.989$ and $r^{2}=0.850$, respectively. The $y=x$ dotted line represents the values at which estimates from both approaches are the same. (B) PVE estimates from the UK Biobank are better correlated with those from the BioBank Japan across 25 traits using LDSC (Spearman $r^{2}=0.848$) than i-LDSC (Spearman $r^{2}=0.666$). (C) Both the original and stratified LDSC models recover the same amount of PVE when the cis-interaction LD score is included as an additional component in the UK Biobank analysis (Spearman $r^{2}=0.989$). These models are listed as i-LDSC and s+i-LDSC, respectively. For s+i-LDSC, we included 97 functional annotations from Gazal et al. to estimate heritability. (D) Estimates of non-additive variance components in i-LDSC versus s+i-LDSC (Spearmen $r^{2}=0.184$). While not statistically significant in the stratified analysis with the additional annotations, the non-additive component still makes nonzero contributions to the PVE estimation for all 25 traits in the UK Biobank (see Tables 1 and 2).

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/90459/elife-90459-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** (A) i-LDSC estimates of the phenotypic variation explained by tagged non-additive genetic effects using the cis-interaction LD score (i.e., estimates of $ϑ$) between traits in the UK Biobank and BioBank Japan (Spearman $r^{2}=0.372$). (B) Estimates of i-LDSC and LDSC intercept terms for 25 traits analyzed in the UK Biobank and BioBank Japan. Intercept terms using LDSC and i-LDSC are highly correlated in both the UK Biobank (Spearman $r^{2}=0.888$) and BioBank Japan (Spearman $r^{2}=0.813$). The $x=y$ dotted line represents points for when the two sets of estimates are equal.

The intercepts estimated by LDSC and i-LDSC are also highly correlated in both the UK Biobank and the BioBank Japan (Figure 4—figure supplement 1B). Recall that these intercept estimates represent the confounding factor due to uncontrolled effects. For LDSC, this does include phenotypic variation that is due to unaccounted for pairwise statistical genetic interactions. The i-LDSC intercept estimates tend to be correlated with, but are generally different than, those computed with LDSC — empirically indicating that non-additive genetic variation is partitioned away and is missed when using the standard LD score alone. This result shows similar patterns in both the UK Biobank ($r^{2}=0.888$, $P=1.962\times10^{-12}$) and BioBank Japan ($r^{2}=0.813$, $P=7.814\times10^{-10}$).

Lastly, we performed an additional analysis in the UK Biobank where the cis-interaction scores are included as an annotation alongside 97 other functional categories in the stratified-LD score regression framework and its software s-LDSC (Gazal et al., 2017; Materials and methods). Here, s-LDSC heritability estimates still showed an increase with the interaction scores versus when the publicly available functional categories were analyzed alone, but albeit at a much smaller magnitude (Table 2). The contributions from the pairwise interaction component to the overall estimate of genetic variance ranged from 0.005 for MCHC ($P=0.373$) to 0.055 for HDL ($P=0.575$; Figure 4C and D). Furthermore, in this analysis, the estimates of the non-additive components were no longer statistically significant for any of the traits in the UK Biobank (Table 2). Despite this, these results highlight the ability of the i-LDSC framework to identify sources of ‘missing’ phenotypic variance explained in heritability estimation. Importantly, moving forward, we suggest using the cis-interaction scores with additional annotations whenever they are available as it provides more conservative estimates of the role of non-additive effects on trait architecture.

**Table 2.**
 Comparison of s-LDSC and i-LDSC estimates of phenotypic variance explained (PVE) by genetic effects for 25 complex traits in the UK Biobank.Here, we use stratified LD score regression (s-LDSC) to partition heritability across different genomic elements (Finucane et al., 2015). We used 97 functional annotations from Gazal et al. to estimate heritability in 25 traits. We then appended cis-interaction LD scores as an additional annotation to obtain heritability estimates (this method is referred to as s+i-LDSC in the table). p-values for the s+i-LDSC model detailing the contributions of tagged non-additive genetic effects for 25 traits are provided in the last column. Note that, while not statistically significant in this stratified analysis with the additional annotations, the non-additive component still makes nonzero contributions to the PVE estimation for all 25 traits.


<table>
  <thead>
    <tr>
      <th>Trait</th>
      <th>UKB PVE (s-LDSC)</th>
      <th>UKB PVE (s+i-LDSC)</th>
      <th>s+i-LDSC p-value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Basophil</td>
      <td>0.0363</td>
      <td>0.0375</td>
      <td>0.4728</td>
    </tr>
    <tr>
      <td>BMI</td>
      <td>0.2100</td>
      <td>0.2482</td>
      <td>0.8126</td>
    </tr>
    <tr>
      <td>Cholesterol</td>
      <td>0.1042</td>
      <td>0.1358</td>
      <td>0.6202</td>
    </tr>
    <tr>
      <td>CRP</td>
      <td>0.0452</td>
      <td>0.0524</td>
      <td>0.6483</td>
    </tr>
    <tr>
      <td>DBP</td>
      <td>0.1228</td>
      <td>0.1441</td>
      <td>0.6125</td>
    </tr>
    <tr>
      <td>EGFR</td>
      <td>0.1826</td>
      <td>0.2105</td>
      <td>0.8507</td>
    </tr>
    <tr>
      <td>Eosinophil</td>
      <td>0.1403</td>
      <td>0.1578</td>
      <td>0.1867</td>
    </tr>
    <tr>
      <td>HBA1C</td>
      <td>0.1040</td>
      <td>0.1275</td>
      <td>0.6917</td>
    </tr>
    <tr>
      <td>HDL</td>
      <td>0.1820</td>
      <td>0.2373</td>
      <td>0.5754</td>
    </tr>
    <tr>
      <td>Height</td>
      <td>0.4315</td>
      <td>0.4726</td>
      <td>0.5224</td>
    </tr>
    <tr>
      <td>Hematocrit</td>
      <td>0.1416</td>
      <td>0.1646</td>
      <td>0.3956</td>
    </tr>
    <tr>
      <td>Hemoglobin</td>
      <td>0.1504</td>
      <td>0.1795</td>
      <td>0.2299</td>
    </tr>
    <tr>
      <td>LDL</td>
      <td>0.0858</td>
      <td>0.1131</td>
      <td>0.8812</td>
    </tr>
    <tr>
      <td>Lymphocyte</td>
      <td>0.0545</td>
      <td>0.0651</td>
      <td>0.1453</td>
    </tr>
    <tr>
      <td>MCH</td>
      <td>0.1497</td>
      <td>0.1545</td>
      <td>0.0968</td>
    </tr>
    <tr>
      <td>MCHC</td>
      <td>0.0450</td>
      <td>0.0496</td>
      <td>0.3728</td>
    </tr>
    <tr>
      <td>MCV</td>
      <td>0.1814</td>
      <td>0.1930</td>
      <td>0.1530</td>
    </tr>
    <tr>
      <td>Monocyte</td>
      <td>0.1085</td>
      <td>0.1431</td>
      <td>0.5421</td>
    </tr>
    <tr>
      <td>Neutrophil</td>
      <td>0.1320</td>
      <td>0.1599</td>
      <td>0.2499</td>
    </tr>
    <tr>
      <td>Platelet</td>
      <td>0.2317</td>
      <td>0.2628</td>
      <td>0.7371</td>
    </tr>
    <tr>
      <td>RBC</td>
      <td>0.1933</td>
      <td>0.2223</td>
      <td>0.3197</td>
    </tr>
    <tr>
      <td>SBP</td>
      <td>0.1206</td>
      <td>0.1419</td>
      <td>0.1100</td>
    </tr>
    <tr>
      <td>Triglycerides</td>
      <td>0.1335</td>
      <td>0.1621</td>
      <td>0.5301</td>
    </tr>
    <tr>
      <td>Urate</td>
      <td>0.1530</td>
      <td>0.1736</td>
      <td>0.1177</td>
    </tr>
    <tr>
      <td>WBC</td>
      <td>0.1221</td>
      <td>0.1482</td>
      <td>0.5155</td>
    </tr>
  </tbody>
</table>

## Discussion

In this paper, we present i-LDSC, an extension of the LD score regression framework which aims to recover missing heritability from GWAS summary statistics by incorporating an additional score that measures the non-additive genetic variation that is tagged by genotyped SNPs. Here, we demonstrate how i-LDSC builds upon the original LDSC model through the development of new ‘cis-interaction’ LD scores which help to investigate signals of cis-acting SNP-by-SNP interactions (Figure 1 and Figure 1—figure supplements 1–5). Through extensive simulations, we show that i-LDSC is well-calibrated under the null model when polygenic traits are generated only by additive effects (Figure 2 and Figure 2—figure supplements 1–2), we highlight that i-LDSC provides greater heritability estimates over LDSC when traits are indeed generated with cis-acting SNP-by-SNP interaction effects (Figure 3 and Figure 3—figure supplement 1, and Supplementary files 1 and 2), and we tested the robustness of i-LDSC on phenotypes where assumptions of the original LD score model are violated (Figure 3—figure supplements 2–13). Finally, in real data, we show examples of many traits with estimated GWAS summary statistics that tag cis-interaction effects in the UK Biobank and BioBank Japan (Figure 4 and Figure 4—figure supplement 1, Tables 1 and 2, and Supplementary files 3-5). We have made i-LDSC a publicly available command line tool that requires minimal updates to the computing environment used to run the original implementation of LD score regression. In addition, we provide pre-computed cis-interaction LD scores calculated from the European (EUR) and East Asian (EAS) reference populations in the 1000 Genomes phase 3 data (see Data and Software Availability under Materials and Methods).

The current implementation of the i-LDSC framework offers many directions for future development and applications. First, an area of future work would be to explore how the relationship between cis-interaction LD scores and interaction effect sizes from the generative model of complex traits might bias heritability estimates provided by i-LDSC (e.g., similar to the relationship we explored between the standard LD scores and linear effect sizes in Figure 3—figure supplement 8). Second, as we showed with our simulation studies (Figure 3—figure supplements 2–8), the cis-interaction LD scores that we propose are not always enough to recover explainable non-additive genetic effects for all types of trait architectures. While we focus on pairwise cis-acting SNP-by-SNP statistical interactions in this work, the theoretical concepts underlying i-LDSC can easily be adapted to other types of interactions as well. Third, in our analysis of the UK Biobank and BioBank Japan, we showed that the inclusion of additional categories via frameworks such as stratified LD score regression (Finucane et al., 2015) can be used to provide more refined heritability estimates from GWAS summary statistics while accounting for linkage (see results in Table 1 versus Table 2). A key part of our future work is to continue to explore whether considering functional annotation groups would also improve our ability to identify tagged non-additive genetic effects. Lastly, we have only focused on analyzing one phenotype at a time in this study. However, many previous studies have extensively shown that modeling multiple phenotypes can often dramatically increase power (Runcie et al., 2020; Stamp et al., 2022). Therefore, it would be interesting to extend the i-LDSC framework to multiple traits to study nonlinear genetic correlations in the same way that LDSC was recently extended to uncover additive genetic correlation maps across traits (Naqvi et al., 2021).

## Materials and methods

### Generative statistical model for complex traits

Our goal in this study is to reanalyze summary statistics from genome-wide association studies (GWAS) and estimate heritability while accounting for both additive genetic associations and tagged interaction effects. We begin by assuming the following generative linear model for complex traits which can be seen as an extended view of Equation 1 in the main text

$$
y=b_{0}+X\beta+X_{D}\omega+W\theta+\epsilon,\epsilon∼N(0,(1−H^{2})I),
$$

where $𝐲$ denotes an $N$-dimensional vector of phenotypic states for a quantitative trait of interest measured in $N$ individuals; $b_{0}$ is an intercept term; $𝐗$ is an $N\timesJ$ matrix of genotypes, with $J$ denoting the number of single nucleotide polymorphism (SNPs) encoded as ${0,1,2}$ copies of a reference allele at each locus; $𝜷=(\beta_{1},…,\beta_{J})$ is a $J$-dimensional vector containing the true additive effect sizes for an additional copy of the reference allele at each locus on $y$; $X_{D}$ is an $N\timesJ$ matrix that represents the dominance for each genotype encoded as ${0,1,1}$ with corresponding effect sizes $\omega$; $W$ is an $N\timesM$ matrix of genetic interactions; $𝜽=(\theta_{1},…,\theta_{M})$ is an $M$-dimensional vector containing the interaction effect sizes; $𝜺$ is a normally distributed error term with mean zero and variance scaled according to the proportion of phenotypic variation not explained by the broad-sense heritability of the trait, denoted by $H^{2}$; and $𝐈$ denotes an $N\timesN$ identity matrix. Note that the encoding for dominance in $𝐗_{D}$ was chosen because it imposes orthogonality with the genotype encoding in $𝐗$ (Purcell et al., 2007; Vitezica et al., 2017; Palmer et al., 2023).

For convenience, we will assume that the genotype matrix (column-wise), the dominance matrix (also column-wise), and trait of interest have all been standardized (Strandén and Christensen, 2011; de Los Campos et al., 2013; Zhou et al., 2013). Furthermore, while the matrix $𝐖$ could encode any source of non-additive genetic interactions (e.g. gene-by-environmental effects) in theory, we limit our focus in this study to trait architectures that have been generated with contributions stemming from cis-acting statistical SNP-by-SNP (or pairwise) interactions. To that end, we assume that the columns of $𝐖$ are the Hadamard (element-wise) product between genotypic vectors of the form $𝐱_{j}∘𝐱_{k}$ for the $j$-th and $k$-th variants. We also want to point out that the generative formulation of Equation 7 can also be easily extended to accommodate other fixed effects (e.g. age, sex, or genotype principal components), as well as other random effects terms that can be used to account for sample non-independence due to other environmental factors.

As a final set of assumptions, we will let the intercept term $b_{0}$ be a fixed parameter while allowing the other coefficients to follow independent Gaussian distributions with variances proportional to their individual contributions to the trait heritability (Yang et al., 2010; Wu et al., 2011; Zhou et al., 2013; Jiang and Reif, 2015; Crawford et al., 2017)

$$
\beta_{j}∼N(0,\phi_{\beta}^{2}/J),\omega_{j}∼N(0,\phi_{\omega}^{2}/J),\theta_{m}∼N(0,\phi_{\theta}^{2}/M),
$$

for $j=1,…,J$ and $m=1,…,M$. The broad-sense heritability of the trait is defined as $H^{2}=\phi_{\beta}^{2}+\phi_{\omega}^{2}+\phi_{\theta}^{2}$. Under the generative model in Equation 7, we then say that $𝕍⁢[𝐗⁢𝜷]=\phi_{\beta}^{2}$ is the proportion of phenotypic variation contributed by additive SNP effects, $𝕍⁢[𝐗_{D}⁢𝝎]=\phi_{\omega}^{2}$ is the proportion of phenotypic variation contributed by dominance effects, and the set of interactions involving some subset of causal SNPs contribute the remaining proportion to the heritability $𝕍⁢[𝐖⁢𝜽]=\phi_{\theta}^{2}$. As we mentioned in the main text, we recognize that the appropriateness of treating genetic effects as random variables in analytical derivations has been questioned (de Los Campos et al., 2015), but our simulation studies show that i-LDSC accurately recovers non-additive genetic variance in Equation 7 under a broad range of conditions.

### Orthogonality between additive and non-additive genetic effects

Assuming that the effect sizes ${𝜷,𝝎,𝜽}$ in Equation 8 follow independent and zero mean Gaussian distributions leads to orthogonality between the additive and non-additive components in Equation 7. Since the genotypes $𝐗$ and the dominance values $𝐗_{D}$ are fixed orthogonal matrices, it is straightforward to show that $Cov⁢[𝐗⁢𝜷,𝐗_{D}⁢𝝎]=0$ (Vitezica et al., 2017; Palmer et al., 2023). The same relationship can be shown for the additive and the pairwise interaction genetic effects where

$$
Cov[X\beta,W\theta]=E[\beta^{⊺}X^{⊺}W\theta]−E[\beta^{⊺}X^{⊺}]E[W\theta]=E[\sumrs\beta_{r}(X^{⊺}W)_{rs}\theta_{s}]−E[\beta^{⊺}]X^{⊺}WE[\theta]=\sumrs(X^{⊺}W)_{rs}E[\beta_{r}\theta_{s}]−0^{⊺}X^{⊺}W0=\sumrs(X^{⊺}W)_{rs}E[\beta_{r}]E[\theta_{s}]=0
$$

with $𝐱_{j}$ and $𝐰_{m}$ denoting the $j$-th and $m$-th column of the individual-level genotype matrix $𝐗$ and the interaction matrix $𝐖$, respectively. Note that a similar derivation to Equation 9 can also be done for the dominance and pairwise genetic interaction effects. This concept of orthogonality is important because we want to preserve a unique partitioning of genetic variance when modeling a trait of interest.

### Genotypes and their interactions are correlated despite being linearly independent

The design matrices $𝐗$ and $𝐖$ in Equation 7 are not linearly dependent because the pairwise interactions between two SNPs are encoded as the Hadamard product of two genotypic vectors in the form $𝐱_{j}∘𝐱_{k}$ (which is a nonlinear function). Linear dependence would have implied that one could find a transformation between a SNP and an interaction term in the form $𝐰_{m}=c\times𝐱_{j}$ for some constant $c$. However, despite their linear independence, $𝐗$ and $𝐖$ are themselves not orthogonal and still have a nonzero correlation. This implies that the inner product between genotypes and their interactions is nonzero $𝐗^{⊺}⁢𝐖\neq𝟎$. To see this, we focus on a focal SNP $𝐱_{j}$ and consider three different types of interactions:

The following derivations rely on the fact that: (1) we assume that genotypes have been mean-centered and scaled to have unit variance, and (2) under Hardy-Weinberg equilibrium, SNPs marginally follow a binomial distribution $𝐱_{j}∼Bin⁢(2,p)$ where $p$ represents the minor allele frequency (MAF) (Wray et al., 2007; Lippert et al., 2013).

#### Scenario I

The covariance between a focal SNP and an interaction with itself is $Cov⁢[𝐱_{j},𝐱_{j}⁢𝐱_{j}]=𝔼⁢[𝐱_{j}^{3}]-𝔼⁢[𝐱_{j}]⁢𝔼⁢[𝐱_{j}^{2}]$. With mean-centered SNPs, this is proportional to $𝔼⁢[𝐱_{j}^{3}]=(q-p)/\sqrt{2⁢p⁢q}$ which is the skewness of the binomial distribution where, again, $p=$ MAF and $q=$ 1-MAF of the $j$-th SNP.

#### Scenario II

Assume that we have two SNPs, $𝐱_{j}∼Bin⁢(2,p_{j})$ and $𝐱_{k}∼Bin⁢(2,p_{k})$ where $p_{j}$ and $p_{k}$ represent their respective minor allele frequencies. We want to compute the correlation between $𝐱_{j}$ and the interaction $𝐱_{j}⁢𝐱_{k}$ where $Cov⁢[𝐱_{j},𝐱_{j}⁢𝐱_{k}]=𝔼⁢[𝐱_{j}^{2}⁢𝐱_{k}]-𝔼⁢[𝐱_{j}]⁢𝔼⁢[𝐱_{j}⁢𝐱_{k}]$. Again, with the mean-centered assumption, the covariance is proportional to the expectation $𝔼⁢[𝐱_{j}^{2}⁢𝐱_{k}]$. Here, with SNPs taking on values ${0,1,2}$, the joint distribution between $𝐱_{j}^{2}$ and $𝐱_{k}$ can be written out as the following Kang and Jung, 2001:

<table>
  <thead>
    <tr>
      <th></th>
      <th>𝐱j2=0</th>
      <th>𝐱j2=1</th>
      <th>𝐱j2=4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>𝐱k=0</td>
      <td>uj⁢k2</td>
      <td>2⁢uj⁢k⁢(1-pk-uj⁢k)</td>
      <td>(1-pk-uj⁢k)2</td>
    </tr>
    <tr>
      <td>𝐱k=1</td>
      <td>2⁢uj⁢k⁢(1-pj-uj⁢k)</td>
      <td>2ujk(ujk+pj+pk−1)+2(1−pj−ujk)(1−pk−ujk)</td>
      <td>2⁢(uj⁢k+pj+pk-1)⁢(1-pk-uj⁢k)</td>
    </tr>
    <tr>
      <td>𝐱k=2</td>
      <td>(1-pj-uj⁢k)2</td>
      <td>2⁢(uj⁢k+pj+pk-1)⁢(1-pj-uj⁢k)</td>
      <td>(uj⁢k+pj+pk-1)2</td>
    </tr>
  </tbody>
</table>

where $u_{j⁢k}=(1-p_{j})⁢(1-p_{k})+r_{j⁢k}⁢\sqrt{p_{j}⁢p_{k}⁢(1-p_{j})⁢(1-p_{k})}$ and $r_{j⁢k}$ is the Pearson correlation or linkage disequilibrium (LD) between the $j$-th and $k$-th SNPs.

#### Scenario III

The covariance between a focal SNP and an interaction with a pair of different SNPs $Cov⁢[𝐱_{j},𝐱_{k}⁢𝐱_{l}]$ will be nonzero if the $j$-th SNP is correlated with either variant (i.e., $r_{j⁢k}\neq0$ or $r_{j⁢l}\neq0$).

### Traditional estimation of additive GWAS summary statistics

As previously mentioned, the key to this work is that SNP-level GWAS summary statistics can also tag non-additive genetic effects when there is a nonzero correlation between individual-level genotypes and their interactions (as defined in Equation 7). Throughout the rest of this section, we will use $𝐗^{⊺}⁢𝐗/N$ to denote the LD or pairwise correlation matrix between SNPs. We will then let $𝐑$ represent an LD matrix empirically estimated from external data (e.g. directly from GWAS study data, or using a pairwise LD map from a population that is representative of the samples analyzed in the GWAS study). The important property here is the following

$$
𝔼⁢[𝐗^{⊺}⁢𝐗]≈N⁢𝐑,𝔼⁢[𝐱_{j}^{⊺}⁢𝐱_{j}]≈N,𝔼⁢[𝐱_{j}^{⊺}⁢𝐱_{k}]≈N⁢r_{j⁢k}
$$

where the term $r_{j⁢k}$ is again defined as the Pearson correlation coefficient between the $j$-th and $k$-th SNPs, respectively.

In traditional GWAS studies, summary statistics of the true additive effects $𝜷=(𝐗^{⊺}⁢𝐗)^{-1}⁢𝐗^{⊺}⁢𝐲$ in Equation 7 are typically derived by computing a marginal least squares estimate with the observed data

$$
\beta^_{j}=(𝐱_{j}^{⊺}⁢𝐱_{j})^{-1}⁢𝐱_{j}^{⊺}⁢𝐲  ⟺  𝜷^=diag⁢(𝐗^{⊺}⁢𝐗)^{-1}⁢𝐗^{⊺}⁢𝐲.
$$

There are two key identities that may be taken from Equation 11. The first uses Equation 10 and is the approximate relationship (in expectation) between the moment matrix $𝐗^{⊺}⁢𝐲$ and the linear effect size estimates $𝜷^$:

$$
𝔼⁢[𝐗^{⊺}⁢𝐲]=𝔼⁢[diag⁢(𝐗^{⊺}⁢𝐗)⁢𝜷^]≈N⁢𝜷^.
$$

The second key point combines Equations 10 and 12 to describe the asymptotic relationship between the observed marginal GWAS summary statistics $𝜷^$ and the joint coefficient values $𝜷$ where (in expectation)

$$
E[\beta]=E[(X^{⊺}X)^{−1}X^{⊺}y]≈(NR)^{−1}N\beta^=R^{−1}\beta^.
$$

After some algebra, the above mirrors a high-dimensional regression model (in expectation) where $𝜷^=𝐑⁢𝜷$ with the estimated summary statistics as the response variables and the empirically estimated LD matrix acting as the design matrix (Hormozdiari et al., 2014; Hormozdiari et al., 2016; Zhang et al., 2018; Cheng et al., 2020; Demetci et al., 2021). Theoretically, the resulting coefficients output from this high-dimensional model are the desired true effect size estimates used to generate the phenotype of interest.

### Additive GWAS summary statistics with tagged interaction effects

When interactions contribute to the architecture of complex traits (i.e. $𝜽\neq𝟎$), the marginal GWAS summary statistics derived using least squares in Equation 11 will also explain non-additive variation when there is a nonzero correlation between genotypes and their interactions. To see this, we use the concept of ‘omitted variable bias’ (Barreto and Howland, 2005) where the fitted model aims to estimate the true additive coefficients $𝜷$ but does not account for contributions from the non-additive components which also contribute to trait architecture. In this case, we get the following

$$
\beta^=diag(X^{⊺}X)^{−1}X^{⊺}y=diag(X^{⊺}X)^{−1}X^{⊺}[X\beta+X_{D}\omega+W\theta+\epsilon].
$$

Since we assume that the genotypes are orthogonal to both the dominance effects in Equation 7, we know that $𝐗^{⊺}⁢𝐗_{D}=𝟎$. This simplifies the above to be the following

$$
\beta^=diag(X^{⊺}X)^{−1}X^{⊺}X\beta+diag(X^{⊺}X)^{−1}X^{⊺}W\theta+diag(X^{⊺}X)^{−1}X^{⊺}\epsilon
$$

where the matrix $𝐗^{⊺}⁢𝐖$(which we showed to be nonzero) can be interpreted as the sample correlation between individual-level genotypes and the cis-interactions between causal SNPs. By taking the expectation using Equations 10 and 12, we get the following alternative (approximate) relationship between the observed marginal GWAS summary statistics $𝜷^$ and the true coefficient values $𝜷$

$$
𝔼⁢[𝜷^]=𝐑⁢𝜷+𝐕⁢𝜽,
$$

which results from our initial assumption that the residuals are normally distributed with mean zero $𝔼⁢[𝜺]=𝟎$ in Equation 7. Here, we define $𝐕$ to represent a sample estimate of the correlation between the individual-level genotypes and the non-additive genetic interaction matrix such that $𝔼⁢[𝐗^{⊺}⁢𝐖]≈N⁢𝐕$. Similar to the LD matrix $𝐑$, the correlation matrix $𝐕$ is also assumed to be computed from reference panel data. Intuitively, when $𝜽\neq𝟎$ there is additional phenotypic variation contributed by pairwise interactions that can be explained by GWAS effect size estimates. Moreover, when $𝐕⁢𝜽=𝟎$, then the relationship in Equation 16 converges onto the conventional asymptotic assumption (in expectation) between GWAS summary statistics and the true additive coefficients in Equation 13; Hormozdiari et al., 2014; Hormozdiari et al., 2016; Zhang et al., 2018; Cheng et al., 2020; Demetci et al., 2021.

### Connection to quantitative genetics theory

The concept of additive genetic effects partially explaining non-additive variation has also described in classical quantitative genetics (Hill et al., 2008; Hivert et al., 2021; Mäki-Tanila and Hill, 2014). Consider an individual genotyped at $J$ loci each with major and minor alleles A and B, respectively. Let $p_{j}$ be the allele frequency of A at the $j$-th locus, $a_{j}$ denote the additive effect, and $[a⁢a]_{j⁢k}$ be the additive-by-additive (pairwise) interaction effect between loci $j$ and $k$, and $[a⁢a⁢a]_{j⁢k⁢l}$ represent a third order interaction between loci $j$, $k$, and $l$. For simplicity in presentation, assume that dominance only makes a small contribution to the genetic variance (Palmer et al., 2023; Pazokitoroudi et al., 2021; Zhu et al., 2015). The population mean is given as the following

$$
\mu=2\sumj=1Jp_{j}a_{j}+4\sumj=1J\sumk>jJp_{j}p_{k}[aa]_{jk}+8\sumj=1J\sumk>jJ\suml>k>jJp_{j}p_{k}p_{l}[aaa]_{jkl}+⋯
$$

We follow the assumption that the genetic variation in human complex traits can predominately be explained by additive effects, with the remainder variation being mostly explained by additive-by-additive effects (Weinreich et al., 2018; Jiang and Reif, 2015; Fisher, 1919; Lynch and Walsh, 1998). As a result, we will ignore the higher order interaction terms in Equation 17. Under Hardy-Weinberg equilibrium, we can find the average effect by taking the first derivative of the population mean with respect to the frequency of the increasing allele (Mäki-Tanila and Hill, 2014; Hivert et al., 2021). For the $j$-th SNP, the average effect (including terms up to second-order interaction) is given by the following

$$
η_{j}=\frac{1}{2}(\frac{∂\mu}{∂p_{j}})=a_{j}+2\sumk\neqjJp_{k}[aa]_{jk}+O([aaa]_{jkl})
$$

which notably contains both the additive effect and a summation of additive-by-additive interactions between pairs of loci. The additive genetic variance for the $j$-th SNP takes on the following form

$$
\sigma_{A}^{2}(j)=2p_{j}(1−p_{j})[a_{j}+2\sumk\neqjJp_{k}[aa]_{jk}]^{2}=2p_{j}(1−p_{j})[a_{j}^{2}+2a_{j}\sumk\neqjJp_{k}[aa]_{jk}+4(\sumk\neqjJp_{k}[aa]_{jk})^{2}]
$$

which is the product of the square of the average effect in Equation 18 and the heterozygosity at $j$-th locus $𝕍⁢[𝐱_{j}]=2⁢p_{j}⁢(1-p_{j})$ (again assuming that SNPs marginally follow a binomial distribution). The total additive variance is then obtained by summing over the $J$ loci such that $\sigma_{A}^{2}=\sum_{j}\sigma_{A}^{2}⁢(j)$ (Falconer and Mackay, 1983).

We can derive a parallel construction for additive genetic variance using the generative random effect model presented in Equation 7; Hivert et al., 2021. Here, we will leverage that with genotype data taken for $N$ individuals, $\sum_{i}x_{i⁢j}/N=2⁢p_{j}$. Ignoring the assumed small contributions from dominance effects, the population mean for a quantitative trait $𝐲$ can be written as the following

$$
\mu=\frac{1}{N}\sumi=1Ny_{i}=\frac{1}{N}\sumi=1N[b_{0}+\sumj=1Jx_{ij}\beta_{j}+\sumj=1J\sumk>jJx_{ij}x_{ik}\theta_{jk}+\epsilon_{i}]=b_{0}+2\sumj=1Jp_{j}\beta_{j}+4\sumj=1J\sumk>jJp_{j}p_{k}\theta_{jk}+\frac{1}{N}\sumi=1N\epsilon_{i}.
$$

To find the average effect for the $j$-th locus, we this time take the first derivative of the population mean in Equation 20 with respect to the allele frequency such that

$$
η_{j}=\frac{1}{2}(\frac{∂\mu}{∂p_{j}})=\beta_{j}+2\sumk\neqjJp_{k}\theta_{jk}
$$

which, similar to the theoretical form in quantitative genetics, also contains both the additive effect of the $j$-th SNP and additional terms encoding the interaction effect between the $j$-th SNP and all other variants in the data. Once again, under Hardy-Weinberg equilibrium, the additive variance for the $j$-th SNP is found as taking on the following form

$$
\sigma_{A}^{2}(j)=2p_{j}(1−p_{j})[\beta_{j}+2\sumk\neqjJp_{k}\theta_{jk}]^{2}=2p_{j}(1−p_{j})[\beta_{j}^{2}+2\beta_{j}\sumk\neqjJp_{k}\theta_{jk}+4(\sumk\neqjJp_{k}\theta_{jk})^{2}]
$$

where we can explicitly draw connections between the two frameworks by setting $\beta_{j}=a_{j}$ and $\theta_{j⁢k}=[a⁢a]_{j⁢k}$. Note that when there no non-additive effects (such that $𝜽=𝟎$), the above reduces to $\sigma_{A}^{2}=\sum_{j}2⁢p_{j}⁢(1-p_{j})⁢\beta_{j}^{2}$ which resembles the classical form for the additive genetic variance (Lynch and Walsh, 1998).

### Full derivation of interaction LD score regression

In order to derive the interaction LD score (i-LDSC) regression framework, recall that our goal is to recover missing heritability from GWAS summary statistics by incorporating an additional score that measures the non-additive genetic variation that is tagged by genotyped SNPs. To do this, we build upon the LD score regression framework and the LDSC software (Bulik-Sullivan et al., 2015b). Here, we assume nonzero contributions from cis-acting pairwise interaction effects in the generative model of complex traits as in Equation 16, and we use the observed least squares estimates from Equation 11 to compute chi-square statistics $χ_{j}^{2}=N⁢\beta^_{j}^{2}$ for every $j=1,…,J$ variant in the data. Taking the expectation of these statistics yields

$$
𝔼⁢[χ_{j}^{2}]=N⁢𝔼⁢[\beta^_{j}^{2}]=N⁢[𝕍⁢[\beta^_{j}]+(𝔼⁢[\beta^_{j}])^{2}].
$$

We can simplify Equation 23 in two steps. First, by combining the prior assumption in Equation 8 and the asymptotic approximation in Equation 16, we can show that marginal expectation (i.e. when not conditioning on the true coefficients) $𝔼⁢[\beta^_{j}]=0$ for all variants. Second, by conditioning on the generative model from Equation 7, we can use the law of total variance to simplify $𝕍⁢[\beta^_{j}]$ where

$$
V[\beta^_{j}]=E[V[\beta^_{j}|X]]+V[E[\beta^_{j}|X]]≈E[V[x_{j}^{⊺}y/N|X]]+0=E[\frac{1}{N^{2}}x_{j}^{⊺}{V[y|X]}x_{j}]=E[\frac{1}{N^{2}}x_{j}^{⊺}{\frac{\phi_{\beta}^{2}}{J}XX^{⊺}+\frac{\phi_{\omega}^{2}}{J}X_{D}X_{D}^{⊺}+\frac{\phi_{\theta}^{2}}{M}WW^{⊺}+(1−H^{2})}x_{j}]=E[\frac{1}{N^{2}}{\frac{\phi_{\beta}^{2}}{J}x_{j}^{⊺}XX^{⊺}x_{j}+\frac{\phi_{\omega}^{2}}{J}x_{j}^{⊺}X_{D}X_{D}^{⊺}x_{j}+\frac{\phi_{\theta}^{2}}{M}x_{j}^{⊺}WW^{⊺}x_{j}+N(1−H^{2})}]=E[\frac{1}{N^{2}}{\frac{\phi_{\beta}^{2}}{J}x_{j}^{⊺}XX^{⊺}x_{j}+\frac{\phi_{\theta}^{2}}{M}x_{j}^{⊺}WW^{⊺}x_{j}+N(1−H^{2})}]
$$

since $𝐱_{j}^{⊺}⁢𝐗_{D}=𝟎$. Using the same logic from the original LDSC regression framework (Bulik-Sullivan et al., 2015b), we can use Isserlis’ theorem Isserlis, 1918 to write the above in terms of more familiar quantities based on sample correlations

$$
\frac{1}{N^{2}}⁢𝐱_{j}^{⊺}⁢𝐗𝐗^{⊺}⁢𝐱_{j}=\sumk=1Jr~_{j⁢k}^{2},\frac{1}{N^{2}}⁢𝐱_{j}^{⊺}⁢𝐖𝐖^{⊺}⁢𝐱_{j}=\summ=1Mv~_{j⁢m}^{2}
$$

where $r~_{j⁢k}$ is used to denote the sample correlation between additively-coded genotypes at the $j$-th and $k$-th variants, and $v~_{j⁢m}$ is used to denote the sample correlation between the genotype of the $j$-th variant and the $m$-th genetic interaction on the phenotype of interest (again see Equation 16). Furthermore, we can use the delta method (only displaying terms up to $𝒪⁢(1/N^{2})$) to show that (in expectation)

$$
𝔼⁢[r~_{j⁢k}^{2}]≈r_{j⁢k}^{2}+(1-r_{j⁢k}^{2})/N,𝔼⁢[v~_{j⁢m}^{2}]≈v_{j⁢m}^{2}+(1-v_{j⁢m}^{2})/N.
$$

Next, we can then approximate the quantities in Equation 24 via the following

$$
𝔼⁢[\sumk=1Jr~_{j⁢k}^{2}]≈ℓ_{j}+(J-ℓ_{j})/N,𝔼⁢[\summ=1Mv~_{j⁢m}^{2}]≈f_{j}+(M-f_{j})/N
$$

where $ℓ_{j}$ is the corresponding LD score for the additive effect of the $j$-th variant and fj represents the “interaction” LD score between the $j$-th SNP and all other variants in the data set (Crawford et al., 2017), respectively. Altogether, this leads to the specification of the univariate framework with the $j$-th SNP

$$
𝔼⁢[χ_{j}^{2}]≈N⁢[(\frac{\phi_{\beta}^{2}}{J})⁢ℓ_{j}+(\frac{\phi_{\theta}^{2}}{M})⁢f_{j}+\frac{1}{N}⁢(1-H^{2})]=ℓ_{j}⁢\tau+f_{j}⁢ϑ+1
$$

where we define $\tau=N⁢\phi_{\beta}^{2}/J$ as estimates of the additive genetic signal, the coefficient $ϑ=N⁢\phi_{\theta}^{2}/M$ as an estimate of the proportion of phenotypic variation explained by tagged pairwise interaction effects, and 1 is the intercept meant to model the misestimation due to uncontrolled confounding effects (e.g. cryptic relatedness and population stratification). Similar to the original LDSC formulation, an intercept greater than one means significant bias. Note that the simplification for many of the terms above such as $(1-H^{2})/N≈1/N$ results from our assumption that the number of individuals in our study is large. For example, the sample sizes for each biobank-scale study considered in the analyses of this manuscript are at least on the order of $N\geq10^{4}$ observations (see Supplementary file 5). Altogether, we can jointly express Equation 27 in multivariate form as

$$
𝔼⁢[𝝌^{2}]≈ℓ⁢\tau+𝒇⁢ϑ+𝟏
$$

where $𝝌^{2}=(χ_{1}^{2},…,χ_{J}^{2})$ is a $J$-dimensional vector of chi-square summary statistics, and $ℓ=(ℓ_{1},…,ℓ_{J})$ and $𝒇=(f_{1},…,f_{J})$ are $J$-dimensional vectors of additive and cis-interaction LD scores, respectively. It is important to note that, while $𝝌^{2}$ must be recomputed for each trait of interest, both vectors $ℓ$ and $𝒇$ only need to be constructed once per reference panel or individual-level genotypes (see next section for efficient computational strategies).

To identify summary statistics that have significant tagged interaction effects, we test the null hypothesis $H_{0}:ϑ=0$. The i-LDSC software package implements the same model fitting strategy as LDSC. Here, we use weighted least squares to fit the joint regression in Equation 28 such that

$$
ϑ^=(𝒇^{⊺}⁢𝚿⁢𝒇)^{-1}⁢𝒇^{⊺}⁢𝚿⁢𝝌^{2},ψ_{j⁢j}=[ℓ_{j}⁢\tau^+f_{j}⁢ϑ^+1]^{-2}
$$

where $𝚿$ is a $J\timesJ$ diagonal weight matrix with nonzero elements set to values inversely proportional to the conditional variance $𝕍⁢[χ_{j}^{2}|ℓ_{j},f_{j}]=ψ_{j⁢j}^{-1}$ to adjust for both heteroscedasticity and over-estimation of the summary statistics for each SNP (Bulik-Sullivan et al., 2015b). Standard errors for each coefficient estimate are derived via a jackknife over blocks of SNPs in the data (Finucane et al., 2015), and we then use those standard errors to derive p-values with a two-sided test (i.e. testing the alternative hypothesis $H_{A}:ϑ\neq0$). It is worth noting that the block-jackknife approach tends to be conservative and yield larger standard errors for hypothesis testing (Efron, 1982). As an alternative, we could first run i-LDSC using the block-jackknife procedure over all traits in a study and then use the average of the standard errors to calculate the statistical significance of coefficient estimates; but we do not explore this strategy here and leave that for future work. The quantitative genetics expression for the additive variance $\sigma_{A}^{2}$ in Equation 22 is important because it represents the theoretical upper bound on the proportion of phenotypic variance that can be explained from GWAS summary statistics via i-LDSC. Using this relationship, we can write the following (approximate) inequality

$$
\tau^+ϑ^≲\sumj=1J2⁢p_{j}⁢(1-p_{j})⁢[\beta_{j}+2⁢\sumk\neqjJp_{k}⁢\theta_{j⁢k}]^{2}=\sigma_{A}^{2}.
$$

For all analyses in this paper, we estimate proportion of phenotypic variance explained by genetic effects using a sum of the coefficients $\tau^+ϑ^$ (i.e. the estimated additive component plus the additional genetic variance explained by the tagged pairwise interaction effects).

### Efficient computation of cis-interaction LD scores

In practice, cis-interaction LD scores in i-LDSC can be computed efficiently through realizing two key opportunities for optimization. First, given $J$ SNPs, the full matrix of genome-wide interaction effects $𝐖$ contains on the order of $J⁢(J-1)/2$ total pairwise interactions. However, to compute the cis-interaction score for each SNP, we simply can replace the full $𝐖$ matrix with a subsetted matrix $𝐖_{j}$ which includes only interactions involving the $j$-th SNP. Analogous to the original LDSC formulation (Bulik-Sullivan et al., 2015b), we consider only interactive SNPs within a cis-window proximal to the focal $j$-th SNP for which we are computing the i-LDSC score. In the original LDSC model, this is based on the observation that LD decays outside of a window of 1 centimorgan (cM) (Bulik-Sullivan et al., 2015b); therefore, SNPs outside the 1 cM window centered on the $j$-th SNP $j$ will not significantly contribute to its LD score. The second opportunity for optimization comes from the fact that the matrix of interaction effects for any focal SNP, $𝐖_{j}$, does not need to be explicitly generated. Referencing Equation 24, the i-LDSC scores are defined as $𝐱_{j}^{⊺}⁢𝐖_{j}⁢𝐖_{j}^{⊺}⁢𝐱_{j}/N^{2}$. This can be re-written as $𝐱_{j}^{⊺}⁢(𝐃_{j}⁢𝐗^{(j)})⁢(𝐃_{j}⁢𝐗^{(j)})^{⊺}⁢𝐱_{j}$, where $𝐃_{j}=diag⁢(𝐱_{j})$ is a diagonal matrix with the $j$-th genotype as its nonzero elements (Crawford et al., 2017) and $𝐗^{(j)}$ denotes the subset SNPs within a cis-window proximal to the focal $j$-th SNP. This means that the i-LDSC score for the $j$-th SNP can be simply computed as the following

$$
f_{j}≈\frac{1}{N^{2}}⁢(𝐱_{j}^{⊺})^{2}⁢𝐗^{(j)}⁢𝐗^{(j)⊺}⁢(𝐱_{j})^{2}.
$$

With these simplifications, the computational complexity of generating i-LDSC scores reduces to that of computing LD scores — modulo a vector-by-vector Hadamard product which, for each SNP, is constant factor of $N$ (i.e. the number of genotyped individuals).

### Coefficient estimates as determined by cis-interaction window size

When computing cis-interaction LD scores, the most important decision is choosing the number of interacting SNPs to include in $𝐗^{(j)}$ (or equivalently $𝐖_{j}$ for each $j$-th focal SNP in the calculation of fj in Equation 31). The i-LDSC framework considers different estimating windows to account for our lack of a priori knowledge about the ‘correct’ non-additive genetic architecture of traits. Theoretically, one could follow previous work Guan and Stephens, 2011; Carbonetto and Stephens, 2012; Zhou et al., 2013; Zhu and Stephens, 2017; Zhu and Stephens, 2018; Demetci et al., 2021 by considering an $L$-valued grid of possible SNP interaction window sizes. After fitting a series of i-LDSC regressions with cis-interaction LD scores $𝒇^{(l)}$ generated under the $L$-different window sizes, we could compute normalized importance weights using their maximized likelihoods via the following

$$
\pi^{(l)}=\frac{ℒ⁢(ℓ,𝒇^{(l)};𝜷^)}{\sum_{l^{′}}ℒ⁢(ℓ,𝒇^{(l^{′})};𝜷^)},\suml=1L\pi^{(l)}=1.
$$

As a final step in the model fitting procedure, we could then compute averaged estimates of the coefficients $\tau$ and $ϑ$ by marginalizing (or averaging) over the $L$-different grid combinations of estimating windows

$$
\tau^=\suml=1L\pi^{(l)}⁢\tau^^{(l)},ϑ^=\suml=1L\pi^{(l)}⁢ϑ^^{(l)}.
$$

This final step can be viewed as an analogy to model averaging where marginal estimates are computed via a weighted average using the importance weights (Hoeting et al., 1999). In the current study, we explore the utility of cis-interaction LD scores generated with different window sizes ± 5, ± 10, ± 25, and ± 50 SNPs around each $j$-th focal SNP. In practice, we find that cis-interaction LD scores that are calculated using larger windows lead to the most robust estimates of heritability while also not over representing the total phenotypic variation explained by tagged non-additive genetic effects (see Figure 3—figure supplement 1). Therefore, unless otherwise stated, we use cis-interaction LD scores calculated with a ± 50 SNP interaction window for all simulations and real data analyses conducted in this work. For a direct comparison between choosing a single window size versus the model averaging strategy described above, see Supplementary files 1 and 2.

### Relationship between minor allele frequency and effect size

The LDSC software computes LD scores using annotations over equally spaced minor allele frequency (MAF) bins. These annotations enable the per trait relationship between the MAF and the effect size of each variant in the genome to vary based on the discrete category (or MAF bin) it is placed into. This additional flexibility is intended to help LDSC be more robust when estimating heritability. The relationship between MAF and effect size is already implicitly encoded in the LDSC formulation since we assume genotypes are normalized. When normalizing by the variance of each SNP (or equivalently its MAF), we make the assumption that rare variants inherently have larger effect sizes. There exists a true functional relationship between MAF and effect size which is likely to be somewhere between the two extremes of (i) normalizing each SNP by its MAF and (ii) allowing the variance per SNP to be dictated by its MAF.

Recent approaches have proposed using a single parameter $\alpha$ to better represent the nonlinear relationship between MAF and variant effect size. The main idea is that this $\alpha$ not only provides the same additional flexibility to LDSC as the MAF-based discrete annotations, but it also empirically yields even more precise heritability estimates (Zabad et al., 2021). Namely, we use

$$
ℓ_{j}⁢(c):=\sumkL_{j⁢k}⁢(\alpha)⁢a_{c}⁢(k),L_{j⁢k}⁢(\alpha)=r_{j⁢k}^{2}⁢𝕍⁢[𝐱_{k}]^{1-\alpha}
$$

where $a_{c}⁢(k)$ is the annotation value for the $c$-th categorical bin. The α parameter is unknown in practice and needs to be estimated for any given trait. While standard ranges for α can be used for heritability estimates, we use a restricted maximum likelihood (REML) based method which was recently developed (Schoech et al., 2019).

In the i-LDSC software, we use this α construction to handle the relationship between MAF and variant effect size for two specific reasons. First, by constructing the LD scores using α, we more accurately capture the variation in chi-square test statistics due to additive effects (Zabad et al., 2021). Second, we note that there is correlation between MAF and (i) LD scores, (ii) cis-interaction LD scores, and (iii) trait architecture. To that end, if we do not properly condition on MAF, there becomes additional bias, and we may falsely attribute some amount of variation in the chi-square test statistics to LD or the tagged interaction effects. Therefore, in our formulation, we include an α term on the LD scores to condition on this effect. We demonstrate in simulations that this removes the bias introduced by the relationship between MAF and trait architecture, and it mitigates potential inflation of type I error rates in the i-LDSC test.

### Estimation of allele frequency parameters

In the main text, we analyzed 25 complex traits in both the UK Biobank and BioBank Japan data sets. In order to account for minor allele frequency (MAF) dependent trait architecture, we calculated $\alpha$ values for each trait that had not been analyzed by previous studies (Schoech et al., 2019). The α estimates for each of the 25 traits analyzed in this study are shown in Supplementary file 4. Intuitively, $\alpha$ parameterizes the weighting of the effects of each individual variant given its frequency in the study cohort and can take on values in the range of [–1,0]. More negative values of $\alpha$ indicate that lower frequency variants contribute more to the observed variation in a trait of interest, whereas values of α closer to zero indicate that common variants contribute a greater amount of variation to observed trait values.

We took α values for 11 traits (again see Supplementary file 4) that had previously been calculated from Schoech et al. For the remaining 14 traits analyzed in this study, we followed the estimation protocol described in the same manuscript. Specifically, using the variants passing the quality control step in our pipeline for 25,000 randomly selected individuals in the UK Biobank cohort, we constructed MAF-dependent genetic relatedness matrices for values of $\alpha={-1,-0.95,-0.9,…,0}$ using the GRM-MAF-LD software (Schoech, 2018). We then used the GCTA software (Yang et al., 2011) to obtain heritability and likelihood estimates using REML for each $\alpha$-trait pairing. We then fit a trait-specific profile likelihood across the range of α values and estimate the maximum likelihood value of $\alpha$ using a natural cubic spline.

### Simulation studies

We used a simulation scheme to generate synthetic quantitative traits and SNP-level summary statistics under multiple genetic architectures using real genome-wide data from individuals of self-identified European ancestry in the UK Biobank. Here, we consider phenotypes that have some combination of additive effects, cis-acting interactions, and a third source of genetic variance stemming from either gene-by-environment (G×E) or gene-by-ancestry (G×Ancestry) effects. For each scenario, we select some set of SNPs to be causal and assume that complex traits are generated via the following general linear model

$$
𝐲=𝐗⁢𝜷+𝐖⁢𝜽+𝐙⁢𝜸+𝜺,𝜺∼𝒩⁢(𝟎,\delta^{2}⁢𝐈),
$$

where $𝐲$ is an $N$-dimensional vector containing all the phenotypes; $𝐗$ is an $N\timesJ$ matrix of genotypes encoded as 0, 1, or 2 copies of a reference allele; β is a $J$-dimensional vector of additive effect sizes for each SNP; $𝐖$ is an $N\timesM$ matrix which holds all pairwise interactions between the randomly selected subset of the interacting SNPs with corresponding effects θ is an $N\timesK$ matrix of either G×E or G×Ancestry interactions with coefficients $𝜸$; and $𝜺$ is an $N$-dimensional vector of environmental noise. The phenotypic variation is assumed to be $𝕍⁢[𝐲]=1$. All additive and interaction effect sizes for SNPs are randomly drawn from independent standard Gaussian distributions and then rescaled so that they explain a fixed proportion of the phenotypic variance $𝕍⁢[𝐗⁢𝜷]+𝕍⁢[𝐖⁢𝜽]+𝕍⁢[𝐙⁢𝜸]=H^{2}$. Note that we do not assume any specific correlation structure between the effect sizes β, θ, and $𝜸$. We then rescale the random error term such that $𝕍⁢[𝜺]=(1-H^{2})$. In the main text, we compare the traditional LDSC to its direct extension in i-LDSC. For each method, GWAS summary statistics are computed by fitting a single-SNP univariate linear model via least squares where $\beta^_{j}=(𝐱_{j}^{⊺}⁢𝐱_{j})^{-1}⁢𝐱_{j}^{⊺}⁢𝐲$ for every $j=1,…,J$ SNP in the data. These effect size estimates are used to derive the chi-square test statistics $χ_{j}^{2}=N⁢\beta^_{j}^{2}$. We implement both LDSC and i-LDSC with the LD matrix $𝐑=𝐗^{⊺}⁢𝐗/N$ and the cis-interaction correlation matrix $𝐕=𝐗^{⊺}⁢𝐖/N$ being computed using a reference panel of 489 individuals from the European superpopulation (EUR) of the 1000 Genomes Project (https://mathgen.stats.ox.ac.uk/impute/data_download_1000G_phase1_integrated.html). The resulting matrices $𝐑$ and $𝐕$ are used to compute the additive and cis-interaction LD scores, respectively.

#### Polygenic simulations with cis-interactions

In our first set of simulations, we consider phenotypes with polygenic architectures that are made up of only additive and cis-acting SNP-by-SNP interactions. Here, we begin by assuming that every SNP in the genome has at least a small additive effect on the traits of interest. Next, when generating synthetic traits, we assume that the additive effects make up $ρ%$ of the heritability while the pairwise interactions make up the remaining $(1-ρ)%$. Alternatively, the proportion of the heritability explained by additivity is said to be $𝕍⁢[𝐗⁢𝜷]=ρ⁢H^{2}$, while the proportion detailed by interactions is given as $𝕍⁢[𝐖⁢𝜽]=(1-ρ)⁢H^{2}$. The setting of $ρ=1$ represents the limiting null case for i-LDSC where the variation of a trait is driven by solely additive effects. Here, we use the same simulation strategy used in Crawford et al. where we divide the causal cis-interaction variants into two groups. One may view the SNPs in group #1 as being the ‘hubs’ of an interaction map. SNPs in group #2 are selected to be variants within some kilobase (kb) window around each SNP in group #1. Given different parameters for the generative model in Equation 35, we simulate data mirroring a wide range of genetic architectures by toggling the following parameters:

All figures and tables show the mean performances (and standard errors) across 100 simulated replicates.

#### Polygenic simulations with gene-by-environmental effects

In our second set of simulations, we continue to consider phenotypes with polygenic architectures that are made up of only additive and cis-acting SNP-by-SNP interactions; however, now we also consider each trait to have contributions stemming from nonzero G×E effects. Here, both the additive and cis-interaction effects are simulated in the same way as previously described where, for the two groups of interacting variants, 10% of SNPs were selected to be in group #1 and we chose ±10 kb windows to assign SNPs to group #2. To create G×E effects, we follow a simulation strategy implemented by Zhu et al. and split our sample population in half to emulate two subsets of individuals coming from different environments. We randomly draw the effect sizes for the first environment from a standard Gaussian distribution which we denote as $𝜸_{1}$. We then selected an amplification coefficient $w$ and set the effect sizes of the G×E interactions in the second environment to be a scaled version of the first environment effects where $𝜸_{2}=w⁢𝜸_{1}$. In this paper, we generate traits with heritability $H^{2}={0.3,0.6}$ and amplification coefficients set to $w=[1.1,1.2,…,2]$. For the first set of simulations, we hold the proportion of phenotypic variation explained by the different genetic components constant by fixing:

where $𝐙=[𝐗_{1},𝐗_{2}]$ is the set of genotypes split according to environment and $𝜸=[𝜸_{1},𝜸_{2}]$. To test the sensitivity of the cis-interaction LD scores to other sources of non-additive variation, we also repeated the same simulations where there were only additive and G×E effects contributing equally to trait architecture:

Again all figures show the mean performances (and standard errors) across 100 simulated replicates.

#### Polygenic simulations with gene-by-ancestry effects

In our third set of simulations, we consider phenotypes with polygenic architectures that are made up of additive, cis-interactions, and G×Ancestry effects. Here, we follow Sohail et al. and first run a matrix decomposition on the individual-level genotype matrix $𝐗=𝐔𝐐^{⊺}$ where $𝐔$ is a unitary $N\timesK$ score matrix, $𝐐$ is a $K\timesJ$ loadings matrix, and $K$ represents the number of (predetermined) principal components (PCs). To generate G×Ancestry interactions, we then create the matrix $𝐙_{k}=𝐗𝐪_{k}$ where $𝐪_{k}$ is a $J$-dimensional vector of SNP loadings for the $k$-th principal component. In this paper, we generate traits with heritability $H^{2}={0.3,0.6}$ and interaction effects taken over $k=1,…,10$ principal components. For the first set of simulations, we hold the proportion of phenotypic variation explained by the different genetic components constant by fixing:

To test the sensitivity of the cis-interaction LD scores to other sources of non-additive variation, we also repeated the same simulations where there were only additive and G×E effects contributing equally to trait architecture:

Note that, for each case, we generate summary statistics in two ways: (i) including the top 10 PCs as covariates in the marginal linear model to correct for population structure and (ii) not correcting for any population structure. Again all figures show the mean performances (and standard errors) across 100 simulated replicates.

#### Sparse simulation study design with additive effects

In this set of simulations, we consider phenotypes with sparse architectures (Zhou et al., 2013). Here, traits were simulated with solely additive effects such that $𝕍⁢[𝐗⁢𝜷]=H^{2}$, but this time only variants with the top or bottom ${1,5,10,25,50,100}$ percentile of LD scores were given nonzero coefficients (a similar simulation approach was also previously implemented in both Bulik-Sullivan et al., 2015b and Lee et al., 2018). We once again generate traits with heritability $H^{2}={0.3,0.6}$. We also want to note that, in each of these specific analyses, synthetic trait architectures were generated using all UK Biobank genotyped variants that passed initial preprocessing and quality control (see next section). Since not all of these SNPs are HapMap3 SNPs, some variants were omitted from the LDSC and i-LDSC regression. Overall, as shown in the main text with results taken over 100 replicates, breaking the assumed relationship between LD scores and chi-squared statistics (i.e. that they are generally positively correlated) led to unbounded estimates of heritability in all but the (more polygenic) scenario when 100% of SNPs contributed to phenotypic variation.

#### Polygenic simulations with unobserved additive effects

In this next set of simulations, we consider another extension of the polygenic case where a portion of the variants with only additive genetic effects are not observed due ascertainment or other quality control procedures. It was found in Hemani et al., 2014. that an initial set of signals pointing towards evidence of genetic interactions were actually better explained using linear models of unobserved variants in the same haplotype. Here, we test whether the i-LDSC framework is prone to overestimate the non-additive genetic variance when additive effects in the same haplotype are not included in the model. In each simulation, we generated haplotypes that each contain 5000 variants. Next, we select either a single causal variant with only an additive effect or a set of ten causal variants with only additive effects — each having an MAF that is randomly selected between: (i) (0.01, 0.1), (ii) (0.1, 0.2), (iii) (0.2, 0.3), (iv) (0.3, 0.4), and (v) (0.4, 0.5). The corresponding additive effect size for each causal variant across the haplotype is simulated inversely proportional with its MAF. For this analysis, we measure the difference between i-LDSC coefficient estimates when every variant is included in the model versus when the haplotype causal variants are omitted for two different trait architectures with broad-sense heritability set to $H^{2}=$ 0.3 and 0.6. Differences in the component estimates between the observed and unobserved single additive variant models are shown in Figure 3—figure supplement 9A and B. Similar estimates when the larger number of ten additive variants are unobserved in each haplotype are shown in Figure 3—figure supplement 9C and D. If i-LDSC was prone to overestimating the non-additive effects, then the omission of the variants with only significant additive effects would lead to increased estimates of $\tau$ and $ϑ$. However, across a range of generative broad-sense heritabilities and haplotype architectures we observe that estimates of $\tau$ and $ϑ$ are robust. Intuitively, this is likely due to the fact that these simulations were done under polygenic trait architectures where, as a result, the omission of a few causal variants with small marginal effect sizes has little impact on the ability to estimate genetic variance.

#### Polygenic simulations with unobserved interaction effects

In this set of simulations, we extend the polygenic case to a setting where a portion of the variants involved in genetic interactions are unobserved. Similar to the case with unobserved additive effects, the purpose of these simulations is to assess whether the i-LDSC framework is prone to false discovery of non-additive genetic variance when causal interacting SNPs are not included during the estimation of GWAS summary statistics. In each simulation, we generated haplotypes that each contain 5000 variants. Traits were simulated using the generative model in Equation (35) with both additive and interaction effects such that $𝕍⁢[𝐗⁢𝜷]+𝕍⁢[𝐖⁢𝜽]=H^{2}$. Here, every SNP in the genome had at least a small additive effect with a corresponding effect size that was drawn to be inversely proportional to its MAF. Only 1% or 5% of variants within each haplotype had causal non-zero interaction effects. However, when running i-LDSC, only a percentage of the interacting SNPs {1%, 5%, 10%, 25% or 50%} were included in the estimation of $ϑ^$. We once again generate traits with heritability $H^{2}={0.3,0.6}$ such that the proportion of genetic variance explained by additive effects was equal to $ρ={0.5,0.8}$. As with the other simulation scenarios, all synthetic traits were generated using UK Biobank genotyped variants that passed initial preprocessing and quality control (see next section). Since not all of these SNPs are HapMap3 SNPs, some variants were omitted from the i-LDSC regression analyses. Overall, as discussed in the main text with results taken over 100 replicates, i-LDSC underestimated values of $ϑ^$ when there were unobserved interacting variants (see Figure 3—figure supplements 10 and 11). As expected, estimates of the additive variance component $\tau^$, on the other hand, were not affected.

#### Polygenic simulations with correlated additive and interaction effects

In our last set of simulations, we sought out to better understand how the relationship between the additive ($\beta$) and interaction ($\theta$) coefficients in the generative model of complex traits could potentially bias the additive and non-additive variance component estimates in LDSC and i-LDSC. To that end, we performed a set of simulations where we varied the correlation between the set of effects. Specifically, we first drew a set of additive effect sizes for each variant using the MAF-dependent procedure described above (i.e. $\alpha=-1$). We next selected a subset of the causal variants to be in cis-interactions. Here, we set the interaction effect sizes to covary with the additive effect size vector in two different ways. In the first, we simply drew the additive and interaction effect sizes from a multivariate normal such that their correlation was equal to $r={-1,-0.8,-0.6,…,0.6,0.8,1}$ (see Figure 3—figure supplement 12). In the second, we simply amplified the interaction effects to be a linear function $\theta=\beta\timesq$ (Figure 3—figure supplement 13A and C) or a squared function $\theta=\beta^{2⁢q}$ (Figure 3—figure supplement 13B and D) of the additive effects where $q={0.1,0.2,…,0.9,1}$. While testing 100 replicates for each value of $q$, we observed that the mean estimate of genetic variance had a slight upward bias as the correlation between the additive and interaction effect sizes in the generative model increased; however, the distribution of these bias estimates covered zero in the first and third quartiles of all results. We evaluated this behavior for multiple broad-sense heritability levels  $H^{2}$ = 0.3 and 0.6.

### Preprocessing for the UK Biobank and BioBank Japan

In order to apply the i-LDSC framework to 25 continuous traits the UK Biobank (Bycroft et al., 2018), we first downloaded genotype data for 488,377 individuals in the UK Biobank using the ukbgene tool (https://biobank.ctsu.ox.ac.uk/crystal/download.cgi) and converted the genotypes using the provided ukbconv tool (https://biobank.ctsu.ox.ac.uk/crystal/refer.cgi?id=149660). Phenotype data for the 25 continuous traits were also downloaded for those same individuals using the ukbgene tool. Individuals identified by the UK Biobank as having high heterozygosity, excessive relatedness, or aneuploidy were removed (1,550 individuals). After separating individuals into self-identified ancestral cohorts using data field 21000, unrelated individuals were selected by randomly choosing an individual from each pair of related individuals. This resulted in $N=$ 349,469 white British individuals to be included in our analysis. We downloaded imputed SNP data from the UK Biobank for all remaining individuals and removed SNPs with an information score below 0.8. Information scores for each SNP are provided by the UK Biobank (http://biobank.ctsu.ox.ac.uk/crystal/refer.cgi?id=1967).

Quality control for the remaining genotyped and imputed variants was then performed on each cohort separately using the following steps. All structural variants were first removed, leaving only single nucleotide polymorphisms (SNPs) in the genotype data. Next, all AT/CG SNPs were removed to avoid possible confounding due to sequencing errors. Then, SNPs with minor allele frequency less than 1% were removed using the PLINK 2.0 (Chang et al., 2015) command --maf 0.01. We then removed all SNPs found to be out of Hardy-Weinberg equilibrium, using the PLINK --hwe 0.000001 flag to remove all SNPs with a Fisher’s exact test p-value $>10^{−6}$. Finally, all SNPs with missingness greater than 1% were removed using the PLINK --mind 0.01 flag.

We then performed a genome-wide association study (GWAS) for each trait in the UK Biobank on the remaining 8,981,412 SNPs. SNP-level GWAS effect sizes were calculated using PLINK and the --glm flag (Chang et al., 2015). Age, sex, and the first 20 principal components were included as covariates for all traits analyzed (Sohail et al., 2019). Principal component analysis was performed using FlashPCA 2.0 (Abraham et al., 2017) on a set of independent markers derived separately for each ancestry cohort using the PLINK command --indep-pairwise 100 10 0.1. Using the parameters --indep-pairwise removes all SNPs that have a pairwise correlation above 0.1 within a 100 SNP window, then slides forward in increments of ten SNPs genome-wide.

In order to analyze data from BioBank Japan, we downloaded publicly available GWAS summary statistics for the 25 traits listed in Supplementary file 5 from https://pheweb.jp/downloads. Summary statistics used age, sex, and the first ten principal components as confounders in the initial GWAS study. We then used individuals from the East Asian (EAS) superpopulation from the 1000 Genomes Project Phase 3 to calculate paired LDSC and i-LDSC scores from a reference panel. We pruned the reference panel using the PLINK command --indep-pairwise 100 10 0.5 to limit the computational time of calculating scores (Chang et al., 2015). This resulted in reference scores for 1,164,666 SNPs that are included on the i-LDSC GitHub repository (https://github.com/lcrawlab/i-LDSC). Using summary statistics from BioBank Japan, with scores calculated from the EAS population in the 1000 Genomes, we obtained i-LDSC heritability estimates for each of the 25 traits.
