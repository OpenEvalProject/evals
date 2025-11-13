# Bayesian machine learning analysis of single-molecule fluorescence colocalization images

## Authors

- Yerdos A Ordabayev<sup>1</sup> ([ORCID: 0000-0002-1493-9364](https://orcid.org/0000-0002-1493-9364))
- Larry J Friedman<sup>1</sup> ([ORCID: 0000-0003-4946-8731](https://orcid.org/0000-0003-4946-8731))
- Jeff Gelles<sup>1</sup> ([ORCID: 0000-0001-7910-3421](https://orcid.org/0000-0001-7910-3421)) †
- Douglas L Theobald<sup>1</sup> ([ORCID: 0000-0002-2695-8343](https://orcid.org/0000-0002-2695-8343)) †

### Affiliations

1. Department of Biochemistry, Brandeis University Waltham United States ([ROR:05abbep66](https://ror.org/05abbep66))

† Corresponding author

## Abstract

Multi-wavelength single-molecule fluorescence colocalization (CoSMoS) methods allow elucidation of complex biochemical reaction mechanisms. However, analysis of CoSMoS data is intrinsically challenging because of low image signal-to-noise ratios, non-specific surface binding of the fluorescent molecules, and analysis methods that require subjective inputs to achieve accurate results. Here, we use Bayesian probabilistic programming to implement Tapqir, an unsupervised machine learning method that incorporates a holistic, physics-based causal model of CoSMoS data. This method accounts for uncertainties in image analysis due to photon and camera noise, optical non-uniformities, non-specific binding, and spot detection. Rather than merely producing a binary ‘spot/no spot’ classification of unspecified reliability, Tapqir objectively assigns spot classification probabilities that allow accurate downstream analysis of molecular dynamics, thermodynamics, and kinetics. We both quantitatively validate Tapqir performance against simulated CoSMoS image data with known properties and also demonstrate that it implements fully objective, automated analysis of experiment-derived data sets with a wide range of signal, noise, and non-specific binding characteristics.

## Introduction

A central concern of modern biology is understanding at the molecular level the chemical and physical mechanisms by which protein and nucleic acid macromolecules perform essential cellular functions. The operation of many such macromolecules requires that they work not as isolated molecules in solution but as components of dynamic molecular complexes that self-assemble and change structure and composition as they function. For more than two decades, scientists have successfully explored the molecular mechanisms of many such complex and dynamic systems using multi-wavelength single molecule fluorescence methods such as smFRET (single-molecule fluorescence resonance energy transfer) (Roy et al., 2008) and multi-wavelength single-molecule colocalization methods (CoSMoS, colocalization single molecule spectroscopy) (Larson et al., 2014; van Oijen, 2011; Friedman and Gelles, 2012).

CoSMoS is a technique to measure the kinetics of dynamic interactions between individual molecules. The CoSMoS method has been used for elucidating the mechanisms of complex biochemical processes in vitro. Examples include cell cycle regulation (Lu et al., 2015b), ubiquitination and proteasome-mediated protein degradation (Lu et al., 2015a), DNA replication (Geertsema et al., 2014; Ticau et al., 2015), transcription (Zhang et al., 2012; Friedman and Gelles, 2012; Friedman et al., 2013), micro-RNA regulation (Salomon et al., 2015), pre-mRNA splicing (Shcherbakova et al., 2013; Krishnan et al., 2013; Warnasooriya and Rueda, 2014), ribosome assembly (Kim et al., 2014), translation (Wang et al., 2015; Tsai et al., 2014; O’Leary et al., 2013), signal recognition particle-nascent protein interaction (Noriega et al., 2014), and cytoskeletal regulation (Smith et al., 2013; Breitsprecher et al., 2012).

Figure 1A illustrates an example CoSMoS experiment to measure the interaction kinetics of RNA polymerase II molecules with DNA. In the experiment (Rosen et al., 2020), we first measured the locations of individual DNA molecules (the ‘targets’) tethered to the surface of an observation chamber at low density. Next, a cell extract solution containing fluorescent RNA polymerase II molecules (the ‘binders’) was added to the solution over the surface and the chamber surface was imaged by total internal reflection fluorescence (TIRF) microscopy. When the binder molecules are freely diffusing in solution, they are not visible in TIRF. In contrast, when bound to a target, a single binder molecule is detected as a discrete fluorescent spot colocalized with the target position (Friedman et al., 2006; Friedman and Gelles, 2015).

![Figure 1.](https://cdn.elifesciences.org/articles/73860/elife-73860-fig1-v2.jpg)

**Figure 1.:** (A) Experiment schematic. DNA target molecules labeled with a blue-excited fluorescent dye (blue star) are tethered to the microscope slide surface. RNA polymerase II (Pol II) binder molecules labeled with a green-excited dye (green star) are present in solution. (B) Data collection and preprocessing. After collecting a single image with blue excitation to identify the locations of the DNA molecules, a time sequence of Pol II images was collected with green excitation. Preprocessing of the images includes mapping of the corresponding points in target and binder channels, drift correction, and identification of two sets of areas of interest (AOIs). One set corresponds to locations of target molecules (e.g., purple square); the other corresponds to locations where no target is present (e.g., yellow square). (C) On-target data. Data are time sequences of 14 × 14 pixel AOI images centered at each target molecule. Frames show presence of on-target (e.g., frame 630) and off-target (e.g., frame 645) Pol II molecules. (D) Off-target control data. Control data consists of images collected from randomly selected sites at which no target molecule is present. Such sites can be AOIs in which no fluorescent target molecule is visible (e.g., the yellow square in the DNA channel shown in B). Alternatively, control data can be taken from a recording of a separate control sample to which no target molecules were added. Image data in B, C, and D is from Data set A in Table 1.

Effective data analysis is a major challenge in the use of the CoSMoS technique. The basic goal is to acquire information at each time point about whether a binder molecule fluorescence spot is observed at the image position of a target molecule (e.g., whether a colocalized green-dye-labeled RNA polymerase II is observed at the surface location of a blue-dye-labeled DNA spot in Figure 1B). Although CoSMoS images are conceptually simple – they consist only of diffraction-limited fluorescent spots collected in several wavelength channels – efficient analysis of the images is inherently challenging. The number of photons emitted by a single fluorophore is limited by fluorophore photobleaching. Consequently, it is desirable to work at the lowest feasible excitation power in order to maximize the duration of experimental recordings and to efficiently capture relevant reaction events. Achieving higher time resolution divides the number of emitted photons between a larger number of images, so that photon shot noise ordinarily dominates the data statistics. Furthermore, the required concentrations of binder molecules can sometimes create significant background noise (Peng et al., 2018; van Oijen, 2011), even with zero-mode waveguide instruments (Chen et al., 2014). These technical difficulties frequently result in CoSMoS images that have low signal-to-noise ratios (SNR), making discrimination of colocalized fluorescence spots from noise a significant challenge. In addition, there are usually non-specific interactions of the binder molecule with the chamber surface, and these artefacts can give rise to both false positive and false negative spot detection (Friedman and Gelles, 2015). Together, these defects in analyzing spot colocalization interfere with the interpretation of CoSMoS data to measure reaction thermodynamics and kinetics and to infer molecular mechanisms.

Most CoSMoS spot detection methods are based on integrating the binder fluorescence intensity by summing the pixel values in small regions of the image centered on the location of individual target molecules, and then using crossings of an intensity threshold to score binder molecule arrival and departure, e.g., (Friedman and Gelles, 2012; Shcherbakova et al., 2013). However, integration discards data about the spatial distribution of intensity that can (and should) be used to distinguish authentic on-target spots from artefacts caused by noise or off-target binding. More recently, improved methods (Friedman and Gelles, 2015; Smith et al., 2019) were developed that directly analyze TIRF images, using the spatial distribution of binder fluorescence intensity around the target molecule location. All these methods, whether image- or integrated intensity-based, make a binary decision about the presence or absence of a binder spot at the target location. Treating all such binary decisions as equal neglects differences in the confidence of each spot detection decision caused by variations in noise, signal intensity, and non-specific binding. Failure to account for spot confidence decreases the reliability of downstream thermodynamic and kinetic analysis.

In this paper, we describe a qualitatively different Bayesian machine learning method for analysis of CoSMoS data implemented in a computer program, Tapqir (Kazakh: clever, inventive; pronunciation: tap-keer). Tapqir analyzes two-dimensional image data, not integrated intensities. Unlike prior methods, our approach is based on an explicit, global causal model for CoSMoS image formation and uses variational Bayesian inference (Kinz-Thompson et al., 2021; Gelman et al., 2013) to determine the values of model parameters and their associated uncertainties. This model, which we call ‘cosmos’, implements time-independent analysis of single-channel (i.e., one-binder) data sets. The cosmos model is physics-informed and includes realistic shot noise in fluorescent spots and background, camera noise, the size and shape of spots, and the presence of both target-specific and nonspecific binder molecules in the images. Most importantly, instead of yielding a binary spot-/no-spot determination, the algorithm calculates the probability of a target-specific spot being present at each time point and target location. The calculated probability can then be used in subsequent analyses of the molecular thermodynamics and kinetics. Unlike alternative approaches, Tapqir and cosmos do not require subjective threshold settings so they can be used effectively and accurately by non-expert analysts. The program is implemented in the Python-based probabilistic programming language Pyro (Bingham et al., 2019), which enables efficient use of graphics processing unit (GPU)-based hardware for rapid parallel processing of data and facilitates future modifications to the model.

## Results

### Data analysis pipeline

The initial steps in CoSMoS data analysis involve preprocessing the data set (Figure 1B) to map the spatial relationship between target and binder images, correct for microscope drift (if any) and list the locations of target molecules. Software packages that perform these preprocessing steps are widely available (e.g., Friedman and Gelles, 2015; Smith et al., 2019).

The input into Tapqir consists of the time sequence of images (Figure 1B, right). For colocalization analysis, it is sufficient to consider the image area local to the target molecule. This analyzed area of interest (AOI) needs to be several times the diameter of a diffraction-limited spot to include both the spot and the surrounding background (Figure 1C).

In addition to AOIs centered at target molecules, it is useful to also select negative control AOIs from randomly selected sites at which no target molecule is present (Figure 1B and D). In Tapqir, such off-target control data is analyzed jointly with on-target data and serves to estimate the background level of target-nonspecific binding.

Once provided with the preprocessing data and image sequence, Tapqir computes for each frame of each AOI the probability, $p(specific)$, that a target-specific fluorescence spot is present. The $p(specific)$ values that are output can then be used to extract information about the kinetics and thermodynamics of the target-binder interaction.

### Bayesian image classification analysis

Tapqir calculates $p(specific)$ values using an objective image classification method built on a rigorous Bayesian statistical approach to the CoSMoS image analysis problem. The Bayesian approach has three components. First, we define a probabilistic model of the CoSMoS images. The probabilistic model, cosmos, is a mathematical formalism that describes the AOI images in terms of a set of parameter values. The model is probabilistic in that each parameter is specified to have a probability distribution that defines the likelihood that it can take on particular values. Model parameters describe physically realistic image features such as the characteristic fluorescence spot width. Second, we specify prior distributions for the parameters of the model. These priors embed pre-existing knowledge about the CoSMoS experiment, such as the fact that target-specific spots will be close to the target molecule locations. Third, we infer the values of the model parameters, including $p(specific)$, using Bayes’ rule (Bishop, 2006; Kinz-Thompson et al., 2021). The cosmos model is ‘time-independent’, meaning that we ignore the time dimension of the recording – the order of the images does not affect the results.

### Probabilistic image model and parameters

A single AOI image from a CoSMoS data set is a matrix of noisy pixel intensity values. In each image, multiple binder molecule fluorescence spots can be present. Figure 2A shows an example image where two spots are present; one spot is located near the target molecule at the center of the image and another is off-target.

![Figure 2.](https://cdn.elifesciences.org/articles/73860/elife-73860-fig2-v2.jpg)

**Figure 2.:** (A) Example AOI image (from Data set A in Table 1). The AOI image is a matrix of 14 × 14 pixel intensities which is shown here as both a 2-D grayscale image and as a 3-D intensity plot. The image contains two spots; one is centered at target location (image center) and the other is located off-target. (B) Examples of four idealized noise-free image representations ($\mu^{I}$). Image representations consist of zero, one, or two idealized spots ($\mu^{S}$) superimposed on a constant background ($b$). Each fluorescent spot is represented as a 2-D Gaussian parameterized by integrated intensity ($h$), width ($w$), and position ($x$, $y$). The presence of spots is encoded in the binary spot existence indicator $m$. (C) Simulated idealized images illustrating different values of the target-specific spot state parameter $z$ and index parameter $\theta$. $\theta$ = 0 corresponds to a case when no specifically bound molecule is present ($z$ = 0); $\theta$ = 1 or 2 corresponds to the cases in which specifically bound molecule is present ($z$ = 1) and corresponds to spot 1 or 2, respectively. (D) Condensed graphical representation of the cosmos probabilistic model. Model parameters are depicted as circles and deterministic functions as diamonds. Observed image ($D$) is represented by a shaded circle. Related nodes are connected by edges, with an arrow pointing towards the dependent node (e.g., the shape of each 2-D Gaussian spot $\mu^{S}$ depends on spot parameters $m$, $h$, $w$, $x$, and $y$). Plates (rounded rectangles) contain entities that are repeated for the number of instances displayed at the bottom-right corner: number of total AOIs ($N+N_{c}$), frame count ($F$), and maximum number of spots in a single image ($K$ = 2). Parameters outside of the plates are global quantities that apply to all frames of all AOIs. A more complete version of the graphical model specifying the relevant probability distributions is given in Figure 2—figure supplement 1.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/73860/elife-73860-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Directed factor graph representation (Bishop, 2006) of model parameters and parameter distributions. This diagram is a more complete version of the graphical model shown in Figure 2D; it includes additional parameters ($\mu^{b}$, $\sigma^{b},\delta$) and explicitly specifies the relevant probability distributions. Model parameters are depicted as circles, parameter distributions as small filled squares, and deterministic functions as diamonds. Names of the probability distributions are written next to the squares. Input parameters and output parameters are connected by lines, with an arrow pointing towards the dependent parameter. Observed AOI image ($D$) is the sum of the noisy photon-dependent image ($I$) and the photon-independent camera offset ($\delta$). Plates (rounded rectangles) contain nodes that are repeated for the number of instances displayed at the bottom-right corner: number of AOIs ($N+N_{c}$), frame count ($F$), maximum number of spots in a single image ($K$), and number of image pixels ($P\timesP$). The prior for $x$ and $y$ is Uniform for target-nonspecific spots $(\theta\neqk)$ and AffineBeta for target-specific spots $(\theta=k)$ (see Figure 2—figure supplement 2).

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/73860/elife-73860-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** Prior distributions for the $x$ and $y$ spot position parameters.Prior distributions of $x$ and $y$ for specific and non-specific binding. Probability densities for $x$ and $y$ are defined in the range $[-(P+1)/2,(P+1)/2]$ relative to the target molecule and are conditional on the identity of the spot (specific or non-specific). The width of the peak in the specific distribution is given by $\sigma^{x⁢y}$, the value of which is learned from the data. Probability densities for $x$ and $y$ are identical.

The probabilistic model mathematically generates images $D$ as follows. We construct a noise-free AOI image $\mu^{I}$ as a constant average background intensity $b$ summed with fluorescence spots modeled as 2-D Gaussians $\mu^{S}$, which accurately approximate the microscope point spread function (Zhang et al., 2007; Figure 2B). Each 2-D Gaussian is described by parameters integrated intensity $h$, width $w$, and position ($x$, $y$). We define $K$ as the maximum number of spots that can be present in a single AOI image. For the data we typically encounter, $K$ = 2 is sufficient. Since the spots may be present or not in a particular image, we define the $K$ = 2 binary indicators $m_{spot(1)}$ and $m_{spot(2)}$. Each indicator can take a value of either 0 denoting spot absence or 1 denoting spot presence.

The resulting mixture model has four possible combinations for $m_{spot(1)}$ and $m_{spot(2)}$: (1) a no-spot image that contains only background (Figure 2B, top left), (2) a single-spot image that contains the first binder molecule spot superimposed on background (Figure 2B, bottom left), (3) a single-spot image that contains the second binder molecule spot superimposed on background (Figure 2B, top right), and (4) a two-spot image that contains both binder molecule spots superimposed on background (Figure 2B, bottom right).

Among the spots that are present in an AOI image, by assumption at most only one can be target-specific. We use a state parameter $z$ to indicate target-specific spot absence ($z$ = 0) or presence ($z$ = 1) in an AOI image. We also introduce an index parameter $\theta$ that identifies which of the spots is the target-specific spot when it is present ($z$ = 1) (e.g., Figure 2C, middle and right have $\theta$ = 1 and $\theta$ = 2, respectively) and equals zero when it is absent ($z$ = 0) (e.g., Figure 2C, left). Since the off-target control AOIs by definition contain only non-specific binding, $z$ = 0 and $\theta$ = 0 for all off-target AOIs.

Finally, to construct realistic noisy AOI images $D$ from the noise-free images $\mu^{I}$, the model adds intensity-dependent noise to each pixel. For cameras that use charge-coupled device (CCD) or electron-multiplier CCD (EMCCD) sensors, each measured pixel intensity in a single-molecule fluorescence image has a noise contribution from photon counting (shot noise) and can also contain additional noise arising from electronic amplification (van Vliet et al., 1998). The result is a characteristic linear relationship between the noise variance and mean intensity with slope defining the gain $g$. This relationship is used to compute the random pixel noise values (see Materials and methods).

The resulting probabilistic image model can be interpreted as a generative process that produces the observed image data $D$. A graphical representation of the probabilistic relationships in the model is shown in Figure 2D. A complete description of the model is given in Materials and methods and Figure 2—figure supplement 1.

### Parameter prior distributions

Specifying prior probability distributions for model parameters is essential for Bayesian analysis and allows us to incorporate pre-existing knowledge about the experimental design. For most model parameters, there is no strong prior information so we use uninformative prior distributions (see Materials and methods). However, we have strong expectations for the positions of specific and non-specific binder molecules that can be expressed as prior distributions and used effectively to discriminate between the two. Non-specific binding can occur anywhere on the surface with equal probability and thus has a uniform prior distribution across the AOI image. Target-specific binding, on the other hand, is colocalized with the target molecule and thus has a prior distribution peaked at the AOI center (Figure 2—figure supplement 2). The width of this peak, proximity parameter $\sigma^{x⁢y}$, depends on multiple features of the experiment such as the spot localization accuracy and the mapping accuracy between target and binder imaging channels. Prior distributions for parameters $\theta$ and $m$ are defined in terms of the average number of target-specific and target non-specific spots per AOI image, $\pi$ and $\lambda$, respectively. To facilitate convenient use of the algorithm, it is not necessary to pre-specify values of $\sigma^{x⁢y}$, $\pi$, and $\lambda$. Instead, values of these parameters appropriate to a given data set are calculated automatically using a hierarchical Bayesian analysis (see Materials and methods; for hierarchical modeling see Chapter 5 of Gelman et al., 2013).

### Bayesian inference and implementation

Tapqir calculates posterior distributions of model parameters conditioned on the observed data by using Bayes’ theorem. In particular, Tapqir approximates posterior distributions using a variational inference approach implemented in Pyro (Bingham et al., 2019). Complete details of the implementation are given in Materials and methods.

### Tapqir analysis

In initial tests, we used Tapqir to analyze simulated CoSMoS image data with a comparatively high SNR of 3.76 as well as data from the experiment shown in Figure 1B–D, which has a lower SNR of 1.61. The simulated data were generated using the same cosmos model (Figure 2D) that was used for analysis. Tapqir correctly detects fluorescent spots in both simulated and experimental images (compare ‘AOI images’ and ‘Spot-detection’ rows in Figure 3). The program precisely calculates the position ($x$, $y$), intensity ($h$), and width ($w$) for each spot and also determines the background intensity ($b$) for each image without requiring a separate analysis. These parameters confirm the desired behavior of the model and could be used in further calculations. However, the most important output of the analysis is assessment of the presence of target-specific binding. For each AOI image, we calculate $p(specific)≡p(z=1)$ (Figure 3, green), the probability that any target-specific spot is present. Spots determined as likely target-specific ($p(specific)$ > 0.5) are represented as filled circles in the spot detection row of Figure 3. For a particular spot to have high $p(specific)$, it must have a high spot probability and be colocalized with the target molecule at the center of the AOI (Figure 3—figure supplement 1).

![Figure 3.](https://cdn.elifesciences.org/articles/73860/elife-73860-fig3-v2.jpg)

**Figure 3.:** (A,B) Tapqir was applied to simulated data (lamda0.5 parameter set in Supplementary file 1) (A) and to experimental data (Data set A in Table 1) (B). (A) and (B) each show a short extract from a single target location in the data set. The first row shows AOI images for the subset of frames indicated by gray shaded stripes in the plots; image contrast and offset settings are consistent within each panel. The second row shows the locations of spots determined by Tapqir. Spot numbers 1 (blue) and 2 (orange) are assigned arbitrarily and may change from fame to frame. For clarity, only data for spots with a spot probability $p(m=1)$ > 0.5 are shown. Spots predicted to be target-specific ($p(\theta=k)$ > 0.5 for spot $k$) are shown as filled circles. The topmost graphs (green) show the calculated probability that a target-specific spot is present ($p(specific)$) in each frame. Below are the calculated spot intensities ($h$), spot widths ($w$), and locations ($x$, $y$) for spot 1 (blue) and spot 2 (orange), and the AOI background intensities ($b$). Again, for clarity data are only shown for likely spots ($p(m=1)$ > 0.5). Error bars: 95% CI (credible interval) estimated from a sample size of 500. Some error bars are smaller than the points and thus not visible.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/73860/elife-73860-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** The data sets used for panels A and B are identical to those in Figure 3A and B; the first two rows and the $p(specific)$ (green) graph are reproduced from that figure. Blue graphs show the probability of being present ($p⁢(m=1)$) and of being target-specific ($p⁢(\theta=1)$) for the arbitrarily designated spot 1 in each frame. Orange graphs show the analogous quantities $p⁢(m=1)$ and $p⁢(\theta=2)$ for spot 2. For a given image, the probability $p(specific)≡p(z=1)$ that any target-specific spot is present is equal to $p⁢(\theta=1)+p⁢(\theta=2)$.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/73860/elife-73860-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** Example frames are shown from Data set A (A: SNR = 1.61), Data set B (B: SNR = 3.77), Data set C (C: SNR = 4.23), and Data set D (D: SNR = 3.06) in Table 1. In each panel the top row shows AOI images selected from the experimental data and middle row shows corresponding images obtained by sampling from the posterior distributions. Image contrast and offset are consistent within each panel. The bottom row shows pixel intensity distributions from the experimental and posterior prediction images.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/73860/elife-73860-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** Simulations (see Materials and methods) consist of 16 data sets where values of global parameters ($\pi,\lambda$, $\sigma^{x⁢y}$, and $g$) were randomly generated for each data set (Supplementary file 2). Simulated data were fit with Tapqir, and parameter values from the fit (with 95% credible interval estimated from a sample size of 10,000) are plotted against the true parameter values. To guide the eye, dashed lines indicate identical true and fit values. (A) Gain of the camera $g$. (B) Average target-specific binding probability $\pi$. (C) Target non-specific binding density $\lambda$. (D) Proximity parameter $\sigma^{x⁢y}$.

![Figure 3—figure supplement 4.](https://cdn.elifesciences.org/articles/73860/elife-73860-fig3-figsupp4-v2.jpg)

**Figure 3—figure supplement 4.:** (A) and (B) each show a short extract from a single target location (AOI 163 in (A) and AOI 0 in (B)) from Data set A (Table 1; SNR = 1.61). Tapqir was applied to the data set using AOI image sizes $P$ of 14 × 14 (first row), 10 × 10 (second row), and 6 × 6 (third row) pixels. Corresponding output $p(specific)$ probabilities are plotted in the graph. Image contrasts in (A) and (B) are different. Unattended calculation time on an AMD Ryzen Threadripper 2990 WX with an Nvidia GeForce RTX 2080Ti GPU using CUDA version 11.5 for the different AOI sizes were: 7 h 40 min ($P$ = 14), 3 h 5 min ($P$ = 10), and 2 h 40 min ($P$ = 6).

### Tapqir robustly fits experimental data sets with different characteristics

Next, we evaluated how well the model fits data sets encompassing a range of characteristics found in typical CoSMoS experiments. We analyzed four experimental data sets with varying SNR, frequency of target-specific spots, and frequencies of non-specific spots (Table 1). We then sampled AOI images from the posterior distributions of parameters (a method known as posterior predictive checking Gelman et al., 2013). These posterior predictive simulations accurately reproduce the experimental AOI appearances, recapitulating the noise characteristics and the numbers, intensities, shapes, and locations of spots (Figure 3—figure supplement 2, images). The distributions of pixel intensities across the AOI are also closely reproduced (Figure 3—figure supplement 2, histograms) confirming that the noise model is accurate. Taken together, these results confirm that the model is rich enough to accurately capture the full range of image characteristics from CoSMoS data sets taken over different experimental conditions. Importantly, all the results on different experimental data sets were obtained using the same model (Figure 2D) and the same priors (Materials and methods). No tuning of the algorithm or prior measurement of data-set-specific properties was needed to achieve good fits for all data sets.

**Table 1.**
 Experimental data sets.


<table>
  <thead>
    <tr>
      <th>Data set sizea</th>
      <th>SNR</th>
      <th>π [95% CI]</th>
      <th>λ [95% CI]</th>
      <th>g [95% CI]</th>
      <th>σxy [95% CI]</th>
      <th>Compute time</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="7">Data set A: Binder, SNAPf-tagged S. cerevisiae RNA polymerase II labeled with DY549; Target, transcription template DNA containing 5× Gal4 upstream activating sequences and CYC1 core promoter; Conditions, yeast nuclear extract supplemented with Gal4-VP16 activator and NTPs. From Rosen et al., 2020.</td>
    </tr>
    <tr>
      <td>N= 331, Nc = 526, F = 790</td>
      <td>1.61</td>
      <td>0.0951 [0.0936, 0.0966]</td>
      <td>0.2943 [0.2924, 0.2963]</td>
      <td>6.645 [6.643, 6.647]</td>
      <td>0.577 [0.573, 0.580]</td>
      <td>7 h 40 mb3 h 50 mc</td>
    </tr>
    <tr>
      <td colspan="7">Data set B: Binder, 0.1 nM E. coli σ54 RNA polymerase labeled with Cy3; Target, 852 bp DNA containing the glnALG promoter; Conditions, physiological buffer, no NTPs. From (Fig. 1E) of Friedman et al., 2013.</td>
    </tr>
    <tr>
      <td>N= 102, Nc = 127, F = 4407</td>
      <td>3.77</td>
      <td>0.0846 [0.0835, 0.0857]</td>
      <td>0.1575 [0.1569, 0.1583]</td>
      <td>11.861 [11.856, 11.865]</td>
      <td>0.476 [0.474, 0.479]</td>
      <td>7 h 40 mb</td>
    </tr>
    <tr>
      <td colspan="7">Data set C: Binder, 0.4 nM E. coli σ54 RNA polymerase labeled with Cy3; Target, 3,591 bp DNA containing the glnALG promoter; Conditions, physiological buffer, no NTPs. From (Fig. 3D) of Friedman et al., 2013.</td>
    </tr>
    <tr>
      <td>N= 122, Nc = 157, F = 3855</td>
      <td>4.23</td>
      <td>0.0267 [0.0262, 0.0273]</td>
      <td>0.0876 [0.0869, 0.0883]</td>
      <td>16.777 [16.773, 16.782]</td>
      <td>0.404 [0.399, 0.408]</td>
      <td>9 h 15 mb</td>
    </tr>
    <tr>
      <td colspan="7">Data set D: Binder, 0.15 nM E. coli Cy3-GreB; Target, reconstituted backtracked EC-6 E. coli transcription elongation complex; Conditions, physiological buffer, no NTPs. Randomly selected subset of data set from Tetone et al., 2017.</td>
    </tr>
    <tr>
      <td>N= 200, Nc = 200, F = 5622</td>
      <td>3.06</td>
      <td>0.0038 [0.0036, 0.0039]</td>
      <td>0.0437 [0.0434, 0.0440]</td>
      <td>18.727 [18.724, 18.731]</td>
      <td>0.451 [0.438, 0.463]</td>
      <td>11 hb</td>
    </tr>
  </tbody>
</table>

_*N - number of on-target AOIs, Nc - number of control off-target AOIs, F - number of frames.bUnattended calculation time on an AMD Ryzen Threadripper 2990WX with an Nvidia GeForce RTX 2080Ti GPU using CUDA version 11.5.cUnattended calculation time on an Intel Xeon CPU with an Nvidia Tesla V100-SXM2-16GB GPU using CUDA version 11.2 in a Google Colab Pro account._

### Tapqir accuracy on simulated data with known global parameter values

Next, we evaluated Tapqir’s ability to reliably infer the values of global model parameters. To accomplish this, we generated simulated data sets using a wide range of randomized parameter values and then fit the simulated data to the model (Supplementary file 2). Fit results show that global model parameters (i.e., average specific spot probability $\pi$, nonspecific binding density $\lambda$, proximity $\sigma^{x⁢y}$, and gain $g$; see Figure 2D) are close to the simulated values (Figure 3—figure supplement 3 and Supplementary file 2). This suggests that CoSMoS data contains enough information to reliably infer global model parameters and that the model is not obviously overparameterized.

### Tapqir classification accuracy

Having tested the basic function of the algorithm, we next turned to the key question of how accurately Tapqir can detect target-specific spots in data sets of increasing difficulty.

We first examined the accuracy of target-specific spot detection in simulated data sets with decreasing SNR (Supplementary file 3). By eye, spots can be readily discerned at SNR >1 but cannot be clearly seen at SNR <1 (Figure 4A). Tapqir gives similar or better performance: if an image contains a target-specific spot, Tapqir correctly assigns it a target-specific spot probability $p(specific)$ that is on average close to one as long as SNR is adequate (i.e., SNR >1) (Figure 4B). In contrast, mean $p(specific)$ sharply decreases at SNR <1, consistent with the subjective impression that no spot is recognized under those conditions. In particular, images that contain a target-specific spot are almost always assigned a high $p(specific)$ for high SNR data and almost always assigned low $p(specific)$ for low SNR data (Figure 4C, green). At marginal SNR ≈ 1, these images are assigned a broad distribution of $p(specific)$ values, accurately reflecting the uncertainty in classifying such data. Just as importantly, images with no target-specific spot are almost always assigned $p(specific)$ < 0.5, correctly reflecting the absence of the spot (Figure 4C, gray).

![Figure 4.](https://cdn.elifesciences.org/articles/73860/elife-73860-fig4-v2.jpg)

**Figure 4.:** (A–D) Analysis of simulated data over a range of SNR. SNR was varied in the simulations by changing spot intensity $h$ while keeping other parameters constant (Supplementary file 3). (A) Example images showing the appearance of the same target-specific spot simulated with increasing SNR. (B) Mean of Tapqir-calculated target-specific spot probability $p(specific)$ (with 95% CI; see Materials and methods) for the subset of images where target-specific spots are known to be present. (C) Histograms of $p(specific)$ for selected simulations with SNR indicated. Data are shown as stacked bars for images known to have (green, 15%) or not have (gray, 85%) target-specific spots. Count is zero for bins where bars are not shown. (D) Accuracy of Tapqir image classification with respect to presence/absence of a target-specific spot. Accuracy was assessed by MCC, recall, and precision (see Results and Materials and methods sections). (E–G) Same as in (B–D) but for the data simulated over a range of non-specific binding densities $\lambda$ at fixed SNR = 3.76 (Supplementary file 1). (H) Spot recognition in AOI images containing closely spaced target-specific and non-specific spots. Images were selected from the $\lambda$ = 1 data set in (E–G). AOI images and spot detection are plotted as in Figure 3, with spot numbers 1 (blue) and 2 (orange) assigned arbitrarily and spots predicted to be target-specific shown as filled circles. (I) Same as in (C) but for the data simulated over a range of non-specific binding densities $\lambda$ with no target-specific binding ($\pi$ = 0) (Supplementary file 4).

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/73860/elife-73860-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** The same $\lambda$ = 1 simulated data set used in Figure 4E–H (lamda1 in Supplementary file 1) was analyzed by Tapqir and spot-picker. The data set contained 418 AOI images containing target-specific spots, of which the 37 shown here were falsely predicted to contain no target-specific spot (3 by Tapqir and 34 by spot-picker). Correct (+) and incorrect (−) predictions by each program are indicated. In all AOI images except AOI 3 frame 109, there is a nearby target non-specific spot in addition to the target-specific one. False negative classifications by spot-picker method are presumably due to the presence of a closely located target non-specific spot that distorts the shape of a target-specific spot. Tapqir, on the other hand, is able to correctly infer the presence of two closely located spots even when they are not completely resolved (Figure 4H). The rare (3 out of 418) false negative classifications by Tapqir likely arise from target-specific spots with centers that deviate from the target location by much more (∼ 0.7 pixels) than the inferred proximity parameter ($\sigma^{x⁢y}$ = 0.2 pixels).

Ideally, we want to correctly identify target-specific binding when it occurs but also to avoid incorrectly identifying target-specific binding when it does not occur. To quantify Tapqir’s classification accuracy, we next examined binary image classification statistics. Binary classification predictions were obtained by thresholding $p(specific)$ at 0.5. We then calculated two complementary statistics: recall and precision (Fawcett, 2006; Figure 4D; see Materials and methods). Recall is defined as the fraction of true target-specific spots that are correctly predicted. Recall is high at high SNR and decreases at lower SNR. Recall is a binary analog of the mean $p(specific)$ for the subset of images containing target-specific spots; as expected the two quantities have similar dependencies on SNR (compare Figure 4B and D, black). Precision is the fraction of predicted target-specific spots that are correctly predicted. Precision is near one at all SNR values tested (Figure 4D, red); this shows that the algorithm rarely misclassifies an image as containing a target-specific spot when none is present.

In order to quantify the effects of both correctly and incorrectly classified images in a single statistic, we used the binary classification predictions to calculate the Matthews Correlation Coefficient (MCC) (Matthews, 1975; see Materials and methods). The MCC is equivalent to the Pearson correlation coefficient between the predicted and true classifications, giving 1 for a perfect match, 0 for a random match, and –1 for complete disagreement. The MCC results (Figure 4D, blue) suggest that the overall performance of Tapqir is excellent at SNR ≥ 1: the program rarely misses target-specific spots that are in reality present and rarely falsely reports a target-specific spot when none is present.

The analyses of Figure 4B–D examined Tapqir performance on data in which the rate of target-nonspecific binding is moderate ($\lambda$ = 0.15 non-specific spots per AOI image on average). We next examined the effects of increasing the non-specific rate. In particular, we used simulated data (Supplementary file 1) with high SNR = 3.76 to test the classification accuracy of Tapqir at different non-specific binding densities up to $\lambda$ = 1, a value considerably higher than typical of usable experimental data (the experimental data sets in Table 1 have $\lambda$ ranging from 0.04 to 0.30). In analysis of these data sets, a few images with target-specific spots are misclassified as not having a specific spot ($p(specific)$ near zero) or as being ambiguous ($p(specific)$ near 0.5) (Figure 4F, green bars), and a few images with target-nonspecific spots are misclassified as having specific spot ($p(specific)$ near or above 0.5) (Figure 4F, gray bars), but these misclassifications only occurred at the unrealistically high $\lambda$ value. Even in the simulation with this highest $\lambda$ value, Tapqir accurately identified target-specific spots (Figure 4E and F) and returned excellent binary classification statistics (Figure 4G).

A weakness of some existing image-based CoSMoS spot discrimination methods is that target-nonspecific binding adjacent to a target-specific spot can interfere with correctly identifying the latter as target-specific. The very high recall values obtained at $\lambda$ = 1 (Figure 4G) confirm that there are few such misidentifications by Tapqir even at high non-specific binding densities. This good performance is likely facilitated by the feature of the Tapqir model that explicitly includes the possibility that both a specifically and a non-specifically bound spot may occur simultaneously in the same AOI. Consistent with this interpretation, we see effective detection of the specific and non-specific spots even in example AOIs in which the two spots are so closely spaced that they are not completely resolved (Figure 4H). In contrast, tests of existing CoSMoS image classification methods show that images with target-nonspecific spots are prone to misclassification. As discussed previously (Friedman and Gelles, 2015), methods based on thresholding of integrated AOI intensities are prone to incorrectly classify target-nonspecific spots as target-specific. Conversely, an existing ‘spot-picker’ method based on empirical binary classification of 2-D AOI images (Friedman and Gelles, 2015) is much more likely than Tapqir to fail to detect target specific spots when there is a nearby non-specific spot (Figure 4—figure supplement 1). This contributes to the superior overall performance we see for Tapqir vs. spot-picker on the $\lambda$ = 1 data set (recall 0.993 vs 0.919; precision 0.943 vs 0.873; MCC 0.961 vs 0.874).

To further evaluate whether Tapqir is prone to misidentifying target-nonspecific spots as specific, we simulated data sets with no target-specific binding at both low and high non-specific binding densities (Supplementary file 4). Analysis of such data (Figure 4I) shows that no target-specific binding (i.e., $p(specific)$ > 0.6) was detected even under the highest non-specific binding density, demonstrating that Tapqir is robust to false-positive target-specific spot detection even under these extreme conditions.

Since target-nonspecific spots are built into the cosmos model, there is no need to choose excessively small AOIs in an attempt to exclude non-specific spots from analysis. We found that reducing AOI size (from 14 × 14 to 6 x 6 pixels) did not appreciably affect analysis accuracy on simulated data, when the width ($w$) of the spots was equal to 1.4 pixels (Table 2). In analysis of experimental data, smaller AOI sizes caused occasional changes in calculated $p(specific)$ values reflecting apparent missed detection of a few spots (Figure 3—figure supplement 4). Out of caution, we therefore used 14 × 14 pixel AOIs routinely, even though the larger AOIs somewhat reduced computation speed (Table 2 and Figure 3—figure supplement 4).

**Table 2.**
 The effect of AOI size on classification accuracy*.


<table>
  <thead>
    <tr>
      <th>AOI dimension†, P (pixels)</th>
      <th>MCC</th>
      <th>Compute time‡</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>14</td>
      <td>0.951</td>
      <td>2 h 10 m</td>
    </tr>
    <tr>
      <td>10</td>
      <td>0.948</td>
      <td>1 h 25 m</td>
    </tr>
    <tr>
      <td>6</td>
      <td>0.939</td>
      <td>1 h 20 m</td>
    </tr>
  </tbody>
</table>

_*Tapqir was applied to the same simulated data set (height1000 parameter set in Supplementary file 3; SNR = 1.25) using different AOI sizes.†The width (w) of the simulated spots (one standard deviation of the 2-D Gaussian) is equal to 1.4 pixels.‡Unattended calculation time on an AMD Ryzen Threadripper 2990WX with an Nvidia GeForce RTX 2080Ti GPU using CUDA version 11.5._

### Kinetic and thermodynamic analysis of molecular interactions

The most widespread application of CoSMoS experiments is to measure rate and equilibrium constants for the binding interaction of the target and binder molecules being studied. We next tested whether these constants can be accurately determined using Tapqir-calculated posterior predictions.

We first simulated CoSMoS data sets (Supplementary file 5) that reproduced the behavior of a one-step association/dissociation reaction mechanism (Figure 5A and B, blue). Simulated data were analyzed with Tapqir yielding $p(specific)$ values for each frame (e.g., Figure 5B, green). We wanted to estimate rate constants using the full information contained in the $p(specific)$ probabilities, so we did not threshold $p(specific)$ for this analysis. Instead, from each single-AOI $p(specific)$ time record we constructed a family of binary time records (Figure 5B, black) by Monte Carlo sampling according to the $p(specific)$ time series. Each family member has well-defined target-specific binder-present and binder-absent intervals $Δt_{on}$ and $Δt_{off}$, respectively. Each of these time records was then analyzed with a two-state hidden Markov model (HMM) (see Materials and methods), producing a distribution of inferred rate constants from which we calculated mean values and their uncertainties (Figure 5C and D). Comparison of the simulated and inferred values shows that both $k_{on}$ and $k_{off}$ rate constants are accurate within 30% at nonspecific binding densities typical of experimental data ($\lambda$ ≤ 0.5). At higher nonspecific binding densities, rare interruptions caused by false-positive and false-negative spot detection shorten $Δt_{on}$ and $Δt_{off}$ distributions, leading to moderate systematic overestimation of the association and dissociation rate constants.

![Figure 5.](https://cdn.elifesciences.org/articles/73860/elife-73860-fig5-v2.jpg)

**Figure 5.:** (A) Chemical scheme for a one-step association/dissociation reaction at equilibrium with pseudo-first-order binding and dissociation rate constants $k_{on}$ and $k_{off}$, respectively. (B) A simulation of the reaction in (A) and scheme for kinetic analysis of the simulated data with Tapqir. The simulation used SNR = 3.76, $k_{on}$ = 0.02 s−1, $k_{off}$ = 0.2 s−1, and a high target-nonspecific binding frequency $\lambda$ = 1 (Supplementary file 5, data set kon0.02lamda1). Full dataset consists of 100 AOI locations and 1,000 frames each for on-target data and off-target control data. Shown is a short extract of on-target data from a single AOI location in the simulation. Plots show simulated presence/absence of the target-specific spot (blue) and Tapqir-calculated estimate of corresponding target-specific spot probability $p(specific)$ (green). Two thousand binary traces (e.g., black records) were sampled from the $p(specific)$ posterior distribution and used to infer $k_{on}$ and $k_{off}$ using a two-state hidden Markov model (HMM) (see Materials and methods). Each sample trace contains well-defined time intervals corresponding to target-specific spot presence and absence (e.g., $Δt_{on}$ and $Δt_{off}$). (C,D,E) Kinetic and equilibrium constants from simulations (Supplementary file 5) using a range of $k_{on}$ values and target-nonspecific spot frequencies $\lambda$, with constant $k_{off}$ = 0.2 s−1. (C) Values of $k_{on}$ used in simulations (blue) and mean values (and 95% CIs, black) inferred by HMM analysis from the 2000 posterior samples. Some error bars are smaller than the points and thus not visible. (D) Same as (C) but for $k_{off}$. (E) Binding equilibrium constants $K_{eq}=k_{on}/k_{off}$ used in simulation (blue) and inferred from Tapqir-calculated π as $K_{eq}=\pi/(1−\pi)$ (black).

From the same simulated data, we calculated the equilibrium constant $K_{eq}$ and its uncertainty. This calculation does not require a time-dependent model and can be obtained directly from the posterior distribution of the average specific-binding probability $\pi$. The estimated equilibrium constants are highly accurate even at excessively high values of $\lambda$ (Figure 5E). The high accuracy results from the fact that equilibrium constant measurements are in general much less affected than kinetic measurements by occasional false positives and false negatives in spot detection.

The forgoing analysis shows that Tapqir can accurately recover kinetic and thermodynamic constants from simulated CoSMoS data. However, experimental CoSMoS data sets can be more diverse. In addition to having different SNR and non-specific binding frequency values, they also may have non-idealities in spot shape (caused by optical aberrations) and in noise (caused by molecular diffusion in and out of the TIRF evanescent field). In order to see if Tapqir analysis is robust to these and other properties of real experimental data, we analyzed several CoSMoS data sets taken from different experimental projects. Analysis of each data set took a few hours of computation time on a GPU-equipped desktop computer or cloud computing service (Table 1). We first visualized the results as probabilistic rastergrams (Figure 6A, Figure 6—figure supplement 1A, Figure 6—figure supplement 2A, and Figure 6—figure supplement 3A), in which each horizontal line represents the time record from a single AOI. Unlike the binary spot/no-spot rastergrams in previous studies (e.g., Friedman et al., 2013; Rosen et al., 2020) we plotted the Tapqir-calculated spot probability $p(specific)$ using a color scale. This representation allows a more nuanced understanding of the data. For example, Figure 6A reveals that while the long-duration spot detection events typically are assigned a high probability (yellow), some of the shortest duration events have an intermediate $p(specific)$ (green) indicating that the assignment of these as target-specific is uncertain.

![Figure 6.](https://cdn.elifesciences.org/articles/73860/elife-73860-fig6-v2.jpg)

**Figure 6.:** Data are from Data set B (SNR = 3.77, $\lambda$ = 0.1575; see Table 1). (A) Probabilistic rastergram representation of Tapqir-calculated target-specific spot probabilities $p(specific)$ (color scale). AOIs were ordered by decreasing times-to-first-binding. For clarity, only every thirteenth frame is plotted. (B) Time-to-first-binding distribution using Tapqir. Plot shows the cumulative fraction of AOIs that exhibited one or more target-specific binding events by the indicated frame number (green) and fit curve (black). Shading indicates uncertainty. (C) Time-to-first-binding distribution using an empirical spot-picker method Friedman et al., 2013. The spot-picker method jointly fits first spots observed in off-target control AOIs (yellow) and in on-target AOIs (purple) yielding fit curves (black). (D) Values of kinetic parameters $k_{a}$, $k_{ns}$, and $A_{f}$ (see text) derived from fits in (B) and (C). Uncertainties reported in (B, C, D) represent 95% credible intervals for Tapqir and 95% confidence intervals for spot-picker (see Materials and methods).

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/73860/elife-73860-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** Data are from Data set A (SNR = 1.61, $\lambda$ = 0.2943; see Table 1). Results are plotted as in Figure 6, except that for clarity only every second frame and every third AOI is shown in (A).

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/73860/elife-73860-fig6-figsupp2-v2.jpg)

**Figure 6—figure supplement 2.:** Data are from Data set C (SNR = 4.23, $\lambda$ = 0.0876; see Table 1). Results are plotted as in Figure 6, except that for clarity only every tenth frame is shown in (A).

![Figure 6—figure supplement 3.](https://cdn.elifesciences.org/articles/73860/elife-73860-fig6-figsupp3-v2.jpg)

**Figure 6—figure supplement 3.:** Data are from Data set D (SNR = 3.06, $\lambda$ = 0.0437; see Table 1). Results are plotted as in Figure 6, except that for clarity only every thirteenth frame and every second AOI is shown in (A).

To demonstrate the utility of Tapqir for kinetic analysis of real experimental data, we measured binder association rate constants in previously published experimental data sets (Table 1). We employed our previous strategy (Friedman and Gelles, 2012; Friedman and Gelles, 2015) of analyzing the duration of the binder-absent intervals that preceded the first binding event. Such time-to-first binding analysis improves the accuracy of association rate constant estimates relative to those obtained by analyzing all $Δt_{off}$ values by minimizing the effects of target molecules occupied by photobleached binders, dye blinking and false negative dropouts that occur within a continuous binder dwell interval. To perform a time-to-first-binding analysis using Tapqir, we used the posterior sampling method (as in Figure 5B, black records) to determine the initial $Δt_{off}$ in each AOI record. These data were fit to a kinetic model (Friedman and Gelles, 2012; Friedman and Gelles, 2015) in which only a fraction of target molecules $A_{f}$ were binding competent and which includes both exponential target-specific association with rate constant $k_{a}$, as well as exponential non-specific association with rate constant $k_{ns}$ (Figure 6B, Figure 6—figure supplement 1B, Figure 6—figure supplement 2B, and Figure 6—figure supplement 3B). The Tapqir-derived fits showed excellent agreement with the kinetic model.

To further assess the utility of the Tapqir method, we used experimental data sets and compared the Tapqir association kinetics results with those from the previously published empirical binary ‘spot-picker’ method (Friedman and Gelles, 2015; Figure 6C, Figure 6—figure supplement 1C, Figure 6—figure supplement 2C, and Figure 6—figure supplement 3C). The values of the association rate constant $k_{a}$ obtained using these two methods are in good agreement with each other (Figure 6D, Figure 6—figure supplement 1D, Figure 6—figure supplement 2D, and Figure 6—figure supplement 3D). We emphasize that while Tapqir is fully objective, achieving these results with the spot-picker method required optimization by subjective adjustment of spot detection thresholds. We noted some differences between the two methods in the non-specific association rate constants $k_{ns}$. Differences are expected because these parameters are defined differently in the different non-specific binding models used in Tapqir and spot-picker (see Materials and methods).

## Discussion

A broad range of physical processes contribute to the formation of CoSMoS images. These include camera and photon noise, target-specific and non-specific binding, and time- and position-dependent variability in fluorophore imaging and image background. Unlike prior CoSMoS analysis methods, Tapqir considers these aspects of imaging in a single, holistic model. This cosmos model explicitly includes the uncertainties due to photon noise, camera gain, and spatial variability in intensity offset. The model also includes the possibility of multiple binder molecule fluorescence spots being present in the vicinity of the target, including both target-specific binding and target-nonspecific interactions of binder molecules with the coverslip surface. This explicit modeling of target-nonspecific spots makes it possible to include off-target control data as a part of the experimental data set. Similarly, all AOIs and frames in the data set are simultaneously fit to the global model in a way that allows for realistic frame-to-frame and AOI-to-AOI variability in image formation caused by variations in laser intensity, fluctuations in background, and other non-idealities. The global analysis based on a single, unified model enables the final results (e.g., kinetic and thermodynamic parameters) to be estimated in a way that is cognizant of the known sources of uncertainty in the data.

Previous approaches to CoSMoS data analysis, including our spot-picker method (Friedman and Gelles, 2015), did not employ a holistic modeling approach and instead relied on a multi-step process that includes a separate binary classification step. These prior methods require subjective setting of classification thresholds. Because they are not fully objective, such methods cannot reliably account for uncertainties in spot classification, which compromises error estimates in the analysis pipeline downstream of spot classification. One recent approach (Smith et al., 2019; Smith et al., 2015), which like spot-picker and Tapqir analyzes 2-D images instead of integrated intensities, used a Bayesian kinetic analysis but a frequentist hypothesis test (a generalized likelihood ratio test) for spot detection. The frequentist method lacks a key advantage of Tapqir’s model-based Bayesian approach that here enables prediction of target-specific spot presence probabilities $p(specific)$ for each image, rather than a binary ‘spot/no spot’ classification. In general, previous approaches in essence assume that spot classifications are correct, and thus the uncertainties in the derived molecular properties (e.g., equilibrium constants) are systematically underestimated because the errors in spot classification, which can be large, are not accounted for. By performing a probabilistic spot classification, Tapqir enables reliable inference of molecular properties, such as thermodynamic and kinetic parameters, and allows statistically well-justified estimation of parameter uncertainties. This more inclusive error estimation likely accounts for the generally larger kinetic parameter error bars obtained from Tapqir compared to those from the existing spot-picker analysis method (Figure 6, Figure 6—figure supplement 1, Figure 6—figure supplement 2, and Figure 6—figure supplement 3). Even though existing analysis methods take advantage of subjective tuning by a human analyst, our comparisons show that Tapqir performs at least comparably to (Figure 6, Figure 6—figure supplement 1, Figure 6—figure supplement 2, and Figure 6—figure supplement 3) and under some conditions much better than (Figure 4—figure supplement 1) the existing spot-picker method.

The Tapqir cosmos model includes parameters of mechanistic interest, such as the average probability of target-specific binding, as well as ‘nuisance’ parameters that are not of primary interest but nevertheless essential for image modeling. In previous image-based methods for CoSMoS analysis (e.g., Friedman and Gelles, 2015; Smith et al., 2019), nuisance parameters were either measured in separate experiments (e.g., gain was determined from calibration data), set heuristically (e.g., a subjective choice of user-set thresholds for spot intensity and proximity in colocalization detection), or determined at a separate analysis step (e.g., rate of non-specific binding). In contrast, Tapqir directly learns parameters from the full set of experimental data, thus eliminating the need for additional experiments, subjective adjustment of tuning parameters, and post-processing steps.

Bayesian analysis has been used previously to analyze data from single-molecule microscopy experiments (e.g., Kinz-Thompson et al., 2021 and references cited therein). A key feature of Bayesian analysis is that the extent of prior knowledge of all model parameters is explicitly incorporated. Where appropriate, cosmos uses relatively uninformative priors that only weakly specify information about the value of the corresponding parameters. In these cases, cosmos mostly infers parameter values from the data. In contrast, some priors are more informative. For example, binder molecule spots near the target molecule are more likely to be target-specific rather than target-nonspecific, so we use this known feature of the experiment by encoding the likely position of target-specific binding as a data-based prior. This tactic effectively enables probabilistic classification of spots as either target-specific or target-nonspecific, which would be difficult using other inference methodologies, while still accommodating data sets with different accuracies of mapping between binder and target channels.

Tapqir is implemented in Pyro, a Python-based probabilistic programming language (PPL) (Bingham et al., 2019). Probabilistic programming is a relatively new paradigm in which probabilistic models are expressed in a high-level language that allows easy formulation, modification, and automated inference (van de Meent et al., 2018). In this work we focused on developing an image model for colocalization detection in a relatively simple binder-target single-molecule experiment. However, Tapqir can be used with more complex models. For example, the cosmos model could be naturally extended to multi-state and multi-color analysis. Furthermore, with the development of more efficient sequential hidden Markov modeling algorithms (Särkkä and García-Fernández, 2019; Obermeyer et al., 2019b) Tapqir can potentially be extended to directly incorporate kinetic processes, allowing direct inference of kinetic mechanisms and rate constants.

Tapqir is free, open-source software. Tapqir is available at https://github.com/gelles-brandeis/tapqir. The results presented here were obtained using release 1.0 of the program (https://github.com/gelles-brandeis/tapqir/releases/tag/v1.0). The Tapqir documentation, which contains tutorials on program use, is at https://tapqir.readthedocs.io/en/stable/. Source data including Figures, Figure supplements, Supplementary files, manuscript text, and the scripts and data used to generate them are available at https://github.com/ordabayevy/tapqir-overleaf.

## Materials and methods

### Notation

In the Materials and methods section, we adopt a mathematical notation for multi-dimensional arrays from the field of machine learning (Chiang et al., 2021). The notation uses named axes and incorporates implicit broadcasting of arrays when their shapes are different.

### Extracting image data

Raw input data into Tapqir consists of (1) binder channel images ($D^{raw}$), each $W\timesH$ pixels in size, for each time point (Figure 1B, right) and (2) lists of locations, corrected for microscope drift if necessary (Friedman and Gelles, 2015), of target molecules and of off-target control locations (Friedman and Gelles, 2015) within the raw images. For simplicity, we use the same notation ($x^{target,raw}$, $y^{target,raw}$) both for target molecule locations and off-target control locations. Tapqir extracts a $P\timesP$ AOI around each target and off-target location and returns (1) the extracted data set $D$ consisting of a set of $P\timesP$ grayscale images, collected at $N$ on-target AOI sites and $N_{c}$ off-target AOI sites for a range of $F$ frames (Figure 1C and D; Figure 7), and (2) new target (and off-target) locations ($x^{target}$, $y^{target}$) adjusted relative to extracted images $D$ where $x^{target}$ and $y^{target}$ both lie within the $(P/2-1,P/2)$ central range of the image. For the data presented in this article, we used $P$ = 14. Cartesian pixel indices (i, $j$) are integers but also represent the center point of a pixel on the image plane. While experimental intensity measurements are integers, we treat them as continuous values in our analysis.

![Figure 7.](https://cdn.elifesciences.org/articles/73860/elife-73860-fig7-v2.jpg)

### The cosmos model

Our intent is to model CoSMoS image data by accounting for the significant physical aspects of image formation, such as photon noise and binding of target-specific and target-nonspecific molecules to the microscope slide surface. A graphical representation of the Tapqir model for CoSMoS data similar to that in Figure 2D but including probability distributions and other additional detail is shown in Figure 2—figure supplement 1. The corresponding generative model represented as pseudocode is shown in Figure 8. All variables with short descriptions and their domains are listed in Table 3. Below, we describe the model in detail starting with the observed data and the likelihood function and then proceed with model parameters and their prior distributions.

![Figure 8.](https://cdn.elifesciences.org/articles/73860/elife-73860-fig8-v2.jpg)

**Table 3.**
 Variables used in the Tapqir model.


<table>
  <thead>
    <tr>
      <th>Symbol</th>
      <th>Meaning</th>
      <th>Domain</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>K</td>
      <td>Maximum number of spots per image</td>
      <td>ℕ</td>
    </tr>
    <tr>
      <td>N</td>
      <td>Number of on-target AOIs</td>
      <td>ℕ</td>
    </tr>
    <tr>
      <td>Nc</td>
      <td>Number of off-target control AOIs</td>
      <td>ℕ</td>
    </tr>
    <tr>
      <td>F</td>
      <td>Number of frames</td>
      <td>ℕ</td>
    </tr>
    <tr>
      <td>P</td>
      <td>Size of the AOI image in pixels</td>
      <td>ℕ</td>
    </tr>
    <tr>
      <td>g</td>
      <td>Camera gain</td>
      <td>R&gt;0</td>
    </tr>
    <tr>
      <td>σx⁢y</td>
      <td>Proximity</td>
      <td>(0,(P+1)/12)</td>
    </tr>
    <tr>
      <td>π</td>
      <td>Average target-specific binding probability</td>
      <td>[0,1]</td>
    </tr>
    <tr>
      <td>λ</td>
      <td>Target-nonspecific binding density</td>
      <td>R&gt;0</td>
    </tr>
    <tr>
      <td>μb</td>
      <td>Mean background intensity across AOI</td>
      <td>R&gt;0AOI[N]</td>
    </tr>
    <tr>
      <td>σb</td>
      <td>Standard deviation of background intensity across AOI</td>
      <td>R&gt;0AOI[N]</td>
    </tr>
    <tr>
      <td>b</td>
      <td>Background intensity</td>
      <td>R&gt;0AOI[N]×frame[F]</td>
    </tr>
    <tr>
      <td>z</td>
      <td>Target-specific spot presence</td>
      <td>{0,1}AOI[N]×frame[F]</td>
    </tr>
    <tr>
      <td>θ</td>
      <td>Target-specific spot index</td>
      <td>{0,1,…,K}AOI[N]×frame[F]</td>
    </tr>
    <tr>
      <td>m</td>
      <td>Spot presence indicator</td>
      <td>{0,1}spot[K]×AOI[N]×frame[F]</td>
    </tr>
    <tr>
      <td>h</td>
      <td>Integrated spot intensity</td>
      <td>R&gt;0spot[K]×AOI[N]×frame[F]</td>
    </tr>
    <tr>
      <td>w</td>
      <td>Spot width</td>
      <td>[0.75,2.25]spot[K]×AOI[N]×frame[F]</td>
    </tr>
    <tr>
      <td>x</td>
      <td>Center of the spot on the x-axis</td>
      <td>Rspot[K]×AOI[N]×frame[F]</td>
    </tr>
    <tr>
      <td>y</td>
      <td>Center of the spot on the y-axis</td>
      <td>Rspot[K]×AOI[N]×frame[F]</td>
    </tr>
    <tr>
      <td>μS</td>
      <td>2-D Gaussian spot</td>
      <td>R&gt;0spot[K]×AOI[N]×frame[F]×pixelX[P]×pixelY[P]</td>
    </tr>
    <tr>
      <td>μI</td>
      <td>Ideal image w/o offset</td>
      <td>R&gt;0AOI[N]×frame[F]×pixelX[P]×pixelY[P]</td>
    </tr>
    <tr>
      <td>δ</td>
      <td>Offset signal</td>
      <td>R&gt;0AOI[N]×frame[F]×pixelX[P]×pixelY[P]</td>
    </tr>
    <tr>
      <td>I</td>
      <td>Observed image w/o offset signal</td>
      <td>R&gt;0AOI[N]×frame[F]×pixelX[P]×pixelY[P]</td>
    </tr>
    <tr>
      <td>D</td>
      <td>Observed image (I+δ)</td>
      <td>R&gt;0AOI[N]×frame[F]×pixelX[P]×pixelY[P]</td>
    </tr>
    <tr>
      <td>xtarget</td>
      <td>Target molecule position on the x-axis</td>
      <td>[P/2−1,P/2]AOI[N]×frame[F]</td>
    </tr>
    <tr>
      <td>ytarget</td>
      <td>Target molecule position on the y-axis</td>
      <td>[P/2−1,P/2]AOI[N]×frame[F]</td>
    </tr>
    <tr>
      <td>i</td>
      <td>Pixel index on the x-axis</td>
      <td>{0,…,(P−1)}pixelX[P]</td>
    </tr>
    <tr>
      <td>j</td>
      <td>Pixel index on the y-axis</td>
      <td>{0,…,(P−1)}pixelX[P]</td>
    </tr>
    <tr>
      <td>W</td>
      <td>Width of the raw microscope images in pixels</td>
      <td>ℕ</td>
    </tr>
    <tr>
      <td>H</td>
      <td>Height of the raw microscope image in pixels</td>
      <td>ℕ</td>
    </tr>
    <tr>
      <td>Draw</td>
      <td>Raw microscope images</td>
      <td>R&gt;0frame[F]×pixelX[H]×pixelY[W]</td>
    </tr>
    <tr>
      <td>xtarget,raw</td>
      <td>Target molecule position in raw images on the x-axis</td>
      <td>[−0.5,H−0.5]AOI[N]×frame[F]</td>
    </tr>
    <tr>
      <td>ytarget,raw</td>
      <td>Target molecule position in raw images on the y-axis</td>
      <td>[−0.5,W−0.5]AOI[N]×frame[F]</td>
    </tr>
  </tbody>
</table>

#### Image likelihood

We model the image data $D$ as the sum of a photon-independent offset $\delta$ introduced by the camera and the noisy photon-dependent pixel intensity values $I$:

$$
D=\delta+I
$$

In our model, each pixel in the photon-dependent image $I$ has a variance which is equal to the mean intensity $\mu^{I}$ of that pixel multiplied by the camera gain $g$, which is the number of camera intensity units per photon. This formulation is appropriate for cameras that use charge-coupled device (CCD) or electron-multiplier CCD (EMCCD) sensors. (The experimental CoSMoS datasets we analyzed (Table 1) were collected with EMCCD cameras.) It accounts for both photon shot noise and additional noise introduced by EMCCD camera amplification (van Vliet et al., 1998) and is expressed using a continuous Gamma distribution:

$$
I∼Gamma(\mu^{I},\sqrt{\mu^{I}⋅g})
$$

The Gamma distribution was chosen because we found it to effectively model the image noise, which includes both Poissonian (shot noise) and non-Poissonian contributions. The Gamma distribution used here is parameterized by its mean and standard deviation. The functional forms of the Gamma distribution and all other distributions we use in this work are given in Table 4.

**Table 4.**
 Probability distributions used in the model.


<table>
  <thead>
    <tr>
      <th>Distribution</th>
      <th>PDF</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>x∼AffineBeta(μ,ν,a,b)</td>
      <td>yα−1(1−y)β−1B(α,β)whereα=ν(μ−a)b−a,β=ν(b−μ)b−a,andy=x−ab−a</td>
    </tr>
    <tr>
      <td>x∼Bernoulli(π)</td>
      <td>πx⁢(1-π)1-x</td>
    </tr>
    <tr>
      <td>x∼Beta(α,β)</td>
      <td>xα-1⁢(1-x)β-1B⁢(α,β)</td>
    </tr>
    <tr>
      <td>x∼Categorical(p)</td>
      <td>∏i=1kpi[x=i]</td>
    </tr>
    <tr>
      <td>x∼Empirical(z,p)</td>
      <td>∏i=1kpi[x=zi]</td>
    </tr>
    <tr>
      <td>x∼Exponential(λ)</td>
      <td>λ⁢e-λ⁢x</td>
    </tr>
    <tr>
      <td>x∼Gamma(μ,σ)</td>
      <td>βαΓ(α)xα−1e−βxwhereα=μ2σ2andβ=μσ2</td>
    </tr>
    <tr>
      <td>x∼HalfNormal(σ)</td>
      <td>2σπexp⁡(−x22σ2)forx&gt;0</td>
    </tr>
    <tr>
      <td>k∼TruncPoisson(λ,K)</td>
      <td>{1−e−λ∑i=0K−1λii!ifk=Kλke−λk!otherwise</td>
    </tr>
    <tr>
      <td>x∼Uniform(a,b)</td>
      <td>1b−aforx∈[a,b]</td>
    </tr>
  </tbody>
</table>

A competing camera technology based on scientific complementary metal-oxide semiconductor (sCMOS) sensors produces images that have also successfully been modeled as having a combination of Poissonian and non-Poissonian (Gaussian, in this case) noise sources. However, sCMOS images have noise characteristics that are considerably more complicated than CCD/EMCCD images, because every pixel has its own characteristic intensity offset, Gaussian noise variance, and amplification gain. Additional validation will be required to determine whether the existing cosmos model requires modification or inclusion of additional prior information (e.g., pixel-by-pixel calibration data as in Huang et al., 2013) to optimize its performance with sCMOS CoSMoS data.

#### Image model

The idealized noise-free image $\mu^{I}$ is represented as the sum of a background intensity $b$ and the intensities from fluorescence spots modeled as 2-D Gaussians $\mu^{S}$:

$$
\mu^{I}=b+\sumspot\mu^{S}
$$

For simplicity, we allow at most $K$ number of spots in each frame of each AOI. (In this article, we always use $K$ equal to 2.) The presence of a given spot in the image is encoded in the binary spot existence parameter $m$, where $m$ = 1 when the corresponding spot is present and $m$ = 0 when it is absent.

The intensities for a 2-D Gaussian spot at each pixel coordinate (i, $j$) is given by:

$$
\mu_{pixelX(i),pixelY(j)}^{S}=\frac{m⋅h}{2\piw^{2}}exp⁡(−\frac{(i−x−x^{target})^{2}+(j−y−y^{target})^{2}}{2w^{2}})
$$

with spot parameters total integrated intensity $h$, width $w$, and center ($x$, $y$) relative to the target (or off-target control) location ($x^{target}$, $y^{target}$).

Our primary interest is whether a target-specific spot is absent or present in a given AOI. We encode this information using a binary state parameter $z$ with 0 and 1 denoting target-specific spot absence and presence, respectively. To indicate which of the $K$ spots is target-specific, we use the index parameter $\theta$ which ranges from 0 to $K$. When a target-specific spot is present ($z$ = 1), $\theta\in{1,…,K}$ specifies the index of the target-specific spot, while $\theta$ = 0 indicates that no target-specific spot is present ($z$ = 0). For example, ${m_{spot(1)}=1,m_{spot(2)}=1,z=1,\theta=2}$ means that both spots are present and spot 2 is target-specific. A combination like ${m_{spot(1)}=0,m_{spot(2)}=1,z=1,\theta=1}$ is impossible (i.e., has zero probability) since spot 1 cannot be absent and target-specific at the same time. For off-target control data, in which no spots are target-specific by definition, $z$ and $\theta$ are always set to zero.

#### Prior distributions

The prior distributions for the model parameters are summarized in Figure 2—figure supplement 1 and detailed below. Unless otherwise indicated we assume largely uninformative priors (such as the Half-Normal distribution with large mean).

Background intensity $b$ follows a Gamma distribution:

$$
b∼Gamma(\mu^{b},\sigma^{b})
$$

where the mean $\mu^{b}\inR_{>0}^{AOI[N]}$ and standard deviation $\sigma^{b}\inR_{>0}^{AOI[N]}$ of the background intensity describe the irregularity in the background intensity in time and across the field of view of the microscope. Priors for $\mu^{b}$ and $\sigma^{b}$ are uninformative:

$$
\mu^{b}∼HalfNormal(1000)
$$



$$
\sigma^{b}∼HalfNormal(100)
$$

The target-specific presence parameter $z$ has a Bernoulli prior parameterized by the average target-specific binding probability $\pi$ for on-target AOIs and zero probability for control off-target AOIs:

$$
z∼{Bernoulli(\pi)on-target AOI0control off-target AOI
$$

The prior distribution for the index of the target-specific spot $\theta$ is conditional on $z$. When no specifically bound spot is present (i.e., $z$ = 0), $\theta$ always equals 0. Since spot indices are arbitrarily assigned, when the target-specific spot is present (i.e., $z$ = 1) $\theta$ can take any value between 1 and $K$ with equal probability. We represent the prior for $\theta$ as a Categorical distribution of the following form:

$$
\theta∼{0z=0Categorical([0,\frac{1}{K},…,\frac{1}{K}])z=1
$$

The average target-specific binding probability $\pi$ has an uninformative Jeffreys prior (Gelman et al., 2013) given by a Beta distribution:

$$
\pi∼Beta(1/2,1/2)
$$

The prior distribution for the spot presence indicator $m$ is conditional on $\theta$. When $\theta$ corresponds to spot index $k$, i.e., $\theta=k$, then $m_{spot(k)}$ = 1. When $\theta$ does not correspond to a spot index $k$, that is, $\theta\neqk$, then either spot $k$ is target-nonspecific or a spot corresponding to $k$ does not exist. Consequently, for $\theta\neqk$ we assign $m_{spot(k)}$ to either 0 or 1 with a probability dependent on the non-specific binding density $\lambda\inR_{>0}$:

$$
m_{spot}(k)∼{1\theta=kBernoulli(\suml=1K\frac{l⋅TruncPoisson(l;\lambda,K)}{K})\theta=0Bernoulli(\suml=1K−1\frac{l⋅TruncPoisson(l;\lambda,K−1)}{K−1})otherwise
$$

The mean non-specific binding density $\lambda$ is expected to be much less than two non-specifically bound spots per frame per AOI; therefore, we use an Exponential prior of the form

$$
\lambda∼Exponential(1)
$$

The prior distribution for the integrated spot intensity $h$ is chosen to fall off at a value much greater than typical spot intensity values

$$
h∼HalfNormal(10000)
$$

In CoSMoS experiments, the microscope/camera hardware is typically designed to set the width $w$ of fluorescence spots to a typical value in the range of 1–2 pixels (Ober et al., 2015). We use a Uniform prior confined to the range between 0.75 and 2.25 pixels:

$$
w∼Uniform(0.75,2.25)
$$

Priors for spot position ($x$, $y$) depend on whether the spot represents target-specific or non-specific binding. Non-specific binding to the microscope slide surface can occur anywhere within the image and therefore has a uniform distribution (Figure 2—figure supplement 2, red). Spot centers may fall slightly outside the AOI image yet still affect pixel intensities within the AOI. Therefore the range for ($x$, $y$) is extended one pixel wider than the size of the image, which allows a spot center to fall slightly beyond the AOI boundary.

In contrast to non-specifically bound molecules, specifically bound molecules are colocalized with the target molecule with a precision that can be better than one pixel and that depends on various factors including the microscope point-spread function and magnification, accuracy of registration between binder and target image channels, and accuracy of drift correction. For target-specific binding, we use an Affine-Beta prior with zero mean position relative to the target molecule location ($x^{target}$, $y^{target}$), and a ‘proximity’ parameter $\sigma^{x⁢y}$ which is the standard deviation of the Affine-Beta distribution (Figure 2—figure supplement 2, green). We chose the Affine-Beta distribution because it models a continuous parameter defined on a bounded interval.

$$
x_{spot(k)},y_{spot(k)}∼{AffineBeta(0,\sigma^{xy},−\frac{P+1}{2},\frac{P+1}{2})\theta=k (target-specific)Uniform(−\frac{P+1}{2},\frac{P+1}{2})\theta\neqk (target-nonspecific)
$$

We give the proximity parameter $\sigma^{x⁢y}$ a diffuse prior, an Exponential with a characteristic width of one pixel:

$$
\sigma^{xy}∼Exponential(1)
$$

Tests on data simulated with increasing proximity parameter values $\sigma^{x⁢y}$ (true) (i.e., with decreasing precision of spatial mapping between the binder and target image channels) confirm that the cosmos model accurately learns $\sigma^{x⁢y}$ (fit) from the data (Figure 3—figure supplement 3D; Table 5). This was the case even if we substituted a less-informative $\sigma^{x⁢y}$ prior (Uniform vs. Exponential; Table 5).

**Table 5.**
 The effect of mapping precision on classification accuracy*.


<table>
  <thead>
    <tr>
      <th>σx⁢y(true)</th>
      <th>σx⁢y(fit) [95% CI]</th>
      <th>MCC</th>
      <th>σx⁢y Prior</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0.2</td>
      <td>0.21 [0.20, 0.22]</td>
      <td>0.989</td>
      <td>Exponential(1)</td>
    </tr>
    <tr>
      <td>1</td>
      <td>0.96 [0.90, 1.02]</td>
      <td>0.939</td>
      <td>Exponential(1)</td>
    </tr>
    <tr>
      <td>1.5</td>
      <td>1.49 [1.40, 1.59]</td>
      <td>0.890</td>
      <td>Exponential(1)</td>
    </tr>
    <tr>
      <td>2</td>
      <td>1.96 [1.84, 2.09]</td>
      <td>0.834</td>
      <td>Exponential(1)</td>
    </tr>
    <tr>
      <td>2</td>
      <td>1.97 [1.84, 2.09]</td>
      <td>0.834</td>
      <td>Uniform(0,(P+1)/12)</td>
    </tr>
  </tbody>
</table>

_*Data were simulated over a range of proximity parameter σxy values at fixed π=0.15 and λ=0.15 (Supplementary file 6)._

The CoSMoS technique is premised on colocalization of the binder spots with the known location of the target molecule. Consequently, for any analysis method, classification accuracy declines when the images in the target and binder channels are less accurately mapped. For the Tapqir cosmos model, low mapping precision has little effect on classification accuracy at typical non-specific binding densities ($\lambda$ = 0.15; see MCC values in Table 5).

Gain $g$ depends on the settings of the amplifier and electron multiplier (if present) in the camera. It has a positive value and is typically in the range between 5 and 50. We use a Half-Normal prior with a broad distribution encompassing this range:

$$
g∼HalfNormal(50)
$$

The prior distribution for the offset signal $\delta$ is empirically measured from the output of camera sensor regions that are masked from incoming photons. Collected data from these pixels are transformed into a density histogram with intensity step size of 1. The resulting histogram typically has a long right hand tail of low density. For computational efficiency, we shorten this tail by binning together pixel intensity values from the upper 0.5% percentile. Since $D=\delta+I$ (Equation 1) and photon-dependent intensity $I$ is positive, all $D$ values have to be larger than the smallest offset intensity value. If that is not the case we add a single value $min⁡(D)-1$ to the offset empirical distribution which has a negligible effect on the distribution. Bin values $\delta_{samples}$ and their weights $\delta_{weights}$ are used to construct an Empirical prior:

$$
\delta∼Empirical(\delta_{samples},\delta_{weights})
$$

All simulated and experimental data sets in this work were analyzed using the prior distributions and hyperparameter values given above, which are compatible with a broad range of experimental conditions (Table 1). Many of the priors are uninformative and we anticipate that these will work well with images taken on variety of microscope hardware. However, it is possible that highly atypical microscope designs (e.g., those with effective magnifications that are sub-optimal for CoSMoS) might require adjustment of some fixed hyperparameters and distributions (those in Eqs. 6a, 6b, 11, 12, 13, 15, and 16). For example, if the microscope point spread function is more than 2 pixels wide, it may be necessary to increase the range of the $w$ prior in Eq. 13. The Tapqir documentation (https://tapqir.readthedocs.io/en/stable/) gives instructions for changing the hyperparameters.

### Joint distribution

The joint distribution of the data and all parameters is the fundamental distribution necessary to perform a Bayesian analysis. Let $ϕ$ be the set of all model parameters. The joint distribution can be expressed in a factorized form:

$$
p(D,ϕ)= p(g)p(\sigma^{xy})p(\pi)p(\lambda)\prodAOI[p(\mu^{b})p(\sigma^{b})\prodframe[\prodFp(b|\mu^{b},\sigma^{b})p(z|\pi)p(\theta|z)\prodpixelXpixelY⋅\prodspot[\prodFp(m|\theta,\lambda)p(h)p(w)p(x|\sigma^{xy},\theta)p(y|\sigma^{xy},\theta)]\prodpixelXpixelYp(\delta)p(D|\mu^{I},g,\delta)]]
$$

The Tapqir generative model is a stochastic function that describes a properly normalized joint distribution for the data and all parameters (Figure 8). In Pyro this is called ‘the model’.

### Inference

For a Bayesian analysis, we want to obtain the posterior distribution for parameters $ϕ$ given the observed data $D$. There are three discrete parameters $z$, $\theta$, and $\delta$ that can be marginalized out exactly so that they do not appear expilictly in either the joint posterior distribution or the likelihood function. Computationally efficient marginalization is implemented using Pyro’s enumeration strategy (Obermeyer et al., 2019a) and KeOps’ kernel operations on the GPU without memory overflows (Charlier et al., 2021). Let $ϕ^{′}=ϕ-{z,\theta,\delta}$ be the rest of the parameters. We obtain posterior distributions of $ϕ^{′}$ using Bayes’ rule:

$$
p(ϕ^{′}|D)=\frac{\sumz,\theta,\deltap(D,ϕ)}{\int_{ϕ}p(D,ϕ)dϕ}=\frac{p(D,ϕ^{′})}{\int_{ϕ}p(D,ϕ)dϕ}=\frac{p(D|ϕ^{′})p(ϕ^{′})}{\int_{ϕ}p(D,ϕ)dϕ}
$$

Note that the integral in the denominator of this expression is necessary to calculate the posterior distribution, but it is usually analytically intractable. However, variational inference provides a robust method to approximate the posterior distribution $p(ϕ^{′}∣D)$ with a parameterized variational distribution $q⁢(ϕ^{′})$ (Bishop, 2006).

$$
p(ϕ^{′}|D)≃q(ϕ^{′})
$$

$q⁢(ϕ^{′})$ has the following factorization:

$$
q(ϕ^{′})= q(g)q(\sigma^{xy})q(\pi)q(\lambda)⋅\prodAOI[q(\mu^{b})q(\sigma^{b})\prodframe[q(b)\prodspot[\prodFq(m)q(h|m)q(w|m)q(x|m)q(y|m)]]]
$$

The variational distribution $q⁢(ϕ^{′})$ is provided as pseudocode for a generative stochastic function (Figure 9). In Pyro this is called ‘the guide’. Variational inference is sensitive to initial values of variational parameters. In Figure 9, step 1 we provide the initial values of variational parameters used in our analyses.

![Figure 9.](https://cdn.elifesciences.org/articles/73860/elife-73860-fig9-v2.jpg)

### Calculation of spot probabilities

Variational inference directly optimizes $q(m)≡m_{prob}$ (see Eq. 21 and Figure 9), which approximates $p(m|D)$. To obtain the marginal posterior probabilities $p(z,\theta|D)$, we use a Monte Carlo sampling method:

$$
p(z,\theta|D)=\int_{ϕ^{′}}p(z,\theta,ϕ^{′}|D)dϕ^{′}=\int_{ϕ^{′}}p(z,\theta|ϕ^{′},D)p(ϕ^{′}|D)dϕ^{′}=\int_{ϕ^{′}}p(z,\theta|ϕ^{′},D)p(ϕ^{′}|D)dϕ^{′}=\int_{ϕ^{′}}\frac{p(z,\theta,ϕ^{′},D)}{\sumz,\thetap(z,\theta,ϕ^{′},D)}p(ϕ^{′}|D)dϕ^{′}≃\frac{1}{S}\sums=1S\frac{p(z,\theta,ϕ_{s}^{′},D)}{\sumz,\thetap(z,\theta,ϕ_{s}^{′},D)}whereϕ_{s}^{′}∼q(ϕ^{′})
$$

In our calculations, we used $S$ = 25 as the number of Monte Carlo samples. Marginal probabilities $p(z|D)$ and $p(\theta|D)$ are calculated as:

$$
p(z|D)=\sum\thetap(z,\theta|D)
$$



$$
p(\theta|D)=\sumzp(z,\theta|D)
$$

The probability, $p(specific)$, that a target-specific fluorescence spot is present in a given image by definition is:

$$
p(specific)≡p(z=1|D)
$$

For simplicity in the main text and figures we suppress the conditional dependency on $D$ in $p(\theta|D)$ and $p(m|D)$ and instead write them as $p⁢(\theta)$ and $p⁢(m)$, respectively.

### Tapqir implementation

The model and variational inference method outlined above are implemented as a probabilistic program in the Python-based probabilistic programming language (PPL) Pyro (Foerster et al., 2018; Bingham et al., 2019; Obermeyer et al., 2019a). We use a variational approximation because exact inference is not analytically tractable for a model as complex as cosmos. As currently implemented in Pyro, variational inference is significantly faster than Monte Carlo inference methods. In Tapqir, the objective that is being optimized is the evidence lower bound (ELBO) estimator that provides unbiased gradient estimates upon differentiation. At each iteration of inference procedure we choose a random subset of AOIs and frames (mini-batch), compute a differentiable ELBO estimate based on this mini-batch and update the variational parameters via automatic differentiation. We use PyTorch’s Adam optimizer (Kingma and Ba, 2014) with the learning rate of $5\times10^{-3}$ and keep other parameters at their default values.

### Credible intervals and confidence intervals

Credible intervals were calculated from posterior distribution samples as the highest density region (HDR), the narrowest interval with probability mass 95% using the pyro.ops.stats.hpdi Pyro function. Confidence intervals were calculated from bootstrap samples as the 95% HDR.

### Data simulation

Simulated data were produced using the generative model (Figure 8). Each simulation has a subset of parameters ($\pi,\lambda$, $g$, $\sigma^{x⁢y}$, $b$, $h$, $w,\delta$) set to desired values while the remaining parameters ($z,\theta$, $m$, $x$, $y$) and resulting noisy images ($D$) are sampled from distributions. The fixed parameter values and data set sizes for all simulations are provided inSupplementary file 1; Supplementary file 2; Supplementary file 3; Supplementary file 4; Supplementary file 5; Supplementary file 6.

For kinetic simulations (Figure 5, Supplementary file 5), $z$ was modeled using a discrete Markov process with the initial probability and the transition probability matrices:

$$
p(z_{frame(0)}|k_{on},k_{off})=Categorical([\frac{k_{off}}{k_{on}+k_{off}}\frac{k_{on}}{k_{on}+k_{off}}])
$$



$$
p(z_{frame(f)}|z_{frame(f−1)},k_{on},k_{off})=Categorical([1−k_{on}k_{on}k_{off}1−k_{off}])
$$

where $k_{on}$ and $k_{off}$ are transition probabilities that numerically approximate the pseudo-first-order binding and first-order dissociation rate constants in units of $s^{−1}$, respectively, assuming 1 s/frame. We assumed that the Markov process is at equilibrium and initialized the chain with the equilibrium probabilities.

### Posterior predictive sampling

For posterior predictive checking, sampled images ($D~$) were produced using Tapqir’s generative model (Figure 8) where model parameters were sampled from the posterior distribution $p⁢(ϕ|D)$, which was approximated by the variational distribution $q⁢(ϕ)$:

$$
D~∼p(D~|D)=\int_{ϕ}p(D~|ϕ)p(ϕ|D)dϕ≃\int_{ϕ}p(D~|ϕ)q(ϕ)dϕ
$$

### Signal-to-noise ratio

We define SNR as:

$$
SNR=mean(\frac{signal}{\sqrt{\sigma_{offset}^{2}+\sigma_{background}^{2}}})
$$

where $\sigma_{background}^{2}=b⋅g$ the variance of the background intensity, $\sigma_{offset}^{2}$ the variance of the offset intensity, and the mean is taken over all target-specific spots. For experimental data, $signal$ is calculated as

$$
signal=\sumpixelXpixelY(D−b_{mean}−\delta_{mean})⋅weight
$$

where $weight$ is

$$
weight=\frac{1}{2\pi⋅w^{2}}exp⁡(−\frac{(i−x−x^{target})^{2}+(j−y−y^{target})^{2}}{2⋅w^{2}})
$$

For simulated data theoretical $signal$ is directly calculated as:

$$
signal=\sumpixelXpixelYh⋅weight^{2}
$$

### Classification accuracy statistics

As a metric of classification accuracy we use three commonly used statistics – recall, precision, and Matthews Correlation Coefficient (Matthews, 1975)

$$
Recall=\frac{TP}{TP+FN}
$$



$$
Precision=\frac{TP}{TP+FP}
$$



$$
MCC=\frac{TP⋅TN−FP⋅FN}{\sqrt{(TP+FP)(TP+FN)(TN+FP)(TN+FN)}}
$$

where TP is true positives, TN is true negatives, FP is false positives, and FN is false negatives.

### Kinetic and thermodynamic analysis

To estimate simple binding/dissociation kinetic parameters (Figure 5C and D), we sample binary time records $z$ from the inferred $p(specific)$ time records for all AOIs. For a two-state hidden Markov model, the maximum-likelihood estimates of $k_{on}$ and $k_{off}$ are given by:

$$
k^_{on},k^_{off}=argmaxk_{on},k_{off}⁡\prodAOI[p(z_{frame(0)}|k_{on},k_{off})\prodf=1F−1p(z_{frame(f)}|z_{frame(f−1)},k_{on},k_{off})]
$$

Repeating this procedure 2,000 times gave the distributions of $k_{on}$ and $k_{off}$ from which we compute mean and 95% credible interval.

Similarly, to estimate mean and 95% CI of $K_{eq}$ (Figure 5E) we sampled π from $q⁢(\pi)$ and for each sampled value of $\pi$ calculated $K_{eq}$ as:

$$
K_{eq}=\frac{\pi}{1−\pi}
$$

To calculate time-to-first binding kinetics from the Tapqir-derived $p(specific)$ (Figure 6B, Figure 6—figure supplement 1B, Figure 6—figure supplement 2B, and Figure 6—figure supplement 3B), 2,000 binary time records $z$ were sampled from the $p(specific)$ time record for each AOI. For each sampled time record initial absent intervals were measured and analyzed using Equation 7 in Friedman and Gelles, 2015, yielding distributions of $k_{a}$, $k_{ns}$, and $A_{f}$. Mean value and 95% credible intervals were calculated from these distributions. Initial absent intervals from ‘spot-picker’ analysis (Figure 6C, Figure 6—figure supplement 1C, Figure 6—figure supplement 2C, and Figure 6—figure supplement 3C) were analyzed as described in Friedman and Gelles, 2015, except that on-target and off-target data were here analyzed jointly instead of being analyzed sequentially (Friedman and Gelles, 2015). Note that the $k_{ns}$ values determined using the two methods are not directly comparable for several reasons, including that the non-specific binding frequencies are effectively measured over different areas. For Tapqir, the target area is approximately $\pi⁢(\sigma^{x⁢y})^{2}$ (which is between 0.3 and 0.8 pixels2 in the different experimental data sets) and for spot-picker the area is subjectively chosen as $\pi⋅1.5^{2}=7$ pixels2.
