# Discovering and deciphering relationships across disparate data modalities

## Authors

- Joshua T Vogelstein<sup>1</sup> ([ORCID: 0000-0003-2487-6237](https://orcid.org/0000-0003-2487-6237)) †
- Eric W Bridgeford<sup>1</sup>
- Qing Wang<sup>1</sup>
- Carey E Priebe<sup>1</sup>
- Mauro Maggioni<sup>1</sup>
- Cencheng Shen<sup>3</sup> ([ORCID: 0000-0003-1030-1432](https://orcid.org/0000-0003-1030-1432))

### Affiliations

1. Johns Hopkins University Baltimore United States
2. Child Mind Institute New York United States
3. University of Delaware Delaware United States

† Corresponding author

## Abstract

Understanding the relationships between different properties of data, such as whether a genome or connectome has information about disease status, is increasingly important. While existing approaches can test whether two properties are related, they may require unfeasibly large sample sizes and often are not interpretable. Our approach, ‘Multiscale Graph Correlation’ (MGC), is a dependence test that juxtaposes disparate data science techniques, including k-nearest neighbors, kernel methods, and multiscale analysis. Other methods may require double or triple the number of samples to achieve the same statistical power as MGC in a benchmark suite including high-dimensional and nonlinear relationships, with dimensionality ranging from 1 to 1000. Moreover, MGC uniquely characterizes the latent geometry underlying the relationship, while maintaining computational efficiency. In real data, including brain imaging and cancer genetics, MGC detects the presence of a dependency and provides guidance for the next experiments to conduct.

## Introduction

Identifying the existence of a relationship between a pair of properties or modalities is the critical initial step in data science investigations. Only if there is a statistically significant relationship does it make sense to try to decipher the nature of the relationship. Discovering and deciphering relationships is fundamental, for example, in high-throughput screening (Zhang et al., 1999), precision medicine (Prescott, 2013), machine learning (Hastie et al., 2001), and causal analyses (Pearl, 2000). One of the first approaches for determining whether two properties are related to—or statistically dependent on—each other is Pearson’s Product-Moment Correlation (published in 1895; Pearson, 1895). This seminal paper prompted the development of entirely new ways of thinking about and quantifying relationships (see Reimherr and Nicolae, 2013 and Josse and Holmes, 2013 for recent reviews and discussion). Modern datasets, however, present challenges for dependence-testing that were not addressed in Pearson’s era. First, we now desire methods that can correctly detect any kind of dependence between all kinds of data, including high-dimensional data (such as ’omics), structured data (such as images or networks), with nonlinear relationships (such as oscillators), even with very small sample sizes as is common in modern biomedical science. Second, we desire methods that are interpretable by providing insight into how or why they discovered the presence of a statistically significant relationship. Such insight can be a crucial component of designing the next computational or physical experiment.

While many statistical and machine learning approaches have been developed over the last 120 years to combat aspects of the first issue—detecting dependencies—no approach satisfactorily addressed the challenges across all data types, relationships, and dimensionalities. Hoeffding and Renyi proposed non-parametric tests to address nonlinear but univariate relationships (Hoeffding, 1948; Rényi, 1959). In the 1970s and 1980s, nearest neighbor style approaches were popularized (Friedman and Rafsky, 1983; Schilling, 1986), but they were sensitive to algorithm parameters resulting in poor empirical performance. ‘Energy statistics’, and in particular the distance correlation test (Dcorr), was recently shown to be able to detect any dependency with sufficient observations, at arbitrary dimensions, and structured data under a proper distance metric (Székely et al., 2007; Székely and Rizzo, 2009; Szekely and Rizzo, 2013; Lyons, 2013). Another set of methods, referred to a ‘kernel mean embedding’ approaches, including the Hilbert Schmidt Independence Criterion (Hsic) (Gretton and Gyorfi, 2010; Muandet et al., 2017), have the same theoretical guarantees, which is shown to be a kernel version of the energy statistics (Sejdinovic et al., 2013; Shen and Vogelstein, 2018). The energy statistics can perform very well with a relatively small sample size on high-dimensional linear data, whereas the kernel methods and another test (Heller, Heller, and Gorfine’s test, Hhg) (Heller et al., 2013) perform well on low-dimensional nonlinear data. But no test performs particularly well on high-dimensional nonlinear data with typical sample sizes, which characterizes a large fraction of real data challenges in the current big data era.

Moreover, to our knowledge, existing dependency tests do not attempt to further characterize the dependency structure. On the other hand, much effort has been devoted to characterizing ‘point cloud data’, that is, summarizing certain global properties in unsupervised settings (for example, having genomics data, but no disease data). Classic examples of such approaches include Fourier (Bracewell and Bracewell, 1986) and wavelet analysis (Daubechies, 1992). More recently, topological and geometric data analysis compute properties of graphs, or even higher order simplices (Edelsbrunner and Harer, 2009). Such methods build multiscale characterization of the samples, much like recent developments in harmonic analysis (Coifman and Maggioni, 2006; Allard et al., 2012). However, these tools typically lack statistical guarantees under noisy observations and are often computationally burdensome.

We surmised that both (i) empirical performance in all dependency structures, in particular high-dimensional, nonlinear, low-sample size settings, and (ii) providing insight into the discovery process, can be addressed via extending existing dependence tests to be adaptive to the data (Zhang et al., 2012). Existing tests rely on a fixed a priori selection of an algorithmic parameter, such as the kernel bandwidth (Gretton et al., 2006), intrinsic dimension (Allard et al., 2012), and/or local scale (Friedman and Rafsky, 1983; Schilling, 1986). Indeed, the Achilles Heel of manifold learning has been the requirement to manually choose these parameters (Levina and Bickel, 2004). Post-hoc cross-validation is often used to make these methods effectively adaptive, but doing so adds an undesirable computational burden and may weaken or destroy any statistical guarantees. There is therefore a need for statistically valid and computationally efficient adaptive methods.

To illustrate the importance of adapting to different kinds of relationships, consider a simple illustrative example: investigate the relationship between cloud density and grass wetness. If this relationship were approximately linear, the data might look like those in Figure 1A (top). On the other hand, if the relationship were nonlinear—such as a spiral—it might look like those in Figure 1A (bottom). Although the relationship between clouds and grass is unlikely to be spiral, spiral relationships are prevalent in nature and mathematics (for example, shells, hurricanes, and galaxies), and are canonical in evaluations of manifold learning techniques (Lee and Verleysen, 2007), thereby motivating its use here.

![Figure 1.](https://cdn.elifesciences.org/articles/41690/elife-41690-fig1-v2.jpg)

**Figure 1.:** Illustration of Multiscale Graph Correlation (Mgc) on simulated cloud density ($x_{i}$) and grass wetness ($y_{i}$).We present two different relationships: linear (top) and nonlinear spiral (bottom; see Materials and methods for simulation details). (A) Scatterplots of the raw data using $50$ pairs of samples for each scenario. Samples $1$, $2$, and $3$ (black) are highlighted; arrows show $x$ distances between these pairs of points while their $y$ distances are almost 0. (B) Scatterplots of all pairs of distances comparing $x$ and $y$ distances. Distances are linearly correlated in the linear relationship, whereas they are not in the spiral relationship. Dcorr uses all distances (gray dots) to compute its test statistic and p-value, whereas Mgc chooses the local scale and then uses only the local distances (green dots). (C) Heatmaps characterizing the strength of the generalized correlation at all possible scales (ranging from $2$ to $n$ for both $x$ and $y$). For the linear relationship, the global scale is optimal, which is the scale that Mgc selects and results in a p-value identical to Dcorr. For the nonlinear relationship, the optimal scale is local in both $x$ and $y$, so Mgc achieves a far larger test statistic, and a correspondingly smaller and significant p-value. Thus, Mgc uniquely detects dependence and characterizes the geometry in both relationships.

Under the linear relationship (top panels), when a pair of observations are close to each other in cloud density, they also tend to be close to each other in grass wetness (for example, observations 1 and 2 highlighted in black in Figure 1A, and distances between them in Figure 1B). Similarly, when a pair of observations are far from each other in cloud density, they also tend to be far from each other in grass wetness (see for example, distances between observations 2 and 3). On the other hand, consider the nonlinear (spiral) relationship (bottom panels). Here, when a pair of observations are close to each other in cloud density, they also tend to be close to each other in grass wetness (see points 1 and 2 again). However, the same is not true for large distances (see points 2 and 3). Thus, in the linear relationship, the distance between every pair of points is informative with respect to the relationship, while under the nonlinear relationship, only a subset of the distances are.

For this reason, we juxtapose nearest neighbor mechanism with distance methods. Specifically, for each point, we find its $k$-nearest neighbors for one property (e.g. cloud density), and its $l$-nearest neighbors for the other property (e.g. grass wetness); we call the pair $(k,l)$ the ‘scale’. A priori, however, we do not know which scales will be most informative. We compute all distance pairs, then efficiently compute the distance correlations for all scales. The local correlations (Figure 1C, described in detail below) illustrate which scales are relatively informative about the relationship. The key, therefore, to successfully discover and decipher relationships between disparate data modalities is to adaptively determine which scales are the most informative, and the geometric implication for the most informative scales. Doing so not only provides an estimate of whether the modalities are related, but also provides insight into how the determination was made. This is especially important in high-dimensional data, where simple visualizations do not reveal relationships to the unaided human eye.

Our method, ‘Multiscale Graph Correlation’ (Mgc, pronounced ‘magic’), generalized and extends previously proposed pairwise comparison-based approaches by adaptively estimating the informative scales for any relationship — linear or nonlinear, low-dimensional or high-dimensional, unstructured or structured—in a computationally efficient and statistically valid and consistent fashion. This adaptive nature of Mgc effectively guarantees an improved statistical performance. Moreover, the dependency strength across all scales is informative about the structure of a statistical relationship, therefore providing further guidance for subsequent experimental or analytical steps. Mgc is thus a hypothesis-testing and insight-providing approach that builds on recent developments in manifold and kernel learning, with complementary developments in nearest-neighbor search, and multiscale analyses.

### The multiscale graph correlation procedure

Mgc is a multi-step procedure to discover and decipher dependencies across disparate data modalities or properties. Given $n$ samples of two different properties, proceed as follows (see Materials and methods and (Shen et al., 2018) for details):

Computing all local correlations, the test statistic, and the p-value requires $O(n^{2}log⁡n)$ time, which is about the same running time complexity as other methods (Shen et al., 2018).

## Results

### Mgc typically requires substantially fewer samples to achieve the same power across all dependencies and dimensions

When, and to what extent, does Mgc outperform other approaches, and when does it not? To address this question, we formally pose the following hypothesis test (see Materials and methods for details):

$$
H_{0}:XandYare independentH_{A}:XandYare not independent.
$$

The standard criterion for evaluating statistical tests is the testing power, which equals the probability that a test correctly rejects the null hypothesis at a given type one error level, that is power = Prob($H_{0}$ is rejected $|H_{0}$ is false). The higher the testing power, the better the test procedure. A consistent test has power converging to $1$ under dependence, and a valid test controls the type one error level under independence. In a complementary manuscript (Shen et al., 2018), we established the theoretical properties of Mgc, proving its validity and universal consistency for dependence testing against all distributions of finite second moments.

Here, we address the empirical performance of Mgc as compared with multiple popular tests: (i) Dcorr, a popular approach from the statistics community (Székely et al., 2007; Székely and Rizzo, 2009), (ii) Mcorr, a modified version of Dcorr designed to be unbiased for sample data (Szekely and Rizzo, 2013), (iii) Hhg, a distance-based test that is very powerful for detecting low-dimensional nonlinear relationships (Heller et al., 2013). (iv) Hsic, a kernel dependency measure (Gretton and Gyorfi, 2010) formulated in the same way as Dcorr except operating on kernels, (v) Mantel, which is historically widely used in biology and ecology (Mantel, 1967). (vi) RV coefficient (Pearson, 1895; Josse and Holmes, 2013), which is a multivariate generalization of Pearson’s product moment correlation whose test statistic is the sum of the trace-norm of the cross-covariance matrix, and (vii) the Cca method, which is the largest (in magnitude) singular value of the cross-covariance matrix, and can be viewed as a different generalization of Pearson in high-dimensions that is more appropriate for sparse settings (Hotelling, 1936; Witten et al., 2009; Witten and Tibshirani, 2011). Note that while we focus on high-dimensional settings, Appendix 1 shows further results in one-dimensional settings, also comparing to a number of tests that are limited to one dimension, including: (viii) Pearson’s product moment correlation, (ix) Spearman’s rank correlation (Spearman, 1904), (x) Kendall’s tau correlation (Kendall, 1970), and (xi) Mic (Reshef et al., 2011). Under the regularity condition that the data distribution has finite second moment, the first four tests are universally consistent, whereas the other tests are not.

We generate an extensive benchmark suite of 20 relationships, including different polynomial (linear, quadratic, cubic), trigonometric (sinusoidal, circular, ellipsoidal, spiral), geometric (square, diamond, W-shape), and other functions. This suite includes and extends the simulated settings from previous dependence testing work (Székely et al., 2007; Simon and Tibshirani, 2012; Gorfine et al., 2012; Heller et al., 2013; Szekely and Rizzo, 2013). For many of them, we introduce high-dimensional variants, to more extensively evaluate the methods; function details are in Materials and methods. The visualization of one-dimensional noise-free (black) and noisy (gray) samples is shown in Figure 2—figure supplement 1. For each relationship, we compute the power of each method relative to Mgc for ~20 different dimensionalities, ranging from 1 up to 10, 20, 40, 100, or 1000. The high-dimensional relationships are more challenging because (1) they cannot be easily visualized and (2) each dimension is designed to have less and less signal, so there are many noisy dimensions. Figure 2 shows that Mgc achieves the highest (or close to the highest) power given 100 samples for each relationship and dimensionality. Figure 2—figure supplement 2 shows the same advantage in one-dimension with increasing sample size.

![Figure 2.](https://cdn.elifesciences.org/articles/41690/elife-41690-fig2-v2.jpg)

**Figure 2.:** Each panel shows the testing power of other methods relative to the power of Mgc (e.g. power of Mcorr minus the power of Mgc) at significance level $\alpha=0.05$ versus dimensionality for $n=100$. Any line below zero at any point indicates that that method’s power is less than Mgc’s power for the specified setting and dimensionality. Mgc achieves empirically better (or similar) power than all other methods in almost all relationships and all dimensions. For the independent relationship (#20), all methods yield power $0.05$ as they should. Note that Mgc is always plotted ‘on top’ of the other methods, therefore, some lines are obscured.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/41690/elife-41690-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Visualization of the $20$ dependencies at $p=q=1$.For each, $n=100$ points are sampled with noise ($κ=1$) to show the actual sample data used for one-dimensional relationships (gray dots). For comparison purposes, $n=1000$ points are sampled without noise ($κ=0$) to highlight each underlying dependency (black dots). Note that only black points are plotted for type 19 and 20, as they do not have the noise parameter $κ$.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/41690/elife-41690-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** Mgc empirically achieves similar or better power than the previous state-of-the-art approaches on most problems. Note that Mic is included in 1D case; RV and Cca both equal Pearson in 1D; Kendall and Spearman are too similar to Pearson in power and thus omitted in plotting.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/41690/elife-41690-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** The default Mgc builds upon Mcorr throughout the paper, and we further consider Mgc on Mantel to illustrate the generalization. The magenta line shows the power difference between Mcorr and Mgc , and the cyan line shows the power difference between Mantel and the Mgc version of Mantel. Indeed, Mgc is able to improve the global counterpart in testing power under nonlinear dependencies, and maintains similar power under linear and independent dependencies.

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/41690/elife-41690-fig2-figsupp4-v2.jpg)

Moreover, for each relationship and each method we compute the required sample size to achieve power 85% at error level 0.05, and summarize the median size for monotone relationships (type 1–5) and non-monotone relationships (type 6–19) in Table 1. Other methods typically require double or triple the number of samples as Mgc to achieve the same power. More specifically, traditional correlation methods (Pearson, RV, Cca, Spearman, Kendall) always perform the best in monotonic simulations, distance-based methods including Mcorr, Dcorr, Mgc, Hhg and Hsic are slightly worse, while Mic and Mantel are the worst. Mgc’s performance is equal to linear methods on monotonic relationships. For non-monotonic relationships, traditional correlations fail to detect the existence of dependencies, Dcorr, Mcorr, and Mic, do reasonably well, but Hhg and Mgc require the fewest samples. In the high-dimensional non-monotonic relationships that motivated this work, and are common in biomedicine, Mgc significantly outperforms other methods. The second best test that is universally consistent (Hhg) requires nearly double as many samples as Mgc, demonstrating that Mgc could half the time and cost of experiments designed to discover relationships at a given effect size.

Mgc extends previously proposed global methods, such as Mantel and Dcorr . The above experiments extended Mcorr , because Mcorr is universally consistent and an unbiased version of Dcorr (Szekely and Rizzo, 2013). Figure 2—figure supplement 3 directly compares multiscale generalizations of Mantel and Mcorr as dimension increases, demonstrating that empirically, Mgc nearly dominates its global variant for essen- tially all dimensions and simulation settings considered here. Figure 2—figure supplement 4 shows a similar result for one-dimensional settings while varying sample size. Thus, not only does Mgc empirically nearly dominate existing tests, it is a framework that one can apply to future tests to further improve their performance.

**Table 1.**
 The median sample size for each method to achieve power 85% at type one error level 0.05, grouped into monotone (type 1–5) and non-monotone relationships (type 6–19) for both one- and ten-dimensional settings, normalized by the number of samples required by Mgc.In other words, a 2.0 indicates that the method requires double the sample size to achieve 85% power relative to Mgc. Pearson, Rv, and Cca all achieve the same performance, as do Spearman and Kendall. Mgc requires the fewest number of samples in all settings, and for high-dimensional non-monotonic relationships, all other methods require about double or triple the number of samples Mgc requires.Table 1—source data 1.Testing power sample size data in one dimension.Table 1—source data 2.Testing power sample size data in high-dimensions.


<table>
  <thead>
    <tr>
      <th>Dimensionality</th>
      <th colspan="3">One-Dimensional</th>
      <th colspan="3">Ten-Dimensional</th>
    </tr>
    <tr>
      <th>Dependency type</th>
      <th>Monotone</th>
      <th>Non-Mono</th>
      <th>Average</th>
      <th>Monotone</th>
      <th>Non-Mono</th>
      <th>Average</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Mgc</td>
    </tr>
    <tr>
      <td>1</td>
      <td>2.6</td>
      <td>2.2</td>
      <td>1</td>
      <td>3.2</td>
      <td>2.6</td>
      <td>Dcorr</td>
    </tr>
    <tr>
      <td>1</td>
      <td>2.8</td>
      <td>2.4</td>
      <td>1</td>
      <td>3.1</td>
      <td>2.6</td>
      <td>Mcorr</td>
    </tr>
    <tr>
      <td>1.4</td>
      <td>1</td>
      <td>1.1</td>
      <td>1.7</td>
      <td>1.9</td>
      <td>1.8</td>
      <td>Hhg</td>
    </tr>
    <tr>
      <td>1.4</td>
      <td>1.1</td>
      <td>1.2</td>
      <td>1.7</td>
      <td>2.4</td>
      <td>2.2</td>
      <td>Hsic</td>
    </tr>
    <tr>
      <td>1.4</td>
      <td>1.8</td>
      <td>1.7</td>
      <td>3</td>
      <td>1.6</td>
      <td>1.9</td>
      <td>Mantel</td>
    </tr>
    <tr>
      <td>1</td>
      <td>&gt;10</td>
      <td>&gt;10</td>
      <td>0.8</td>
      <td>&gt;10</td>
      <td>&gt;10</td>
      <td>Pearson / Rv / Cca</td>
    </tr>
    <tr>
      <td>1</td>
      <td>&gt;10</td>
      <td>&gt;10</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>Spearman / Kendall</td>
    </tr>
    <tr>
      <td>2.4</td>
      <td>2</td>
      <td>2.1</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>n/a</td>
      <td>Mic</td>
    </tr>
  </tbody>
</table>

### Mgc deciphers latent dependence structure

Beyond simply testing the existence of a relationship, the next goal is often to decipher the nature or structure of the relationship, thereby providing insight and guiding future experiments. A single scalar quantity (such as effect size) is inadequate given the vastness and complexities of possible relationships. Existing methods would require a secondary procedure to characterize the relationship, which introduces complicated ‘post selection’ statistical quandaries that remain mostly unresolved (Berk et al., 2013). Instead, Mgc provides a simple, intuitive, and nonparametric (and therefore infinitely flexible) 'map’ of how it discovered the relationship. As described below, this map not only provides interpretability for how Mgc detected a dependence, it also partially characterize the geometry of the investigated relationship.

The Mgc-Map shows local correlation as a function of the scales of the two properties. More concretely, it is the matrix of $c^{kl}$’s, as defined above. Thus, the Mgc-Map is an n-by-n matrix which encodes the strength of dependence for each possible scale. Figure 3 provides the Mgc-Map for all 20 different one-dimensional relationships; the optimal scale to achieve $t^_{*}$ is marked with a green dot. For the monotonic dependencies (1-5), the optimal scale is always the largest scale, that is the global one. For all non-monotonic dependencies (6-19), Mgc chooses smaller scales. Thus, a global optimal scale implies a close-to-linear dependency, otherwise the dependency is strongly nonlinear. In fact, this empirical observation led to the following theorem (which is proved in Materials and methods):

Theorem 1. When $(X,Y)$ are linearly related (meaning that $Y$ can be constructed from $X$ by rotation, scaling, translation, and/or reflection), the optimal scale of Mgc equals the global scale. Conversely, a local optimal scale implies a nonlinear relationship.

Thus, the Mgc-Map explains how Mgc discovers relationships, specifically, which scale has the most informative pairwise comparisons, and how that relates to the geometry of the relationship. Note that Mgc provides the geometric characterization ‘for free’, meaning that no separate procedure is required; therefore, Mgc provides both a valid test and information about the geometric relationship.

![Figure 3.](https://cdn.elifesciences.org/articles/41690/elife-41690-fig3-v2.jpg)

**Figure 3.:** For each of the 20 panels, the abscissa and ordinate denote the number of neighbors for $X$ and $Y$, respectively, and the color denotes the magnitude of each local correlation. For each simulation, the sample size is 60, and both $X$ and $Y$ are one-dimensional. Each dependency has a different Mgc-Map characterizing the geometry of dependence, and the optimal scale is shown in green. In linear or close-to-linear relationships (first row), the optimal scale is global, that is the green dot is in the top right corner. Otherwise the optimal scale is non-global, which holds for the remaining dependencies. Moreover, similar dependencies often share similar Mgc-Maps and similar optimal scales, such as (10) logarithmic and (11) fourth root, the trigonometric functions in (12) and (13 , 16) circle and (17) ellipse, and (14) square and (18) diamond. The Mgc-Maps for high-dimensional simulations are provided in Figure 3—figure supplement 1.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/41690/elife-41690-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** For each simulation, the sample size is 100, and the dimension is selected as the dimension such that Mgc has a testing power above 0.5. It has similar behavior and interpretation as the one-dimensional power maps in Figure 3, that is the linear relationships optimal scales are global, and similar dependencies share similar Mgc-Maps.

Moreover, similar dependencies have similar Mgc-Maps and often similar optimal scales. For example, logarithmic (10) and fourth root (11), although very different functions analytically, are geometrically similar, and yield very similar Mgc-Maps. Similarly, (12) and (13) are trigonometric functions, and they share a narrow range of significant local scales. Both circle (16) and ellipse (17), as well as square (14) and diamond (18), are closely related geometrically and also have similar Mgc-Maps. This indicates that the Mgc-Map partially characterizes the geometry of these relationships, differentiating different dependence structures and assisting subsequent analysis steps. Moreover, in Shen and Vogelstein, 2018, we proved that the sample Mgc-Map (which Mgc estimates) converges to the true Mgc-Map provided by the underlying joint distribution of the data. In other words, each relationship has a specific map that characterizes it based on its joint distribution, and Mgc is able to accurately estimate it via sample observations. The existence of a population level characterization of the joint distribution strongly differentiates Mgc from previously proposed multi-scale geometric or topological characterizations of data, such as persistence diagrams (Edelsbrunner and Harer, 2009).

#### Mgc is computationally efficient

Mgc does not incur large computational costs and has a similar complexity as existing methods. Though a naïve implementation of Mgc requires $𝒪(n^{4})$ operations, we devised a nested implementation that requires only $𝒪(n^{2}log⁡n)$ operations. Moreover, obtaining the Mgc-Map costs no additional computation, whereas other methods would require running a secondary computational step to decipher geometric properties of the relationship. Mgc can also trivially be parallelized, reducing computation to $𝒪(n^{2}log⁡n/T)$, where $T$ is the number of cores (see Algorithm C1 for details). Since $T$ is often larger than $log⁡n$, in practice, Mgc can be $𝒪(n^{2})$, meaning only a constant factor slower than Dcorr and Hsic, which is illustrated in Figure 6 of Shen and Vogelstein, 2018. For example, at sample size $n=5000$ and dimension $p=1$, on a typical laptop computer, Dcorr requires around 0.5 s to compute the test statistic, whereas Mgc requires no more than $5$ s. But the cost and time to obtain 2.5× more data (so Dcorr has same average power as Mgc) typically far exceeds a few seconds. In comparison, the cost to compute a persistence diagram is typically $𝒪(n^{3})$, which is orders of magnitude slower when $n>10$. The running time of each method on the real data experiments are reported in Materials and methods.

### Mgc uniquely reveals relationships in real data

Geometric intuition, numerical simulations, and theory all provide evidence that Mgc will be useful for real data discoveries. Nonetheless, real data applications provide another necessary ingredient to justify its use in practice. Below, we describe several real data applications where we have used Mgc to understand relationships in data that other methods were unable to provide.

#### Mgc discovers the relationships between brain and mental properties

The human psyche is of course dependent on brain activity and structure. Previous work has studied two particular aspects of our psyche: personality and creativity, developing quantitative metrics for evaluating them using structured interviews (Costa and McCrae, 1992; Jung et al., 2009). However, the relationship between brain activity and structure, and these aspects of our psyche, remains unclear (DeYoung et al., 2010; Xu and Potenza, 2012; Bjørnebekk et al., 2013; Sampaio et al., 2014). For example, prior work did not evaluate the relationship between entire brain connectivity and all five factors of the standard personality model (Costa and McCrae, 1992). We therefore utilized Mgc to investigate published open access data (see Materials and methods for details).

First, we analyzed the relationship between resting-state functional magnetic resonance (rs-fMRI) activity and personality (Adelstein et al., 2011). The first row of Table 2 compares the p-value of different methods, and Figure 4A shows the Mgc-Map for the sample data. Mgc is able to yield a significant p-value (< 0.05), whereas all previously proposed global dependence tests under consideration (Mantel, Dcorr, Mcorr, or Hhg) fail to detect dependence at a significance level of 0.05. Moreover, the Mgc-Map provides a characterization of the dependence, for which the optimal scale indicates that the dependency is strongly nonlinear. Interestingly, the Mgc-Map does not look like any of the 20 images from the simulated data, suggesting that the nonlinearity characterizing this dependency is more complex or otherwise different from those we have considered so far.

![Figure 4.](https://cdn.elifesciences.org/articles/41690/elife-41690-fig4-v2.jpg)

**Figure 4.:** (A) The Mgc-Map for brain activity versus personality. Mgc has a large test statistic and a significant p-value at the optimal scale (13, 4), while the global counterpart is non-significant. That the optimal scale is non-global implies a strongly nonlinear relationship. (B) The Mgc-Map for brain connectivity versus creativity. The image is similar to that of a linear relationship, and the optimal scale equals the global scale, thus both Mgc and Mcorr are significant in this case. (C) For each peptide, the x-axis shows the p-value for testing dependence between pancreatic and healthy subjects by Mgc, and the y-axis shows the p-value for testing dependence between pancreatic and all other subjects by Mgc. At critical level $0.05$, Mgc identifies a unique protein after multiple testing adjustment. (D) The true and false positive counts using a k-nearest neighbor (choosing the best $k\in[1,10]$) leave-one-out classification using only the significant peptides identified by each testing method. The peptide identified by Mgc achieves the best true and false positive rates, as compared to the peptides identified by Hsic or Hhg.

**Table 2.**
 The p-values for brain imaging vs mental properties.Mgc always uncovers the existence of significant relationships and discovers the underlying optimal scales. Bold indicates significant p-value per dataset.Table 2—source data 1.p-value data for activity vs personality.Table 2—source data 2.p-value data for connetivity vs creativity.


<table>
  <thead>
    <tr>
      <th>Testing Pairs/Methods</th>
      <th>Mgc</th>
      <th>Dcorr</th>
      <th>Mcorr</th>
      <th>Hhg</th>
      <th>Hsic</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Activity vs Personality</td>
      <td>0.043</td>
      <td>0.667</td>
      <td>0.441</td>
      <td>0.059</td>
      <td>0.124</td>
    </tr>
    <tr>
      <td>Connectivity vs Creativity</td>
      <td>0.011</td>
      <td>0.010</td>
      <td>0.011</td>
      <td>0.031</td>
      <td>0.092</td>
    </tr>
  </tbody>
</table>

Second, we investigated the relationship between diffusion MRI derived connectivity and creativity (Jung et al., 2009). The second row of Table 2 shows that Mgc is able to ascertain a dependency between the whole brain network and the subject’s creativity. The Mgc-Map in Figure 4B closely resembles a linear relationship where the optimal scale is global. The close-to-linear relationship is also supported from the p-value table as all methods except Hsic are able to detect significant dependency, which suggests that there is relatively little to gain by pursuing nonlinear regression techniques, potentially saving valuable research time by avoiding tackling an unnecessary problem. The test statistic for both Mgc and Mcorr equal 0.04, which is quite close to zero despite a significant p-value, implying a relatively weak and noisy relationship. A prediction of creativity via linear regression turns out to be non-significant, which implies that the sample size is too low to obtain useful predictive accuracy (not shown), indicating that more data are required for single subject predictions. If one had first directly estimated the regression function, obtaining a null result, it would remain unclear whether a relationship existed. This experiment demonstrates that for high-dimensional and potentially structured data, Mgc is able to reveal dependency with relatively small sample size while parametric techniques and directly estimating regression functions can often be ineffective.

The performance in the real data closely matches the simulations results: the first dataset exhibits a strongly nonlinear relationship, for which Mgc has the lowest p-value, followed by Hhg and Hsic and then all other methods; the second dataset exhibits a close-to-linear relationship, for which global methods perform the best while Hhg and Hsic are trailing. Moreover, Mgc detected a complex nonlinear relationship for brain activity versus personality, and a nearly linear but noisy relationship for brain network versus creativity, the only method able to make either of those claims. In a separate experiment, we assessed the frequency with which Mgc obtained false positive results using brain activity data, based on experiments from Eklund et al. (2012); Eklund et al. (2016). Appendix 1—figure 1 shows that Mgc achieves a false positive rate of 5% when using a significance level of 0.05, implying that it correctly controls for false positives, unlike typical parametric methods on these data.

#### Mgc identifies potential cancer proteomics biomarkers

Mgc can also be useful for a completely complementary set of scientific questions: screening proteomics data for biomarkers, often involving the analysis of tens of thousands of proteins, peptides, or transcripts in multiple samples representing a variety of disease types. Determining whether there is a relationship between one or more of these markers and a particular disease state can be challenging but is a necessary first step (Frantzi et al., 2014). We sought to discover new useful protein biomarkers from a quantitative proteomics technique that measures protein and peptide abundance called Selected Reaction Monitoring (SRM) (Wang et al., 2011). Specifically, we were interested in finding biomarkers that were unique to pancreatic cancer, because it is lethal and no clinically useful biomarkers are currently available (Bhat et al., 2012).

The data consist of proteolytic peptides derived from the blood samples of 95 individuals harboring pancreatic ($n=10$), ovarian ($n=24$), colorectal cancer ($n=28$), and healthy controls ($n=33$). The processed data included 318 peptides derived from 121 proteins. Previously, we used these data and other techniques to find ovarian cancer biomarkers (a much easier task because the dataset has twice as many ovarian patients) and validated them with subsequent experiments (Wang et al., 2017). Therefore, our first step was to check whether Mgc could correctly identify ovarian biomarkers. Indeed, the peptides that have been validated previously are also identified by Mgc. Emboldened, using the same dataset, we applied Mgc to screen for biomarkers unique to pancreatic cancer. To do so, we first screened for a difference between pancreatic cancer and healthy controls, identifying several potential biomarkers. Then, we screened for a difference between pancreatic cancer and all other conditions, to find peptides that differentiate pancreatic cancer from other cancers. Figure 4C shows the p-value of each peptide assigned by Mgc, which reveals one particular protein, neurogranin, that exhibits a strong dependency specifically with pancreatic cancer. Subsequent literature searches reveal that neurogranin is a potentially valuable biomarker for pancreatic cancer because it is exclusively expressed in brain tissue among normal tissues and has not been linked with any other cancer type (Yang et al., 2015; Willemse et al., 2018). In comparison, Hsic identified neurogranin as well, but it also identified another peptide; Hhg identified the same two by Hsic, and a third peptide. A literature evaluation of these additional peptides shows that they are upregulated in other cancers as well and are unlikely to be useful as a pancreatic biomarker (Helfman et al., 2018; Lam et al., 2012). The rest of the global methods did not identify any markers at significance level $0.05$, see Materials and methods for more details and Appendix 1—table 2 for identified peptide information using each method.

Since there is no ground truth yet in this experiment, we further carried out a classification task using the biomarkers identified by the various algorithms, using a k-nearest-neighbor classifier to predict pancreatic cancer, and a leave-one-subject-out validation. Figure 4D shows that the peptide selected by Mgc (neurogranin) works better than any other subset of the peptides selected by Hsic or Hhg, in terms of both fewer false positives and negatives. This analysis suggests Mgc can effectively be used for screening and subsequent classification.

## Discussion

There are a number of connections between Mgc and other prominent statistical procedures that may be worth further exploration. First, Mgc can be thought of as a regularized or sparsified variant of distance or kernel methods. Regularization is central to high-dimensional and ill-posed problems, where dimensionality is larger than sample size. Second, Mgc can also be thought of as learning a metric because it chooses the optimal scale amongst a set of $n^{2}$ truncated distances, motivating studying the relationship between Mgc and recent advances in metric learning (Xing et al., 2003). In particular, deep learning can be thought of as metric learning (Giryes et al., 2015), and generative adversarial networks (Goodfellow et al., 2014) are implicitly testing for equality, which is closely related to dependence (Sutherland et al., 2016). While Mgc searches over a two-dimensional parameter space to optimize the metric, deep learning searches over a much larger parameter space, sometimes including millions of dimensions. Probably neither is optimal, and somewhere between the two would be useful in many tasks. Third, energy statistics provide state of the art approaches to other problems, including goodness-of-fit (Székely and Rizzo, 2005), analysis of variance (Rizzo and Székely, 2010), conditional dependence (Székely and Rizzo, 2014; Wang et al., 2015), and feature selection (Li et al., 2012; Zhong and Zhu, 2015), so Mgc can be adapted for them as well. Indeed, Mgc can also implement a two-sample (or generally the K-sample) test (Szekely and Rizzo, 2004; Heller et al., 2016; Shen and Vogelstein, 2018). Specifically, for more than two modalities, one may use summation of pairwise Mgc test statistics, similar to how energy statistic is generalized to K-sample testing from two-sample testing (Rizzo and Székely, 2010; Rizzo and Székely, 2016; Shen and Vogelstein, 2018), or how canonical correlation analysis is generalized into more than two modalities (Kettenring, 1971; Tenenhaus and Tenenhaus, 2011; Shen et al., 2014). Finally, although energy statistics have not yet been explicitly used for classification, regression, or dimensionality reduction, Mgc opens the door to these applications by providing guidance as to how to proceed. Specifically, it is well documented in machine learning literature that the choice of kernel, metric, or scale often has a strong effect on the performance of different machine learning algorithms (Levina and Bickel, 2004). Mgc provides a mechanism to estimate scale that is both theoretically justified and computationally efficient, by optimizing a metric for a task wherein the previous methods lacked a notion of optimization. Nonlinear dimensionality reduction procedures, such as Isomap (Tenenbaum et al., 2000) and local linear embedding (Roweis and Saul, 2000) for example, must also choose a scale, but have no principled criteria for doing so. Mgc could be used to provide insight into multimodal dimensionality reduction as well.

The default metric choice of Mgc in this paper is always the Euclidean distance, but other metric choices may be more appropriate in different fields, and using the strong negative type metric as specified in Lyons (2013) guarantees consistency. However, if multiple metric choices are experimented to yield multiple Mgc p-values, then the optimal p-value should be properly corrected for multiple testing. Alternatively, one may use the maximum Mgc statistic among multiple metric choices, apply the same procedure in each permutation (i.e. in each permutation, use the same number of metric choices and take the maximum Mgc as the permuted statistic), then derive a single p-value. Such a testing procedure properly controls the type one error level without the need for additional correction.

Mgc also addresses a particularly vexing statistical problem that arises from the fact that methods methods for discovering dependencies are typically dissociated from methods for deciphering them. This dissociation creates a problem because the statistical assumptions underlying the ‘deciphering’ methods become compromised in the process of ‘discoverying’; this is called the ‘post-selection inference’ problem (Berk et al., 2013). The most straightforward way to address this issue is to collect new data, which is costly and time-consuming. Therefore, researchers often ignore this fact and make statistically invalid claims. Mgc circumvents this dilemma by carefully constructing its permutation test to estimate the scale in the process of estimating a p-value, rather than after. To our knowledge, Mgc is the first dependence test to take a step towards valid post-selection inference.

As a separate next theoretical extension, we could reduce the computational space and time required by Mgc. Mgc currently requires space and time that are quadratic with respect to the number of samples, which can be costly for very large data. Recent advances in related work demonstrated that one could reduce computational time of distance-based tests to close to linear via faster implementation, subsampling, random projection, and null distribution approximation (Huo and Székely, 2016; Huang and Huo, 2017; Zhang et al., 2018; Chaudhuri and Hu, 2018), making it feasible for large amount of data. Alternately, semi-external memory implementations would allow running Mgc even as the interpoint comparison matrix exceeds the size of main memory (Da Zheng et al., 2015; Da Zheng et al., 2016a; Da Zheng et al., 2016b; Da Zheng et al., 2016c).

Finally, Mgc is easy to use. Source code is available in MATLAB, R, and Python from https://mgc.neurodata.io/ (Bridgeford et al., 2018; experiments archived at https://github.com/elifesciences-publications/MGC-paper). Code for reproducing all the figures in this manuscript is also available from the above websites. We showed Mgc’s value in diverse applications spanning neuroscience (which motivated this work) and an ’omics example. Applications in other domains facing similar questions of dependence, such as finance, pharmaceuticals, commerce, and security, could likewise benefit from Mgc.

## Materials and methods

### Mathematical details

This section contains essential mathematical details on independence testing, the notion of the generalized correlation coefficient and the distance-based correlation measure, how to compute the local correlations, and the smoothing technique. A statistical treatment on MGC is in Shen and Vogelstein, 2018, which introduces the population version of Mgc and various theoretical properties.

#### Testing independence

Given pairs of observations $(x_{i},y_{i})\inR^{p}\timesR^{q}$ for $i=1,…,n$, assume they are independently identically distributed as $(X,Y)∼iidF_{XY}$. If the two random variables $X$ and $Y$ are independent, the joint distribution equals the product of the marginals, that is $F_{XY}=F_{X}F_{Y}$. The statistical hypotheses for testing independence is as follows:

$$
H_{0}:F_{XY}=F_{X}F_{Y},
$$



$$
H_{A}:F_{XY}\neqF_{X}F_{Y}.
$$

Given a test statistic, the testing power equals the probability of rejecting the independence hypothesis (i.e. the null hypothesis) when it is false. A test statistic is consistent if and only if the testing power increases to $1$ as sample size increases to infinity. We would like a test to be universally consistent, that is consistent against all joint distributions. Dcorr, Mcorr, Hsic, and Hhg are all consistent against any joint distribution of finite second moments and finite dimension.

Note that $p$ is the dimension for $x$’s, $q$ is the dimension for $y$’s. For Mgc and all benchmark methods, there is no restriction on the dimensions, that is the dimensions can be arbitrarily large, and $p$ is not required to equal $q$. The ability to handle data of arbitrary dimension is crucial for modern big data. There also exist some special methods that only operate on one-dimensional data, such as (Reshef et al., 2011; Heller et al., 2016; Huo and Székely, 2016), which are not directly applicable to multidimensional data.

#### Correlation measures

To achieve consistent testing, most state-of-the-art dependence measures operate on pairwise comparisons, either similarities (such as kernels) or dissimilarities (such as distances).

Let $𝒳_{n}={x_{1},⋯,x_{n}}\inR^{p\timesn}$ and $𝒴_{n}={y_{1},⋯,y_{n}}\inR^{q\timesn}$ denote the matrices of sample observations, and $d_{x}$ be the distance function for $x$’s and $d_{y}$ for $y$’s. One can then compute two $n\timesn$ distance matrices $A~={a~_{ij}}$ and $B~={b~_{ij}}$, where $a~_{ij}=\delta_{x}(x_{i},x_{j})$ and $b~_{ij}=\delta_{y}(y_{i},y_{j})$. A common example of the distance function is the Euclidean metric ($L^{2}$ norm), which serves as the starting point for all methods in this manuscript.

Let $A$ and $B$ be the transformed (e.g., centered) versions of the distance matrices $A~$ and $B~$, respectively. Any ‘generalized correlation coefficient’ (Spearman, 1904; Kendall, 1970) can be written as:

$$
c(𝒳_{n},𝒴_{n})=\frac{1}{z}\sumi=1n\sumj=1na_{ij}b_{ij},
$$

where $z$ is proportional to the standard deviations of $A$ and $B$, that is $z=n^{2}\sigma_{a}\sigma_{b}$. In words, $c$ is the global sample correlation across pairwise comparison matrices $A$ and $B$, and is normalized into the range $[-1,1]$, which usually has expectation 0 under independence and implies a stronger dependency when the correlation is further away from 0.

Traditional correlations such as the Pearson’s correlation and the rank correlation can be written via the above correlation formulation, by using $A$ and $B$ directly from sample observations rather than distances. Distance-based methods like Dcorr and Mantel operate on the Euclidean distance by default, or other metric choices on the basis of domain knowledge; then transform the resulting distance matrices $A~$ and $B~$ by certain centering schemes into $A$ and $B$. Hsic chooses the Gaussian kernel and computes two kernel matrices, then transform the kernel matrices $A~$ and $B~$ by the same centering scheme as Dcorr. For Mgc, $A$ and $B$ are always distance matrices (or can be transformed to distances from kernels by Sejdinovic et al. (2013)), and we shall apply a slightly different centering scheme that turns out to equal Dcorr.

To carry out the hypothesis testing on sample data via a nonparametric test statistic, for example a generalized correlation, the permutation test is often an effective choice (Good, 2005), because a p-value can be computed by comparing the correlation of the sample data to the correlation of the permuted sample data. The independence hypothesis is rejected if the p-value is lower than a pre-determined type $1$ error level, say 0.05. Then the power of the test statistic equals the probability of a correct rejection at a specific type $1$ error level. Note that Hhg is the only exception that cannot be cast as a generalized correlation coefficient, but the permutation testing is similarly effective for the Hhg test statistic; also note that the iid assumption is critical for permutation test to be valid, which may not be applicable in special cases like auto-correlated time series (Guillot and Rousset, 2013).

#### Distance correlation (Dcorr) and the Unbiased Version (Mcorr)

Define the row and column means of $A~$ by $a¯_{⋅j}=\frac{1}{n}\sumi=1na~_{ij}$ and $a¯_{i⋅}=\frac{1}{n}\sumj=1na~_{ij}$. Dcorr defines

$$
a_{ij}={a~_{ij}−a¯_{i⋅}−a¯_{⋅j}+a¯, if i\neqj,0, if i=j,
$$

and similarly for $b_{ij}$. For distance correlation, the numerator of Equation 1 is named the distance covariance (Dcov), while $s_{a}$ and $s_{b}$ in the denominator are the square root of each distance variance. The centering scheme is important to guarantee the universal consistency of Dcorr, whereas Mantel uses a simple centering scheme and thus not universally consistent.

Let $c(X,Y)$ be the population distance correlation, that is, the distance correlation between the underlying random variables $X$ and $Y$. Székely et al. (2007) define the population distance correlation via the characteristic functions of $F_{X}$ and $F_{Y}$, and show that the population distance correlation equals zero if and only if $X$ and $Y$ are independent, for any joint distribution $F_{XY}$ of finite second moments and finite dimensionality. They also show that as $n→∞$, the sample distance correlation converges to the population distance correlation, that is, $c(𝒳_{n},𝒴_{n})→c(X,Y)$. Thus the sample distance correlation is consistent against any dependency of finite second moments and dimensionality. Of note, the distance covariance, distance variance, and distance correlation are always non-negative. Moreover, the consistency result holds for a much larger family of metrics, those of strong negative type (Lyons, 2013).

It turns out that the sample distance correlation has a finite-sample bias, especially as the dimension $p$ or $q$ increases (Szekely and Rizzo, 2013). For example, for independent Gaussian distributions, the sample distance correlation converges to $1$ as $p,q→∞$. By excluding the diagonal entries and slightly modifies the off-diagonal entries of $𝒜$ and $B$, Szekely and Rizzo (Szekely and Rizzo, 2013; Székely and Rizzo, 2014) show that Mcorr is an unbiased estimator of the population distance correlation $c(x,y)$ for all $p,q,n$, which is approximately normal even if $p,q→∞$. Thus it enjoys the same theoretical consistency as Dcorr and always has zero mean under independence.

#### Local correlations

Given any matrices $A$ and $B$, we can define a set of local correlations as follows. Let $R(A_{⋅j},i)$ be the ‘rank’ of $x_{i}$ relative to $x_{j}$, that is, $R(A_{⋅j},i)=k$ if $x_{i}$ is the $k^{th}$ closest point (or ‘neighbor’) to $x_{j}$, as determined by ranking the $n-1$ distances to $x_{j}$. Define $R(B_{i⋅},j)$ equivalently for the $Y$’s, but ranking relative to the rows rather than the columns (see below for explanation). For any neighborhood size $k$ around each $x_{i}$ and any neighborhood size $l$ around each $y_{j}$, we define the local pairwise comparisons:

$$
a~_{ij}^{k}={a_{ij},if R(A_{⋅j},i)\leqk,0,otherwise;b~_{ij}^{l}={b_{ij},if R(B_{i⋅},j)\leql,0,otherwise;
$$

and then let $a_{ij}^{k}=a~_{ij}^{k}−a¯^{k}$, where $a¯^{k}$ is the mean of ${a~_{ij}^{k}}$, and similarly for $b_{ij}^{l}$.

The local correlation coefficient at a given scale is defined to effectively exclude large distances:

$$
c^{kl}(𝒳_{n},𝒴_{n})=\frac{1}{z_{kl}}\sumi,j=1na_{ij}^{k}b_{ij}^{l},
$$

where $z_{kl}=n^{2}\sigma_{a}^{k}\sigma_{b}^{l}$, with $s_{a}^{k}$ and $s_{b}^{l}$ is the standard deviations for the truncated pairwise comparisons. The Mgc-Map can be constructed by computing all local correlations, which allows the discovery of the optimal correlation. For any aforementioned correlation (Dcorr, Mcorr, Hsic, Mantel, Pearson), one can define its local correlations by using Equation 3 and plugging in the respective $a_{ij}$ and $b_{ij}$ from Equation 1.

As most nonlinear relationships intrinsically exhibit a local linear structure, considering the nearest-neighbors is able to amplify the dependency signal over the global correlation. There could be two other scenarios: when the small distances in one modality mostly correspond to large distances in another modality, or when the large distances in one modality correspond to large distance in another modality. For the first scenario, the small distances become negative terms after centering while the large distances become positive terms after centering, so adding their product to $c^{kl}$ will cause the test statistic to be smaller — in fact, as distance correlation is shown to be > 0 under dependence (Székely et al., 2007), the first scenario cannot happen for all distances pairs. For the second scenario, one can experiment using the large distances (or the furthest neighbors) only by reversing the ranking scheme in local correlation to descending order. However, whenever the large distances are highly correlated, the small distances must also be highly correlated after centering by the mean distances, so global correlation coefficient like Dcorr already handles this scenario. Therefore considering the nearest-neighbor may significantly improve the performance over global correlation, while considering the other scenarios does not.

#### Mgc as the optimal local correlation

We define the multiscale graph correlation statistic as the optimal local correlation, for which the family of local correlation is computed based on Euclidean distance and Mcorr transformation.

Instead of taking a direct maximum, Mgc takes a smoothed maximum, that is the maximum local correlation of the largest connected component $R$ such that all local correlations within $R$ are significant. If no such region exists, Mgc defaults the test statistic to the global correlation (details in Algorithm C2). Thus, we can write:

$$
c^{∗}(𝒳_{n},𝒴_{n})=max(k,l)\inRc^{kl}(𝒳_{n},𝒴_{n})
$$



$$
R=Largest Connected Component of {(k,l) such thatc^{kl}>max(\tau,c^{nn})}.
$$

Then the optimal scale equals all scales within $R$ whose local correlations are as large as $c^{∗}$. The choice of $\tau$ is made explicit in the pseudo-code, with further discussion and justification offered in Shen and Vogelstein, 2018.

#### Proof for theorem 1

Theorem 1. When $(X,Y)$ are linearly related (rotation, scaling, translation, reflection), the optimal scale of Mgc equals the global scale. Conversely, that. the optimal scale is local implies a nonlinear relationship.

Proof. It suffices to prove the first statement, then the second statement follows by contrapositive. When $(X,Y)$ are linearly related, $Y=WX+b$ for a unitary matrix $W$ and a constant $b$ up-to possible scaling, in which case the distances are preserved, that is $‖y_{i}−y_{j}‖=‖Wx_{i}−Wx_{j}‖=‖x_{i}−x_{j}‖$. It follows that $Mcorr(𝒳_{n},𝒴_{n})=1$, so the global scale achieves the maximum possible correlation, and the largest connected region $R$ is empty. Thus the optimal scale is global and $Mgc(𝒳_{n},𝒴_{n})=Mcorr(𝒳_{n},𝒴_{n})=1$.

#### Computational complexity of each step

The distance computation takes $𝒪(n^{2}max{p,q})$, and the ranking process takes $𝒪(n^{2}log⁡n)$. Once the distance and ranking are completed, computing one local generalized correlation requires $𝒪(n^{2})$ (see Algorithm C4). Thus, a naive approach to compute all local generalized correlations requires at least $𝒪(n^{2}max{n^{2},p,q})$ by going through all possible scales, meaning possibly $𝒪(n^{4})$ which would be computationally prohibitive. However, given the distance and ranking information, we devised an algorithm that iteratively computes all local correlations in $𝒪(n^{2})$ by re-using adjacent smaller local generalized correlations (see Algorithm C5). Therefore, when including the distance computation and ranking overheads, the MGC statistic is computed in $𝒪(n^{2}max{log⁡n,p,q})$), which has the same running time as the Hhg statistic, and the same running time up to a factor of $log⁡n$ as global correlations like Dcorr and Mcorr, which require $𝒪(n^{2}max{p,q})$ time. By utilizing a multi-core architecture, Mgc can be computed in $𝒪(n^{2}max{log⁡n,p,q}/T)$ instead. As $T=log⁡(n)$ is often a small number, for example $T$ is no more than $30$ at $1$ billion samples, thus Mgc can be effectively computed in the same complexity as Dcorr. Note that the permutation test adds another $r$ random permutations to the $n^{2}$ term, so computing the p-value requires $𝒪(n^{2}max{log⁡n,p,q,r}/T)$.

### Mgc algorithms and testing procedures

Six algorithms are presented in order:

For ease of presentation, we assume there are no repeating observations of $X$ or $Y$, and note that Mcorr is the global correlation choice that Mgc builds on.

<table>
  <tbody>
    <tr>
      <td colspan="3">Pseudocode C1 Multiscale Graph Correlation (Mgc); requires 𝒪(n2max(log⁡n,p,q,r)/T) time, where r is the number of permutations and T is the number of cores available for parallelization.</td>
    </tr>
    <tr>
      <td colspan="3">Input: n samples of (xi,yi) pairs, an integer r for the number of random permutations.</td>
    </tr>
    <tr>
      <td colspan="3">Output: (i) MGC statistic c*, (ii) the optimal scale (k,l), (iii) the p-value p(c∗),</td>
    </tr>
    <tr>
      <td colspan="2">function MG((xi,yi), for i∈[n])</td>
      <td></td>
    </tr>
    <tr>
      <td colspan="2">(1) Calculate all pairwise distances:</td>
      <td></td>
    </tr>
    <tr>
      <td colspan="2">for i,j:=1,…,n do</td>
      <td></td>
    </tr>
    <tr>
      <td colspan="2">aij=δx(xi,xj)</td>
      <td>dx is the distance between pairs of x samples</td>
    </tr>
    <tr>
      <td colspan="2">bij=δy(yi,yj)</td>
      <td>dy is the distance between pairs of y samples</td>
    </tr>
    <tr>
      <td colspan="2">end for</td>
      <td></td>
    </tr>
    <tr>
      <td colspan="2">Let A={aij} and B={bij}.</td>
      <td></td>
    </tr>
    <tr>
      <td colspan="2">(2) Calculate Multiscale Correlation Map 𝒞 &amp; Mgc Test Statistic:</td>
      <td></td>
    </tr>
    <tr>
      <td colspan="2">[c∗,𝒞,k,l]=MGCSAMPLESTAT(A,B)</td>
      <td>Algorithm C2</td>
    </tr>
    <tr>
      <td colspan="2">(3) Calculate the p-value</td>
      <td></td>
    </tr>
    <tr>
      <td colspan="2">pval(c∗)=PERMUTATIONTEST(A,B,r,c∗)</td>
      <td>Algorithm C3</td>
    </tr>
    <tr>
      <td colspan="2">end Function</td>
      <td></td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td colspan="3">Pseudocode C2 Mgc test statistic. This algorithm computes all local correlations, take the smoothed maximum, and reports the (k,l) pair that achieves it. For the smoothing step, it: (i) finds the largest connected region in the correlation map, such that each correlation is significant, that is larger than a certain threshold to avoid correlation inflation by sample noise, (ii) take the largest correlation in the region, (iii) if the region area is too small, or the smoothed maximum is no larger than the global correlation, the global correlation is used instead. The running time is 𝒪(n2).</td>
    </tr>
    <tr>
      <td colspan="3">Input: A pair of distance matrices (A,B)∈Rn×n×Rn×n.</td>
    </tr>
    <tr>
      <td colspan="3">Output: The Mgc statistic c∗∈R, all local statistics 𝒞∈Rn×n, and the corresponding local scale (k,l)∈N×N.</td>
    </tr>
    <tr>
      <td>1:</td>
      <td>function MGCSampleStat(A,B)</td>
      <td></td>
    </tr>
    <tr>
      <td>2:</td>
      <td>𝒞=MGCALLLOCAL(A,B)</td>
      <td>All local correlations</td>
    </tr>
    <tr>
      <td>3:</td>
      <td>τ=THRESHOLDING(𝒞)</td>
      <td>find a threshold to determine large local correlations</td>
    </tr>
    <tr>
      <td>4:</td>
      <td>for i,j:=1,…,ndo rij←I(cij&gt;τ)end for</td>
      <td>identify all scales with large correlation</td>
    </tr>
    <tr>
      <td>5:</td>
      <td>ℛ←{rij:i,j=1,…,n}</td>
      <td>binary map encoding scales with large correlation</td>
    </tr>
    <tr>
      <td>6:</td>
      <td>ℛ=CONNECTED(ℛ)</td>
      <td>largest connected component of the binary matrix</td>
    </tr>
    <tr>
      <td>7:</td>
      <td>c∗←𝒞(n,n)</td>
      <td>use the global correlation by default</td>
    </tr>
    <tr>
      <td>8:</td>
      <td>k←n,l←n</td>
      <td></td>
    </tr>
    <tr>
      <td>9:</td>
      <td>if (∑i,jrij)≥2n then</td>
      <td>proceed when the significant region is sufficiently large</td>
    </tr>
    <tr>
      <td>10:</td>
      <td>[c∗,k,l]←max(𝒞∘ℛ)</td>
      <td>find the smoothed maximum and the respective scale</td>
    </tr>
    <tr>
      <td>11:</td>
      <td>end if</td>
      <td></td>
    </tr>
    <tr>
      <td>12:</td>
      <td>end Function</td>
      <td></td>
    </tr>
    <tr>
      <td colspan="3">Input: 𝒞∈Rn×n.</td>
    </tr>
    <tr>
      <td colspan="3">Output: A threshold t to identify large correlations.</td>
    </tr>
    <tr>
      <td>13:</td>
      <td>function Thresholding 𝒞</td>
      <td></td>
    </tr>
    <tr>
      <td>14:</td>
      <td>τ←∑cij&lt;0(cij)2/∑cij&lt;01</td>
      <td>variance of all negative local generalized correlations</td>
    </tr>
    <tr>
      <td>15:</td>
      <td>τ←max{0.01,τ}×3.5</td>
      <td>threshold based on negative correlations</td>
    </tr>
    <tr>
      <td>16:</td>
      <td>τ←max{τ,2/n,cnn}</td>
      <td></td>
    </tr>
    <tr>
      <td>17:</td>
      <td>end Function</td>
      <td></td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td colspan="3">Pseudocode C3 Permutation Test. This algorithm uses the random permutation test with r random permutations for the p-value, requiring 𝒪(rn2log⁡n) for Mgc. In the real-data experiment, we always set r=10,000. Note that the p-value computation for any other global generalized correlation coefficient follows from the same algorithm by replacing Mgc with the respective test statistic.</td>
    </tr>
    <tr>
      <td colspan="3">Input: A pair of distance matrices (A,B)∈Rn×n×Rn×n, the number of permutations r, and Mgc statistic c* for the observed data.</td>
    </tr>
    <tr>
      <td colspan="3">Output: The p-value pval∈[0,1].</td>
    </tr>
    <tr>
      <td>1:</td>
      <td>function PermutationTest(A, B, r, c*)</td>
      <td></td>
    </tr>
    <tr>
      <td>2:</td>
      <td>for t:=1,…,r do</td>
      <td></td>
    </tr>
    <tr>
      <td>3:</td>
      <td>π=RANDPERM(n)</td>
      <td>generate a random permutation of size n</td>
    </tr>
    <tr>
      <td>4:</td>
      <td>c0∗[t]=MGCSAMPLESTAT(A,B(π,π))</td>
      <td>calculate the permuted Mgc statistic</td>
    </tr>
    <tr>
      <td>5:</td>
      <td>end for</td>
      <td></td>
    </tr>
    <tr>
      <td>6:</td>
      <td>pval(c∗)←1t∑t=1rI(c∗≤c0∗[t])</td>
      <td>compute p-value of Mgc</td>
    </tr>
    <tr>
      <td>7:</td>
      <td>end function</td>
      <td></td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td colspan="3">Pseudocode C4 Compute local test statistic at a given scale. This algorithm runs in 𝒪(n2) once the rank information is provided, which is suitable for Mgc computation if an optimal scale is already estimated. But it would take 𝒪(n4) if used to compute all local generalized correlations. Note that for the default Mgc implementation uses single centering, the centering function centers A by column and B by row, and the sorting function sorts A within column and B within row. By utilizing T=log⁡(n) cores, the sorting function can be easily parallelized to take 𝒪(n2log⁡(n)/T)=𝒪(n2).</td>
    </tr>
    <tr>
      <td colspan="3">Input: A pair of distance matrices (A,B)∈Rn×n×Rn×n, and a local scale (k,l)∈N×N.</td>
    </tr>
    <tr>
      <td colspan="3">Output: The local generalized correlation coefficient ckl∈[−1,1].</td>
    </tr>
    <tr>
      <td>1:</td>
      <td>function LocalGenCorr(A, B, k, l)</td>
      <td></td>
    </tr>
    <tr>
      <td>2:</td>
      <td>for Z:=A,B do ℰZ=SORT(Z) end for</td>
      <td>parallelized sorting</td>
    </tr>
    <tr>
      <td>3:</td>
      <td>for Z:=A,B do Z=CENTER(Z) end for</td>
      <td>center distance matrices</td>
    </tr>
    <tr>
      <td>4:</td>
      <td>c~kl←tr((A∘ℰA)T×(B∘(ℰB)T))</td>
      <td>un-normalized local distance covariance</td>
    </tr>
    <tr>
      <td>5:</td>
      <td>vA←tr((A∘ℰA)T×(A∘(ℰA)T))</td>
      <td>local distance variances</td>
    </tr>
    <tr>
      <td>6:</td>
      <td>vB←tr((B∘ℰB)T×(B∘(ℰB)T))</td>
      <td></td>
    </tr>
    <tr>
      <td>7:</td>
      <td>eA←∑i,j=1n(A∘ℰA)ij</td>
      <td>sample means</td>
    </tr>
    <tr>
      <td>8:</td>
      <td>eB←∑i,j=1n(B∘ℰB)ij</td>
      <td></td>
    </tr>
    <tr>
      <td>9:</td>
      <td>ckl←(c~kl−eAeB/n2)/(vA−(eA/n)2)(vB−(eB/n)2)</td>
      <td>center and normalize</td>
    </tr>
    <tr>
      <td>10:</td>
      <td>end function</td>
      <td></td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td colspan="3">Pseudocode C5 Compute the multiscale correlation map (i.e., all local generalized correlations) in 𝒪(n2log⁡n/T). Once the distances are sorted, the remaining algorithm runs in 𝒪(n2). An important observation is that each product aijbij is included in ckl if and only if (k,l) satisfies k≤R(A⋅j,i) and l≤R(B⋅j,i), so it suffices to iterate through aijbij for i,j:=1,…,n, and add the product simultaneously to all ckl whose scales are no more than (R(A⋅j,i),R(B⋅j,i)). To achieve the above, we iterate through each product, add it to ckl at (kl)=(R(A⋅j,i),R(B⋅j,i)) only (so only one local scale is accessed for each operation); then add up adjacent ckl for k,l=1,…,n. The same applies to all local covariances, variances, and expectations.</td>
    </tr>
    <tr>
      <td colspan="3">Input: A pair of distance matrices (A,B)∈Rn×n×Rn×n.</td>
    </tr>
    <tr>
      <td colspan="3">Output: The multiscale correlation map 𝒞∈[−1,1]n×nfor k,l=1,…,n.</td>
    </tr>
    <tr>
      <td>1:</td>
      <td>function MGCAllLocal(A, B)</td>
      <td></td>
    </tr>
    <tr>
      <td>2:</td>
      <td>for Z:=A,B do ℰZ=SORT(Z) end for</td>
      <td></td>
    </tr>
    <tr>
      <td>3:</td>
      <td>for Z:=A,B do Z=CENTER(Z)end for</td>
      <td></td>
    </tr>
    <tr>
      <td>4:</td>
      <td>for i,j:=1,…,n do</td>
      <td>iterate through all local scales to calculate each term</td>
    </tr>
    <tr>
      <td>5:</td>
      <td>k←ℰijZ</td>
      <td></td>
    </tr>
    <tr>
      <td>6:</td>
      <td>l←ℰijZ</td>
      <td></td>
    </tr>
    <tr>
      <td>7:</td>
      <td>c~kl←c~kl+aijbij</td>
      <td></td>
    </tr>
    <tr>
      <td>8:</td>
      <td>vkA←vkA+aij2</td>
      <td></td>
    </tr>
    <tr>
      <td>9:</td>
      <td>vlB←vlB+bij2</td>
      <td></td>
    </tr>
    <tr>
      <td>10:</td>
      <td>ekA←ekA+aij</td>
      <td></td>
    </tr>
    <tr>
      <td>11:</td>
      <td>elB←elB+bij</td>
      <td></td>
    </tr>
    <tr>
      <td>12:</td>
      <td>end for</td>
      <td></td>
    </tr>
    <tr>
      <td>13:</td>
      <td>for k:=1,…,n-1 do</td>
      <td>iterate through each scale again and add up adjacent terms</td>
    </tr>
    <tr>
      <td>14:</td>
      <td>c~1,k+1←c~1,k+c~1,k+1</td>
      <td></td>
    </tr>
    <tr>
      <td>15:</td>
      <td>c~k+1,1←c~k+1,1+c~k+1,1</td>
      <td></td>
    </tr>
    <tr>
      <td>16:</td>
      <td>for Z:=A,B do vk+1Z←vkZ+vk+1Z end for</td>
      <td></td>
    </tr>
    <tr>
      <td>17:</td>
      <td>for Z:=A,B do ek+1Z←ekZ+ek+1Z end for</td>
      <td></td>
    </tr>
    <tr>
      <td>18:</td>
      <td>end for</td>
      <td></td>
    </tr>
    <tr>
      <td>19:</td>
      <td>for k,l:=1,…,n-1 do</td>
      <td></td>
    </tr>
    <tr>
      <td>20:</td>
      <td>c~k+1,l+1←c~k+1,l+c~k,l+1+c~k+1,l+1−c~k,l</td>
      <td></td>
    </tr>
    <tr>
      <td>21:</td>
      <td>end for</td>
      <td></td>
    </tr>
    <tr>
      <td>22:</td>
      <td>for k,l:=1,…,n do</td>
      <td></td>
    </tr>
    <tr>
      <td>23:</td>
      <td>ckl←(c~kl−ekAelB/n2)/(vkA−ekA2/n2)(vlB−elB2/n2)</td>
      <td></td>
    </tr>
    <tr>
      <td>24:</td>
      <td>end for</td>
      <td></td>
    </tr>
    <tr>
      <td>25:</td>
      <td>end function</td>
      <td></td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td colspan="3">Pseudocode C6 Power computation of Mgc against a given distribution. By repeatedly sampling from the joint distribution FXY, sample data of size n under the null and the alternative are generated for r Monte-Carlo replicates. The power of Mgc follows by computing the test statistic under the null and the alternative using Algorithm C2. In the simulations we use r=10,000 MC replicates. Note that power computation for other benchmarks follows from the same algorithm by plugging in the respective test statistic.</td>
    </tr>
    <tr>
      <td colspan="3">Input: A joint distribution FXY, the sample size n, the number of MC replicates r, and the type 1 error level a.</td>
    </tr>
    <tr>
      <td colspan="3">Output: The power ß of Mgc.</td>
    </tr>
    <tr>
      <td>1:</td>
      <td>function MGCPower(FXY, n, r, a)</td>
      <td></td>
    </tr>
    <tr>
      <td>2:</td>
      <td>for t:=1,…,r do</td>
      <td></td>
    </tr>
    <tr>
      <td>3:</td>
      <td>for i:=[n] do</td>
      <td></td>
    </tr>
    <tr>
      <td>4:</td>
      <td>xi0∼iidFX,yi0∼iidFY</td>
      <td>sample from null</td>
    </tr>
    <tr>
      <td>5:</td>
      <td>(xi1,yi1)∼iidFXY,</td>
      <td>sample from alternative</td>
    </tr>
    <tr>
      <td>6:</td>
      <td>end for</td>
      <td></td>
    </tr>
    <tr>
      <td>7:</td>
      <td>for i,j:=1,…,n do</td>
      <td></td>
    </tr>
    <tr>
      <td>8:</td>
      <td>aij0=δx(xi0,xj0), bij0=δy(yi0,yj0)</td>
      <td>pairwise distances under the null</td>
    </tr>
    <tr>
      <td>9:</td>
      <td>aij1=δx(xi1,xj1), bij1=δy(yi1,yj1)</td>
      <td>pairwise distances under the alternative</td>
    </tr>
    <tr>
      <td>10:</td>
      <td>end for</td>
      <td></td>
    </tr>
    <tr>
      <td>11:</td>
      <td>c0∗[t]=MGCSAMPLESTAT(A0,B0)</td>
      <td>Mgc statistic under the null</td>
    </tr>
    <tr>
      <td>12:</td>
      <td>c1∗[t]=MGCSAMPLESTAT(A1,B1)</td>
      <td>Mgc statistic under the alternative</td>
    </tr>
    <tr>
      <td>13:</td>
      <td>end for</td>
      <td></td>
    </tr>
    <tr>
      <td>14:</td>
      <td>ωα←CDF1−α(c0∗[t],t∈[r])</td>
      <td>the critical value of Mgc under the null</td>
    </tr>
    <tr>
      <td>15:</td>
      <td>β←∑t=1r(c1∗[t]&gt;ωα)/r</td>
      <td>compute power by the alternative distribution</td>
    </tr>
    <tr>
      <td>16:</td>
      <td>end function</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Simulation dependence functions

This section provides the 20 different dependency functions used in the simulations. We used essentially the exact same relationships as previous publications to ensure a fair comparison (Székely et al., 2007; Simon and Tibshirani, 2012; Gorfine et al., 2012). We only made changes to add white noise and a weight vector for higher dimensions, thereby making them more difficult, to better compare all methods throughout different dimensions and sample sizes. A few additional relationships are also included.

For each sample $x\inR^{p}$, we denote $x_{[d]},d=1,…,p$ as the $d^{th}$ dimension of the vector $x$. For the purpose of high-dimensional simulations, $w\inR^{p}$ is a decaying vector with $w_{[d]}=1/d$ for each $d$, such that $w^{T}x$ is a weighted summation of all dimensions of $x$. Furthermore, $𝒰(a,b)$ denotes the uniform distribution on the interval $(a,b)$, $ℬ(p)$ denotes the Bernoulli distribution with probability $p$, $𝒩(\mu,Σ)$ denotes the normal distribution with mean $µ$ and covariance $S$, $U$ and $V$ represent some auxiliary random variables, $κ$ is a scalar constant to control the noise level (which equals $1$ for one-dimensional simulations and 0 otherwise), and $ϵ$ is a white noise from independent standard normal distribution unless mentioned otherwise.

For all the below equations, $(X,Y)∼iidF_{XY}=F_{Y|X}F_{X}$. For each relationship, we provide the space of $(X,Y)$, and define $F_{Y|X}$ and $F_{X}$, as well as any additional auxiliary distributions.

1. Linear $(X,Y)\inR^{p}\timesR$,

$$
X∼𝒰(−1,1)^{p},Y=w^{T}X+κϵ.
$$

2. Exponential $(X,Y)\inR^{p}\timesR$:

$$
X∼𝒰(0,3)^{p},Y=exp(w^{T}X)+10κϵ.
$$

3. Cubic $(X,Y)\inR^{p}\timesR$:

$$
X∼𝒰(−1,1)^{p},Y=128(w^{T}X−\frac{1}{3})^{3}+48(w^{T}X−\frac{1}{3})^{2}−12(w^{T}X−\frac{1}{3})+80κϵ.
$$

4. Joint normal $(X,Y)\inR^{p}\timesR^{p}$: Let $ρ=1/2p$, $I_{p}$ be the identity matrix of size $p\timesp$, $J_{p}$ be the matrix of ones of size $p\timesp$, and $Σ=[I_{p}ρJ_{p}ρJ_{p}(1+0.5κ)I_{p}]$. Then

$$
(X,Y)∼𝒩(0,Σ).
$$

5. Step Function $(X,Y)\inR^{p}\timesR$

$$
X∼𝒰(−1,1)^{p},Y=I(w^{T}X>0)+ϵ,
$$

where $I$ is the indicator function, that is $I(z)$ is unity whenever $z$ true, and zero otherwise.

6. Quadratic $(X,Y)\inR^{p}\timesR$:

$$
X∼𝒰(−1,1)^{p},Y=(w^{T}X)^{2}+0.5κϵ.
$$

7. W Shape $(X,Y)\inR^{p}\timesR:U∼𝒰(−1,1)^{p}$,

$$
X∼𝒰(−1,1)^{p},Y=4[((w^{T}X)^{2}−\frac{1}{2})^{2}+w^{T}U/500]+0.5κϵ.
$$

8. Spiral $(X,Y)\inR^{p}\timesR:U∼𝒰(0,5)$, $ϵ∼𝒩(0,1)$

$$
X_{[d]}=Usin⁡(\piU)cos^{d}⁡(\piU)ford=1,…,p−1,X_{[d]}=Ucos^{p}⁡(\piU),Y=Usin⁡(\piU)+0.4pϵ.
$$

9. Uncorrelated Bernoulli $(X,Y)\inR^{p}\timesR:U∼ℬ(0.5)ϵ_{1}∼𝒩(0,I_{p}),ϵ_{2}∼𝒩(0,1),$

$$
X∼ℬ(0.5)^{p}+0.5ϵ_{1},Y=(2U−1)w^{T}X+0.5ϵ_{2}.
$$

10. Logarithmic $(X,Y)\inR^{p}\timesR^{p}:ϵ∼𝒩(0,I_{p})$

$$
X∼𝒩(0,I_{p}),Y_{[d]}=2log_{2}⁡(|X_{[d]}|)+3κϵ_{[d]}ford=1,…,p.
$$

11. Fourth Root $(X,Y)\inR^{p}\timesR^{p}:$

$$
X∼𝒰(−1,1)^{p},Y=|w^{T}X|^{\frac{1}{4}}+\frac{κ}{4}ϵ.
$$

12. Sine Period $4\pi(X,Y)\inR^{p}\timesR^{p}:U∼𝒰(−1,1),V∼𝒩(0,1)^{p},\theta=4\pi$,

$$
X_{[d]}=U+0.02pV_{[d]}ford=1,…,p,Y=sin⁡(\thetaX)+κϵ.
$$

13. Sine Period $16\pi(X,Y)\inR^{p}\timesR^{p}$: Same as above except $\theta=16\pi$ and the noise on $Y$ is changed to $0.5κϵ$.

14. Square $(X,Y)\inR^{p}\timesR^{p}$: Let $U∼𝒰(−1,1),V∼𝒰(−1,1),ϵ∼𝒩(0,1)^{p},\theta=−\frac{\pi}{8}$. Then

$$
X_{[d]}=Ucos⁡\theta+Vsin⁡\theta+0.05pϵ_{[d]},Y_{[d]}=−Usin⁡\theta+Vcos⁡\theta,
$$

for $d=1,…,p.$

15. Two Parabolas $(X,Y)\inR^{p}\timesR$: $ϵ∼𝒰(0,1),U∼ℬ(0.5)$,

$$
X∼𝒰(−1,1)^{p},Y=((w^{T}X)^{2}+2κϵ)⋅(U−\frac{1}{2}).
$$

16. Circle $(X,Y)\inR^{p}\timesR:U∼𝒰(−1,1)^{p},ϵ∼𝒩(0,I_{p}),r=1,$

$$
X_{[d]}=r(sin⁡(\piU_{[d+1]})\prodj=1dcos⁡(\piU_{[j]})+0.4ϵ_{[d]})ford=1,…,p−1,X_{[p]}=r(\prodj=1pcos⁡(\piU_{[j]})+0.4ϵ_{[p]}),Y=sin⁡(\piU_{[1]}).
$$

17. Ellipse $(X,Y)\inR^{p}\timesR$: Same as above except $r=5$.

18. Diamond $(X,Y)\inR^{p}\timesR^{p}$: Same as 'Square' except $\theta=−\frac{\pi}{4}$.

19. Multiplicative Noise $(x,y)\inR^{p}\timesR^{p}:u∼𝒩(0,I_{p}),$

$$
x∼𝒩(0,I_{p}),y_{[d]}=u_{[d]}x_{[d]}ford=1,…,p.
$$

20. Multimodal Independence $(X,Y)\inR^{p}\timesR^{p}:LetU∼𝒩(0,I_{p}),V∼𝒩(0,I_{p}),$$U^{′}∼ℬ(0.5)^{p},V^{′}∼ℬ(0.5)^{p}$. Then

$$
X=U/3+2U^{′}−1,Y=V/3+2V^{′}−1.
$$

For each distribution, $X$ and $Y$ are dependent except (20); for some relationships (8,14,16-18) they are independent upon conditioning on the respective auxiliary variables, while for others they are 'directly' dependent. A visualization of each dependency with $D=D_{y}=1$ is shown in Figure 2—figure supplement 1.

For the increasing dimension simulation in the main paper, we always set $κ=0$ and $n=100$, with $p$ increasing. Note that $q=p$ for types 4, 10, 12, 13, 14, 18, 19, 20,, otherwise $q=1$. The decaying vector $w$ is utilized for $p>1$ to make the high-dimensional relationships more difficult (otherwise, additional dimensions only add more signal). For the one-dimensional simulations, we always set $p=q=1$, $κ=1$ and $n=100$.
