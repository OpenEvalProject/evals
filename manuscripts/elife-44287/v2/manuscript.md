# A statistical framework to assess cross-frequency coupling while accounting for confounding analysis effects

## Authors

- Jessica K Nadalin<sup>1</sup>
- Louis-Emmanuel Martinet<sup>2</sup>
- Ethan B Blackwood<sup>3</sup> ([ORCID: 0000-0002-3049-0640](https://orcid.org/0000-0002-3049-0640))
- Meng-Chen Lo<sup>3</sup> ([ORCID: 0000-0003-3913-3233](https://orcid.org/0000-0003-3913-3233))
- Alik S Widge<sup>3</sup> ([ORCID: 0000-0001-8510-341X](https://orcid.org/0000-0001-8510-341X))
- Sydney S Cash<sup>2</sup>
- Uri T Eden<sup>1</sup>
- Mark A Kramer<sup>1</sup> ([ORCID: 0000-0002-9979-7202](https://orcid.org/0000-0002-9979-7202)) †

### Affiliations

1. Department of Mathematics and Statistics Boston University Boston United States
2. Department of Neurology Massachusetts General Hospital Boston United States
3. Department of Psychiatry University of Minnesota Minneapolis United States

† Corresponding author

## Abstract

Cross frequency coupling (CFC) is emerging as a fundamental feature of brain activity, correlated with brain function and dysfunction. Many different types of CFC have been identified through application of numerous data analysis methods, each developed to characterize a specific CFC type. Choosing an inappropriate method weakens statistical power and introduces opportunities for confounding effects. To address this, we propose a statistical modeling framework to estimate high frequency amplitude as a function of both the low frequency amplitude and low frequency phase; the result is a measure of phase-amplitude coupling that accounts for changes in the low frequency amplitude. We show in simulations that the proposed method successfully detects CFC between the low frequency phase or amplitude and the high frequency amplitude, and outperforms an existing method in biologically-motivated examples. Applying the method to in vivo data, we illustrate examples of CFC during a seizure and in response to electrical stimuli.

## Introduction

Brain rhythms - as recorded in the local field potential (LFP) or scalp electroencephalogram (EEG) - are believed to play a critical role in coordinating brain networks. By modulating neural excitability, these rhythmic fluctuations provide an effective means to control the timing of neuronal firing (Engel et al., 2001; Buzsáki and Draguhn, 2004). Oscillatory rhythms have been categorized into different frequency bands (e.g., theta [4–10 Hz], gamma [30–80 Hz]) and associated with many functions: the theta band with memory, plasticity, and navigation (Engel et al., 2001); the gamma band with local coupling and competition (Kopell et al., 2000; Börgers et al., 2008). In addition, gamma and high-gamma (80–200 Hz) activity have been identified as surrogate markers of neuronal firing (Rasch et al., 2008; Mukamel et al., 2005; Fries et al., 2001; Pesaran et al., 2002; Whittingstall and Logothetis, 2009; Ray and Maunsell, 2011), observable in the EEG and LFP.

In general, lower frequency rhythms engage larger brain areas and modulate spatially localized fast activity (Bragin et al., 1995; Chrobak and Buzsáki, 1998; von Stein and Sarnthein, 2000; Lakatos et al., 2005; Lakatos et al., 2008). For example, the phase of low frequency rhythms has been shown to modulate and coordinate neural spiking (Vinck et al., 2010; Hyafil et al., 2015b; Fries et al., 2007) via local circuit mechanisms that provide discrete windows of increased excitability. This interaction, in which fast activity is coupled to slower rhythms, is a common type of cross-frequency coupling (CFC). This particular type of CFC has been shown to carry behaviorally relevant information (e.g., related to position [Jensen and Lisman, 2000; Agarwal et al., 2014], memory [Siegel et al., 2009], decision making and coordination [Dean et al., 2012; Pesaran et al., 2008; Wong et al., 2016; Hawellek et al., 2016]). More generally, CFC has been observed in many brain areas (Bragin et al., 1995; Chrobak and Buzsáki, 1998; Csicsvari et al., 2003; Tort et al., 2008; Mormann et al., 2005; Canolty et al., 2006), and linked to specific circuit and dynamical mechanisms (Hyafil et al., 2015b). The degree of CFC in those areas has been linked to working memory, neuronal computation, communication, learning and emotion (Tort et al., 2009; Jensen et al., 2016; Canolty and Knight, 2010; Dejean et al., 2016; Karalis et al., 2016; Likhtik et al., 2014; Jones and Wilson, 2005; Lisman, 2005; Sirota et al., 2008), and clinical disorders (Gordon, 2016; Widge et al., 2017; Voytek and Knight, 2015; Başar et al., 2016; Mathalon and Sohal, 2015), including epilepsy (Weiss et al., 2015). Although the cellular mechanisms giving rise to some neural rhythms are relatively well understood (e.g. gamma [Whittington et al., 2000; Whittington et al., 2011; Mann and Mody, 2010]), the neuronal substrate of CFC itself remains obscure.

Analysis of CFC focuses on relationships between the amplitude, phase, and frequency of two rhythms from different frequency bands. The notion of CFC, therefore, subsumes more specific types of coupling, including: phase-phase coupling (PPC), phase-amplitude coupling (PAC), and amplitude-amplitude coupling (AAC) (Hyafil et al., 2015b). PAC has been observed in rodent striatum and hippocampus (Tort et al., 2008) and human cortex (Canolty et al., 2006), AAC has been observed between the alpha and gamma rhythms in dorsal and ventral cortices (Popov et al., 2018), and between theta and gamma rhythms during spatial navigation (Shirvalkar et al., 2010), and both PAC and AAC have been observed between alpha and gamma rhythms (Osipova et al., 2008). Many quantitative measures exist to characterize different types of CFC, including: mean vector length or modulation index (Canolty et al., 2006; Tort et al., 2010), phase-locking value (Mormann et al., 2005; Lachaux et al., 1999; Vanhatalo et al., 2004), envelope-to-signal correlation (Bruns and Eckhorn, 2004), analysis of amplitude spectra (Cohen, 2008), coherence between amplitude and signal (Colgin et al., 2009), coherence between the time course of power and signal (Osipova et al., 2008), and eigendecomposition of multichannel covariance matrices (Cohen, 2017). Overall, these different measures have been developed from different principles and made suitable for different purposes, as shown in comparative studies (Tort et al., 2010; Cohen, 2008; Penny et al., 2008; Onslow et al., 2011).

Despite the richness of this methodological toolbox, it has limitations. For example, because each method focuses on one type of CFC, the choice of method restricts the type of CFC detectable in data. Applying a method to detect PAC in data with both PAC and AAC may: (i) falsely report no PAC in the data, or (ii) miss the presence of significant AAC in the same data. Changes in the low frequency power can also affect measures of PAC; increases in low frequency power can increase the signal to noise ratio of phase and amplitude variables, increasing the measure of PAC, even when the phase-amplitude coupling remains constant (Aru et al., 2015; van Wijk et al., 2015; Jensen et al., 2016). Furthermore, many experimental or clinical factors (e.g., stimulation parameters, age or sex of subject) can impact CFC in ways that are difficult to characterize with existing methods (Cole and Voytek, 2017). These observations suggest that an accurate measure of PAC would control for confounding variables, including the power of low frequency oscillations.

To that end, we propose here a generalized linear model (GLM) framework to assess CFC between the high-frequency amplitude and, simultaneously, the low frequency phase and amplitude. This formal statistical inference framework builds upon previous work (Kramer and Eden, 2013; Penny et al., 2008; Voytek et al., 2013; van Wijk et al., 2015) to address the limitations of existing CFC measures. In what follows, we show that this framework successfully detects CFC in simulated signals. We compare this method to the modulation index, and show that in signals with CFC dependent on the low-frequency amplitude, the proposed method more accurately detects PAC than the modulation index. We apply this framework to in vivo recordings from human and rodent cortex to show examples of PAC and AAC detected in real data, and how to incorporate new covariates directly into the model framework.

## Materials and methods

### Estimation of the phase and amplitude envelope

To study CFC we estimate three quantities: the phase of the low frequency signal, $ϕ_{low}$; the amplitude envelope of the high frequency signal, $A_{high}$; and the amplitude envelope of the low frequency signal, $A_{low}$. To do so, we first bandpass filter the data into low frequency (4–7 Hz) and high frequency (100–140 Hz) signals, $V_{low}$ and $V_{high}$, respectively, using a least-squares linear-phase FIR filter of order 375 for the high frequency signal, and order 50 for the low frequency signal. Here we choose specific high and low frequency ranges of interest, motivated by previous in vivo observations (Canolty et al., 2006; Tort et al., 2008; Scheffer-Teixeira et al., 2013). However, we note that this method is flexible and not dependent on this choice. We select a wide high frequency band consistent with recommendations from the literature (Aru et al., 2015) and the mechanistic explanation that extracellular spikes produce this broadband high frequency activity (Scheffer-Teixeira et al., 2013). We use the Hilbert transform to compute the analytic signals of $V_{low}$ and $V_{high}$, and from these compute the phase and amplitude of the low frequency signal $(A_{low}$ and $ϕ_{low})$ and the amplitude of the high frequency signal $(A_{high})$.

### Modeling framework to assess CFC

Generalized linear models (GLMs) provide a principled framework to assess CFC (Penny et al., 2008; Kramer and Eden, 2013; van Wijk et al., 2015). Here, we present three models to analyze different types of CFC. The fundamental logic behind this approach is to model the distribution of $A_{high}$ as a function of different predictors. In existing measures of PAC, the distribution of $A_{high}$ versus $ϕ_{low}$ is assessed using a variety of different metrics (e.g., Tort et al., 2010). Here, we estimate statistical models to fit $A_{high}$ as a function of $ϕ_{low}$, $A_{low}$, and their combinations. If these models fit the data sufficiently well, then we estimate distances between the modeled surfaces to measure the impact of each predictor.

#### The ϕlow model

The $ϕ_{low}$ model relates $A_{high}$, the response variable, to a linear combination of $ϕ_{low}$, the predictor variable, expressed in a spline basis:

$$
A_{high}|ϕ_{low}∼Gamma⁢[\mu,ν]
$$



$$
log⁡\mu=\sumk=1n\beta_{k}⁢f_{k}⁢(ϕ_{low}),
$$

where the conditional distribution of $A_{high}$ given $ϕ_{low}$ is modeled as a Gamma random variable with mean parameter $\mu$ and shape parameter $ν$, and $\beta_{k}$ are undetermined coefficients, which we refer to collectively as $\beta_{ϕ_{low}}$. We choose this distribution as it guarantees real, positive amplitude values; we note that this distribution provides an acceptable fit to the example human data analyzed here (Figure 1). The functions ${f_{1},⋯,f_{n}}$ correspond to spline basis functions, with $n$ control points equally spaced between 0 and $2⁢\pi$, used to approximate $ϕ_{low}$. We note that the spline functions sum to 1, and therefore we omit a constant offset term. We use a tension parameter of 0.5, which controls the smoothness of the splines. We note that, because the link function of the conditional mean of the response variable $(A_{high})$ varies linearly with the model coefficients $\beta_{k}$ the model is a GLM, though the spline basis functions situate the model in the larger class of Generalized Additive Models (GAMs). Here we fix $n=10$, which is a reasonable choice for smooth PAC with one or two broad peaks (Kramer and Eden, 2013). To support this choice, we apply an AIC-based selection procedure to 1000 simulated instances of signals of duration 20 s with phase-amplitude coupling and amplitude-amplitude coupling (see Materials and methods: Synthetic Time Series with PAC and Synthetic Time Series with AAC, below, for simulation details). For each simulation, we fit the model in Equation 1 to these data for 27 different values of $n$ from $n=4$ to $n=30$. For each simulated signal, we record the value of $n$ that minimizes the AIC, defined as

$$
AIC=Δ+2n,
$$

where $Δ$ is the deviance from the model in Equation 1. The values of $n$ that minimize the AIC tend to lie between $n=7$ and $n=12$ (Figure 2). These simulations support the choice of $n=10$ as a sufficient number of splines.

![Figure 1.](https://cdn.elifesciences.org/articles/44287/elife-44287-fig1-v2.jpg)

**Figure 1.:** Three examples of 20 s duration recorded from a single electrode during a human seizure. In each case, the gamma fit (red curve) provides an acceptable fit to the empirical distributions of the high frequency amplitude.

![Figure 2.](https://cdn.elifesciences.org/articles/44287/elife-44287-fig2-v2.jpg)

**Figure 2.:** Distribution of the number of control points $(n)$ that minimize the AIC.Values of $n$ between 7 and 12 minimize the AIC in a simulation with phase-amplitude coupling and amplitude-amplitude coupling.

For a more detailed discussion and simulation examples of the PAC model, see Kramer and Eden (2013). We note that the choices of distribution and link function differ from those in Penny et al. (2008) and van Wijk et al. (2015), where the normal distribution and identity link are used instead.

#### The Alow model

The $A_{low}$ model relates the high frequency amplitude to the low frequency amplitude:

$$
A_{high}|A_{low}∼Gamma⁢[\mu,ν]
$$



$$
log⁡\mu=\beta_{1}+\beta_{2}⁢A_{low},
$$

where the conditional distribution of $A_{high}$ given $A_{low}$ is modeled as a Gamma random variable with mean parameter $\mu$ and shape parameter $ν$. The predictor consists of a single variable and a constant, and the length of the coefficient vector $\beta_{A_{low}}={\beta_{1},\beta_{2}}$ is 2.

#### The Alow,ϕlow model

The $A_{low},ϕ_{low}$ model extends the $ϕ_{low}$ model in Equation 1 by including three additional predictors in the GLM: $A_{low}$, the low frequency amplitude; and interaction terms between the low frequency amplitude and the low frequency phase: $A_{low}sin⁡(ϕ_{low})$, and $A_{low}cos⁡(ϕ_{low})$. These new terms allow assessment of phase-amplitude coupling while accounting for linear amplitude-amplitude dependence and more complicated phase-dependent relationships on the low frequency amplitude without introducing many more parameters. Compared to the original $ϕ_{low}$ model in Equation 1, including these new terms increases the number of variables to $n+3$, and the length of the coefficient vector $\beta_{A_{low},ϕ_{low}}$ to $n+3$. These changes result in the following model:

$$
A_{high}|ϕ_{low},A_{low}∼Gamma⁢[\mu,ν],
$$



$$
log⁡\mu=\sumk=1n\beta_{k}⁢f_{k}⁢(ϕ_{low})+\beta_{n+1}⁢A_{low}+\beta_{n+2}⁢A_{low}⁢sin⁡(ϕ_{low})+\beta_{n+3}⁢A_{low}⁢cos⁡(ϕ_{low}).
$$

Here, the conditional distribution of $A_{high}$ given $ϕ_{low}$ and $A_{low}$ is modeled as a Gamma random variable with mean parameter $\mu$ and shape parameter $ν$, and $\beta_{k}$ are undetermined coefficients. We note that we only consider two interaction terms, rather than the spline basis function of phase, to limit the number of parameters in the model.

### The statistics RPAC and RAAC

We compute two measures of CFC, $R_{PAC}$ and $R_{AAC}$ which use the three models defined in the previous section. We evaluate each model in the three-dimensional space ($ϕ_{low}$, $A_{low}$, $A_{high}$) and calculate the statistics $R_{PAC}$ and $R_{AAC}$. We use the MATLAB $(R⁢R⁢I⁢D:S⁢C⁢R_{0}⁢01622)$ function fitglm to estimate the models; we note that this procedure estimates the dispersion directly for the gamma distribution. In what follows, we first discuss the three model surfaces estimated from the data, and then how we use these surfaces to compute the statistics $R_{PAC}$ and $R_{AAC}$.

To create the surface $S_{A_{low},ϕ_{low}}$, which fits the $A_{low},ϕ_{low}$ model in the three-dimensional ($A_{low}$, $ϕ_{low}$, $A_{high}$) space, we first compute estimates of the parameters $\beta_{A_{low},ϕ_{low}}$ in Equation 3. We then estimate $A_{high}$ by fixing $A_{low}$ at one of 640 evenly spaced values between the 5th and 95th quantiles of $A_{low}$ observed; we choose these quantiles to avoid extremely small or large values of $A_{low}$. Finally, at the fixed $A_{low}$, we compute the high frequency amplitude values from the $A_{low},ϕ_{low}$ model over 100 evenly spaced values of $ϕ_{low}$ between $-\pi$ and $\pi$. This results in a two-dimensional curve $C_{A_{low},ϕ_{low}}$ in the two-dimensional ($ϕ_{low}$, $A_{high}$) space with fixed $A_{low}$. We repeat this procedure for all 640 values of $A_{low}$ to create a surface $S_{A_{low},ϕ_{low}}$ in the three-dimensional space ($A_{low}$, $ϕ_{low}$, $A_{high}$) (Figure 3C). To create the surface $S_{A_{low}}$, which fits the $A_{low}$ model in the three-dimensional ($A_{low}$, $ϕ_{low}$, $A_{high}$) space, we estimate the coefficient vector $\beta_{A_{low}}$ for the model in Equation 2. We then estimate the high frequency amplitude over 640 evenly spaced values between the 5th and 95th quantiles of $A_{low}$ observed, again to avoid extremely small or large values of $A_{low}$. This creates a mean response function which appears as a curve $C_{A_{low}}$ in the two-dimensional ($A_{low}$, $A_{high}$) space. We extend this two-dimensional curve to a three-dimensional surface $S_{A_{low}}$ by extending $C_{A_{low}}$ along the $ϕ_{low}$ dimension (Figure 3A).

![Figure 3.](https://cdn.elifesciences.org/articles/44287/elife-44287-fig3-v2.jpg)

**Figure 3.:** Example model surfaces used to determine $R_{PAC}$ and $R_{AAC}$.(A,B,C) Three example surfaces (A) $S_{A_{low}}$, (B) $S_{ϕ_{low}}$, and (C) $S_{A_{low},ϕ_{low}}$ in the three-dimensional space ($A_{low}$, $ϕ_{low}$, $A_{high}$). (D) The maximal distance between the surfaces $S_{A_{low}}$ (red) and $S_{A_{low},ϕ_{low}}$ (yellow) is used to compute $R_{PAC}$. (E) The maximal distance between the surfaces $S_{ϕ_{low}}$ (blue) and $S_{A_{low},ϕ_{low}}$ (yellow) is used to compute $R_{AAC}$.

To create the surface $S_{ϕ_{low}}$, which fits the $ϕ_{low}$ model in the three-dimensional ($A_{low}$, $ϕ_{low}$, $A_{high}$) space, we first estimate the coefficients $\beta_{ϕ_{low}}$ for the model in Equation 1. From this, we then compute estimates for the high frequency amplitude using the $ϕ_{low}$ model with 100 evenly spaced values of $ϕ_{low}$ between $-\pi$ and $\pi$. This results in the mean response function of the $ϕ_{low}$ model. We extend this curve $C_{ϕ_{low}}$ in the $A_{low}$ dimension to create a surface $S_{ϕ_{low}}$ in the three-dimensional ($A_{low}$, $ϕ_{low}$, $A_{high}$) space. The surface $S_{ϕ_{low}}$ has the same structure as the curve $C_{ϕ_{low}}$ in the ($ϕ_{low}$, $A_{high}$) space, and remains constant along the dimension $A_{low}$ (Figure 3B).

The statistic $R_{PAC}$ measures the effect of low frequency phase on high frequency amplitude, while accounting for fluctuations in the low frequency amplitude. To compute this statistic, we note that the model in Equation 3 measures the combined effect of $A_{low}$ and $ϕ_{low}$ on $A_{high}$, while the model in Equation 2 measures only the effect of $A_{low}$ on $A_{high}$. Hence, to isolate the effect of $ϕ_{low}$ on $A_{high}$, while accounting for $A_{low}$, we compare the difference in fits between the models in Equations 2 and 3. We fit the mean response functions of the models in Equations 2 and 3, and calculate $R_{PAC}$ as the maximum absolute fractional difference between the resulting surfaces $S_{A_{low},ϕ_{low}}$ and $S_{A_{low}}$ (Figure 3D):

$$
R_{PAC}=max[abs[1−S_{A_{low}}/S_{A_{low},ϕ_{low}}]],
$$

That is we measure the largest distance between the $A_{low}$ and the $A_{low},ϕ_{low}$ models. We expect fluctuations in $S_{A_{low},ϕ_{low}}$ not present in $S_{A_{low}}$ to be the result of $ϕ_{low}$, that is PAC. In the absence of PAC, we expect the surfaces $S_{A_{low},ϕ_{low}}$ and $S_{A_{low}}$ to be very close, resulting in a small value of $R_{PAC}$. However, in the presence of PAC, we expect $S_{A_{low},ϕ_{low}}$ to deviate from $S_{A_{low}}$, resulting in a large value of $R_{PAC}$. We note that this measure, unlike R2 metrics for linear regression, is not meant to measure the goodness-of-fit of these models to the data, but rather the differences in fits between the two models. We also note that $R_{PAC}$ is an unbounded measure, as it equals the maximum absolute fractional difference between distributions, which may exceed 1.

To compute the statistic $R_{AAC}$, which measures the effect of low frequency amplitude on high frequency amplitude while accounting for fluctuations in the low frequency phase, we compare the difference in fits of the model in Equation 3 from the model in Equation 1. We note that the model in Equation 3 predicts $A_{high}$ as a function of $A_{low}$ and $ϕ_{low}$, while the model in Equation 1 predicts $A_{high}$ as a function of $ϕ_{low}$ only. Therefore we expect a difference in fits between the models in Equations 1 and 3 results from the effects of $A_{low}$ on $A_{high}$. We fit the mean response functions of the models in Equations 1 and 3 in the three-dimensional ($ϕ_{low}$, $A_{low}$, $A_{high}$) space, and calculate $R_{AAC}$ as the maximum absolute fractional difference between the resulting surfaces $S_{A_{low},ϕ_{low}}$ and $S_{ϕ_{low}}$ (Figure 3E):

$$
R_{AAC}=max[abs[1−S_{ϕ_{low}}/S_{A_{low},ϕ_{low}}]].
$$

That is we measure the distance between the $ϕ_{low}$ and the $A_{low},ϕ_{low}$ models. We expect fluctuations in $S_{A_{low},ϕ_{low}}$ not present in $S_{ϕ_{low}}$ to be the result of $A_{low}$, that is AAC. In the absence of AAC, we expect the surfaces $S_{A_{low},ϕ_{low}}$ and $S_{ϕ_{low}}$ to be very close, resulting in a small value for $R_{AAC}$. Alternatively, in the presence of AAC, we expect $S_{A_{low},ϕ_{low}}$ to deviate from $S_{ϕ_{low}}$, resulting in a large value of $R_{AAC}$.

### Estimating 95% confidence intervals for RPAC and RAAC

We compute 95% confidence intervals for $R_{PAC}$ and $R_{AAC}$ via a parametric bootstrap method (Kramer and Eden, 2013). Given a vector of estimated coefficients $\beta_{x}$ for $x={A_{low}; ϕ_{low};orA_{low},ϕ_{low}}$, we use its estimated covariance and estimated mean to generate 10,000 normally distributed coefficient sample vectors $\beta_{x}^{j}$, $j\in{0,…,10000}$. For each $\beta_{x}^{j}$, we then compute the high frequency amplitude values from the $A_{low}$, $ϕ_{low}$, or $A_{low},ϕ_{low}$ model, $S_{x}^{j}$. Finally, we compute the statistics $R_{PAC}^{j}$ and $R_{AAC}^{j}$ for each $j$ as,

$$
R_{PAC}^{j}=max[abs[1−S_{A_{low}}^{j}/S_{A_{low},ϕ_{low}}^{j}]],
$$



$$
R_{AAC}^{j}=max[abs[1−S_{ϕ_{low}}^{j}/S_{A_{low},ϕ_{low}}^{j}]].
$$

The 95% confidence intervals for the statistics are the values of $R_{PAC}^{j}$ and $R_{AAC}^{j}$ at the 0.025 and 0.975 quantiles (Kramer and Eden, 2013).

### Assessing significance of AAC and PAC with bootstrap p-values

To assess whether evidence exists for significant PAC or AAC, we implement a bootstrap procedure to compute p-values as follows. Given two signals $V_{low}$ and $V_{high}$, and the resulting estimated statistics $R_{PAC}$ and $R_{AAC}$ we apply the Amplitude Adjusted Fourier Transform (AAFT) algorithm (Theiler et al., 1992) on $V_{high}$ to generate a surrogate signal $V_{high}^{i}$. In the AAFT algorithm, we first reorder the values of $V_{high}$ by creating a random Gaussian signal $W$ and ordering the values of $V_{high}$ to match $W$. For example, if the highest value of $W$ occurs at index $j$, then the highest value of $V_{high}$ will be reordered to occur at index $j$. Next, we apply the Fourier Transform (FT) to the reordered $V_{high}$ and randomize the phase of the frequency domain signal. This signal is then inverse Fourier transformed and rescaled to have the same amplitude distribution as the original signal $V_{high}$. In this way, the algorithm produces a permutation $V_{high}^{i}$ of $V_{high}$ such that the power spectrum and amplitude distribution of the original signal are preserved.

We create 1000 such surrogate signals $V_{high}^{i}$, and calculate $R_{PAC}^{i}$ and $R_{AAC}^{i}$ between $V_{low}$ and each $V_{high}^{i}$. We define the p-values $p_{PAC}$ and $p_{AAC}$ as the proportion of values in ${𝐑_{PAC}^{i}}_{i=1}^{1000}$ and ${𝐑_{AAC}^{i}}_{i=1}^{1000}$ greater than the estimated statistics $R_{PAC}$ and $R_{AAC}$, respectively. If the proportion is zero, we set $p=0.0005$.

We calculate p-values for the modulation index in the same way. The modulation index calculates the distribution of high frequency amplitudes versus low frequency phases and measures the distance from this distribution to a uniform distribution of amplitudes. Given the signals $V_{low}$ and $V_{high}$, and the resulting modulation index MI between them, we calculate the modulation index between $V_{low}$ and 1000 surrogate permutations of $V_{high}$ using the AAFT algorithm. We set $p_{MI}$ to be the proportion of these resulting values greater than the MI value estimated from the original signals.

### Synthetic time series with PAC

We construct synthetic time series to examine the performance of the proposed method as follows. First, we simulate 20 s of pink noise data such that the power spectrum scales as $1/f$. We then filter these data into low (4–7 Hz) and high (100–140 Hz) frequency bands, as described in Materials and methods: Estimation of the phase and amplitude envelope, creating signals $V_{low}$ and $V_{high}$. Next, we couple the amplitude of the high frequency signal to the phase of the low frequency signal. To do so, we first locate the peaks of $V_{low}$ and determine the times $t_{k},k={1,2,3,…,K}$, of the $K$ relative extrema. We note that these times correspond approximately to $ϕ_{low}=0$. We then create a smooth modulation signal M which consists of a 42 ms Hanning window of height $1+I_{PAC}$ centered at each $t_{k}$, and a value of 1 at all other times (Figure 4A). The intensity parameter $I_{PAC}$ in the modulation signal corresponds to the strength of PAC. $I_{PAC}=0.0$ corresponds to no PAC, while $I_{PAC}=1.0$ results in a 100% increase in the high frequency amplitude at each $t_{k}$, creating strong PAC. We create a new signal $V_{high}^{′}$ with the same phase as $V_{high}$, but with amplitude dependent on the phase of $V_{low}$ by setting,

$$
V_{high}^{′}=MV_{high}.
$$

We create the final voltage trace $V$ as

$$
V=V_{low}+V_{high}^{′}+cV_{pink},
$$

where $V_{pink}$ is a new instance of pink noise multiplied by a small constant $c=0.01$. In the signal $V$, brief increases of the high frequency activity occur at a specific phase (0 radians) of the low frequency signal (Figure 4B).

![Figure 4.](https://cdn.elifesciences.org/articles/44287/elife-44287-fig4-v2.jpg)

**Figure 4.:** (A) Example simulation of $V_{low}$ (blue) and modulation signal M (red). When the phase of $V_{low}$ is near 0 radians, M increases. (B) Example simulation of PAC. When the phase of $V_{low}$ is approximately 0 radians, the high frequency amplitude (yellow) increases. (C) Example simulations of AAC. When the amplitude of $V_{low}$ is large, so is the amplitude of the high frequency signal (purple).

### Synthetic time series with AAC

To generate synthetic time series with dependence on the low frequency amplitude, we follow the procedure in the preceding section to generate $V_{low}$, $V_{high}$, and $A_{low}$. We then induce amplitude-amplitude coupling between the low and high frequency components by creating a new signal $V_{high}^{*}$ such that

$$
V_{high}^{∗}=V_{high}(1+I_{AAC}\frac{A_{low}}{max(A_{low})}),
$$

where $I_{AAC}$ is the intensity parameter corresponding to the strength of amplitude-amplitude coupling. We define the final voltage trace $V$ as

$$
V=V_{low}+V_{high}^{∗}+cV_{pink},
$$

where $V_{pink}$ is a new instance of pink noise multiplied by a small constant $c=0.01$ (Figure 4C).

### Human subject data

A patient (male, age 32 years) with medically intractable focal epilepsy underwent clinically indicated intracranial cortical recordings for epilepsy monitoring. In addition to clinical electrode implantation, the patient was also implanted with a 10 × 10 (4 mm ×4 mm) NeuroPort microelectrode array (MEA; Blackrock Microsystems, Utah) in a neocortical area expected to be resected with high probability in the temporal gyrus. The MEA consists of 96 platinum-tipped silicon probes, with a length of 1.5 mm, corresponding to neocortical layer III as confirmed by histology after resection. Signals from the MEA were acquired continuously at 30 kHz per channel. Seizure onset times were determined by an experienced encephalographer (S.S.C.) through inspection of the macroelectrode recordings, referral to the clinical report, and clinical manifestations recorded on video. For a detailed clinical summary, see patient P2 of Wagner et al. (2015). For these data, we analyze the 100–140 Hz and 4–7 Hz frequency bands to illustrate the proposed method; a more rigorous study of CFC in these data may require a more principled choice of high frequency band. All patients were enrolled after informed consent and consent to publish was obtained, and approval was granted by local Institutional Review Boards at Massachusetts General Hospital and Brigham Women’s Hospitals (Partners Human Research Committee), and at Boston University according to National Institutes of Health guidelines.

### Code availability

The code to perform this analysis is available for reuse and further development at https://github.com/Eden-Kramer-Lab/GLM-CFC (Nadalin and Kramer, 2019; copy archived at https://github.com/elifesciences-publications/GLM-CFC).

## Results

We first examine the performance of the CFC measure through simulation examples. In doing so, we show that the statistics $𝐑_{PAC}$ and $𝐑_{AAC}$ accurately detect different types of cross-frequency coupling, increase with the intensity of coupling, and detect weak PAC coupled to the low frequency amplitude. We show that the proposed method is less sensitive to changes in low frequency power, and outperforms an existing PAC measure that lacks dependence on the low frequency amplitude. We conclude with example applications to human and rodent in vivo recordings, and show how to extend the modeling framework to include a new covariate.

### The absence of CFC produces no significant detections of coupling

We first consider simulated signals without CFC. To create these signals, we follow the procedure in Materials and methods: Synthetic Time Series with PAC with the modulation intensity set to zero ($I_{PAC}=0$). In the resulting signals, $A_{high}$ is approximately constant and does not depend on $ϕ_{low}$ or $A_{low}$ (Figure 5A). We estimate the $ϕ_{low}$ model, the $A_{low}$ model, and the $A_{low},ϕ_{low}$ model from these data; we show example fits of the model surfaces in Figure 5B. We observe that the models exhibit small modulations in the estimated high frequency amplitude envelope as a function of the low frequency phase and amplitude.

![Figure 5.](https://cdn.elifesciences.org/articles/44287/elife-44287-fig5-v2.jpg)

**Figure 5.:** (A–C) Simulations with no CFC. (A) When no CFC occurs, the low frequency signal (blue) and high frequency signal (orange) evolve independently. (B) The surfaces $S_{A_{low}}$, $S_{ϕ_{low}}$, and $S_{A_{low},ϕ_{low}}$ suggest no dependence of $A_{high}$ on $ϕ_{low}$ or $A_{low}$. (C) Significant ($p$<0.05) values of $𝐑_{PAC}$ and $𝐑_{AAC}$ from 1000 simulations. Very few significant values for the statistics R are detected. (D–G) Simulations with PAC only. (D) When the phase of the low frequency signal is near 0 radians (red tick marks), the amplitude of the high frequency signal increases. (E) The surfaces $S_{A_{low}}$, $S_{ϕ_{low}}$, and $S_{A_{low},ϕ_{low}}$ suggest dependence of $A_{high}$ on $ϕ_{low}$. (F) In 1000 simulations, significant values of $R_{PAC}$ frequently appear, while significant values of $𝐑_{AAC}$ rarely appear. (G) As the intensity of PAC increases, so do the significant values of $𝐑_{PAC}$ (black), while any significant values of $𝐑_{AAC}$ remain small. (H–K) Simulations with AAC only. (H) The amplitudes of the high frequency signal and low frequency signal are positively correlated. (I) The surfaces $S_{A_{low}}$, $S_{ϕ_{low}}$, and $S_{A_{low},ϕ_{low}}$ suggest dependence of $A_{high}$ on $A_{low}$. (J) In 1000 simulations, significant values of $𝐑_{AAC}$ frequently appear. (K) As the intensity of AAC increases, so do the significant values of $𝐑_{AAC}$ (blue), while any significant values of $𝐑_{PAC}$ remain small. (L–O) Simulations with PAC and AAC. (L) The amplitude of the high frequency signal increases when the phase of the low frequency signal is near 0 radians and the amplitude of the low frequency signal is large. (M) The surfaces $S_{A_{low}}$, $S_{ϕ_{low}}$, and $S_{A_{low},ϕ_{low}}$ suggest dependence of $A_{high}$ on $ϕ_{low}$ and $A_{low}$. (N) In 1000 simulations, significant values of $𝐑_{PAC}$ and $𝐑_{AAC}$ frequently appear. (O) As the intensity of PAC and AAC increase, so do the significant values of $𝐑_{PAC}$ and $𝐑_{AAC}$. In (G,K,O), circles indicate the median, and x’s the 5th and 95th quantiles.

To assess the distribution of significant R values in the case of no cross-frequency coupling, we simulate 1000 instances of the pink noise signals (each of 20 s) and apply the R measures to each instance, plotting significant R values in Figure 5C. We find that for all 1000 instances, $p_{PAC}$ and $p_{AAC}$ are less than 0.05 in only 0.6% and 0.2% of the simulations, respectively, indicating no significant evidence of PAC or AAC, as expected.

We also applied these simulated signals to assess the performance of two standard model comparison procedures for GLMs. Simulating 1000 instances of pink noise signals (each of 20 s) with no induced PAC or AAC, we performed a chi-squared test for nested models (Kramer and Eden, 2016) between models $A_{low}$ and $A_{low},ϕ_{low}$, and detected significant PAC (p < 0.05) in 59.7% of simulations. Similarly, performing a chi-squared test for nested models between models $ϕ_{low}$ and $A_{low},ϕ_{low}$, we detected significant AAC (p < 0.05) in 41.5% of simulations. Using an AIC-based model comparison, we found a decrease in AIC from the $A_{low}$ model to the $A_{low},ϕ_{low}$ model (consistent with significant PAC) in 98.6% of simulations, and a decrease in AIC from the $ϕ_{low}$ model to the $A_{low},ϕ_{low}$ model (consistent with significant AAC) in 87.2% of simulations. By contrast, we rarely detect significant PAC (<0.6% of simulations) or AAC (<0.2% of simulations) in the pink noise signals using the two statistics $𝐑_{PAC}$ and $𝐑_{AAC}$ implemented here. We conclude that, in this modeling regime, two deviance-based model comparison procedures for GLMs are less robust measures of significant PAC and AAC.

### The proposed method accurately detects PAC

We next consider signals that possess phase-amplitude coupling, but lack amplitude-amplitude coupling. To do so, we simulate a 20 s signal with $A_{high}$ modulated by $ϕ_{low}$ (Figure 5D); more specifically, $A_{high}$ increases when $ϕ_{low}$ is near 0 radians (see Materials and methods, $I_{PAC}=1$). We then estimate the $ϕ_{low}$ model, the $A_{low}$ model, and the $A_{low},ϕ_{low}$ model from these data; we show example fits in Figure 5E. We find that in the $ϕ_{low}$ model $A_{high}$ is higher when $ϕ_{low}$ is close to 0 radians, and the $A_{low},ϕ_{low}$ model follows this trend. We note that, because the data do not depend on the low frequency amplitude ($A_{low})$, the $ϕ_{low}$ and $A_{low},ϕ_{low}$ models have very similar shapes in the ($ϕ_{low}$, $A_{low}$, $A_{high}$) space, and the $A_{low}$ model is nearly flat.

Simulating 1000 instances of these 20 s signals with induced phase-amplitude coupling, we find $p_{AAC}<0.05$ for only 0.6% of the simulations, while $p_{PAC}<0.05$ for 96.5% of the simulations. We find that the significant values of $𝐑_{PAC}$ lie well above 0 (Figure 5F), and that as the intensity of the simulated phase-amplitude coupling increases, so does the statistic $𝐑_{PAC}$ (Figure 5G). We conclude that the proposed method accurately detects the presence of phase-amplitude coupling in these simulated data.

### The proposed method accurately detects AAC

We next consider signals with amplitude-amplitude coupling, but without phase-amplitude coupling. We simulate a 20 s signal such that $A_{high}$ is modulated by $A_{low}$ (see Materials and methods, $I_{AAC}=1$); when $A_{low}$ is large, so is $A_{high}$ (Figure 5H). We then estimate the $ϕ_{low}$ model, the $A_{low}$ model, and the $A_{low},ϕ_{low}$ model (example fits in Figure 5I). We find that the $A_{low}$ model increases along the $A_{low}$ axis, and that the $A_{low},ϕ_{low}$ model closely follows this trend, while the $ϕ_{low}$ model remains mostly flat, as expected.

Simulating 1000 instances of these signals we find that $p_{AAC}<0.05$ for 97.9% of simulations, while $p_{PAC}<0.05$ for 0.3% of simulations. The significant values of $𝐑_{AAC}$ lie above 0 (Figure 5J), and increases in the intensity of AAC produce increases in $𝐑_{AAC}$ (Figure 5K). We conclude that the proposed method accurately detects the presence of amplitude-amplitude coupling.

### The proposed method accurately detects the simultaneous occurrence of PAC and AAC

We now consider signals that possess both phase-amplitude coupling and amplitude-amplitude coupling. To do so, we simulate time series data with both AAC and PAC (Figure 5L). In this case, $A_{high}$ increases when $ϕ_{low}$ is near 0 radians and when $A_{low}$ is large (see Materials and methods, $I_{PAC}=1$ and $I_{AAC}=1$). We then estimate the $ϕ_{low}$ model, the $A_{low}$ model, and the $A_{low},ϕ_{low}$ model from the data and visualize the results (Figure 5M). We find that the $ϕ_{low}$ model increases near $ϕ_{low}=0$, and that the $A_{low}$ model increases linearly with $A_{low}$. The $A_{low},ϕ_{low}$ model exhibits both of these behaviors, increasing at $ϕ_{low}=0$ and as $A_{low}$ increases.

Simulating 1000 instances of signals with both AAC and PAC present, we find that $p_{AAC}<0.05$ in 96.7% of simulations and $p_{PAC}<0.05$ in 98.1% of simulations. The distributions of significant $𝐑_{PAC}$ and $𝐑_{AAC}$ values lie above 0, consistent with the presence of both PAC and AAC (Figure 5N), and as the intensity of PAC and AAC increases, so do the values of $𝐑_{PAC}$ and $𝐑_{AAC}$ (Figure 5O). We conclude that the model successfully detects the concurrent presence of PAC and AAC.

### 𝐑PAC and modulation index are both sensitive to weak modulations

To investigate the ability of the proposed method and the modulation index to detect weak coupling between the low frequency phase and high frequency amplitude, we perform the following simulations. For each intensity value $I_{PAC}$ between 0 and 0.5 (in steps of 0.025), we simulate 1000 signals (see Materials and methods) and compute $𝐑_{PAC}$ and a measure of PAC in common use: the modulation index MI (Tort et al., 2010) (Figure 6). We find that both MI and $𝐑_{PAC}$, while small, increase with $I_{PAC}$; in this way, both measures are sensitive to small values of $I_{PAC}$. However, we note that $𝐑_{PAC}$ is not significant for very small intensity values ($I_{PAC}\leq0.3$), while MI is significant at these small intensities. Significant $𝐑_{PAC}$ appears when the MI exceeds 0.7 × 10-3, a value below the range of MI values detected in many existing studies (Tort et al., 2008; Zhong et al., 2017; Jackson et al., 2019; Axmacher et al., 2010; Tort et al., 2018). We conclude that, while the modulation index may be more sensitive than $𝐑_{PAC}$ to very weak phase-amplitude coupling, $𝐑_{PAC}$ can detect phase-amplitude coupling at MI values consistent with those observed in the literature.

![Figure 6.](https://cdn.elifesciences.org/articles/44287/elife-44287-fig6-v2.jpg)

**Figure 6.:** The mean (circles) and 5th to 95th quantiles (x’s) of (A) $𝐑_{PAC}$ and (B) MI for intensity values between 0 and 0.5. Black bars indicate $p_{PAC}$ or $p_{MI}$ is below 0.05 for ≥95% of simulations; gray bars indicate $p_{PAC}$ is not below 0.05 for ≥95% of simulations. While both measures increase with intensity, MI detects more instances of significant PAC than does $𝐑_{PAC}$ for very small values of $I_{PAC}$.

### The proposed method is less affected by fluctuations in low-frequency amplitude and AAC

Increases in low frequency power can increase measures of phase-amplitude coupling, although the underlying PAC remains unchanged (Aru et al., 2015; Cole and Voytek, 2017). Characterizing the impact of this confounding effect is important both to understand measure performance and to produce accurate interpretations of analyzed data. To examine this phenomenon, we perform the following simulation. First, we simulate a signal $V$ with fixed PAC (intensity $I_{PAC}=1$, see Materials and methods). Second, we filter $V$ into its low and high frequency components $V_{low}$ and $V_{high}$, respectively. Then, we create a new signal $V^{*}$ as follows:

$$
V^{∗}=2V_{low}+V_{high}+V_{noise},
$$

where $V_{noise}$ is a pink noise term (see Materials and methods). We note that we only alter the low frequency component of $V$ and do not alter the PAC. To analyze the PAC in this new signal we compute $𝐑_{PAC}$ and MI.

We show in Figure 7 population results (1000 realizations each of the simulated signals $V$ and $V^{*}$) for the R and MI values. We observe that increases in the amplitude of $V_{low}$ produce increases in MI and $𝐑_{PAC}$. However, this increase is more dramatic for MI than for $𝐑_{PAC}$; we note that the distributions of $𝐑_{PAC}$ almost completely overlap (Figure 7A), while the distribution of MI shifts to larger values when the amplitude of $V_{low}$ increases (Figure 7B). We conclude that the statistic $𝐑_{PAC}$ — which includes the low frequency amplitude as a predictor in the GLM — is more robust to increases in low frequency power than a method that only includes the low frequency phase.

![Figure 7.](https://cdn.elifesciences.org/articles/44287/elife-44287-fig7-v2.jpg)

**Figure 7.:** Increases in the amplitude of the low frequency signal, and the amplitude-amplitude coupling (AAC), increase the modulation index more than $R_{PAC}$.(A,B) Distributions of (A) $R_{PAC}$ and (B) MI when $A_{low}$ is small (blue) and when $A_{low}$ is large (red). (C,D) Distributions of (C) $R_{PAC}$ and (D) MI when AAC is small (blue) and when AAC is large (red).

We also investigate the effect of increases in amplitude-amplitude coupling (AAC) on the two measures of PAC. As before, we simulate a signal $V$ with fixed PAC (intensity $I_{PAC}=1$) and no AAC (intensity $I_{AAC}=0$). We then simulate a second signal $V^{*}$ with the same fixed PAC as $V$, and with additional AAC (intensity $I_{AAC}=10$). We simulate 1000 realizations of $V$ and $V^{*}$ and compute the corresponding $𝐑_{PAC}$ and MI values. We observe that the increase in AAC produces a small increase in the distribution of $𝐑_{PAC}$ values (Figure 7C), but a large increase in the distribution of MI values (Figure 7D). We conclude that the statistic $𝐑_{PAC}$ is more robust to increases in AAC than MI.

These simulations show that at a fixed, non-zero PAC, the modulation index increases with increased $A_{low}$ and AAC. We now consider the scenario of increased $A_{low}$ and AAC in the absence of PAC. To do so, we simulate 1000 signals of 200 s duration, with no PAC (intensity $I_{PAC}=0$). For each signal, at time 100 s (i.e., the midpoint of the simulation) we increase the low frequency amplitude by a factor of 10 (consistent with observations from an experiment in rodent cortex, as described below), and include AAC between the low and high frequency signals (intensity $I_{AAC}=0$ for $t<100s$ and intensity $I_{AAC}=2$ for $t\geq100s$). We find that, in the absence of PAC, $𝐑_{PAC}$ detects significant PAC (p<0.05) in 0.4% of the simulated signals, while MI detects significant PAC in 34.3% of simulated signals. We conclude that in the presence of increased low frequency amplitude and amplitude-amplitude coupling, MI may detect PAC where none exists, while $R_{PAC}$, which accounts for fluctuations in low frequency amplitude, does not.

### Sparse PAC is detected when coupled to the low frequency amplitude

While the modulation index has been successfully applied in many contexts (Canolty and Knight, 2010; Hyafil et al., 2015b), instances may exist where this measure is not optimal. For example, because the modulation index was not designed to account for the low frequency amplitude, it may fail to detect PAC when $A_{high}$ depends not only on $ϕ_{low}$, but also on $A_{low}$. For example, since the modulation index considers the distribution of $A_{high}$ at all observed values of $ϕ_{low}$, it may fail to detect coupling events that occur sparsely at only a subset of appropriate $ϕ_{low}$ occurrences. $R_{PAC}$, on the other hand, may detect these sparse events if these events are coupled to $A_{low}$, as $R_{PAC}$ accounts for fluctuations in low frequency amplitude. To illustrate this, we consider a simulation scenario in which PAC occurs sparsely in time.

We create a signal $V$ with PAC, and corresponding modulation signal M with intensity value $I_{PAC}=1.0$ (see Materials and methods, Figure 8A–B). We then modify this signal to reduce the number of PAC events in a way that depends on $A_{low}$. To do so, we preserve PAC at the peaks of $V_{low}$ (i.e., when $ϕ_{low}=0$), but now only when these peaks are large, more specifically in the top 5% of peak values.

![Figure 8.](https://cdn.elifesciences.org/articles/44287/elife-44287-fig8-v2.jpg)

**Figure 8.:** (A) The low frequency signal (blue), amplitude envelope (yellow), and threshold (black dashed). (B–C) The modulation signal increases (B) at every occurrence of $ϕ_{low}=0$, or (C) only when $A_{low}$ exceeds the threshold and $ϕ_{low}=0$.

We define a threshold value $T$ to be the 95th quantile of the peak $V_{low}$ values, and modify the modulation signal M as follows. When M exceeds 1 (i.e., when $ϕ_{low}=0$) and the low frequency amplitude exceeds $T$ (i.e., $A_{low}\geqT$), we make no change to M. Alternatively, when M exceeds one and the low frequency amplitude lies below $T$ (i.e., $A_{low}<T)$, we decrease M to 1 (Figure 8C). In this way, we create a modified modulation signal $M_{1}$ such that in the resulting signal $V_{1}$, when $ϕ_{low}=0$ and $A_{low}$ is large enough, $A_{high}$ is increased; and when $ϕ_{low}=0$ and $A_{low}$ is not large enough, there is no change to $A_{high}$. This signal $V_{1}$ hence has fewer phase-amplitude coupling events than the number of times $ϕ_{low}=0$.

We generate 1000 realizations of the simulated signals $V_{1}$, and compute $R_{PAC}$ and MI. We find that while MI detects significant PAC in only 37% of simulations, $R_{PAC}$ detects significant PAC in 72% of simulations. In this case, although the PAC occurs infrequently, these occurrences are coupled to $A_{low}$, and $R_{PAC}$, which accounts for changes in $A_{low}$, successfully detects these events much more frequently. We conclude that when the PAC is dependent on $A_{low}$, $R_{PAC}$ more accurately detects these sparse coupling events.

### The CFC model detects simultaneous PAC and AAC missed in an existing method

To further illustrate the utility of the proposed method, we consider another scenario in which $A_{low}$ impacts the occurrence of PAC. More specifically, we consider a case in which $A_{high}$ increases at a fixed low frequency phase for high values of $A_{low}$, and $A_{high}$ decreases at the same phase for small values of $A_{low}$. In this case, we expect that the modulation index may fail to detect the coupling because the distribution of $A_{high}$ over $ϕ_{low}$ would appear uniform when averaged over all values of $A_{low}$; the dependence of $A_{high}$ on $ϕ_{low}$ would only become apparent after accounting for $A_{low}$.

To implement this scenario, we consider the modulation signal M (see Materials and methods) with an intensity value $I_{PAC}=1$. We consider all peaks of $A_{low}$ and set the threshold $T$ to be the 50th quantile (Figure 9A). We then modify the modulation signal M as follows. When M exceeds 1 (i.e., when $ϕ_{low}=0$) and the low frequency amplitude exceeds $T$ (i.e., $A_{low}\geqT$), we make no change to M. Alternatively, when M exceeds one and the low frequency amplitude lies below $T$ (i.e. $A_{low}<T)$, we decrease M to 0 (Figure 9B). In this way, we create a modified modulation signal M such that when $ϕ_{low}=0$ and $A_{low}$ is large enough, $A_{high}$ is increased; and when $ϕ_{low}=0$ and $A_{low}$ is small enough, $A_{high}$ is decreased (Figure 9C).

![Figure 9.](https://cdn.elifesciences.org/articles/44287/elife-44287-fig9-v2.jpg)

**Figure 9.:** (A) The low frequency signal (blue), amplitude envelope (yellow), and threshold (black dashed). (B) The modulation signal (red) increases when $ϕ_{low}=0$ and $A_{low}>T$, and deceases when $ϕ_{low}=0$ and $A_{low}<T$. (C) The modulated $A_{high}$ signal (purple) increases and decreases with the modulation signal. (D) The proportion of significant detections (out of 1000) for MI and $R_{PAC}$.

Using this method, we simulate 1000 realizations of this signal, and calculate MI and $R_{PAC}$ for each signal (Figure 9D). We find that $R_{PAC}$ detects significant PAC in nearly all (96%) of the simulations, while MI detects significant PAC in only 58% of the simulations. We conclude that, in this simulation, $R_{PAC}$ more accurately detects PAC coupled to low frequency amplitude.

### A simple stochastic spiking neural model illustrates the utility of the proposed method

In the previous simulations, we created synthetic data without a biophysically principled generative model. Here we consider an alternative simulation strategy with a more direct connection to neural dynamics. While many biophysically motivated models of cross-frequency coupling exist (Sase et al., 2017; Chehelcheraghi et al., 2017; Sotero, 2016; Hyafil et al., 2015a; Lepage and Vijayan, 2015; Onslow et al., 2014; Fontolan et al., 2013; Malerba and Kopell, 2013; Jirsa and Müller, 2013; Spaak et al., 2012; Wulff et al., 2009; Tort et al., 2007), we consider here a relatively simple stochastic spiking neuron model (Aljadeff et al., 2016). In this stochastic model, we generate a spike train ($V_{high}$) in which an externally imposed signal $V_{low}$ modulates the probability of spiking as a function of $A_{low}$ and $ϕ_{low}$. We note that high frequency activity is thought to represent the aggregate spiking activity of local neural populations (Ray and Maunsell, 2011; Buzsáki and Wang, 2012; Ray et al., 2008a; Jia and Kohn, 2011); while here we simulate the activity of a single neuron, the spike train still produces temporally focal events of high frequency activity. In this framework, we allow the target phase ($ϕ_{low}^{∗}$) modulating $A_{high}$ to change as a function of $A_{low}$: when $A_{low}$ is large, the probability of spiking is highest near $ϕ_{low}=\pm\pi$, and when $A_{low}$ is small, the probability of spiking is highest near $ϕ_{low}=0.$ More precisely, we define $ϕ_{low}^{∗}$ as

$$
ϕ_{low}^{∗}=\pi(1+A_{low})
$$

where $A_{low}$ is a sinusoid oscillating between 1 and 2 with period 0.1 Hz. We define the spiking probability, $\lambda$, as

$$
\lambda=\lambda_{0}exp⁡[−(1+\frac{s(ϕ_{low}−ϕ_{low}^{∗})^{2}}{2\sigma^{2}})],
$$

where $\sigma=0.01$, $s(ϕ)$ is a triangle wave, and we choose $\lambda_{0}$ so that the maximum value of $\lambda$ is 2. We note that the spiking probability $\lambda$ is zero except near times when the phase of the low frequency signal $(ϕ_{low})$ is near $ϕ_{low}^{∗}$. We then define $A_{high}$ as:

$$
A_{high}=S+n,
$$

where $S$ is the binary sequence generated by the stochastic spiking neuron model, and $n$ is Gaussian noise with mean zero and standard deviation 0.1. In this scenario, the distribution of $A_{high}$ over $ϕ_{low}$ appears uniform when averaged over all values of $A_{low}$. We therefore expect the modulation index to remain small, despite the presence of PAC with maximal phase dependent on $A_{low}$. However, we expect that $R_{PAC}$, which accounts for fluctuations in low frequency amplitude, will detect this PAC. We show an example signal from this simulation in Figure 10A. As expected, we find that $R_{PAC}$ detects PAC ($R_{PAC}=0.172$, $p=0.02$); we note that the ($A_{low}$, $ϕ_{low}$) surface exhibits a single peak near $ϕ_{low}=0$ at small values of $A_{low}$, and at $ϕ_{low}=\pm\pi$ at large value of $A_{low}$ (Figure 10B). The ($A_{low}$, $ϕ_{low}$) surface deviates significantly from the $A_{low}$ surface, resulting in a large $R_{PAC}$ value. However, the non-uniform shape of the ($A_{low}$, $ϕ_{low}$) surface is lost when we fail to account for $A_{low}$. In this scenario, the distribution of $A_{high}$ over $ϕ_{low}$ appears uniform, resulting in a low MI value (Figure 10C).

![Figure 10.](https://cdn.elifesciences.org/articles/44287/elife-44287-fig10-v2.jpg)

**Figure 10.:** $R_{PAC}$, but not MI, detects phase-amplitude coupling in a simple stochastic spiking neuron model.(A) The phase and amplitude of the low frequency signal (blue) modulate the probability of a high frequency spike (orange). (B) The surfaces $S_{A_{low}}$ (red) and $S_{A_{low},ϕ_{low}}$ (yellow). The phase of maximal $A_{high}$ modulation depends on $A_{low}$. (C) The modulation index fails to detect this type of PAC.

### Application to in vivo human seizure data

To evaluate the performance of the proposed method on in vivo data, we first consider an example recording from human cortex during a seizure (see Materials and methods: Human subject data). Visual inspection of the LFP data (Figure 11A) reveals the emergence of large amplitude voltage fluctuations during the approximately 80 s seizure. We compute the spectrogram over the entire seizure, using windows of width 0.8 s with 0.002 s overlap, and identify a distinct 10 s interval of increased power in the 4–7 Hz band (Figure 11B). We analyze this section of the voltage trace $V$, filtering into $V_{high}$ (100–140 Hz) and $V_{low}$ (4–7 Hz), and extracting $A_{high}$, $A_{low}$, and $ϕ_{low}$ as in Methods (Figure 11C). Visual inspection reveals the occurrence of large amplitude, low frequency oscillations and small amplitude, high frequency oscillations.

![Figure 11.](https://cdn.elifesciences.org/articles/44287/elife-44287-fig11-v2.jpg)

**Figure 11.:** (A,B) Voltage recording (A) and spectrogram (B) from one MEA electrode over the course of a seizure; PAC and AAC were computed for the time segment outlined in red. (C) The 10 s voltage trace (blue) corresponding to the outlined segment in (A), and $V_{low}$ (red), $V_{high}$ (yellow), and $A_{low}$ (purple). (D) A 2 s subinterval of the voltage trace (blue), $V_{low}$ (red), $V_{high}$ (yellow), $A_{low}$ (purple), and $ϕ_{low}$ (green). (E) $A_{low}$ (purple) and $A_{high}$ (red) for the 10 s segment in (C), normalized and smoothed.

We find during this interval significant phase-amplitude coupling computed using $R_{PAC}$ ($R_{PAC}=1.55$, $p_{PAC}=0.005$, Figure 12), and using the modulation index ($MI=0.03$, $p_{MI}=5.0\times10^{−4}$). To examine the phase-amplitude coupling in more detail, we isolate a 2 s segment (Figure 11D) and display the signal $V$, the high frequency signal $V_{high}$, the low frequency phase $ϕ_{low}$, and the low frequency amplitude $A_{low}$. We observe that when $ϕ_{low}$ is near $\pi$, the amplitude of $V_{high}$ tends to increase, consistent with the presence of PAC and a significant value of $R_{PAC}$ and MI.

![Figure 12.](https://cdn.elifesciences.org/articles/44287/elife-44287-fig12-v2.jpg)

**Figure 12.:** The $S_{A_{low},ϕ_{low}}$ surface shows how PAC changes with the low frequency amplitude and phase during an interval of human seizure.(A) The full model surface (blue) in the ($ϕ_{low}$, $A_{low}$, $A_{high}$) space, and components of that surface when (B) $A_{low}$ is small (black), and $A_{low}$ is large (red).

We also find significant amplitude-amplitude coupling computed using $R_{AAC}$ ($R_{AAC}=0.85$, $p_{AAC}=0.005$). Comparing $A_{high}$ and $A_{low}$ over the 10 s interval (each smoothed using a 1 s moving average filter and normalized), we observe that both $A_{high}$ and $A_{low}$ steadily increase over the duration of the interval (Figure 11E).

### Application to in vivo rodent data

As a second example to illustrate the performance of the new method, we consider LFP recordings from from the infralimbic cortex (IL) and basolateral amygdala (BLA) of an outbred Long-Evans rat before and after the delivery of an experimental electrical stimulation intervention described in Blackwood et al. (2018). Eight microwires in each region, referenced as bipolar pairs, sampled the LFP at 30 kHz, and electrical stimulation was delivered to change inter-regional coupling (see Blackwood et al., 2018 for a detailed description of the experiment). Here we examine how cross-frequency coupling between low frequency (5–8 Hz) IL signals and high frequency (70–110 Hz) BLA signals changes from the pre-stimulation to the post-stimulation condition. To do so, we filter the data $V$ into low and high frequency signals (see Materials and methods), and compute the MI, $R_{PAC}$ and $R_{AAC}$ between each possible BLA-IL pairing, sixteen in total.

We find three separate BLA-IL pairings where $R_{PAC}$ reports no significant PAC pre- or post-stimulation, but MI reports significant coupling post-stimulation. Investigating further, we note that in all three cases, the amplitude of the low frequency IL signal increases from pre- to post-stimulation, and $R_{AAC}$, the measure of amplitude-amplitude coupling, increases from pre- to post-stimulation. These observations are consistent with the simulations in Results: The proposed method is less affected by fluctuations in low-frequency amplitude and AAC, in which we showed that increases in the low frequency amplitude and AAC produced increases in MI, although the PAC remained fixed. We therefore propose that, consistent with these simulation results, the increase in MI observed in these data may result from changes in the low frequency amplitude and AAC, not in PAC.

### Using the flexibility of GLMs to improve detection of phase-amplitude coupling in vivo

One advantage of the proposed framework is its flexibility: covariates are easily added to the generalized linear model and tested for significance. For example, we could include covariates for trial, sex, and stimulus parameters and explore their effects on PAC, AAC, or both.

Here, we illustrate this flexibility through continued analysis of the rodent data. We select a single electrode recording from these data, and hypothesize that the condition, either pre-stimulation or post-stimulation, affects the coupling. To incorporate this new covariate into the framework, we consider the concatenated voltage recordings from the pre-stimulation condition $V_{pre}$ and the post-stimulation condition $V_{post}$:

$$
V=[V_{pre},V_{post}].
$$

From $V$, we obtain the corresponding high frequency signal $V_{high}$ and low frequency signal $V_{low}$, and subsequently the high frequency amplitude $A_{high}$, low frequency phase $ϕ_{low}$, and low frequency amplitude $A_{low}$. We use these data to generate two new models:

$$
A_{high}|ϕ_{low},A_{low},P∼Gamma[\mu,ν],
$$



$$
log⁡\mu=\sumk=1n\beta_{k}f_{k}(ϕ_{low})+\beta_{n+1}A_{low}+\beta_{n+2}A_{low}sin⁡(ϕ_{low})+\beta_{n+3}A_{low}cos⁡(ϕ_{low})+P(\sumj=1n\beta_{n+3+j}f_{j}(ϕ_{low})+\beta_{2n+4}A_{low})
$$



$$
A_{high}|ϕ_{low},A_{low},P∼Gamma[\mu,ν]
$$



$$
log⁡\mu=\sumk=1n\beta_{k}f_{k}(ϕ_{ low})+\beta_{n+1}A_{low}+\beta_{n+2}A_{low}sin⁡(ϕ_{low })+\beta_{n+3}A_{low}cos⁡(ϕ_{low})+P(\beta_{n+4}A_{ low}),
$$

where $P$ is an indicator function specifying whether the signal is in the pre-stimulation ($P=0$) or post-stimulation ($P=1$) condition. The effect of the indicator function is to include the effect of stimulus condition on the high frequency amplitude. The models in Equations 9 and 10 now include the effect of low frequency amplitude, low frequency phase, and condition on high frequency amplitude. To determine whether the condition has an effect on PAC, we test whether the term $P(\sumj=1n\beta_{n+3+j}f_{j}(ϕ_{low}))$ in Equation 9 is significant, that is whether there is a significant difference between the models in Equations 9 and 10. If the difference between the two models is very small, we gain no improvement in modeling $A_{high}$ by including the interaction between $P$ and $ϕ_{low}$. In that case, the impact of $ϕ_{low}$ on $A_{high}$ can be modeled without considering stimulus condition $P$, that is the impact of stimulus condition on PAC is negligible.

To measure the difference between the models in Equations 9 and 10, we construct a surface $S_{Pϕ_{low}}$ from the model in Equation 9, and a surface $S_{P}$ from the model in Equation 10 in the ($A_{low}$, $ϕ_{low}$, $A_{high}$, P) space, assessing the models at $P=1$. We compute $R_{PAC,condition}$, which measures the impact of stimulus condition on PAC, as:

$$
R_{PAC, condition}=max[abs[1−S_{P}/S_{Pϕ_{low}}]].
$$

We find for the example rodent data an $R_{PAC, condition}$ value of 0.3608, with a p-value of 0.0005. Hence, we find evidence for a significant effect of stimulus on PAC.

To further explore this assessment of stimulus condition on PAC, we simulate 1000 instances of a 40 s signal divided into two conditions: no PAC for the first 20 s ($I_{PAC}=0$) and non-zero PAC for the final 20 s $(I_{PAC}=1)$. We design this simulation to mimic an increase in PAC from pre-stimulation to post-stimulation (Figure 13A). Using the models in Equations 9 and 10, and computing $R_{PAC, condition}$, we find $p<0.05$ for 100% of simulated signals. We also simulate 1000 instances of a 40 s signal with no PAC ($I_{PAC}=0$) for the entire 40 s, that is PAC does not change from pre-stimulation to post-stimulation (Figure 13B), and find in this case $p<0.05$ for only 4.6% of simulations. Finally, we simulate 1000 instances of a 40 s signal with fixed PAC $(I_{PAC}=1)$, and with a doubling of the low frequency amplitude occuring at 20 s (i.e., pre-stimulation the low frequency amplitude is 1, and post-stimulation the low frequency amplitude is 2). We find $p<0.05$ for only 3.6% of simulations. We conclude that this method effectively determines whether stimulation condition significantly changes PAC.

![Figure 13.](https://cdn.elifesciences.org/articles/44287/elife-44287-fig13-v2.jpg)

**Figure 13.:** Example simulated $V_{low}$ (blue) and $V_{high}$ (orange) signals for which (A) PAC increases at 20 s (indicated by black dashed line), and (B) no increase in PAC occurs.

This example illustrates the flexibility of the statistical modeling framework. Extending this framework is straightforward, and new extensions allow a common principled approach to test the impact of new predictors. Here we considered an indicator function that divides the data into two states (pre- and post-stimulation). We note that the models are easily extended to account for multiple discrete predictors such as gender and participation in a drug trial, or for continuous predictors such as age and time since stimulus.

## Discussion

In this paper, we proposed a new method for measuring cross-frequency coupling that accounts for both phase-amplitude coupling and amplitude-amplitude coupling, along with a principled statistical modeling framework to assess the significance of this coupling. We have shown that this method effectively detects CFC, both as PAC and AAC, and is more sensitive to weak PAC obscured by or coupled to low-frequency amplitude fluctuations. Compared to an existing method, the modulation index (Tort et al., 2010), the newly proposed method more accurately detects scenarios in which PAC is coupled to the low-frequency amplitude. Finally, we applied this method to in vivo data to illustrate examples of PAC and AAC in real systems, and show how to extend the modeling framework to include a new covariate.

One of the most important features of the new method is an increased ability to detect weak PAC coupled to AAC. For example, when sparse PAC events occur only when the low frequency amplitude ($A_{low}$) is large, the proposed method detects this coupling while another method not accounting for $A_{low}$ misses it. While PAC often occurs in neural data, and has been associated with numerous neurological functions (Canolty and Knight, 2010; Hyafil et al., 2015b), the simultaneous occurrence of PAC and AAC is less well studied (Osipova et al., 2008). Here, we showed examples of simultaneous PAC and AAC recorded from human cortex during a seizure, and we note that this phenomena has been simulated in other works (Mazzoni et al., 2010).

While the exact mechanisms that support CFC are not well understood (Hyafil et al., 2015b), the general mechanisms of low and high frequency rhythms have been proposed. Low frequency rhythms are associated with the aggregate activity of large neural populations and modulations of neuronal excitability (Engel et al., 2001; Varela et al., 2001; Buzsáki and Draguhn, 2004), while high frequency rhythms provided a surrogate measure of neuronal spiking (Rasch et al., 2008; Mukamel et al., 2005; Fries et al., 2001; Pesaran et al., 2002; Whittingstall and Logothetis, 2009; Ray and Maunsell, 2011; Ray et al., 2008b). These two observations provide a physical interpretation for PAC: when a low frequency rhythm modulates the excitability of a neural population, we expect spiking to occur (i.e., an increase in $A_{high}$) at a particular phase of the low frequency rhythm ($ϕ_{low}$) when excitation is maximal. These notions also provide a physical interpretation for AAC: increases in $A_{low}$ produce larger modulations in neural excitability, and therefore increased intervals of neuronal spiking (i.e., increases in $A_{high}$). Alternatively, decreases in $A_{low}$ reduce excitability and neuronal spiking (i.e., decreases in $A_{high}$).

The function of concurrent PAC and AAC, both for healthy brain function and during a seizure as illustrated here, is not well understood. As PAC occurs normally in healthy brain signals, for example during working memory, neuronal computation, communication, learning and emotion (Tort et al., 2009; Jensen et al., 2016; Canolty and Knight, 2010; Dejean et al., 2016; Karalis et al., 2016; Likhtik et al., 2014; Jones and Wilson, 2005; Lisman, 2005; Sirota et al., 2008), these preliminary results may suggest a pathological aspect of strong AAC occurring concurrently with PAC.

Proposed functions of PAC include multi-item encoding, long-distance communication, and sensory parsing (Hyafil et al., 2015b). Each of these functions takes advantage of the low frequency phase, encoding different objects or pieces of information in distinct phase intervals of $ϕ_{low}$. PAC can be interpreted as a type of focused attention; $A_{high}$ modulation occurring only in a particular interval of $ϕ_{low}$ organizes neural activity - and presumably information - into discrete packets of time. Similarly, a proposed function of AAC is to encode the number of represented items, or the amount of information encoded in the modulated signal (Hyafil et al., 2015b). A pathological increase in AAC may support the transmission of more information than is needed, overloading the communication of relevant information with irrelevant noise. The attention-based function of PAC, that is having reduced high frequency amplitude at phases not containing the targeted information, may be lost if the amplitude of the high frequency oscillation is increased across wide intervals of low frequency phase.

Like all measures of CFC, the proposed method possesses specific limitations. We discuss five limitations here. First, the choice of spline basis to represent the low frequency phase may be inaccurate, for example if the PAC changes rapidly with $ϕ_{low}$. Second, the value of $R_{AAC}$ depends on the range of $A_{low}$ observed. This is due to the linear relationship between $A_{low}$ and $A_{high}$ in the $A_{low}$ model, which causes the maximum distance between the surfaces $S_{A_{low}}$ and $S_{A_{low},ϕ_{low}}$ to occur at the largest or smallest value of $A_{low}$. To mitigate the impact of extreme $A_{low}$ values on $R_{AAC}$, we evaluate the surfaces $S_{A_{low}}$ and $S_{A_{low},ϕ_{low}}$ over the 5th to 95th quantiles of $A_{low}$. We note that an alternative metric of AAC could instead evaluate the slope of the $S_{A_{low}}$ surface; to maintain consistency of the PAC and AAC measures, we chose not to implement this alternative measure here. Third, the frequency bands for $V_{high}$ and $V_{low}$ must be established before R values are calculated. Hence, if the wrong frequency bands are chosen, coupling may be missed. It is possible, though computationally expensive, to scan over all reasonable frequency bands for both $V_{high}$ and $V_{low}$, calculating R values for each frequency band pair. Fourth, we note that the proposed modeling framework assumes the data contain approximately sinusoidal signals, which have been appropriately isolated for analysis. In general, CFC measures are sensitive to non-sinusoidal signals, which may confound interpretation of cross-frequency analyses (Cole and Voytek, 2017; Kramer et al., 2008; Aru et al., 2015). While the modeling framework proposed here does not directly account for the confounds introduced by non-sinusoidal signals, the inclusion of additional predictors (e.g. detections of sharp changes in the unfiltered data) in the model may help mitigate these effects. Fifth, we simulate time series with known PAC and AAC, and then test whether the proposed analysis framework detects this coupling. The simulated relationships between $A_{high}$ and ($ϕ_{low}$,$A_{low}$) may result in time series with simpler structure than those observed in vivo. For example, a latent signal may drive both $A_{high}$ and $ϕ_{low}$, and in this way establish nonlinear relationships between the two observables $A_{high}$ and $ϕ_{low}$. We note that, if this were the case, the latent signal could also be incorporated in the statistical modeling framework (Yousefi et al., 2019).

We chose the statistics $R_{PAC}$ and $R_{AAC}$ for two reasons. First, we found that two common methods of model comparison for GLMs provide less robust measures of significance than $R_{PAC}$ and $R_{AAC}$. While the statistics $R_{PAC}$ and $R_{AAC}$ are less powerful than standard model comparison tests, the large amount of data typically assessed in CFC analysis may compensate for this loss. We showed that the statistics $R_{PAC}$ and $R_{AAC}$ performed well in simulations, and we note that these statistics are directly interpretable. While many model comparison methods exist - and another method may provide specific advantages - we found that the framework implemented here is sufficiently powerful, interpretable, and robust for real-world neural data analysis.

The proposed method can easily be extended by inclusion of additional predictors in the GLM. Polynomial $A_{low}$ predictors, rather than the current linear $A_{low}$ predictors, may better capture the relationship between $A_{low}$ and $A_{high}$. One could also include different types of covariates, for example classes of drugs administered to a patient, or time since an administered stimulus during an experiment. To capture more complex relationships between the predictors ($A_{low}$, $ϕ_{low}$) and $A_{high}$, the GLM could be replaced by a more general form of Generalized Additive Model (GAM). Choosing GAMs would remove the restriction that the conditional mean $A_{high}$ must be linear in each of the model parameters (which would allow us to estimate knot locations directly from the data, for example), at the cost of greater computational time to estimate these parameters. The code developed to implement the method is flexible and modular, which facilitates modifications and extensions motivated by the particular data analysis scenario. This modular code, available at https://github.com/Eden-Kramer-Lab/GLM-CFC, also allows the user to change latent assumptions, such as choice of frequency bands and filtering method. The code is freely available for reuse and further development.

Rhythms, and particularly the interactions of different frequency rhythms, are an important component for a complete understanding of neural activity. While the mechanisms and functions of some rhythms are well understood, how and why rhythms interact remains uncertain. A first step in addressing these uncertainties is the application of appropriate data analysis tools. Here we provide a new tool to measure coupling between different brain rhythms: the method utilizes a statistical modeling framework that is flexible and captures subtle differences in cross-frequency coupling. We hope that this method will better enable practicing neuroscientists to measure and relate brain rhythms, and ultimately better understand brain function and interactions.
