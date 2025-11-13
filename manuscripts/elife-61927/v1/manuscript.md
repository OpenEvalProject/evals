# Fast and flexible estimation of effective migration surfaces

## Authors

- Joseph Marcus<sup>1</sup> ([ORCID: 0000-0002-0923-9881](https://orcid.org/0000-0002-0923-9881)) †
- Wooseok Ha<sup>2</sup> ([ORCID: 0000-0002-9069-854X](https://orcid.org/0000-0002-9069-854X)) †
- Rina Foygel Barber<sup>3</sup> †
- John Novembre<sup>1</sup> ([ORCID: 0000-0001-5345-0214](https://orcid.org/0000-0001-5345-0214)) †

### Affiliations

1. Department of Human Genetics, University of Chicago Chicago United States
2. Department of Statistics, University of California, Berkeley Berkeley United States
3. Department of Statistics, University of Chicago Chicago United States
4. Department of Ecology and Evolution, University of Chicago Chicago United States

† Corresponding author

## Abstract

Spatial population genetic data often exhibits ‘isolation-by-distance,’ where genetic similarity tends to decrease as individuals become more geographically distant. The rate at which genetic similarity decays with distance is often spatially heterogeneous due to variable population processes like genetic drift, gene flow, and natural selection. Petkova et al., 2016 developed a statistical method called Estimating Effective Migration Surfaces (EEMS) for visualizing spatially heterogeneous isolation-by-distance on a geographic map. While EEMS is a powerful tool for depicting spatial population structure, it can suffer from slow runtimes. Here, we develop a related method called Fast Estimation of Effective Migration Surfaces (FEEMS). FEEMS uses a Gaussian Markov Random Field model in a penalized likelihood framework that allows for efficient optimization and output of effective migration surfaces. Further, the efficient optimization facilitates the inference of migration parameters per edge in the graph, rather than per node (as in EEMS). With simulations, we show conditions under which FEEMS can accurately recover effective migration surfaces with complex gene-flow histories, including those with anisotropy. We apply FEEMS to population genetic data from North American gray wolves and show it performs favorably in comparison to EEMS, with solutions obtained orders of magnitude faster. Overall, FEEMS expands the ability of users to quickly visualize and interpret spatial structure in their data.

## Introduction

The relationship between geography and genetics has had enduring importance in evolutionary biology (see Felsenstein, 1982). One fundamental consideration is that individuals who live near one another tend to be more genetically similar than those who live far apart (Wright, 1943; Wright, 1946; Malécot, 1948; Kimura, 1953; Kimura and Weiss, 1964). This phenomenon is often referred to as ‘isolation-by-distance’ (IBD) and has been shown to be a pervasive feature in spatial population genetic data across many species (Slatkin, 1985; Dobzhansky and Wright, 1943; Meirmans, 2012). Statistical methods that use both measures of genetic variation and geographic coordinates to understand patterns of IBD have been widely applied (Bradburd and Ralph, 2019; Battey et al., 2020). One major challenge in these approaches is that the relationship between geography and genetics can be complex. Particularly, geographic features can influence migration in localized regions leading to spatially heterogeneous patterns of IBD (Bradburd and Ralph, 2019).

Multiple approaches have been introduced to model spatially non-homogeneous IBD in population genetic data (McRae, 2006; Duforet‐Frebourg and Blum, 2014; Hanks and Hooten, 2013; Petkova et al., 2016; Bradburd et al., 2018; Al-Asadi et al., 2019; Safner et al., 2011; Ringbauer et al., 2018). Particularly relevant to our proposed approach is the work of Petkova et al., 2016 and Hanks and Hooten, 2013. Both approaches model genetic distance using the ‘resistance distance’ on a weighted graph. This distance metric is inspired by concepts of effective resistance in circuit theory models, or alternatively understood as the commute time of a random walk on a weighted graph or as a Gaussian graphical model (specifically a conditional auto-regressive process) (Chandra et al., 1996; Hanks and Hooten, 2013; Rue and Held, 2005). Additionally, the resistance distance approach is a computationally convenient and accurate approximation to spatial coalescent models (McRae, 2006), although it has limitations in asymmetric migration settings (Lundgren and Ralph, 2019).

Hanks and Hooten, 2013 introduced a Bayesian model that uses measured ecological covariates, such as elevation, to predict genetic distances across sub-populations. Specifically, they use a graph-based model for genotypes observed at different spatial locations. Expected genetic distances across sub-populations in their model are given by resistance distances computed from the edge weights. They parameterize the edge weights of the graph to be a function of known biogeographic covariates, linking local geographic features to genetic variation across the landscape.

Concurrently, the Estimating Effective Migration Surfaces (EEMS) method was developed to help interpret and visualize non-homogeneous gene-flow on a geographic map (Petkova, 2013; Petkova et al., 2016). EEMS uses resistance distances to approximate the between-sub-population component of pairwise coalescent times in a ‘stepping-stone’ model of migration and genetic drift (Kimura, 1953; Kimura and Weiss, 1964). EEMS models the within-sub-population component of pairwise coalescent times, with a node-specific parameter. Instead of using known biogeographic covariates to connect geographic features to genetic variation as in Hanks and Hooten, 2013, EEMS infers a set of edge weights (and diversity parameters) that explain the genetic distance data. The inference is based on a hierarchical Bayesian model and a Voronoi-tessellation-based prior to encourage piece-wise constant spatial smoothness in the fitted edge weights.

EEMS uses Markov Chain Monte Carlo (MCMC) and outputs a visualization of the posterior mean for effective migration and a measure of genetic diversity for every spatial position of the focal habitat. Regions with relatively low effective migration can be interpreted to have reduced gene-flow over time, whereas regions with relatively high migration can be interpreted as having elevated gene-flow. EEMS has been applied to multiple systems to describe spatial genetic structure, but despite EEMS’s advances in formulating a tractable solution to investigate spatial heterogeneity in IBD, the MCMC algorithm it uses can be slow to converge, in some cases leading to days of computation time for large datasets (Peter et al., 2020).

The inference problems faced by EEMS and Hanks and Hooten are related to a growing area referred to as ‘graph learning’ (Dong et al., 2019; Mateos et al., 2019). In graph learning, a noisy signal is measured as a scalar value at a set of nodes from the graph, and the aim is then to infer non-negative edge weights that reflect how spatially ‘smooth’ the signal is with respect to the graph topology (Kalofolias, 2016). In population genetic settings, this scalar could be an allele frequency measured at locations in a discrete spatial habitat with effective migration rates between sub-populations. Like the approach taken by Hanks and Hooten, 2013, one widely used representation of smooth graph signals is to associate the smoothness property with a Gaussian graphical model where the precision matrix has the form of a graph Laplacian (Dong et al., 2016; Egilmez et al., 2016). The probabilistic model defined on the graph signal then naturally gives rise to a likelihood for the observed samples, and thus much of the literature in this area focuses on developing specialized algorithms to efficiently solve optimization problems that allow reconstruction of the underlying latent graph. For more information about graph learning and signal processing in general see the survey papers of Dong et al., 2019 and Mateos et al., 2019.

To position the present work in comparison to the ‘graph learning’ literature, our contributions are twofold. First, in population genetics, it is impossible to collect individual genotypes across all the geographic locations and, as a result, we often work with many, often the majority, of nodes having missing data. As far as we are aware, none of the work in graph signal processing considers this scenario and thus their algorithms are not directly applicable to our setting. In addition, if the number of the observed nodes is much smaller than the number of nodes of a graph, one can project the large matrices associated with the graph to the space of observed nodes, therefore allowing for fast and efficient computation. Second, highly missing nodes in the observed signals can result in significant degradation of the quality of the reconstructed graph unless it is regularized properly. Motivated by the Voronoi-tessellation-based prior adopted in EEMS (Petkova et al., 2016), we propose regularization that encourages spatial smoothness in the edge weights.

Building on advances in graph learning, we introduce a method, Fast Estimation of Effective Migration Surfaces (FEEMS), that uses optimization to obtain penalized-likelihood-based estimates of effective migration parameters. In contrast to EEMS which uses a node-specific parameterization of effective migration, we optimize over edge-specific parameters allowing for more flexible migration processes to be fit, such as spatial anisotropy, in which the migration process is not invariant to rotation of the coordinate system (e.g. migration is more extensive along a particular axis). Although we developed this model as a Gaussian Markov Random Field, the resulting likelihood has key similarities to the EEMS model, in that it is a Wishart-distribution that is a function of a genetic distance matrix. Expected genetic distances in both models can be interpreted as ‘resistance distances’ (McRae, 2006).

To fit the model, rather than using MCMC, we develop a fast quasi-Newton optimization algorithm (Nocedal and Wright, 2006) and a cross-validation approach for choosing the penalty parameter used in the penalized likelihood. We demonstrate the method using coalescent simulations and an application to a dataset of gray wolves from North America. The output is comparable to the results of EEMS but is provided in orders of magnitude less time. With this improvement in speed, FEEMS opens up the ability to perform fast exploratory data analysis of spatial population structure.

## Results

### Overview of FEEMS

Figure 1 shows a visual schematic of the FEEMS method. The input data are genotypes and spatial locations (e.g. latitudes and longitudes) for a set of individuals sampled across a geographic region. We construct a dense spatial grid embedded in geographic space where nodes represent sub-populations, and we assign individuals to nodes based on spatial proximity (see Appendix 1—figure 1 for a visualization of the grid construction and node assignment procedure). The density of the grid is user defined and must be explored to appropriately balance model mis-specification and computational burden. As the density of the lattice increases, the model is similar to discrete approximations used for continuous spatial processes, but the increased density comes at the cost of computational complexity.

![Figure 1.](https://cdn.elifesciences.org/articles/61927/elife-61927-fig1-v1.jpg)

**Figure 1.:** (A) Map of sample coordinates (black points) from a dataset of gray wolves from North America (Schweizer et al., 2016). The input to FEEMS are latitude and longitude coordinates as well as genotype data for each sample. (B) The spatial graph edge weights after random initialization uniformly over the graph to begin the optimization algorithm. (C) The edge weights after 10 iterations of running FEEMS, when the algorithm has not converged yet. (D) The final output of FEEMS after the algorithm has fully converged. The output is annotated with important features of the visualization.

Details on the FEEMS model are described in the Materials and methods section, however at a high level, we assume exchangeability of individuals within each sub-population and estimate allele frequencies, $f^_{j}⁢(k)$, for each sub-population, indexed by $k$, and single nucleotide polymorphism (SNP), indexed by $j$, under a simple Binomial sampling model. We also use the recorded sample sizes at each node to model the precision of the estimated allele frequency. With the estimated allele frequencies in hand, we model the data at each SNP using an approximate Gaussian model whose covariance is, up to constant factors, shared across all SNPs—in other words, after rescaling by SNP-specific variation factors, we assume that the set of observed frequencies at each SNP is an independent realization of the same spatial process. The latent frequency variables, $f_{j}⁢(k)$, are modeled as a Gaussian Markov Random Field (GMRF) with a sparse precision matrix determined by the graph Laplacian and a set of residual variances that vary across SNPs. The pseudo-inverse of the graph Laplacian in a GMRF is inherently connected to the notion of resistance distance in an electrical circuit (Hanks and Hooten, 2013) that is often used in population genetics to model the genetic differentiation between sub-populations (McRae, 2006). The graph’s weighted edges, denoted by $w_{i⁢j}$ between nodes $i$ and $j$, represent gene-flow between the sub-populations (Friedman et al., 2008; Hanks and Hooten, 2013; Petkova et al., 2016). The Gaussian approximation has the advantage that we can analytically marginalize out the latent frequency variables. The resulting likelihood of the observed frequencies shares a number of similarities to that of EEMS (see Materials and methods).

To prevent over-fitting we use penalized maximum likelihood to estimate the edge weights of the graph. Our overall goal is thus to solve the following optimization problem:

$$
w^=argminl\leqw\lequ ℓ(w)+ϕ_{\lambda}(w),
$$

where $𝒘$ is a vector that stores all the unique elements of the weighted adjacency matrix, $𝒍$ and $𝒖$ are element-wise non-negative lower and upper bounds for $𝒘$, $ℓ⁢(𝒘)$ is the negative log-likelihood function that comes from the GMRF model described above, and $ϕ_{\lambda}⁢(𝒘)$ is a penalty that controls how constant or smooth the output migration surface will be and is controlled by the hyperparameter $\lambda>0$. Writing $𝒱$ to denote the set of nodes in the graph and $ℰ⁢(i)⊂𝒱$ to denote the subset of nodes that have edges connected to node $i$, our penalty is given by

$$
ϕ_{\lambda}⁢(𝒘)=\frac{\lambda}{2}⁢\sumi\in𝒱\sumk,ℓ\inℰ⁢(i)(log⁡(e^{w_{i⁢k}/w^_{0}}-1)-log⁡(e^{w_{i⁢ℓ}/w^_{0}}-1))^{2}.
$$

This function serves to penalize large differences between the weights $w_{i⁢k}$ and $w_{i⁢ℓ}$ on edges that are adjacent, that is, penalizing differences for any pair of edges that share a common node. The tuning parameter λ controls the overall strength of the penalization placed on the output of the migration surface—if λ is large, the fitted surface will favor a homogeneous set of inferred migration weights on the graph, while if λ is low, more flexible graphs can be fitted to recover richer local structure, but this suffers from the potential for over-fitting. The tuning parameter λ is selected by evaluating the model’s performance at predicting allele frequencies at held out locations using leave-one-out cross-validation (see Materials and methods ‘Leave-one-out cross-validation to select tuning parameters’).

The scale parameter $w^_{0}$ is chosen first fitting a ‘constant $w$’ model, which is a spatially homogeneous isolation-by-distance model constrained to have a single $w$ value for all edges. In the $ϕ_{\lambda}$ penalty, for adjacent edges $(i,k)$ and $(i,ℓ)$, if $w_{i⁢k}$ and $w_{i⁢ℓ}$ are large (relative to $w^_{0}$) then the corresponding term of the penalty is approximately proportional to $(w_{i⁢k}-w_{i⁢ℓ})^{2}$, penalizing differences among neighboring edges on a linear scale; if instead $w_{i⁢k}$ and $w_{i⁢ℓ}$ are small relative to $w^_{0}$, then the penalty is approximately proportional to $(log⁡(w_{i⁢k})-log⁡(w_{i⁢ℓ}))^{2}$, penalizing differences on a logarithmic scale. In fact, it is also possible to consider treating this scale parameter as a second tuning parameter—we can define a penalty function $ϕ_{\lambda,\alpha}⁢(𝒘)=\frac{\lambda}{2}⁢\sum_{i\in𝒱}\sum_{k,ℓ\inℰ⁢(i)}(log⁡(e^{\alpha⁢w_{i⁢k}}-1)-log⁡(e^{\alpha⁢w_{i⁢ℓ}}-1))^{2}$, and explore the solution across different values of both λ and α. However, we find that empirically choosing $\alpha=1/w^_{0}$ offers good performance as well as an intuitive interpretation (i.e. scaling edge weights $w_{i⁢k}$ with reference to the constant-$w$ model), and allows us to avoid the computational burden of searching a two-dimensional tuning parameter space.

We use sparse linear algebra routines to efficiently compute the objective function and gradient of our parameters, allowing for the use of widely applied quasi-Newton optimization algorithms (Nocedal and Wright, 2006) implemented in standard numerical computing libraries like scipy (Virtanen et al., 2020) (RRID:SCR_008058). See the Materials and methods section for a detailed description of the statistical models and algorithms used.

### Evaluating FEEMS on ‘out of model’ coalescent simulations

While our statistical model is not directly based on a population genetic process, it is useful to see how it performs on simulated data under the coalescent stepping stone model (Figure 2, also see Appendix 1—figure 2 for additional scenarios). In these simulations we know, by construction, the model we fit (FEEMS) is different from the true model we simulate data under (the coalescent), allowing us to assess the robustness of the fit to a controlled form of model mis-specification.

![Figure 2.](https://cdn.elifesciences.org/articles/61927/elife-61927-fig2-v1.jpg)

**Figure 2.:** In each simulation, we used leave-one-out cross-validation (at the level of sampled nodes) to select the smoothness parameter λ. The first column (A–C) shows the ground-truth and fit of FEEMS to coalescent simulations with a homogeneous migration history that is, a single migration parameter for all edge weights. Note that the ground-truth simulation figures (A,D,G) display coalescent migration rates, not fitted effective migration rates output by FEEMS. The second column (D–F) shows the ground truth and fit of FEEMS to simulations with a heterogeneous migration history that is, reduced gene-flow, with 10-fold lower migration, in the center of the habitat. The third column (G–I) shows the ground truth and fit of FEEMS to an anisotropic migration history with edge weights facing east-west having five fold higher migration than north-south. The second row (B,E,H) shows a sampling design with no missing observations on the graph. The final row (C,F,I) shows a sampling design with 80% of nodes missing at random.

The first migration scenario (Figure 2A–C) is a spatially homogeneous model where all the migration rates are set to be a constant value on the graph, this is equivalent to simulating data under an homogeneous isolation-by-distance model. In the second migration scenario (Figure 2D–E), we simulate a non-homogeneous process by representing a geographic barrier to migration, lowering the migration rates by a factor of 10 in the center of the habitat relative to the left and right regions of the graph. Finally, in the third migration scenario (Figure 2G–I), we simulate a pattern which corresponds to anisotropic migration with edges that point east/west being assigned to a fivefold higher migration rate than edges pointing north/south. For each migration scenario, we simulate two sampling designs. In the first ‘dense-sampling’ design (Figure 2B,E,I) we sample individuals for every node of the graph. Next, in the ‘sparse-sampling’ design (Figure 2C,F,J) we sample individuals for only a randomly selected 20% of the nodes.

For each coalescent simulation, we used leave-one-out cross-validation (at the level of sampled nodes) to select the smoothness parameter λ. In the homogeneous migration simulations, the best value for the smoothness parameter, as determined by the grid value with the lowest leave-one-out cross-validation error, is $\lambda_{cv}=100$ in both sampling scenarios with complete and missing data. In the heterogeneous migration simulations $\lambda_{cv}=0.298$ with no missing data and $\lambda_{cv}=37.927$ with missing data. Finally, in the anisotropic simulations with no missing data $\lambda_{cv}=0.298$ and with missing data $\lambda_{cv}=0.042$. We note the magnitude of the selected λ depends on the scale of the loss function so comparisons across different datasets are not generally interpretable.

With regard to the visualizations of effective migration, FEEMS performs best when all the nodes are sampled on the graph, that is, when there is no missing data (Figure 2B,E,H). Interestingly, in the simulated scenarios with many missing nodes, FEEMS can still partly recover the migration history, including the presence of anisotropic migration (Figure 2I). A sampling scheme with a central gap leads to a slightly narrower barrier in the heterogeneous migration scenario (Appendix 1—figure 2I) and for the anisotropic scenario, a degree of over-smoothness in the northern and southern regions of the center of the graph (Appendix 1—figure 2N). For the missing at random sampling design, FEEMS is able to recover the relative edge weights surprisingly well for all scenarios, with the inference being the most challenging when there is anisotropic migration. The potential for FEEMS to recover anisotropic migration is novel relative to EEMS, which was parameterized for fitting non-stationary isotropic migration histories and produces banding patterns perpendicular to the axis of migration when applied to data from anisotropic coalescent simulations (Petkova et al., 2016, Supplementary Figure 2; see also Appendix 1 ‘Edge versus node parameterization’ for a related discussion). Overall, even with sparsely sampled graphs, FEEMS is able to produce visualizations that qualitatively capture the migration history in coalescent simulations.

### Application of FEEMS to genotype data from North American gray wolves

To assess the performance of FEEMS on real data, we used a previously published dataset of 111 gray wolves sampled across North America typed at 17,729 SNPs (Schweizer et al., 2016; Appendix 1—figure 5). This dataset has a number of advantageous features that make it a useful test case for evaluating FEEMS: (1) The broad sampling range across North America includes a number of relevant geographic features that, a priori, could conceivably lead to restricted gene-flow averaged throughout the population history. These geographic features include mountain ranges, lakes, and islands. (2) The scale of the data is consistent with many studies for non-model systems whose spatial population structure is of interest. For instance, the relatively sparse sampling leads to a challenging statistical problem where there is the potential for many unobserved nodes (sub-populations), depending the density of the grid chosen.

Before applying FEEMS, we confirmed a signature of spatial structure in the data through regressing genetic distances on geographic distances and top genetic PCs against geographic coordinates (Appendix 1—figures 6, 7, 8, 9). We also ran multiple replicates of ADMIXTURE for $K=2$ to $K=8$, selecting for each $K$ the highest likelihood run among replicates to visualize (Appendix 1—figure 10). As expected in a spatial genetic dataset, nearby samples have similar admixture proportions and continuous gradients of changing ancestries are spread throughout the map (Bradburd et al., 2018). Whether such gradients in admixture coefficients are due to isolation by distance or specific geographic features that enhance or diminish the levels of genetic differentiation is an interpretive challenge. Explicitly modeling the spatial locations and genetic distance jointly using a method like EEMS or FEEMS is exactly designed to explore these types of questions in the data (Petkova, 2013; Petkova et al., 2016).

We first show FEEMS results for four different values of the smoothness parameter, λ from large $\lambda=100$ to small $\lambda=0.0008$ (Figure 3). One interpretation of our regularization penalty is that it encourages fitting models of homogeneous and isotropic migration. When λ is very large (Figure 3A), we see FEEMS fits a model where all of the edge weights on the graph nearly equal the mean value, hence all the edge weights are colored white in the relative log-scale. In this case, FEEMS is fitting a relatively homogeneous migration model where all the estimated edge weights get assigned nearly the same value on the graph. As we sequentially lower the penalty parameter, (Figure 3B,C,D) the fitted graph begins to appear more complex and heterogeneous as expected (discussed further below). Figure 3E shows the cross-validation error for a pre-defined grid of λ values (also see Appendix 1—figure 6 for visualizations of the fitted versus genetic distance on the full dataset).

![Figure 3.](https://cdn.elifesciences.org/articles/61927/elife-61927-fig3-v1.jpg)

**Figure 3.:** The fit of FEEMS to the North American gray wolf dataset for different choices of the smoothing regularization parameter λ: (A) $\lambda=100$, (B) $\lambda=2.06$, (C) $\lambda=0.04$, and (D) $\lambda=0.0008$.As expected, when λ decreases from large to small (A–D), the fitted graph becomes less smooth and eventually over-fits to the data, revealing a patchy surface in (D), whereas earlier in the regularization path FEEMS fits a homogeneous surface with all edge weights having nearly the same fitted value, as in (A). (E) shows the mean square error between predicted and held-out allele frequencies output by running leave-one-out cross-validation to select the smoothness parameter λ. The cross-validation error is minimized over a pre-selected grid at an intermediate value of $\lambda=2.06$ as shown in (B).

The cross-validation approach finds the optimal value of λ to be 2.06. This solution visually appears to have a moderate level of regularization and aligns with several known landscape features (Figure 4). Spatial features in the FEEMS visualization qualitatively matches the structure plot output from ADMIXTURE using $K=6$ (Appendix 1—figure 10). We add labels on the figure to highlight a number of pertinent features: (A) St. Lawrence Island, (B) the coastal islands and mountain ranges in British Columbia, (C) the boundary of Boreal Forest and Tundra eco-regions in the Shield Taiga, (D) Queen Elizabeth Islands, (E) Hudson Bay, and (F) Baffin Island. Many of these features were described in Schweizer et al., 2016 by interpretation of ADMIXTURE, PCA, and $F_{S⁢T}$ statistics. FEEMS is able to succinctly provide an interpretable view of these data in a single visualization. Indeed many of these geographic features plausibly impact gray wolf dispersal and population history (Schweizer et al., 2016).

![Figure 4.](https://cdn.elifesciences.org/articles/61927/elife-61927-fig4-v1.jpg)

**Figure 4.:** Leave-one-out cross-validation (at the level of sampled nodes) was used to select the smoothness parameter $\lambda=2.06$. We show the fitted parameters in log-scale with lower effective migration shown in orange and higher effective migration shown in blue. The bold text letters highlights a number of known geographic features that could have plausibly influenced wolf migration over time: (A) St. Lawrence Island, (B) Coastal mountain ranges in British Columbia, (C) The boundary of Boreal Forest and Tundra eco-regions in the Shield Taiga, (D) Queen Elizabeth Islands, (E) Hudson Bay, and (F) Baffin Island. We also display two insets to help interpret the results and compare them to EEMS. In the top left inset we show a map of sample coordinates colored by an ecotype label provided by Schweizer et al., 2016. These labels were devised using a combination of genetic and ecological information for 94 ‘un-admixed’ gray wolf samples, and the remaining samples were labeled ‘Other’. We can see these ecotype labels align well with the visualization output provided by FEEMS. In the right inset, we display a visualization of the posterior mean effective migration rates from EEMS.

### Comparison to EEMS

We also ran EEMS on the same gray wolf dataset. We used default parameters provided by EEMS but set the number of burn-in iterations to $20\times10^{6}$, MCMC iterations to $50\times10^{6}$, and thinning intervals to 2000. We were unable to run EEMS in a reasonable run time ($\leq3$ days) for the dense spatial grid of 1207 nodes so we ran EEMS and FEEMS on a sparser graph with 307 nodes.

We find that FEEMS is multiple orders of magnitude faster than EEMS, even when running multiple runs of FEEMS for different regularization settings on both the sparse and dense graphs (Table 1). We note that constructing the graph and fitting the model with very low regularization parameters are the most computationally demanding steps in running FEEMS.

**Table 1.**
 Runtimes for FEEMS and EEMS on the North American gray wolf dataset.We show a table of runtimes for FEEMS and EEMS for two different grid densities, a sparse grid with 307 nodes and a dense grid with 1207 nodes. The second row shows the FEEMS run-times for applying leave-one-out cross-validation to select λ. The third row shows the run-times when applying FEEMS at the best λ value selected using cross-validation. FEEMS is orders of magnitude faster than EEMS, even when using cross-validation to select λ. Runtimes are based on computation using Intel Xeon E5-2680v4 2.4 GHz CPUs with 5 Gb RAM reserved using the University of Chicago Midway2 cluster.


<table>
  <thead>
    <tr>
      <th>Method</th>
      <th>Sparse grid (run-time)</th>
      <th>Dense grid (run-time)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>EEMS</td>
      <td>27.43 hr</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>FEEMS (Cross-validation)</td>
      <td>10 min 32 s</td>
      <td>1.03 hr</td>
    </tr>
    <tr>
      <td>FEEMS (Best λ)</td>
      <td>1.23 s</td>
      <td>4.08 s</td>
    </tr>
  </tbody>
</table>

We find that many of the same geographic features that have reduced or enhanced gene-flow are concordant between the two methods. The EEMS visualization, qualitatively, best matches solutions of FEEMS with lower λ values (Figure 4, Appendix 1—figure 11); however, based on the ADMIXTURE results, visual inspection in relation to known geographical features and inspection of the observed vs fitted dissimilarity values (Appendix 1—figures 14, 22), we find these solutions to be less satisfying compared to the FEEMS solution found with λ chosen by leave-one-out cross-validation. We note that in many of the EEMS runs the MCMC appears to not have converged (based on visual inspection of trace plots) even after a large number of iterations.

## Discussion

FEEMS is a fast approach that provides an interpretable view of spatial population structure in real datasets and simulations. We want to emphasize that beyond being a fast optimization approach for inferring population structure, our parameterization of the likelihood opens up a number of exciting new directions for improving spatial population genetic inference. Notably, one major difference between EEMS and FEEMS is that in FEEMS each edge weight is assigned its own parameter to be estimated, whereas in EEMS each node is assigned a parameter and each edge is constrained to be the average effective migration between the nodes it connects (see Materials and methods and Appendix 1 ‘Edge versus node parameterization’ for details). The node-based parameterization in EEMS makes it difficult to incorporate anisotropy and asymmeteric migration (Lundgren and Ralph, 2019). As we have shown here, FEEMS’s simple and novel parameterization already has potential to fit anisotropic migration (as shown in coalescent simulations) and may be extendable to other more complex migration processes (such as long-range migration, see below).

One general challenge, which is not unique to this method, is selecting the tuning parameters controlling the strength of regularization (λ in our case). A natural approach is to use cross-validation, which estimates the out-of-sample fit of FEEMS for a particular choice of λ. We used leave-one-out cross-validation, leaving one sampled population out at a time, and find such an approach works well based on the coalescent simulations and application to the North American wolf data. That said, we sometimes found high variability in the selected solution when we used cross-validation with fewer folds (e.g. five-fold versus leave-one-out, results not shown). We expect this happens when the number of sampled populations is small relative to the complexity of the gene flow landscape, and we recommend using leave-one-out cross-validation in general. We also find it useful to fit FEEMS to a sequential grid of regularization parameters and to look at what features are consistent or vary across multiple fits. Informally, one can gain an indication of the strongest features in the data by looking at the order they appear in the regularization path that is, what features overcome the strong penalization of smoothness in the data and that are highly supported by the likelihood. For example, early in the regularization path, we see regions of reduced gene-flow occurring in the west coast of Canada that presumably correspond to Coastal mountain ranges and islands in British Columbia (Figure 3B) and this reduced gene-flow appears throughout more flexible fits with lower λ.

An important caveat is that the objective function we optimize is non-convex so any visualization output by FEEMS should be considered a local optimum and, keeping in mind that with different initialization one could get different results. That said, for the datasets investigated, we found the output visualizations were not sensitive to initialization, and thus our default setting is constant initialization fitted under an homogeneous isolation by distance model (See Materials and methods).

When comparing to EEMS, we found FEEMS to be much faster (Table 1). While this is encouraging, care must be taken because the goals and outputs of FEEMS and EEMS have a number of differences. FEEMS fits a sequential grid of solutions for different regularization parameters, whereas EEMS infers a posterior distribution and outputs the posterior mean as a point estimate. FEEMS is not a Bayesian method and unlike EEMS, which explores the entire landscape of the posterior distribution, FEEMS returns a particular point estimate: a local minimum point of the optimization landscape. Setting the prior hyper-parameters in EEMS act somewhat like a choice of the tuning parameter λ, except that EEMS uses hierarchical priors that in principle allow for exploration of multiple scales of spatial structure in a single run, but requires potentially long computation times for adequate MCMC convergence.

Like EEMS, FEEMS is based on an assumed underlying spatial graph of populations exchanging gene flow with neighboring populations. While the inferred migration rates explain the data under an assumed model, it is important for users and readers of FEEMS results to keep in mind the range and density of the chosen grid when interpreting results. We note that using a denser grid has the two potential advantages of providing improved approximation for continuously distributed species, as well as a more flexible model space to fit the data.

Depending on the scale of the analysis and the life history of the species, the process of assuming and assigning a single geographic location for each individual is a potential limitation of the modeling framework used here. For instance, the North American wolves studied here are understood to be generally territorial with individual ranges that are on the scale of 103 km2 (Burch et al., 2005), which is small relative to the greater than 106 km2 scale of our analysis. Thus, modeling individual wolves with single locations may not generally be problematic. However, at the boundary of the Boreal forest and Tundra, there are wolves with larger annual ranges and seasonal migrations that track caribou herds roughly north-south over distances of 1000 km (Musiani et al., 2007), and the wolves in the study were sampled in the winter (Musiani et al., 2007; Schweizer et al., 2016). If the samples were instead obtained in the summer, the position of the inferred low migration feature near the boundary of the Boreal Forest (marked 'C' in Figure 4) would presumably shift northward. The general cautionary lesson is that one must be careful when interpreting these maps to consider the life history of dispersal for the organism under study during the interpretation of results. Extending the methodology to incorporate knowledge of uncertainty in position or known dispersal may be an interesting direction for future work.

One natural extension to FEEMS, pertinent to a number of biological systems, is incorporating long-range migration (Pickrell and Pritchard, 2012; Bradburd et al., 2016). In this work, we have used a triangular lattice embedded in geographic space and enforced smoothness in nearby edge weights through penalizing their squared differences (see Materials and methods). We could imagine changing the structure of the graph by adding edges to allow for long-range connections; however, our current regularization scheme would not be appropriate for this setting. Instead, we could imagine adding an additional penalty to the objective, which would only allow a few long range connections to be tolerated. This could be considered to be a combination of two existing approaches for graph-based inference, graphical lasso (GLASSO) and graph Laplacian smoothing, combining the smoothness assumption for nearby connections and the sparsity assumption for long-range connections (Friedman et al., 2008; Wang et al., 2016). Another potential methodological avenue to incorporate long-range migration is to use a ‘greedy’ approach. We could imagine adding long-range edges one a time, guided by re-fitting the spatial model and taking a data-driven approach to select particular long-range edges to include. The proposed greedy approach could be considered to be a spatial graph analog of TreeMix (Pickrell and Pritchard, 2012).

Another interesting extension would be to incorporate asymmetric migration into the framework of resistance distance and Gaussian Markov Random Field based models. FEEMS, like EEMS, used a likelihood that is based on resistance distances, which are limited in their ability to model asymmetric migration (Lundgren and Ralph, 2019). Recently, Hanks, 2015 developed a promising new framework for deriving the stationary distribution of a continuous time stochastic process with asymmetric migration on a spatial graph. Interestingly, the expected distance of this process has similarities to the resistance distance-based models, in that it depends on the pseudo-inverse of a function of the graph Laplacian. Hanks, 2015 used MCMC to estimate the effect of known covariates on the edge weights of the spatial graph. Future work could adapt this framework into the penalized optimization approach we have considered here, where adjacent edge weights are encouraged to be smooth.

Finally, when interpreted as mechanistic rather than statistical models, both EEMS and FEEMS implicitly assume time-stationarity, so the estimated migration parameters should be considered to be ‘effective’ in the sense of being averaged over time in a reality where migration rates are dynamic and changing (Pickrell and Reich, 2014). The MAPS method is one recent advance that utilizes long stretches of shared haplotypes between pairs of individuals to perform Bayesian inference of time varying migration rates and population sizes (Al-Asadi et al., 2019). With the growing ability to extract high quality DNA from ancient samples, another exciting future direction would be to apply FEEMS to ancient DNA datasets over different time transects in the same focal geographic region to elucidate changing migration histories (Mathieson et al., 2018). There are a number of technical challenges in ancient DNA data that make this a difficult problem, particularly high levels of missing and low-coverage data. Our modeling approach could be potentially more robust, in that it takes allele frequencies as input, which may be estimable from dozens of ancient samples at the same spatial location, in spite of high degrees of missingness (Korneliussen et al., 2014).

In closing, we look back to a review titled ‘How Can We Infer Geography and History from Gene Frequencies?’ published in 1982 (Felsenstein, 1982). In this review, Felsenstein laid out fundamental open problems in statistical inference in population genetic data, a few of which we restate as they are particularly motivating for our work:

The methods developed here aim to help address these longstanding problems in statistical population genetics and to provide a foundation for future work to elucidate the role of geography and dispersal in ecological and evolutionary processes.

## Materials and methods

### Model description

See Appendix 1 ‘Mathematical notation’ for a detailed description of the notation used to describe the model. To visualize and model spatial patterns in a given population genetic dataset, FEEMS uses an undirected graph, $𝒢=(𝒱,ℰ)$ with $|𝒱|=d$, where nodes represent sub-populations and edge weights $(w_{k⁢ℓ})_{(k,ℓ)\inℰ}$ represent the level of gene-flow between sub-populations $k$ and $ℓ$. For computational convenience, we assume $𝒢$ is a highly sparse graph, specifically a triangular grid that is embedded in geographic space around the sample coordinates. We observe a genotype matrix, $𝒀\inℝ^{n\timesp}$, with $n$ rows representing individuals and $p$ columns representing SNPs. We imagine diploid individuals are sampled on the nodes of $𝒢$ so that $y_{i⁢j}⁢(k)\in{0,1,2}$ records the count of some arbitrarily predefined allele in individual $i$, SNP $j$, on node $k\in𝒱$. We assume a commonly used simple Binomial sampling model for the genotypes:

$$
y_{ij}(k)| f_{j}(k)∼Binomial(2,f_{j}(k)),
$$

where conditional on $f_{j}⁢(k)$ for all $j,k$, the $y_{i⁢j}⁢(k)$’s are independent. We then estimate an allele frequency at each node and SNP by maximum likelihood:

$$
f^_{j}⁢(k)=\frac{\sum_{i=1}^{n_{k}}y_{i⁢j}⁢(k)}{2⁢n_{k}},
$$

where $n_{k}$ is the number of individuals sampled at node $k$. We estimate allele frequencies at $o$ of the observed nodes out of $d$ total nodes on the graph. From Equation (1), the estimated frequency in a particular sub-population, conditional on the latent allele frequency, will approximately follow a Gaussian distribution:

$$
f^_{j}(k)| f_{j}(k)∼𝒩(f_{j}(k),\frac{f_{j}(k)(1−f_{j}(k))}{2n_{k}}).
$$

Using vector notation, we represent the joint model of estimated allele frequencies as:

$$
f^_{j}| f_{j}∼𝒩_{o}(Af_{j},diag(d_{f,n})),
$$

where $𝒇^_{j}$ is a $o\times1$ vector of estimated allele frequencies at observed nodes, $𝒇_{j}$ is a $d\times1$ vector of latent allele frequencies at all the nodes (both observed and unobserved), and $𝑨$ is a $o\timesd$ node assignment matrix where $𝑨_{k⁢ℓ}=1$ if the kth estimated allele frequency comes from sub-population $ℓ$ and $𝑨_{k⁢ℓ}=0$ otherwise; and $diag⁢(𝒅_{𝒇,𝒏})$ denotes a $o\timeso$ diagonal matrix whose diagonal elements corresponds to the appropriate variance term at observed nodes.

To summarize, we estimate allele frequencies from a subset of nodes on the graph and define latent allele frequencies for all the nodes of the graph. The assignment matrix $𝑨$ maps these latent allele frequencies to our observations. Our summary statistics (the data) are thus $(𝑭^,𝒏)$ where $𝑭^$ is a $o\timesp$ matrix of estimated allele frequencies and $𝒏$ is a $o\times1$ vector of sample sizes for every observed node. We assume the latent allele frequencies come from a Gaussian Markov Random Field:

$$
𝒇_{j}∼𝒩_{d}⁢(\mu_{j}⁢𝟏,\mu_{j}⁢(1-\mu_{j})⁢𝑳^{†}),
$$

where $𝑳$ is the graph Laplacian, † represents the pseudo-inverse operator, and $\mu_{j}$ represents the average allele frequency across all of the sub-populations. Note that the multiplication by the SNP-specific factor $\mu_{j}⁢(1-\mu_{j})$ ensures that the variance of the latent allele frequencies vanishes as the average allele frequency approaches to 0 or 1. One interpretation of this model is that the expected squared Euclidean distance between latent allele frequencies on the graph, after being re-scaled by $\mu_{j}⁢(1-\mu_{j})$, is exactly the resistance distance of an electrical circuit (McRae, 2006; Hanks and Hooten, 2013):

$$
\frac{E[(f_{j}(k)−f_{j}(ℓ))^{2}]}{\mu_{j}(1−\mu_{j})}=r_{kℓ},where r_{kℓ}=(o_{k}−o_{ℓ})^{⊤}L^{†}(o_{k}−o_{ℓ})=L_{kk}^{†}−2L_{kℓ}^{†}+L_{ℓℓ}^{†},
$$

where $𝒐_{i}$ is a one-hot vector (i.e. storing a 1 in element $i$ and zeros elsewhere). It is known that the resistance distance $r_{k⁢ℓ}$ is equivalent to the expected commute time between nodes $k$ and $ℓ$ of a random walker on the weighted graph $𝒢$ (Chandra et al., 1996). Additionally, the model (Equation 3) forms a Markov random field, and thus any latent allele frequency $f_{j}⁢(k)$ is conditionally independent of all other allele frequencies given its neighbors which are encoded by nonzero elements of $𝑳$ (Lauritzen, 1996; Koller and Friedman, 2009). Since we use a triangular grid embedded in geographic space to define the graph $𝒢$, the pattern of nonzero elements is prefixed by the structure of the sparse traingular grid.

Using the law of total variance formula, we can derive from (Equations 2, 3) an analytic form for the marginal likelihood. Before proceeding, however, we further approximate the model by assuming $\frac{1}{2}⁢f_{j}⁢(k)⁢(1-f_{j}⁢(k))≈\sigma^{2}⁢\mu_{j}⁢(1-\mu_{j})$ for all $j$ and $k$ (see Appendix 1 ‘Estimating the edge weights under the exact likelihood model’ for the data model without this approximation). This assumption is mainly for computational purposes and may be a coarse approximation in general. On the other hand, the assumption is not too strong if we exclude SNPs with extremely rare allele frequencies, and more importantly, we find it leads to a good empirical performance, both statistically and computationally. With this approximation, the residual variance parameter $\sigma^{2}$ is still unknown and needs to be estimated.

Under (Equation 2, 3), the law of total variance formula leads to specific formulas for the mean and variance structure as given in (Equation 4). With those results, we arrive at the following approximate marginal likelihood:

$$
𝒇^_{j}∼𝒩_{o}⁢(\mu_{j}⁢𝟏,\mu_{j}⁢(1-\mu_{j})⋅(𝑨⁢𝑳^{†}⁢𝑨^{⊤}+\sigma^{2}⁢diag⁢(𝒏^{-1}))),
$$

where $diag⁢(𝒏^{-1})$ is a $o\timeso$ diagonal matrix computed from the sample sizes at observed nodes. We note the marginal distribution of $f^_{j}$ is not necessarily a Gaussian distribution; however, we use a Gaussian approximation to facilitate computation.

To remove the SNP means we transform the estimated frequencies by a contrast matrix, $𝑪\inℝ^{(o-1)\timeso}$, that is orthogonal to the one-vector:

$$
𝑪⁢𝒇^_{j}∼\sqrt{\mu_{j}⁢(1-\mu_{j})}⋅𝒩_{o-1}⁢(,𝑪⁢𝑨⁢𝑳^{†}⁢𝑨^{⊤}⁢𝑪^{⊤}+\sigma^{2}⁢𝑪⁢diag⁢(𝒏^{-1})⁢𝑪^{⊤}).
$$

Let $𝚺^=\frac{1}{p}⁢𝑭^_{s}⁢𝑭^_{s}^{⊤}$ be the $o\timeso$ sample covariance matrix of estimated allele frequencies after re-scaling, that is, $𝑭^_{s}$ is a matrix formed by rescaling the columns of $𝑭^$ by $\sqrt{\mu^_{j}⁢(1-\mu^_{j})}$, where $\mu^_{j}$ is an estimate of the average allele frequency (see above). We can then express the model in terms of the transformed sample covariance matrix:

$$
p⋅𝑪⁢𝚺^⁢𝑪^{⊤}∼𝒲_{o-1}⁢(𝑪⁢𝑨⁢𝑳^{†}⁢𝑨^{⊤}⁢𝑪^{⊤}+\sigma^{2}⁢𝑪⁢diag⁢(𝒏^{-1})⁢𝑪^{⊤},p),
$$

where $𝒲_{p}$ denotes a Wishart distribution with $p$ degrees of freedom. Note we can equivalently use the sample squared Euclidean distance (often refereed to as a genetic distance) as a summary statistic: letting $𝑫^$ be the genetic distance matrix with $𝑫^_{k⁢ℓ}=\sum_{j=1}^{p}(f^_{j}⁢(k)-f^_{j}⁢(ℓ))^{2}/p⋅\mu^_{j}⁢(1-\mu^_{j})$, we have

$$
𝑫^=𝟏⁢diag⁢(𝚺^)^{⊤}+diag⁢(𝚺^)⁢𝟏^{⊤}-2⁢𝚺^,
$$

and so

$$
𝑪⁢𝑫^⁢𝑪^{⊤}=-2⁢𝑪⁢𝚺^⁢𝑪^{⊤},
$$

using the fact that the contrast matrix $𝑪$ is orthogonal to the one-vector. Thus, we can use the same spatial covariance model implied by the allele frequencies once we project the distances on to the space of contrasts:

$$
-\frac{p}{2}⋅𝑪⁢𝑫^⁢𝑪^{⊤}∼𝒲_{o-1}⁢(𝑪⁢𝑨⁢𝑳^{†}⁢𝑨^{⊤}⁢𝑪^{⊤}+\sigma^{2}⁢𝑪⁢diag⁢(𝒏^{-1})⁢𝑪^{⊤},p).
$$

Overall, the negative log-likelihood function implied by our spatial model is the following (ignoring constant terms):

$$
ℓ(w,\sigma^{2};CΣ^C^{⊤})=p⋅tr((CAL^{†}A^{⊤}C^{⊤}+\sigma^{2}Cdiag(n^{−1})C^{⊤})^{−1}CΣ^C^{⊤})−p⋅log⁡det(CAL^{†}A^{⊤}C^{⊤}+\sigma^{2}Cdiag(n^{−1})C^{⊤})^{−1},
$$

where $𝒘\inℝ^{m}$ is a vectorized form of the non-zero lower-triangular entries of the weighted adjacency matrix $𝑾$ (recall that the graph Laplacian is completely defined by the edge weights, $𝑳=diag⁢(𝑾⁢𝟏)-𝑾$, so there is an implicit dependency here). Since the graph is a triangular lattice, we only need to consider the non-zero entries to save computational time, that is, not all sub-populations are connected to each other.

We note our model (Equation 6) assumes that the $p$ SNPs are independent. This assumption is unlikely to hold when datasets are analyzed with SNPs that statistically covary (linkage disequilibrium). However, we note that the degree of freedom parameter does not affect the point estimate produced by FEEMS because it is treated as a constant term in the log-likelihood function.

One key difference between EEMS (Petkova et al., 2016) and FEEMS is how the edge weights are parameterized. In EEMS, each node is given an effective migration parameter $m_{k}$ for node $k\in𝒱$ and the edge weight is parameterized as the average between the nodes it connects, that is, $w_{k⁢ℓ}=(m_{k}+m_{ℓ})/2$ for $(k,ℓ)\inℰ$. FEEMS, on the other hand, assigns a parameter to every nonzero edge-weight. The former has fewer parameters, with the specific consequence that it only allows isotropy and imposes an additional degree of similarity among edge weights; instead, in the latter, the edge weights are free to vary apart from the regularization imposed by the penalty. See Appendix 1 ‘Edge versus node parameterization’ and Appendix 1—figures 15, 17 for more details.

### Penalty description

As mentioned previously, we would like to encourage that nearby edge weights on the graph have similar values to each other. This can be performed by penalizing differences between all edges connected to the same node, that is, spatially adjacent edges:

$$
ϕ_{\lambda,\alpha}(w)=\frac{\lambda}{2}\sumi\in𝒱\sumk,ℓ\inℰ(i)(log⁡(e^{\alphaw_{ik}}−1)−log⁡(e^{\alphaw_{iℓ}}−1))^{2},
$$

where, as before, $ℰ⁢(i)$ denotes the set of edges that is connected to node $i$. (As mentioned earlier, in practice we choose $\alpha=1/w^_{0}$, where $w^_{0}$ is the solution for the ‘constant-$w$’ model, but we use the free parameter α here for full generality.) The function $x↦log⁡(e^{x}-1)$ (on positive values $x\in(0,∞)$) is approximately equal to $x$, for $x$ much larger than 1, and is approximately equal to $log⁡(x)$, for $x$ much smaller than 1. This means that our penalty function effectively penalizes differences on the log scale for edges $(i,k)$ and $(i,ℓ)$ with very small weights, but penalizes differences on the original non-log scale for edges with large weights. Using a logarithmic-scale penalty for edges with low weights (rather than simply penalizing $(w_{i⁢k}-w_{i⁢ℓ})^{2}$) leads to smooth graphs for small edge values, and thus allow for an additional degree of flexibility across orders of magnitude of edge weights. The penalty parameter, λ, controls the overall contribution of the penalty to the objective function. It is convenient to write the penalty in matrix-vector form which we will use throughout:

$$
ϕ_{\lambda,\alpha}(w)=\frac{\lambda}{2}‖Δlog⁡(e^{\alphaw}−1)‖_{2}^{2},
$$

where $𝚫$ is a signed graph incidence matrix derived from a unweighted graph denoting if pairs of edges are connected to the same node. Specifically, in this expression, we treat $𝒘$ as a vector of length $|ℰ|$ (i.e. the number of edges), and apply the function $w↦log⁡(e^{\alpha⁢w}-1)$ entrywise to this vector. For each pair adjacent edges $(i,k)$ and $(i,ℓ)$ in the graph, there is a corresponding row of $𝚫$ with the value +1 in the entry corresponding to edge $(i,k)$, a −1 in the entry corresponding to edge $(i,ℓ)$, and 0’s elsewhere.

One might wonder whether it is possible to use the $ℓ_{1}$ norm in the penalty form Equation (8) in place of the $ℓ_{2}$ norm. While it is known that the $ℓ_{1}$ norm might increase local adaptivity and better capture the sharp changes of the underlying structure of the latent allele frequencies (e.g. Wang et al., 2016), in our case, we found an inferior performance when using the $ℓ_{1}$ norm over the $ℓ_{2}$ norm—in particular, our primary application of interest is the regime of highly missing nodes, that is, $o≪d$, in which case the global smoothing seems somewhat necessary to encourage stable recovery of the edge weights at regions with sparsely observed nodes (see Appendix 1 ‘Smooth penalty with $ℓ_{1}$norm’). In addition, adding the penalty $ϕ_{\lambda,\alpha}⁢(𝒘)$ allows us to implement faster algorithms to solve the optimization problem due to the differentiability of the $ℓ_{2}$ norm, and as a result, it leads to better overall computational savings and a simpler implementation.

### Optimization

Putting Equation (7) and Equation (8) together, we infer the migration edge weights $𝒘^$ by minimizing the following penalized negative log-likelihood function:

$$
w^=argminl\leqw\lequ ℓ(w,\sigma^{2};CΣ^C^{⊤})+ϕ_{\lambda,\alpha}(w)=argminl\leqw\lequ [p⋅tr((CAL^{†}A^{⊤}C^{⊤}+\sigma^{2}Cdiag(n^{−1})C^{⊤})^{−1}CΣ^C^{⊤})−p⋅log⁡det(CAL^{†}A^{⊤}C^{⊤}+\sigma^{2}Cdiag(n^{−1})C^{⊤})^{−1}+\frac{\lambda}{2}‖Δlog⁡(e^{\alphaw}−1)‖_{2}^{2}],
$$

where $𝒍,𝒖\inℝ_{+}^{m}$ represent respectively the entrywise lower- and upper bounds on $𝒘$, that is, we constrain the lower- and upper bound of the edge weights to $𝒍$ and $𝒖$ throughout the optimization. When no prior information is available on the range of the edge weights, we often set $𝒍=$ and $𝒖=+∞$.

One advantage of the formulation of Equation 9 is the use of the vector form parameterization $𝒘\inℝ_{+}^{m}$ of the symmetric weighted adjacency matrix $𝑾\inℝ_{+}^{d\timesd}$. In our triangular graph $𝒢=(𝒱,ℰ)$, the number of non-zero lower-triangular entries is $m=𝒪⁢(d)≪d^{2}$, so working directly on the space of vector parameterization saves computational cost. In addition, this avoids the symmetry constraint imposed on the adjacency matrix $𝑾$, hence making optimization easier (Kalofolias, 2016).

We solve the optimization problem using a constrained quasi-Newton optimization algorithm, specifically L-BFGS implemented in scipy (Byrd et al., 1995; Virtanen et al., 2020) (RRID:SCR_008058). Since our objective Equation 9 is non-convex, the L-BFGS algorithm is guaranteed to converge only to a local minimum. Even so, we empirically observe that local minima starting from different initial points are qualitatively similar to each other across many datasets. The L-BFGS algorithm requires gradient and objective values as inputs. Note the naive computation of the objective Equation 9 is computationally prohibitive because inverting the graph Laplacian has complexity $𝒪⁢(d^{3})$. We take advantage of the sparsity of the graph and specific structure of the problem to efficiently compute gradient and objective values. In theory, our implementation has computational complexity of $𝒪⁢(d⁢o+o^{3})$ per iteration which, in the setting of $o≪d$, is substantially smaller than $𝒪⁢(d^{3})$. It is possible to achieve $𝒪⁢(d⁢o+o^{3})$ per-iteration complexity by using a solver that is specially designed for a sparse Laplacian system. In our work, we use sparse Cholesky factorization which may slightly slow down the per-iteration complexity (See Appendix Material for the details of the gradient and objective computation).

### Estimating the residual variance and edge weights under the null model

For estimating the residual variance parameter $\sigma^{2}$, we first estimate it via maximum likelihood assuming homogeneous isolation by distance. This corresponds to the scenario where every edge-weight in the graph is given the exact same unknown parameter value $w_{0}$. Under this model, we only have two unknown parameters $w_{0}$ and the residual variance $\sigma^{2}$. We estimate these two parameters by jointly optimizing the marginal likelihood using a Nelder-Mead algorithm implemented in scipy (Virtanen et al., 2020) (RRID:SCR_008058). This requires only likelihood computations which are efficient due to the sparse nature of the graph. This optimization routine outputs an estimate of the residual variance $\sigma^^{2}$ and the null edge weight $w^_{0}$, which can be used to construct $𝑾⁢(w^_{0})$ and in turn $𝑳⁢(w^_{0})$.

One strategy we found effective is to fit the model of homogeneous isolation by distance and then fix the estimated residual variance $\sigma^^{2}$ throughout later fits of the more flexible penalized models—See Appendix 1 ‘Jointly estimating the residual variance and edge weights’. Additionally, we find that initializing the edge weights to $w^_{0}$ to be a useful and intuitive strategy to set the initial values for the entries of $𝒘$ to the correct scale.

### Leave-one-out cross-validation to select tuning parameters

FEEMS estimates one set of graph edge weights for each setting of the tuning parameters λ and α which control the smoothness of the fitted edge weights. Figure 3 shows that the estimated migration surfaces vary substantially depending on the particular choices of the tuning parameters, and indeed, due to the large fraction of unobserved nodes, it can highly over-fit the observed data unless regularized accordingly. To address the issue of selecting the tuning parameters, we propose using leave-one-out cross-validation to assess each fitted model’s generalization ability at held out locations.

To simplify the notation, we write the model Equation 4 for the estimated allele frequencies in SNP $j$ as

$$
𝒇^_{j}∼𝒩_{o}⁢(𝝁_{j},𝚺_{j}),
$$

where

$$
𝝁_{j}=\mu_{j}⁢𝟏⁢and ⁢𝚺_{j}=\mu_{j}⁢(1-\mu_{j})⋅(𝑨⁢𝑳^{†}⁢𝑨^{⊤}+\sigma^{2}⁢diag⁢(𝒏^{-1})).
$$

For each fold, we hold out one node from the set of observed nodes in the graph and use the rest of the nodes to fit FEEMS across a sequential grid of regularization parameters. Note that our objective function is non-convex, so the algorithm converges to different local minima for different regularization parameters, even with the same initial value $w^_{0}$. To stabilize the cross-validation procedure, we recommend using a warm start strategy in which one solves the problem for the largest value of regularization parameters first and use this solution to initialize the algorithm at the next largest value of regularization parameters, and so on. Empirically, we find that using warm starts gives far more reliable model selection than with cold starts, where the problems over the sequence of parameters are solved independently with same initial value $w^_{0}$. We suspect that the poor performance of leave-one-out cross-validation without warm starts is attributed to spatial dependency of allele frequencies and the large fraction of unobserved nodes. Without loss of generality, we assume that the last node has been held out. Re-writing the distribution of the observed frequencies according to the split of observed nodes,

$$
f^_{j}=(f^_{j}^{tr}f^_{j}^{val})∼𝒩_{o}((\mu_{j}^{tr}\mu_{j}^{val}),(Σ_{j}^{tr}Σ_{j}^{cov}Σ_{j}^{cov⊤}Σ_{j}^{val})),
$$

the conditional mean of the observed frequency $f^_{j}^{val}$ on the held out node, given the rest, is given by

$$
f^_{j}^{val,pred}=𝔼[f^_{j}^{val}|𝒇^_{j}^{tr}]=\mu_{j}^{val}+𝚺_{j}^{cov}𝚺jtr⊤(𝒇^_{j}^{tr}-𝝁_{j}^{tr})-1.
$$

Using this formula, we can predict allele frequencies at held out locations using the fitted graph $𝑳^=𝑳^⁢(\lambda,\alpha)$ for each setting of tuning parameters λ and α. Note that in Equation (10), the parameters $\mu_{j}$ and σ are also unknown, and we use an estimate of the average allele frequency $\mu^_{j}$ and the estimated residual variance $\sigma^$ from the ‘constant-$w$’ model (they are not dependent on λ and α). Then we select the tuning parameters λ and α that output the minimum prediction error averaged over all SNPs $\frac{1}{p}\sumj‖f^_{j}^{val,pred}−f^_{j}^{val}‖_{2}^{2}$, averaged over all the held out nodes (with $o$ observed nodes in total). As mentioned earlier, in practice we choose $\alpha=1/w^_{0}$ and hence we can use the leave-one-out cross-validation to search for λ only, which allows us to avoid the computational cost of searching over the two-dimensional parameter space.

### Comparison between FEEMS and EEMS models

At a high level, we can summarize the differences between FEEMS and EEMS as follows: (1) the likelihood functions of FEEMS and EEMS are slightly different as a function of the graph Laplacian $𝑳$; (2) the migration rates are parameterized in terms of edge weights or in terms of node weights; and (3) EEMS is based on Bayesian inference and thus chooses a prior and studies the posterior distribution, while FEEMS is an optimization-based approach and thus chooses a penalty function and minimizes the penalized log-likelihood (in particular, the EEMS prior and the FEEMS penalty are both aiming for locally constant type migration surfaces). The last two points were already discussed in the above sections, so here we focus on the difference of the likelihoods between the two methods.

FEEMS develops the spatial model for the genetic differentiation through Gaussian Markov Random Field, but the resulting likelihood has similarities to EEMS (Petkova et al., 2016) which considers the pairwise coalescent times. Using our notation, we can write the EEMS model as

$$
-\frac{ν}{2}⋅𝑪⁢𝑫^^{*}⁢𝑪^{⊤}∼𝒲_{o-1}⁢(\sigma^{*}⋅𝑪⁢(\frac{1}{2}⁢𝑨⁢𝑳^{†}⁢𝑨^{⊤}+diag⁢(𝑨⁢𝒒))⁢𝑪^{⊤},ν),
$$

where $ν\in[o-1,p]$ is the effective degree of freedom, $\sigma^{*}>0$ is the scale nuisance parameter, and $𝒒$ is a $d\times1$ vector of the within-sub-population coalescent rates. $𝑫^^{*}$ represents the genetic distance matrix without re-scaling, where the $(k,ℓ)$-th element is given by $𝑫^_{k⁢ℓ}^{⋆}=\sum_{j=1}^{p}(f^_{j}⁢(k)-f^_{j}⁢(ℓ))^{2}/p$. That is, unlike FEEMS, EEMS does not consider the SNP-specific re-scaling factor $\mu_{j}⁢(1-\mu_{j})$ to account for the vanishing variance of the observed allele frequencies as the average allele frequency approaches to 0 or 1.

In Equation (11), the effective degree of freedom ν is introduced to account for the dependency across SNPs in close proximity. Because EEMS uses a hierarchical Bayesian model to infer the effective migration rates, ν is being estimated alongside other model parameters. On the other hand, FEEMS uses an optimization-based approach and the degrees of freedom has no influence on the point estimate of the migration rates. Besides the effective degree of freedom and the SNP-specific re-scaling by $\mu_{j}⁢(1-\mu_{j})$, the EEMS and FEEMS likelihoods are equivalent up to constant factors, as long as only one individual is observed per node and the residual variance $\sigma^{2}$ is allowed to vary across nodes—See Appendix 1 ‘Jointly estimating the residual variance and edge weights’ for details. The constant factors, such as $\sigma^{*}$, can be effectively absorbed into the unknown model parameters $𝑳$ and $𝒒$ and therefore they do not affect the estimation of effective migration rates, up to constant factors.

### Data description and quality control

We analyzed a population genetic dataset of North American gray wolves previously published in Schweizer et al., 2016. For this, we downloaded plink (RRID:SCR_001757) formatted files and spatial coordinates from https://doi.org/10.5061/dryad.c9b25. We removed all SNPs with minor allele frequency less than 5% and with missingness greater then 10%, resulting in a final set of 111 individuals and 17,729 SNPs.

### Population structure analyses

We fit the Pritchard, Donnelly, and Stephens model (PSD) and ran principal components analysis on the genotype matrix of North American gray wolves (Price et al., 2006; Pritchard et al., 2000). For the PSD model, we used the ADMIXTURE software (RRID:SCR_001263) on the un-normalized genotypes, running five replicates per choice of $K$, from $K=2$ to $K=8$ (Alexander et al., 2009). For each $K$, we choose the one that achieved the highest likelihood to visualize. For PCA, we centered and scaled the genotype matrix and then ran sklearn (RRID:SCR_019053) implementation of PCA, truncated to compute 50 eigenvectors.

### Grid construction

To create a dense triangular lattice around the sample locations, we first define an outer boundary polygon. As a default, we construct the lattice by creating a convex hull around the sample points and manually trimming the polygon to adhere to the geography of the study organism and balancing the sample point range with the extent of local geography using the following website https://www.keene.edu/campus/maps/tool/. We often do not exclude internal ‘holes’ in the habitat (e.g. water features for terrestrial animals), and let the model instead fit effective migration rates for those features to the extent they lead to elevated differentiation. We also emphasize the importance of defining the lattice for FEEMS as well as EEMS and suggest this should be carefully curated with prior biological knowledge about the system.

To ensure edges cover an equal area over the entire region, we downloaded and intersected a uniform grid defined on the spherical shape of earth (Sahr et al., 2003). These defined grids are pre-computed at a number of different resolutions, allowing a user to test FEEMS at different grid densities which is an important feature to explore.

### Code availability

The code to reproduce the results of this paper and more can be found at https://github.com/jhmarcus/feems-analysis (Marcus and Ha, 2021a, copy archived at swh:1:rev:f2d7330f25f8a11124db09000918ae38ae00d4a7, Marcus and Ha, 2021b). A python (RRID:SCR_008394) package implementing the method can be found at https://github.com/Novembrelab/feems.
