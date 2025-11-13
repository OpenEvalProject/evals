# Efficient estimation for large-scale linkage disequilibrium patterns of the human genome

## Authors

- Xin Huang<sup>1</sup>
- Tian-Neng Zhu<sup>1</sup> ([ORCID: 0009-0007-7507-4521](https://orcid.org/0009-0007-7507-4521))
- Ying-Chao Liu<sup>1</sup>
- Guo-An Qi<sup>1</sup> ([ORCID: 0000-0002-2412-3932](https://orcid.org/0000-0002-2412-3932))
- Jian-Nan Zhang<sup>5</sup>
- Guo-Bo Chen<sup>2</sup> ([ORCID: 0000-0001-5475-8237](https://orcid.org/0000-0001-5475-8237)) †

### Affiliations

1. Institute of Bioinformatics, Zhejiang University Hangzhou China ([ROR:00a2xv884](https://ror.org/00a2xv884))
2. Center for General Practice Medicine, Department of General Practice Medicine, Zhejiang Provincial People’s Hospital, People’s Hospital of Hangzhou Medical College Hangzhou China ([ROR:03k14e164](https://ror.org/03k14e164))
3. Center for Reproductive Medicine, Department of Genetic and Genomic Medicine, and Clinical Research Institute, Zhejiang Provincial People’s Hospital, People’s Hospital of Hangzhou Medical College Zhejiang China ([ROR:03k14e164](https://ror.org/03k14e164))
4. Hainan Institute of Zhejiang University Hainan China ([ROR:00a2xv884](https://ror.org/00a2xv884))
5. Alibaba Group Hangzhou China ([ROR:00k642b80](https://ror.org/00k642b80))
6. Key Laboratory of Endocrine Gland Diseases of Zhejiang Province Hangzhou China

† Corresponding author

## Abstract

In this study, we proposed an efficient algorithm (X-LD) for estimating linkage disequilibrium (LD) patterns for a genomic grid, which can be of inter-chromosomal scale or of small segments. Compared with conventional methods, the proposed method was significantly faster, dropped from O(nm2) to O(n2m)—n the sample size and m the number of SNPs, and consequently we were permitted to explore in depth unknown or reveal long-anticipated LD features of the human genome. Having applied the algorithm for 1000 Genome Project (1KG), we found (1) the extended LD, driven by population structure, universally existed, and the strength of inter-chromosomal LD was about 10% of their respective intra-chromosomal LD in relatively homogeneous cohorts, such as FIN, and to nearly 56% in admixed cohort, such as ASW. (2) After splitting each chromosome into upmost of more than a half million grids, we elucidated the LD of the HLA region was nearly 42 folders higher than chromosome 6 in CEU and 11.58 in ASW; on chromosome 11, we observed that the LD of its centromere was nearly 94.05 folders higher than chromosome 11 in YRI and 42.73 in ASW. (3) We uncovered the long-anticipated inversely proportional linear relationship between the length of a chromosome and the strength of chromosomal LD, and their Pearson’s correlation was on average over 0.80 for 26 1KG cohorts. However, this linear norm was so far perturbed by chromosome 11 given its more completely sequenced centromere region. Uniquely chromosome 8 of ASW was found most deviated from the linear norm than any other autosomes. The proposed algorithm has been realized in C++ (called X-LD) and is available at https://github.com/gc5k/gear2, and can be applied to explore LD features in any sequenced populations.

## Introduction

Linkage disequilibrium (LD) is the association for a pair of loci and the metric of LD serves as the basis for developing genetic applications in agriculture, evolutionary biology, and biomedical research (Weir, 2008; Hill and Robertson, 1966). The structure of LD of the human genome is shaped by many factors, mutation, recombination, population demography, epistatic fitness, and completeness of genomic data itself (Myers et al., 2005; Nei and Li, 1973; Ardlie et al., 2002). Due to its overwhelming cost, LD structure investigation is often compromised to a small genomic region (Chang et al., 2015; Theodoris et al., 2021), and their typical LD structure is as illustrated for a small segment (Barrett et al., 2005). Now, given the availability of large-scale genomic data, such as millions of single-nucleotide polymorphisms (SNPs), the large-scale LD patterns of the human genome play crucial roles in determining genomics studies, and many theories and useful algorithms upon large-scale LD structure, from genome-wide association studies, polygenic risk prediction for complex diseases, and choice for reference panels for genotype imputation (Vilhjálmsson et al., 2015; Yang and Zhou, 2020; Bulik-Sullivan et al., 2015; Yang et al., 2011; Das et al., 2016).

However, there are impediments, largely due to intensified computational cost, in both investigating large-scale LD and providing high-resolution illustrations for their details. If we consider a genomic grid that consists of $m^{2}$ SNP pairs, given a sample of $n$ individuals and $m$ SNPs ($n≪m$)—typically as observed in 1000 Genomes Project (1KG) (Lowy et al., 2019), its benchmark computational time cost for calculating all pairwise LD is $O(nm^{2})$, a burden that quickly drains computational resources given the volume of the genomic data. In practice, it is of interest to know the mean LD of the $m_{i}^{2}$ SNP pairs for a genomic grid, which covers $m_{i}\timesm_{j}$ SNP pairs. Upon how a genomic grid is defined, a genomic grid consequently can consist of (1) the whole genome-wide $m^{2}$ SNP pairs, and we denote their mean LD as $l_{g}$ ; (2) the intra-chromosomal mean LD for the ith chromosome of $m_{i}^{2}$ SNP pairs, and denote as $l_{i}$ ; and (3) the inter-chromosomal mean LD ith and jth chromosomal $m_{i}m_{j}$ SNP pairs, and denoted as $l_{i⋅j}$ .

In this study, we propose an efficient algorithm that can estimate $l_{g}$ , $l_{i}$ , and $l_{i⋅j}$ , the computational time of which can be reduced from $O(nm_{i}^{2})$ to $O(n^{2}m_{i})$ for $l_{i}$ and $O(nm_{i}m_{j})$ to $O(n^{2}m_{i}+n^{2}m_{j})$ for $l_{i⋅j}$ . The rationale of the proposed method relies on the connection between the genetic relationship matrix (GRM) and LD (Chen, 2014; Goddard, 2009), and in this study a more general transformation from GRM to LD can be established via Isserlis’s theorem (Isserlis, 1918; Zhou, 2017). The statistical properties, such as sampling variance, of the estimated LD have been derived too.

The proposed method can be analogously considered a more powerful realization for Haploview (Barrett et al., 2005), but additional utility can be derived to bring out an unprecedented survey of LD patterns of the human genome. As demonstrated in 1KG, we consequently investigate how biological factors such as population structure, admixture, or variable local recombination rates can shape large-scale LD patterns of the human genomes.

The proposed algorithm has been realized in C++ and is available at https://github.com/gc5k/gear2, (copy archived at Chen, 2023). As tested, the software could handle sample sizes as large as 10,000 individuals.

## Methods

### The overall rationale for large-scale LD analysis

We assume LD for a pair of biallelic loci is measured by squared Pearson’s correlation, $ρ_{l_{1}l_{2}}^{2}=\frac{D_{l_{1}l_{2}}^{2}}{p_{l_{1}}q_{l_{1}}p_{l_{2}}q_{l_{2}}}$ , in which $D_{l_{1}l_{2}}$ the LD of loci $l_{1}$ and $l_{2}$ , $p_{.}$ and $q_{.}$ the reference and the alternative allele frequencies. If we consider the averaged LD for a genomic grid over $m_{i}^{2}$ SNP pairs, the conventional estimator is $l^_{i}=\frac{1}{m_{i}^{2}}\suml_{1},l_{2}m_{i}ρ_{l_{1}l_{2}}^{2}$ , and, if we consider the averaged LD for $m_{i}$ and $m_{j}$ SNP pairs between two genomic segments, then $l^_{i⋅j}=\frac{1}{m_{i}m_{j}}\suml_{1},l_{2}m_{i},m_{j}ρ_{l_{1}l_{2}}^{2}$ . Now let us consider the 22 human autosomes (Figure 1A). We naturally partition the genome into $C=22$ blocks, and its genomic LD, denoted as $l_{g},$ can be expressed as

$$
l_{g}=\frac{1}{m^{2}}\suml_{1},l_{2}mρ_{l_{1}l_{2}}^{2}=\frac{1}{m^{2}}(\sumiC(\suml_{1},l_{2}m_{i}ρ_{l_{1}l_{2}}^{2})+\sumi\neqjC(\suml_{1}m_{i}\suml_{2}m_{j}ρ_{l_{1}l_{2}}^{2}))=\sumiC\frac{m_{i}^{2}}{m^{2}}l_{i}+\sumi\neqjC\frac{m_{i}m_{j}}{m^{2}}l_{i⋅j}
$$

![Figure 1.](https://cdn.elifesciences.org/articles/90636/elife-90636-fig1-v2.jpg)

**Figure 1.:** (A) The 22 human autosomes have consequently 22 $l^_{i}$ and 231 $l^_{i⋅j}$ , without (left) and with (right) scaling transformation; Scaling transformation is given in Equation 8. (B) If zoom into chromosome 2 of 420,946 single-nucleotide polymorphisms (SNPs), a chromosome of relative neutrality is expected to have self-similarity structure that harbors many approximately strong $l^_{u}$ along the diagonal, and relatively weak $l^_{uv}$ off-diagonally. Here chromosome 2 of CONVERGE has been split into 1000 blocks and yielded 1000 $l^_{u}$ LD grids, and 499,500 $l^_{uv}$ LD grids. (C) An illustration of the construction process for the LD-decay regression model.

So we can decompose $l_{g}$ into $C$$l_{i}$ and $\frac{C(C−1)}{2}$ unique $l_{i⋅j}$ . Obviously, Equation 1 can be also expressed in the context of a single chromosome $l_{i}=\frac{1}{\beta_{i}^{2}}(\sumu\beta_{i}l_{u}+\sumu\neqv\beta_{i}l_{uv})$, in which $\beta_{i}=\frac{m_{i}}{m}$ the number of SNP segments, each of which has $m$ SNPs. Geometrically it leads to $\beta_{i}$ diagonal grids and $\frac{\beta_{i}\beta_{i}-1}{2}$ unique off-diagonal grids (Figure 1B).

### LD-decay regression

As human genome can be boiled down to small LD blocks by genome-widely spread recombination hotspots (Hinch et al., 2019; Li et al., 2022), mechanically there is self-similarity for each chromosome that the relatively strong $l_{i}$ for juxtaposed grids along the diagonal but weak $l_{i⋅j}$ for grids slightly off-diagonal. So, for a chromosomal $l_{i}$ , we can further express it as

$$
l_{i}=\frac{1}{\beta_{i}^{2}}(\sumu\beta_{i}l_{u}+\sumu\neqv\beta_{i}l_{uv})=E(l_{u})\frac{1}{\beta_{i}}+E(l_{uv})(1−\frac{1}{\beta_{i}})=\frac{1}{\beta_{i}}[E(l_{u})−E(l_{uv})]+E(l_{uv})
$$

in which $l_{u}$ is the mean LD for a diagonal grid, $l_{uv}$ the mean LD for off-diagonal grids, and $m_{i}$ the number of SNPs on the ith chromosome. Consider a linear model below (see Figure 1C for its illustration),

$$
l=b_{0}+b_{1}x+e
$$

in which $l$ represents a vector composed of $Cl_{i},x$ , $x$ represents a vector composed of $C$$x_{i}$, and $x_{i}=\frac{1}{m_{i}}$ the inversion of the SNP number of the ith chromosome. The regression coefficient and intercept can be estimated as below:

$$
b_{1}=\frac{cov(x,l)}{var(x)}=\frac{E(xl)−E(x)E(l)}{var(x)}
$$

and

$$
b_{0}=E(l)−b_{1}E(x)
$$

There are some technical details in order to find the interpretation for $b_{0}$ and $b_{1}$ . We itemize them briefly. For the mean and variance of $x$:

$$
{E(x)=\frac{1}{C}\sumiC\frac{1}{m_{i}}var(x)=\frac{1}{C}\sumiC\frac{1}{m_{i}^{2}}−(\frac{1}{C}\sumiC\frac{1}{m_{i}})^{2}
$$

For $E(xl)$:

$$
E(xl)=\frac{\sumiC\frac{1}{m_{i}}{E(l_{u}\frac{m}{m_{i}})+E(l_{uv})(1−\frac{m}{m_{i}})}}{C}=\frac{\sumiC{E(l_{u}\frac{m}{m_{i}^{2}})+E(l_{uv})(1−\frac{m}{m_{i}})}}{C}=[(E(l_{u})−E(l_{uv}))m](\frac{1}{C}\sumiC\frac{1}{m_{i}^{2}})+E(l_{uv})(\frac{1}{C}\sumiC\frac{1}{m_{i}})
$$

For $E(x)E(l)$:

$$
E(x)E(l)={\frac{1}{C}\sumiC\frac{1}{m_{i}}}{(\frac{1}{C}\sumiC\frac{1}{m_{i}})(E(l_{u})⋅m)+[1−m(\frac{1}{C}\sumiC\frac{1}{m_{i}})]E(l_{uv})}=[(E(l_{u})−E(l_{uv}))m](\frac{1}{C}\sumiC\frac{1}{m_{i}})^{2}+E(l_{uv})(\frac{1}{C}\sumiC\frac{1}{m_{i}})
$$

Then we integrate these items to have the expectation for $b_{1}:$

$$
E(b_{1})=\frac{E(xl)−E(x)E(l)}{var(x)}=\frac{{[(E(l_{u})−E(l_{uv}))m](\frac{1}{C}\sumiC\frac{1}{m_{i}^{2}})+E(l_{uv})(\frac{1}{C}\sumiC\frac{1}{m_{i}})}−{[(E(l_{u})−E(l_{uv}))m](\frac{1}{C}\sumiC\frac{1}{m_{i}})^{2}+E(l_{uv})(\frac{1}{C}\sumiC\frac{1}{m_{i}})}}{\frac{1}{C}\sumiC\frac{1}{m_{i}^{2}}−(\frac{1}{C}\sumiC\frac{1}{m_{i}})^{2}}=[E(l_{u})−E(l_{uv})]m
$$

Similarly, we plug in $E(b_{1})$ so as to derive $b_{0}$ :

$$
E(b_{0})=E(l)−E(b_{1})E(x)={(\frac{1}{C}\sumiC\frac{1}{m_{i}})(E(l_{u})⋅m)+[1−m(\frac{1}{C}\sumiC\frac{1}{m_{i}})]E(l_{uv})}−{(E(l_{u})−E(l_{uv}))⋅m⋅(\frac{1}{C}\sumiC\frac{1}{m_{i}})}=E(l_{uv})
$$

After some algebra, if $E(l_{u})≫E(l_{uv})$—say if the former is far greater than the latter, the interpretation of $b_{1}$ and $b_{0}$ can be

$$
{E(b_{1})=E(l_{u}−l_{uv})m≈E(l_{u})mE(b_{0})=E(l_{uv})
$$

It should be noticed that $E(b_{1})≈E(l_{u})m$ quantifies the averaged LD decay of the genome. Conventional LD decay is analyzed via the well-known LD decay analysis, but Equation 4 provides a direct estimate of both LD decay and possible existence of extended LD. We will see the application of the model in Figure 5 that the strength of the long-distance LD is associated with population structure. Of note, the underlying assumption of Equations 3 and 4 is genome-wide spread of recombination hotspots, an established result that has been revealed and confirmed (Hinch et al., 2019).

### Efficient estimation for lg, li, and li⋅j

For the aforementioned analyses, the bottleneck obviously lies in the computational cost in estimating $l_{i}$ and $l_{i⋅j}$ . $l_{i}$ and $l_{i⋅j}$ are used to be estimated via the current benchmark algorithm as implemented in PLINK (Chang et al., 2015), and the computational time complex is proportional to $O(nm^{2})$. We present a novel approach to estimate $l_{i}$ and $l_{i⋅j}$ . Given a genotypic matrix $X$, a $n\timesm$ matrix, if we assume that there are $m_{i}$ and $m_{j}$ SNPs on chromosomes $i$ and $j$, respectively, we can construct $n\timesn$ genetic relatedness matrices as below:

$$
{K_{i}=\frac{1}{m_{i}}X~_{i}X~_{i}^{T}K_{j}=\frac{1}{m_{j}}X_{j}~X~_{j}^{T}
$$

in which $X~_{i}$ is the standardized $X_{i}$ and $x~_{kl}=\frac{x_{kl}-2p_{l}}{\sqrt{2(1+F)p_{l}q_{l}}}$ , where $x_{kl}$ is the genotype for the kth individual at the lth biallelic locus, $F$ is the inbreeding coefficient having the value of 0 for random mating population and 1 for an inbred population, and $p_{l}$ and $q_{l}$ are the frequencies of the reference and the alternative alleles ($p_{l}+q_{l}=1$), respectively. When GRM is given, we can obtain some statistical characters of $K_{i}$ . We extract two vectors $k_{i_{o}}$ , which stacks the off-diagonal elements of $K_{i}$ , and $k_{i_{d}}$ , which takes the diagonal elements of $K_{i}$ . The mathematical expectation of $k_{i_{o}}^{2}$ , in which $E(k_{i_{o}}^{2})=\frac{1}{n(n−1)}\sumk_{1}\neqk_{2}nk_{k_{1},k_{2}}^{2}$ , can be established according to Isserlis’s theorem in terms of the four-order moment (Isserlis, 1918),

$$
E(k_{i_{o}}^{2})=\frac{1}{m_{i}^{2}n(n−1)}\sumk_{1}\neqk_{2}n\suml_{1},l_{2}m_{i}[(1+\theta_{k_{1}k_{2}}^{2})ρ_{l_{1}l_{2}}^{2}+\theta_{k_{1}k_{2}}^{2}]
$$

in which $E(\theta_{k_{1}k_{2}})=(\frac{1}{2})^{r}$ is the expected relatedness score and $r$ indicates the rth-degree relatives. $r=0$ for the same individual, and $r=1$ for the first-degree relatives. Similarly, we can derive for $Ek_{i_{o}}k_{j_{o}}$.Equation 6 establishes the connection between GRM and the aggregated LD estimation that $l_{i}=E(k_{i_{o}}^{2})$ . According to Delta method as exampled in Appendix I of Lynch and Walsh, 1998, the means and the sampling variances for $l_{i}$ and $l_{i⋅j}$ are

$$
{E(k_{i_{o}}^{2})=l_{i}=\frac{1}{m_{i}^{2}}\suml_{1},l_{2}m_{i}ρ_{l_{1},l_{2}}^{2}var(l_{i})=\frac{4[var^(k_{i_{o}})]^{2}}{n(n−1)}E(k_{i_{o}}k_{k_{o}})=l_{i⋅j}=\frac{1}{m_{i}m_{j}}\suml_{1},l_{2}=1m_{i},m_{j}ρl_{1}^{2},l_{2}var(k_{i_{o}})=E(k_{i_{o}}^{2})−[E(k_{i_{o}})]^{2}=l_{i}−\frac{1}{(n−1)^{2}}
$$

in which $var(k_{i_{o}})=E(k_{i_{o}}^{2})−[E(k_{i_{o}})]^{2}=l_{i}−\frac{1}{(n−1)^{2}}$ and $cov(k_{i_{o}},k_{j_{o}})=E(k_{i_{o}}k_{j_{o}})−E(k_{i_{o}})E(k_{j_{o}})=l_{i⋅j}−\frac{1}{(n−1)^{2}}$ , respectively. Of note, the properties of $l_{g}$ can be derived similarly if we replace $l_{i}$ with $l_{g}$ in Equation 7. We can develop $l∼_{i⋅j}$ , a scaled version of $l_{i⋅j}$ , as below:

$$
l∼_{i⋅j}=\frac{l_{i⋅j}}{\sqrt{l∼_{i}l∼_{j}}}
$$

in which $l∼_{i}=\frac{m_{i}l_{i}−1}{m_{i}−1}$ , a modification that removed the LD with itself. According to Delta method, the sampling variance of $l∼_{i⋅j}$ is

$$
var(l_{i⋅j}~)=\frac{2(l_{i⋅j}~^)^{2}}{n(n−1)}[\frac{var^(k_{i_{o}})var^(k_{j_{o}})}{(cov^(k_{i_{o}},k_{j_{o}}))^{2}}+\frac{(cov^(k_{i_{o}},k_{j_{o}}))^{2}}{var^(k_{i_{o}})var^(k_{j_{o}})}−2]
$$

Of note, when there is no LD between a pair of loci, $l$ yields zero and its counterpart PLINK estimate yields $\frac{1}{n}$ , a difference that can be reconciled in practice (see Figure 2).

![Figure 2.](https://cdn.elifesciences.org/articles/90636/elife-90636-fig2-v2.jpg)

**Figure 2.:** (A) Consistency examination for the 26 1KG cohorts for their $l^_{i}$ and $l^_{i⋅j}$ estimated by X-LD and PLINK (--r2). In each figure, the 22 $l^_{i}$ fitting line is in purple, whereas the 231 $l^_{i⋅j}$ fitting line is in green. The gray solid line, $y=\frac{1}{n}+x$, in which $n$ the sample size of each cohort, represents the expected fit between PLINK and X-LD estimates, and the two estimated regression models at the top-right corner of each plot show this consistency. The sample size of each cohort is in parentheses. (B) Distribution of $R^{2}$ of $l^_{i}$ and $l^_{i⋅j}$ fitting lines is based on X-LD and PLINK algorithms in the 26 cohorts; $R^{2}$ represents variation explained by the fitted model. 26 1KG cohorts: MSL (Mende in Sierra Leone), GWD (Gambian in Western Division, The Gambia), YRI (Yoruba in Ibadan, Nigeria), ESN (Esan in Nigeria), ACB (African Caribbean in Barbados), LWK (Luhya in Webuye, Kenya), ASW (African Ancestry in Southwest US), CHS (Han Chinese South), CDX (Chinese Dai in Xishuangbanna, China), KHV (Kinh in Ho Chi Minh City, Vietnam), CHB (Han Chinese in Beijing, China), JPT (Japanese in Tokyo, Japan), BEB (Bengali in Bangladesh), ITU (Indian Telugu in the UK), STU (Sri Lankan Tamil in the UK), PJL (Punjabi in Lahore, Pakistan), GIH (Gujarati Indian in Houston, TX), TSI (Toscani in Italia), IBS (Iberian populations in Spain), CEU (Utah residents [CEPH] with Northern and Western European ancestry), GBR (British in England and Scotland), FIN (Finnish in Finland); MXL (Mexican Ancestry in Los Angeles, CA), PUR (Puerto Rican in Puerto Rico), CLM (Colombian in Medellin, Colombia), and PEL (Peruvian in Lima, Peru).

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/90636/elife-90636-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** In each figure, the 22 $l^_{i}$ fit line is in purple, whereas the 231 $l^_{i⋅j}$ fit line is in green. The gray solid line, $y=\frac{1}{n}+x$, in which $n$ the sample size, represents the expected fit between PLINK and X-LD, and the two estimated regression models at the top-right corner show this consistency.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/90636/elife-90636-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** Considering the high computational cost of PLINK, only the first chromosome was chosen. In the process of evaluating computational efficiency, we kept adding single-nucleotide polymorphisms (SNPs) until the inclusion of the entire chromosome. The bar chart and line chart show the actual calculation time and theoretical calculation complexity, respectively.

### Raise of LD due to population structure

In this study, the connection between LD and population structure is bridged via two pathways below, in terms of a pair of loci and of the aggregated LD for all pair of loci. For a pair of loci, their LD is often simplified as $ρ_{l_{1}l_{2}}^{2}=\frac{D_{l_{1}l_{2}}^{2}}{p_{l_{1}}q_{l_{1}}p_{l_{2}}q_{l_{2}}}$ , but will be inflated if there are subgroups (Nei and Li, 1973). In addition, it is well established the connection between population structure and eigenvalues, and in particular the largest eigenvalue is associated with divergence of subgroups (Patterson et al., 2006). In this study, the existence of subgroups of cohort is surrogated by the largest eigenvalue $\lambda_{1}$ or $F-_{st}≈\frac{\lambda_{1}}{n}$ .

### Data description and quality control

The 1KG (Auton et al., 2015), which was launched to produce a deep catalog of human genomic variation by whole-genome sequencing (WGS) or whole-exome sequencing (WES), and 2503 strategically selected individuals of global diversity were included (containing 26 cohorts). We used the following criteria for SNP inclusion for each of the 26 1KG cohorts: (1) autosomal SNPs only; (2) SNPs with missing genotype rates higher than 0.2 were removed, and missing genotypes were imputed; and (3) only SNPs with minor allele frequencies higher than 0.05 were retained. Then 2,997,635 consensus SNPs that were present in each of the 26 cohorts were retained. According to their origins, the 26 cohorts are grouped as African (AFR: MSL, GWD, YRI, ESN, ACB, LWK, and ASW), European (EUR: TSI, IBS, CEU, GBR, and FIN), East Asian (EA: CHS, CDX, KHV, CHB, and JPT), South Asian (SA: BEB, ITU, STU, PJL, and GIH), and American (AMR: MXL, PUR, CLM, and PEL), respectively.

In addition, to test the capacity of the developed software (X-LD), we also included CONVERGE cohort ($n=10,640$), which was used to investigate major depressive disorder (MDD) in the Han Chinese population (Cai et al., 2015). We performed the same criteria for SNP inclusion as that of the 1KG cohorts, and $m=5,215,820$ SNPs remained for analyses.

### X-LD software implementation

The proposed algorithm has been realized in our X-LD software, which is written in C++ and reads in binary genotype data as often used in PLINK. As multi-thread programming is adopted, the efficiency of X-LD can be improved upon the availability of computational resources. We have tested X-LD in various independent datasets for its reliability and robustness. Certain data management options, such as flexible inclusion or exclusion of chromosomes, have been built into the commands of X-LD. In X-LD, missing genotypes are naively imputed according to Hardy–Weinberg proportions; however, when the missing rate is high, we suggest the genotype matrix should be imputed by other advanced imputation tools.

The most time-consuming part of X-LD was the construction of GRM $K=\frac{1}{m}X~X~^{T}$ , and the established computational time complex was $O(n^{2}m)$. However, if $X~$ is decomposed into $X~=[X~_{t_{1},}⋮X~_{t_{2},}⋮⋯⋮X~_{t_{z},}]$, in which $X~_{[t_{i},]}$ has dimension of $n\timesB$, using Mailman algorithm the computational time complex for building $K$ can be reduced to $O(\frac{n^{2}m}{log_{3}⁡m})$ (Liberty and Zucker, 2009). This idea of embedding Mailman algorithm into certain high-throughput genomic studies has been successful, and our X-LD software is also leveraged by absorbing its recent practice in genetic application (Wu and Sankararaman, 2018).

## Results

### Statistical properties of the proposed method

Table 1 introduces the symbols frequently cited in this study. As schematically illustrated in Figure 1, $l_{g}$ could be decomposed into $Cl_{i}$ and $\frac{C(C−1)}{2}$ unique $l_{i⋅j}$ components. We compared the estimated $l_{i}$ and $l_{i⋅j}$ in X-LD with those being estimated in PLINK (known as ‘--r2,’ and the estimated squared Pearson’s correlation LD is denoted as $r^{2}$). Considering the substantial computational cost of PLINK, only 100,000 randomly selected autosome SNPs were used for each 1KG cohort, and 22 $l^_{i}$ and 231 $l^_{i⋅j}$ were estimated. After regressing 22 $l^_{i}$ against those of PLINK, we found that the regression slope was close to unity and bore an anticipated intercept a quantity of approximately $\frac{1}{n}$ (Figure 2A and B). In other words, PLINK gave $\frac{1}{n}$ even for SNPs of no LD. However, when regressing 231 $l^_{i⋅j}$ estimates against those of PLINK, it was found that largely because of the tiny quantity of $l^_{i⋅j}$ it was slightly smaller than 1 but statistically insignificant from 1 in these 26 1KG cohorts (mean of 0.86 and SD of 0.10, and its 95% CI was (0.664, 1.056)); when the entire 1KG samples were used, its much larger LD due to subgroups, nearly no estimation bias was found (Figure 2A and B). In contrast, because of their much larger values, $l^_{i}$ components were always consistent with their corresponding estimates from PLINK (mean of 1.03 and SD of 0.012, 95% CI was (1.006, 1.053), bearing an ignorable bias). Furthermore, we also combined the African cohorts together (MSL, GWD, YRI, ESN, LWK, totaling 599 individuals), the East Asian cohorts together (CHS, CDX, KHV, CHB, and JPT, totaling 504 individuals), and the European cohorts together (TSI, IBS, CEU, GBR, and FIN, totaling 503 individuals), and the resemblance pattern between X-LD and PLINK was similar as observed in each cohort alone (Figure 2—figure supplement 1). The empirical data in 1KG verified that the proposed method was sufficiently accurate.

**Table 1.**
 Notation definitions.


<table>
  <thead>
    <tr>
      <th>Notation</th>
      <th>Definition</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>C</td>
      <td>The number of chromosomes.</td>
    </tr>
    <tr>
      <td>i and j</td>
      <td>Subscripts index chromosome i and j.</td>
    </tr>
    <tr>
      <td>βi</td>
      <td>The number of SNP segments of chromosome i, each of which has m SNPs.</td>
    </tr>
    <tr>
      <td>Dl1l2</td>
      <td>The difference between the observed and expected haplotype frequencies, with Dl1l2=pl1l2-pl1pl2 .</td>
    </tr>
    <tr>
      <td>F</td>
      <td>The inbreeding coefficient.</td>
    </tr>
    <tr>
      <td>Ki</td>
      <td>Genetic relatedness matrix for chromosome i, and two vectors, kio and kid , from Ki , where kio stacks the off-diagonal elements and kid stacks the diagonal elements.</td>
    </tr>
    <tr>
      <td>k</td>
      <td>Subscript indexes individual.</td>
    </tr>
    <tr>
      <td>l1 and l2</td>
      <td>Subscripts index a pair of SNPs.</td>
    </tr>
    <tr>
      <td>m</td>
      <td>The number of SNPs; mi the number of SNPs on chromosome i.</td>
    </tr>
    <tr>
      <td>n</td>
      <td>The number of samples; ni , the number of samples in subpopulation i.</td>
    </tr>
    <tr>
      <td>pl and ql</td>
      <td>Frequency of the lth reference allele and alternative allele in the population.</td>
    </tr>
    <tr>
      <td>θk1k2</td>
      <td>The relatedness score between individual k1 and k2 .</td>
    </tr>
    <tr>
      <td>xkl</td>
      <td>The genotype for the kth individual at the lth biallelic locus.</td>
    </tr>
    <tr>
      <td>Xi and X~i</td>
      <td>Genotype and standardized genotype matrixes for chromosome i.</td>
    </tr>
    <tr>
      <td>ρl1l22</td>
      <td>Squared Pearson’s correlation coefficient for any pair of SNPs, including an SNP to itself when l1=l2 .</td>
    </tr>
    <tr>
      <td>r2</td>
      <td>Squared Pearson’s correlation metric for LD but estimated from PLINK (--r2) or PopLDdecay.</td>
    </tr>
    <tr>
      <td>lg</td>
      <td>The mean LD of the whole genome-wide m2 SNP pairs.</td>
    </tr>
    <tr>
      <td>li</td>
      <td>The intra-chromosomal mean LD for the ith chromosome of mi2 SNP pairs.</td>
    </tr>
    <tr>
      <td>li⋅j</td>
      <td>The inter-chromosomal mean LD ith and jth chromosomal mimj SNP pairs, a scaled version is ℓ∼ij .</td>
    </tr>
    <tr>
      <td>lu</td>
      <td>The mean LD for a diagonal grid.</td>
    </tr>
    <tr>
      <td>luv</td>
      <td>The mean LD for off-diagonal grids.</td>
    </tr>
  </tbody>
</table>

_LD, linkage disequilibrium; SNP, single-nucleotide polymorphism._

To fairly evaluate the computational efficiency of the proposed method, the benchmark comparison was conducted on the first chromosome of the entire 1KG dataset ($n=2,503$ and $m=225,967$), and 10 CPUs were used for multi-thread computing. Compared with PLINK, the calculation efficiency of X-LD was nearly 30–40 times faster for the tested chromosome, and its computational time of X-LD was proportional to $O(\frac{n^{2}m}{log_{3}⁡m})$ (Figure 2—figure supplement 2). So, X-LD provided a feasible and reliable estimation of large-scale complex LD patterns. More detailed computational time of the tested tasks is reported in their corresponding sections below; since each 1KG cohort had a sample size of around 100, otherwise specified the computational time was reported for CHB ($n=103$) as a reference (Table 2). In order to test the capability of the software, the largest dataset tested was CONVERGE ($n=10,640$, and $m=5,215,820$), and it took 77,508.00 s, about 22 hr, to estimate 22 autosomal $l^_{i}$ and 231 $l^_{i⋅j}$ (Figure 1A); when zooming into chromosome 2 of CONVERGE, on which 420,949 SNPs had been evenly split into 1000 blocks and yielded 1000 $l^_{u}$ grids, and 499,500 $l^_{uv}$ LD grids, it took 45,125.00 s, about 12.6 hr, to finish the task (Figure 1B).

**Table 2.**
 Computational time for the demonstrated estimation tasks.


<table>
  <thead>
    <tr>
      <th>Cohort</th>
      <th>Task description</th>
      <th>Time cost</th>
      <th>Computational time complex</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CHB (n=103, m=2,997,655)</td>
      <td>Estimation for 22 autosomal ℓi , and 231 inter-chromosomal ℓi⋅j . For results, see Figure 3 and Table 3.</td>
      <td>101,34 s</td>
      <td>O(n2m)</td>
    </tr>
    <tr>
      <td>1KG (n=2,503, m=2,997,655)</td>
      <td>Same as above.</td>
      <td>3008.29 s</td>
      <td>Same as above</td>
    </tr>
    <tr>
      <td>CONVERGE (n=10,640, m=5,215,820)</td>
      <td>Same as above. For results, see Figure 1A.</td>
      <td>77,508.00 s</td>
      <td>Same as above</td>
    </tr>
    <tr>
      <td></td>
      <td>Estimation for high-resolution LD interaction given bin size of 250 SNPs</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>CHB (n=103, m2=241,241)</td>
      <td>Chromosome 2, estimation for 965 li, and 465,130 li⋅j . For results, see Figure 4.</td>
      <td>66.86 s</td>
      <td>O(n2(mi+(mi250)2))</td>
    </tr>
    <tr>
      <td>CHB (n=103, m22=40,378)</td>
      <td>Chromosome 22, estimation for 162 li, and 13,041 li⋅j . For results, see Figure 4.</td>
      <td>3.22 s</td>
      <td>Same as above</td>
    </tr>
    <tr>
      <td>CONVERGE (n=10,640, m22=71,407)</td>
      <td>Chromosome 22, estimation for 286 li, and 40,755 li⋅j .</td>
      <td>8,736.29 s</td>
      <td>Same as above</td>
    </tr>
    <tr>
      <td>CONVERGE (n=10,640, m2=420,949)</td>
      <td>Chromosome 2, estimation for 1000 li, and 499,500 li⋅j . For results, see Figure 1B.</td>
      <td>45,125.00 s</td>
      <td>Chromosome 2 was split into 1000 blocks, each of which had about 420 SNPs</td>
    </tr>
  </tbody>
</table>

_For the sake of fair comparison, 10 CPUs were used for multi-thread computing.LD, linkage disequilibrium; SNP, single-nucleotide polymorphism._

### Ubiquitously extended LD and population structure/admixture

We partitioned the 2,997,635 SNPs into 22 autosomes ( Figure 3A , Figure 3—figure supplement 1), and the general LD patterns were as illustrated for CEU, CHB, YRI, ASW, and 1KG. As expected, $l^_{i⋅j}<l^_{g}<l^_{i}$ for each cohort (Figure 3B). As observed in these 1KG cohorts, all three LD measures were associated with population structure, which was surrogated by $F-_{st}≈\frac{\lambda_{1}}{n}$ , and their squared correlation $R^{2}$ was greater than 0.8. ACB, ASW, PEL, and MXL, which all showed certain admixture, tended to have much greater $l^_{g}$ , $l^_{i}$ , and $l^_{i⋅j}$ (Table 3 and Figure 3B). In contrast, East Asian (EA) and European (EUR)-orientated cohorts, which showed little within-cohort genetic differentiation—as their largest eigenvalues were slightly greater than 1—had their aggregated LD relatively low and resembled each other (Table 3). Furthermore, for several European (TSI, IBS, and FIN) and East Asian (JPT) cohorts, the ratio between $l^_{i⋅j}$ and $l^_{i}$ components could be smaller than 0.1, and the smallest ratio was found to be about 0.091 in FIN. The largest ratio was found in 1KG that $l^_{i⋅j}=5.7e−3$ and $l^_{i}=6.5e−3$, and the ratio was 0.877 because of the inflated LD due to population structure. A more concise statistic to describe the ratio between $l_{i⋅j}$ and $l_{i}$ was $l∼_{i⋅j}$ (Equation 8), and the corresponding value for 231 scaled $l∼_{i⋅j}$ for FIN was $l∼^_{i⋅j}=0.10$ (SD of 0.027) and for 1KG was $l∼^_{i⋅j}=0.88$ (SD of 0.028).

![Figure 3.](https://cdn.elifesciences.org/articles/90636/elife-90636-fig3-v2.jpg)

**Figure 3.:** (A) Chromosomal scale LD components for five representative cohorts (CEU, CHB, YRI, ASW, and 1KG). The upper parts of each figure represent $l^_{i}$ (along the diagonal) and $l^_{i⋅j}$ (off-diagonal), and the lower part $l∼^_{i⋅j}$ as in Equation 8. For visualization purposes, the quantity of LD before scaling is transformed to a -log10 scale, with smaller values (red hues) representing larger LD, and a value of 0 representing that all single-nucleotide polymorphisms (SNPs) are in LD. (B) The relationship between the degree of population structure (approximated by $F-_{st}$) and $l^_{i}$ , $l^_{g}$ , and $l^_{i⋅j}$ in the 26 1KG cohorts.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/90636/elife-90636-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** The upper and lower parts of each figure represent the LD before and after scaling according to Equation 8. $l^_{i}$ and $l^_{i⋅j}$ are represented by the diagonal and the off-diagonal elements, respectively. For visualization purposes, LD before scaling is transformed to a -log10-scale, with smaller values (red hues) representing larger LD, and a value of 0 representing that all single-nucleotide polymorphisms (SNPs) are in LD.

**Table 3.**
 X-LD estimation for complex LD components (2,997,635 SNPs).


<table>
  <thead>
    <tr>
      <th>Cohort (n)</th>
      <th>Ancestry</th>
      <th>λ1(Fst)*</th>
      <th>l^g (SE)†</th>
      <th>l¯i^ (SD) ‡</th>
      <th>l¯i⋅j^ (SD) ‡</th>
      <th>l∼^i⋅j (SD) ‡</th>
      <th>Lower bound of LD §</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>MSL (85)</td>
      <td>AFR</td>
      <td>1.10 (0.013)</td>
      <td>1.9e-4 (1.21e-6)</td>
      <td>6.9e-4 (2.0e-4)</td>
      <td>1.7e-4 (1.7e-5)</td>
      <td>0.26 (0.053)</td>
      <td>0.161971831</td>
    </tr>
    <tr>
      <td>GWD (113)</td>
      <td>AFR</td>
      <td>1.07 (0.009)</td>
      <td>1.1e-4 (5.61e-7)</td>
      <td>6.0e-4 (2.0e-4)</td>
      <td>8.7e-5 (8.1e-6)</td>
      <td>0.16 (0.037)</td>
      <td>0.247218789</td>
    </tr>
    <tr>
      <td>YRI (107)</td>
      <td>AFR</td>
      <td>1.05 (0.010)</td>
      <td>1.1e-4 (4.23e-7)</td>
      <td>5.9e-4 (2.0e-4)</td>
      <td>8.8e-5 (6.9e-6)</td>
      <td>0.16 (0.04)</td>
      <td>0.242001641</td>
    </tr>
    <tr>
      <td>ESN (99)</td>
      <td>AFR</td>
      <td>1.09 (0.011)</td>
      <td>1.4e-4 (7.67e-7)</td>
      <td>7.0e-4 (2.2e-4)</td>
      <td>1.2e-4 (1.2e-5)</td>
      <td>0.19 (0.043)</td>
      <td>0.217391304</td>
    </tr>
    <tr>
      <td>ACB (96)</td>
      <td>AFR</td>
      <td>2.01 (0.021)</td>
      <td>2.9e-4 (3.78e-6)</td>
      <td>9.1e-4 (2.5e-4)</td>
      <td>2.5e-4 (3.6e-5)</td>
      <td>0.29 (0.070)</td>
      <td>0.147727273</td>
    </tr>
    <tr>
      <td>LWK (99)</td>
      <td>AFR</td>
      <td>1.35 (0.014)</td>
      <td>2.2e-4 (2.38e-6)</td>
      <td>8.4e-4 (2.5e-4)</td>
      <td>1.9e-4 (3.2e-5)</td>
      <td>0.24 (0.052)</td>
      <td>0.173913043</td>
    </tr>
    <tr>
      <td>ASW (61)</td>
      <td>AFR</td>
      <td>1.90 (0.031)</td>
      <td>1.1e-3 (2.73e-5)</td>
      <td>2.0e-3 (3.2e-4)</td>
      <td>1.1e-3 (6.2e-5)</td>
      <td>0.57 (0.059)</td>
      <td>0.079681275</td>
    </tr>
    <tr>
      <td>CHS (105)</td>
      <td>EA</td>
      <td>1.08 (0.010)</td>
      <td>1.4e-4 (9.39e-7)</td>
      <td>9.5e-4 (3.4e-4)</td>
      <td>1.0e-4 (1.3e-5)</td>
      <td>0.12 (0.030)</td>
      <td>0.31147541</td>
    </tr>
    <tr>
      <td>CDX (93)</td>
      <td>EA</td>
      <td>1.11 (0.012)</td>
      <td>1.8e-4 (1.38e-6)</td>
      <td>1.1e-3 (3.6e-4)</td>
      <td>1.4e-4 (2.0e-5)</td>
      <td>0.14 (0.040)</td>
      <td>0.272277228</td>
    </tr>
    <tr>
      <td>KHV (99)</td>
      <td>EA</td>
      <td>1.07 (0.011)</td>
      <td>1.4e-4 (7.67e-7)</td>
      <td>9.5e-4 (3.5e-4)</td>
      <td>1.0e-4 (1.2e-5)</td>
      <td>0.12 (0.031)</td>
      <td>0.31147541</td>
    </tr>
    <tr>
      <td>CHB (103)</td>
      <td>EA</td>
      <td>1.07 (0.010)</td>
      <td>1.3e-4 (6.94e-7)</td>
      <td>9.3e-4 (3.4e-4)</td>
      <td>9.5e-5 (1.1e-5)</td>
      <td>0.11 (0.030)</td>
      <td>0.317948718</td>
    </tr>
    <tr>
      <td>JPT (104)</td>
      <td>EA</td>
      <td>1.06 (0.010)</td>
      <td>1.3e-4 (7.22e-7)</td>
      <td>1.0e-3 (3.8e-4)</td>
      <td>9.3e-5 (1.2e-5)</td>
      <td>0.10 (0.028)</td>
      <td>0.338638673</td>
    </tr>
    <tr>
      <td>BEB (86)</td>
      <td>SA</td>
      <td>1.07 (0.012)</td>
      <td>1.7e-4 (8.09e-7)</td>
      <td>9.1e-4 (3.1e-4)</td>
      <td>1.4e-4 (1.5e-5)</td>
      <td>0.17 (0.042)</td>
      <td>0.236363636</td>
    </tr>
    <tr>
      <td>ITU (102)</td>
      <td>SA</td>
      <td>1.61 (0.016)</td>
      <td>1.9e-4 (1.84e-6)</td>
      <td>9.5e-4 (3.1e-4)</td>
      <td>1.5e-4 (1.7e-5)</td>
      <td>0.18 (0.044)</td>
      <td>0.231707317</td>
    </tr>
    <tr>
      <td>STU (102)</td>
      <td>SA</td>
      <td>1.56 (0.015)</td>
      <td>2.6e-4 (3.21e-6)</td>
      <td>1.0e-3 (3.3e-4)</td>
      <td>2.3e-4 (3.1e-5)</td>
      <td>0.23 (0.047)</td>
      <td>0.171526587</td>
    </tr>
    <tr>
      <td>PJL (96)</td>
      <td>SA</td>
      <td>1.67 (0.017)</td>
      <td>2.4e-4 (2.74e-6)</td>
      <td>1.1e-3 (3.4e-4)</td>
      <td>2.0e-4 (2.2e-5)</td>
      <td>0.21 (0.048)</td>
      <td>0.20754717</td>
    </tr>
    <tr>
      <td>GIH (103)</td>
      <td>SA</td>
      <td>1.73 (0.017)</td>
      <td>2.7e-4 (3.41e-6)</td>
      <td>1.1e-3 (3.4e-4)</td>
      <td>2.4e-4 (1.9e-5)</td>
      <td>0.23 (0.049)</td>
      <td>0.179153094</td>
    </tr>
    <tr>
      <td>TSI (107)</td>
      <td>EUR</td>
      <td>1.07 (0.010)</td>
      <td>1.2e-4 (6.10e-7)</td>
      <td>9.1e-4 (3.3e-4)</td>
      <td>9.0e-5 (1.1e-5)</td>
      <td>0.11 (0.029)</td>
      <td>0.325</td>
    </tr>
    <tr>
      <td>IBS (107)</td>
      <td>EUR</td>
      <td>1.07 (0.010)</td>
      <td>1.2e-4 (6.10e-7)</td>
      <td>9.1e-4 (3.3e-4)</td>
      <td>8.8e-5 (1.1e-5)</td>
      <td>0.11 (0.028)</td>
      <td>0.329949239</td>
    </tr>
    <tr>
      <td>CEU (99)</td>
      <td>EUR</td>
      <td>1.07 (0.011)</td>
      <td>1.4e-4 (7.67e-7)</td>
      <td>9.6e-4 (3.4e-4)</td>
      <td>1.1e-4 (1.3e-5)</td>
      <td>0.12 (0.030)</td>
      <td>0.293577982</td>
    </tr>
    <tr>
      <td>GBR (91)</td>
      <td>EUR</td>
      <td>1.11 (0.012)</td>
      <td>1.7e-4 (1.08e-6)</td>
      <td>1.0e-3 (3.6e-4)</td>
      <td>1.4e-4 (1.8e-5)</td>
      <td>0.15 (0.036)</td>
      <td>0.253807107</td>
    </tr>
    <tr>
      <td>FIN (99)</td>
      <td>EUR</td>
      <td>1.09 (0.011)</td>
      <td>1.5e-4 (9.69e-7)</td>
      <td>1.1e-3 (3.8e-4)</td>
      <td>1.0e-4 (1.5e-5)</td>
      <td>0.10 (0.027)</td>
      <td>0.34375</td>
    </tr>
    <tr>
      <td>MXL (64)</td>
      <td>AMR</td>
      <td>2.29 (0.036)</td>
      <td>7.2e-4 (1.49e-5)</td>
      <td>2.1e-3 (4.1e-4)</td>
      <td>6.3e-4 (9.6e-5)</td>
      <td>0.32 (0.072)</td>
      <td>0.136986301</td>
    </tr>
    <tr>
      <td>PUR (104)</td>
      <td>AMR</td>
      <td>1.43 (0.014)</td>
      <td>1.6e-4 (1.30e-6)</td>
      <td>1.2e-3 (4.2e-4)</td>
      <td>1.2e-4 (1.7e-5)</td>
      <td>0.11 (0.026)</td>
      <td>0.322580645</td>
    </tr>
    <tr>
      <td>CLM (94)</td>
      <td>AMR</td>
      <td>1.58 (0.017)</td>
      <td>2.3e-4 (2.49e-6)</td>
      <td>1.4e-3 (4.5e-4)</td>
      <td>1.7e-4 (2.6e-5)</td>
      <td>0.13 (0.035)</td>
      <td>0.281690141</td>
    </tr>
    <tr>
      <td>PEL (85)</td>
      <td>AMR</td>
      <td>2.38 (0.028)</td>
      <td>4.5e-4 (7.33e-6)</td>
      <td>1.9e-3 (5.1e-4)</td>
      <td>3.7e-4 (8.5e-5)</td>
      <td>0.21 (0.062)</td>
      <td>0.196483971</td>
    </tr>
    <tr>
      <td>1KG (2503)</td>
      <td>MIX</td>
      <td>164.20 (0.066)</td>
      <td>5.8e-3 (4.63e-6)</td>
      <td>6.5e-3 (4.1e-4)</td>
      <td>5.7e-3 (2.4e-4)</td>
      <td>0.88 (0.028)</td>
      <td>0.051505547</td>
    </tr>
  </tbody>
</table>

_LD, linkage disequilibrium; SNPs, single-nucleotide polymorphisms.*Eigenvalue was estimated. In parentheses is the ratio between the listed largest eigenvalue and the sample size. Since there exists an approximation that F-st≈λ1n , the ratio can be taken as an approximation of population structure.†Standard error was calculated as 2n(n−1)[l^g−1(n−1)2], as Equation 7.‡Estimated empirically from C chromosomal l^i ; Estimated empirically from C(C−1)2 inter-chromosomal l^i⋅j .§It is estimated by 22ℓ¯^i22ℓ¯^i+231ℓ¯^i⋅j , indicating lower bound of true LD._

In terms of computational time, for 103 CHB samples, it took about 101.34 s to estimate 22 autosomal $l^_{i}$ and 231 $l^_{i⋅j}$ ; for all 1KG 2503 samples, X-LD took about 3008.29 s (Table 1). Conventional methods took too long to complete the analyses in this section, so no comparable computational time was provided. For detailed 22 $l^_{i}$ and 231 $l^_{i⋅j}$ estimates for each 1KG cohort, please refer to Supplementary file 1 (Excel sheet 1–27).

### Detecting exceedingly high LD grids shaped by variable recombination rates

We further explored each autosome with high-resolution grid LD visualization. We set $m=250$, so each grid had the $l_{uv}$ for 250 × 250 SNP pairs. The computational time complex was $O(n^{2}(m_{i}+\frac{\beta_{i}^{2}}{4}))$, in which $\beta_{i}=\frac{m_{i}}{250}$ , and with our proposed method in CHB it cost 66.86 s for chromosome 2, which had 241,241 SNPs and totaled 466,095 unique grids, and 3.22 s only for chromosome 22, which had 40,378 SNPs and totaled 13,203 unique grids (Table 1). In contrast, under conventional methods those LD grids were not very likely to be exhaustively surveyed because its computational cost was $O(nm_{i}^{2})$: for CHB chromosome 2, it would have taken about 40 hr as estimated. As the result was very similar for $m=500$ (Figure 4—figure supplement 1), we only report the results under $m=250$ below.

As expected, chromosome 6 (206,165 SNPs, totaling 340,725 unique grids) had its HLA cluster showing much higher LD than the rest of chromosome 6. In addition, we found a very dramatic variation of the HLA cluster LD $l^_{HLA}$ (28,477,797–33,448,354 bp, totaling 3160 unique grids) across ethnicities. For CEU, CHB, YRI, and ASW, their $l^_{6}=0.0010$, 0.00090, 0.00064, and 0.0019, respectively, but their corresponding HLA cluster grids had $l^_{HLA}=0.042$, 0.029, 0.025, and 0.022, respectively (Figure 4). Consequently, the largest ratio for $\frac{l^_{HLA}}{l^_{6}}$ was 42.00 in CEU, 39.06 in YRI, and 32.22 in CHB, but was reduced to 11.58 in ASW. Before the release of CHM13 (Hoyt et al., 2022), chromosome 11 had the most completely sequenced centromere region, which had much rarer recombination events, and all four cohorts showed a strong LD $l^_{11.c}$ around the centromere (46,061,947–59,413,484 bp, totaling 1035 unique grids) regardless of their ethnicities (Figure 4). $l^_{11}=0.0012$, 0.0012, 0.00084, and 0.0022, respectively, and $l^_{11.c}=0.098$, 0.10, 0.079, and 0.094, respectively; the ratio for $\frac{l^_{11.c}}{l^_{11}}=$ 81.67, 83,33, and 94,05, for CEU, CHB, and YRI, respectively; the lowest ratio was found in ASW of 42.73. In addition, removing the HLA region of chromosome 6 or the centromere region of chromosome 11 would significantly reduce $l^_{6}$ or $l^_{11}$ in comparison with the random removal of other regions (Figure 4—figure supplement 2).

![Figure 4.](https://cdn.elifesciences.org/articles/90636/elife-90636-fig4-v2.jpg)

**Figure 4.:** High-resolution illustration for linkage disequilibrium (LD) grids for CEU, CHB, YRI, and ASW ($m=250$).For each cohort, we partition chromosomes 6 and 11 into high-resolution LD grids (each LD grid contains 250 ×250 single-nucleotide polymorphism [SNP] pairs). The bottom half of each figure shows the LD grids for the entire chromosome. Further zooming into HLA on chromosome 6 and the centromere region on chromosome 11, and their detailed LD in the relevant regions are also provided in the upper half of each figure. For visualization purposes, LD is transformed to a -log10-scale, with smaller values (red hues) representing larger LD, and a value of 0 representing that all SNPs are in LD.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/90636/elife-90636-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** High-resolution illustration for linkage disequilibrium (LD) grids for CEU, CHB, YRI, and ASW ($m=500$).For each cohort, we partitioned each chromosome into consecutive LD grids (each LD grid containing 500 single-nucleotide polymorphisms [SNPs]). For visualization purposes, LD is transformed to a -log10-scale, with smaller values (red hues) representing larger LD, and a value of 0 representing that all SNPs are in LD.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/90636/elife-90636-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** When another region was removed, to avoid chance, the same number of consecutive single-nucleotide polymorphisms (SNPs) as HLA region or centromere region was randomly removed from the genomic region, and this operation was repeated 100 times.

### Model-based LD decay regression revealed LD composition

The real LD block size was not exact of $m=250$ or $m=500$, but an unknown parameter that should be inferred in computational intensive ‘LD decay’ analysis (Zhang et al., 2019; Chang et al., 2015). We conducted the conventional LD decay for the 26 1KG cohorts (Figure 5A), and the time cost was 1491.94 s for CHB. For each cohort, we took the area under the LD decay curve in the LD decay plot, and it quantified approximately the LD decay score for each cohort. The smallest score was 0.0421 for MSL, and the largest was 0.0598 for PEL (Table 5). However, this estimation did not take into account the real extent of LD, so it was not precise enough to reflect the LD decay score. For example, for admixture population, such as the American cohorts, the extent of LD would be longer.

![Figure 5.](https://cdn.elifesciences.org/articles/90636/elife-90636-fig5-v2.jpg)

**Figure 5.:** (A) Conventional LD decay analysis in PLINK for 26 cohorts. To eliminate the influence of sample size, the inverse of sample size has been subtracted from the original LD values. The YRI cohort, represented by the orange dotted line, is chosen as the reference cohort in each plot. The top-down arrow shows the order of LDdecay values according to Table 5. (B) Model-based LD decay analysis for the 26 1KG cohorts. We regressed each autosomal $l^_{i}$ against its corresponding inversion of the single-nucleotide polymorphism (SNP) number for each cohort. Regression coefficient $b_{1}$ quantifies the averaged LD decay of the genome and intercept $b_{0}$ provides a direct estimate of the possible existence of long-distance LD. The $R$ values in the first three plots indicate the correlation between $b^_{1}$ and LD decay score in three different physical distance and the correlation between $b^_{1}$ (left-side vertical axis) and LD decay score (right-side vertical axis) and the correlation between $b^_{0}$ (left-side vertical axis) and $F-_{st}$ (right-side vertical axis), respectively. The last plot assessed the impact of centromere region of chromosome 11 on the linear relationship between chromosomal LD and the inverse of the SNP number. The dark and light gray dashed lines represent the mean of the $R$ with and without the presence of centromere region of chromosome 11.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/90636/elife-90636-fig5-figsupp1-v2.jpg)

In contrast, we proposed a model-based method, as given in Equation 3, which could estimate LD decay score (regression coefficient $b_{1}$) and long-distance LD score (intercept $b_{0}$) jointly. Given the estimated 22 $l^_{i}$ (Supplementary file 1; see Table 4 for four representative cohorts and Supplementary R code), we regressed each autosomal $l^_{i}$ against its corresponding inversion of SNP number, and all yielded positive slopes (Pearson’s correlation $R>0.80$, Table 5 and Figure 5B), an observation that was consistent with genome-wide spread of recombination hotspots. This linear relationship could consequently be considered the norm for a relatively homogeneous population as observed in most 1KG cohorts (Figure 5—figure supplement 1), while for all the 2503 1KG samples $R=0.55$ only (Table 5), indicating that the population structure and possible differentiated recombination hotspots across ethnicities disturbed the assumption underlying Equation 3 and smeared the linearity. We extracted $b^_{0}$ and $b^_{1}$ for the 26 1KG cohorts for further analysis. The rates of LD decay score, as indicated by $b^_{1}$ , within the African cohorts (AFR) were significantly faster than the other continents, consistent with previous observation that the African population had relatively shorter LD Gabriel et al., 2002; while subgroups within the American continent (AMR) tended to have extended LD range due to their admixed genetic composition (Table 4 and Figure 5). Notably, the correlation between $b^_{1}$ and the approximated LD decay score was $R=0.88$. The estimated $F-_{st}$ was highly correlated with $b^_{0}$ ($R=0.94$).

**Table 4.**
 Estimates for 22 autosomal ﻿$l^_{i}$ in CEU, CHB, YRI, and ASW, respectively.


<table>
  <thead>
    <tr>
      <th rowspan="2">Chromosome</th>
      <th rowspan="2">SNP number</th>
      <th></th>
      <th colspan="4">l^i</th>
    </tr>
    <tr>
      <th></th>
      <th>CEU</th>
      <th>CHB</th>
      <th>YRI</th>
      <th>ASW</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>225,967</td>
      <td></td>
      <td>5.0e-4 (8.2e-6)</td>
      <td>0.00049 (7.8e-6)</td>
      <td>0.00032 (4.3e-6)</td>
      <td>0.0015 (4e-05)</td>
    </tr>
    <tr>
      <td>2</td>
      <td>241,241</td>
      <td></td>
      <td>5.0e-4 (8.1e-6)</td>
      <td>5.0e-4 (7.9e-6)</td>
      <td>3.0e-4 (4.1e-6)</td>
      <td>0.0015 (4e-05)</td>
    </tr>
    <tr>
      <td>3</td>
      <td>212,670</td>
      <td></td>
      <td>6.0e-04 (1.0e-5)</td>
      <td>0.00058 (9.5e-6)</td>
      <td>0.00039 (5.7e-6)</td>
      <td>0.0018 (5.1e-5)</td>
    </tr>
    <tr>
      <td>4</td>
      <td>222,241</td>
      <td></td>
      <td>0.00062 (1.0e-5)</td>
      <td>0.00061 (1.0e-5)</td>
      <td>0.00038 (5.4e-6)</td>
      <td>0.0018 (5.0e-5)</td>
    </tr>
    <tr>
      <td>5</td>
      <td>193,632</td>
      <td></td>
      <td>0.00069 (1.2e-5)</td>
      <td>7.0e-04 (1.2e-5)</td>
      <td>0.00043 (6.5e-6)</td>
      <td>0.0018 (4.9e-5)</td>
    </tr>
    <tr>
      <td>6</td>
      <td>206,165</td>
      <td></td>
      <td>0.0010 (1.9e-5)</td>
      <td>9.0e-04 (1.6e-5)</td>
      <td>0.00064 (1.0e-5)</td>
      <td>0.0019 (5.4e-5)</td>
    </tr>
    <tr>
      <td>7</td>
      <td>177,414</td>
      <td></td>
      <td>0.00073 (1.3e-5)</td>
      <td>0.00071 (1.2e-5)</td>
      <td>0.00045 (6.8e-6)</td>
      <td>0.0016 (4.3e-5)</td>
    </tr>
    <tr>
      <td>8</td>
      <td>163,436</td>
      <td></td>
      <td>0.00075 (1.3e-5)</td>
      <td>0.00069 (1.2e-5)</td>
      <td>0.00043 (6.5e-6)</td>
      <td>0.0022 (6.4e-5)</td>
    </tr>
    <tr>
      <td>9</td>
      <td>129,440</td>
      <td></td>
      <td>0.00074 (1.3e-5)</td>
      <td>0.00074 (1.3e-5)</td>
      <td>0.00047 (7.2e-6)</td>
      <td>0.0018 (5.0e-5)</td>
    </tr>
    <tr>
      <td>10</td>
      <td>152,251</td>
      <td></td>
      <td>0.00078 (1.4e-5)</td>
      <td>8.0e-04 (1.4e-5)</td>
      <td>0.00058 (9.3e-6)</td>
      <td>0.0019 (5.6e-5)</td>
    </tr>
    <tr>
      <td>11</td>
      <td>151,751</td>
      <td></td>
      <td>0.0012 (2.3e-5)</td>
      <td>0.0012 (2.2e-5)</td>
      <td>0.00084 (1.4e-5)</td>
      <td>0.0022 (6.2e-5)</td>
    </tr>
    <tr>
      <td>12</td>
      <td>139,684</td>
      <td></td>
      <td>8.0e-4 (1.4e-5)</td>
      <td>0.00073 (1.2e-5)</td>
      <td>0.00049 (7.5e-6)</td>
      <td>0.0017 (4.8e-5)</td>
    </tr>
    <tr>
      <td>13</td>
      <td>113,390</td>
      <td></td>
      <td>0.0010 (1.8e-5)</td>
      <td>0.00094 (1.6e-5)</td>
      <td>0.00061 (9.8e-6)</td>
      <td>0.0018 (4.9e-5)</td>
    </tr>
    <tr>
      <td>14</td>
      <td>97,335</td>
      <td></td>
      <td>0.0011 (2.0e-5)</td>
      <td>0.0010 (1.8e-5)</td>
      <td>0.00065 (1.1e-5)</td>
      <td>0.0020 (5.6e-5)</td>
    </tr>
    <tr>
      <td>15</td>
      <td>85,307</td>
      <td></td>
      <td>0.0010 (1.8e-5)</td>
      <td>0.00098 (1.7e-5)</td>
      <td>6.0e-4 (9.6e-6)</td>
      <td>0.0020 (5.8e-5)</td>
    </tr>
    <tr>
      <td>16</td>
      <td>92,007</td>
      <td></td>
      <td>0.00088 (1.6e-5)</td>
      <td>0.00084 (1.5e-5)</td>
      <td>0.00054 (8.4e-6)</td>
      <td>0.0021 (6.2e-5)</td>
    </tr>
    <tr>
      <td>17</td>
      <td>79,478</td>
      <td></td>
      <td>0.0012 (2.3e-5)</td>
      <td>0.0011 (2.0e-5)</td>
      <td>0.00069 (1.1e-5)</td>
      <td>0.0021 (6.0e-5)</td>
    </tr>
    <tr>
      <td>18</td>
      <td>87,105</td>
      <td></td>
      <td>0.0010 (1.8e-5)</td>
      <td>0.00095 (1.7e-5)</td>
      <td>0.00058 (9.2e-6)</td>
      <td>0.0023 (6.8e-5)</td>
    </tr>
    <tr>
      <td>19</td>
      <td>72,794</td>
      <td></td>
      <td>0.0012 (2.3e-05)</td>
      <td>0.0012 (2.1e-5)</td>
      <td>0.00082 (1.4e-5)</td>
      <td>0.0022 (6.2e-5)</td>
    </tr>
    <tr>
      <td>20</td>
      <td>68,881</td>
      <td></td>
      <td>0.0014 (2.6e-5)</td>
      <td>0.0015 (2.7e-5)</td>
      <td>0.00078 (1.3e-5)</td>
      <td>0.0024 (7.0e-5)</td>
    </tr>
    <tr>
      <td>21</td>
      <td>45,068</td>
      <td></td>
      <td>0.0018 (3.4e-5)</td>
      <td>0.0017 (3.2e-5)</td>
      <td>0.00098 (1.7e-5)</td>
      <td>0.0024 (7.1e-5)</td>
    </tr>
    <tr>
      <td>22</td>
      <td>40,378</td>
      <td></td>
      <td>0.0016 (3.1e-5)</td>
      <td>0.0016 (2.9e-5)</td>
      <td>0.0010 (1.8e-5)</td>
      <td>0.0027 (8.1e-5)</td>
    </tr>
  </tbody>
</table>

_Each l^i and its standard error are in parentheses, as estimated in Equation 7.SNP, single-nucleotide polymorphism._

**Table 5.**
 LD decay regression analysis for 26 cohorts.


<table>
  <thead>
    <tr>
      <th rowspan="2">Cohort (n)</th>
      <th colspan="3">LD-decay regression*</th>
      <th colspan="3">Population parameters†</th>
      <th></th>
    </tr>
    <tr>
      <th>b^0</th>
      <th>b^1</th>
      <th>R</th>
      <th>LD decay score</th>
      <th>Fst¯ (%)</th>
      <th>Ancestry</th>
      <th>True LD ‡</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>MSL (85)</td>
      <td>0.00041</td>
      <td>29.97</td>
      <td>0.84</td>
      <td>0.0421</td>
      <td>0.013</td>
      <td>AFR</td>
      <td>0.62727273</td>
    </tr>
    <tr>
      <td>GWD (113)</td>
      <td>0.00031</td>
      <td>30.17</td>
      <td>0.83</td>
      <td>0.0439</td>
      <td>0.009</td>
      <td>AFR</td>
      <td>0.65934066</td>
    </tr>
    <tr>
      <td>YRI (107)</td>
      <td>0.00030</td>
      <td>30.64</td>
      <td>0.85</td>
      <td>0.0436</td>
      <td>0.010</td>
      <td>AFR</td>
      <td>0.66292135</td>
    </tr>
    <tr>
      <td>ESN (99)</td>
      <td>0.00037</td>
      <td>34.82</td>
      <td>0.87</td>
      <td>0.0436</td>
      <td>0.011</td>
      <td>AFR</td>
      <td>0.65420561</td>
    </tr>
    <tr>
      <td>ACB (96)</td>
      <td>0.00053</td>
      <td>39.62</td>
      <td>0.88</td>
      <td>0.0451</td>
      <td>0.021</td>
      <td>AFR</td>
      <td>0.63194444</td>
    </tr>
    <tr>
      <td>LWK (99)</td>
      <td>0.00046</td>
      <td>40.52</td>
      <td>0.92</td>
      <td>0.0447</td>
      <td>0.014</td>
      <td>AFR</td>
      <td>0.64615385</td>
    </tr>
    <tr>
      <td>ASW (61)</td>
      <td>0.0015</td>
      <td>46.88</td>
      <td>0.83</td>
      <td>0.0472</td>
      <td>0.031</td>
      <td>AFR</td>
      <td>0.57142857</td>
    </tr>
    <tr>
      <td>CHS (105)</td>
      <td>0.00046</td>
      <td>52.36</td>
      <td>0.87</td>
      <td>0.0555</td>
      <td>0.010</td>
      <td>EA</td>
      <td>0.67375887</td>
    </tr>
    <tr>
      <td>CDX (93)</td>
      <td>0.00055</td>
      <td>53.77</td>
      <td>0.83</td>
      <td>0.0557</td>
      <td>0.012</td>
      <td>EA</td>
      <td>0.66666667</td>
    </tr>
    <tr>
      <td>KHV (99)</td>
      <td>0.00044</td>
      <td>53.79</td>
      <td>0.87</td>
      <td>0.0560</td>
      <td>0.011</td>
      <td>EA</td>
      <td>0.68345324</td>
    </tr>
    <tr>
      <td>CHB (103)</td>
      <td>0.00041</td>
      <td>54.90</td>
      <td>0.90</td>
      <td>0.0558</td>
      <td>0.010</td>
      <td>EA</td>
      <td>0.69402985</td>
    </tr>
    <tr>
      <td>JPT (104)</td>
      <td>0.00045</td>
      <td>57.75</td>
      <td>0.85</td>
      <td>0.0568</td>
      <td>0.010</td>
      <td>EA</td>
      <td>0.68965517</td>
    </tr>
    <tr>
      <td>BEB (86)</td>
      <td>0.00045</td>
      <td>48.84</td>
      <td>0.88</td>
      <td>0.0556</td>
      <td>0.012</td>
      <td>SA</td>
      <td>0.66911765</td>
    </tr>
    <tr>
      <td>ITU (102)</td>
      <td>0.00048</td>
      <td>49.58</td>
      <td>0.89</td>
      <td>0.0546</td>
      <td>0.016</td>
      <td>SA</td>
      <td>0.66433566</td>
    </tr>
    <tr>
      <td>STU (102)</td>
      <td>0.00055</td>
      <td>52.84</td>
      <td>0.89</td>
      <td>0.0546</td>
      <td>0.015</td>
      <td>SA</td>
      <td>0.64516129</td>
    </tr>
    <tr>
      <td>PJL (96)</td>
      <td>0.00054</td>
      <td>54.00</td>
      <td>0.90</td>
      <td>0.0546</td>
      <td>0.017</td>
      <td>SA</td>
      <td>0.67073171</td>
    </tr>
    <tr>
      <td>GIH (103)</td>
      <td>0.00057</td>
      <td>55.81</td>
      <td>0.91</td>
      <td>0.0562</td>
      <td>0.017</td>
      <td>SA</td>
      <td>0.65868263</td>
    </tr>
    <tr>
      <td>TSI (107)</td>
      <td>0.00041</td>
      <td>53.17</td>
      <td>0.91</td>
      <td>0.0558</td>
      <td>0.010</td>
      <td>EUR</td>
      <td>0.68939394</td>
    </tr>
    <tr>
      <td>IBS (107)</td>
      <td>0.00039</td>
      <td>54.22</td>
      <td>0.92</td>
      <td>0.0555</td>
      <td>0.010</td>
      <td>EUR</td>
      <td>0.7</td>
    </tr>
    <tr>
      <td>CEU (99)</td>
      <td>0.00045</td>
      <td>54.23</td>
      <td>0.89</td>
      <td>0.0559</td>
      <td>0.011</td>
      <td>EUR</td>
      <td>0.68085106</td>
    </tr>
    <tr>
      <td>GBR (91)</td>
      <td>0.00047</td>
      <td>58.23</td>
      <td>0.91</td>
      <td>0.0555</td>
      <td>0.012</td>
      <td>EUR</td>
      <td>0.68027211</td>
    </tr>
    <tr>
      <td>FIN (99)</td>
      <td>0.00054</td>
      <td>59.24</td>
      <td>0.86</td>
      <td>0.0579</td>
      <td>0.011</td>
      <td>EUR</td>
      <td>0.67073171</td>
    </tr>
    <tr>
      <td>MXL (64)</td>
      <td>0.0014</td>
      <td>66.13</td>
      <td>0.89</td>
      <td>0.0558</td>
      <td>0.036</td>
      <td>AMR</td>
      <td>0.6</td>
    </tr>
    <tr>
      <td>PUR (104)</td>
      <td>0.00059</td>
      <td>67.20</td>
      <td>0.89</td>
      <td>0.0571</td>
      <td>0.014</td>
      <td>AMR</td>
      <td>0.67039106</td>
    </tr>
    <tr>
      <td>CLM (94)</td>
      <td>0.00069</td>
      <td>75.97</td>
      <td>0.95</td>
      <td>0.0572</td>
      <td>0.017</td>
      <td>AMR</td>
      <td>0.66985646</td>
    </tr>
    <tr>
      <td>PEL (85)</td>
      <td>0.0012</td>
      <td>78.15</td>
      <td>0.85</td>
      <td>0.0598</td>
      <td>0.028</td>
      <td>AMR</td>
      <td>0.61290323</td>
    </tr>
    <tr>
      <td>1KG (2503)</td>
      <td>0.0061</td>
      <td>40.65</td>
      <td>0.55</td>
      <td></td>
      <td>0.066</td>
      <td>Mixed</td>
      <td>0.51587302</td>
    </tr>
  </tbody>
</table>

_LD, linkage disequilibrium; SNP, single-nucleotide polymorphism.*The regression intercept b^0 and the coefficients b^1 are as represented in Equation 3.†The column for LD decay score was taken as the mean of the estimated r2-1n from PopLDdecay in a physical distance of 1500 kb, which was approximated to the area under the curve in Figure 5A for each cohort; Fst was approximated by λ1n , in which λ1 the largest eigenvalue for the cohort. r2 was the estimated LD statistic from PLINK (--r2).‡True LD is defined as l¯^i⋅jl¯^i⋅j+b^0 ._

A common feature was universally relative high LD of chromosome 6 and 11 in the 26 1KG cohorts (Figure 5—figure supplement 1). We quantified the impact of chromosome 6 and 11 by leave-one-chromosome-out test in CEU, CHB, YRI, and ASW for details (Figure 6A and B) and found that dropping chromosome 6 off could lift $R$ on average by 0.017 and chromosome 11 by 0.046. One possible explanation was that the centromere regions of chromosomes 6 and 11 have been assembled more completely than other chromosomes before the completion of CHM13 (Hoyt et al., 2022), whereas meiotic recombination tended to be reduced around the centromeres (Hinch et al., 2019). We estimated $l_{i}$ after having knocked out the centromere region (46,061,947–59,413,484 bp, chr 11) in CEU, CHB, YRI, and ASW, and chromosome 11 then did not deviate much from their respective fitted lines (Figure 6C). A notable exceptional pattern was found in ASW, chromosome 8 of which had even more deviation than chromosome 11 ($R$ was 0.83 and 0.87 with and without chromosome 8 in leave-one-chromosome out test) (Figure 6B). The deviation of chromosome 8 of ASW was consistent even more SNPs were added (Figure 6—figure supplement 1). We also provided high-resolution LD grids illustration for chromosome 8 (163,436 SNPs, totaling 214,185 grids) of the four representative cohorts for more detailed virtualization (Figure 6D). ASW had $l^_{8}=$ 0.0022, but 0.00075, 0.00069, and 0.00043 for CEU, CHB, and YRI, respectively.

![Figure 6.](https://cdn.elifesciences.org/articles/90636/elife-90636-fig6-v2.jpg)

**Figure 6.:** The correlation between the inversion of the single-nucleotide polymorphism (SNP) number and $l^_{i}$.(A) The correlation between the inversion of the SNP number and $l^_{i}$ in CEU, CHB, YRI, and ASW. (B) Leave-one-chromosome-out strategy is adopted to evaluate the contribution of a certain chromosome on the correlation between the inverse of the SNP number and $l^_{i}$ . (C) The correlation between the inversion of the SNP number and chromosomal linkage disequilibrium (LD) in CEU, CHB, YRI, and ASW after removing the centromere region of chromosome 11. (D) High-resolution illustration for LD grids for chromosome 8 in CEU, CHB, YRI, and ASW. For each cohort, we partition chromosome 8 into consecutive LD grids (each LD grid contains 250 ×250 SNP pairs). For visualization purposes, LD is transformed to a -log10-scale, with smaller values (red hues) representing larger LD, and a value of 0 representing that all SNPs are in LD.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/90636/elife-90636-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** Randomly selected SNPs that were presented in ASW but were not 2,997,635 consensus SNPs were added to the ASW cohort to demonstrate the stable pattern of chromosome 8.

## Discussion

In this study, we present a computationally efficient method to estimate the mean LD of genomic grids of many SNP pairs. Our LD analysis framework is based on GRM, which has been embedded in variance component analysis for complex traits and genomic selection (Goddard, 2009; Visscher et al., 2014; Chen, 2014). The key connection from GRM to LD is bridged via the transformation between $n\timesn$ matrix and $m\timesm$ matrix, in particular here via Isserlis’s theorem under the fourth-order moment (Isserlis, 1918). With this connection, the computational cost for estimating the mean LD of $m\timesm$ SNP pairs is reduced from $O(nm^{2})$ to $O(n^{2}m)$, and the statistical properties of the proposed method are derived in theory and validated in 1KG datasets. In addition, as the genotype matrix $X$ is of limited entries {0, 1, 2}, assuming missing genotypes are imputed first, using Mailman algorithm the computational cost of GRM can be further reduced to $O(\frac{n^{2}m}{log_{3}⁡m})$ (Liberty and Zucker, 2009). The largest data tested so far for the proposed method has a sample size of 10,640 and more than 5 million SNPs, so it can complete genomic LD analysis in 77,508.00 s (Table 1). The weakness of the proposed method is obvious that the algorithm remains slow when the sample size is large or the grid resolution is increased. With the availability of such a UK Biobank data (Bycroft et al., 2018), the proposed method may not be adequate, and much advanced methods, such as randomized implementation for the proposed methods, are needed.

We also applied the proposed method into 1KG and revealed certain characteristics of the human genomes. Firstly, we found the ubiquitous existence of extended LD, which likely emerged because of population structure, even very slightly, and admixture history. We quantified the $l^_{i}$ and $l^_{i⋅j}$ in 1KG, and as indicated by $l∼_{i⋅j}$ we found that the inter-chromosomal LD was nearly an order lower than intra-chromosomal LD; for admixed cohorts, the ratio was much higher, even very close to each other such as in all 1KG samples. Secondly, variable recombination rates shaped peak of local LD. For example, the HLA region showed high LD in the European and East Asian cohorts, but relatively low LD in such as YRI, consistent with their much longer population history. Thirdly, there existed a general linear correlation between $l_{i}$ and the inversion of the SNP number, a long-anticipated result that is as predicted with genome-wide spread of recombination hotspots (Hinch et al., 2019). One outlier of this linear norm was chromosome 11, which had so far the most completely genotyped centromere and consequently had more elevated LD compared with other autosomes. We anticipate that with the release of CHM13 the linear correlation should be much closer to unity (Hoyt et al., 2022). Of note, under the variance component analysis for complex traits, it is often a positive correlation between the length of a chromosome (as surrogated by the number of SNPs) and the proportion of heritability explained (Chen et al., 2014).

In contrast, throughout the study recurrent outstanding observations were found in ASW. For example, in ASW the ratio of $l^_{HLA}/l^_{6}$ substantially dropped compared with that of CEU, CHB, or YRI as illustrated in Figure 4. Furthermore, chromosome 8 in ASW fluctuated upward most from the linear correlation (Figure 6) even after various analyses, such as expanding SNP numbers. One possible explanation may lie under the complex demographic history of ASW, which can be investigated and tested in additional African American samples or possible existence for epistatic fitness (Ni et al., 2020).
