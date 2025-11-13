# The geometry and dimensionality of brain-wide activity

## Authors

- Zezhen Wang<sup>1</sup> ([ORCID: 0009-0006-1401-9871](https://orcid.org/0009-0006-1401-9871))
- Weihao Mai<sup>2</sup> ([ORCID: 0000-0002-2320-2276](https://orcid.org/0000-0002-2320-2276))
- Yuming Chai<sup>3</sup> ([ORCID: 0000-0003-0184-1824](https://orcid.org/0000-0003-0184-1824))
- Kexin Qi<sup>3</sup>
- Hongtai Ren<sup>5</sup>
- Chen Shen<sup>3</sup>
- Shiwu Zhang<sup>5</sup>
- Guodong Tan<sup>4</sup>
- Yu Hu<sup>2</sup> ([ORCID: 0000-0003-0790-1605](https://orcid.org/0000-0003-0790-1605)) †
- Quan Wen<sup>1</sup> ([ORCID: 0000-0003-0268-8403](https://orcid.org/0000-0003-0268-8403)) †

### Affiliations

1. School of Data Science, University of Science and Technology of China Hefei China ([ROR:04c4dkn09](https://ror.org/04c4dkn09))
2. Division of Life Science, The Hong Kong University of Science and Technology Hong Kong China ([ROR:00q4vv597](https://ror.org/00q4vv597))
3. Hefei National Laboratory for Physical Sciences at the Microscale, Center for Integrative Imaging, University of Science and Technology of China Hefei China ([ROR:04c4dkn09](https://ror.org/04c4dkn09))
4. Division of Life Sciences and Medicine, University of Science and Technology of China Hefei China ([ROR:04c4dkn09](https://ror.org/04c4dkn09))
5. Department of Precision Machinery and Precision Instrumentation, University of Science and Technology of China Hefei China ([ROR:04c4dkn09](https://ror.org/04c4dkn09))
6. Department of Mathematics, The Hong Kong University of Science and Technology Hong Kong China ([ROR:00q4vv597](https://ror.org/00q4vv597))

† Corresponding author

## Abstract

Understanding neural activity organization is vital for deciphering brain function. By recording whole-brain calcium activity in larval zebrafish during hunting and spontaneous behaviors, we find that the shape of the neural activity space, described by the neural covariance spectrum, is scale-invariant: a smaller, randomly sampled cell assembly resembles the entire brain. This phenomenon can be explained by Euclidean Random Matrix theory, where neurons are reorganized from anatomical to functional positions based on their correlations. Three factors contribute to the observed scale invariance: slow neural correlation decay, higher functional space dimension, and neural activity heterogeneity. In addition to matching data from zebrafish and mice, our theory and analysis demonstrate how the geometry of neural activity space evolves with population sizes and sampling methods, thus revealing an organizing principle of brain-wide activity.

## Introduction

Geometric analysis of neuronal population activity has revealed the fundamental structures of neural representations and brain dynamics (Churchland et al., 2012; Zhang et al., 2023; Kriegeskorte and Wei, 2021; Chung and Abbott, 2021). Dimensionality reduction methods, which identify collective or latent variables in neural populations, simplify our view of high-dimensional neural data (Cunningham and Yu, 2014).Their applications to optical and multi-electrode recordings have begun to reveal important mechanisms by which neural cell assemblies process sensory information (Stringer et al., 2019a; Si et al., 2019), make decisions (Mante et al., 2013; Yang et al., 2022), maintain working memory (Xie et al., 2022) and generate motor behaviors (Churchland et al., 2012; Nguyen et al., 2016; Lindén et al., 2022; Urai et al., 2022).

In the past decade, the number of neurons that can be simultaneously recorded in vivo has grown exponentially (Buzsáki, 2004; Ahrens et al., 2012; Jun et al., 2017; Stevenson and Kording, 2011; Nguyen et al., 2016; Sofroniew et al., 2016; Lin et al., 2022; Meshulam et al., 2019; Demas et al., 2021). This increase spans various brain regions (Musall et al., 2019; Stringer et al., 2019a; Jun et al., 2017) and the entire mammalian brain (Stringer et al., 2019b; Kleinfeld et al., 2019). As more neurons are recorded, the multidimensional neural activity space, with each axis representing a neuron’s activity level (Figure 1A), becomes more complex. The changing size of observed cell assemblies raises a number of basic questions. How does this space’s geometry evolve and what structures remain invariant with increasing number of neurons recorded?

![Figure 1.](https://cdn.elifesciences.org/articles/100666/elife-100666-fig1-v1.jpg)

**Figure 1.:** (A) Illustration of how dimensionality of neural activity ($D_{PR}$) changes with the number of recorded neurons. (B) The eigenvalues of the neural covariance matrix dictate the geometrical configuration of the neural activity space with $\sqrt{\lambda}_{i}$ being the distribution width along a principal axis. (C) Examples of two neural populations with identical dimensionality ($D_{PR}=25/11≈2.27$) but different spatial configurations, as revealed by the eigenvalue spectrum (green: ${\lambda_{i}}={7,7,1}$, blue: ${\lambda_{i}}={9,3,3}$).

A key measure, the effective dimension or participation ratio (denoted as $D_{PR}$, Figure 1B), captures a major part of variability in neural activity (Recanatesi et al., 2019; Litwin-Kumar et al., 2017; Gao et al., 2017 ; Clark et al., 2023; Dahmen et al., 2020). How does $D_{PR}$ vary with the number of sampled neurons (Figure 1A)? Two scenarios are possible: $D_{PR}$ grows continuously with more sampled neurons; $D_{PR}$ saturates as the sample size increases. Which scenario fits the brain? Furthermore, even if two cell assemblies have the same $D_{PR}$, they can have different shapes (the geometric configuration of the neural activity space, as dictated by the eigenspectrum of the covariance matrix, Figure 1C). How does the shape vary with the number of neurons sampled? Lastly, are we going to observe the same picture of neural activity space when using different recording methods such as two-photon microscopy, which records all neurons in a brain region, versus Neuropixels (Jun et al., 2017), which conducts a broad random sampling of neurons?

Here, we aim to address these questions by analyzing brain-wide Ca2+ activity in larval zebrafish during hunting or spontaneous behavior (Figure 2A) recorded by Fourier light-field microscopy (Cong et al., 2017). The small size of this vertebrate brain, together with the volumetric imaging method, enables us to capture a significant amount of neural activity across the entire brain simultaneously. To characterize the geometry of neural activity beyond its dimensionality $D_{PR}$, we examine the eigenvalues or spectrum of neural covariance (Hu and Sompolinsky, 2022; Figure 1C). The covariance spectrum has been instrumental in offering mechanistic insights into neural circuit structure and function, such as the effective strength of local recurrent interactions and the depiction of network motifs (Hu and Sompolinsky, 2022; Morales et al., 2023; Dahmen et al., 2020). Intriguingly, we find that both the dimensionality and covariance spectrum remain invariant for cell assemblies that are randomly selected from various regions of the zebrafish brain. We also verify this observation in datasets recorded by different experimental methods, including light-sheet imaging of larval zebrafish (Chen et al., 2018), two-photon imaging of mouse visual cortex (Stringer et al., 2019b), and multi-area Neuropixels recording in the mouse (Stringer et al., 2019b). To explain the observed phenomenon, we model the covariance matrix of brain-wide activity by generalizing the Euclidean Random Matrix (ERM) (Mézard et al., 1999) such that neurons correspond to points distributed in a $d$-dimensional functional or feature space, with pairwise correlation decaying with distance. The ERM theory, studied in theoretical physics (Mézard et al., 1999Goetschy and Skipetrov, 2013), provides extensive analytical tools for a deep understanding of the neural covariance matrix model, allowing us to unequivocally identify three crucial factors for the observed scale invariance.

![Figure 2.](https://cdn.elifesciences.org/articles/100666/elife-100666-fig2-v1.jpg)

**Figure 2.:** (A) Rapid light-field Ca2+ imaging system for whole-brain neural activity in larval zebrafish. (B) Inferred firing rate activity from the brain-wide calcium imaging. The ROIs are sorted by their weights in the first principal component (Stringer et al., 2019b). (C) Procedure of calculating the covariance spectrum on the full and sampled neural activity matrices. (D) Dimensionality (circles, average across eight samplings (dots)), as a function of the sampling fraction. The curve is the predicted dimensionality using Equation 5. (E) Iteratively sampled covariance matrices. Neurons are sorted in each matrix to maximize values near the diagonal. (F) The covariance spectra, that is, eigenvalue versus rank/N, for randomly sampled neurons of different sizes (colors). The gray dots represent the sorted variances $C_{ii}$ of all neurons. (G–I) Same as F but from three models of covariance (see details in Methods): (G) a Wishart random matrix calculated from a random activity matrix of the same size as the experimental data; (H) replacing the eigenvectors by a random orthogonal set; (I) covariance generated from a randomly connected recurrent network. The collapse index (CI), which quantifies the level of scale invariance in the eigenspectrum (see Methods), is: (G) CI = 0.214; (H) CI = 0.222; (I) CI = 0.139.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/100666/elife-100666-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** (A) Spatial distribution of segmented ROIs (shown in different colors). There are 1347–3086 ROIs in each animal. Scale bar, 100 μm. (B) Explained variance of the activity data by PCs up to 500 rank. The different colored lines represent different fish data (n = 6).

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/100666/elife-100666-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** (A–D) Distribution of normalized pairwise covariances, where $E(\sigma_{i}^{2})=1$ (Methods). (E–H) Sampled covariance eigenspectra of different datasets. (I–L) Pdfs of sampled covariance matrix eigenspectra of different datasets. The datasets correspond to the following examples: column 1: fish data (from fish 1, all fish data are shown in Figure 5—figure supplement 1A–F) from whole-brain light-field imaging; column 2: fish data from whole-brain light-sheet imaging; column 3: mouse data from multi-area Neuropixels recording; column 4: mouse data from two-photon visual cortex recording.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/100666/elife-100666-fig2-figsupp3-v1.jpg)

**Figure 2—figure supplement 3.:** Red: eigenspectrum of the original data covariance matrix. Blue: eigenspectrum of the covariance matrix with negative entries replaced by zeros. In this figure, all neurons recorded in each fish were utilized without any sampling. (A–F) fish 1 to fish 6.

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/100666/elife-100666-fig2-figsupp4-v1.jpg)

**Figure 2—figure supplement 4.:** Analysis of multi-area Neuropixels recordings (Stringer et al., 2019b) from 1024 neurons, downsampled to different rates resulting in 7200 time frames per condition (6, 12, 18, and 24 Hz; columns 1–4, respectively). (A–D) Distribution of pairwise covariances after normalization to unit variance ($E(\sigma_{i}^{2})=1$, see Methods). (E–H) Eigenvalue spectra of the covariance matrices, showing similar power-law scaling across sampling rates. (I–L) Probability density functions (PDFs) of the eigenvalues, demonstrating that the characteristic shape of the distribution is preserved across different temporal resolutions.

Building upon our theoretical results, we further explore the connection between the spatial arrangement of neurons and their locations in functional space, which allows us to distinguish among three sampling approaches: random sampling, anatomical sampling (akin to optical recording of all neurons within a specific region of the brain) and functional sampling (Meshulam et al., 2019). Our ERM theory makes distinct predictions regarding the scaling relationship between dimensionality and the size of cell assembly, as well as the shape of covariance eigenspectrum under various sampling methods. Taken together, our results offer a new perspective for interpreting brain-wide activity and unambiguously show its organizing principles, with unexplored consequences for neural computation.

## Results

### Geometry of neural activity across random cell assemblies in zebrafish brain

We recorded brain-wide Ca2+activity at a volume rate of 10 Hz in head-fixed larval zebrafish (Figure 2A) during hunting attempts (Methods) and spontaneous behavior using a Fourier light-field microscopy (Cong et al., 2017). Approximately 2000 ROIs (1977.3 ± 677.1, mean ± SD) with a diameter of 16.84 ± 8.51 µm were analyzed per fish based on voxel activity (Methods, Figure 2—figure supplement 1). These ROIs likely correspond to multiple nearby neurons with correlated activity. Henceforth, we refer to the ROIs as ‘neurons’ for simplicity.

We first investigate the dimensionality of neural activity $D_{PR}$ (Figure 1B) in a randomly chosen cell assembly in zebrafish, similar to multi-area Neuropixels recording in a mammalian brain. We focus on how $D_{PR}$ changes with a large sample size $N$. We find that if the mean squared covariance remains finite instead of vanishing with $N$, the dimensionality $D_{PR}$ (Figure 1B) becomes sample size independent and depends only on the variance $\sigma_{i}^{2}$ and the covariance $C_{ij}$ between neurons $i$ and $j$:

$$
limN→∞D_{PR}=\frac{E(\sigma_{i}^{2})^{2}}{E_{i\neqj}(C_{ij}^{2})},
$$

where $E(…)$ denotes average across neurons (Methods and Dahmen et al., 2020). The finite mean squared covariance condition is supported by the observation that the neural activity covariance $C_{ij}$ is positively biased and widely distributed with a long tail (Figure 2—figure supplement 2A). As predicted, the data dimensionality grows with sample size and reaches the maximum value specified by Equation 1 (Figure 2D).

Next, we investigate the shape of the neural activity space described by the eigenspectrum of the covariance matrix derived from the activity of $N$ randomly selected neurons (Figure 2C). When the eigenvalues are arranged in descending order and plotted against the normalized rank $r/N$, where $r=1,…,N$ (we refer to it as the rank plot), this curve shows an approximate power law that spans 10 folds. Interestingly, as the size of the covariance matrices decreases ($N$ decreases), the eigenspectrum curves nearly collapse over a wide range of eigenvalues. This pattern holds across diverse datasets and experimental techniques (Figure 2F, Figure 2—figure supplement 2E–L). The similarity of the covariance matrices of randomly sampled neural populations can be intuitively visualized (Figure 2E), after properly sorting the neurons (Methods).

The scale invariance in the neural covariance matrix – the collapse of the covariance eigenspectrum under random sampling – is non-trivial. The spectrum is not scale invariant in a common covariance matrix model based on independent noise (Figure 2G). It is absent when replacing the neural covariance matrix eigenvectors with random ones, keeping the eigenvalues identical (Figure 2H). A recurrent neural network with random connectivity (Hu and Sompolinsky, 2022) does not yield a scale-invariant covariance spectrum (Figure 2I). A recently developed latent variable model (Morrell et al., 2024; Appendix 1—figure 6), which is able to reproduce avalanche criticality, also fails to generate the scale-invariant covariance spectrum. Thus, a new model is needed for the covariance matrix of neural activity.

### Modeling covariance by organizing neurons in functional space

Dimension reduction methods simplify and visualize complex neuron interactions by embedding them into a low-dimensional map, within which nearby neurons have similar activities. Inspired by these ideas, we use the ERM (Mézard et al., 1999) to model neural covariance. Imagine sprinkling neurons uniformly distributed on a $d$-dimensional functional space of size $L$ (Figure 3A), where the distance between neurons $i$ and $j$ affects their correlation. Let $x→_{i}$ represent the functional coordinate of the neuron $i$. The distance-correlation dependency is described by kernel function$f(x→_{i}−x→_{j})>0$ with $f(0)=1$, indicating closer neurons have stronger correlations, and decreases as distance $‖x→_{i}−x→_{j}‖$ increases (Figure 3A and Methods). To model the covariance, we extend the ERM by incorporating heterogeneity of neuron activity levels (shown as the size of the neuron in the functional space in Figure 3A).

$$
C_{ij}=\sigma_{i}\sigma_{j}f(x→_{i}−x→_{j}),i,j=1,2,…,N.
$$

The variance of neural activity $\sigma_{i}^{2}$ is drawn i.i.d. from a given distribution and is independent of neurons’ position.

![Figure 3.](https://cdn.elifesciences.org/articles/100666/elife-100666-fig3-v1.jpg)

**Figure 3.:** (A) Schematic of the ERM model, which reorganizes neurons (circles) from the anatomical space to the functional space (here $d=2$ is a two-dimensional box). The correlation between a pair of neurons decreases with their distance in the functional space according to a kernel function $f(x→)$. This correlation is then scaled by neurons’ variance $\sigma_{i}^{2}$ (circle size) to obtain the covariance $C_{ij}$. (B) An example ERM correlation matrix (i.e., when $\sigma_{i}^{2}≡1$). (C) Spectrum (same as Figure 2F) for the ERM correlation matrix in (B). The gray dots represent the sorted variances $C_{ii}$ of all neurons (same as in Figure 2F). (D) Visualizing the distribution of the same ERM eigenvalues in C by plotting the probability density function (pdf).

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/100666/elife-100666-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** Covariance spectra under different kernel functions $f(x→)$.The figure presents both the sampled eigenvalue rank plot and the pdf of Euclidean Random Matrix (ERM) with different functions $f(x→)$ and varying dimensions $d$, where panels (A–D, I, J) display the rank plot and panels (E–H, K, L) show the pdf of ERM. (A, E) Exponential function $f(x→)=e^{−\frac{‖x‖}{b}}$ where $b=1$ and dimension $d=2$. (B, F) Exponential function $f(x→)=e^{−\frac{‖x‖}{b}}$ where $b=1$ and dimension $d=3$. (C, G) Gaussian pdf $f(x→)=e^{−\frac{‖x‖^{2}}{2\sigma_{x}^{2}}}$ where $\sigma_{x}^{2}=0.1$ and dimension $d=2$. (D, H) Gaussian pdf $f(x→)=e^{−\frac{‖x‖^{2}}{2\sigma_{x}^{2}}}$ where $\sigma_{x}^{2}=0.1$ and dimension $d=3$. (I, K) t pdf (Equation 11) and dimension $d=2$. (J, L) t pdf (Equation 11) and dimension $d=3$. The ERM simulations were conducted 100 times and each ERM used an identical sampling technique described in (Methods). The results represent mean ± SEM. (M) Summary of CIs for different $f(x→)$ and $d$. On the x-axis labels, ‘e’ denotes the Exponential function $f(x→)$, ‘g’ denotes the Gaussian pdf $f(x→)$, ‘t’ denotes the t-distribution pdf $f(x→)$, while ‘2’ and ‘3’ indicate $d=2$ or $d=3$, respectively.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/100666/elife-100666-fig3-figsupp2-v1.jpg)

**Figure 3—figure supplement 2.:** Impact of $η$ and $d$ on the scale invariance of covariance eigenspectra in the Euclidean Random Matrix (ERM) with $f(x→)=e^{−‖x→‖^{η}}$.The columns from left to right correspond to $η=0.3,0.5,0.7,0.9$, and the rows from top to bottom correspond to $d=1,2,3$ (Equations 2 and 11). Other ERM simulation parameters: $N=4096$, $ρ=256$, $L=(N/ρ)^{1/d}$, $ϵ=0.03125$, and $\sigma_{i}^{2}=1$. Each panel shows a single ERM realization. For visualization purposes, the views in some panels are truncated since we use the same range for the eigenvalues in all panels.

This multidimensional functional space may represent attributes to which neurons are tuned, such as sensory features (e.g., visual orientation Hubel and Wiesel, 1959, auditory frequency) and movement characteristics (e.g., direction, speed Stefanini et al., 2020; Kropff et al., 2015). In sensory systems, it represents stimuli as neural activity patterns, with proximity indicating similarity in features. For motor control, it encodes movement parameters and trajectories. In the hippocampus, it represents the place field of a place cell, acting as a cognitive map of physical space (O’Keefe, 1976; Moser et al., 2008; Tingley and Buzsáki, 2018).

We first explore the ERM with various forms of $f(x→)$ and find that fast-decaying functions like Gaussian and exponential functions do not produce eigenspectra similar to the data and no scale invariance over random sampling (Figure 3—figure supplement 1A–H and Appendix 2). Thus, we turn to slow-decaying functions including the power law, which produce spectra similar to the data (Figure 3C, D; see also Figure 3—figure supplement 2). We adopt a particular kernel function because of its closed-form and analytical properties: $f(x→)=ϵ^{\mu}(ϵ^{2}+‖x→‖^{2})^{−\mu/2}$ (Methods). For large distance $‖x→‖≫ϵ$, it approximates a power law $f(x→)≈ϵ^{\mu}‖x→‖^{−\mu}$ and smoothly transitions at small distance to satisfy the correlation requirement $f(0)=1$ (Appendix 1—figure 3I, J).

### Analytical theory on the conditions of scale invariance in ERM

To determine the conditions for scale invariance in ERM, we analytically calculate the eigenspectrum of covariance matrix $C$ (Equation 2) for large $N,L$ using the replica method (Mézard et al., 1999). A key order parameter emerging from this calculation is the neuron density $ρ:=N/L^{d}$. In the high-density regime $ρϵ^{d}≈1$, the covariance spectrum can be approximated in a closed form (Methods). For the slow-decaying kernel function $f(x→)$ defined above, the spectrum for large eigenvalues follows a power law (Appendix 2):

$$
\lambda∼(r/N)^{−1+\frac{\mu}{d}}ρ^{\frac{\mu}{d}},andequivalentlyp(\lambda)∼ρ^{\frac{\mu}{d−\mu}}\lambda^{−\frac{2d−\mu}{d−\mu}},
$$

where r is the rank of the eigenvalues in descending order and $p(\lambda)$ is their probability density function. Equation 3 intuitively explains the scale invariance over random sampling. Sampling in the ERM reduces the neuron density ρ. The eigenspectrum is ρ-independent whenever $\mu/d≈0$. This indicates two factors contributing to the scale invariance of the eigenspectrum. First, a small exponent μ in the kernel function $f(x→)$ means that pairwise correlations slowly decay with functional distance and can be significantly positive across various functional modules and throughout the brain. For a given μ, an increase in dimension $d$ improves the scale invariance. The dimension $d$ could represent the number of independent features or latent variables describing neural activity or cognitive states.

We verify our theoretical predictions by comparing sampled eigenspectra in finite-size simulated ERMs across different $\mu$ and $d$ (Figure 4A). We first consider the case of homogeneous neurons ($\sigma_{i}^{2}≡1$ in Equation 2, revisited later) in these simulations (Figures 3C, D, 4A), making $C$’s entries correlation coefficients. To quantitatively assess the level of scale invariance, we introduce a collapse index (CI, see Methods for a detailed definition). Motivated by Equation 3, the CI measures the shift of the eigenspectrum when the number of sampled neurons changes. The smaller CI values indicate higher scale invariance. Intuitively, it is defined as the area between spectrum curves from different sample sizes (Figure 4A, upper right). In the log–log scale rank plot, Equation 3 shows the spectrum shifts vertically with $ρ$.

![Figure 4.](https://cdn.elifesciences.org/articles/100666/elife-100666-fig4-v1.jpg)

**Figure 4.:** (A) Impact of $\mu$ and $d$ (see text) on the scale invariance of Euclidean Random Matrix (ERM) spectrum (same plots as Figure 3C) with $f(x→)=ϵ^{\mu}(ϵ^{2}+‖x→‖^{2})^{−\mu/2}$. The degree of scale invariance is quantified by the collapse index (CI), which essentially measures the area between different spectrum curves (upper right inset). For comparison, we fix the same coordinate range across panels hence some plots are cropped. The gray dots represent the sorted variances $C_{ii}$ of all neurons (same as in Figure 2F). (B) Top: sampled correlation matrix spectrum in an example animal (fish 1). Bottom: same as top but for the covariance matrix that incorporates heterogeneous variances. The gray dots represent the sorted variances $C_{ii}$ of all neurons (same as in Figure 2F). (C) The CI of the correlation matrix (filled squares) is found to be larger than that for the covariance matrix (opened squares) across different datasets: f1 to f6: six light-field zebrafish data (10 Hz per volume, this paper); fl: light-sheet zebrafish data (2 Hz per volume, Chen et al., 2018); mn: mouse Neuropixels data (downsampled to 10 Hz per volume); mp: mouse two-photon data (3 Hz per volume, Stringer et al., 2019b).

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/100666/elife-100666-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** (A–C) Rank plots of the normalized eigenspectra ($\lambda/ρ$), with the simulations obtained using correlation matrix (sim: corr, $\sigma_{i}^{2}=1$) and covariance matrix (sim: cov, neuron’s activity variance $\sigma_{i}^{2}$ is i.i.d. sampled from a log-normal distribution with zero mean and a standard deviation of 0.5 in the natural logarithm of the $\sigma_{i}^{2}$ values; we also normalize $E(\sigma_{i}^{2})=1$ (Methods)). The curves between ‘sim: corr’ and ‘sim: cov’ are nearly identical in panels (A) and (B). The theoretical predictions of normalized eigenvalues $\lambda/ρ$ are obtained using the high-density theory (cyan, Equation 12). The density ρ decreases from panel (A) to panel (C) ($ρ=1024,256,10.24$, respectively). (D–F) Numerical validation of the theoretical spectrum by comparing probability density functions for increasing density of covariance ERM ($ρ=1024,256,10.24$, respectively). Other simulation parameters: $N=1024$, $d=2$, $L=(N/ρ)^{1/d}$, $\mu=0.5$, $ϵ=0.03125$. The ERM simulations were conducted 100 times. The results are presented as the mean ± SEM.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/100666/elife-100666-fig4-figsupp2-v1.jpg)

**Figure 4—figure supplement 2.:** (A) The CI as a function of the heterogeneity of neural activity levels $E(\sigma_{i}^{4})$. We generate Euclidean Random Matrix (ERM) where each neuron’s activity variance $\sigma_{i}^{2}$ is i.i.d. sampled from a log-normal distribution where the logarithm of the variable follows a normal distribution with zero mean and a sequence of standard deviation ($0,0.05,0.1,…,0.5$) in the natural logarithm of the values $\sigma_{i}^{2}$. We also normalize $E(\sigma_{i}^{2})=1$ (Methods). The solid blue line is the average across 100 ERM simulations, and the shaded area represents the SD. The red line results from the Gaussian variational method with simulation value integration limit $q_{s}^{s}$. The green line is the result of the Gaussian variational method with high-density value integration limit $q_{s}^{h}$ (Methods). $ρ_{0}=128$. (B) Same as A, but with a smaller $ρ_{0}=10.24$. Other parameters: $\mu=0.5$, $d=2$, $N=1024$, $L=(N/ρ)^{1/d}$, $ϵ=0.03125$. (C) The collapse index (CI) of the correlation matrix (filled symbols) is larger than that of the covariance matrix (opened symbols) across different datasets excluding those shown in Figure 4. We use 7200 time frame data across all the datasets. l2 to l3: light-sheet zebrafish data (2 Hz per volume); n2 to n3: Neuropixels mouse data, downsampled to 10 Hz per volume, p2 to p3: two-photon mouse data (3 Hz per volume).

Thus, we define CI as this average displacement (Figure 4A, upper right, Methods), and a smaller CI means more scale invariant. Using CI, Figure 4A shows that scale invariance improves with slower correlation decay as $\mu$ decreases and the functional dimension $d$ increases. Conversely, with large $\mu$ and small $d$, the covariance eigenspectrum varies significantly with scale (Figure 4A).

Next, we consider the general case of unequal neural activity levels $\sigma_{i}^{2}$ and check for differences between the correlation (equivalent to $\sigma_{i}^{2}≡1$) and covariance matrix spectra. Using the collapsed index (CI), we compare the scale invariance of the two spectra in the experimental data. Intriguingly, the CI of the covariance matrix is consistently smaller (more scale-invariant) across all datasets (Figure 4C, Figure 4—figure supplement 2C, open vs. closed squares), indicating that the heterogeneity of neuronal activity variances significantly affects the eigenspectrum and the geometry of neural activity space (Tian et al., 2024). By extending our spectrum calculation to the intermediate density regime $ρϵ^{d}≪1$ (Methods), we show that the ERM model can quantitatively explain the improved scale invariance in the covariance matrix compared to the correlation matrix (Figure 4—figure supplement 2B; Table 1).

**Table 1.**
 Table of notations.


<table>
  <thead>
    <tr>
      <th>Notation</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>C\begin{document}$C$\end{document}</td>
      <td>Covariance matrix, Equation 2</td>
    </tr>
    <tr>
      <td>Cij\begin{document}$C_{ij}$\end{document}</td>
      <td>Pairwise covariance between neuron i, j; entries of C\begin{document}$C$\end{document}</td>
    </tr>
    <tr>
      <td>DPR\begin{document}$D_{\rm PR}$\end{document}</td>
      <td>Participation ratio dimension, Equation 5</td>
    </tr>
    <tr>
      <td>DPRASap\begin{document}$D_{\rm PR}^{\rm ASap}$\end{document}</td>
      <td>Anatomical sampling dimension, Equation 4</td>
    </tr>
    <tr>
      <td>λ</td>
      <td>Eigenvalue of a covariance matrix C\begin{document}$C$\end{document}</td>
    </tr>
    <tr>
      <td>p(λ)\begin{document}$p(\lambda)$\end{document}</td>
      <td>Probability density function of covariance eigenvalues, Equation 8</td>
    </tr>
    <tr>
      <td>r</td>
      <td>Rank of an eigenvalue in descending order, Equation 3</td>
    </tr>
    <tr>
      <td>q</td>
      <td>Fraction of eigenvalues up to λ and q=r/N\begin{document}$q=r/N$\end{document}; Equation 13</td>
    </tr>
    <tr>
      <td>f(x→)=f(‖x→i−x→j‖)\begin{document}$f(\vec x)=f(\|\vec x_i-\vec x_j\|)$\end{document}</td>
      <td>Kernel function or distance-correlation function, Equation 11</td>
    </tr>
    <tr>
      <td>f~(k→)\begin{document}$\tilde f(\vec k)$\end{document}</td>
      <td>Fourier transform of f(x→),f~(k→)=∫Rdf(x→)e−ix→⋅k→ddx→\begin{document}$f(\vec{x}), \tilde{f}(\vec{k})=\int_{\mathbb{R}^d} f(\vec{x}) e^{-i \vec{x} \cdot \vec{k}}d^{d}\vec x$\end{document}</td>
    </tr>
    <tr>
      <td>μ</td>
      <td>Power-law exponent in f(x→)\begin{document}$f(\vec x)$\end{document} , Equation 11</td>
    </tr>
    <tr>
      <td>ε</td>
      <td>Resolution parameter in f(x→)\begin{document}$f(\vec x)$\end{document} to smooth the singularity near 0, Equation 11</td>
    </tr>
    <tr>
      <td>N\begin{document}$N$\end{document}</td>
      <td>Number of neurons</td>
    </tr>
    <tr>
      <td>N0\begin{document}$N_0$\end{document}</td>
      <td>The total number of neurons prior to sampling</td>
    </tr>
    <tr>
      <td>k</td>
      <td>N/N0\begin{document}$N/N_0$\end{document} the fraction of sampled neurons</td>
    </tr>
    <tr>
      <td>L\begin{document}$L$\end{document}</td>
      <td>Linear box size of the functional space</td>
    </tr>
    <tr>
      <td>ρ</td>
      <td>Density of neurons in the functional space, Equation 3</td>
    </tr>
    <tr>
      <td>d\begin{document}$d$\end{document}</td>
      <td>Dimension of the functional space, Equation 3</td>
    </tr>
    <tr>
      <td>ai(t)\begin{document}$a_i(t)$\end{document}</td>
      <td>Neural activity of neuron i at time t</td>
    </tr>
    <tr>
      <td>σi2\begin{document}$\sigma _i^2$\end{document}</td>
      <td>Temporal variance of neural activity, Equation 2</td>
    </tr>
    <tr>
      <td>Cl</td>
      <td>Collapse index for measuring scale invariance, Equation 13</td>
    </tr>
    <tr>
      <td>α</td>
      <td>Power-law coefficient of eigenspectrum in the rank plot, see Discussion</td>
    </tr>
    <tr>
      <td>x→i,y→i\begin{document}$\vec x_i,\vec y_i$\end{document}</td>
      <td>Neuron i's coordinate in the functional and anatomical space, respectively</td>
    </tr>
    <tr>
      <td>v→func,v→anat\begin{document}$\vec v_{func},\vec v_{anat}$\end{document}</td>
      <td>The first canonical directions in the functional and anatomical space, respectively</td>
    </tr>
    <tr>
      <td>RCCA\begin{document}$R_{\rm CCA}$\end{document}</td>
      <td>The first canonical correlation</td>
    </tr>
    <tr>
      <td>RASap\begin{document}$R_{\rm ASap}$\end{document}</td>
      <td>Correlation between anatomical and functional coordinates along ASap direction, Equation 4</td>
    </tr>
  </tbody>
</table>

Lastly, we examine factors that turn out to have minimal impact on the scale invariance of the covariance spectrum. First, the shape of the kernel function $f(x→)$ over a small distance (small distance means f(x) near x = 0 in the functional space, Appendix 1—figure 3) does not affect the distribution of large eigenvalues (Appendix 1—figure 3, Table 3, Appendix 1—figure 2, Appendix 1—figure 1A).

This supports our use of a specific $f(x→)$ to represent a class of slow-decaying kernels. Second, altering the spatial distribution of neurons in the functional space, whether using a Gaussian, uniform, or clustered distribution, does not affect large covariance eigenvalues, except possibly the leading ones (Appendix 1—figure 1B, Appendix 1). Third, different geometries of the functional space, such as a flat square, a sphere, or a hemisphere, result in eigenspectra similar to the original ERM model (Appendix 1—figure 1C). These findings indicate that our theory for the covariance spectrum’s scale invariance is robust to various modeling details.

### Connection among random sampling, functional sampling, and anatomical sampling

So far, we have focused on random sampling of neurons, but how does the neural activity space change with different sampling methods? To this end, we consider three methods (Figure 5A1): random sampling (RSap), anatomical sampling (ASap) where neurons in a brain region are captured by optical imaging (Grewe and Helmchen, 2009; Gauthier and Tank, 2018; Stringer et al., 2019a), and functional sampling (FSap) where neurons are selected based on activity similarity (Meshulam et al., 2019). In ASap or FSap, sampling involves expanding regions of interest in anatomical space or functional space while measuring all neural activity within those regions (Appendix 1). The difference among sampling methods depends on the neuron organization throughout the brain. If anatomically localized neurons also cluster functionally (Figure 5A4), ASap ≈ FSap; if they are spread in the functional space (Figure 5A2), ASap ≈ RSap. Generally, the anatomical–functional relationship is in-between and can be quantified using the Canonical Correlation Analysis (CCA). This technique finds axes (CCA vectors $v→_{anat}$ and $v→_{func}$) in anatomical and functional spaces such that the neurons’ projection along these axes has the maximum correlation, $R_{CCA}$. The extreme scenarios described above correspond to $R_{CCA}=1$ and $R_{CCA}=0$.

![Figure 5.](https://cdn.elifesciences.org/articles/100666/elife-100666-fig5-v1.jpg)

**Figure 5.:** (A) Three sampling methods (A1) and $R_{CCA}$ (see text). When $R_{CCA}≈0$ (A2), the anatomical sampling (ASap) resembles the random sampling (RSap), and while when $R_{CCA}≈1$ (A4), ASap is similar to the functional sampling (FSap). (B) Distribution of neurons in the functional space inferred by MDS. Each neuron is color-coded by its projection along the first canonical direction $v→_{anat}$ in the anatomical space (see text). Data based on fish 6, same for (C-E). (C) Similar to (B) but plotting neurons in the anatomical space with color based on their projection along $v→_{func}$ in the functional space (see text). (D) Dimensionality ($D_{PR}$) across sampling methods: average $D_{PR}$ under RSap (circles), average and individual brain region $D_{PR}$ under ASap (squares and dots), and $D_{PR}$ under FSap for the most correlated neuron cluster (triangles; Methods). Dashed and solid lines are theoretical predictions for $D_{PR}$ under RSap and FSap, respectively (Methods). (E) The CI of correlation matrices under three sampling methods in six animals (colors). **p < 0.01; ***p < 0.001; one-sided paired t tests: RSap versus ASap, p = 0.0010; RSap versus FSap, p = 0.0004; ASap versus FSap, p = 0.0014.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/100666/elife-100666-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** Comparison of sampled covariance eigenspectra in fish data and fitted ERM models. The columns correspond to six light-field zebrafish data: fish 1 to fish 6. Number of time frames: fish 1 – 7495, fish 2 – 9774, fish 3 – 13,904, fish 4 – 7318, fish 5 – 7200, and fish 6 – 9388. (A–F) sampled covariance eigenspectra for different fish data. (G–L) Same as (A–F) but for ERM models with fitted parameters ($\mu/d$, $L$), functional coordinates inferred using MDS, and the experimental $\sigma_{i}$. (M–R) Same as (A–F) but for ERM models with fitted parameters ($\mu/d$, $L$), uniform distributed functional coordinates, and a log-normal distribution of $\sigma^{2}$. $\mu/d=[0.456,0.258,0.205,0.262,0.302,0.308]$ in fish 1–6.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/100666/elife-100666-fig5-figsupp2-v1.jpg)

**Figure 5—figure supplement 2.:** Comparison of the covariance matrix between fish data and our fitted model. The columns correspond to six light-field zebrafish data: fish 1 to fish 6. (A–F) The covariance matrix of different fish data. (G–L) The covariance matrix of ERM models with fitted parameters ($\mu$, $L$) and functional coordinates inferred using MDS and the experimental $\sigma_{i}$.

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/100666/elife-100666-fig5-figsupp3-v1.jpg)

**Figure 5—figure supplement 3.:** Columns correspond to five light-field zebrafish data: fish 1 to fish 6. (A–F) Comparison of the power-law kernel function $f(x→)$ in the model (blue line) and the correlation–distance relationship in the data (red line). The distance is calculated from the inferred coordinates using MDS. The shaded area represents the SD. (G–L) Same as (A–D) but on the log–log scale.

![Figure 5—figure supplement 4.](https://cdn.elifesciences.org/articles/100666/elife-100666-fig5-figsupp4-v1.jpg)

**Figure 5—figure supplement 4.:** Columns correspond to six light-field zebrafish data: fish 1 to fish 6. (A–F) CCA correlation between the first CCA variables with different embedding dimensions in the functional space. Blue line indicates the CCA correlation of example fish data, green line shows the CCA correlation of example fish data with shuffled functional coordinates, and error bars represent the SD.

![Figure 5—figure supplement 5.](https://cdn.elifesciences.org/articles/100666/elife-100666-fig5-figsupp5-v1.jpg)

**Figure 5—figure supplement 5.:** Columns correspond to five light-field zebrafish data: fish 1 to fish 5 (with fish 6 has been shown in Figure 5). (A–E) Distribution of neurons in the functional space, where each neuron is color-coded by the projection of its coordinate along the canonical axis $b→_{1}$ in anatomical space (see text in Result). Arrow: the first CCA direction $a→_{1}$ in functional space. (F–J) Distribution of neurons in the anatomical space with the forebrain neuron located on the left side and the hindbrain neuron on the right side. Each neuron is color-coded by the projection of its coordinate along the canonical axis $a→_{1}$ in functional space (see text in Result). Arrow: the first CCA direction $b→_{1}$ in anatomical space.

![Figure 5—figure supplement 6.](https://cdn.elifesciences.org/articles/100666/elife-100666-fig5-figsupp6-v1.jpg)

**Figure 5—figure supplement 6.:** Dimensionality ($D_{PR}$) across sampling methods in fish data.(A–F) Result from fish 1 to fish 6: mean RSap $D_{PR}$ (circles), mean (squares), and individual ASap $D_{PR}$, and FSap’s most correlated cluster $D_{PR}$ (triangles). Dashed and solid lines indicate RSap and uniform FSap theoretical predictions, respectively.

![Figure 5—figure supplement 7.](https://cdn.elifesciences.org/articles/100666/elife-100666-fig5-figsupp7-v1.jpg)

**Figure 5—figure supplement 7.:** Dimensionality ($D_{PR}$) across sampling methods in Euclidean Random Matrix (ERM).PR dimensionality result of ERM model, coordinate in funcitonal and anatomical space are multivariate Gaussian distribution, the CCA correlation between funcitonal and anatomical space are $R_{CCA}=0.4,0.6,0.8$ in (A–C). Mean RSap $D_{PR}$ (circles), mean (squares), and individual ASap $D_{PR}$, and FSap’s most correlated cluster $D_{PR}$ (triangles). Dashed and solid lines indicate RSap and uniform FSap theoretical predictions, respectively. ERM parameter:$\mu=0.6$ , $d=2$, functional coordinates follow a multivariate normal distribution with variance $\sigma_{x1}^{2}=2,\sigma_{x2}^{2}=1$, anatomical coordinates follow a multivariate normal distribution with variance $\sigma_{y1}^{2}=1,\sigma_{y2}^{2}=1,\sigma_{y3}^{2}=1$.

To determine the anatomical–functional relationship in neural data, we infer the functional coordinates $x→_{i}$ of each neuron by fitting the ERM using multidimensional scaling (MDS) (Cox and Cox, 2000) (Methods). For simplicity and better visualization, we use a low-dimensional functional space where $d=2$. The fitted functional coordinates confirm the slow decay kernel function in ERM except for a small distance (Figure 5—figure supplement 3). The ERM with inferred coordinates $x→_{i}$ also reproduces the experimental covariance matrix, including cluster structures (Figure 5—figure supplement 2) and its sampling eigenspectra (Figure 5—figure supplement 1).

Equipped with the functional and anatomical coordinates, we next use CCA to determine which scenarios illustrated in Figure 5A align better with the neural data. Figure 5B, C shows a representative fish with a significant $R_{CCA}=0.327$ (p-value = 0.0042, Anderson–Darling test). Notably, the CCA vector in the anatomical space, $v→_{anat}$, aligns with the rostrocaudal axis. Coloring each neuron in the functional space by its projection along $v→_{anat}$ shows a correspondence between clustering and anatomical coordinates (Figure 5B). Similarly, coloring neurons in the anatomical space (Figure 5C) by their projection along $v→_{func}$ reveals distinct localizations in regions like the forebrain and optic tectum. Across animals, functionally clustered neurons show anatomical segregation (Chen et al., 2018), with an average $R_{CCA}$ of 0.335 ± 0.054 (mean ± SD).

Next, we investigate the effects of different sampling methods (Figure 5A1) on the geometry of the neural activity space when there is a significant but moderate anatomical–functional correlation as in the experimental data. Interestingly, dimensionality $D_{PR}^{ASap}$ in data under anatomical sampling consistently falls between random and functional sampling values (Figure 5D). This phenomenon can be intuitively explained by the ERM theory. Recall that for large $N$, the key term in Equation 1 is $E_{i\neqj}(C_{ij}^{2})$. For a fixed number of sampled neurons, this average squared covariance is maximized when neurons are selected closely in the functional space (FSap) and minimized when distributed randomly (RSap). Thus, RSap and FSap $D_{PR}$ set the upper and lower bounds of dimensionality, with ASap expected to fall in between. This reasoning can be precisely formulated to obtain quantitative predictions of the bounds (Methods). We predict the ASap dimension at large $N$ as

$$
D_{PR}^{ASap}≈(1−R_{ASap}^{2}+k^{2}R_{ASap}^{2})^{\mu/d}D_{PR}.
$$

Here, $D_{PR}$ is the dimensionality under RSap (Equation 1), $k$ represents the fraction of sampled neurons. $R_{ASap}$ is the correlation between anatomical and functional coordinates along the direction where the anatomical subregions are divided (Methods), and it is bounded by the canonical correlation $R_{ASap}\leqR_{CCA}$. When $R_{ASap}=0$, we get the upper bound $D_{PR}^{ASap}=D_{PR}$ (Figure 5D, dashed line). The lower bound is reached when $R_{ASap}=R_{CCA}=1$ (Figure 5A4), where Equation 4 shows a scaling relationship $D_{PR}^{ASap}=D_{PR}^{FSap}∼k^{2\mu/d}D_{PR}$ that depends on the sampling fraction $k$ (Figure 5D, solid line). This contrasts with the $k$-independent dimensionality of RSap in Equation 1. Furthermore, if $R_{ASap}$ and its upper bound is not close to 1 (precisely $R_{ASap}\leq0.84$ for the ERM model in Figure 5D), $D_{PR}^{ASap}$ align closer to the upper bound of RSap. This prediction agrees well with our observations in data across animals (Figure 5D, Figure 5—figure supplement 6, and Figure 5—figure supplement 7).

Beyond dimensionality, our theory predicts the difference in the covariance spectrum between sampling methods based on the neuronal density ρ in the functional space (Equation 3). This density ρ remains constant during FSap (Figure 5A1) and decreases under RSap; the average density across anatomical regions $⟨ρ⟩$ in ASap lies between those of FSap and RSap. Analogous to Equation 4, the relationship in ρ orders the spectra: ASap’s spectrum lies between those of FSap and RSap (Methods). This further implies that the level of scale invariance under ASap should fall between that of RSap and FSap, which is confirmed by our experimental data (Figure 5E).

## Discussion

### Impact of hunting behavior on scale invariance and functional space organization

How does task-related neural activity shape the covariance spectrum and brain-wide functional organization? We examine the hunting behavior in larval zebrafish, marked by eye convergence (both eyes move inward to focus on the central visual field) (Bianco et al., 2011). We find that scale invariance of the eigenspectra persists and is enhanced even after removing the hunting frames from the Ca2+ imaging data (Figure 4C, Appendix 1—figure 7A, B, Appendix 1). This is consistent with the scale-invariant spectrum found in other datasets during spontaneous behaviors (Figure 5—figure supplement 1F, Figure 2—figure supplement 2G, H), suggesting scale invariance is a general phenomenon.

Interestingly, in the inferred functional space, we observe reorganizations of neurons after removing hunting behavior (Appendix 1—figure 7C, D). Neurons in one cluster disperse from their center of mass (Appendix 1—figure 7D) and decreases the local neuronal density ρ (Appendix 1 and Appendix 1—figure 7E). The neurons in this dispersed cluster have a consistent anatomical distribution from the midbrain to the hindbrain in four out of five fish (Appendix 1—figure 9). During hunting, the cluster has robust activations that are widespread in the anatomical space but localized in the functional space (Appendix 1, Appendix 1—Video 1).

Our findings suggest that the functional space could be defined by latent variables that represent cognitive factors such as decision-making, memory, and attention. These variables set the space’s dimensions, with neural activity patterns reflecting cognitive state dynamics. Functionally related neurons – through sensory tuning, movement parameters, internal conditions, or cognitive factors – become closer in this space, leading to stronger activity correlations.

### Criticality and power law

What drives brain dynamics with a slow-decaying distance–correlation function $f(x→)$ in functional space? Long-range connections and a slow decline in projection strength over distance (Kunst et al., 2019) may cause extensive correlations, enhancing global activity patterns. This behavior is also reminiscent of phase transitions in statistical mechanics (Kardar, 2007), where local interactions lead to expansive correlated behaviors. Studies suggest that critical brains optimize information processing (Beggs and Plenz, 2003; Dahmen et al., 2019). The link between neural correlation structures and neuronal connectivity topology is an exciting area for future exploration.

In the high-density regime of the ERM model, the rank plot (Equation 3) for large eigenvalues ($\lambda>1$) follows a power law $\lambda∼r^{−\alpha}$, with $\alpha=1−\mu/d<1$. The scale-invariant spectrum occurs when α is close to 1. Experimental data, however, align more closely with the model in the intermediate-density regime, where the power-law spectrum is an approximation and the decay is slower (for ERM model, Figure 4—figure supplement 1BC, and for data $\alpha=0.47\pm0.08$, mean ± SD, n =6 fish). Stringer et al., 2019a found an $\alpha≳1$ decay in the mouse visual cortex’s stimulus trial averaged covariance spectrum, and they argued that this decay optimizes visual code efficiency and smoothness. Our study differs in two fundamental ways. First, we recorded brain-wide activity during spontaneous or hunting behavior, calculating neural covariance from single-trial activity. Much of the neural activity was not driven by sensory stimulus and unrelated to specific tasks, requiring a different interpretation of the neural covariance spectrum. Second, without loss of generality, we normalized the mean variance of neural activity $E(\sigma^{2})$ by scaling the covariance matrix so that its eigenvalues sum up to $N$. This normalization imposes a constraint on the spectrum. In particular, large and small eigenvalues may have different behaviors and do not need to obey a single power law $\lambda∼r^{−\alpha}$ for all $N$ eigenvalues (Pospisil and Pillow, 2024) (Methods). Stringer et al., 2019a did not take this possibility into account, making their theory less applicable to our analysis.

We draw inspiration from the renormalization group (RG) approach to navigate neural covariance across scales, which has also been explored in the recent literature. Following Kadanoff’s block spin transformation (Kardar, 2007, Meshulam et al., 2019) formed size-dependent neuron clusters and their covariance matrices by iteratively pairing the most correlated neurons and placing them adjacent on a lattice. The groups expanded until the largest reached the system size. The RG process, akin to spatial sampling in functional space (FSap), maintains constant neuron density ρ. Thus, for any kernel function $f(x→)$, including the power law and exponential, the covariance eigenspectrum remains invariant across scales (Appendix 1—figure 5A, B, D, E).

Morrell et al., 2024; Morrell et al., 2021 proposed a simple model in which a few time-varying latent factors impact the whole neural population. We evaluated if this model could account for the scale invariance seen in our data. Simulations showed that the resulting eigenspectra differed considerably from our findings (Appendix 1—figure 6). Although the Morrell model demonstrated a degree of scale invariance under functional sampling (or RG), it did not align with the scale-invariant features under random sampling, suggesting that this simple model might not capture all crucial features in our observations.

We emphasize that the covariance spectrum being a power law is distinct from the scale invariance we define in this study, namely the collapse of spectrum curves under random neuron sampling. The random RNN model in Figure 2I shows a power-law behavior, but lacks true scale invariance as spectrum curves for different sizes do not collapse. When connection strength $g$ approaches 1, the system exhibits a power-law spectrum of $\lambda∝(\frac{r}{N})^{−\frac{3}{2}}$. Subsampling causes the spectrum to shift by $\lambda∝k^{−\frac{1}{2}}(\frac{r}{N})^{−\frac{3}{2}}$, where $k=N_{s}/N$ is the sampling fraction (derived from Equation 24 in Hu and Sompolinsky, 2022).

### Bounded dimensionality under random sampling

The saturation of the dimensionality $D_{PR}$ at large sample sizes indicates a limit to neural assembly complexity, evidenced by the finite mean square covariance. This is in contrast with neural dynamics models such as the balanced excitatory–inhibitory (E–I) neural network (Renart et al., 2010), where $E_{i\neqj}(C_{ij}^{2})∼1/N$ resulting in an unbounded dimensionality (see Appendix 2). Our results suggest that the brain encodes experiences, sensations, and thoughts using a finite set of dimensions instead of an infinitely complex neural activity space.

We found that the relationship between dimensionality and the number of recorded neurons depends on the sampling method. For functional sampling, the dimensionality scales with the sampling fraction $k:D_{PR}^{FSap}∼k^{2\mu/d}D_{PR}$. This suggests that if anatomically sampled neurons are functionally clustered, as with cortical neurons forming functional maps, the increase in dimensionality with neuron number may seem unbounded. This offers new insights for interpreting large-scale neural activity data recorded under various techniques.

Manley et al., 2024 found that, unlike in our study, neural activity dimensionality in head-fixed, spontaneously behaving mice did not saturate. They used shared variance component analysis (SVCA) and noted that PCA-based estimates often show dimensionality saturation, which is consistent with our findings. We intentionally chose PCA in our study for several reasons. First, PCA is a trusted and widely used method in neuroscience, proven to uncover meaningful patterns in neural data. Second, its mathematical properties are well understood, making it particularly suitable for our theoretical analysis. Although newer methods such as SVCA might offer valuable insights, we believe PCA remains the most appropriate method for our research questions.

It is important to note that the scale invariance of dimensionality and covariance spectrum are distinct phenomena with different underlying requirements. Dimensionality invariance relies on finite mean square covariance, causing saturation at large sample sizes. In contrast, spectral invariance requires a slow-decaying correlation kernel (small $\mu$) and/or a high-dimensional functional space (large $d$). Although both features appear in our data, they result from distinct mechanisms. A neural system could show saturating dimensionality without spectral invariance if it has finite mean square covariance but rapidly decaying correlations with functional distance. Understanding these requirements clarifies how neural organization affects different scale-invariant properties.

### Computational benefits of a scale-invariant covariance spectrum

Our findings are validated across multiple datasets obtained through various recording techniques and animal models, ranging from single-neuron calcium imaging in larval zebrafish to single-neuron multi-electrode recordings in the mouse brain (see Figure 2—figure supplement 2). The conclusion remains robust when the multi-electrode recording data are reanalyzed under different sampling rates (6–24 Hz, Figure 2—figure supplement 4). We also confirm that substituting a few negative covariances with zero retains the spectrum of the data covariance matrix (Figure 2—figure supplement 3 and Methods).

The scale invariance of neural activity across different neuron assembly sizes could support efficient multiscale information encoding and processing. This indicates that the neural code is robust and requires minimal adjustments despite changes in population size. One recent study shows that randomly sampled and coarse-grained macrovoxels can predict population neural activity (Hoffmann et al., 2023), reinforcing that a random neuron subset may capture overall activity patterns. This enables downstream circuits to readout and process information through random projections (Gao et al., 2017). A recent study demonstrates that a scale-invariant noise covariance spectrum with a specific slope $\alpha<1$ enables neurons to convey unlimited stimulus information as the population size increases (Moosavi et al., 2024). The linear Fisher information, in this context, grows at least as $N^{1−\alpha}$.

Understanding how dimensionality and spectrum change with sample size also suggests the possibility of extrapolating from small samples to overcome experimental limitations. This is particularly feasible when $\mu/d→0$, where the dimensionality and spectrum under anatomical, random, and functional sampling coincide (Equations 3 and 4). Developing extrapolation methods and exploring the benefits of scale-invariant neural code are promising future research directions.

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
      <td>Strain, strain background (Danio rerio)</td>
      <td>Tg(elavl3: H2B- GCaMP6f)</td>
      <td>https://doi.org/10.7554/eLife.12741</td>
      <td></td>
      <td>Jiu-Lin Du, Institute of Neuroscience, Chinese Academy of Sciences, Shanghai</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>julia1.7</td>
      <td>https://julialang.org/</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MATLAB</td>
      <td>https://ww2.mathworks.cn/</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Mathematica</td>
      <td>https://www.wolfram.com/mathematica/</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

### Experimental methods

The handling and care of the zebrafish complied with the guidelines and regulations of the Animal Resources Center of the University of Science and Technology of China (USTC). All larval zebrafish (huc:h2b -GCaMP6f Cong et al., 2017) were raised in E2 embryo medium (comprising 7.5 mM NaCl, 0.25 mM KCl, 0.5 mM MgSO4, 0.075 mM KH2PO4, 0.025 mM Na2HPO4, 0.5 mM CaCl2, and 0.35 mM NaHCO3; containing 0.5 mg/l methylene blue) at 28.5°C and with a 14-hr light and 10-hr dark cycle.

To induce hunting behavior (composed of motor sequences like eye convergence and J turn) in larval zebrafish, we fed them a large amount of paramecia over a period of 4–5 days post-fertilization (dpf). The animals were then subjected to a 24-hr starvation period, after which they were transferred to a specialized experimental chamber. The experimental chamber was 20 mm in diameter and 1 mm in depth, and the head of each zebrafish was immobilized by applying 2% low melting point agarose. The careful removal of the agarose from the eyes and tail of the fish ensured that these body regions remained free to move during hunting behavior. Thus, characteristic behavioral features such as J-turns and eye convergence could be observed and analyzed. Subsequently, the zebrafish were transferred to an incubator and stayed overnight. At 7 dpf, several paramecia were introduced in front of the previously immobilized animals, each of which was monitored by a stereomicroscope. Those displaying binocular convergence were selected for subsequent Ca2+ imaging experiments.

We developed a novel optomagnetic system that allows (1) precise control of the trajectory of the paramecium and (2) imaging brain-wide Ca2+ activity during the hunting behavior of zebrafish. To control the movement of the paramecium, we treated these microorganisms with a suspension of ferric tetroxide for 30 min and selected those that responded to its magnetic attraction. A magnetic paramecium was then placed in front of a selected larva, and its movement was controlled by changing the magnetic field generated by Helmholtz coils that were integrated into the imaging system. The real-time position of the paramecium, captured by an infrared camera, was identified by online image processing. The positional vector relative to a predetermined target position was calculated. The magnitude and direction of the current in the Helmholtz coils were adjusted accordingly, allowing for precise control of the magnetic field and hence the movement of the paramecium. Multiple target positions could be set to drive the paramecium back and forth between multiple locations.

The experimental setup consisted of head-fixed larval zebrafish undergoing two different types of behavior: induced hunting behavior by a moving paramecium in front of a fish (fish 1–5), and spontaneous behavior without any visual stimulus as a control (fish 6). Experiments were carried out at ambient temperature (ranging from 23 to 25°C). The behavior of the zebrafish was monitored by a high-speed infrared camera (Basler acA2000-165umNIR, 0.66×) behind a 4F optical system and recorded at 50 Hz. Brain-wide Ca2+ imaging was achieved using XLFM. Light-field images were acquired at 10 Hz, using customized LabVIEW software (National Instruments, USA) or Solis software (Oxford Instruments, UK), with the help of a high-speed data acquisition card (PCIe-6321, National Instruments, USA) to synchronize the fluorescence with behavioral imaging.

#### Behavior analysis

The background of each behavior video was removed using the clone stamp tool in Adobe Photoshop CS6. Individual images were then processed by an adaptive thresholding algorithm, and fish head and yolk were selected manually to determine the head orientation. The entire body centerline, extending from head to tail, was divided into 20 segments. The amplitude of a bending segment was defined as the angle between the segment and the head orientation. To identify the paramecium in a noisy environment, we subtracted a background image, averaged over a time window of 100 s, from all the frames. The major axis of the left or right eye was identified using DeepLabCut (Mathis et al., 2018). The eye orientation was defined as the angle between the rostrocaudal axis and the major axis of an eye. The convergence angle was defined as the angle between the major axes of the left and right eyes. An eye-convergence event was defined as a period of time where the angle between the long axis of the eyes stayed above 50° (Bianco et al., 2011).

#### Imaging data acquisition and processing

We used a fast eXtended light-field microscope (XLFM, with a volume rate of 10 Hz) to record Ca2+ activity throughout the brain of head-fixed larval zebrafish. Fish were ordered by the dates of experiments. As previously described (Cong et al., 2017), we adopted the Richardson–Lucy deconvolution method to iteratively reconstruct 3D fluorescence stacks (600 × 600 × 250) from the acquired 2D images (2048 × 2048). This algorithm requires an experimentally measured point spread function of the XLFM system. The entire recording for each fish is 15.3 ± 4.3 min (mean ± SD).

To perform image registration and segmentation, we first cropped and resized the original image stack to 400 × 308 × 210, which corresponded to the size of a standard zebrafish brain (zbb) atlas (Tabor et al., 2019). This step aimed to reduce substantial memory requirements and computational costs in subsequent operations. Next, we picked a typical volume frame and aligned it with the zbb atlas using a basic 3D affine transformation. This transformed frame was used as a template. We aligned each volume with the template using rigid 3D intensity-based registration (Studholme et al., 1997) and non-rigid pairwise registration (Rueckert et al., 1999) in the Computational Morphometry Toolkit (CMTK) (https://www.nitrc.org/projects/cmtk/). After voxel registration, we computed the pairwise correlation between nearby voxel intensities and performed the watershed algorithm on the correlation map to cluster and segment voxels into consistent ROIs across all volumes. We defined the diameter of each ROI using the maximum Feret diameter (the longest distance between any two voxels within a single ROI).

Finally, we adopted the ‘OASIS’ deconvolution method to denoise and infer neural activity from the fluorescence time sequence (Friedrich et al., 2017). The deconvolved $ΔF/F$ of each ROI was used to infer firing rates for subsequent analysis.

### Other experimental datasets analyzed

To validate our findings across different recording methods and animal models, we also analyzed three additional datasets (Table 2). We include a brief description below for completeness. Further details can be found in the respective reference. The first dataset includes whole-brain light-sheet Ca2+ imaging of immobilized larval zebrafish in the presence of visual stimuli as well as in a spontaneous state (Chen et al., 2018). Each volume of the brain was scanned through 2.11 ± 0.21 planes per second, providing a near-simultaneous readout of neuronal Ca2+ signals. We analyzed fish 8 (69,207 neurons × 7890 frames), 9 (79,704 neurons × 7720 frames), and 11 (101,729 neurons × 8528 frames), which are the first three fish data with more than 7200 frames. For simplicity, we labeled them l2, l3, and l1(fl). The second dataset consists of Neuropixels recordings from approximately ten different brain areas in mice during spontaneous behavior (Stringer et al., 2019b). Data from the three mice, Kerbs, Robbins, and Waksman, include the firing rate matrices of 1462 neurons × 39,053 frames, 2296 neurons × 66,409 frames, and 2688 neurons × 74,368 frames, respectively. The last dataset comprises two-photon Ca2+ imaging data (2–3 Hz) obtained from the visual cortex of mice during spontaneous behavior. While this dataset includes numerous animals, we focused on the first three animals that exhibited spontaneous behavior. While this dataset includes numerous animals, we focused on the first three animals that exhibited spontaneous behavior:spont_M150824_MP019_2016-04-05 (11,983 neurons × 21,055 frames), spont_M160825_MP027_2016-12-12 (11,624 neurons × 23,259 frames), and spont_M160907_MP028_2016-09-26 (9392 neurons × 10,301 frames) (Stringer et al., 2019b).

**Table 2.**
 Resources for additional experimental datasets.


<table>
  <thead>
    <tr>
      <th>Dataset</th>
      <th>Data reference</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Light-sheet imaging of larval zebrafish (Chen et al., 2018)</td>
      <td>https://janelia.figshare.com/articles/dataset/Whole-brain_light-sheet_imaging_data/7272617</td>
    </tr>
    <tr>
      <td>Neuropixels recordings in mice (Stringer et al., 2019b)</td>
      <td>https://janelia.figshare.com/articles/dataset/Eight-probe_Neuropixels_recordings_during_spontaneous_behaviors/7739750</td>
    </tr>
    <tr>
      <td>Two-photon imaging in mice (Stringer et al., 2019b)</td>
      <td>https://janelia.figshare.com/articles/dataset/Recordings_of_ten_thousand_neurons_in_visual_cortex_during_spontaneous_behaviors/6163622</td>
    </tr>
  </tbody>
</table>

### Covariance matrix, eigenspectrum, and sampling procedures

To begin, we multiplied the inferred firing rate of each neuron (see Methods) by a constant such that in the resulting activity trace $a_{i}$, the mean of $a_{i}(t)$ over the nonzero time frames equaled one (Meshulam et al., 2019). Consistent with the literature (Meshulam et al., 2019), this step aimed to eliminate possible confounding factors in the raw activity traces, such as the heterogeneous expression level of the fluorescence protein within neurons and the nonlinear conversion of the electrical signal to Ca2+ concentration. Note that after this scaling, neurons could still have different activity levels characterized by the variance of $a_{i}(t)$ over time, due to differences in the sparsity of activity (proportion of nonzero frames) and the distribution of nonzero $a_{i}(t)$ values. Without normalization, the covariance matrix becomes nearly diagonal, causing significant underestimation of the covariance structures.

The three models of covariance in Figure 2G–I were constructed as follows. For model in Figure 2G, the entries of matrix $G$ (with dimensions $N\timesT$) were sampled from an i.i.d. Gaussian distribution with zero mean and standard deviation $\sigma=1$. In Figure 2H, we constructed the composite covariance matrix for fish 1 achieved by maintaining the eigenvalues from the fish 1 data covariance matrix and replacing the eigenvectors $U$ with a set of random orthonormal basis. Lastly, the covariance matrix in Figure 2I was generated from a randomly connected recurrent network of linear rate neurons. The entries in the synaptic weight matrix are normally distributed with $J_{ij}∼N(0,g^{2}/N)$, with a coupling strength  $g=0.95$ (Hu and Sompolinsky, 2022; Morales et al., 2023). For consistency, we used the same number of time frames $T=7200$ when comparing CI across all the datasets (Figures 4B, C, 5D, E, Figure 4—figure supplement 2C). For other cases, we analyzed the full length of the data (number of time frames: fish 1 – 7495, fish 2 – 9774, fish 3 – 13,904, fish 4 – 7318, fish 5 – 7200, and fish 6 – 9388). Next, the covariance matrix was calculated as $C_{ij}=\frac{1}{T−1}\sumt=1T(a_{i}(t)−a¯_{i})(a_{j}(t)−a¯_{j})$, where $a¯_{i}$ is the mean of $a_{i}(t)$ over time. Finally, to visualize covariance matrices on a common scale, we multiplied matrix C by a constant such that the average of its diagonal entries equaled one, that is, $Tr⁡(C)/N=1$. This scaling did not alter the shape of covariance eigenvalue distribution, but set the mean at 1 (see also Equation 8).

To maintain consistency across datasets, we fixed the same initial number of neurons at $N_{0}=1,024$. These $N_{0}$ neurons were randomly chosen once for each zebrafish dataset and then used throughout the subsequent analyses. We adopted this setting for all analyses except in two particular instances: (1) for comparisons among the three sampling methods (RSap, ASap, and FSap), we specifically chose 1024 neurons centered along the anterior–posterior axis, mainly from the midbrain to the anterior hindbrain regions (Figure 5DE, Figure 5—figure supplement 6). (2) When investigating the impact of hunting behavior on scale invariance, we included the entire neuronal population (Appendix 1).

We used an iterative procedure to sample the covariance matrix $C$ (calculated from data or as simulated ERMs). For RSap, in the first iteration, we randomly selected half of the neurons. The covariance matrix for these selected neurons was a $N/2\timesN/2$ diagonal block of $C$. Similarly, the covariance matrix of the unselected neurons was another diagonal block of the same size. In the next iteration, we similarly created two new sampled blocks with half the number of neurons for each of the blocks we had. Repeating this process for $n$ iterations resulted in 2n blocks, each containing $N:=N_{0}/2^{n}$ neurons. At each iteration, the eigenvalues of each block were calculated and averaged across the blocks after being sorted in descending order. Finally, the averaged eigenvalues were plotted against rank/$N$ on a log–log scale.

In the case of ASap and FSap, the process of selecting neurons was different, although the remaining procedures followed the RSap protocol. In ASap, the selection of neurons was based on a spatial criterion: neurons close to the anterior end on the anterior–posterior axis were grouped to create a diagonal block of size $\frac{N}{2}\times\frac{N}{2}$, with the remaining neurons forming a separate block. FSap, on the other hand, used the RG framework (Meshulam et al., 2019) to define the blocks (details in Appendix 1). In each iteration, the cluster of neurons within a block that showed the highest average correlation ($E_{i\neqj}(C_{ij}^{2})$) was identified and labeled as the most correlated cluster (refer to Figure 5D, Figure 5—figure supplement 6, and Figure 5—figure supplement 7).

In the ERM model, as part of implementing ASap, we generated anatomical and functional coordinates for neurons with a specified CCA properties as described in Methods. Mirroring the approach taken with our data, ASap segmented neurons into groups based on the first dimension of their anatomical coordinates, akin to the anterier–posterior axis. FSap employed the same RG procedures outlined earlier (Appendix 1).

To determine the overall power-law coefficient of the eigenspectra, α, throughout sampling, we fitted a straight line in the log–log rank plot to the large eigenvalues that combined the original and three iterations of sampled covariance matrices (selecting the top 10% eigenvalues for each matrix and excluding the first four largest ones for each matrix). We averaged the estimated α over 10 repetitions of the entire sampling procedure. $R^{2}$ of the power-law fit was computed in a similar way. To visualize the statistical structures of the original and sampled covariance matrices, the orders of the neurons (i.e., columns and rows) are determined by the following algorithm. We first construct a symmetric Toeplitz matrix $T$, with entries $T_{i,j}=t_{i−j}$ and $t_{i−j}≡t_{j−i}$. The vector $t→=[t_{0},t_{1},…,t_{N−1}]$ is equal to the mean covariance vector of each neuron calculated below. Let $c_{i}→$ be a row vector of the data covariance matrix; we identify $t→=\frac{1}{N}\sumi=1ND(c_{i}→)$, where $D(⋅)$ denotes a numerical ordering operator, namely rearranging the elements in a vector $c→$ such that $c_{0}\geqc_{1}\geq…\geqc_{N−1}$. The second step is to find a permutation matrix P such that $‖T−PCP^{T}‖_{F}$ is minimized, where $‖ ‖_{F}$ denotes the Frobenius norm. This quadratic assignment problem is solved by simulated annealing. Note that after sampling, the smaller matrix will appear different from the larger one. We need to perform the above reordering algorithm for every sampled matrix so that matrices of different sizes become similar in Figure 2E.

The composite covariance matrix with substituted eigenvectors in Figure 2H was created as described in the following steps. First, we generated a random orthogonal matrix $U_{r}$ (based on the Haar measure) for the new eigenvectors. This was achieved by QR decomposition $A=U_{r}R$ of a random matrix $A$ with i.i.d. entries $A_{ij}∼N(0,1/N)$. The composite covariance matrix $C_{r}$ was then defined as $C_{r}:=U_{r}ΛU_{r}^{T}$, where $Λ$ is a diagonal matrix that contains the eigenvalues of $C$. Note that since all the eigenvalues are real and $U_{r}$ is orthogonal, the resulting $C_{r}$ is a real and symmetric matrix. By construction, $C_{r}$ and $C$ have the same eigenvalues, but their sampled eigenspectra can differ.

### Dimensionality

In this section, we introduce the participation ratio ($D_{PR}$) as a metric for effective dimensionality of a system, based on Recanatesi et al., 2019; Litwin-Kumar et al., 2017; Gao and Ganguli, 2015; Gao et al., 2017; Clark et al., 2023; Dahmen et al., 2020. $D_{PR}$ is defined as:

$$
D_{PR}(C)=\frac{(\sumi\lambda_{i})^{2}}{\sumi\lambda_{i}^{2}}=\frac{(Tr(C))^{2}}{Tr(C^{2})}=\frac{N^{2}E(\sigma^{2})^{2}}{NE(\sigma^{4})+N(N−1)E_{i\neqj}(C_{ij}^{2})}
$$

Here, $\lambda_{i}$ are the eigenvalues of the covariance matrix $C$, representing variances of neural activities. $Tr(⋅)$ denotes the trace of the matrix. The term $E_{i\neqj}(C_{ij}^{2})$ denotes the expected value of the squared elements that lie off the main diagonal of $C$. This represents the average squared covariance between the activities of distinct pairs of neurons.

With these definitions, we explore the asymptotic behavior of $D_{PR}$ as the number of neurons $N$ approaches infinity:

$$
limN→∞D_{PR}(C)=\frac{E(\sigma^{2})^{2}}{E_{i\neqj}(C_{ij}^{2})}
$$

This limit highlights the relationship between the PR dimension and the average squared covariance among different pairs of neurons. To predict how $D_{PR}$ scales with the number of neurons (Figure 2D), we first estimated these statistical quantities ($E_{i\neqj}(C_{ij}^{2})$, $E(\sigma^{2})$, and $E(\sigma^{4})$) using all available neurons, then applied Equation 5 for different values of $N$. It is worth mentioning that a similar theoretical finding is established by Dahmen et al., 2020. The transition from increasing $D_{PR}$ with $N$ to approaching the saturation point occurs when $N$ is significantly larger than $D_{PR}$.

### ERM model

We consider the eigenvalue distribution or spectrum of the matrix $C$ at the limit of $N≫1$ and $L≫1$. This spectrum can be analytically calculated in both high- and intermediate-density scenarios using the replica method (Mézard et al., 1999). The following sketch shows our approach, and detailed derivations can be found in Appendix 2. To calculate the probability density function of the eigenvalues (or eigendensity), we first compute the resolvent or Stieltjes transform $g(z)=−\frac{2}{N}∂_{z}⟨ln⁡ det(zI−C)^{−1/2}⟩$, $z\inC$. Here, $⟨…⟩$ is the average across the realizations of $C$ (i.e., random $x→_{i}$’ s and $\sigma_{i}^{2}$’ s). The relationship between the resolvent and the eigendensity is given by the Sokhotski–Plemelj formula:

$$
p(\lambda)=−\frac{1}{\pi}limη→0^{+}Img(\lambda+iη),
$$

where $Im$ means imaginary part.

Here we follow the field-theoretic approach (Mézard et al., 1999), which turns the problem of calculating the resolvent to a calculation of the partition function in statistical physics by using the replica method. In the limit $N→∞$, $L^{d}→∞$, ρ being finite, by performing a leading order expansion of the canonical partition function at large $z$ (Appendix 2), we find the resolvent is given by

$$
g(z)=\frac{1}{ρ}\int\frac{d^{d}k→}{(2\pi)^{d}}\frac{1}{z−ρE(\sigma^{2})f~(k→)}
$$

In the high-density regime, the probability density function (pdf) of the covariance eigenvalues can be approximated and expressed from Equations 6 and 7 using the Fourier transform of the kernel function $f~(k→)$:

$$
p(\lambda)=\frac{1}{ρE(\sigma^{2})}\int_{R^{d}}\frac{d^{d}k→}{(2\pi)^{d}}\delta(\frac{\lambda}{E(\sigma^{2})}−ρf~(k→)),
$$

where $\delta(x)$ is the Dirac delta function and $E(\sigma^{2})$ is the expected value of the variances of neural activity. Intuitively, Equation 8 means that $\lambda/ρ$ are distributed with a density proportional to the area of $f~(k→)$’ level sets (i.e., isosurfaces).

In Results, we found that the covariance matrix consistently shows greater scale invariance compared to the correlation matrix across all datasets. This suggests that the variability in neuronal activity significantly influences the eigenspectrum. This finding, however, cannot be explained by the high-density theory, which predicts that the eigenspectrum of the covariance matrix is simply a rescaling of the correlation eigenspectrum by $E(\sigma_{i}^{2})$, the expected value of the variances of neural activity. Without loss of generality, we can always standardize the fluctuation level of neural activity by setting $E(\sigma^{2})=1$. This is equivalent to multiplying the covariance matrix $C$ by a constant such that $Tr⁡(C)/N=1$, which in turn scales all the eigenvalues of $C$ by the same factor. Consequently, the heterogeneity of $\sigma_{i}^{2}$ has no effect on the scale invariance of the eigenspectrum (see Equation 8). This theoretical prediction is indeed correct and is confirmed by direct numerical simulations and quantifying the scale invariance using the CI (Figure 4—figure supplement 2A).

Fortunately, the inconsistency between theory and experimental results can be resolved by focusing the ERM within the intermediate density regime $ρϵ^{d}≪1$, where neurons are positioned at a moderate distance from each other. As mentioned above, we set $E(\sigma^{2})=1$ in our model and vary the diversity of activity fluctuations among neurons represented by $E(\sigma^{4})$. Consistent with the experimental observations, we find that the CI decreases with $E(\sigma^{4})$ (see Figure 4—figure supplement 2B). This agreement indicates that the neural data are better explained by the ERM in the intermediate density regime.

To gain a deeper understanding of this behavior, we use the Gaussian variational method (Mézard et al., 1999) to calculate the eigenspectrum. Unlike the high-density theory where the eigendensity has an explicit expression, in the intermediate density the resolvent $g(z)$ no longer has an explicit expression and is given by the following equation:

$$
g(z)=⟨\frac{1}{z−\sigma^{2}\intDk→G~(k→,z)}⟩_{\sigma},
$$

where $⟨…⟩_{\sigma}$ computes the expectation value of the term within the bracket with respect to σ, namely $⟨…⟩_{\sigma}≡\int…p(\sigma)d\sigma$. Here and in the following, we denote $\intDk→≡\int\frac{d^{d}k→}{(2\pi)^{d}}$. The function $G(k→,z)$ is determined by a self-consistent equation,

$$
\frac{1}{f~(k→)}=\frac{1}{G~(k→,z)}+⟨\frac{ρ\sigma^{2}}{z−\sigma^{2}\intDk→G~(k→,z)}⟩_{\sigma}
$$

We can solve $\intDk→G(k→,z)$ from Equation 10 numerically and below is an outline, and the details are explained in Appendix 2. Let us define the integral $G≡\intDk→G~(k→,z)$. First, we substitute $z≡\lambda+iη$ into Equation 10 and write $G=ReG+iImG$. Equation 10 can thus be decomposed into its real part and imaginary part, and a set of nonlinear and integral equations, each of which involves both $ReG$ and $ImG$. We solve these equations at the limit $η→0$ using a fixed-point iteration that alternates between updating $ReG$ and $ImG$ until convergence.

We find that the variational approximations exhibit excellent agreement with the numerical simulation for both large and intermediate ρ where the high-density theory starts to deviate significantly (for $ρ=256$ and $ρ=10.24$, $ϵ=0.03125$, Figure 4—figure supplement 1). Note that the departure of the leading eigenvalues in these plots is expected, since the power-law kernel function we use is not integrable (see Methods).

To elucidate the connection between the two different methods, we estimate the condition when the result of the high-density theory (Equation 8) matches that of the variational method (Equations 9 and 10; Appendix 2). The transition between these two density regimes can also be understood (see Equation 22 and Appendix 2).

Importantly, the scale invariance of the spectrum at $\mu/d→0$ previously derived using the high-density result (Equation 3) can be extended to the intermediate-density regime by proving the ρ-independence using the variational method (Appendix 2).

Finally, using the variational method and the integration limit estimated by simulation (see Methods), we show that the heterogeneity of the variance of neural activity, quantified by $E(\sigma^{4})$, indeed improves the collapse of the eigenspectra for intermediate ρ (Appendix 2). Our theoretical results agree excellently with the ERM simulation (Figure 4—figure supplement 2A, B).

### Kernel function

Throughout the paper, we have mainly considered a particular approximate power-law kernel function inspired by the Student’s t distribution

$$
f(x→)=ϵ^{\mu}(ϵ^{2}+‖x→‖^{2})^{−\mu/2}.
$$

To understand how to choose $ϵ$ and $\mu$, see Methods. Variations of Equation 11 near $x=0$ have also been explored; see a summary in Table 3.

**Table 3.**
 Modifications of the shape of $f(x→)$ near $‖x→‖=0$ used in Appendix 1—figures 1–3.Flat: when $‖x→‖<ϵ$, $f(x→)=1$. Tangent: when $‖x→‖<cϵ$, $f(x→)$ follows a tangent line of the exact power law ($b‖x→‖+1$ and $\frac{ϵ^{\mu}}{‖x→‖^{\mu}}$ have a same first-order derivative when $‖x→‖=cϵ$). b and c are constants. Tent: when $‖x→‖<cϵ$, $f(x→)$ follows a straight line while the slope is not the same as the tangent case. Parabola: when $‖x→‖<cϵ$, $f(x→)$ follows a quadratic function ($ax^{2}+1$ and $\frac{ϵ^{\mu}}{‖x→‖^{\mu}}$ have same first-order derivative). t pdf: mimic the smoothing treatment like the t distribution. All the constant parameters are set such that $f(0)=1$.


<table>
  <thead>
    <tr>
      <th>f(x→)\begin{document}$f(\vec x)$\end{document}</th>
      <th>Definition</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Flat</td>
      <td>f(x→)={1,‖x→‖&lt;ϵeμ‖x→‖μ,‖x→‖≥ϵ\begin{document}$f \left(\vec x\right) =\left\{\begin{array}{cl} 1, &amp; \|\vec{x}\|&lt;\epsilon \\ \frac{e^\mu}{\|\vec{x}\|^\mu}, &amp; \|\vec{x}\| \geq \epsilon \end{array}\right.$\end{document}</td>
    </tr>
    <tr>
      <td>Tangent</td>
      <td>f(x→)={b‖x→‖+1,‖x→‖&lt;cϵ,f′(cϵ)=beμ‖x→‖μ,‖x→‖≥cϵ\begin{document}$f \left(\vec x\right) =\left\{\begin{array}{cc} b\|\vec{x}\|+1, &amp; \|\vec{x}\|&lt;c \epsilon, f^{\prime}(c \epsilon)=b \\ \frac{e^\mu}{\|\vec{x}\|^\mu}, &amp; \|\vec{x}\| \geq c \epsilon \end{array}\right.$\end{document}</td>
    </tr>
    <tr>
      <td>Tent</td>
      <td>f(x→)={b‖x→‖+1,‖x→‖&lt;cϵ,f′(cϵ)≠beμ‖x→‖μ,‖x→‖≥cϵ\begin{document}$f\left(\vec x\right) =\left\{\begin{array}{ll} b\|\vec{x}\|+1, &amp;\|\vec{x}\|&lt;c \epsilon, f^{\prime}(c \epsilon) \neq b \\ \frac{e^\mu}{\|\vec{x}\|^\mu}, &amp; \|\vec{x}\| \geq c \epsilon \end{array}\right. $\end{document}</td>
    </tr>
    <tr>
      <td>Parabola</td>
      <td>f(x→)={b‖x→‖2+1,‖x→‖&lt;cϵ,f′(cϵ)=2bcϵeμ‖x→‖μ,‖x→‖≥cϵ\begin{document}$f\left(\vec{x}\right) =\left\{\begin{array}{ll} b\|\vec{x}\|^2+1, &amp; \|\vec{x}\|&lt;c \epsilon , f^{\prime}(c \epsilon)=2 b c \epsilon \\ \frac{e^\mu}{\|\vec{x}\|^\mu}, &amp; \|\vec{x}\| \geq c \epsilon \end{array}\right.$\end{document}</td>
    </tr>
    <tr>
      <td>t pdf</td>
      <td>f(x→)=εμ(ε2+‖x→‖2)−μ/2\begin{document}$f(\vec x)=\varepsilon ^\mu(\varepsilon ^2+\|\vec x\|^2)^{-\mu/2}$\end{document}</td>
    </tr>
  </tbody>
</table>

It is worth mentioning that a power law is not the only slow-decaying function that can produce a scale-invariant covariance spectrum (Figure 3—figure supplement 2). We choose it for its analytical tractability in calculating the eigenspectrum. Importantly, we find numerically that the two contributing factors to scale invariance – namely, slow spatial decay and higher functional space – can be generalized to other nonpower-law functions. An example is the stretched exponential function $f(x→)=e^{−‖x→‖^{η}}$ with $0<η<1$. When $η$ is small and $d$ is large, the covariance eigenspectra also display a similar collapse upon random sampling (Figure 3—figure supplement 2).

This approximate power-law $f(x→)$ has the advantage of having an analytical expression for its Fourier transform, which is crucial for the high-density theory (Equation 8),

$$
f(k→)=\frac{2^{\frac{d−\mu+2}{2}}\pi^{\frac{d}{2}}k^{\frac{\mu−d}{2}}ϵ^{\frac{\mu+d}{2}}K_{(d−\mu)/2}(kϵ)}{Γ(\mu/2)},k=‖k→‖
$$

Here, $K_{\alpha}(x)$ is the modified Bessel function of the second kind, and $Γ(x)$ is the Gamma function. We calculated the above formulas analytically for $d=1,2,3$ with the assistance of Mathematica and conjectured the case for general dimension $d$, which we confirmed numerically for $d\leq10$.

We want to explain two technical points relevant to the interpretation of our numerical results and the choice of $f(x→)$. Unlike the case in the usual ERM, here we allow $f(x→)$ to be non-integrable (over $R^{d}$), which is crucial to allow power law $f(x→)$. The nonintegrability violates a condition in the classical convergence results of the ERM spectrum (Bordenave, 2008) as $N→∞$. We believe that this is exactly the reason for the departure of the first few eigenvalues from our theoretical spectrum (e.g., in Figure 3). Our hypothesis is also supported by ERM simulations with integrable $f(x→)$ (Figure 3—figure supplement 1), where the numerical eigenspectrum matches closely with our theoretical one, including the leading eigenvalues. For ERM to be a legitimate model for covariance matrices, we need to ensure that the resulting matrix $C$ is positive semidefinite. According to the Bochner theorem (Rudin, 1990), this is equivalent to the Fourier transform (FT) of the kernel function $f~(k→)$ being nonnegative for all frequencies. For example, in 1D, a rectangle function $rect⁡(x)={1,if|x|\leq\frac{1}{2}0,otherwise$ does not meet the condition (its FT is $sinc(x)=\frac{sin⁡(x)}{x}$), but a tent function $tent⁡(x)={1−|x|, if |x|\leq10,otherwise$ does (its FT is $sinc^{2}(x)$). For the particular kernel function $f(x→)$ in Equation 11, this condition can be easily verified using the analytical expressions of its Fourier transform (Equation 12). The integral expression for $K_{\alpha}(x)$, given as $K_{\alpha}(x)=\int_{0}^{∞}e^{−xcosh⁡t}cosh⁡(\alphat)dt$, shows that $K_{\alpha}(x)$ is positive for all $x>0$. Likewise, the Gamma function $Γ(x)>0$. Therefore, the Fourier transform of Equation 11 is positive and the resulting matrix $C$ (of any size and values of $x→_{i}$) is guaranteed to be positive definite.

Building upon the theory outlined above, numerical simulations further validated the empirical robustness of our ERM model, as showcased in Figures 3B–D–4A. In Figure 3B–D, the ERM was characterized by the parameters $N=1024$, $d=2$, $L=10$, $ρ=10.24$, and $\mu=0.5$ and $ϵ=0.03125$ for $f(x→)$. To numerically compute the eigenvalue probability density function, we generated the ERM 100 times, each sampled using the method described in Methods. The pdf was computed by calculating the pdf of each ERM realization and averaging these across the instances. The curves in Figure 3D showed the average of over 100 ERM simulations. The shaded area (most of which is smaller than the marker size) represented the SEM. For Figure 4A, the columns from left to right were corresponded to $\mu=0.5,0.9,1.3$,  and the rows from top to bottom were corresponded to $d=1,2,3$. Other ERM simulation parameters: $N=4096$, $ρ=256$, $L=(N/ρ)^{1/d}$, $ϵ=0.03125$, and $\sigma_{i}^{2}=1$. It should be noted that for Figure 4A, the presented data pertain to a single ERM realization.

### Collapse index

We quantify the extent of scale invariance using CI defined as the area between two spectrum curves (Figure 4A, upper right), providing an intuitive measure of the shift of the eigenspectrum when varying the number of sampled neurons. We chose the CI over other measures of distance between distributions for several reasons. First, it directly quantifies the shift of the eigenspectrum, providing a clear and interpretable measure of scale invariance. Second, unlike methods that rely on estimating the full distribution, the CI avoids potential inaccuracies in estimating the probability of the top leading eigenvalues. Finally, the use of CI is motivated by theoretical considerations, namely the ERM in the high-density regime, which provides an analytical expression for the covariance spectrum (Equation 3) valid for large eigenvalues.

$$
CI:=\frac{1}{log⁡(q_{0}/q_{1})}\int_{log⁡q_{1}}^{log⁡q_{0}}|\frac{∂log⁡\lambda(q)}{∂log⁡ρ}|dlog⁡q,
$$

we set $q_{1}$ such that $\lambda(q_{1})=1$, which is the mean of the eigenvalues of a normalized covariance matrix. The other integration limit $q_{0}$ is set to 0.01 such that $\lambda(q_{0})$ is the 1% largest eigenvalue.

Here, we provide numerical details on calculating CI for the ERM simulations and experimental data.

#### A calculation of CI for experimental datasets/ERM model

To calculate CI for a covariance matrix $C$ of size $N_{0}$, we first computed its eigenvalues $\lambda_{i}^{0}$ and those of the sampled block $C_{s}$ of size $N_{s}=N_{0}/2$, denoted as $\lambda_{i}^{s}$ (averaged over 20 times for the ERM simulation and 2000 times in experimental data). Next, we estimated $log⁡\lambda(q)$ using the eigenvalues of $C_{0}$ and $C_{s}$ at $q=i/N_{s}$, $i=1,2,…,N_{s}$. For the sampled $C_{s}$, we simply had $log⁡\lambda(q=i/N_{s})=log⁡\lambda_{i}^{s}$, its ith largest eigenvalue. For the original $C_{0}$, $log⁡\lambda(q=i/N_{s})$ was estimated by a linear interpolation, on the $log⁡\lambda−log⁡q$ scale, using the value of $log⁡\lambda(q)$ in the nearest neighboring $q=i/N_{0}$’s (which again are simply $log⁡\lambda_{i}^{0}$). Finally, the integral (Equation 13) was computed using the trapezoidal rule, discretized at $q=i/N_{s}$’s, using the finite difference $\frac{∂log⁡\lambda(q)}{∂log⁡ρ}≈\frac{1}{log⁡(N_{0}/N_{s})}|Δlog⁡\lambda(q)|$, where $Δ$ denotes the difference between the original eigenvalues of $C_{0}$ and those of sampled $C_{s}$.

#### Estimating CI using the variational method

In the definition of CI (Equation 13), calculating $\lambda(q)$ and $\frac{∂log⁡\lambda(q)}{∂log⁡ρ}$ directly using the variational method is difficult, but we can make use of an implicit differentiation

$$
\frac{∂log⁡\lambda(q,ρ)}{∂log⁡ρ}=\frac{ρ}{\lambda}\frac{∂\lambda(q,ρ)}{∂ρ}=−\frac{ρ}{\lambda}\frac{\frac{∂q(ρ,\lambda)}{∂ρ}}{\frac{∂q(ρ,\lambda)}{∂\lambda}},
$$

where $q(\lambda):=\int_{\lambda}^{∞}p(\lambda)d\lambda$ is the complementary cdf (the inverse function of $\lambda(q)$ in Methods). Using this, the integral in CI (Equation 13) can be rewritten as

$$
\int_{log⁡q_{1}}^{log⁡q_{0}}|\frac{∂log⁡\lambda(q,ρ)}{∂log⁡ρ}|dlog⁡q=\int_{q_{1}}^{q_{0}}|−\frac{ρ}{q\lambda}\frac{\frac{∂q}{∂ρ}}{\frac{∂q}{∂\lambda}}|dq=\int_{\lambda(q_{1})}^{\lambda(q_{0})}|−\frac{ρ}{q\lambda}\frac{\frac{∂q}{∂ρ}y}{\frac{∂q}{∂\lambda}}|\frac{∂q}{∂\lambda}d\lambda=\int_{\lambda(q_{0})}^{\lambda(q_{1})}|\frac{1}{\lambda}\frac{∂log⁡q}{∂log⁡ρ}|d\lambda.
$$

Since $\frac{∂q}{∂\lambda}=−p(\lambda)<0$, we switch the order of the integration interval in the final expression of Equation 15.

First, we explain how to compute the complementary cdf $q(\lambda)$ numerically using the variational method. The key is to integrate the probability density function $p(\lambda)$ from λ to a finite $\lambda(q_{s})$ rather than to infinity,

$$
q(\lambda)=\int_{\lambda}^{∞}p(\lambda)d\lambda=\int_{\lambda(q_{s})}^{∞}p(\lambda)d\lambda+\int_{\lambda}^{\lambda(q_{s})}p(\lambda)d\lambda=q_{s}+\int_{\lambda}^{\lambda(q_{s})}p(\lambda)d\lambda.
$$

The integration limit $\lambda(q_{s})$ cannot be calculated directly using the variational method. We thus used the value of $\lambda^{s}(q_{s}≈q_{0})$ (Methods) from simulations of the ERM with a large $N=1024$ as an approximation. Furthermore, we employed a smoothing technique to reduce bias in the estimation of $\lambda^{s}(q_{s})$ due to the leading zigzag eigenvalues (i.e., the largest eigenvalues) of the eigenspectrum. Specifically, we determined the nearest rank $j<Nq_{0}$ and then smoothed the eigenvalue $log⁡\lambda^{s}(q_{s})$ on the log–log scale using the formula $log⁡\lambda^{s}(q_{s})=\frac{1}{3}\sumi=02log⁡\lambda^{s}(\frac{j+i}{N})$ and $log⁡q_{s}=\frac{1}{3}\sumi=02log⁡\frac{j+i}{N}$, averaging over 100 ERM simulations.

Note that we can alternatively use the high-density theory (Appendix 2) to compute the integration limit $\lambda(q_{s}=1/N)$ instead of resorting to simulations. However, since the true value deviates from the $\lambda^{h}(q_{s}=1/N)$ derived from high-density theory, this approach introduces a constant bias (Figure 4—figure supplement 2) when computing the integral in Equation 16. Therefore we used the simulation value $\lambda^{s}(q_{s}≈q_{0})$ when producing Figure 4—figure supplement 2AB.

Next, we describe how each term within the integral of Equation 15 was numerically estimated. First, we calculated $\frac{∂log⁡q}{∂log⁡ρ}$ with a similar method described in Methods. Briefly, we calculated $q_{0}(\lambda)$ for density $ρ_{0}=\frac{N_{0}}{L^{d}}$ and $q_{s}(\lambda)$ for density $ρ_{s}=\frac{N_{s}}{L^{d}}$, and then used the finite difference $\frac{1}{log⁡(ρ_{0}/ρ_{s})}|Δlog⁡q(\lambda)|$. Second, $\frac{∂log⁡q(\lambda)}{∂log⁡ρ}$ was evaluated at $\lambda=\lambda(q_{1})+i\frac{\lambda(q_{0})−\lambda(q_{1})}{k−1}$, where $i=0,1,2,…,k−1$, and we used $k=20$. Finally, we performed a cubic spline interpolation of the term $\frac{∂log⁡q}{∂log⁡ρ}$, and obtained the theoretical CI by an integration of Equation 15. Figure 4—figure supplement 2A, B shows a comparison between theoretical CI and that obtained by numerical simulations of ERM (Methods).

### Fitting ERM to data

#### Estimating the ERM parameters

Our ERM model has four parameters: $\mu$ and $ϵ$ dictate the kernel function $f(x→)$, whereas the box size $L$ and the embedding dimension $d$ determine the neuronal density $ρ$. In the following, we describe an approximate method to estimate these parameters from pairwise correlations measured experimentally $R_{ij}=\frac{C_{ij}}{\sigma_{i}\sigma_{j}}$. We proceed by deriving a relationship between the correlation probability density distribution $h(R)$ and the pairwise distance probability density distribution $g(u):=g(‖x→_{1}−x→_{2}‖)$ in the functional space, from which the parameters of the ERM can be estimated.

Consider a distribution of neurons in the functional space with a coordinate distribution $p(x→)$. The pairwise distance density function $g(u)$ is related to the spatial point density by the following formula:

$$
g(u)=\int_{[0,L]^{d}}p(x→_{1})p(x→_{2})\delta(‖x→_{1}−x→_{2}‖−u)dx→_{1}dx→_{2}
$$

For ease of notation, we subsequently omit the region of integration, which is the same as here. In the case of a uniform distribution, $p(x→_{1})=p(x→_{2})=1/V=1/L^{d}$. For other spatial distributions, Equation 17 cannot be explicitly evaluated. We therefore make a similar approximation by focusing on a small pairwise distance (i.e., large correlation):

$$
p(x→_{1})≈p(x→_{2})≈p(\frac{x→_{1}+x→_{2}}{2})
$$

By a change of variables:

$$
X→=\frac{x→_{1}+x→_{2}}{2},u→=x→_{1}−x→_{2},
$$

Equation 17 can be rewritten as

$$
g(u)≈\intp^{2}(X→)\delta(‖u→‖−u)dX→du→=S_{d−1}(u)\intp^{2}(X→)dX→
$$

where $S_{d−1}(u)$ is the surface area of $d−1$ sphere with radius u. Note that the approximation of $g(u)$ is not normalized to 1, as Equation 19 provides an approximation valid only for small pairwise distances (i.e., large correlation). Therefore, we believe this does not pose an issue.

With the approximate power-law kernel function $R=f(u)≈(\frac{ϵ}{u})^{\mu}$, the probability density function of pairwise correlation $h(R)$ is given by:

$$
h(R)=g(u)|\frac{du}{dR}|=\frac{2\pi^{\frac{d}{2}}ϵ^{d}}{Γ(\frac{d}{2})\muR^{(\mu+d)/\mu}}\intp^{2}(X→)dX→
$$

Taking the logarithm on both sides

$$
log⁡h(R)=log⁡(ϵ^{d}\intp^{2}(X→)dX→)+log⁡\frac{2\pi^{\frac{d}{2}}}{Γ(\frac{d}{2})\mu}−\frac{\mu+d}{\mu}log⁡R
$$

Equation 21 is the key formula for ERM parameters estimation. In the case of a uniform spatial distribution, $ϵ^{d}\intp^{2}(X→)dX→=ϵ^{d}/V=(ϵ/L)^{d}$. For a given dimension $d$, we can therefore estimate $\mu$ and $(ϵ/L)^{d}$ separately by fitting $h(R)$ on the log–log scale using the linear least squares. Lastly, we fit the distribution of $\sigma^{2}$ (the diagonal entries of the covariance matrix $C$) to a log-normal distribution by estimating the maximum likelihood.

There is a redundancy between the unit of the functional space (using a rescaled $ϵ_{\delta}≡ϵ/\delta$) and the unit of $f(x→)$ (using a rescaled $f_{\delta}(x→)≡f(x→/\delta)$), thus $ϵ$ and $L$ are a pair of redundant parameters: once ε is given, $L$ is also determined. We set $ϵ=0.03125$ throughout the article. In summary, for a given dimension $d$ and $ϵ$, $\mu$ of $f(x→)$ (Equation 11), the distribution of $\sigma^{2}$ and $ρ$ (or equivalently $L$) can be fitted by comparing the distribution of pairwise correlations in experimental data and ERM. Furthermore, knowing $(ϵ/L)^{d}$ enables us to determine a fundamental dimensionless parameter

$$
ρϵ^{d}:=N(ϵ/L)^{d},
$$

which tells us whether the experimental data are better described by the high-density theory or the Gaussian variational method (Appendix 2). Indeed, the fitted $ρϵ^{d}∼10^{−3}−10^{0}$ is much smaller than 1, consistent with our earlier conclusion that neural data are better described by an ERM model in the intermediate-density regime.

Notably, we found that a smaller embedding dimension $d\leq5$ gave a better fit to the overall pairwise correlation distribution. The following is an empirical explanation. As $d$ grows, to best fit the slope of $log⁡h(R)−log⁡R$, $\mu$ will also grow. However, for very high dimensions $d$, the y-intercept would become very negative, or equivalently, the fitted correlation would become extremely small. This can be verified by examining the leading order $log⁡R$ independent term in Equation 21, which can be approximated as $dlog⁡\frac{ϵ}{L}+\frac{d}{2}(log⁡\pi+1−log⁡\frac{d}{2})$. It becomes very negative for large $d$ since $ϵ≪L$ by construction. Throughout this article, we use $d=2$ when fitting the experimental data with our ERM model.

The above calculation can be extended to the cases where the coordinate distribution $p(x→)$ becomes dependent on other parameters. To estimate the parameters in coordinate distributions that can generate ERMs with a similar pairwise correlation distribution (Appendix 1—figure 1), we fixed the integral value $\intp^{2}(x→)dx→$. Consider, for example, a transformation of the uniform coordinate distribution to the normal distribution $N(\mu_{p}=0,\sigma_{p}^{2}I)$ in $R^{2}$. We imposed $\intp^{2}(x→)dx→=1/(4\pi\sigma_{p}^{2})=1/L^{2}$. For the log-normal distribution, a similar calculation led to $Lexp⁡(\sigma_{p}^{2}/4−\mu_{p})=2\sqrt{\pi}\sigma_{p}$. The numerical values for these parameters are shown in Appendix 1. However, note that due to the approximation we used (Equation 18), our estimate of the ERM parameters becomes less accurate if the density function $p(x→)$ changes rapidly over a short distance in the functional space. More sophisticated methods, such as grid search, may be needed to tackle such a scenario.

After determining the parameters of the ERM, we first examine the spectrum of the ERM with uniformly distributed random functional coordinates $x→_{i}\in[0,L]^{d}$ (Figure 5—figure supplement 1M–R). Second, we use $f(x→)$ to translate experimental pairwise correlations into pairwise distances for all neurons in the functional space (Figure 5—figure supplement 2, Figure 5—figure supplement 1G–L). The embedding coordinates $x→_{i}$ in the functional space can then be solved through multidimensional scaling (MDS) by minimizing the Sammon error (Methods). The similarity between the spectra of the uniformly distributed coordinates (Figure 5—figure supplement 1M–R) and those of the embedding coordinates (Figure 5—figure supplement 1G–L) is also consistent with the notion that specific coordinate distributions in the functional space have little impact on the shape of the eigenspectrum (Appendix 1—figure 1).

#### Nonnegativity of data covariance

To use ERM to model the covariance matrix, the pairwise correlation is given by a non-negative kernel function $f(x→)$ that monotonically decreases with the distance between neurons in the functional space. This nonnegativeness brings about a potential issue when applied to experimental data, where, in fact, a small fraction of pairwise correlations/covariances are negative. We have verified that the spectrum of the data covariance matrix (Figure 2—figure supplement 3) remains virtually unchanged when replacing these negative covariances with zero (Figure 2—figure supplement 3). This confirms that the ERM remains a good model when the neural dynamics is in a regime where pairwise covariances are mostly positive Dahmen et al., 2019 (see also Figure 2—figure supplement 2B, Figure 2—figure supplement 2B–D).

#### Multidimensional scaling

With the estimated ERM parameters ($\mu$ in $f(x→)$ and the box size $L$ for given $ϵ$ and $d$, see Methods), we performed MDS to infer neuronal coordinates $x→_{i}$ in functional space. First, we computed a pairwise correlation $R_{ij}=\frac{C_{ij}}{\sigma_{i}\sigma_{j}}$ from the data covariances. Next, we calculated the pairwise distance, denoted by $u_{ij}^{∗}$, by computing the inverse function of $f(x→)$ with respect to the absolute value of $R_{ij}$, $u_{ij}^{∗}=f^{−1}(|R_{ij}|)$. We used the absolute value $|R_{ij}|$ instead of $R_{ij}$ as a small percentage of $R_{ij}$ are negative (Figure 2—figure supplement 2A–D) where the distance is undefined. This substitution by the absolute value serves as a simple workaround for the issue and is only used here in the analysis to infer the neuronal coordinates by MDS. Finally, we estimated the embedding coordinates $x→_{i}$ for each neuron by the SMACOF algorithm (Scaling by MAjorizing a COmplicated Function), which minimizes the Sammon error

$$
E=\frac{1}{\sumi<ju_{ij}^{∗}}\sumi<j\frac{(u_{ij}^{∗}−u_{ij})^{2}}{u_{ij}^{∗}}
$$

where $u_{ij}=‖x→_{i}−x→_{j}‖$ is the pairwise distance in the embedding space calculated above. To reduce errors at large distances (i.e., small correlations with $R_{ij}<f(L)$, where $L$ is the estimated box size), we performed a soft cut-off at a large distance:

$$
u_{ij}^{∗}=f^{−1}(|R_{ij}|),R_{ij}\geqf(L)u_{ij}^{∗}=Llog⁡(f^{−1}(|R_{ij}|)/L)+L,R_{ij}<f(L)
$$

During the optimization process, we started at the embedding coordinates estimated by the classical MDS (Cox and Cox, 2000), with an initial sum of squares distance error that can be calculated directly, and ended with an error or its gradient smaller than 10−4.

The fitted ERM with the embedding coordinates $x→_{i}$ reproduced the experimental covariance matrix including the cluster structures (Figure 5—figure supplement 2) and its sampling eigenspectra (Figure 5—figure supplement 1).

### Canonical correlation analysis

Here we briefly explain the CCA method (Knapp, 1978) for completeness. The basis vectors $v→_{func}$ and $v→_{anat}$, in functional and anatomical space, respectively, were found by maximizing the correlation $R_{CCA}=corr({v→_{func}⋅x→_{i}},{v→_{anat}⋅y→_{i}})$. These basis vectors satisfy the condition that the projections of the neuron coordinates along them, ${x→_{i}⋅v→_{func}}$ and ${y→_{i}⋅v→_{anat}}$, are maximally correlated among all possible choices of $v→_{func}$ and $v→_{anat}$. Here, ${x→_{i}}$, ${y→_{i}}$ represent the coordinates in functional and anatomical spaces, respectively. The resulting maximum correlation is $R_{CCA}$. To check the significance of the canonical correlation, we shuffled the functional space coordinates ${x→_{i}}$ across neurons’ identity and re-calculated the canonical correlation with the anatomical coordinates, as shown in Figure 5—figure supplement 4.

To study the effect of functional–anatomical relation described by $R_{CCA}$ in the ERM model, we generated three-dimensional anatomical coordinates ${y→_{i}}$ and two-dimensional functional coordinates ${x→_{i}}$ for each neuron which are jointly five-dimensional zero-mean multivariate Gaussian random variables. The coordinates are independent among each other, except for the first dimension ${x→_{i}^{1}}$ of the functional coordinates and the first dimension ${y→_{i}^{1}}$, which are assigned to have a correlation coefficient equals to $R_{CCA}$. The variances of the coordinates are $\sigma_{y1}^{2}=1,\sigma_{y2}^{2}=1,\sigma_{y3}^{2}=1$, and $\sigma_{x1}^{2}=2,\sigma_{x2}^{2}=1$ for the numerics in Figure 5—figure supplement 7. Under this construction, the first canonical correlation between the anatomical and functional coordinates equals $R_{CCA}$, and the first canonical direction $v→_{anat}$ in the anatomical space is $(1,0,0)^{T}$ and the first canonical direction $v→_{func}$ in the functional space is $(1,0)^{T}$.

### Spectrum of three types of sampling procedures in ERM model

In Result, we have considered three types of sampling procedures: random sampling (RSap), spatial sampling in the anatomical space (ASap, e.g., recording neurons in a brain region), and spatial sampling in the functional space (FSap), namely spatial sampling in functional space by subdividing the space into smaller regions, is equivalent to the previously reported RG inspired process (Bradde and Bialek, 2017). Here, we consider the relationship between the spectrum of three types of sampling procedures.

We assume a uniform random distribution of neurons in a $d$-dimensional functional space, $[0,L]^{d}$. For RSap procedures, the resulting neuronal density $ρ_{R}$ is reduced to $ρ_{R}=kρ_{0}$, with $k$ representing the sampling ratio ($k=N/N_{0}$) and $ρ_{0}$ being the initial density. In contrast, FSap maintains the original density, $ρ_{F}=ρ_{0}$. This constancy in neuronal density under FSap ensures that the covariance eigenspectrum remains invariant across scales for any spatial correlation functions $f(x→)$, such as power law and exponential, as shown in Appendix 1—figure 5A, B, D, E. In contrast, RSap reduces ρ, thus demanding more rigorous conditions to achieve a scale-invariant covariance spectrum (e.g., compare Appendix 1—figure 5A, C).

Under ASap, sampled neurons are not spread out evenly in functional space, whereas our theoretical framework assumes a uniform distribution. To reconcile this discrepancy, we employ a uniform approximation of the neural distribution. This approach involves introducing an effective density, $ρ^{′}$, defined as the spatial average of the density function $ρ(x→)$. This adjustment allows our theoretical model to accommodate non-uniform distributions encountered in anatomically spatial sampling.

$$
ρ^{′}≡⟨ρ(x→)⟩=\intp(x→)ρ(x→)dx→=kN_{0}\intp^{2}(x→)dx→,
$$

where $p(x→)$ is the normalized density distribution (see Methods).

Using the Cauchy–Schwarz inequality, we have

$$
\intp^{2}(x→)dx→\intdx→\geq(\intp(x→)dx→)^{2}
$$

thus $ρ^{′}\geqkρ_{0}$.

According to the condition $p(x→)<\frac{1}{kV}$, we have $ρ^{′}\leqρ_{0}$, intuitively, sampling within a uniformly distributed neuron population does not increase the density.

So we have $ρ_{0}\geqρ_{A}^{′}\geqkρ_{0}$, that is, $ρ_{F}\geqρ_{A}^{′}\geqρ_{R}$. Thus, the spectrum ASap should be between FSap and RSap.

### Dimensions of three types of sampling procedures in ERM model

#### Scaling of dimensions through random sampling

Let us revisit the definition of the participation ratio (PR) dimension as defined in Equation 5:

$$
D_{PR}(C)=\frac{(\sumi\lambda_{i})^{2}}{\sumi\lambda_{i}^{2}}=\frac{(Tr(C))^{2}}{Tr(C^{2})}=\frac{N^{2}E(\sigma^{2})^{2}}{NE(\sigma^{4})+N(N−1)E_{i\neqj}(C_{ij}^{2})}
$$

During the random sampling process, the expected values $E(\sigma^{2})$, $E(\sigma^{4})$, and $E_{i\neqj}(C_{ij}^{2})$ remain constant. These constants allow for the estimation of the PR dimension across various scales using:

$$
D_{PR}^{RSap}=\frac{kN_{0}E(\sigma^{2})^{2}}{E(\sigma^{4})+(kN_{0}−1)E_{i\neqj}(C_{ij}^{2})}
$$

Here, $k=N/N_{0}$ represents a scaling factor (fraction) associated with sampling. The key question is to understand how the dimensionality changes with $k$. Under random sampling, as $k$ increases, the dimensionality will quickly approaches a saturating point defined by Equation 1.

#### Scaling of dimensions through functional sampling

In this section, we leverage the uniform ERM model to estimate dimensions within the context of functional sampling, specifically focusing on the estimation of squared pairwise covariance $E_{i\neqj}(C_{ij}^{2})$ and dimensionality. Adopting an approximation for a power-law kernel function $f(x)≈ϵ^{\mu}‖x‖^{−\mu}$ allows us to express the expected value of the squared covariance $E_{i\neqj}(C_{ij}^{2})$ as follows:

$$
E_{i\neqj}(C_{ij}^{2})=\int_{[0,L]^{d}}p(x→_{1})p(x→_{2})f^{2}(‖x→_{1}−x→_{2}‖)dx→_{1}dx→_{2}≈\int_{[0,L]^{d}}p(x→_{1})p(x→_{2})ϵ^{2\mu}‖x→_{1}−x→_{2}‖^{−2\mu}dx→_{1}dx→_{2}.
$$

For a set subjected to functional sampling with a sampling fraction $k$, this procedure adjusts the size of the functional space in the ERM model by a factor of $k^{−1/d}$. Consequently, the $E_{i\neqj}^{k}(C_{ij}^{2})$ for the sampled fraction $k$ is given by:

$$
E_{i\neqj}^{k}(C_{ij}^{2})=\int_{[0,k^{1/d}L]^{d}}p(x→_{1})p(x→_{2})f^{2}(‖x→_{1}−x→_{2}‖)dx→_{1}dx→_{2}=\int_{[0,L]^{d}}p(x→_{1})p(x→_{2})f^{2}(k^{1/d}‖x→_{1}−x→_{2}‖)dx→_{1}dx→_{2}≈\int_{[0,L]^{d}}p(x→_{1})p(x→_{2})ϵ^{2\mu}k^{−2\mu/d}‖x→_{1}−x→_{2}‖^{−2\mu}dx→_{1}dx→_{2}≈k^{−2\mu/d}E_{i\neqj}(C_{ij}^{2}),
$$

Here, we assume that $E[\sigma^{2}]$ and $E[\sigma^{4}]$ are constant across the sampling process. This model enables the estimation of the ratio $\mu/d$ as detailed in the Methods.

$$
D_{PR}^{FSap}≈\frac{kN_{0}E(\sigma^{2})^{2}}{E(\sigma^{4})+(kN_{0}−1)k^{−2\mu/d}E_{i\neqj}(C_{ij}^{2})}
$$

In the large $N$ limit, we observe distinct behaviors in the evolution of dimensionality in both theory and data: it saturates in RSap (dashed line in Figure 5D), namely $D_{PR}^{RSap}≈D_{PR}$ defined in Equation 1, whereas it follows a different scaling relationship $D_{PR}^{FSap}≈k^{2\mu/d}D_{PR}$ in FSap (solid line in Figure 5D).

#### Comparative analysis of PR dimension across sampling techniques

This section examines the behavior of the PR dimension under three sampling techniques: anatomical sampling, random sampling, and functional sampling. We show that the average PR dimension following anatomical sampling occupies a middle ground between the extremes presented by random and functional sampling.

The PR dimension, denoted $D_{PR}$, reflects the sampling impact and depends on the distribution $p(X→)$ of the functional coordinates $X→$. Defining the sampling fraction as $k=1/q$, the mean $D_{PR}$ is represented as:

$$
mean(D_{PR})=\frac{1}{q}\sumi=1qD_{PR}^{i}=\frac{1}{q}\sumi=1qJ(p_{i}(X→)),
$$

where the neuron set $1,2,...,N$ is segmented into $q$ clusters ${X→_{1},X→_{2},...,X→_{q}}$, each comprising $\frac{N}{q}$ neurons. The probability distribution $p_{i}(X→)$ corresponds to each cluster ${X→_{i}}$. The probability distribution for each cluster, $p_{i}(X→)$, emerges naturally from the sampling process.

The equivalence of the mean probability density function across the sampled clusters to the original set’s probability density function leads us to the condition:

$$
\frac{1}{q}\sumi=1qp_{i}(X→)=p(X→),
$$

This condition is a direct consequence of the sampling process, ensuring that the aggregated probability density function of all sampled sets mirrors the overall density distribution of the neurons.

Applying the Lagrange multiplier method to optimize the mean $D_{PR}$:

$$
L(p,\lambda)=\frac{1}{q}\sumi=1qJ(p_{i}(X→))+\int_{D}d^{d}X→\lambda(X→)(\frac{1}{q}\sumi=1qp_{i}(X→)−p(X→)),
$$

Here, $L(p,\lambda)$ is the Lagrangian, $\lambda(X→)$ is the Lagrange multiplier, we derive the optimal condition:

$$
\frac{∂L(p,\lambda)}{∂p_{i}}=0,
$$

yielding:

$$
\frac{1}{q}\frac{∂J}{∂p_{i}(X→)}+\frac{\lambda(X→)}{q}=0.
$$

At the optimal mean $D_{PR}$, each $p(X→_{i})$ is equivalent, leading to $p(X→_{i})=p(X→_{j})=p(X→)$ (representative of random sampling). Hence, the mean $D_{PR}$ post-random sampling sets the upper limit for the mean $D_{PR}$ after anatomical sampling.

Let us investigate the lower bound of the mean PR dimension with the ERM model. For the minimization of mean $(D_{PR})$, a key requirement is the functional spatial proximity of neurons within the same cluster, in other words, the neuron set should be distinctly separated in functional space. Consequently, achieving the minimum mean PR dimension necessitates a functional sampling strategy.

#### Derive upper bound of dimension from spectrum

To deduce $D_{PR}$ from the spectrum, for simplicity, we focus on the high-density region, where we have an analytical expression for λ that is valid for large eigenvalues:

$$
\lambda_{r}=\gamma(\frac{r}{N})^{−1+\frac{\mu}{d}}⋅ρ^{\frac{\mu}{d}}=\gammar^{−1+\frac{\mu}{d}}L^{−\mu}Nforr\leq\beta(N),
$$

where $L$ is the size of the functional space, $\gamma$ is the coefficient in Equation 3, which depends on $d$, $\mu$, and $E(\sigma^{2})$. Note that the eigenvalue $\lambda_{r}$ decays rapidly after the threshold $r=\beta(N)$. Since we did not discuss small eigenvalues in this article, we represent them here as an unknown function $η(r,N,L)$:

$$
\lambda_{r}=η(r,N,L)forr>\beta(N)
$$

As discussed in Methods, without changing the properties of the spectrum, we can always impose $E(\sigma^{2})=1$ such that

$$
\sumr=1N\lambda_{r}=Tr⁡(C)=N
$$

We emphasize that this constraint requires that large and small eigenvalues behave differently because otherwise $\sumr=1Nr^{−\alpha}$ with $\alpha<1$ would scale as $N^{1−\alpha}$, and $\sumr=1N\lambda_{r}$ is not proportional to $N$.

Using the Cauchy–Schwarz inequality, we have an upper bound of $\sumr=1N\lambda_{r}^{2}$:

$$
\sumr=1N\lambda_{r}^{2}\leq(\sumr\lambda_{r})^{2}=N^{2}
$$

On the other hand, $\lambda_{1}^{2}$ is a lower bound of $\sumr=1N\lambda_{r}^{2}$:

$$
\sumr=1N\lambda_{r}^{2}>\lambda_{1}^{2}=L^{−2\mu}N^{2}\gamma^{2}
$$

As a result, the dimensionality

$$
D_{PR}=\frac{(\sumr=1N\lambda_{r})^{2}}{\sumr=1N\lambda_{r}^{2}},
$$

is bounded as

$$
1\leqD_{PR}<L^{2\mu}\gamma^{−2}
$$

Under random sampling, $L$ remains fixed. Thus, we must have a bounded dimensionality that is independent of $N$ for our ERM model. A tighter lower bound of $\sumr=1N\lambda_{r}^{2}$ is

$$
\sumr=1N\lambda_{r}^{2}>\gamma^{2}L^{−2\mu}N^{2}\sumr=1\beta(N)(r^{−2+2\mu/d})
$$

A tighter upper bound of participation ratio $D_{PR}$ can be written as:

$$
D_{PR}=\frac{(\sumr=1N\lambda_{r})^{2}}{\sumr=1N\lambda_{r}^{2}}<\frac{L^{2\mu}\gamma^{−2}}{\sumr=1\beta(N)(r^{−2+2\mu/d})}<L^{2\mu}\gamma^{−2}
$$

However, in functional sampling, enlarging the region size with constant density ρ results in $L∼N^{1/d}$. Thus, the upper bound of $D_{PR}$ should grow as $N^{2\mu/d}$, consistent with the previously derived result (Equation 31) in Methods.

#### Simulating CCA and anatomical sampling

In this section, we estimate the dimensions of the anatomically sampled neuron set. For simplicity, we assume that the functional coordinates of neurons, $X_{i}$, and the anatomical coordinates of neurons, $Y_{i}$, both follow a multivariate Gaussian distribution. We define anatomical sampling, which involves sampling on $Y_{i}$, along a direction chosen arbitrarily and denote this direction as $Y^{A}$. Subsequently, we perform sampling on $X_{i}$ in the direction denoted by $X^{A}$, which is determined to have the highest correlation with $Y^{A}$ according to CCA. This process effectively mimics the scenario of functional sampling.

The key to calculating the PR dimension involves computing the expected value $E_{i\neqj}(C_{ij}^{2})$. In the ERM model, the distribution of $C_{ij}$ can be estimated by the distribution of points in the functional space. This allows for the calculation of the PR dimension across anatomical sampling by comparing the distribution of $X_{i}$ after anatomical sampling with that after functional sampling. We can model the distribution of $X^{A}$ and $Y^{A}$ as follows:

$$
R_{ASap}=corr(X^{A},Y^{A}),C_{ASap}=corr(X^{A},Y^{A})\sigma_{x}\sigma_{y},[X^{A}Y^{A}]∼N([00],[\sigma_{x}^{2}C_{ASap}C_{ASap}\sigma_{y}^{2}]),
$$

Here, we consider only the projection of the functional coordinate onto the direction $X^{A}$, which exhibits the highest correlation, denoted by $R_{ASap}$, with $Y^{A}$. Specifically, when selecting the anatomical direction as the first CCA direction, the correlation between $X^{A}$ and $Y^{A}$ reaches its maximum, such that $R_{ASap}=R_{CCA}$. In this case, anatomical sampling results in the minimization of the dimensionality.

Now, let us perform anatomical sampling on the neurons. The $X→_{i}$ and $Y→_{i}$ denote the functional and anatomical coordinates of the $i^{th}$ neuron cluster after anatomical sampling, respectively.

To approximate, we need to calculate the functional coordinate probability distribution $p(X→_{i})=p(X→|q_{ik}^{y}<Y^{A}<q_{(i+1)k}^{y})$, which is the distribution of the $i^{th}$ neuron cluster after anatomical sampling. $Y^{A}$ represents the selected direction in anatomical space, and $q_{ik}^{y}$ denotes the $ik^{th}$ quantile of $Y^{A}$, where $k$ is the sampled fraction. Note the following relationships and distributions:

$$
p(X^{A}|Y^{A}=y)=\frac{p(X^{A},Y^{A}=y)}{p(Y^{A}=y)},p(X^{A}|Y^{A}=y)∼N(y\frac{\sigma_{x}}{\sigma_{y}}R_{ASap},\sigma_{x}^{2}(1−R_{ASap}^{2})).
$$



$$
p(X_{i}^{A})=p(X^{A}|q_{ik}^{y}<Y^{A}<q_{(i+1)k}^{y})=\frac{1}{k}\int_{q_{ik}^{y}}^{q_{(i+1)k}^{y}}p(X^{A}|Y^{A}=y)dy
$$

The conditional probability distribution $P(X^{A}|q_{ik}^{y}<Y^{A}<q_{(i+1)k}^{y})$ is equivalent to the distribution of the sum of $Y_{i}^{A}\frac{\sigma_{x}}{\sigma_{y}}R_{ASap}$ and $X_{0}$, where $X_{0}∼N(0,\sigma_{x}^{2}(1−R_{ASap}^{2}))$:

$$
X_{i}^{A}=Y_{i}^{A}\frac{\sigma_{x}}{\sigma_{y}}R_{ASap}+X_{0},
$$



$$
p(Y_{i}^{A}=y)={\frac{1}{k\sqrt{2\pi}\sigma_{y}}exp⁡(−\frac{y^{2}}{2\sigma_{y}^{2}})for q_{ik}^{y}<y<q_{(i+1)k}^{y},0otherwise.
$$

The computation of $X_{i}^{A}$ involves two technical challenges: (1) The distribution of $Y_{i}^{A}$ is represented by a non-elementary function (Equation 49), which complicates the direct calculation of $X_{i}^{A}$, which is the sum of $Y_{i}^{A}R_{ASap}\sigma_{x}/\sigma_{y}$ and $X_{0}$. To facilitate approximation, we model $Y_{i}^{A}$ using a normal distribution with equivalent variance. (2) Calculating the variance of $Y_{i}^{A}$ presents direct challenges, and the variance of $Y_{i}^{A}$ differs across different neuron clusters i. Using a uniform distribution for $Y$ simplifies this task (this assumption is only used to calculate the variance of $Y_{i}^{A}$). Under this assumption, the variance of $Y_{i}^{A}$ can be straightforwardly calculated as $Var(Y_{i}^{A})=k^{2}\sigma_{y}^{2}$. Consequently, we approximate $Y_{i}^{A}$ and $X_{i}^{A}$ as follows:

$$
Y_{i}^{A}∼N(\frac{q_{ik}^{y}+q_{(i+1)k}^{y}}{2},k^{2}\sigma_{y}^{2}),
$$



$$
X_{i}^{A}∼N(\frac{q_{ik}^{y}+q_{(i+1)k}^{y}}{2}\frac{\sigma_{x}}{\sigma_{y}}R_{ASap},\sigma_{x}^{2}(1−R_{ASap}^{2}+k^{2}R_{ASap}^{2})).
$$

Calculating the PR dimension directly from the distribution of $X_{i}^{A}$ is difficult; thus, we approximate anatomical sampling with fraction $k$ as functional sampling with fraction $k_{f}$, leading to:

$$
k_{f}=\sqrt{1+k^{2}R_{ASap}^{2}−R_{ASap}^{2}}.
$$

Using the equation for functional sampling $E_{i\neqj}^{k}(C_{ij}^{2})≈k^{−2\mu/d}E_{i\neqj}(C_{ij}^{2})$ (Equation 30):

$$
E_{i\neqj}^{k}(C_{ij}^{2})≈(1+k^{2}R_{ASap}^{2}−R_{ASap}^{2})^{−\mu/d}E_{i\neqj}(C_{ij}^{2}).
$$



$$
D_{PR}^{ASap}≈\frac{kN_{0}E(\sigma^{2})^{2}}{E(\sigma^{4})+(kN_{0}−1)(1+k^{2}R_{ASap}^{2}−R_{ASap}^{2})^{−\mu/d}E_{i\neqj}(C_{ij}^{2})}
$$
