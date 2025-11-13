# Are single-peaked tuning curves tuned for speed rather than accuracy?

## Authors

- Movitz Lenninger<sup>1</sup> ([ORCID: 0000-0002-6165-4900](https://orcid.org/0000-0002-6165-4900)) †
- Mikael Skoglund<sup>1</sup>
- Pawel Andrzej Herman<sup>2</sup> ([ORCID: 0000-0001-6553-823X](https://orcid.org/0000-0001-6553-823X))
- Arvind Kumar<sup>2</sup> ([ORCID: 0000-0002-8044-9195](https://orcid.org/0000-0002-8044-9195)) †

### Affiliations

1. Division of Information Science and Engineering, KTH Royal Institute of Technology Stockholm Sweden ([ROR:026vcq606](https://ror.org/026vcq606))
2. Division of Computational Science and Technology, KTH Royal Institute of Technology Stockholm Sweden ([ROR:026vcq606](https://ror.org/026vcq606))
3. Science for Life Laboratory Stockholm Sweden ([ROR:04ev03g22](https://ror.org/04ev03g22))

† Corresponding author

## Abstract

According to the efficient coding hypothesis, sensory neurons are adapted to provide maximal information about the environment, given some biophysical constraints. In early visual areas, stimulus-induced modulations of neural activity (or tunings) are predominantly single-peaked. However, periodic tuning, as exhibited by grid cells, has been linked to a significant increase in decoding performance. Does this imply that the tuning curves in early visual areas are sub-optimal? We argue that the time scale at which neurons encode information is imperative to understand the advantages of single-peaked and periodic tuning curves, respectively. Here, we show that the possibility of catastrophic (large) errors creates a trade-off between decoding time and decoding ability. We investigate how decoding time and stimulus dimensionality affect the optimal shape of tuning curves for removing catastrophic errors. In particular, we focus on the spatial periods of the tuning curves for a class of circular tuning curves. We show an overall trend for minimal decoding time to increase with increasing Fisher information, implying a trade-off between accuracy and speed. This trade-off is reinforced whenever the stimulus dimensionality is high, or there is ongoing activity. Thus, given constraints on processing speed, we present normative arguments for the existence of the single-peaked tuning organization observed in early visual areas.

## Introduction

One of the fundamental problems in systems neuroscience is understanding how sensory information can be represented in the spiking activity of an ensemble of neurons. The problem is exacerbated by the fact that individual neurons are highly noisy and variable in their responses, even to identical stimuli (Arieli et al., 1996). A common feature of early sensory representation is that the neocortical neurons in primary sensory areas change their average responses only to a small range of features of the sensory stimulus. For instance, some neurons in the primary visual cortex respond to moving bars oriented at specific angles (Hubel and Wiesel, 1962). This observation has led to the notion of tuning curves. Together, a collection of tuning curves provides a possible basis for a neural code.

A considerable emphasis has been put on understanding how the structure of noise and correlations affect stimulus representation given a set of tuning curves (Shamir and Sompolinsky, 2004; Averbeck and Lee, 2006; Franke et al., 2016; Zylberberg et al., 2016; Moreno-Bote et al., 2014; Kohn et al., 2016). More recently, the issue of local and catastrophic errors, dating back to the work of Shannon (Shannon, 1949), has been raised in the context of neuroscience (e.g. Xie, 2002; Sreenivasan and Fiete, 2011). Intuitively, local errors are small estimation errors that depend on the trial-by-trial variability of the neural responses and the local shapes of the tuning curves surrounding the true stimulus condition (Figure 1a bottom plot, see s1). On the other hand, catastrophic errors are very large estimation errors that depend on the trial-by-trial variability and the global shape of the tuning curves (Figure 1a bottom plot, see s2). While a significant effort has been put into studying how stimulus tuning and different noise structures affect local errors, less is known about the interactions with catastrophic errors. For example, Fisher information is a common measure of the accuracy of a neural code (Brunel and Nadal, 1998; Abbott and Dayan, 1999; Guigon, 2003; Moreno-Bote et al., 2014; Benichoux et al., 2017). The Cramér-Rao bound states that a lower limit of the minimal mean squared error (MSE) for any unbiased estimator is given by the inverse of Fisher information (Lehmann and Casella, 1998). Thus, increasing Fisher information reduces the lower bound on MSE. However, because Fisher information can only capture local errors, the true MSE might be considerably larger in the presence of catastrophic errors (Xie, 2002; Kostal et al., 2015; Malerba et al., 2022), especially if the available decoding time is short (Bethge et al., 2002; Finkelstein et al., 2018).

![Figure 1.](https://cdn.elifesciences.org/articles/84531/elife-84531-fig1-v3.jpg)

**Figure 1.:** (a) Top: A two-neuron system encoding a single variable using single-peaked tuning curves ($\lambda=1$). Bottom: The tuning curves create a one-dimensional activity trajectory embedded in a two-dimensional neural activity space (black trajectory). Decoding the two stimulus conditions, s1 and s2, illustrates the two types of estimation errors that can occur due to trial-by-trial variability, local ($s^_{1}$) and catastrophic ($s^_{2}$). (b) Same as in (a) but for periodic tuning curves ($\lambda=0.5$). Notice that the stimulus conditions are intermingled and that the stimulus can not be determined from the firing rates. (c) Time evolution of the root mean squared error (RMSE) using maximum likelihood estimation (solid line) and the Cramér-Rao bound (dashed line) for a population of single-peaked tuning curves ($N=600$, $w=0.3$, average evoked firing rate $f_{s⁢t⁢i⁢m}¯=20⁢exp⁡(-1/w)⁢B_{0}⁢(1/w)$ sp/s, and $b=2$ sp/s). For about 50 ms the RMSE is significantly larger than the predicted lower bound. (d) The empirical error distributions for the time point indicated in (c), where the RMSE strongly deviates from the predicted lower bound. Inset: A non-zero empirical error probability spans the entire stimulus domain. (e) Same as in (d) when the RMSE roughly converges to the Cramér-Rao bound. Notice the absence of large estimation errors.

A curious observation is that the tuning curves in early visual areas predominately use single-peaked firing fields, whereas grid cells in the entorhinal cortex are known for their periodically distributed firing fields (Hafting et al., 2005). It has been shown that the multiple firing locations of grid cells increase the precision of the neural code compared to single-peaked tuning curves (Sreenivasan and Fiete, 2011; Mathis et al., 2012; Wei et al., 2015). This raises the question of why periodic firing fields are not a prominent organization of early visual processing too?

The theoretical arguments in favor of periodic tuning curves have mostly focused on local errors under the assumption that catastrophic errors are negligible (Sreenivasan and Fiete, 2011). However, given the response variability, it takes a finite amount of time to accumulate a sufficient number of spikes to decode the stimulus. Given that fast processing speed is a common feature of visual processing (Thorpe et al., 1996; Fabre-Thorpe et al., 2001; Rolls and Tovee, 1994; Resulaj et al., 2018), it is crucial that each neural population in the processing chain can quickly produce a reliable stimulus-evoked signal. Therefore, the time required to produce signals without catastrophic errors will likely put fundamental constraints on any neural code, especially in early visual areas.

Here, we contrast Fisher information with the minimal decoding time required to remove catastrophic errors (i.e. the time until Fisher information becomes a reasonable descriptor of the MSE). We base the results on the maximum likelihood estimator for uniformly distributed stimuli (i.e., the maximum a posteriori estimator) using populations of tuning curves with different numbers of peaks. We show that the minimal decoding time tends to increase with increasing Fisher information in the case of independent Poissonian noise to each neuron. This suggests a trade-off between the decoding accuracy of a neural population and the speed by which it can produce a reliable signal. Furthermore, we show that the difference in minimal decoding time grows with the number of jointly encoded stimulus features (stimulus dimensionality) and in the presence of ongoing (non-specific) activity. Thus, single-peaked tuning curves require shorter decoding times and are more robust to ongoing activity than periodic tuning curves. Finally, we illustrate the issue of large estimation errors and periodic tuning in simple spiking neural network model tracking either a step-like stimulus change or a continuously time-varying stimulus.

## Results

### Shapes of tuning curves, Fisher information, and catastrophic errors

To enable a comparison between single-peaked and periodic (multi-peaked) tuning curves, we consider circular tuning curves responding to a D-dimensional stimulus, $s$, according to

$$
f_{i}(s)=a_{i}\prodj=1Dexp⁡(\frac{1}{w}(cos⁡(\frac{2\pi}{\lambda_{i}}(s_{j}−s_{i,j}^{′}))−1))+b
$$

where ai is the peak amplitude of the stimulus-related tuning curve $i$, $w$ is a width scaling parameter, $\lambda_{i}$ defines the spatial period of the tuning curve, $s_{i,j}^{′}$ determines the location of the peak(s) in the $j$:th stimulus dimension, and $b$ determines the amount of ongoing activity (see Figure 1a–b, top panels). The parameters are kept fixed for each neuron, thus ignoring any effect of learning or plasticity. In the following, the stimulus domain is set to $s\in[0,1)^{D}$ for simplicity. To avoid boundary effects, we assume that the stimulus has periodic boundaries (i.e. $s_{j}=0$ and $s_{j}=1$ are the same stimulus condition) and adjust any decoded value to lie within the stimulus domain, for example,

$$
s^_{ML}=1+0.1(mod1)=0.1,
$$

see Materials and methods - ’Implementation of maximum likelihood estimator’ for details.

We assume that the stimulus is uniformly distributed across its domain and that its dimensions are independent. This can be seen as a worst-case scenario as it maximizes the entropy of the stimulus. In a single trial, we assume that the number of emitted spikes for each neuron is conditionally independent, and follows a Poisson distribution, given some stimulus-dependent rate $f_{i}⁢(s)$. Thus, the probability of observing a particular activity pattern, $r$, in a population of $N$ neurons given the stimulus-dependent rates and decoding time, $T$, is

$$
p(r|s,T)=\prodi=1Np(r_{i}|Tf_{i}(s))=\prodi=1N\frac{(Tf_{i}(s))^{r_{i}}exp⁡(−Tf_{i}(s))}{r_{i}!}.
$$

Given a model of neural responses, the Cramér-Rao bound provides a lower bound on the accuracy by which the population can communicate a signal as the inverse of the Fisher information. For sufficiently large populations, using the population and spike count models in Equation 1 and Equation 3, Fisher information is given by (for $a_{i}=a$ and $b=0$ for all neurons, see Sreenivasan and Fiete, 2011 or Appendix 2 - 'Fisher information and the Cramér-Rao bound' for details)

$$
J≈(2\pi)^{2}\frac{aTN}{w}B_{0}(1/w)^{D−1}B_{1}(1/w)exp⁡(−D/w)\lambda^{−2}¯
$$

where $\lambda^{−2}¯$ denotes the sample average of the squared inverse of the (relative) spatial periods across the population, and $B_{\alpha}⁢(⋅)$ denotes the modified Bessel functions of the first kind. Equation 4 (and similar expressions) suggests that populations consisting of periodic tuning curves, for which $\lambda^{−2}¯≫1$, are superior at communicating a stimulus signal than a population using tuning curves with only single peaks, where $\lambda^{−2}¯=1$. However, (inverse) Fisher information only predicts the amount of local errors for an efficient estimator. Hence, the presence of catastrophic errors (Figure 1a, bottom) can be identified by large deviations from the predicted MSE for an asymptotically efficient estimator (Figure 1c–d). Therefore, we define minimal decoding time as the shortest time required to approach the Cramér-Rao bound (Figure 1c and e).

### Periodic tuning curves and stimulus ambiguity

To understand why the amount of catastrophic error can differ with different spatial periods, consider first the problem of stimulus ambiguity that can arise with periodic tuning curves. If all tuning curves in the population share the same relative spatial period, $\lambda$, then the stimulus-evoked responses can only provide unambiguous information about the stimulus in the range $[0,\lambda)$. Beyond this range, the response distributions are no longer unique. Thus, single-peaked tuning curves ($\lambda=1$) provide unambiguous information about the stimulus. Periodic tuning curves ($\lambda<1$), on the other hand, require the use of tuning curves with two or more distinct spatial periods to resolve the stimulus ambiguity (Fiete et al., 2008; Mathis et al., 2012; Wei et al., 2015). In the following, we assume the tuning curves are organized into discrete modules, where all tuning curves within a module share spatial period (Figure 1b) mimicking the organization of grid cells (Stensola et al., 2012). For convenience, assume that $\lambda_{1}>\lambda_{2}>...>\lambda_{L}$ where $L$ is the number of modules. Thus, the first module provides the most coarse-grained resolution of the stimulus interval, and each successive module provides an increasingly fine-grained resolution. It has been suggested that a geometric progression of spatial periods, such that $\lambda_{i}=c⁢\lambda_{i-1}$ for some spatial factor $0<c\leq1$, may be optimal for maximizing the resolution of the stimulus while reducing the required number of neurons (Mathis et al., 2012; Wei et al., 2015). However, trial-by-trial variability can still cause stimulus ambiguity and catastrophic errors - at least for short decoding times, as we show later, even when using multiple modules with different spatial periods.

### (Very) Short decoding times - when both Fisher information and MSE fails

While it is known that Fisher information is not an accurate predictor of the MSE when the decoding time is short (Bethge et al., 2002), less has been discussed about the issue of MSE. Although MSE is often interpreted as a measure of accuracy, its insensitivity to rare outliers makes it a poor measure of reliability. Therefore, comparing MSE directly between populations can be a misleading measure of reliability if the distributions of errors are qualitatively different. If the amounts of local errors differ, lower MSE does not necessarily imply fewer catastrophic errors. This is exemplified in Figure 2, comparing a single-peaked and a periodic population encoding a two-dimensional stimulus using the suggested optimal scale factor, $c≈1/1.44$ (Wei et al., 2015). During the first $≈30$ ms, the single-peaked population has the lowest MSE of the two populations despite having lower Fisher information (Figure 2a). Furthermore, comparing the error distribution after the periodic population achieves a lower MSE (the black circle in Figure 2a) shows that the periodic population still suffers from rare errors that span the entire stimulus range (Figure 2b–c, insets). As we will show, a comparison of MSE, as a measure of reliability, only becomes valid once catastrophic errors are removed. Here we assume that catastrophic errors should strongly affect the usability of a neural code. Therefore, we argue that the first criterion for any rate-based neural code should be to satisfy its constraint on decoding time to avoid catastrophic errors.

![Figure 2.](https://cdn.elifesciences.org/articles/84531/elife-84531-fig2-v3.jpg)

**Figure 2.:** (a) Time evolution of root mean squared error (RMSE), averaged across trials and stimulus dimensions, using maximum likelihood estimation (solid lines) for two populations (blue: $\lambda_{1}=1$, $c=1$, red: $\lambda_{1}=1$, $c=1/1.44$). Dashed lines indicate the lower bound predicted by Cramér-Rao. The black circle indicates the point where the periodic population has become optimal in terms of MSE. (b) The empirical distribution of errors for the time indicated by the black circle in (a). The single-peaked population (blue) has a wider distribution of errors centered around 0 compared to the periodic population (red), as suggested by having a higher MSE. Inset: Zooming in on rare error events reveals that while the periodic population has a narrower distribution of errors around 0, it also has occasional errors across large parts of the stimulus domain. (c) The empirical CDF of the errors for the same two populations as in (b). Inset: a zoomed-in version (last 1%) of the empirical CDF highlights the heavy-tailed distribution of errors for the periodic population. Parameters used in the simulations: stimulus dimensionality $D=2$, the number of modules $L=5$, number of neurons $N=600$, average evoked firing rate $f_{s⁢t⁢i⁢m}¯=20⁢exp⁡(-1/w)⁢B_{0}⁢(1/w)$ sp/s, ongoing activity $b=2$ sp/s, and width parameter $w=0.3$. Note that the estimation errors for the two stimulus dimensions are pooled together.

### Minimal decoding times in populations with two modules

How does the choice of spatial periods impact the required decoding time to remove catastrophic errors? To get some intuition, we first consider the case of populations encoding a one-dimensional stimulus using only two different spatial scales, $\lambda_{1}$ and $\lambda_{2}$. From the perspective of a probabilistic decoder (Seung and Sompolinsky, 1993; Deneve et al., 1999; Ma et al., 2006), assuming that the stimulus is uniformly distributed, the maximum likelihood (ML) estimator is Bayesian optimal (and asymptotically efficient). The maximum likelihood estimator aims at finding the stimulus condition which is the most likely cause of the observed activity, $r$, or

$$
s^_{ML}=argmaxs⁡p(r|s),
$$

where $p⁢(r|s)$ is called the likelihood function. The likelihood function equals the probability of observing the observed neural activity, $r$, assuming that the stimulus condition was $s$. In the case of independent Poisson spike counts (or at least independence across modules), each module contributes to the joint likelihood function $p⁢(r|s)$ with individual likelihood functions, Q1 and Q2 (Wei et al., 2015). Thus, the joint likelihood function can be seen as the product of the two individual likelihood functions, where each likelihood is $\lambda_{i}$-periodic

$$
p(r|s)=Q_{1}(r|s)Q_{2}(r|s).
$$

In this sense, each module provides its own ML-estimate of the stimulus, $s_{M⁢L}^{(1)}=arg⁢max_{s}⁡Q_{1}⁢(r|s)$ and $s_{M⁢L}^{(2)}=arg⁢max_{s}⁡Q_{2}⁢(r|s)$. Because of the periodicity of the tuning curves, there can be multiple modes for each of the likelihoods (e.g. Figure 3a and b, top panels). For the largest mode of the joint likelihood function to also be centered close to the true stimulus condition, the distance $\delta$ between $s_{M⁢L}^{(1)}$ and $s_{M⁢L}^{(2)}$ must be smaller than between any other pair of modes of Q1 and Q2. Thus, to avoid catastrophic errors, $\delta$ must be smaller than some largest allowed distance $\delta^{*}$ which guarantees this relation (see Equations 25–30 for calculation of $\delta^{*}$ assuming the stimulus is in the middle of the domain). As $\delta$ varies from trial to trial, we limit the probability of the decoder experiencing catastrophic errors to some small error probability, $p_{e⁢r⁢r⁢o⁢r}$, by imposing that

$$
Pr(|\delta|>\delta^{∗})<p_{error}.
$$

Assuming that the estimation of each module becomes efficient before the joint estimation, Equation 7 can be reinterpreted as a lower bound on the required decoding time before the estimation based on the joint likelihood function becomes efficient

$$
T_{th}>2(\frac{erfinv(1−p_{error})}{\delta^{∗}})^{2}(\frac{1}{J_{1,norm}}+\frac{1}{J_{2,norm}}),
$$

where $erfinv⁢(⋅)$ is the inverse of the error function and $J_{k,n⁢o⁢r⁢m}$ refers to the time-normalized Fisher information of module $k$ (see Materials and methods for derivation). Thus, the spatial periods of the modules influence the minimal decoding time by determining: (1) the largest allowed distance $\delta^{*}$ between the estimates of the modules and (2) the variances of the estimations given by the inverse of their respective Fisher information.

![Figure 3.](https://cdn.elifesciences.org/articles/84531/elife-84531-fig3-v3.jpg)

**Figure 3.:** (a) Top: Sampled individual likelihood functions of two modules with very different spatial periods. Bottom: The sampled joint likelihood function for the individual likelihood functions in the top panel. (b–c) Same as in (a) but for spatial periods that are similar but not identical and for a single-peaked population, respectively. (d) Bottom: The dependence of the scale factor c on the minimal decoding time for $\lambda_{1}=1$. Blue circles indicate the simulated minimal decoding times, and the black line indicates the estimation of the minimal decoding times according to Equation 8, with $p_{e⁢r⁢r⁢o⁢r}=10^{-4}$. Top left: The predicted value of $1/\delta^{*}$. Top right: The inverse of the Fisher information. (e) Same as (d) but for $\lambda_{1}=1/2$. (f) RMSE (lines), the 99.8th percentile (filled circles), and the maximal error (open circles) of the error distribution for several choices of scale factor, $c$, and decoding time. The color code is the same as in panels (d-e). The parameters used in (d-f) are: population size $N=600$, number of modules $L=2$, scale factors $c=0.05-1$, width parameter $w=0.3$, average evoked firing rate $f_{s⁢t⁢i⁢m}¯=20⁢exp⁡(-1/w)⁢B_{0}⁢(1/w)$ sp/s, ongoing activity $b=0$ sp/s, and threshold factor $\alpha=2$.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/84531/elife-84531-fig3-figsupp1-v3.jpg)

**Figure 3—figure supplement 1.:** Top: Sampled likelihood functions of two modules with $\lambda_{1}=1$ and $\lambda_{2}=1/2.3$. Bottom: The joint likelihood function is shifted across the periodic boundary. Such shifts across the periodic boundary can become more pronounced when $\lambda_{2}$ is slightly below a multiple of $\lambda_{1}$.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/84531/elife-84531-fig3-figsupp2-v3.jpg)

**Figure 3—figure supplement 2.:** Same as (Figure 2d–e) but using threshold factor $\alpha=1.2$.Notice the stronger deviations from the predicted minimal decoding time for $\lambda_{1}=1$ when c is slightly below $1/2,1/3,1/4,…$, etc.

To give some intuition of the approximation, if the spatial periods of the modules are very different, $\lambda_{2}≪\lambda_{1}$, then there exist many peaks of Q2 around the peak of Q1 (Figure 3a). Additionally, there can be modes of Q1 and Q2 far away from the true stimulus close together. Thus, $\lambda_{2}≪\lambda_{1}$ can create a highly multi-modal joint likelihood function where small deviations in $s_{M⁢L}^{(1)}$ and $s_{M⁢L}^{(2)}$ can cause a shift, or a change, of the maximal mode of the joint likelihood. To avoid this, $\delta^{*}$ must be small, leading to longer decoding times by Equation 8. Furthermore, suppose the two modules have similar spatial periods $\lambda_{2}∼\lambda_{1}$, or $\lambda_{1}$ is close to a multiple of $\lambda_{2}$. In that case, the distance between the peaks a few periods away is also small, again leading to longer decoding times (Figure 3b). In other words, periodic tuning suffers from the dilemma that small shifts in the individual stimulus estimates can cause catastrophic shifts in the joint likelihood function. Although these might be rare events, the possibility of such errors increases the probability of catastrophic errors. Thus, assuming $\lambda_{1}<1$, both small and large scale factors $c$ can lead to long decoding times. When $\lambda_{1}=1$, however, only small-scale factors $c$ pose such problems, at least unless the stimulus is close to the periodic edge (i.e. $s≈0$ or $s≈1$, see Figure 3—figure supplement 1). On the other hand, compared to single-peaked tuning curves, periodic tuning generally leads to sharper likelihood functions, increasing the accuracy of the estimates once catastrophic errors are removed (e.g., compare the widths of the joint likelihood functions in Figure 3a–c).

To test the approximation in Equation 8, we simulated a set of populations ($N=600$ neurons) with different spatial periods. The populations were created using identical tuning parameters except for the spatial periods, whose distribution varied across the populations, and the amplitudes, which were adjusted to ensure an equal average firing rate (across all stimulus conditions) for all neurons (see Materials and methods for details on simulations). As described above, the spatial periods were related by a scale factor $c$. Different values of $c$ were tested for the largest period being either $\lambda_{1}=1$ or $\lambda_{1}=1/2$. Furthermore, only populations with unambiguous codes over the stimulus interval were included (i.e. $c\neq1/2,1/3,1/4,…$ for $\lambda_{1}=1/2$; Mathis et al., 2012). Note, however, that there is no restriction on the periodicity of the tuning curves to align with the periodicity of the stimulus (i.e. $1/\lambda_{i}$ does not need to be an integer). For each population, the minimal decoding time was found by gradually increasing the decoding time until the empirical MSE was lower than twice the predicted lower bound (i.e. $\alpha=2$, see Equation 10 and Materials and methods for details). Limiting the probability of catastrophic errors to $p_{e⁢r⁢r⁢o⁢r}=10^{-4}$, Equation 8 is a good predictor of the minimal decoding time (Figure 3d–e, bottom panels, coefficient of determination $R^{2}≈0.92$ and $R^{2}≈0.95$ for $\lambda_{1}=1$ and $\lambda_{1}=1/2$, respectively). For both $\lambda_{1}=1$ and $\lambda_{1}=1/2$, the minimal decoding time increases overall with decreasing scale factor, $c$ (see Figure 3d–e). However, especially for $\lambda_{1}=1/2$, the trend is interrupted by large peaks (Figure 3e). For $\lambda_{1}=1$, there are deviations from the predicted minimal decoding time for small scale factors, $c$. They occur whenever $\lambda_{2}$ is slightly below a multiple of $\lambda_{1}=1$, and get more pronounced when increasing the sensitivity to the threshold factor $\alpha=1.2$ (see Figure 3—figure supplement 2). We believe one cause of these deviations is the additional shifts across the periodic boundary (as in Figure 3—figure supplement 1) that can occur when $c$ is just below $1/2,1/3,1/4,…$, etc.

To confirm that the estimated minimal decoding times have some predictive power on the error distributions, we re-simulated a subset of the populations for various decoding times, $T$, using 15,000 randomly sampled stimulus conditions (Figure 3f). Both the RMSE and outlier errors (99.8th percentile and the maximal error, that is, 100th percentile) agree with the shape of minimal decoding times, suggesting that a single-peaked population is good at removing large errors at very short time scales.

### Minimal decoding times for populations with more than two modules

From the two-module case above, it is clear that the choice of scale factor influences the minimal decoding time. However, Equation 8 is difficult to interpret and is only valid for two-module systems ($L=2$). To approximate how the minimal decoding time scales with the distribution of spatial periods in populations with more than two modules, we extended the approximation method first introduced by Xie (Xie, 2002). The method was originally used to assess the number of neurons required to reach the Cramér-Rao bound for single-peaked tuning curves with additive Gaussian noise for the ML estimator. In addition, it only considered encoding a one-dimensional stimulus variable. We adapted this method to approximate the required decoding time for stimuli with arbitrary dimensions, Poisson-distributed spike counts, and tuning curves with arbitrary spatial periods. In this setting, the scaling of minimum decoding time with the spatial periods, $\lambda_{1},…,\lambda_{L}$, can be approximated as (see Materials and methods for derivation)

$$
T_{th}≫A(w)\frac{1}{aN}\frac{exp⁡(D/w)}{B_{0}(1/w)^{(D−1)}}\frac{\lambda^{−3}¯^{2}}{\lambda^{−2}¯^{3}}≃\frac{A^{∗}(w)}{Nf_{stim}(D)¯}\frac{\lambda^{−3}¯^{2}}{\lambda^{−2}¯^{3}},
$$

where $\lambda^{−2}¯$ and $\lambda^{−3}¯$ indicate the sample average across the inverse spatial periods (squared or cubed, respectively) in the population, $f_{stim}(D)¯$ is the average evoked firing rate across the stimulus domain, and $A(w)$ (or $A^{∗}(w)$) is a function of $w$ (see Materials and methods for detailed expression). The last approximation holds with equality whenever all tuning curves have an integer number of peaks. The derivation was carried out assuming the absence of ongoing activity and that the amplitudes within each population are similar, $a_{1}≈…≈a_{N}$. Importantly, the approximation also assumes the existence of a unique solution to the maximum likelihood equations. Therefore, it is ill-equipped to predict the issues of stimulus ambiguity. Thus, going back to the two-module cases, Equation 9 cannot capture the additional effects of $\lambda_{2}≪\lambda_{1}$ or when $\lambda_{1}$ is close to a multiple of $\lambda_{2}$, as in Figure 3d–e. On the other hand, complementing the theory presented in Equation 8, Equation 9 provides a more interpretable expression of the scaling of minimal decoding time. For $c\leq1$, the minimal decoding time, $T_{t⁢h}$, is expected to increase with decreasing scale factor, $c$ (see Equation 47). The scaling should also be similar for different choices of $\lambda_{1}$. Furthermore, assuming all other parameters are constant, the minimal decoding time should grow roughly exponentially with the number of stimulus dimensions.

To confirm the validity of Equation 9, we simulated populations of $N=600$ tuning curves across $L=5$ modules. Again, the spatial periods across the modules were related by a scale factor, $c$ (Figure 4a). To avoid the effects of $c≪1$, we limited the range of the scale factor to $0.3\leqc\leq1$. The upper bound on $c$ was kept (for $\lambda_{1}=1$) to include entirely single-peaked populations. Again, the assumption of homogeneous amplitudes in Equation 9 was dropped in simulations (Figure 4b, left column) to ensure that the average firing rate across the stimulus domain is equal for all neurons (see Figure 4b, right column, for the empirical average firing rates). This had little effect on Fisher information, where the theoretical prediction was based on the average amplitudes across all populations with the same $\lambda_{1}$ and stimulus dimensionality $D$ (see Figure 4c, inset). As before, Fisher information grows with decreasing scale factor, $c$, and with decreasing spatial period $\lambda_{1}$. As expected, increasing the stimulus dimensionality decreases Fisher information if all other parameters are kept constant. On the other hand, the minimal decoding time increases with decreasing spatial periods and increases with stimulus dimensionality (Figure 4c). The increase in decoding time between $D=1$ and $D=2$ is also very well predicted by Equation 9, at least for $c>0.5$ (Figure 4—figure supplement 1a). In these simulations, the choice of width parameter is compatible with experimental data (Ringach et al., 2002), but similar trends were found for a range of different width parameters (although the differences become smaller for small $w$, see Figure 4—figure supplement 1b–d).

![Figure 4.](https://cdn.elifesciences.org/articles/84531/elife-84531-fig4-v3.jpg)

**Figure 4.:** (a) Illustration of the likelihood functions of a population with $L=5$ modules using scale factor $c=0.7$. (b) The peak stimulus-evoked amplitudes of each neuron (left column) were selected such that all neurons shared the same expected firing rate for a given stimulus condition (right column). (c) Inset: Plot of average Fisher information as a function of the scale factor $c$ (colored lines: estimations from simulation data, black lines: theoretical approximations). Main plot: Plot of minimal decoding time as a function of scale factor $c$. Minimal decoding time tends to increase with decreasing grid scales (colored lines: estimated minimal decoding time from simulations, black lines: fitted theoretical predictions using Equation 47). The gray color corresponds to points with large discrepancies between the predicted and the simulated minimal decoding times. (d) Plot of the average Fisher information against the minimal decoding time. Points colored in gray are the same as in panel (c). (e) RMSE (lines), the 99.8th percentile (filled circles), and the maximal error (open circles) of the error distribution when decoding a 1-dimensional stimulus for several choices of decoding time. The color code is the same as above. (f) same as (e) but for a two-dimensional stimulus. Note that the error distributions across stimulus dimensions are pooled together. Parameters used in panels (a-d): population size $N=600$, number of modules $L=5$, scale factors $c=0.3-1$, width parameter $w=0.3$, average evoked firing rate $f_{s⁢t⁢i⁢m}¯=20⁢exp⁡(-D/w)⁢B_{0}⁢(1/w)^{D}$ sp/s, ongoing activity $b=0$ sp/s, and threshold factor $\alpha=2$.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/84531/elife-84531-fig4-figsupp1-v3.jpg)

**Figure 4—figure supplement 1.:** (a) The predicted minimal decoding time from $D=1$ scaled by $\frac{exp⁡(1/w)}{B_{0}⁢(1/w)}$ provides a reasonable prediction of the minimal decoding time for $D=2$. The data used is the same as in Figure 4c (solid lines with circles, color code the same as in the main figure). (b–d) Minimal decoding times for various width parameters $w$. As in Figure 4c, there is a trend of increasing minimal decoding time with decreasing scale factor $c$. However, the range of minimal decoding times decreases with decreasing widths (for $D=1$).

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/84531/elife-84531-fig4-figsupp2-v3.jpg)

**Figure 4—figure supplement 2.:** Same as Figure 4a–d in the main text, but simulated using threshold factor. For each $T$, the MSE is evaluated based on 15,000 random stimulus samples.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/84531/elife-84531-fig4-figsupp3-v3.jpg)

**Figure 4—figure supplement 3.:** Same as Figure 4a–d in the main text, but simulated using the one-sided KS-test for determining minimal decoding time (see main text for details). For each $T$, the MSE is evaluated based on 15,000 random stimulus samples.

![Figure 4—figure supplement 4.](https://cdn.elifesciences.org/articles/84531/elife-84531-fig4-figsupp4-v3.jpg)

**Figure 4—figure supplement 4.:** (a) Time evolution of the RMSE (non-transparent lines) for periodic and single-peaked populations and the lower bound set by the Cramér-Rao bound (transparent lines) when decoding a $D=1$ stimulus. (b) Same as in (a) but for the 99.8th (non-transparent lines) and the 100th (transparent lines) percentiles of the root squared error distributions. (c–d) same as (a-b) but for a $D=2$ stimulus. For each decoding time $T$, the RMSE and outliers are evaluated based on 15,000 random stimulus samples.

![Figure 4—figure supplement 5.](https://cdn.elifesciences.org/articles/84531/elife-84531-fig4-figsupp5-v3.jpg)

**Figure 4—figure supplement 5.:** Plot of the mean spike counts (summed over the population) required to remove catastrophic errors for the populations in Figure 4. Each circle indicates the minimal spike count for a single population with a constant scale factor encoding either a one-dimensional (x-axis) or a two-dimensional stimulus (y-axis). Blue circles indicate $\lambda_{1}=1$ and red circles $\lambda_{1}=1/2$. Being on the grey line corresponds to having the same required spike count for both stimulus cases.

![Figure 4—figure supplement 6.](https://cdn.elifesciences.org/articles/84531/elife-84531-fig4-figsupp6-v3.jpg)

**Figure 4—figure supplement 6.:** Same as Figure 4c, e and f, but only using tuning curves with an integer number of peaks, that is, being all integers. Thus, there is no common scale factor relating the spatial frequencies of the modules within a population. The populations here have $1/\lambda=[1]$, $[1,2]$, $[1,3]$, $[1,4]$, $[1,2,3]$, $[1,2,4]$, $[1,3,4]$, or $[1,2,3,4]$. Note that for the single-peaked population, $\lambda^{−3}¯^{2}/\lambda^{−2}¯^{3}=1$. (a) Shows the RMSE (solid lines) and the outliers, 99.8th (filled circles) and 100th (open circles) percentiles, for a $D=1$ stimulus. (b) Same as (a) but for a $D=2$ stimulus. (c) Same as Figure 4c but for the integer peaked populations listed above (blue: $D=1$, green: $D=2$).

From Equation 9, we fitted two constants, K1 (regressor) and K2 (intercept), using least square regression across populations sharing the same largest period, $\lambda_{1}$, and stimulus dimensionality, $D$ (see Equation 47). Within the simulated range of scale factors, the regressions provide reasonable fits for the populations with $\lambda_{1}=1$ (Figure 4c, coefficient of determination $R^{2}≈0.89$ and $R^{2}≈0.90$ for $D=1$ and $D=2$, respectively). For the populations with $\lambda_{1}=1/2$, Equation 9 becomes increasingly unable to predict the behavior of the minimal decoding time as $c$ approaches 1 (see the red and yellow lines in Figure 4c–d). On the other hand, as was suggested above, the scaling of the minimal decoding time with $c$ is, in fact, similar for $\lambda_{1}=1$ and $\lambda_{1}=1/2$ whenever $c$ is less than $≈0.9$. As suggested by Figure 4d, there is also a strong correlation between Fisher information and minimal decoding time, again indicating a speed-accuracy trade-off. Furthermore, similar results are obtained when either decreasing the threshold factor to $\alpha=1.2$ (Figure 4—figure supplement 2) or changing the minimal decoding time criterion to a one-sided Kolmogorov–Smirnov test (KS-test) between the empirical distribution of errors and the Gaussian error distribution predicted by the Cramér-Rao bound (Figure 4—figure supplement 3, using an ad-hoc Bonferroni-type correction for multiple sequential testing, $\alpha/j$, where $j$ is the $j$ th time comparison and $\alpha=0.05$ is the significance level.)

To further illustrate the relationship between minimum decoding time and the distribution of catastrophic errors, we re-simulated the same populations using fixed decoding times, evaluating the RMSE together with the 99.8th and 100th (maximal error) percentiles of the root squared error distributions across 15,000 new uniformly sampled stimuli (Figure 4e–f). As suggested by the minimal decoding times, there is a clear trade-off between minimizing RMSE over longer decoding times and removing outliers, especially the maximal error, over shorter decoding times. Figure 4—figure supplement 4 shows the time evolution for a few of these populations.

Additionally, to verify that the minimal decoding times are good predictors of the decoding time necessary to suppress large estimation errors, we compared the same error percentiles as in Figure 4e–f (i.e. the 99.8th and 100th percentiles) against the minimal decoding times, $T_{t⁢h}$, estimated in Figure 4c. For each population, we expect a strong reduction in the magnitude of the largest errors when the decoding time, $T$, is larger than the minimal decoding time, $T_{t⁢h}$. Figure 5 shows a clear difference in large estimation errors between populations for which $T_{th}<T$ and populations with $T_{th}>T$ (circles to the left and right of the magenta lines in Figure 5, respectively). Thus, although only using the difference between MSE and Fisher information, our criterion on minimal decoding time still carries important information about the presence of large estimation errors.

![Figure 5.](https://cdn.elifesciences.org/articles/84531/elife-84531-fig5-v3.jpg)

**Figure 5.:** (a) The 99.8th percentile (filled circles) and the maximal error (i.e., 100th percentile, open circles) of the root squared error distributions for $D=1$ against the estimated minimal decoding time for the corresponding populations ($\alpha=2$) for various choices of decoding time, $T$ (indicted by the vertical magenta lines). (b) same as (a) but for $D=2$. (c-d) Same as for (a-b) but for $\alpha=1.2$. Note that the plots (a) and (c), or (b) and (d), illustrate the same percentile data only remapped on the x-axis by the different minimal decoding times from the different threshold factors $\alpha$. Color code: same as in Figure 4.

To summarize, while periodic tuning curves provide lower estimation errors for long decoding times by minimizing local errors (Figure 4c, inset), a population of single-peaked tuning curves is faster at producing a statistically reliable signal by removing catastrophic errors (Equation 9 and Figure 4c). Generalizing minimal decoding times to an arbitrary number of stimulus dimensions reveals that the minimal decoding time also depends on the stimulus dimensionality (Figure 4c, compare lines for $D=1$ and $D=2$). Interestingly, however, the approximation predicts that although minimal decoding time grows with increasing stimulus dimensionality, the minimal required spike count might be independent of stimulus dimensionality, at least for populations with integer spatial frequencies, that is, integer number of peaks (see Equation A5.4). The populations simulated here have non-integer spatial frequencies. However, the trend of changes in the mean spike count is still just slightly below 1 (indicating that slightly fewer spikes across the population are needed with increasing $D$, see Figure 4—figure supplement 5). Thus, as the average firing rate decreases with the number of encoded features $D$ (Figure 4b, right column), the increase in minimal decoding time for stimuli of higher dimensionality can be primarily explained by requiring a longer time to accumulate the sufficient number of spikes across the population. Lastly, to rule out that the differences in minimal decoding time cannot be explained by the periodicity of the tuning curves not aligning to that of the stimulus, we also simulated populations with different combinations of integer peaks (Figure 4—figure supplement 6). Again, the same phenomenon is observed: periodic tuning curves increase the required decoding time to remove catastrophic errors. This also highlights that the approximation of minimal decoding time does not require the spatial periods to be related by a scale factor, $c$.

### Effect of ongoing activity

Many cortical areas exhibit ongoing activity, that is, activity that is not stimulus-specific (Snodderly and Gur, 1995; Barth and Poulet, 2012). Thus, it is important to understand the impact of ongoing activity on the minimal decoding time, too. Unfortunately, because our approximation of the minimal decoding times did not include ongoing activity, we relied on simulations to study the effect of such non-specific activity.

When including independent ongoing (background) activity at 2 spikes/s to all neurons for the same populations as in Figure 4, minimal decoding times were elevated across all populations (Figure 6). Furthermore, the minimal decoding time increased faster with decreasing $c$ in the presence of ongoing activity compared to the case without ongoing activity (ratios of fitted regressors $K_{1}⁢(b=2)/K_{1}⁢(b=0)$ using Equation 47 were approximately 1.69 and 1.72 for $D=1$ and $D=2$, respectively). Similar results are found using $\alpha=1.2$ (Figure 6—figure supplement 1) or the alternative criterion on minimal decoding time based on one-sided KS-tests described earlier (Figure 6—figure supplement 2). Thus, ongoing activity can have a substantial impact on the time required to produce reliable signals. Figure 6 suggests that areas with ongoing activity are less suited for periodic tuning curves. Especially, the combination of multidimensional stimuli and ongoing activity leads to much longer minimal decoding times for tuning curves with small spatial periods ($c≪1$). For example, when encoding a two-dimensional stimulus, only the populations with $\lambda_{1}=1$, $c=1$ and $\lambda_{1}=1$, $c=0.95$ could remove catastrophic errors in less than 40ms when ongoing activity at 2 sp/s was present. Thus, the ability to produce reliable signals at high speeds severely deteriorates for periodic tuning curves in the presence of non-specific ongoing activity.

![Figure 6.](https://cdn.elifesciences.org/articles/84531/elife-84531-fig6-v3.jpg)

**Figure 6.:** (a) The case of encoding a one-dimensional stimulus ($D=1$) with or without ongoing activity at 2 sp/s (diamond and circle shapes, respectively). (b) The case of a two-dimensional stimulus ($D=2$) under the same conditions as for (a). In both conditions, ongoing activity increases the time required for all populations to produce reliable signals, but the effect is strongest for $c≪1$. The parameters used in the simulations are: population size $N=600$, number of modules $L=5$, scale factors $c=0.3-1$, width parameter $w=0.3$, average evoked firing rate $f_{s⁢t⁢i⁢m}¯=20⁢exp⁡(-D/w)⁢B_{0}⁢(1/w)^{D}$ sp/s, ongoing activity $b=2$ sp/s, and threshold factor $\alpha=2$.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/84531/elife-84531-fig6-figsupp1-v3.jpg)

**Figure 6—figure supplement 1.:** Same as Figure 6 in the main text, but using $\alpha=1.2$.

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/84531/elife-84531-fig6-figsupp2-v3.jpg)

**Figure 6—figure supplement 2.:** Same as Figure 6 in the main text, but using the one-sided KS-test criterion described before (see Figure 4—figure supplement 4).

This result has an intuitive explanation. The amount of catastrophic errors depends on the probability that the trial variability reshapes the neural activity to resemble the possible activities for a distinct stimulus condition (see Figure 1a). From the analysis presented above, periodic tuning curves have been suggested to be more susceptible to such errors. Adding ongoing activity does not reshape the stimulus-evoked parts of the tuning curves but only increases the trial-by-trial variability. Thus, by this reasoning, it is not surprising that the systems which are already more susceptible also are even more negatively affected by the increased variability induced by ongoing activity. The importance of Figure 6 is that even ongoing activity as low as 2 sp/s can have a clearly visible effect on minimal decoding time.

### Implications for a simple spiking neural network with sub-optimal readout

Until this point, the arguments about minimal decoding time have relied on rate-based tuning curves encoding static stimuli. To extend beyond static stimuli and to exemplify the role of decoding time for spiking neurons, we simulated simple two-layer feed-forward spiking neural networks to decode time-varying stimulus signals. The first layer ($N_{1}=500$) corresponds to the tuning curves (without connections between the simulated neurons). The stimulus-specific tuning of the Poissonian inputs to these neurons is either fully single-peaked, creating a population of single-peaked tuning curves, or periodic with different spatial periods, creating a population of periodic tuning curves (Figure 7a, see Materials and methods for details). The second layer instead acts as a readout layer ($N_{2}=400$, allowing a weak convergence of inputs from the first layer). This layer receives both stimulus-specific excitatory input from the first layer and external non-specific Poissonian excitation (corresponding to background activity). The connection strength between the first and second layers depends on the difference in preferred stimulus conditions between the pre- and post-synaptic neurons. Such connectivity could, for example, be obtained by unsupervised Hebbian learning. Because the tuning curves in the first layer can be periodic, they can also connect strongly to several readout neurons. We introduced lateral inhibition among the readout neurons (without explicitly modeling inhibitory neurons) to create a winner-take-all style of dynamics. The readout neurons with large differences in preferred stimulus inhibit each other more strongly. Decoding is assumed to be instantaneous and based on the preferred stimulus condition of the spiking neuron in the readout layer. However, to compare the readouts, we averaged the stimulus estimates in sliding windows.

![Figure 7.](https://cdn.elifesciences.org/articles/84531/elife-84531-fig7-v3.jpg)

**Figure 7.:** (a) Illustration of the spiking neural networks (SNNs). (b) Example of single trials. Top row: Two example trials for step-like change in stimulus (green line). The left and right plots show the readout activity for the single-peaked (blue) and periodic SSNs (orange), respectively. Note that the variance around true stimulus is larger for the single-peaked SNN (i.e. larger local errors) but that there are fewer very large errors than for the periodic SNN. Bottom row: Same as for the top row but with a continuously time-varying stimulus. (c) Bottom: The median RMSE (thick lines) over all trials in a sliding window (length 50ms) for the single-peaked (blue) and periodic (orange) SNNs. The shadings correspond to the regions between the 5th and 95th percentiles. Top: The instantaneous population firing rates of the readout layers and the standard deviations (same color code as in the bottom panel). (d) Bottom left: The median estimated stimulus across trials in a sliding window (length 10ms) for the single-peaked (blue) and periodic (orange) SNNs. Shaded areas again correspond to the regions between the 5th and 95th percentiles. The true stimulus is shown in green. Bottom right: the average firing rate of each neuron, arranged according to the preferred stimulus condition. Top: The instantaneous population firing rates of the readout layers and the standard deviations. See Materials and methods for simulation details and Table 1, Table 2, Table 3 for all parameters used in the simulation.

We tested two different types of time-varying stimuli: (1) a step-like change from $s=0.25$ to $s=0.75$ (Figure 7b top row, green trace) and (2) a continuously time-varying stimulus drawn from an Ornstein–Uhlenbeck process (Figure 7b bottom row, green trace; see Materials and methods). In the case of a step-like stimulus change, the readout layer for the single-peaked population required a shorter time to switch states than the periodic network (Figure 7c). The shorter switching time is consistent with the hypothesis that single-peaked tuning curves have shorter minimal decoding times than periodic tuning curves. In these simulations, the difference is mainly due to some neurons in the first layer of the periodic network responding both before and after the step change. Thus, the correct readout neurons (after the change) must compensate for the hyper-polarization built up before the change and the continuing inhibitory input from the previously correct readout neurons (which still get excitatory inputs). Note that there are only minor differences in the population firing rates between the readout layers, confirming that this is not a consequence of different excitation levels but rather of the structures of excitation.

The continuously time-varying stimulus could be tracked well by both networks. However, averaging across trials shows that SNNs with periodic tuning curves have larger sporadic fluctuations (Figure 7d). This suggests that decoding with periodic tuning curves has difficulties in accurately estimating the stimulus without causing sudden, brief periods of large errors. To make a statistical comparison between the populations, we investigated the distributions of root mean squared error (RMSE) across trials. In both stimulus cases, there is a clear difference between the network with single-peaked tuning curves and the network with periodic ones. For the step-like change in stimulus condition, a significant difference in RMSE arises roughly 100 ms after the stimulus change (Figure 8a). For the time-varying stimulus, using single-peaked tuning curves also results in significantly lower RMSE compared to a population of periodic tuning curves (Figure 8b, RMSE calculated across the entire trial).

![Figure 8.](https://cdn.elifesciences.org/articles/84531/elife-84531-fig8-v3.jpg)

**Figure 8.:** (a) Step-like change: Comparison between the distributions of accumulated RMSEs at different decoding times ($p=0.4$, $9.0⋅10^{-4}$, and $8.7⋅10^{-5}$, respectively). (b) OU-stimulus: The distributions of RMSE across trials for the two SNNs ($p=4.3⋅10^{-8}$). All statistical comparisons in (a) and (b) were based on two-sample Kolmogorov–Smirnov (KS) tests using 30 trials per network.

## Discussion

Several studies have suggested that periodic tuning creates an unparalleled precise neural code by minimizing local errors (Sreenivasan and Fiete, 2011; Mathis et al., 2012; Wei et al., 2015; Malerba et al., 2022). Nevertheless, despite this advantage of periodic tuning, single-peaked tuning curves are widespread in early sensory areas and especially in the early visual system. There is a long history of studying information representation using rate-based tuning curves. Still, the effect of spatial periodicity and catastrophic errors on the required decoding time has not been addressed. Here, we showed that the possibility of catastrophic estimation errors (Figure 1a) introduces the possibility that different shapes of tuning curves can have different minimal decoding times.

The emerging question is whether there is a trade-off between the accuracy of a neural code and the minimal required decoding time for single-peaked and periodic tuning. The answer is yes. We found that minimal decoding time increased with decreasing spatial periods of the tuning curves (Figure 4c), suggesting a trade-off between accuracy and speed for populations of tuning curves. The differences in minimal decoding time cannot be explained by the periodicity of the tuning curves not aligning to the stimulus domain, as the same holds comparing populations with integer number of peaks (Figure 4—figure supplement 6). Furthermore, our results remained unchanged when we discarded any decoded stimuli which needed the $mod⁢1$ operation to lie within the stimulus domain $[0,1)^{D}$, thus ruling out any possible distortion effect of the periodic stimulus and decoding approach. In addition, we show that our results are valid for a range of population sizes (Figure 9a-b), ongoing (Figure 9a-b) and evoked activities (Figure 9c), and stimulus dimensions (Figure 9d). We used the more conservative threshold factor on MSE, $\alpha=1.2$, to capture all the nuances w.r.t. the level of ongoing activity even for large population sizes. In simulated networks with spiking neurons, we showed that the use of periodic tuning curves increased the chances of large estimation errors, leading to longer times before switching ‘states’ (Figure 7c) and difficulties tracking a time-varying, one-dimensional stimulus (Figure 7d).

![Figure 9.](https://cdn.elifesciences.org/articles/84531/elife-84531-fig9-v3.jpg)

**Figure 9.:** (a-b) Minimal decoding time for different combinations of population sizes ($N$) and levels of ongoing background activity ($b$) for the single-peaked population (a) and the periodic population (b). (c) Minimal decoding time as a function of average stimulus-evoked firing rate (x-axis re-scaled to the corresponding peak amplitude, $a$, for single-peaked tuning curves for easier interpretation). The corresponding amplitudes are $a=8,16,$ and $32$ sp/s, respectively. (d) Minimal decoding time as a function of stimulus dimensionality. Unless indicated on the axes, the parameters are set according to the orange circles and rectangles in (a-d). Auxiliary parameters: number of modules $L=5$, width parameter $w=0.3$, and threshold factor $\alpha=1.2$.

Experimental data suggest that decoding times can be very short, of the order of tens of milliseconds, reflecting that a considerable part of the information contained in firing rates over long periods is also present in short sample periods (Tovée et al., 1993). Additionally, the first few spikes have been shown to carry significant amounts of task information in both visual (Resulaj et al., 2018), olfactory (Resulaj and Rinberg, 2015), and somatosensory areas (Panzeri et al., 2001; Petersen et al., 2001). As the tuning curves in this study all have equal average firing rates, we can reinterpret the minimal decoding time in terms of the prominence of the first spikes. In our simulations, tens of spikes carry enough information to produce a reliable stimulus estimate free of catastrophic errors (Figure 4—figure supplement 5). As with decoding time, single-peaked tuning curves also need fewer spikes to produce reliable signals. Thus, the speed-accuracy trade-off can be reinterpreted as a trade-off between being accurate and efficient.

The notion of a speed-accuracy trade-off is further strengthened when considering high-dimensional stimuli that demand longer minimal decoding times. Natural stimuli typically have higher dimensionality than those used in animal experiments. Many sensory neurons are tuned to multiple features of the external stimulus, creating mixed selectivity of features (e.g. Garg et al., 2019). For neurons responding to task-related variables, mixed selectivity has been shown to enable linear separability and to improve discriminability (Rigotti et al., 2013; Fusi et al., 2016; Johnston et al., 2020). For continuous stimulus estimations, mixed selectivity has also been proposed to decrease MSE when decoding time is limited (Finkelstein et al., 2018). However, to remove catastrophic errors, which, as we have argued, is not necessarily synonymous with lower MSE, the exponential increase in minimal decoding time could easily lead to very long decoding times. Thus, minimal decoding time should set a bound on the number of features a population can jointly encode reliably. In addition, neurons in sensory areas often exhibit a degree of non-specific activity (Snodderly and Gur, 1995; Barth and Poulet, 2012). Introducing ongoing activity to the populations in our simulations further amplified the differences in minimal decoding times (Figure 6). Thus, for jointly encoded stimuli, especially in areas with high degrees of ongoing activity, a population of single-peaked tuning curves might be the optimal encoding strategy for rapid and reliable communication.

We note that these results might extend beyond the visual areas, too. Although this study focused on tuning curves encoding continuous variables, catastrophic errors can also occur in systems with discrete tuning curves. Sensory stimuli can be fast-varying (or even discontinuous), and large errors can potentially harm the animal. Therefore, constraints on decoding time are likely important for any early sensory area. In addition, hippocampal place cells involved in spatial navigation (O’Keefe and Dostrovsky, 1971; Wilson and McNaughton, 1993) are known for their single-peaked tuning. The interesting observation in this context is that place cells produce reliable signals faster than their input signals from the medial entorhinal cortex with a combination of single- and multi-peaked tuning (Cholvin et al., 2021). On the other hand, for sufficiently slow-varying stimuli, a periodic population can be used together with error correction to remove catastrophic errors (Sreenivasan and Fiete, 2011). Furthermore, for non-periodic stimuli with large domains, the combinatorial nature of periodic tuning curves can create unique stimulus representations far exceeding the spatial periods of the tuning curves (Fiete et al., 2008). Thus, periodic tuning curves are ideal for representing space, where the stimulus domain can be vast, and the change in position is constrained by the speed of movement. Interestingly, when faced with very large arenas, place cells can also exhibit multi-peaked tuning (Eliav et al., 2021).

To summarize, we provide normative arguments for the single-peaked tuning of early visual areas. Rapid decoding of stimulus is crucial for the survival of the animals. Consistent with this, animals and humans can process sensory information at impressive speeds. For example, the human brain can generate differentiating event-related potentials to go/no-go categorization tasks using novel complex visual stimuli in as little as 150 ms (Thorpe et al., 1996). These ‘decoding’ times do not decrease for highly familiar objects, suggesting that the speed of visual processing cannot be reduced by learning (Fabre-Thorpe et al., 2001). Given constraints on low latency communication, it is crucial that each population can quickly produce a reliable signal. In this regard, single-peaked tuning curves are superior to periodic ones. The fact that early visual areas exhibit ongoing activity and encode multi-dimensional stimuli further strengthens the relevance of the differences in minimal decoding time.

To conclude, our work highlights that minimum decoding time is an important attribute and should be considered while evaluating candidate neural codes. Our analysis suggests that decoding of high-dimensional stimuli can be prohibitively slow with rate-based tuning curves. Experimental data on the representation of high-dimensional stimuli is rather scant as relatively low-dimensional stimuli are typically used in experiments (e.g. oriented bars). Our work gives a compelling reason to understand whether and how biological brains can reliably encode high-dimensional stimuli at behaviorally relevant time scales.

## Materials and methods

### Minimal decoding times - simulation protocols

To study the dependence of decoding time $T$ on MSE for populations with different distributions of spatial frequencies, we simulated populations of synthetic tuning curves (Equation 1). The stimulus was circular with a $[0,1)^{D}$ range. The preferred stimulus conditions $s^{′}$ were sampled independently from a random uniform distribution over $[0,1)^{D}$ (independently and uniformly for each stimulus dimension). To ensure equal comparison, the preferred locations $s^{′}$ were shared across all populations. Each neuron’s amplitude, ai, was tuned according to Equation A1.5 to ensure an equal average firing rate across the stimulus domain for all neurons. In each trial, a stimulus $s\in[0,1)^{D}$ was also independently sampled from a uniform distribution over $[0,1)^{D}$. The spike count for each neuron was then sampled according to Equation 3.

Minimal decoding time was defined as the shortest time for which the neural population approximately reaches the Cramér-Rao bound. To estimate the reaction time in simulations, we incrementally increased the decoding time $T$ (using 1 ms increments, starting at $T=1$ ms) until

$$
MSE(T,\lambda)¯\leq\alpha⋅diag(J(T,\lambda)^{−1})¯.
$$

As the ML estimator is asymptotically efficient (attaining the Cramér-Rao bound in the limit of infinite data), the threshold factor, $\alpha$, in Equation 10 was added as a relaxation (see figure captions for choices of $\alpha$). Note that the mean bars on the left- and right-hand sides of Equation 10 refer to the means across stimulus dimensions (for multi-dimensional stimuli) and that $diag⁢(⋅)$ refers to taking the diagonal elements from the inverse of the Fisher information matrix, $J(T,\lambda)^{−1}$. For a given decoding time $T$, the estimation of MSE was done by repeatedly sampling random stimulus conditions (from a uniform distribution), sampling a noisy response to the stimulus (Poisson distributed spike counts), and then applying maximum likelihood estimation (see next section ’Implementation of maximum likelihood estimator’ for details on implementation). In Figures 3 and 9, 15000 stimulus conditions were drawn for each $T$, and in Figure 4, stimulus conditions were repeatedly drawn until the two first non-zero digits of the MSE were stable for 1000 consecutive trials. However, in controls not presented here, we could not see any significant difference between these two sampling approaches. Because the Fisher information matrix $J$ was analytically estimated only in the special case without ongoing activity, it was approximated in simulations by the element-wise average across 10,000 randomly sampled stimulus conditions (also uniformly distributed), where each element was calculated according to Equation A2.12or Equation A2.13 given a random stimulus trial.

### Implementation of maximum likelihood estimator

Given some noisy neural responses, $r$, the maximum likelihood estimator (MLE) chooses the stimulus condition which maximizes the likelihood function, $s^_{M⁢L}=arg⁢max_{s}⁡ℒ⁢(r,s)=arg⁢max_{s}⁢\prod_{i=1}^{N}p⁢(r_{i}|s)$. A common approach is to instead search for the maximum of the log-likelihood function (the logarithm is a monotonic function and therefore preserves any maxima/minima). The stimulus-dependent terms of the log-likelihood can then be expressed as

$$
log⁡p(r|s)∝V(r;s)=\sumi=1Nr_{i}log⁡(Tf_{i}(s))−Tf_{i}(s).
$$

Unfortunately, the log-likelihood function is not guaranteed to be concave, and finding the stimulus condition $s^_{M⁢L}$ which maximizes the log-likelihood function is not trivial (a non-convex optimization problem). To overcome this difficulty, we combined grid-search with the Nelder–Mead method, an unconstrained non-linear program solver (implemented using MATLAB’s built-in function fminsearch, https://www.mathworks.com/help/matlab/ref/fminsearch.html).

Grid search was used to find a small set of starting points with large log-likelihood values. To do so, we sampled 100 random stimulus conditions within the stimulus interval $[0,1)^{D}$ and selected the four stimulus conditions with the largest log-likelihood values. The true stimulus condition, $s_{t⁢r⁢u⁢e}$, was always added to the set of starting points regardless of the log-likelihood value of that condition (yielding a total of 5 starting points).

Then the Nelder–Mead method was used with these starting points to find a set of 5 (possibly local) maxima. The stimulus was decoded as the stimulus, $s^$, yielding the largest log-likelihood of the 5 maxima. As we always included the true stimulus condition in the Nelder-Mead search, this approach should not overestimate the amount of threshold distortion but can potentially miss some global estimation errors instead. Finally, as the Nelder–Mead method is unconstrained but the stimulus domain periodic, the output of the maximum likelihood decoder was transformed into the stimulus interval $[0,1)^{D}$ by applying the mod 1 operation on each stimulus dimension,

$$
s^_{ML}=s^(mod1).
$$

Given an estimated stimulus, $s^_{M⁢L}$, the error was then evaluated along each stimulus dimension independently, taking into account the periodic boundary,

$$
ϵ_{i}^{2}=min[(s_{i}−s^_{ML,i})^{2},(s_{i}−s^_{ML,i}+1)^{2},(s_{i}−s^_{ML,i}−1)^{2}]
$$

for $i\in{1,…,D}$.

Lastly, to rule out that the estimates before the mod-operation, $s^$, outside of the stimulus domain $[0,1)^{D}$ did not influence the results, we also discarded these samples, but this produced similar results.

### Spiking network model

#### Stimuli

As in the previous simulations, we assumed that the stimulus domain was a circular stimulus defined between $[0,1)$. We simulated the responses to two different types of stimuli, (1) a step-like change in stimulus condition from $s=0.25$ to $s=0.75$ and (2) a stimulus drawn from a modified Ornstein–Uhlenbeck process

$$
\frac{ds_{t}}{dt}=−\frac{s_{t}}{\tau_{s}}+\sqrt{\frac{2\sigma_{s}^{2}}{\tau_{s}}}ξ_{s}(mod 1).
$$

For parameter values, see Table 1.

**Table 1.**
 Parameters and parameter values for O-U stimulus.


<table>
  <thead>
    <tr>
      <th>Parameters</th>
      <th>Parameter values</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>τs</td>
      <td>0.5 (s)</td>
    </tr>
    <tr>
      <td>σs</td>
      <td>0.1</td>
    </tr>
  </tbody>
</table>

#### Network model

The spiking networks were implemented as two-layer, feed-forward networks using LIF neurons with (Dirac) delta synapses. The dynamics of the membrane potential for the neurons in the first layer were described by

$$
\frac{dV_{i}}{dt}=−\frac{V_{i}−V_{rest}}{\tau_{mem}}+\sumkJ_{E}\delta(t−t_{k}),
$$

where $V_{i}$ is the voltage of neuron $i$, $\tau_{m⁢e⁢m}$ the membrane time constant, tk the timing of the $k$ th input spike to neuron $i$, and $J_{E}$ the induced EPSP. The neurons in the first layer were constructed to correspond to either single-peaked or periodic tuning curves. Two networks were tested, one network where the first layer corresponds to single-peaked tuning curves and a second network corresponding to periodic tuning curves (with $L=4$ modules). For each neuron $i$ in module $j$ in the first layer, the input was drawn from independent Poisson point processes with stimulus-dependent rates $f_{i}^{(j)}⁢(s⁢(t))$

$$
f_{i}^{(j)}(s(t))=aexp⁡(\frac{1}{w}(cos⁡(\frac{2\pi}{\lambda_{j}}(s(t)−s_{i}^{(j)}))−1))+b.
$$

Here, the constants $a$ and $b$ were chosen such that the baseline firing rate was slightly above zero and the maximal firing rate was slightly below 20 sp/s (see Table 3 for all network-related parameter values). Because of the choice of $\lambda_{j}$, the modulation strengths of the inputs were such that the average input to each neuron was equal. For each module in the first layer, the preferred locations $s_{i}^{(j)}$ were equidistantly placed across $[0,\lambda_{j})$.

Similarly, for the second layer, the membrane potential was described by

$$
\frac{dV_{i}}{dt}=−\frac{V_{i}−V_{rest}}{\tau_{mem}}+\sumj\in[1,...,N_{1}]\sumkJ_{EE}(Δ_{i,j})\delta(t−t_{k}^{(j)}−d)+\sumj\in[1,...,N_{2}]\sumkJ_{I}(Δ_{i,j})\delta(t−t_{k}^{(j)}−d)+\sumkJ_{E}\delta(t−t_{k}),
$$

where $J_{E⁢E}⁢(Δ_{i,j})$ and $J_{I}⁢(Δ_{i,j})$ are synapse-specific EPSPs/IPSPs which depends on the difference in preferred tuning $Δ_{i,j}$ between the pre- and post-synaptic neurons (see Equation 18), $t_{k}^{(j)}$ the timing of the $k$ th spike of pre-synaptic neuron $j$, and $d$ the delay (see Table 2, Table 3 for parameter values). The neurons in the second layer were only tuned to a single preferred stimulus location each, equidistantly placed across $[0,1)$. Whenever a spike occurred in the first layer, it elicited EPSPs with a delay of 1.5 ms in all neurons in the second layer. The size of the EPSPs depended on the difference in preferred tuning, $Δ_{i,j}$, between the pre- and post-synaptic neurons

$$
J_{EE}(Δ_{i,j})=exp⁡(\frac{1}{w_{ro}}(cos⁡(2\piΔ_{i,j})−1))J_{EE}.
$$

Here, $J_{E⁢E}$ determines the maximal EPSP (mV), and the constant $w_{r⁢o}$ was chosen such that the full width at half maximum of the EPSP kernels tiled the stimulus domain without overlap. Note that for periodically tuned neurons in the first layer (i.e. with multiple preferred locations), the $Δ_{i,j}$ were determined by the smallest difference in preferred tuning across the multiple preferred locations.

As for the excitatory neurons in the first layer, whenever a spike occurred in the second layer, it elicited IPSPs with a delay of 1.5 ms in all other neurons in the second layer. Again, the size of the IPSPs depended on the difference in preferred tuning, $Δ_{i,j}$ between the two neurons, but this time according to

$$
J_{I}(Δ_{i,j})=−|sin⁡(\piΔ_{i,j})|J_{I}.
$$

Thus, the range of inhibition was much broader compared to the excitation.

**Table 2.**
 Parameters and parameter values for LIF neurons.


<table>
  <thead>
    <tr>
      <th>Parameters</th>
      <th>Parameter values</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Membrane time constant, τmemb (ms)</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Threshold memb. potential, Vth (mV)</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Reset memb. potential (mV)</td>
      <td>10</td>
    </tr>
    <tr>
      <td>Resting potential, V0 (mV)</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Refractory period, τrp (ms)</td>
      <td>2</td>
    </tr>
  </tbody>
</table>

**Table 3.**
 Spiking network parameters and parameter values.


<table>
  <thead>
    <tr>
      <th>Parameters</th>
      <th>Parameter values</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Number of neurons 1st layer, N1</td>
      <td>500</td>
    </tr>
    <tr>
      <td>Number of neurons 2nd layer, N2</td>
      <td>400</td>
    </tr>
    <tr>
      <td>Maximal stimulus-evoked input rate, a (sp/s)</td>
      <td>750</td>
    </tr>
    <tr>
      <td>Baseline input rate, b (sp/s)</td>
      <td>4250</td>
    </tr>
    <tr>
      <td>Spatial periods, λj</td>
      <td>[1] or [1,2,3,4]</td>
    </tr>
    <tr>
      <td>Width parameter, w</td>
      <td>0.3</td>
    </tr>
    <tr>
      <td>Width parameter (readout layer), wro</td>
      <td>(π/N2)22log⁡(2)</td>
    </tr>
    <tr>
      <td>Input EPSP (1st layer), JE (mV)</td>
      <td>0.2</td>
    </tr>
    <tr>
      <td>Maximal EPSP (2nd layer), JEE (mV)</td>
      <td>2</td>
    </tr>
    <tr>
      <td>Maximal IPSP (2nd layer), JII (mV)</td>
      <td>2</td>
    </tr>
    <tr>
      <td>Synaptic delays, d (ms)</td>
      <td>1.5</td>
    </tr>
  </tbody>
</table>

#### Evaluating decoding performance

We assumed that the decoder was instantaneously based on the neuron index of the firing neuron in the readout layer. Let $Φ⁢(t_{k})$ denote a function that provides the index of the neuron firing at time tk. Given the equidistant distribution of preferred locations for the readout neurons, the stimulus is instantaneously decoded by mapping the neuron identity to the interval $[0,1]$

$$
s^(t_{k})=\frac{Φ(t_{k})}{N_{2}},
$$

where N2 is the number of neurons in the readout layer. For both stimulus cases, the decoding performance was evaluated using (1) the distribution of RMSE (Figure 7d) or estimated stimulus conditions (Figure 7e) in a sliding window or (2) the distributions of accumulated RMSE (Figure 8).

### Parameters

#### Simulation tools

All the simulations were done using code written in MATLAB and Python (using Brian2 simulator Stimberg et al., 2019). The simulation code is available at https://github.com/movitzle/Short_Decoding_Time (copy archived at Lenninger, 2023 ).

### Approximating minimal decoding time in two-module systems

To gain an understanding of the interaction between two modules with different spatial periods, consider the likelihood function as a product of the likelihood functions of the two modules individually

$$
p⁢(r|s)=Q_{1}⁢(s)⁢Q_{2}⁢(s).
$$

Using the Laplace approximation, each of these functions can be approximated as a periodic sum of Gaussians (Wei et al., 2015). Assuming that each module becomes efficient before the joint likelihood, we only focus on the largest, periodically occurring, peaks

$$
Q_{i}(s)≈Q^_{i}(r^{(i)}|s)=A_{i}\sumn_{i}=−K_{i}K_{i}exp⁡(−\frac{Σ_{i}}{2}(s−(s_{ML}^{(i)}+n_{i}\lambda_{i}))^{2}),
$$

where $r^{(i)}$ denotes the activity pattern of module $i$, $s_{M⁢L}^{(i)}$ the peak closest to the true stimulus condition, s0, and $K_{i}$ is large enough for $Q^_{i}⁢(r^{(i)}|s)$ to cover the entire stimulus range $[0,1)$. The approximation can be seen as ‘rolling out’ the stimulus domain from $[0,1)$ to $ℝ$. Therefore, to neglect the impact of the stimulus boundary, we assume that the stimulus is in the middle of the stimulus domain and $K_{1}=⌈\frac{1}{2⁢\lambda_{1}}⌉$ and $K_{2}=⌈\frac{1}{2⁢\lambda_{2}}⌉$. Furthermore, assuming that each module is efficient, the width of the Gaussians can be approximated as

$$
Σ_{i}≈−\frac{d^{2}}{ds^{2}}log⁡Q_{i}(s)≈J_{i}(s),
$$

where $J_{i}⁢(s)≈J_{i}$ is the Fisher information of module $i$. The joint likelihood function can thus be approximated as

$$
p(r|s)≈Q^_{1}(r^{(1)}|s)Q^_{2}(r^{(2)}|s)==A_{1}A_{2}\sumn_{1}=−K_{1}K_{1}exp⁡(−\frac{J_{1}}{2}(s−(s_{ML}^{(1)}+n_{1}\lambda_{1}))^{2})\sumn_{2}=−K_{2}K_{2}exp⁡(−\frac{J_{2}}{2}(s−(s_{ML}^{(2)}+n_{2}\lambda_{2}))^{2}).
$$

As the likelihood functions depend on the particular realization of the spike counts, the distance between the modes of the respective likelihoods closest to the true stimulus condition s0, $\delta_{0,0}=s_{M⁢L}^{(1)}-s_{M⁢L}^{(2)}$, is a random variable. Note that in the Results section, $\delta_{0,0}$ is simply referred to as $\delta$ for clarity.

The joint likelihood distribution $p⁢(r|s)$ has its maximal peak close to the true stimulus condition s0 if $\delta_{0,0}$ is the smallest distance between any pairs of peaks of Q1 and Q2 (see Equation A3.7 for details). Assuming that both modules provide efficient estimates, the distance $\delta_{0,0}$ can be approximated as a normally distributed random variable

$$
\delta_{0,0}=s_{ML}^{(1)}−s_{ML}^{(2)}=(s_{ML}^{(1)}−s_{0})−(s_{ML}^{(2)}−s_{0})∼N(0,\frac{1}{T}(J_{1,norm}^{−1}+J_{2,norm}^{−1})),
$$

where $J_{k,n⁢o⁢r⁢m}$ refers to the time-normalized Fisher information of module $k$. Thus, as the decoding time $T$ increases, the variance of $\delta_{0,0}$ decreases. Hence, it is necessary for the decoding time $T$ to be large enough such that it is rare for $\delta_{0,0}$ not to be the smallest distance between any pair of peaks. Similarly, the distance between the other pair of peaks in Q1 and Q2 within the stimulus range becomes

$$
\delta_{n_{1},n_{2}}=(s_{ML}^{(1)}+n_{1}\lambda_{1})−(s_{ML}^{(2)}+n_{2}\lambda_{2})==\delta_{0,0}+(n_{1}\lambda_{1}−n_{2}\lambda_{2}),
$$

where $n_{1}\in{-K_{1},…,K_{1}}$ and $n_{2}\in{-K_{2},…,K_{2}}$ are indexing the different Gaussians as before. Thus, the threshold for catastrophic error is reached when there is another pair of modes with the same distance between them, that is,

$$
|\delta_{0,0}|=|\delta_{n_{1},n_{2}}|=|\delta_{0,0}+(n_{1}\lambda_{1}−n_{2}\lambda_{2})|,
$$

for some n1 and n2 belonging to the index sets as above. Thus, to avoid catastrophic errors, it is necessary that

$$
|\delta_{0,0}|\leq|\delta_{0,0}+(n_{1}\lambda_{1}−n_{2}\lambda_{2})|,
$$

for all $n_{1}\in{-K_{1},…,K_{1}}$ and $n_{2}\in{-K_{2},…,K_{2}}$. By solving Equation 28, and taking into account that $\delta_{0,0}$ can be either positive or negative, we get the maximally allowed displacement

$$
\delta^{∗}=minn_{1},n_{2}:(n_{1},n_{2})\neq(0,0),n_{1}\in{−K_{1},...,K_{1}},n_{2}\in{−K_{2},...,K_{2}}\frac{1}{2}|(n_{1}\lambda_{1}−n_{2}\lambda_{2})|.
$$

Note that for $\lambda_{1}=1$, all n1 represent the same mode (but one full rotation 1 away). Thus, we limit the search such that $\lambda_{1}|n_{1}|<1$ and $\lambda_{2}|n_{2}|<1$. Assuming that the period of the second module is a scaling of the first module, $\lambda_{2}=c⁢\lambda_{1}$, the above equation becomes

$$
\delta^{∗}=minn_{1},n_{2}:(n_{1},n_{2})\neq(0,0)\frac{1}{2}|\lambda_{1}(n_{1}−n_{2}c)|.
$$

Note that stimulus ambiguity can never be resolved if $\delta_{n_{1},n_{2}}=\delta_{0,0}$ for some pair $(n_{1},n_{2})\neq(0,0)$, which is analogous to the condition in Mathis et al., 2012. To limit the probability of catastrophic estimation errors from the joint distribution to some small error probability $p_{e⁢r⁢r⁢o⁢r}$, the following should hold

$$
Pr(|\delta_{0,0}|>\delta^{∗})<p_{error}.
$$

Because $\delta_{0,0}∼N(0,J_{1}^{−1}+J_{2}^{−1})$, we have

$$
Pr(|\delta_{0,0}|>\delta^{∗})=1−erf(\frac{\delta^{∗}}{\sqrt{2}\sigma})<p_{error},
$$

where $erf⁢(⋅)$ is the error-function and $\sigma=\sqrt{J_{1}^{-1}+J_{2}^{-1}}$. By rearranging the terms and using Equation A2.8, we can obtain a lower bound on the required decoding time

$$
T_{th}>2(\frac{erf^{−1}(1−p_{error})}{\delta^{∗}})^{2}(\frac{1}{J_{1,norm}}+\frac{1}{J_{2,norm}}),
$$

where $J_{i,n⁢o⁢r⁢m}$ is the time-normalized Fisher information of module $i$. Note that $\delta^{*}$ can easily be found using an exhaustive search according to Equation 29 or Equation 30.

### Approximating minimal decoding time

To approximate the order by which the population reaction time scales with the distribution of spatial periods and the stimulus dimensionality, we extended the approximation method introduced by Xie, 2002. The key part of the approximation method is to use a Taylor series to reason about which conditions must hold for the distribution of errors to be normally distributed with a covariance equal to the inverse of the Fisher information matrix. Note that this approximation assumes the existence of a unique solution to the maximum likelihood equations, thus, it does not apply to ambiguous neural codes (e.g. $c=1/2,1/3,1/4,…$, etc.).

First, let’s recollect the Taylor series with Lagrangian reminder for a general function g

$$
g(x+\delta)=g(x)+g^{′}(x)\delta+\frac{1}{2}g^{′′}(x^{∗})\delta^{2},
$$

where $x^{*}$ is somewhere on the interval $[x,x+\delta)$. Thus, in the multivariate case, the derivative in the j:th direction of the log-likelihood function for stimulus condition $s^_{M⁢L}=s^$ can be rewritten using a Taylor series with Lagrangian reminder as

$$
\frac{∂}{∂s_{k}}log⁡p(r|s)|_{s=s^}=\frac{∂}{∂s_{k}}log⁡p(r|s)|_{s=s^{∘}}+\suml=1D\frac{∂^{2}}{∂s_{l}∂s_{k}}log⁡p(r|s)|_{s=s^{∘}}(s^_{l}−s_{l}^{∘})++\frac{1}{2}\suml=1D\summ=1D\frac{∂^{3}}{∂s_{m}∂s_{l}∂s_{k}}log⁡p(r|s)|_{s=s^{∗}}(s^_{l}−s_{l}^{∘})(s^_{m}−s_{m}^{∘}),
$$

for all $k\in{1,…,D}$ where $s^{∘}$ is the true stimulus condition and $s^{*}$ is a stimulus point between $s^{∘}$ and $s^$.

If the estimated stimulus is close to the true stimulus, then the quadratic order terms are small. If so, the variance of $(s^-s^{∘})$ converges towards $N(0,J^{−1})$ (in distribution), where $J$ is the Fisher information matrix (Lehmann and Casella, 1998). However, if the estimated stimulus is not close to the true stimulus, then the quadratic terms are not negligible. Therefore, when $T$ is sufficiently large, and the variance of the estimation follows the Cramér-Rao bound, the following should hold for all $k\in{1,…,D}$

$$
|\suml=1D\frac{∂^{2}}{∂s_{l}∂s_{k}}log⁡p(r|s)|_{s=s^{∘}}(s^_{l}−s_{l}^{∘})|≫|\frac{1}{2}\suml=1D\summ=1D\frac{∂^{3}}{∂s_{m}∂s_{l}∂s_{k}}log⁡p(r|s)|_{s=s^{∗}}(s^_{l}−s_{l}^{∘})(s^_{m}−s_{m}^{∘})|.
$$

In this regime, we make the following term-wise approximations

$$
\frac{∂^{2}}{∂s_{l}∂s_{k}}log⁡p(r|s)|_{s=s^{∘}}≈E[\frac{∂^{2}}{∂s_{l}∂s_{k}}log⁡p(r|s)|_{s=s^{∘}}]=−J_{k,l}(s^{∘})=−J_{k,l},
$$

and

$$
\frac{∂^{3}}{∂s_{m}∂s_{l}∂s_{k}}log⁡p(r|s)|_{s=s^{∗}}≈E[\frac{∂^{3}}{∂s_{m}∂s_{l}∂s_{k}}log⁡p(r|s)|_{s=s^{∗}}]=M_{k,l,m}(s^{∗}),
$$

which gives

$$
|\suml=1DJ_{k,l}(s^_{l}−s_{l}^{∘})|≫|\frac{1}{2}\suml=1D\summ=1DM_{k,l,m}(s^{∗})(s^_{l}−s_{l}^{∘})(s^_{m}−s_{m}^{∘})|.
$$

Because $M_{k,l,m}≈0$ unless $k=l=m$ (see Equation A4.3, Equation A4.4, Equation A4.5), Equation 39 simplifies to

$$
|\suml=1DJ_{k,l}(s^_{l}−s_{l}^{∘})|≫|\frac{1}{2}M_{k,k,k}(s^{∗})(s^_{k}−s_{k}^{∘})^{2}|.
$$

Furthermore, because $J⁢(s)$ is a diagonal matrix (see Equation A2.18), we have

$$
|J_{k,k}(s^_{k}−s_{k}^{∘})|≫|\frac{1}{2}M_{k,k,k}(s^{∗})(s^_{k}−s_{k}^{∘})^{2}|.
$$

Next, by taking the square of the absolute values, we obtain

$$
J_{k,k}^{2}(s^_{k}−s_{k}^{∘})^{2}≫\frac{1}{4}M_{k,k,k}^{2}(s^{∗})((s^_{k}−s_{k}^{∘})^{2})^{2}.
$$

Because we assumed that $N$ and $T$ are sufficiently large to meet the Cramér-Rao bound, we have that

$$
(s^_{k}−s_{k}^{∘})(s^_{l}−s_{l}^{∘})∼{J¯^{−1}}_{k,l}.
$$

Inserting Equation 43 into Equation 42 gives

$$
J_{k,k}^{2}{J^{−1}}_{k,k}≫\frac{1}{4}M_{k,k,k}^{2}(s^{∗})({J^{−1}}_{k,k})^{2},
$$

or, equivalently,

$$
1≫\frac{1}{4}M_{k,k,k}^{2}(s^{∗}){J^{−1}}_{k,k}^{3}=\frac{1}{4}\frac{M_{k,k,k}^{2}(s^{∗})}{{J}_{k,k}^{3}}.
$$

By approximating the term $M_{k,k,k}⁢(s^{*})$ with an upper bound $M^{*}$ (see Equation A4.10) and using the expression for Fisher information (Equation A2.8), the expression for population reaction times can be obtained as

$$
T_{th}≫A(w)\frac{1}{aN}B_{0}(\frac{1}{w})^{−(D−1)}exp⁡(\frac{D}{w})\frac{\lambda^{−3}¯^{2}}{\lambda^{−2}¯^{3}},
$$

where $A⁢(w)$ is a function of $w$. Lastly, by casting Equation 46 in terms of the scale factor $c$, and fitting using (for example) least square regression, we obtain

$$
T_{th}≈K_{1}A(w)\frac{1}{aM}\frac{exp⁡(D/w)}{B_{0}(1/w)^{(D−1)}}\frac{(\sumj=0L−1c^{−3j})^{2}}{(\sumj=0L−1c^{−2j})^{3}}+K_{2},
$$

where $M$ is the number of neurons per module, and K1 and K2 are constants. Note that in the simulations, $w$ is fixed and $A⁢(w)$ can therefore be incorporated into K1.
