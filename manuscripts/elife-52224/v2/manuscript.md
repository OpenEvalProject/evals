# Deciphering anomalous heterogeneous intracellular transport with neural networks

## Authors

- Daniel Han<sup>1</sup> ([ORCID: 0000-0002-9088-1651](https://orcid.org/0000-0002-9088-1651)) †
- Nickolay Korabel<sup>1</sup>
- Runze Chen<sup>4</sup>
- Mark Johnston<sup>2</sup>
- Anna Gavrilova<sup>1</sup>
- Victoria J Allan<sup>2</sup> ([ORCID: 0000-0003-4583-0836](https://orcid.org/0000-0003-4583-0836)) †
- Sergei Fedotov<sup>1</sup> †
- Thomas A Waigh<sup>3</sup> ([ORCID: 0000-0002-7084-559X](https://orcid.org/0000-0002-7084-559X)) †

### Affiliations

1. Department of Mathematics, University of Manchester Manchester United Kingdom
2. School of Biological Sciences, University of Manchester Manchester United Kingdom
3. Department of Physics and Astronomy, University of Manchester Manchester United Kingdom
4. Department of Computer Science, University of Manchester Manchester United Kingdom
5. The Photon Science Institute, University of Manchester Manchester United Kingdom

† Corresponding author

## Abstract

Intracellular transport is predominantly heterogeneous in both time and space, exhibiting varying non-Brownian behavior. Characterization of this movement through averaging methods over an ensemble of trajectories or over the course of a single trajectory often fails to capture this heterogeneity. Here, we developed a deep learning feedforward neural network trained on fractional Brownian motion, providing a novel, accurate and efficient method for resolving heterogeneous behavior of intracellular transport in space and time. The neural network requires significantly fewer data points compared to established methods. This enables robust estimation of Hurst exponents for very short time series data, making possible direct, dynamic segmentation and analysis of experimental tracks of rapidly moving cellular structures such as endosomes and lysosomes. By using this analysis, fractional Brownian motion with a stochastic Hurst exponent was used to interpret, for the first time, anomalous intracellular dynamics, revealing unexpected differences in behavior between closely related endocytic organelles.

## Introduction

The majority of transport inside cells on the mesoscale (nm-100μm) is now known to exhibit non-Brownian anomalous behavior (Metzler and Klafter, 2004; Barkai et al., 2012; Waigh, 2014). This has wide ranging implications for most of the biochemical reactions inside cells and thus cellular physiology. It is vitally important to be able to quantitatively characterize the dynamics of organelles and cellular responses to different biological conditions (van Bergeijk et al., 2015; Patwardhan et al., 2017; Moutaux et al., 2018). Classification of different non-Brownian dynamic behaviors at various time scales has been crucial to the analysis of intracellular dynamics (Fedotov et al., 2018; Bressloff and Newby, 2013), protein crowding in the cell (Banks and Fradin, 2005; Weiss et al., 2004), microrheology (Waigh, 2005; Waigh, 2016), entangled actin networks (Amblard et al., 1996), and the movement of lysosomes (Ba et al., 2018) and endosomes (Flores-Rodriguez et al., 2011). Anomalous transport is currently analyzed by statistical averaging methods and this has been a barrier to understanding the nature of its heterogeneity.

Spatiotemporal analysis of intracellular dynamics is often performed by acquiring and tracking microscopy movies of fluorescing membrane-bound organelles in a cell (Rogers et al., 2007; Flores-Rodriguez et al., 2011; Chenouard et al., 2014; Zajac et al., 2013). These tracks are then commonly interpreted using statistical tools such as the mean square displacement (MSD) averaged over the ensemble of tracks, $⟨Δ⁢r^{2}⁢(t)⟩$. The MSD is a measure that is widely used in physics, chemistry and biology. In particular, MSDs serve to distinguish between anomalous and normal diffusion at different temporal scales by determining the anomalous exponent $\alpha$ through $⟨Δ⁢r^{2}⁢(t)⟩∼t^{\alpha}$ (Metzler and Klafter, 2000). Diffusion is defined as $\alpha=1$, sub-diffusion $0<\alpha<1$ and super-diffusion $1<\alpha<2$ (Klafter and Sokolov, 2011). To improve the statistics of MSDs, they are often averaged over different temporal scales, forming the time-averaged MSD (TAMSD), $Δr^{2}(\tau)¯∼\tau^{\alpha}$, where $\tau$ is the lag time (Sokolov, 2012).

For stochastic processes with long-range time dependence such as fractional Brownian motion (fBm), other statistical averaging methods exist. For fBm, the MSD is $⟨B_{H}^{2}⁢(t)⟩∼t^{2⁢H}$ with the Hurst exponent, $H$ varying between 0 and 1. One can use rescaled and sequential range analysis (Samorodnitsky, 2016; Peters, 1994) to estimate $H$. The advantage of modeling intracellular transport with fBm is that both sub-diffusion ($0<H<1/2$) and super-diffusion ($1/2<H<1$) can be explained in a unified manner using only the Hurst exponent. The essence of fBm is that long-range correlations result in random trajectories that are anti-persistent ($0<H<1/2$) or persistent ($1/2<H<1$). How can we understand persistence in the context of intracellular transport? The term persistence can be understood as the processive motor-protein transport of cargo in one direction, whether it be retrograde or anterograde. From a probabilistic viewpoint, persistence can be interpreted as the cargo being more likely to keep the same direction given it had been moving in this fashion before. Conversely, anti-persistence is interpreted as cargo being more likely to change its direction given it had been moving in that direction before. Anti-persistence can arise if cargo is confined to a local volume in the cytoplasm simply due to crowding or tethering biochemical interactions (Harrison et al., 2013), which in effect leads to sub-diffusion (Weiss et al., 2004; Ernst et al., 2012). By interpreting intracellular cargo transport as fBm, there are two main advantages: we can describe movement with the intuitive biological concepts of persistence and anti-persistence; and we can provide an immediate link to anomalous diffusion since α = 2H for constant H.

Cargo movement in vivo often exhibits random switching between persistent and anti-persistent movement, even in a single trajectory (Chen et al., 2015). Therefore, we can model this by a stochastic local Hurst exponent, $H⁢(t)$, which jumps between persistent ($1/2<H⁢(t)<1$) and anti-persistent ($0<H⁢(t)<1/2$) states. Still, a major challenge exists: how can we estimate a local stochastic Hurst exponent from a trajectory?

Whilst exponent estimation using neural networks is an emerging field (Bondarenko et al., 2016), segmentation of single trajectories into persistent and anti-persistent sections based on instantaneous dynamic behavior has not been studied. Instead, hidden Markov models (Monnier et al., 2015; Persson et al., 2013) and windowed analyses (Getz and Saltz, 2008) are commonly used to segment local behavior along single trajectories (see Appendix A for comparisons). Even so, most methods neglect the microscopic processes which are often a feature of intracellular transport (e.g. alternation between ‘runs’ and ‘rests’) (Weiss et al., 2004; Chen et al., 2015; Fedotov et al., 2018) and the non-Markovian nature of their motion (Fuliński, 2017). fBm was chosen due to its self-similar properties that allow direct analysis at short time scales given by experimental systems; and the experimental evidence for fBm in the crowded cytoplasm (Weiss et al., 2004; Szymanski and Weiss, 2009; Krapf et al., 2019). Moreover, other anomalous diffusion models, such as scaled Brownian motion (Lim and Muniandy, 2002), subdiffusive continuous time random walks (Sokolov, 2012) and superdiffusive Lévy walks (Fedotov et al., 2018) are not suitable to interpret anomalous trajectories on the microscopic level.

Here, we present a new method for characterizing anomalous transport inside cells based on a Deep Learning Feedforward Neural Network (DLFNN) that is trained on fBm. Neural networks are becoming a general tool in a wide range of fields, such as single-cell transcriptomics (Deng et al., 2019) and protein folding (Evans et al., 2018). We find the neural network is a much more sensitive method to characterise fBm than previous statistical tools, since it is an intrinsically non-linear regression method that accounts for correlated time series. In addition, it can estimate the Hurst exponent using as few as seven consecutive time points with good accuracy.

To test the ability of the DLFNN to segment real-world biological motility, we focused on organelles in the endocytic pathway. This pathway is essential for cell homeostasis, allowing nutrient uptake, the turnover of plasma membrane components, and uptake of growth factor receptors bound to their ligands. Early endosomes then sort components destined for degradation from material that needs to be recycled back to the cell surface or to the Trans-Golgi Network (TGN) (Naslavsky and Caplan, 2018). Many aspects of endosome function are regulated by Rab5, a small GTPase that is localized to the cytosolic face of early endosomes (Stenmark and Olkkonen, 2001). Sorting nexin 1 (SNX1) also localises to early endosomes, where it works with the retromer complex to retrieve and recycle cargoes from early endosomes to the TGN (Simonetti and Cullen, 2019). SNX1 achieves this through regulating tubular membrane elements on early endosomes by associating with regions of high membrane curvature (Carlton et al., 2004). Early endosomes mature into late endosomes, which then fuse with lysosomes, delivering their contents for degradation (Huotari and Helenius, 2011). Endocytic pathway components are highly dynamic, with microtubule motors driving long-distance movement while short-range dynamics involve actin-based motility (Granger et al., 2014; Cabukusta and Neefjes, 2018), making them ideal test cases for DLFNN analysis. The new method enables the interpretation of experimental trajectories of lysosomes and endosomes as fBm with stochastic local Hurst exponent, H (t). This in turn allows us to unambiguously and directly classify endosomes and lysosomes to be in anti-persistent or persistent states of motion at different times. From experiments, we observe that the time spent within these two states both exhibit truncated heavy-tailed distributions.

To our knowledge, this is the first method which is capable of resolving heterogeneous behavior of anomalous transport in both time and space. We anticipate that this method will be useful in characterizing a wide range of systems that exhibit anomalous heterogeneous transport. We have therefore created a GUI computer application in which the DLFNN is implemented, so that the wider community can conveniently access this analysis method.

## Results and discussion

### The DLFNN is more accurate than established methods

We tested a DLFNN trained on fBm with three hidden layers of densely connected nodes on N = 104 computer-generated fBm trajectories each with n = 102 evenly spaced time points and constant Hurst exponent $H_{s⁢i⁢m}$, randomly chosen between 0 and 1. The DLFNN estimated the Hurst exponents $H_{e⁢s⁢t}$ based on the trajectories, and these were compared with those estimated from TAMSD, rescaled range, and sequential range methods (Figure 1a). The difference between the simulated and estimated values $Δ⁢H=H_{s⁢i⁢m}-H_{e⁢s⁢t}$ was much smaller for the DLFNN than for the other methods (Figure 1a), and the DLFNN was $∼3$ times more accurate at estimating Hurst exponents with a mean absolute error ($\sigma_{H}$) $∼0.05$. Also, the errors in estimation of the DLFNN are more stable across values of $H_{s⁢i⁢m}$.

![Figure 1.](https://cdn.elifesciences.org/articles/52224/elife-52224-fig1-v2.jpg)

**Figure 1.:** (a) Plots showing the Hurst exponent estimates of fBm trajectories with $n=10^{2}$ data points by a triangular DLFNN with three hidden layers compared with conventional methods. Plots are vertically grouped by Hurst exponent estimation method: (left to right) rescaled range, MSD, sequential range and DLFNN. $\sigma_{H}$ values are shown in the title. Top row: Scatter plots of estimated Hurst exponents $H_{e⁢s⁢t}$ and the true value of Hurst exponents from simulation $H_{s⁢i⁢m}$. The red line shows perfect estimation. Second row: Due to the density of points, a Gaussian kernel density estimation was made of the plots in the top row (see Materials and methods). Third row: Scatter plots of the difference between the true value of Hurst exponents from simulation and estimated Hurst exponent $Δ⁢H=H_{s⁢i⁢m}-H_{e⁢s⁢t}$. Last row: Gaussian kernel density estimation of the plots in the third row. (b) $\sigma_{H}$ as a function of the number of consecutive fBm trajectory data points $n$ for different methods of exponent estimation. Example structures for two hidden layers and $n=5$ time series input points of the anti-triangular, rectangular and triangular DLFNN are shown in (c, d and e), respectively. (f) $\sigma_{H}$ as a function of the number of hidden layers in the DLFNN for triangular, rectangular and anti-triangular structures. (g) $\sigma_{H}$ as a function of the number of randomly sampled fBm trajectory data points $n_{r⁢a⁢n⁢d}$ with different number of hidden layers in the DLFNN shown in the legend. (h) $\sigma_{H}$ as a function of the noise-to-signal ratio ($\frac{N⁢o⁢i⁢s⁢e}{S⁢i⁢g⁢n⁢a⁢l}$) (NSR) from Gaussian random numbers added to all $n=10^{2}$ data points in simulated fBm trajectories. (i) Plots of bias $b⁢(H_{s⁢i⁢m})$, variance $Var⁢(H_{s⁢i⁢m})$ and mean square error (MSE) as functions of $H_{s⁢i⁢m}$. For each value of $H_{s⁢i⁢m}$, fBm trajectories with $n=100$ points were simulated and estimated by a triangular DLFNN.

Tracking of intracellular motion usually generates trajectories with a variable number of data points. We therefore compared the performance of the different exponent estimation methods when the number of evenly spaced, consecutive fBm time points in a trajectory varied over $n=5,6,…,10^{2}$ points. The DLFNN maintained an accuracy of $\sigma_{H}∼0.05$ across $n$, whereas $\sigma_{H}$ of other methods increase as $n$ decreases (Figure 1b), and was always substantially worse than that of the DLFNN estimation. Different DLFNN structures (see Figure 1c,d and e) performed similarly, and introducing more hidden layers did not affect the accuracy of estimation (Figure 1f and g). Given that the structure of DLFNN does not significantly affect the accuracy of exponent estimation, a triangular densely connected DLFNN was used for all subsequent analyses.

The structure of a triangular DLFNN means that the input layer consists of $n$ nodes, which are densely connected to $n-1$ nodes in the first hidden layer, such that at the $l$th hidden layer, there would be $n-l$ densely connected nodes. Then to estimate the Hurst exponent these nodes are connected to a single node using a Rectified Linear Unit (ReLU) activation function, which returns the exponent estimate. A triangular DLFNN therefore uses only $\sum_{l=0}^{L}(n-l)+1$ nodes for $L$ hidden layers and $n$ input points, whereas the rectangular structure uses $n⁢L+1$ nodes and the anti-triangular structure uses $\sum_{l=0}^{L}(n+l)+1$. The triangular structure results in a significant decrease in training parameters, and hence computational requirements, while maintaining good levels of accuracy. This demonstrates that a computationally inexpensive neural network can accurately estimate exponents.

The DLFNN’s estimation capabilities were tested further by inputting $n_{r⁢a⁢n⁢d}$ randomly sampled time points from the original fBm trajectories. Surprisingly, $\sigma_{H}∼0.05$ is regained even with just 40 out of 100 data points randomly sampled from the time series for any triangular DLFNN with more than one hidden layer (Figure 1g). For this method to work with experimental systems, it must estimate Hurst exponents even when the trajectories are noisy. Figure 1h shows how the exponent estimation error increases when Gaussian noise with varying strength compared to the original signal is added to the fBm trajectories. Importantly, the DLFNN accuracy $\sigma_{H}$ at 20% NSR is as good as the accuracy of other methods with no noise (compare 1a and h).

To characterize the accuracy of $H_{s⁢i⁢m}$ estimation by the DLFNN, we calculated the bias, $b⁢(H_{s⁢i⁢m})=𝔼⁢[H_{e⁢s⁢t}]-H_{s⁢i⁢m}$; variance, $Var⁢(H_{s⁢i⁢m})=𝔼⁢[H_{e⁢s⁢t}-𝔼⁢[H_{e⁢s⁢t}]^{2}]$; and mean square error, $MSE=Var⁢(H_{s⁢i⁢m})+b⁢(H_{s⁢i⁢m})^{2}$ (Figure 1i). To quantify the efficiency of the estimator the Fisher information of the neural network’s estimation needs to be found and the Cramer-Rao lower bound calculated. The values of bias, variance and MSE were very low (Figure 1i), which taken together with the simplicity of calculation and the accuracy of estimation even with small number of data points, demonstrates the strength of the DLFNN method. Furthermore, once trained, the model can be saved and reloaded at any time. Saved DLFNN models, code and the DLFNN Exponent Estimator GUI are available to download (see Software and Code).

### DLFNN allows analysis of simulated trajectories with local stochastic Hurst exponents

Estimating local Hurst exponents is fundamentally important because much research has focused on inferring active and passive states of transport within living cells using position-derived quantities such as windowed MSDs, directionality and velocity (Arcizet et al., 2008; Monnier et al., 2015). The trajectories are then segmented and Hurst exponents measured in an effort to characterize the behavior of different cargo when they are actively transported by motor proteins (Chen et al., 2015; Fedotov et al., 2018) or sub-diffusing in the cytoplasm (Jeon et al., 2011). However, conventional methods such as the MSD and TAMSD need trajectories with many time points ($n∼10^{2}-10^{3}$) to calculate a single Hurst exponent value with high fidelity. In contrast, the DLFNN enables the Hurst exponent to be estimated, directly from positional data, for a small number of points. Furthermore, the DLFNN measures local Hurst exponents without averaging over time points and is able to characterize particle trajectories that may exhibit multi-fractional, heterogeneous dynamics.

To provide a synthetic data set that mimics particle motion in cells, we simulated fBm trajectories with Hurst exponents that varied in time, and applied a symmetric moving window to estimate the Hurst exponent using a small number of data points before and after each time point (Figure 2). The DLFNN was able to identify segments with different exponents, and provided a good running estimation of the Hurst exponent values. The DLFNN could also handle trajectories with different diffusion coefficients, and generally performed better than MSD analysis when a sliding window was used (see Appendix B).

![Figure 2.](https://cdn.elifesciences.org/articles/52224/elife-52224-fig2-v2.jpg)

**Figure 2.:** Top: Plot of displacement as a function of time from a simulated fBm trajectory (blue) with multiple exponent values. Bottom: Hurst exponent values used for simulation (magenta), and the DLFNN exponent predictions of the neural network using a 15 point moving window (black).

### DLFNN analysis reveals differences in motile behavior of organelles in the endocytic pathway

Early endosomes labeled with green fluorescent protein (GFP)-Rab5 undergo bursts of rapid cytoplasmic dynein-driven motility interspersed with periods of rest (Flores-Rodriguez et al., 2011; Zajac et al., 2013). We therefore applied the DLFNN method to experimental trajectories obtained from automated tracking (Newby et al., 2018) data of GFP-Rab5-labeled endosomes in an MRC-5 cell line that stably expressed GFP-Rab5 at low levels (Figure 3). A moving window of 15 points identified persistent (green) and anti-persistent (magenta) segments, which corresponded well to the moving window velocity plots (Figure 3, lower panel), confirming that the neural network is indeed distinguishing passive states from active transport states with non-zero average velocity. We then used it to analyze the motility of two other endocytic compartments: SNX1-positive endosomes (Allison et al., 2017; Hunt et al., 2013) and lysosomes (Cabukusta and Neefjes, 2018; Hendricks et al., 2010). It successfully segmented tracks of GFP-SNX1 endosomes (Figure 3—figure supplement 1) in a stable MRC-5 cell line (Allison et al., 2017) and lysosomes visualized using lysobrite dye (Figure 3—figure supplement 2). A total of 63–71 MRC-5 cells were analyzed, giving 40,800 (GFP-Rab5 endosome), 11,273 (GFP-SNX1 endosome) and 38,039 (lysosome) tracks that were segmented into 277,926 (GFP-Rab5), 215,087 (GFP-SNX1) and 474,473 (lysosome) persistent or anti-persistent sections, each yielding a displacement, duration and average $H$.

![Figure 3.](https://cdn.elifesciences.org/articles/52224/elife-52224-fig3-v2.jpg)

**Figure 3.:** Top: Plot of displacement from a single trajectory in an MRC-5 cell (blue). Shaded areas show persistent (0.55 < H < 1 in green) and anti-persistent (0 < H < 0.45 in magenta) behaviour. Middle: A 15 point moving window DLFNN exponent estimate for the trajectory (black) with a line (dashed) marking diffusion H = 0.5 and two lines (dotted) marking confidence bounds for estimation marking H = 0.45 and 0.55. Bottom: Plot of instantaneous and moving (15 point) window velocity. Right: Plot of the trajectory with start and finish positions. Persistent (green) and anti-persistent (magenta) segments are shown. For sections that were 0.45 < H < 0.55 were not classified as persistent or anti-persistent and are depicted in blue.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/52224/elife-52224-fig3-figsupp1-v2.jpg)

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/52224/elife-52224-fig3-figsupp2-v2.jpg)

These data revealed intriguing similarities and differences in behavior between the three endocytic components. Analysis of the duration and displacement of segments (Appendix C) revealed that all organelles spent longer in anti-persistent than persistent states (Figure 4) but moved much further when persistent (Appendix 3—figure 1), as expected. However, GFP-SNX1 endosomes spent much less time than GFP-Rab5 endosomes or lysosomes in an anti-persistent state (Figure 4). This difference in behavior was also seen when histograms of the Hurst exponents were plotted (Figure 5), as SNX1 endosomes were much less likely to exhibit anti-persistent behavior, particularly with $H<0.3$, than Rab5 endosomes or lysosomes. This was confirmed by fitting the histograms of the Hurst exponent with a six component Gaussian mixture model (Figure 5b–d; Appendix D). In contrast, all three organelle classes exhibited a similar range of Hurst exponents when they underwent directionally persistent motion.

![Figure 4.](https://cdn.elifesciences.org/articles/52224/elife-52224-fig4-v2.jpg)

**Figure 4.:** Fit parameters can be found in Appendix 3—table 1.

![Figure 5.](https://cdn.elifesciences.org/articles/52224/elife-52224-fig5-v2.jpg)

**Figure 5.:** (a) Histograms of Hurst exponents for GFP-Rab5 (black), GFP-SNX1 (magenta) endosomes and lysosomes (green) plot on the same axes for comparison. The individual histograms of Hurst exponents (black solid) for GFP-Rab5-tagged endosomes, GFP-SNX1-tagged endosomes and lysosomes are shown in (b, c and d) respectively. For each histogram, the Gaussian mixture model fit for six components (red dashed) and individual Gaussian distribution components are shown on the same plot. The number of components were chosen through the Bayes information criterion shown in Appendix 4—figure 1.

To understand organelle motility in the context of cell behavior, an additional layer of complexity needs to be considered - the location of the moving structure within the cell itself. Such information would reveal zones that favor anti-persistent or persistent movement (Bálint et al., 2013). Using the neural network, trajectories of GFP-Rab5, GFP-SNX1 endosomes and lysosomes from MRC-5 cells were plotted with colors depicting the changing Hurst exponent at different points in each trajectory (Figure 6). For Rab5- and SNX1-positive endosomes, anti-persistent organelles were enriched in the cell periphery, but occasionally underwent long-range persistent movement towards the nucleus (Figure 6—video 1; Figure 6—video 2), as expected (Flores-Rodriguez et al., 2011; Zajac et al., 2013; Hunt et al., 2013; Allison et al., 2017). Lysosomes displayed completely different behavior, with most trajectories being anti-persistent, while the persistent trajectories were not obviously organized spatially (Figure 6; Figure 6—video 3). The location information together with classification of anti-persistent and persistent trajectories qualitatively shows the regions of high motor-driven activity within the cell for different endocytic organelles.

![Figure 6.](https://cdn.elifesciences.org/articles/52224/elife-52224-fig6-v2.jpg)

**Figure 6.:** The colours show the value of $H$ estimated by the neural network using a 15 point window. The scalebar is 10 µm.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/52224/elife-52224-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** MRC-5 cells were fixed and labeled with antibodies to Rab5 and SNX1, then imaged by confocal microscopy. A maximum-intensity z-projection of deconvolved images is shown. The boxed region is enlarged and presented as grey-scale single channels and a two color merged image. The scale bar is 10 µm (main image) and 2 µm (enlargements).

Many cargos that move along microtubules can switch their direction of motility, between dynein-driven inward (retrograde) motion toward the microtubule minus ends at the cell centre and plus-end-directed outward (anterograde) movement driven by kinesin family members (Hancock, 2014). To investigate the characteristics of anterograde and retrograde motility of endocytic organelles, we adapted our method to subdivide persistent segments according to whether the movement occurred towards or away from the user-defined centrosomal region (see Materials and methods). Only tracks with displacement of >0.5µm from their start point were selected, which yielded 2369 Rab5, 2099 SNX1 and 7645 lysosome persistent segments that were then analyzed to give the duration, displacement and velocity of anterograde and retrograde excursions (Figure 7; Table 1). The anti-persistent segments contained within these tracks were also analyzed.

![Figure 7.](https://cdn.elifesciences.org/articles/52224/elife-52224-fig7-v2.jpg)

**Figure 7.:** Any segment with $H>0.55$ was classed as persistent and $H<0.45$ as anti-persistent. These H values were chosen as a precaution against the mean error of the neural network estimation. Each data point within the box and whisker plots are averages of all trajectory segments in a single cell. A total of 65 MRC-5 cells for GFP-Rab5-tagged endosomes, 63 MRC-5 cells for SNX1-GFP-tagged endosomes and 71 MRC-5 cells for lysosomes were analysed with at least 5 to 500 (average 54) anterograde or retrograde segments for each cell.

**Table 1.**
 Statistics of experimental trajectory segments.The persistent and anti-persistent segments in this table are: from trajectories that travelled over 0.5 µm at any point from their initial starting positions; contained more points than the window size; and switched behavior more than twice in the trajectory. Note that these conditions are much stricter than those to generate Figures 4 and 5. Each persistent segment was then further subdivided into retrograde and anterograde segments (see Materials and methods).


<table>
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th>Rab5</th>
      <th>SNX1</th>
      <th>Lyso</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="2">Number of persistent segments</td>
      <td>2369</td>
      <td>2099</td>
      <td>7645</td>
    </tr>
    <tr>
      <td colspan="2">Number of anti-persistent segments</td>
      <td>6983</td>
      <td>3947</td>
      <td>19,320</td>
    </tr>
    <tr>
      <td colspan="2">Number of retrograde segments</td>
      <td>2925</td>
      <td>2343</td>
      <td>5882</td>
    </tr>
    <tr>
      <td colspan="2">Number of anterograde segments</td>
      <td>2303</td>
      <td>1609</td>
      <td>6827</td>
    </tr>
    <tr>
      <td rowspan="3">Anti-persistent displacement (µm)</td>
      <td>Mean</td>
      <td>0.05</td>
      <td>0.05</td>
      <td>0.03</td>
    </tr>
    <tr>
      <td>Median</td>
      <td>0.04</td>
      <td>0.05</td>
      <td>0.03</td>
    </tr>
    <tr>
      <td>St. Dev</td>
      <td>0.02</td>
      <td>0.01</td>
      <td>0.004</td>
    </tr>
    <tr>
      <td rowspan="3">Anti-persistent speed (µms-1)</td>
      <td>Mean</td>
      <td>0.82</td>
      <td>0.75</td>
      <td>0.10</td>
    </tr>
    <tr>
      <td>Median</td>
      <td>0.70</td>
      <td>0.73</td>
      <td>0.09</td>
    </tr>
    <tr>
      <td>St. Dev</td>
      <td>0.31</td>
      <td>0.19</td>
      <td>0.02</td>
    </tr>
    <tr>
      <td rowspan="3">Anti-persistent time (s)</td>
      <td>Mean</td>
      <td>0.23</td>
      <td>0.20</td>
      <td>0.93</td>
    </tr>
    <tr>
      <td>Median</td>
      <td>0.23</td>
      <td>0.19</td>
      <td>0.92</td>
    </tr>
    <tr>
      <td>St. Dev</td>
      <td>0.05</td>
      <td>0.03</td>
      <td>0.11</td>
    </tr>
    <tr>
      <td rowspan="3">Retrograde displacement (µm)</td>
      <td>Mean</td>
      <td>0.53</td>
      <td>0.74</td>
      <td>0.29</td>
    </tr>
    <tr>
      <td>Median</td>
      <td>0.49</td>
      <td>0.69</td>
      <td>0.29</td>
    </tr>
    <tr>
      <td>St. Dev</td>
      <td>0.19</td>
      <td>0.28</td>
      <td>0.08</td>
    </tr>
    <tr>
      <td rowspan="3">Retrograde speed (µms-1)</td>
      <td>Mean</td>
      <td>2.29</td>
      <td>1.35</td>
      <td>1.49</td>
    </tr>
    <tr>
      <td>Median</td>
      <td>2.21</td>
      <td>1.29</td>
      <td>1.46</td>
    </tr>
    <tr>
      <td>St. Dev</td>
      <td>0.87</td>
      <td>0.39</td>
      <td>0.25</td>
    </tr>
    <tr>
      <td rowspan="3">Retrograde time (s)</td>
      <td>Mean</td>
      <td>0.22</td>
      <td>0.46</td>
      <td>0.17</td>
    </tr>
    <tr>
      <td>Median</td>
      <td>0.21</td>
      <td>0.45</td>
      <td>0.17</td>
    </tr>
    <tr>
      <td>St. Dev</td>
      <td>0.09</td>
      <td>0.09</td>
      <td>0.03</td>
    </tr>
    <tr>
      <td rowspan="3">Anterograde displacement (µm)</td>
      <td>Mean</td>
      <td>0.35</td>
      <td>0.43</td>
      <td>0.31</td>
    </tr>
    <tr>
      <td>Median</td>
      <td>0.33</td>
      <td>0.37</td>
      <td>0.32</td>
    </tr>
    <tr>
      <td>St. Dev</td>
      <td>0.17</td>
      <td>0.20</td>
      <td>0.08</td>
    </tr>
    <tr>
      <td rowspan="3">Anterograde speed (µms-1)</td>
      <td>Mean</td>
      <td>2.06</td>
      <td>1.10</td>
      <td>1.51</td>
    </tr>
    <tr>
      <td>Median</td>
      <td>1.71</td>
      <td>1.08</td>
      <td>1.48</td>
    </tr>
    <tr>
      <td>St. Dev</td>
      <td>0.95</td>
      <td>0.30</td>
      <td>0.27</td>
    </tr>
    <tr>
      <td rowspan="3">Anterograde time (s)</td>
      <td>Mean</td>
      <td>0.18</td>
      <td>0.34</td>
      <td>0.18</td>
    </tr>
    <tr>
      <td>Median</td>
      <td>0.15</td>
      <td>0.33</td>
      <td>0.18</td>
    </tr>
    <tr>
      <td>St. Dev</td>
      <td>0.08</td>
      <td>0.08</td>
      <td>0.03</td>
    </tr>
  </tbody>
</table>

These statistics revealed that each endocytic organelle moved with different characteristics. GFP-Rab5 endosomes moved much faster than GFP-SNX1 endosomes or lysosomes, particularly in the retrograde direction (Figure 7, upper panel). Strikingly, although the GFP-SNX1 endosomes were slowest in both directions, they moved furthest and for longest in each segment, in keeping with the longer duration of persistent segments seen in the global analysis of tracks (Figure 4) and higher H values (Figure 5). The differences in behavior between Rab5 and SNX1 endosomes is intriguing, since both are recruited to the early endosome by the lipid phosphoinositol-3-phosphate (Christoforidis et al., 1999; Carlton et al., 2004; Behnia and Munro, 2005; Huotari and Helenius, 2011). However, SNX1 also senses membrane curvature (Carlton et al., 2004), and immunofluorescence labeling of MRC-5 cells with antibodies to Rab5 and SNX1 demonstrated that they reside on distinct domains of larger early endosomes (Figure 6—figure supplement 1), as expected van Weering et al. (2012). In addition, while SNX1 endosomes were usually Rab5-positive, there was a significant population of Rab5 endosomes that lacked SNX1, especially smaller early endosomes that were often located in the cell periphery. It is likely that this population of Rab5-positive, SNX1-negative endosomes is particularly motile. The high retrograde velocity of these endosomes might be explained by the recruitment of dynein to Rab5 endosomes via Hook family members (Bielska et al., 2014; Zhang et al., 2014; Schroeder and Vale, 2016; Guo et al., 2016). These dynein adaptors have the intriguing property of recruiting two dyneins per dynactin (Urnavicius et al., 2018; Grotjahn et al., 2018), leading to faster rates of movement in motility assays using purified protein than adaptors that only recruit one dynein per dynactin. Perhaps, SNX1 endosomes move more slowly than Rab5 endosomes because they use a ‘single-dynein’ adaptor. An alternative explanation could be that SNX1 endosomes are slowed down by interactions with the actin cytoskeleton, since SNX1 domains are enriched in the WASH complex, which in turn controls localized actin assembly (Gomez and Billadeau, 2009; Simonetti and Cullen, 2019). Actin might also contribute to the slow, steady motion of SNX1 endosomes via myosin motors or the formation of actin comets (Simonetti and Cullen, 2019). These interesting possibilities remain to be tested experimentally.

The analysis of anterograde and retrograde segments revealed that lysosomes moved at moderate speed, and were equally fast in both directions, but each burst of movement was short (Figure 7, upper panels). In addition, pauses were $\geq4$ times longer for lysosomes than either early endosome type (Figure 7, lower panels). Lysosomes also often changed direction of movement (e.g. Figure 3—figure supplement 2), as previously reported (Hendricks et al., 2010). So far, no activating dynein adaptor has been identified on lysosomes (Reck-Peterson et al., 2018), although several potential dynein interactors have been identified, such as RILP (Rab7 interacting lysosomal protein (Cabukusta and Neefjes, 2018). Whether this underlies the difference in motile behavior between lysosomes and early endosomes remains to be tested: however, a less active dynein could well contribute to frequent reversals in direction (Hancock, 2014).

### fBm with a stochastic Hurst exponent is a new possible intracellular transport model

fBm is a Gaussian process $B_{H}⁢(t)$ with zero mean and covariance $⟨B_{H}⁢(t)⁢B_{H}⁢(s)⟩∼t^{2⁢H}+s^{2⁢H}-(t-s)^{2⁢H}$, where the Hurst exponent, $H$ is a constant between 0 and 1. With the DLFNN providing local estimates of the Hurst exponent, the motion of endosomes and lysosomes can be described as fBm with a stochastic Hurst exponent, $H⁢(t)$. This is different to multifractional Brownian motion (Peltier and Lévy Véhel, 1995) where $H⁢(t)$ is a function of time. In our case, $H⁢(t)$ is itself a stochastic process and such a process has been considered theoretically (Ayache and Taqqu, 2005). This is the first application of such a theory to intracellular transport and opens a new method for characterizing vesicular movement. Furthermore, Figure 3 shows that the motion of a vesicle, $B_{H}⁢(t)$, exhibits regime switching behavior between persistent and anti-persistent states.

We found that the times that lysosomes and endosomes spend in a persistent and anti-persistent state are heavy-tailed (Figure 4). These times are characterized by the probability densities $ψ⁢(t)∼t^{-\mu-1}$, where anti-persistent states have 0 < µ < 1 and persistent states have 1 < µ < 2. Extensive plots and fittings are shown in Figure 4 and Appendix C. In fact, the residence time probability density has an infinite mean to remain in an anti-persistent state ($0<H⁢(t)<1/2$) but in persistent states ($1/2<H⁢(t)<1$) the mean of the residence time probability density is finite and the second moment is infinite. This implies that the vesicles may have a biological mechanism to prioritize certain interactions within the complex cytoplasm, similar to ecological searching patterns (Reynolds and Rhodes, 2009), mRNPs song2018neuronal, swarming bacteria (Ariel et al., 2015) and how human dynamics are often heavy tailed and bursty (Barabási, 2005).

### Conclusions

We developed a Deep Learning Feedforward Neural Network trained on fBm that estimates accurately the Hurst exponent for heterogeneous trajectories. Estimating the Hurst exponent using a DLFNN is not only more accurate than conventional methods but also enables direct trajectory segmentation without a drastic increase in computational cost. We package this DLFNN analysis code into a user-friendly application, which can predict the Hurst exponent with consistent accuracy for as few as seven consecutive data points. This is useful to biologists since major limitations to trajectory analysis are: the brevity of tracks due to the fact that particles may rapidly switch between motile states or move out of the plane of focus; the rapid nature of some biochemical reactions; and the bleaching of fluorescent probes (with non-bleaching probes often being bulky or cytotoxic). This method can be used to detect persistent and anti-persistent states of motion purely from the positional data of trajectories and removes the prerequisite of time or ensemble averaging for effective heterogeneous transport characterization.

The DLFNN enabled us to discover regime switching in lysosome and endosome movement that can be modeled by fBm with a stochastic Hurst exponent. This interpretation is a unified approach to describe motion with anti-persistence and persistence varying over time. Furthermore, the residence time of vesicles in a persistent or anti-persistent state is found to be heavy tailed, which implies that endosomes and lysosomes possess biological mechanisms to prioritize varying biological processes similar to ecological searching patterns (Reynolds and Rhodes, 2009), mRNPs song2018neuronal, swarming bacteria (Ariel et al., 2015) and even human dynamics (Barabási, 2005). Importantly, applying this method to identify and analyze the anterograde and retrograde motility reveals unexpected differences in behavior between closely-related organelles. Finally, in addition to providing a new segmentation method of active and passive transport, this new technique distinguishes the difference in motility between lysosomes, Rab5-positive endosomes and SNX1 positive endosomes. The results suggest that the manner in which these vesicles move is dependent on their identity within the endocytic pathway, especially when the motion is anti-persistent. This implies that directionality and the correlation between consecutive steps is important to measure in addition to the displacement, velocity and duration of movement. There is considerable scope for using these methods to identify changes in motility of different organelles caused by disease. We hope that this type of analysis will allow discoveries in particle motility of a more refined nature and make applying anomalous transport theory more accessible to researchers in a wide variety of disciplines.

## Materials and methods

**Key resources table**


<table>
  <thead>
    <tr>
      <th>Reagent type or resource</th>
      <th>Designation</th>
      <th>Source</th>
      <th>Identifiers</th>
      <th>Additional information</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>Lung fibroblast line</td>
      <td>Allison et al., 2017 https://doi.org/10.1083/jcb.201609033</td>
      <td>GFP-SNX1-MRC5</td>
      <td>MRC5 cell line stably expressing GFP-SNX1. Mycoplasma free.</td>
    </tr>
    <tr>
      <td>Cell line (H. sapiens)</td>
      <td>Lung fibroblast line</td>
      <td>Other</td>
      <td>GFP-Rab5-MRC5</td>
      <td>MRC5 cell line stably expressing GFP-Rab5 generated by retroviral transduction by G. Pearson and E. Reid, University of Cambridge. Mycoplasma free.</td>
    </tr>
    <tr>
      <td>Cell line (H. sapiens)</td>
      <td>MRC-5 SV1 TG1 Lung fibroblast line</td>
      <td>ECACC</td>
      <td>MRC-5 SV1 TG1 cells, cat no. 85042501</td>
      <td>Mycoplasma free.</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-human Rab5A Rabbit monoclonal</td>
      <td>Cell Signalling Technology</td>
      <td>3547S</td>
      <td>IF(1/200)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-human sorting nexin 1 (mouse monoclonal)</td>
      <td>BD Biosciences</td>
      <td>611482</td>
      <td>IF(1/200)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Alexa594-conjugated anti-mouse IgG (donkey polyclonal)</td>
      <td>Jackson ImmunoResearch</td>
      <td>715-585-150</td>
      <td>IF(1/400)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>A488-conjugated donkey anti-rabbit IgG</td>
      <td>Jackson Immunoresearch</td>
      <td>711-545-152</td>
      <td>IF(1/400)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pLXIN-GFP-Rab5C-I-NeoR</td>
      <td>Other</td>
      <td></td>
      <td>Used by G. Pearson and E. Reid, University of Cambridge to generate retrovirus containing GFP-Rab5C</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Hpa1 GFP Forward</td>
      <td>Other</td>
      <td>PCR primer</td>
      <td>Used by G. Pearson and E. Reid, University of Cambridge to generate retrovirus containing GFP-Rab5C. TAGGGAGTTAACATGGTGAGCAAGGGCGAGGA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Not1 Rab5C Reverse</td>
      <td>Other</td>
      <td>PCR primer</td>
      <td>Used by G. Pearson and E. Reid, University of Cambridge to generate retrovirus containing GFP-Rab5C . ATCCCTGCGGCCGCTCAGTTGCTGCAGCACTGGC</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>DAPI</td>
      <td>Biolegend</td>
      <td>422801</td>
      <td>IF (1 µg/mL)</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Prolong Gold</td>
      <td>ThermoFisher</td>
      <td>P36930</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Lysobrite Red</td>
      <td>AAT Bioquest</td>
      <td>22645</td>
      <td>(1/2500)</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Geneticin (G418)</td>
      <td>Sigma-Aldrich</td>
      <td>G1397</td>
      <td>200 µg/mL to maintain GFP-Rab5-MRC5 and GFP-SNX1-MRC5 cells in culture.</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Formaldehyde solution, 37% (wt/v)</td>
      <td>Sigma-Aldrich</td>
      <td>252549</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Triton X-100</td>
      <td>Anatrace</td>
      <td>T1001</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>NNT (aitracker.net)</td>
      <td>Newby et al., 2018</td>
      <td>AITracker</td>
      <td>Web-based automated tracking service</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Metamorph</td>
      <td>Molecular Devices LLC</td>
      <td>Metamorph</td>
      <td>Metamorph Microscopy Automation and Image Analysis Software</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>FIJI</td>
      <td>Schindelin, J.; Arganda-Carreras, I. and Frise, E. et al. (2012) ,‘Fiji: an open-source platform for biological-image analysis’, Nature methods 9 (7): 676–682, PMID22743772, doi:10.1038/nmeth.2019</td>
      <td>FIJI/ImageJ</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>DLFNN Exponent Estimator</td>
      <td>Han, Daniel. (2020, January 20). DLFNN Exponent Estimator (Version 0). http://doi.org/10.1101/777615</td>
      <td>DLFNN/DLFNN Exponent Estimator</td>
      <td>Hurst exponent estimator with Deep Learning Feed-forward Neural Network application for Windows 10. Documentation included.</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Python3</td>
      <td>Python Software Foundation.Python Language Reference 3.7. Available at www.python.org</td>
      <td>Python/Python3</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>SciPy</td>
      <td>Virtanen et al. (2020) SciPy 1.0: Fundamental Algorithms for Scientific Computing in Python. Nature Methods, in press.</td>
      <td>SciPy/scipy</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Tensorflow</td>
      <td>Abadi et al., 2016</td>
      <td>Tensorflow</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Keras</td>
      <td>Chollet, François and others. ‘Keras.' (2015). Available from https://keras.io</td>
      <td>Keras</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>fbm</td>
      <td>Flynn, Christopher, fbm 0.3.0 available for download at https://pypi.org/project/fbm/ or https://github.com/crflynn/fbm</td>
      <td>FBM package in Python</td>
      <td>Exact methods for simulating fractional Brownian motion (fBm) or fractional Gaussian noise (fGn) in python. Approximate simulation of multifractional Brownian motion (mBm) or multifractional Gaussian noise (mGn).</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>35 mm glass-bottomed dishes (µ-Dish)</td>
      <td>Ibidi</td>
      <td>Cat. No. 81150</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Hurst exponent estimation methods

Time averaged MSDs were calculated using

$$
⟨x^{2}⁢(n⁢\delta⁢t)⟩=\frac{1}{N-n}⁢\summ=0N-n[x⁢((m+n)⁢\delta⁢t)-x⁢(m⁢\delta⁢t)]^{2}
$$

where $x⁢(n⁢\delta⁢t)$ is the track displacement at time $n⁢\delta⁢t$ and a track contains $N$ coordinates spaced at regular time intervals of $\delta⁢t$. From now on, $⟨x⟩$ will denote the time average of $x$ unless explicitly specified otherwise. The total time is $T=(N-1)⁢\delta⁢t$ and $n=1,2,…,N-1$. Lag-times are the set of possible $n⁢\delta⁢t$ within the data set and $⟨x^{2}⁢(n⁢\delta⁢t)⟩$ was then fit to a power-law $∼t^{2⁢H}$ using the ‘scipy.optimize’ package in Python3 to estimate the exponent $H$.

Rescaled ranges were calculated by creating a mean adjusted cumulative deviate series $z⁢(n⁢\delta⁢t)=\sum_{m=0}^{n}x⁢(m⁢\delta⁢t)-⟨x⟩$ from original displacements $x⁢(n⁢\delta⁢t)$ and mean displacement $⟨x⟩$. Then the rescaled range is calculated by

$$
[R/S]⁢(n⁢\delta⁢t)=\frac{max⁢({z}_{n})-min⁢({z}_{n})}{\sqrt{\frac{1}{n⁢\delta⁢t}⁢\sum_{m=0}^{n}(x⁢(m⁢\delta⁢t)-⟨x⁢(n⁢\delta⁢t)⟩)^{2}}}
$$

where ${z}_{n}=z⁢(0),z⁢(\delta⁢t),z⁢(2⁢\delta⁢t),…,z⁢(n⁢\delta⁢t)$. The rescaled range is then fitted to a power law $[R/S]⁢(n⁢\delta⁢t)∼(n⁢\delta⁢t)^{H}$ where $H$ is the Hurst (1951). The ‘compute_Hc’ function in the ‘hurst’ package in Python3 estimates the Hurst exponent in this way.

Sequential ranges are defined as

$$
M⁢(n⁢\delta⁢t)=sup0\leqs\leqn⁢\delta⁢t⁡(x⁢(s)-x⁢(0))-inf0\leqs\leqn⁢\delta⁢t⁡(x⁢(s)-x⁢(0))
$$

where $sup⁡(x)$ is the supremum and $inf⁡(x)$ is the infimum for the set $x$ of real numbers. Then $M⁢(n⁢\delta⁢t)=(n⁢\delta⁢t)^{H}⁢M⁢(\delta⁢t)$ Feller (1951).

### DLFNN structure and training

The fractional Brownian trajectories were generated using the Hosking method within the ‘FBM’ function available from the ‘fbm’ package in Python3. The DLFNN was built using Tensorflow Abadi et al. (2016) and Keras Chollet (2015) in Python3 and trained by using the simulated fractional Brownian trajectories. The training and testing of the neural network were performed on a workstation PC equipped with 2 CPUs with 32 cores (Intel(R) Xeon CPU E5-2640 v3) and 1 GPU (NVIDIA Tesla V100 with 16 GB memory). The structure of the neural network was a multilayer, feedforward neural network where all nodes of the previous layer were densely connected to nodes of the next layer. Each node had a ReLU activation function and the parameters were optimized using the RMSprop optimizer (see Keras documentation Chollet, 2015). Three separate structures were explored and examples of these structures for two hidden layers and five time point inputs are shown in Figure 1g,h and i. The triangular structure was predominantly used since this was the least computationally expensive and accuracy between different structures were similar. To compare the accuracy of different methods, the mean absolute error ($\sigma_{H}$) of $N$ trajectories, $\sigma_{H}=\sum_{m=1}^{N}(H_{n}^{s⁢i⁢m}-H_{n}^{e⁢s⁢t})/N$, was used. Before inputting values into the neural network, the time series was differenced to make it stationary. The input values of a fBm trajectory ${x}=x_{0},x_{1},…,x_{n}$ were differenced and normalized so that ${x_{i⁢n⁢p⁢u⁢t}}=(x_{1}-x_{0})/range⁢(x),(x_{2}-x_{1})/range⁢(x),…,(x_{n}-x_{n-1})/range⁢(x)$. Since the model requires differenced and normalized input values, in theory it should be applicable to a wide range of datasets. However, further testing must be done in order to confirm this expectation.

### Gaussian kernel density estimation

Kernel density estimation (KDE) is a non-parametric method to estimate the probability density function (PDF) of random variables. If $N$ random variables $x_{n}$ are distributed by an unknown density function $P⁢(x)$, then the kernel density estimate $P⁢(x)$ is

$$
P^⁢(x)=\frac{1}{N}⁢\sumn=1NK⁢(\frac{x-x_{n}}{l})
$$

where $K⁢(⋅)$ is the kernel function and $l$ is the bandwidth. In this paper, we have used a Gaussian KDE, $K⁢(y)=\frac{1}{\sqrt{2⁢\pi}}⁢e^{-y^{2}/2}$, to estimate the two dimensional PDFs of the second and bottom row in Figure 1a. This was performed in Python3 using ‘scipy.stats.gaussian_kde’ and Scott’s rule of thumb for bandwidth selection.

### Segmenting trajectories into persistent and anti-persistent segments

From the estimates of Hurst exponent from the DLFNN, trajectories were segmented into persistent and anti-persistent segments. Given an experimental trajectory $x=x_{0},x_{1},…,x_{n}$ and window of length $N_{w}$ (an odd number) starting at $x_{i}$, we obtain the $H$ estimate for the position at $x_{j}$, where $j=i+(N_{w}-1)/2$. This will give us a series of $H_{t}$ values, $H_{(N_{w}-1)/2},H_{(N_{w}-1)/2+1},…,H_{n-(N_{w}-1)/2}$, which correspond to the positions, $x_{(N_{w}-1)/2},x_{(N_{w}-1)/2+1},…,x_{n-(N_{w}-1)/2}$. Then, the values $H_{t}$ can be segmented into consecutive points of persistence $H_{t}>0.55$ and anti-persistence $H_{t}<0.45$. The bounding values, 0.55 and 0.45, were used since the mean error of the DLFNN estimation method was $\sigma_{H}∼0.05$. Any segment less than the length of $N_{w}$ was discarded as a precaution against spurious detection.

### Directional segmentation of persistent segments

Once segments of persistence and anti-persistence were defined, we measured the displacement, time and velocity of these segments, shown in the bottom row of Figure 7 and Table 1. The persistent segments were filtered to be only from trajectories that travelled over 0.5 µm; contained more points than the window size; and switched behaviour more than twice in the trajectory. In addition, we assessed if persistent segments were anterograde or retrograde in direction. In order to do this, the centrosomal region was defined by the user as the point where the lysosomes, Rab5 and SNX1 organelles were the largest, brightest, or the most clustered. Image contrast enhancements, such as histogram equalization, were used to locate the centrosomes. By locating the centrosomal region and the cell boundary from user input, the persistent segments can then be classified as anterograde or retrograde. This was done by finding the cosine of the angles, $cos⁡(\theta)$, between the vector, $r→_{0,i}$, from the centrosome to the current particle position $x_{i}$ and the vector, $r→_{i,i+1}$, from the current particle position to the next particle position $x_{i+1}$. The exact formula is $cos⁡(\theta)=r→_{0,i}⋅r→_{i,i+1}/|r→_{0,i}|⁢|r→_{i,i+1}|$. Using windows in a similar fashion as determining persistent and anti-persistent segments, $cos⁡(\theta_{i})$ corresponding to position $x_{i}$ was found for the points within a persistent segment. If $cos⁡(\theta_{i})>\sigma_{cos⁡(\theta)}$, then the motion was deemed to be anterograde and if $cos⁡(\theta_{i})<-\sigma_{cos⁡(\theta)}$, retrograde. Sweeping through the points of $x_{i}$, consecutive retrograde or anterograde points formed segments from the persistent segments. A threshold of $\sigma_{cos⁡(\theta)}=0.3$ was used.

### Cell lines

The MRC-5 SV1 TG1 Lung fibroblast cell line was purchased from ECACC. MRC-5 cell lines stably expressing GFP-Rab5C and GFP-SNX1 were kindly provided by Drs. Guy Pearson and Evan Reid (Cambridge Institute for Medical Research, University of Cambridge). The GFP-SNX1 cell line has been previously described in Allison et al. (2017). Cell lines were routinely tested for mycoplasma infection. To generate the MRC-5 GFP-Rab5C stable cell line, GFP-Rab5C was PCRed from pIRES GFP-Rab5C Seaman (2004) using ‘Hpa1 GFP Forward’ (TAGGGAGTTAACATGGTGAGCAAGGGCGAGGA) and ‘Not1 Rab5C Reverse’ (ATCCCTGCGGCCGCTCAGTTGCTGCAGCACTGGC) oligonucleotide primers. The GFP-Rab5C PCR product and a pLXIN-I-NeoR plasmid were digested using Hpa1 (New England Biolabs - R0105) and Not1 (New England Biolabs - R3189) restriction enzymes. The GFP-Rab5C PCR product was then ligated into the digested pLXIN-I-NeoR using T4 DNA Ligase (New England Biolabs - M0202). The ligated plasmid was amplified in bacteria selected with ampicillin and verified using Sanger Sequencing. To generate the GFP-Rab5C MRC-5 cell line, Phoenix retrovirus producer HEK293T cells were transfected with the pLXIN-GFP-Rab5C-I-NeoR plasmid to generate retrovirus containing GFP-Rab5C. MRC-5 cells were inoculated with the virus, and successfully transduced cells were selected using 200 µg/mL Geneticin (G418 - Sigma-Aldrich G1397). Cells used for imaging were not clonally selected.

### Live-imaging and tracking

Stably expressing MRC-5 cells were co-stained with LysoBrite Red (AAT Bioquest), imaged live using fluorescence microscopy and tracked with NNT aitracker.net; Newby et al. (2018). The cells were grown in MEM (Sigma Life Science) and 10% FBS (HyClone) and incubated for 48 hr at 37 in 5% CO2 on 35 mm glass-bottomed dishes (µ-Dish, Ibidi, Cat. No. 81150). For LysoBrite staining, LysoBrite was diluted 1 in 500 with Hank’s Balanced Salt solution (Sigma Life Science). Then 0.5 mL of this solution was added to cells on a 35 mm dish containing 2 mL of growing media and incubated at 37 for at least 1 hr. Cells were then washed with sterile PBS and the media replaced with growing media.

After at least 6 hr incubation, the growing media was replaced with live-imaging media composed of Hank’s Balanced Salt solution (Sigma Life Science, Cat. No. H8264) with added essential and non-essential amino acids, glutamine, penicillin/streptomycin, 25 mM HEPES (pH 7.0) and 10% FBS (HyClone). Live-cell imaging was performed on an inverted Olympus IX71 microscope with an Olympus 100 × 1.35 oil PH3 objective. Samples were illuminated using an OptoLED (Cairn Research) light source with 470 nm and white LEDs. For GFP, a 470 nm LED and Chroma ET470/40 excitation filter was used in combination with a Semrock FITC-3540C filter set. For Lysobrite-Red, a white light LED, Chroma ET573/35 was used with a dualband GFP/mCherry dichroic and an mCherry emission filter (ET632/60). GFP-Rab5-labeled endosomes were imaged in a total of 65 cells, from three independent experiments. GFP-SNX1-labeled endosomes were imaged in a total of 63 cells from four independent experiments. Lysosomes were imaged in separate experiments, with 71 cells imaged from three independent repeats. A stream of 20 ms exposures was collected with a Prime 95B sCMOS Camera (Photometrics) for 17 s using Metamorph software while the cells were kept at 37 (in atmospheric CO2 levels). The endosomes and lysosomes in the videos were then tracked using an automated tracking software (AITracker) Newby et al. (2018).

### Confocal imaging

To compare the localization of SNX1 and Rab5, GFP-Rab5-MRC-5 cells were grown on #1.5 coverslips and then fixed in 3% (w/v) formaldehyde in PBS for 20 min at room temperature (RT). Coverslips were washed twice in PBS, quenched in PBS with glycine, then permeabilized by incubation for 5 min in 0.1% Triton X-100. After another wash in PBS, coverslips were labeled with antibodies to SNX1 and Rab5 for 1 h at RT, washed three times in PBS, then labeled with Alexa488-donkey anti-rabbit and Alexa594-donkey anti-mouse antibodies in 1 µg/mL DAPI in PBS for 30 min. After three PBS washes, coverslips were dipped in deionized water, air-dried and mounted on slides using Prolong Gold.

Images were collected on a Leica TCS SP8 AOBS inverted confocal using a 100x/1.40 NA PL apo objective. The confocal settings were as follows: pinhole, one airy unit; scan speed 400 Hz unidirectional; format 2048 × 2048. Images were collected using hybrid detectors (A488 and A594) or a PMT (DAPI) with these detection mirror settings; [Alexa488, 498 nm-577 nm; Alexa594, 602 nm-667 nm; DAPI, 420 nm-466 nm] using the SuperK Extreme supercontinuum white light laser for 488 nm (10.5%) and 594 nm (5%) excitation, and a 405 nm laser (5%) for DAPI. Images were collected sequentially to eliminate cross-talk between channels. When acquiring 3D optical stacks the confocal software was used to determine the optimal number of Z sections. The data were deconvolved using Huygens software before generating maximum intensity projections of 3D stacks using FIJI.

### Software and code

The code and documentation for determining the Hurst exponent can be found in https://github.com/dadanhan/hurst-exp (copy archived at https://github.com/elifesciences-publications/hurst-exp; Han, 2019) and a GUI is available on https://zenodo.org/record/3613843#.XkPf2Wj7SUl.
