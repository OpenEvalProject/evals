# Bayesian inference of kinetic schemes for ion channels by Kalman filtering

## Authors

- Jan L Münch<sup>1</sup> ([ORCID: 0000-0002-9177-6466](https://orcid.org/0000-0002-9177-6466)) †
- Fabian Paul<sup>2</sup>
- Ralf Schmauder<sup>1</sup>
- Klaus Benndorf<sup>1</sup> ([ORCID: 0000-0002-0707-4083](https://orcid.org/0000-0002-0707-4083)) †

### Affiliations

1. Institut für Physiologie II, Universitätsklinikum Jena, Friedrich Schiller University Jena Jena Germany ([ROR:05qpz1x62](https://ror.org/05qpz1x62))
2. Department of Biochemistry and Molecular Biology, University of Chicago Chicago United States ([ROR:024mw5h28](https://ror.org/024mw5h28))

† Corresponding author

## Abstract

Inferring adequate kinetic schemes for ion channel gating from ensemble currents is a daunting task due to limited information in the data. We address this problem by using a parallelized Bayesian filter to specify hidden Markov models for current and fluorescence data. We demonstrate the flexibility of this algorithm by including different noise distributions. Our generalized Kalman filter outperforms both a classical Kalman filter and a rate equation approach when applied to patch-clamp data exhibiting realistic open-channel noise. The derived generalization also enables inclusion of orthogonal fluorescence data, making unidentifiable parameters identifiable and increasing the accuracy of the parameter estimates by an order of magnitude. By using Bayesian highest credibility volumes, we found that our approach, in contrast to the rate equation approach, yields a realistic uncertainty quantification. Furthermore, the Bayesian filter delivers negligibly biased estimates for a wider range of data quality. For some data sets, it identifies more parameters than the rate equation approach. These results also demonstrate the power of assessing the validity of algorithms by Bayesian credibility volumes in general. Finally, we show that our Bayesian filter is more robust against errors induced by either analog filtering before analog-to-digital conversion or by limited time resolution of fluorescence data than a rate equation approach.

## Introduction

Ion channels are essential proteins for the homeostasis of an organism. Disturbance of their function by mutations often causes severe diseases, such as epilepsy (Oyrer et al., 2018; Goldschen-Ohm et al., 2010), sudden cardiac death (Clancy and Rudy, 2001), or sick sinus syndrome (Verkerk and Wilders, 2014) indicating a medical need (Goldschen-Ohm et al., 2010) to gain further insight into the biophysics of ion channels. The gating of ion channels is usually interpreted by kinetic schemes which are inferred either from macroscopic currents with rate equations (REs) (Colquhoun and Hawkes, 1995b; Celentano and Hawkes, 2004; Milescu et al., 2005; Stepanyuk et al., 2011; Wang et al., 2012) or from single-channel currents using dwell time distributions (Neher and Sakmann, 1976; Colquhoun et al., 1997a; Horn and Lange, 1983; Qin et al., 1996; Epstein et al., 2016; Siekmann et al., 2016) or hidden Markov models (HMMs) (Chung et al., 1990; Fredkin and Rice, 1992; Qin et al., 2000; Venkataramanan and Sigworth, 2002). A HMM consists of a discrete set of metastable states. Changes of their occupation occur as random events over time. Each state is characterized by transition probabilities, related to transition rates, and a probability distribution of the observed signal (Rabiner, 1989). It is becoming increasingly clear that the use of Bayesian statistics in HMM estimation constitutes a major advantage (Ball et al., 1999; De Gunst et al., 2001; Rosales et al., 2001; Rosales, 2004; Gin et al., 2009; Siekmann et al., 2012; Siekmann et al., 2011; Hines et al., 2015; Sgouralis and Pressé, 2017b; Sgouralis and Pressé, 2017a; Kinz-Thompson and Gonzalez, 2018). In ensemble patches, simultaneous orthogonal fluorescence measurement of either conformational changes (Zheng and Zagotta, 2000; Taraska and Zagotta, 2007; Taraska et al., 2009; Bruening-Wright et al., 2007; Kalstrup and Blunck, 2013; Kalstrup and Blunck, 2018; Wulf and Pless, 2018) or ligand binding itself (Biskup et al., 2007; Kusch et al., 2010; Kusch et al., 2011; Wu et al., 2011) has increased insight into the complexity of channel activation.

Currently, a Bayesian estimator that can collect information from cross-correlations and time correlations inherent in multi-dimensional signals of ensembles of ion channels is still missing. Traditionally, macroscopic currents are analyzed with solutions of REs which yield a point estimate of the rate matrix or its eigenvalues (Colquhoun et al., 1997a; Sakmann and Neher, 2013; d’Alcantara et al., 2002; Milescu et al., 2005; Wang et al., 2012) if they are fitted to the data. The RE approach is based on a deterministic differential equation derived by averaging the chemical master equation (CME) for the underlying kinetic scheme (Kurtz, 1972; Van Kampen, 1992; Jahnke and Huisinga, 2007). Its accuracy can be improved by processing the information contained in the intrinsic noise (stochastic gating and binding) (Milescu et al., 2005; Munsky et al., 2009). Nevertheless, all deterministic approaches do not use the information of the time- and cross-correlations of the intrinsic noise. These deterministic approaches are asymptotically valid for an infinite number of channels. Thus, a time trace with a finite number of channels contains, strictly speaking, only one independent data point. Previous rigorous attempts to incorporate the autocorrelation of the intrinsic noise of current data into the estimation (Celentano and Hawkes, 2004) suffer from cubic computational complexity (Stepanyuk et al., 2011) in the amount of data points, rendering the algorithm non-optimal or even impractical for a Bayesian analysis of larger data set. To understand this, note, that a maximum likelihood optimization (ML) usually takes several orders of magnitude fewer likelihood evaluations to converge compared to the number of posterior evaluations when one samples the posterior. One Monte Carlo iteration (Betancourt, 2017) evaluates the posterior distribution and its derivatives many times to propose one sample from the posterior. Stepanyuk suggested an algorithm (Stepanyuk et al., 2011; Stepanyuk et al., 2014) which derives from the algorithm of Celentano and Hawkes, 2004 but evaluates the likelihood quicker. Under certain conditions, Stepanyuk’s algorithm can be faster than the Kalman filter (Moffatt, 2007). The algorithm by Milescu et al., 2005 achieves its superior computation time efficiency at the cost of ignoring the time correlations of the fluctuations. A further argument for our approach, independent of the Bayesian context, is investigated in this paper: The KF is the minimal variance filter (Anderson and Moore, 2012). Instead of strong analog filtering of currents to reduce the noise, but with the inevitable signal distortions (Silberberg and Magleby, 1993), we suggest to apply the KF with higher analyzing frequency on minimally filtered data.

On the one hand, a complete HMM analysis (forward algorithm) would deliver the most exact likelihood of macroscopic data. On the other hand, the computational complexity of the forward algorithm limits this type of analysis in ensemble patches to no more than a few hundred channels per time trace (Moffatt, 2007). To tame the computational complexity (Jahnke and Huisinga, 2007), we approximate the solution of the CME with a Kalman filter (KF), thereby remaining in a stochastic framework Kalman, 1960. This allows us to explicitly model the time evolution of the first two moments (mean value and covariance matrix) of the probability distribution of the hidden channel states. Notably, for linear (first or pseudo) Gaussian system dynamics, the KF is optimal in producing a minimal prediction error for the mean state. KFs have been used previously in several protein expression studies which also demonstrate the connection of the KF to the linear noise approximation (Komorowski et al., 2009; Finkenstädt et al., 2013; Fearnhead et al., 2014; Folia and Rattray, 2018; Calderazzo et al., 2019; Gopalakrishnan et al., 2011).

Our approach generalizes the work of Moffatt, 2007 by including state-dependent fluctuations such as open-channel noise and Poisson noise in additional fluorescence data. A central technical difficulty which we solved is that due to the state-dependent noise the central Bayesian update equation loses its analytical solution. We derived an approximation which is correct for the first two moments of the probability distributions. Stochastic rather than deterministic modeling is generally preferable for small systems or non-linear dynamics (Van Kampen, 1992; Gillespie and Golightly, 2012). However, even with simulated data of unrealistic high numbers of channels per patch (more than several thousands within one patch), the KF outperforms the deterministic approach in estimating the model parameters. Moffatt, 2007 already demonstrated the advantage of the KF to learn absolute rates from time traces at equilibrium. Like all algorithms that estimate the variance and the mean (Milescu et al., 2005) the KF can infer the number of channels $N_{ch}$ for each time trace, the single-channel current $i$ and analogous in optical recordings the mean number $\lambda_{b}$ of photons from bound ligands per recorded frame. To select models and to identify parameters, stochastic models are formulated within the framework of Bayesian statistics where parameters are assigned uncertainties by treating them as random variables (Hines, 2015; Ball, 2016). In contrast, previous work on ensemble currents combined the KF only with ML estimation (Moffatt, 2007). Difficulties in treating simple stochastic models by ML approaches in combination with the KF (Auger-Méthé et al., 2016), especially with non-observable dynamics, justify the computational burden of Bayesian statistics. Bayesian statistics has an intuitive way to incorporate soft or hard constrains from diverse sources of prior information. Those sources include mathematical prerequisites, other experiments, simulations or theoretical assumptions. They are applied as additional model assumptions by a prior probability distribution over the possible parameter space. Hence, knowledge of the model parameters prior to the experiment are correctly accounted for in the analyzes of the new data. Alternatively, some of these benefits of prior knowledge can be incorporated by penalized maximum likelihood (Salari et al., 2018; Navarro et al., 2018). Bayesian inference provides outmatching tools for modeling over point estimates: First, the Bayesian approach is still applicable in situations where parameters are not identifiable (Hines et al., 2014; Middendorf and Aldrich, 2017b) or posteriors are non-Gaussian, whereas ML fitting ceases to be valid (Calderhead et al., 2013; Watanabe, 2007). Second, a Bayesian approach provides superior model selection tools for singular models such as HMMs or KFs Gelman et al. (2014). Third, Bayesian statistics has a correct uncertainty quantification (Gillespie and Golightly, 2012) based on the data and the prior for the statistical problem. In contrast, ML or maximum posterior approaches lack uncertainty quantification based on one data set (Joshi et al., 2006). Only under optimal conditions their uncertainty quantification becomes equivalent to Bayesian credibility volumes (Jaynes and Kempthorne, 1976). This study focuses on the effects on the posterior due to formulating the likelihood via a KF instead of an RE approach and the benefits of adding a second dimension of observation. We consider the performance of our algorithm against the gold standards in four different aspects: (I) The relative distance of the posterior to the true values, (II) the uncertainty quantification, here in the form of the shape of the posterior, (III) parameter identifiability, and (IV) robustness against typical misspecifications of the likelihood (such as ignoring that currents are filtered or that the integration time of fluorescence data points is finite) of real experimental data.

## Results and discussion

### Simulation of ligand-gated ion-channel data

Here we treat an exemplary ligand-gated channel with two ligand binding steps and one open-closed isomerization described by an HMM (see Figure 1a). For this model, confocal patch-clamp fluorometry (cPCF) data were simulated: time courses of ligand binding and channel current upon concentration jumps were generated (see Appendix 5 and Materials and methods section). Idealized example data with added white noise are shown in Figure 1b–d. We added realistic instrumental noise to the simulated data (see Appendix 5). A qualitative description of the statistical problem that needs to be addressed when modeling time series data such as the simulated is outlined in Box. 1.

![Figure 1.](https://cdn.elifesciences.org/articles/62714/elife-62714-fig1-v2.jpg)

**Figure 1.:** (a) The Markov state model (kinetic scheme) consists of two binding steps and one opening step. The rate matrix $K$ is parametrized by the absolute rates $k_{i⁢j}$, the ratios $K_{i⁢j}$ between on and off rates (i.e. equilibrium constants) and $L$, the ligand concentration in the solution. The units of the rates are $s^{-1}$ and $\mu⁢M^{-1}⁢s^{-1}$, respectively. The liganded states are C2, C3, O4. The open state O4 conducts a mean single-channel current $i=1$. Note, that absolute magnitude of the single channel current is irrelevant regarding this study what matters is its relative magnitude compared with $\sigma_{op}$ and $\sigma_{ex}$. Simulations were performed with 10 kHz or 100 kHz (for Figures 11 and 12) sampling, KF analysis frequency fana for cPCF data is in the range of (200-500) Hz while pure current data is analyzed at 2-5 kHz. (b-c) Normalized time traces of simulated relaxation experiments of ligand concentration jumps with $N_{ch}=10^{3}$ channels, $\lambda_{b}=0.375$ mean photons per bound ligand per frame and single-channel current $i=1$, open-channel noise with $\sigma_{op}^{2}=0.1⁢i^{2}$ and an instrumental noise with the variance $\sigma_{m}^{2}=i^{2}$. The current ycurr and fluorescence yflu time courses are calculated from the same simulation. For visualization, the signals are normalized by the respective median estimates of the KF. The black lines are the theoretical open probabilities $P_{o}⁢(t)$ and the average binding per channel $B⁢(t)$ for $N_{ch}→∞$ of the used model. Typically, we used 10 ligand concentrations which are (0.0625, 0.125, 0.25, 0.5, 1, 2,4, 8, 16, 64) $\mu⁢M$. d, Equilibrium binding and open probability as function of the ligand concentration $L$.

### Kalman filter derived from a Bayesian filter

Here and in the Materials and methods section, we derive the mathematical tools to account correctly for the stochastic Markov dynamics of single molecules in the fluctuations of macroscopic signals. The KF is a Bayesian filter (see Materials and methods), that is a continuous state HMM with a multivariate normal transition probability Ghahramani, 1997 (Figure 2a). We define the hidden ensemble state vector

$$
n(t):=(n_{1}(t),n_{2}(t),n_{3}(t),n_{4}(t))^{⊤}=\sumi=1N_{ch}s_{i}(t),
$$

which counts the number of channels in each state $s$ (see Methods). To make use of the KF, we assume the following general form of the dynamic model: The evolution of $n(t)$ is determined by a linear model that is parametrized by the state evolution matrix $T$

$$
n_{t+1}=Tn_{t}+\omega_{t}∼N(⋅|Tn_{t},Q_{t}),
$$

where ∼ means sampled from and $N(⋅|\mu,Σ)$ is a shorthand for the multivariate normal distribution, with the mean μ and the variance-covariance matrix $Σ$. The state evolution matrix (transition matrix) is related to the rate matrix $K$ by the matrix exponential $T=exp⁡(KΔt)$. The mean of the hidden state evolves according to the equation $E[n_{t+1}|n_{t}]=Tn_{t}$. It is perturbed by normally distributed white process noise $\omega$ with the following properties: The mean value of the noise fulfills $E[\omega_{t}]=0$ and the variance-covariance matrix of the noise is $cov⁡[\omega_{t},\omega_{t}]=Q(T,n_{t})$ (see Materials and methods Equation 38d, Ball, 2016). In short, Equation 3 defines a Gaussian Markov process.

![Figure 2.](https://cdn.elifesciences.org/articles/62714/elife-62714-fig2-v2.jpg)

**Figure 2.:** The filter can be seen as continuous state analog of the forward algorithm. (a) Graphical model of the conditional dependencies of the stochastic process. Horizontal black arrows represent the conditional multivariate normal transition probability $N(n_{t+1}|Tn_{t},Q_{t})$ of a continuous state Markov process. Notably, it is $n(t)$ which is treated as the Markov state by the KF. The transition matrix $T$ and the time-dependent covariance $Q_{t}=Q(T,n_{t})$ characterise the single-channel dynamics. The vertical black arrows represent the conditional observation distribution $O(y_{t}|n_{t})$. The observation distribution summarizes the noise of the experiment, which in the KF is assumed to be multivariate normal. Given a set of model parameters and a data point $y_{t}$, the Bayesian theorem allows to calculate in the correction step $P(n_{t}|y_{t})$ (red arrow). The posterior is propagated linearly in time by the model, predicting a state distribution $P(n_{t+1})$ (orange arrow). The propagated posterior predicts together with the observation distribution the mean and covariance of the next observation. Thus, it creates a multivariate normal likelihood for each data point in the observation space. (b) Observation space trajectories of the predictions and data of the binding per channel vs. open probability for different ligand concentrations. The curves are normalized by the median estimates of $\lambda_{b}$, $i$ and $N_{ch}$ and the ratio of open-channels $\frac{y_{curr}}{N_{ch}i}$ which approximates the open probability $P_{o}(t)$. The black crosses represent the predicted mean signal $HE⁡[n_{t+1}]$, which is calculated by multiplying the observational matrix $H$ with the mean predicted state $E⁡[n_{t+1}]$. For clarity, we used the mean value of the posterior of the KF. The green and blue trajectories represent the part of the time traces with after the jump to non-zero ligand concentration and after jumping backt to zero ligand concentration in the bulk, respectively.

The observations $y_{t}$ depend linearly on the hidden state $n_{t}$. The linear map is determined by an observation matrix $H$.

$$
y_{t}=Hn_{t}+ν_{t}∼O(⋅|Hn_{t}):=N(⋅|Hn_{t},Σ_{t})
$$

The noise of the measurement setup (Appendix 5 and Equation 43) is modeled as a random perturbation of the mean observation vector. The noise fulfills $E[ν]=0$ and $cov⁡[ν_{t},ν_{t}]=Σ_{t}$. Equation 4 defines the state-conditioned observation distribution $O$ (Figure 2a). If the system strictly obeys Equation 3 and Equation 4 then the KF is optimal in the sense that it is the minimum variance filter of that system Anderson and Moore, 2012. If the distributions of ν and ω are not normal, the KF is still the minimum variance filter in the class of all linear filters but there might be better non-linear filters. In case of colored noise ν and ω the filtering equations (see Materials and methods) can be reformulated by state augmentation or measurement-time-difference approach techniques Chang, 2014. For each element in a sequence of hidden states ${n_{t}:0<t<T}$ and for a fixed set of parameters $\theta$, an algorithm based on a Bayesian filter (Figure 2a), explicitly exploits the conditional dependencies of the assumed Markov process. A Bayesian filter recursively predicts prior distributions for the next $n_{t}$

$$
P(n_{t})=\intP(n_{t}|n_{t−1})P(n_{t−1}|y_{t−1})dn_{t−1},
$$

given what is known about $n_{t−1}$ due to $y_{t−1}$. The KF as a special Bayesian filter assumes that the transition probability is multivariate normal according to Equation 3

$$
P(n_{t})=\intN(n_{t}|Tn_{t−1},Q_{t−1})P(n_{t−1}|y_{t−1})dn_{t−1}
$$

Note, that Equation 6 is a central approximation of the KF. While the exact transition distribution of an ensemble of ion channels is the generalized-multinomial distribution (Methods Equation 32), the quality of normal approximations to multinomial Milescu et al., 2005 or generalized-multinomial Moffatt, 2007 distributions depends on the number of ion channels $N_{ch}$ in the patch and on the position of the probability vector in the simplex space. The difference between the log-likelihoods of the true generalized-multinomial dynamics and Equation 6 type approximation scales as $1/N_{ch}$ Moffatt, 2007. As a rule of thumb one should be careful with both algorithms for time traces with $N_{ch}\in[10^{1},10^{2}]$. Below or even inside this interval there are more qualified concepts such as the forward algorithm or even particle filters (Golightly and Wilkinson, 2011; Gillespie and Golightly, 2012) which avoid the normal approximation.

Each prediction of $n_{t}$ (Equation 6) is followed by a correction step,

$$
P(n_{t}|y_{t})=\frac{O(y_{t}|n_{t})P(n_{t})}{\intO(y_{t}|n_{t})P(n_{t})dn_{t}},
$$

that allows to incorporate the current data point into the estimate, based on the Bayesian theorem (Chen, 2003). Additionally, the KF assumes (Anderson and Moore, 2012; Moffatt, 2007) a multivariate normal observation distribution

$$
P(n_{t}|y_{t})=\frac{N(y_{t}|Hn_{t},Σ_{t})P(n_{t})}{\intN(y_{t}|Hn_{t},Σ_{t})P(n_{t})dn_{t}},
$$

If the initial prior distribution is multivariate normal then due to the mathematical properties of the normal distributions the prior and posterior $ℙ⁢(⋅)$ in Equation 8 become multivariate normal Chen, 2003 for each time step. In this case, one can derive algebraic equations for the prediction (Materials and methods Equation 37, Equation 38d) and correction (Materials and methods Equation 58 and Equation 58) of the mean and covariance. The algebraic equations originate from the fact that a normal prior is the conjugated prior for the mean value of a normal likelihood. Due to the recursiveness of its equations, the KF has a time complexity that is linear in the number of data points, allowing a fast algorithm. The denominator of Equation 8 is the normal distributed marginal likelihood $L(y_{t}|Y_{t−1},\theta)$ for each data point, which constructs by

$$
L(Y_{T}|\theta)=\prodt=2N_{T}L(y_{t}|Y_{t−1},\theta)=\prodt=2N_{T}\intO(y_{t}|n_{t})P(n_{t}|Y_{t−1},\theta)dn_{t}=\prodt=2N_{T}N(y_{t}|HE[n_{t}],HP_{t}H^{⊤}+Σ_{t}),
$$

a product marginal likelihood of normal distributions of the whole time trace $Y_{T}={y_{1},…,y_{N_{T}}}$ of length $N_{T}$ for the KF. For the derivation of $P_{t}$ and $Σ_{t}$ see Materials and methods (Equation 38d) and Equation 43. $P_{t}$ is the covariance of the prior distribution over $n(t)$ before the KF took $y(t)$ into account. The likelihood for the data allows to ascribe a probability to the parameters $\theta$, given the observed data (Methods Equation 20). An illustration for the operation of the KF on the observation space is given in Figure 2b. The predicted mean signal $HE[n(t)]$ corresponds to binding degree $B(t)=\frac{HE[n(t)]_{1}}{N_{ch}}$ and open probability $P_{O}(t)=\frac{HE[n(t)]_{2}}{N_{ch}}$. These values are plotted as vector trajectories.

The standard KF (Moffatt, 2007; Anderson and Moore, 2012; Chen, 2003) has additive constant noise $Σ_{t}=const$ in the observation model. Thus, in this case a constant variance term $Σ$ is added, in Equation 9 to the aleatory variance $HP_{t}H^{⊤}$ which, as mentioned above, originates (Equation 38d) from the the fact that we do not know the true system state $n(t)$. For signals with Poisson-distributed photon counting or open-channel noise, we need to generalize the noise model to account for additional white-noise fluctuations with $n(t)$-dependent variance. For instance, in single-channel currents additional noise is often observed whose variance is referred to by $\sigma_{op}^{2}$. In macroscopic currents this additional noise can be modeled by a term $\sigma_{op}^{2}n_{4}(t)$, causing state-dependency of our noise model.

$$
y(t)=Hn(t)+ν_{m}(t)+ν_{op}(t)⇔y∼O(y|n)=N(y|Hn(t),\sigma_{m}^{2}+n_{4}(t)\sigma_{op}^{2})=N(y|Hn(t),Σ_{t})
$$

The second noise term $ν_{op}$ is defined in terms of the first two moments $E(ν_{op})=0$ and $var(ν_{op})=E(ν_{op}^{2})=\sigma_{op}^{2}n_{4}(t)$. To the best of our knowledge such a state-dependent noise makes the integration of the denominator of Equation 8 (which is also the incremental likelihood) intractable

$$
P(y(t))=\intN(y|Hn,\sigma_{m}^{2}+n_{4}\sigma_{op}^{2})N(n|n¯(t),P(t))dn
$$



$$
=\frac{1}{const}\intexp⁡(\frac{(y−Hn)^{2}}{2(\sigma_{m}^{2}+n_{4}\sigma_{op}^{2})})exp⁡(\frac{1}{2}(n−n¯(t))P^{−1}(n−n¯(t))^{⊤})dn
$$

This is because the state distribution $N(n|n¯(t),P(t))$ as the prior also influences the variance parameter of the likelihood which means that the conjugacy property is lost. While a normal distribution is the conjugated prior of the mean of a normal likelihood, it is not the conjugated prior for the variance. However, by applying the theorem of total variance decomposition Equation 46a we deduce a normal approximation to Equation 8 and to the related problem of Poisson-distributed noise in fluorescence Equation 57, Equation 55a data. By computing the mean and the variance or covariance matrix of the signal, we can reformulate the noise model to fit the form of the traditional KF framework. Note, that the derived equations for the covariance matrix are still exact for the more general noise model. Mean and covariance just do not form a set of sufficient statistics anymore.

Our derivation is not limited to ligand-gated ion channels. For example, when investigating voltage-gated channels, the corresponding noise model can be easily adapted. This holds also when using the P/n protocol for which the noise model resembles that of the additional variance in the fluorescence signal. The additional variance is induced because the mean signal from the ligands swimming in the bulk (Materials amd methods Equation 43 Appendix 5) is eliminated by subtracting scaled mean reference signal which itself has an error. This manipulation adds additional variance to the resulting signal comparable to P/n protocol. Other experimental challenges, as for example series resistance compensation promoting oscillatory behavior of the amplifier, deserve certainly advanced treatment. Nevertheless, for voltage-clamp experiments with a rate equation approach it also becomes clear (Lei et al., 2020) that modeling of the actual experimental limitations, including series resistance, membrane and pipette capacitance, voltage offsets, imperfect compensations by the amplifier, and leak currents are necessary for consistent kinetic scheme inference.

The Bayesian posterior distribution

$$
P(\theta|Y_{T})=\frac{L(Y_{T}|\theta)P(\theta)}{\intL(Y_{T}|\theta)P(\theta)d\theta}
$$

encodes all information from model assumptions and experimental data used during model training (see Materials and methods). A full Bayesian inference is usually not an optimization (finding the global maximum or mode of the posterior or likelihood) but calculates all sorts of quantities derived from the posterior distribution such as mean values of any function $f$ including the mean value or covariance matrix of the parameters themselves or even the likelihood of the data.

$$
E[f]=\intf(\theta)P(\theta|Y_{T})d\theta
$$

Besides the covariance matrix of the parameter to express parameter uncertainty, the posterior allows to calculate a credibility volume. The smallest volume $V_{P}$ that encloses a probability mass $P$ of

$$
P=\int_{V_{P}}P(\theta|Y_{T})d\theta.
$$

is called the Highest Density Credibility Volume/Interval (HDCV/HDCI). Those credibility volumes should not be confused with confidence volumes although under certain conditions they can become equivalent. Given that our model sufficiently captures the true process, the true values $\theta_{true}$ will be inside that volume with a probability $P$. Unfortunately, typically there is no analytical solution to Equation 12 . However, it can be solved numerically with Monte Carlo techniques, enabling to calculate all quantities related to Equation 13 and Equation 14 . Our algorithm uses automatic differentiation of the statistical model to sample from the posterior (Appendix 1—figure 1a) via Hamiltonian Monte Carlo (HMC) (Betancourt, 2017), see Appendix 7 , as provided by the Stan software (Hoffman and Gelman, 2014; Gelman et al., 2015).

### Benchmark for PC data against the gold standard algorithms

We compare the posterior distribution (Figure 3) of our algorithm against Bayesian versions of the deterministic (Milescu et al., 2005) and stochastic (Moffatt, 2007) algorithms, which we consider as the gold standard algorithms for macroscopic patch-clamp data. Simulated currents of a patch with $N_{ch}=5⋅10^{3}$ are shown in (Figure 3d). The resulting posteriors (Figure 3a) show that both former algorithms are further away from the true parameter values with their maxima or mean values (Figure 3a). E.g., the relative error of the maximum of the posterior are $Δk_{21}≈200%$ for Milescu et al., 2005 and $Δk_{32}≈240%$ for Moffatt, 2007 . The four other parameters including the three equilibrium constants behave less problematic as judged by their relative error. Additionally, if one does not only judge the performance by the relative distance of maximum (or some other significant point) of the posterior but considers the spread of the posterior as well, it becomes apparent, that the marginal posterior of both former algorithms fail to cover the true values within at least the reasonable parts of their tails. Accordingly, for maximum likelihood inferences the true value would be far outside the estimated confidence interval. For the RE approach only the marginal posterior of $K~_{21}$ is nicely centered over the true values and the marginal of $K~_{32}$ could be considered to cover within a reasonable part of the distribution the true value. Uncertainty quantification is investigated in more detail further down (Figures 4—9). Note that in Figure 3a, parameter unidentifiability by heavy tails/ multiple maxima of the posterior distribution or (anti-) correlation is easily visible as non axial symmetric patterns.

![Figure 3.](https://cdn.elifesciences.org/articles/62714/elife-62714-fig3-v2.jpg)

**Figure 3.:** Overall it shows the highest accuracy and the posterior covers the true values. The classical deterministic RE (blue), 2007 Kalman filter (red) and our Bayesian filter (green) are implemented as a full Bayesian version and the obtained posterior distributions are compared. For all PC data sets in the figure the analysing frequencies $f_{ana}$ ranges within 2-5. (a) Posterior of the parameters for the 3 algorithms for the data set displayed in panel d. The blue crosses indicate the true values. All samples are normalized by their true values which is indicated by the ∼ above the parameters. For clarity, we only show a fraction of the samples of the posterior for blue and red. b, Effect of open channel noise: The Euclidean error for all three approaches is plotted vs. $\sigma_{op}/i$ (low axis).The upper axis displays the ratio of the ‘typical’ standard deviation of the open channel excess noise of the ensemble of channels $\sigma_{op}\sqrt{N0.5P_{o,max}}$ to the standard deviation of instrumental noise. c, Influence of patch size: Scaling of the Euclidean error vs. $N_{ch}$ follows $∼(N_{ch})^{−0.5}$ indicated by the dashed lines for $N_{ch}>2⋅10^{3}$ for the RE and the Bayesian filter approach. The data indicates a constant error ratio (orange) for large $N_{ch}$. For $N_{ch}<2⋅10^{3}$ samples of the posteriors for many data sets suggest an improper posterior. An instrumental noise of $\sigma_{ex}/i=1$ and $\sigma_{op}/i=0.01$ was used. (d) The time traces on which the posteriors of panel a are based (for the ligand concentrations see Figure 1). Panel b used the same data too, but σ and $\sigma_{op}$ were varied.

![Figure 4.](https://cdn.elifesciences.org/articles/62714/elife-62714-fig4-v2.jpg)

**Figure 4.:** However, only the Bayesian filter covers the true value in a reasonable HDCV while RE based posteriors are too narrow. All samples are normalized by their true values which is indicated by the ∼ above the parameters. (a) Euclidean errors of the maximum for the rate $k_{ij}$ and equilibrium constants $K_{ij}$ obtained by the KF (green) and from the REs (blue) are plotted against $N_{ch}$ for $\sigma_{ex}/i=0.5$, $\sigma_{op}/i=0.05$ and $\lambda_{b}=5$. Both algorithms scale like $1/\sqrt{N_{ch}}$ (dashed lines) for larger $N_{ch}$ which is the expected scaling For smaller $N_{ch}<500$ (gray range) the error is roughly the same indicating that limitations of the normal approximation to the multinomial distribution dominate the overall error in this regime. The combination of fluorescence and current data(cPCF) decreases the eucleadian error for both approaches compared to current data alone(PC). (b), HDCI and the mode of the 3 $k_{ij}$ and 3 $K_{ij}$ plotted vs. $N_{ch}$ revealing that the maximum is a consistent estimator (converges in distribution to the true value with increasing data quality). While the KF (green) 0.95-HDCI includes usually the true value, the RE HDCI (blue) is too narrow and, thus, the real values are frequently not included. (c) Bayesian estimation of true success probability for the event that all 6 0.95-HDCI include the respective true values at the same time by a binomial likelihood. Since the data sets have different $N_{ch}$ and the model approximations become better with increasing $N_{ch}$, we use a cut-off for $N_{ch}=200$. d, Comparison of 1-D and combinations of 2-D marginal posteriors of the parameters of interest for both algorithms calculated from a $N_{ch}=10^{3}$ simulation. Blue lines indicate the true value. We depict that in two dimensions the disproportion of the deviation of the mode and the spread of RE (blue) approach is worsened while KF (green) posterior includes the true values with more reasonable probability mass.

![Figure 5.](https://cdn.elifesciences.org/articles/62714/elife-62714-fig5-v2.jpg)

**Figure 5.:** (a) Cumulative χ-square distribution vs. the Mahalanobis distance $d_{Mah}$. The y axis denotes the probability mass which is counted by moving away from the maximum before an ellipsoid with distance $d_{Mah}$ is reached. The different colours represent the changes of the cdf with an increasing number of rate parameters. The blue cdf at $d_{Mah}=1$ represents how much probability mass can be found from $\int_{−\sigma}^{\sigma}normal⁡(\theta,0,\sigma)d\theta$, see inset. In one dimension, we can expect to find the true value within $2⁢\sigma$ around the mean with the usual probability of $P=0.682$ for univariate normally distributed random variables. The six parameters (brown) of the full rate matrix will almost certainly be beyond $d_{Mah}=1.0$. The higher the dimensions of the space the less important becomes the maximum of the probability density distribution for the typical set which is by definition the region where the probability mass resides. The mathematical reason for this is that the probability mass $P=\int_{V}ℙ⁢(\theta)⁢dV$ is the integrated product of volume and probability density. b, The two methods to count volume in units of probability mass for the KF (green) and the RE (blue). The gray area indicates which data sets are considered a success if one chooses to evaluate a proababilty mass of 0.4 of each posterior around its mode. All data sets in the white area are considered a failure. For the optimistic noise assumptions $\sigma_{ex}=0.5⋅i$, $\sigma_{op}=0.05⋅i$ and a mean photon count per bound ligand per frame $\lambda_{b}=5$ the RE approach (blue) distributes the probability mass such that the HDCV never includes the true rate matrix. From $N_{ch}>100$ both HDCV estimates of the KF posterior (green curves) include the true value within a reasonable volume and show a similar behaviour. c, Binomial success statistics of HDCV to cover the true value vs. the expected probability constructed from the data of (b). Calculated for $i=0.25⁢\sigma$ and $\sigma_{op}=0.025⁢i$ and $\lambda_{b}=5$ and minimal background noise.

![Figure 6.](https://cdn.elifesciences.org/articles/62714/elife-62714-fig6-v2.jpg)

**Figure 6.:** (a) Binomial success statistics of HDCV to cover the true value vs. the expected probability. Calculated for $i=\sigma$ and $\sigma_{op}=0.1⁢i$ and $\lambda_{b}=0.375$ and a strong background noise. (b) Binomial success statistics of HDCV to cover the true value vs. the expected probability. For $10⋅i=\sigma$ and $\sigma_{op}=1⁢i$ and $\lambda_{b}=0.375$ and a strong background noise. For both algorithms, the adaptation of the sampler of the posterior was more fragile for small $N_{ch}$, leading to differences in the posterior if the posterior is constructed from different independent sampling chains. Those data sets were then excluded. We assume that these instabilities are induced in both algorithms by the shortcomings of the multivariate normal assumptions. (c) Comparison of the Euclidean error vs. $N_{ch}$ for the pessimistic noise case (solid lines) with Euclidean error for the optimistic noise case (dotted lines).

![Figure 7.](https://cdn.elifesciences.org/articles/62714/elife-62714-fig7-v2.jpg)

**Figure 7.:** With PC data the RE approach is frequently incapable to identify all parameters while the Bayesian filter is more robust. cPCF data alleviate the parameter unidentifiabilities for patch sizes for which PC data are insufficient. Each panel column corresponds to a particular true process with increasing complexity from left to right, as indicated by the model schemes on top. Within all kinetic schemes, each transition to the right adds one bound ligand. Each transition to left is an unbinding step. Vertical transitions are either conformational or opening transitions. Plots in each row share the same y-axis respectively. Each column shares the same abscissa. (a-c) Error ratio for PC data (blue) and cPCF data (red). The dashed lines indicate the mean error ratio under the simplifying assumption that the error ratio does not depend on $N_{ch}.$ The vertical bars are the standard deviations of the mean values. Theses values were calculated from the Euclidean errors shown in Figures 3c and 4a for a, and panels (d-e), for (b-c), respectively. Results from the KF algorithm (green) and the RE algorithm (blue) are compared for PC (lighter shades) and cPCF (strong lines). The diagonal gray areas indicate a $∼(N_{ch})^{-0.5}$ proportionality. For simulating the underlying PC data, we used standard deviations of $\sigma_{op}=0.1$ and $\sigma=1$ and for the cPCF data additionally a ligand of brightness $\lambda_{b}=5$. To facilitate the inference for the two more complex models, we assumed that the experimental noise and the single channel current are well characterized, meaning $i∼N(i|1,0.01)$, $\sigma∼N(\sigma|1,0.01)$ and $\sigma_{op}∼gamma⁡(\sigma_{op}|1,100)$. In the models containing loops (last 2 columns), a prior was used to enforce microscopic-reversibility and set to $k_{25}^{⋆}∼beta⁡(100,100)$ multiplied by $k_{1}=k_{5}⁢k_{6}⁢k_{7}⁢k_{8}⁢(k_{2}⁢k_{3}⁢k_{4})^{-1}⋅0.995+0.01⋅k_{1}^{⋆}$.

![Figure 8.](https://cdn.elifesciences.org/articles/62714/elife-62714-fig8-v2.jpg)

**Figure 8.:** Comparison of a series of HDCIs shown as functions of $N_{ch}$ for each parameter of the rate matrix obtained by the KF (green) and the RE algorithm (blue). The differing shades of green and blue indicate the set of $(0.95,0.6,0.2,0.1)$-HDCIs. Only the interval $N_{ch}>2⋅10^{3}$ in which all parameters are identified is displayed. The data are taken from the KF vs. RE benchmark of Figures 3c and 7a . The first row corresponds to three rates $k_{i⁢j}$ the second row to the equilibrium constants $K_{i⁢j}$. All parameters are normalized by their true value. The insets show the error ratios of the respective single parameter estimates. Note that the error ratios on the single-parameter level can be even of the order of magnitude of 102. Thus, they can be much larger than the error ratios calculated from the Euclidean error if the errors of the respective parameters are small compared to other error terms in the Euclidean error Equation 15 .The lowest Euclidean error for this kinetic scheme has cPCF data analyzed with the KF. (Figure 7d). A 6-state-1-open-states model with cPCF data has again an error ratio of the the usual scale (Figure 7c). As expected, the Euclidean error continuously increases with model complexity (Figure 7d and e). For PC data of the 6-state-1-open-states model even the likelihood of the KF is that weak (Figure 7e) that it delivers unidentified parameters even for $N_{ch}=10^{4}$ and we can detect heavy tailed distributions up until $N_{ch}=10^{5}$. Using RE on PC data alone does not lead to parameter identification, thus no error ratio can be calculated.

![Figure 9.](https://cdn.elifesciences.org/articles/62714/elife-62714-fig9-v2.jpg)

**Figure 9.:** In contrast, the HDCE for RE approach frequently does not include the true value and in general appears biased and frequently leaves certain parameters unidentified. Comparison of a series of $(0.95,0.6,0.2,0.1)$-HDCIs as functions of $N_{ch}$ for each parameter of the rate matrix obtained by the KF (green) and the RE algorithm (blue). The HDCIs correspond to the PC data displayed in Figure 7b and d . The first row corresponds to three rates $k_{i⁢j}$ the second row to the equilibrium constants $K_{i⁢j}$. All parameters are normalized by their true value. $K~_{25}$ is because of the microscopic-reversibility prior a parameter which is strongly dependent on the other rates and ratios. Refer to the caption of Figure 7 for details about the prior that enforces microscopic-reversibility. Thus, the deviations of $K~_{25}$ are inherited from the other parameters. The rate $k~_{54}$ is frequently not identified by the RE approach and only the limits of the sampling box confines he posterior.

To assess the location of the posterior conditioned on $N_{ch}$, we select the median vector $\theta$ of the marginal posteriors and calculate its Euclidean distance to the true values by:

$$
Euclidean Error=\sqrt{\sumi[\theta_{i}/\theta_{i,true}-1]^{2}}
$$

This defines a single value to judge the overall accuracy of the posterior. Varying $\sigma_{op}/i$ reveals the range of the validity (Figure 3b) of the algorithm (red) from Moffatt, 2007 . While both stochastic approaches are nearly equivalent for low open-channel noise, the RE (blue) performs consistently poorer. It may seem surprising that even for In fact, the KF method beha the two stochastic algorithms start to produce different results. But considering the scaling (Materials and methods Equation 46a) of the total open-channel noise (top axis) from currents of an ensemble patch $∝(N_{ch}⁢P_{open,max}⁢0.5)^{0.5}⁢\sigma_{open}$ one sees that if $∝(N_{ch}⁢P_{open,max}⁢0.5)^{0.5}⁢\sigma_{open}$ approaches σ the traditional KF suffers from ignoring state dependent noise contributions. The lower scale changes with experiments (e.g. $N_{ch}$ and $\sigma_{o⁢p}$). In contrast, the upper scale is largely independent of the particular measurements. The two different normalizations indicate an experimental intuition: “ Why should I consider the extra noise from the open state of the single channel if only $\sigma_{op}/i=\sigma_{op}/\sigma≈0.01$” is misleading. The small advantage of our algorithm for small $\sigma_{op}/i$ over Moffatt, 2007 is due to the fact that we could apply an informative prior in the formulation of the inference problem on $\sigma_{exp}∼normal⁡(\sigma_{exp,true}^{2},\sigma_{exp,true}^{2}⋅0.01)$ by taking advantage of our generalization (Equation 46a) Bayesian filter. Further, Figure 3b indicates the importance that the functional form of the likelihood is flexible enough to capture the second order statistics of the noise of the data sufficiently.

For an increasing data quality, which in our benchmark is an increasing $N_{ch}$ per trace, we show (Figure 3c) that the deterministic RE and our Bayesian filter are consistent estimators, that is they converge in distribution to the true parameter values with their posterior maxima or median for increasing data quality. The scaling of the RE approach (blue) and our Bayesian filter (green) vs. $N_{ch}$ shows that for large $N_{ch}$ both algorithms seem to have a constant error ratio relative to each other. They are both well described by $error⁡(N_{ch})∝a/\sqrt{N_{ch}}$ with an error ratio computed from the fit of 4.4. Thus, although our statistical model is singular (meaning that the fisher information matrix is singular Watanabe, 2007), its asymptotic learning behaviour is similar to a regular model (Figure 4c) which, however, means that the euclidean error from both algorithms stays different also for large $N_{ch}$. For data with $N_{ch}<2⋅10^{3}$ the samples from the posterior typically indicate that the posterior is improper which is defined as

$$
\intℙ⁢(\theta|y)⁢d\theta=∞
$$

We consider this as the case of unidentified parameters. This data-driven definition is in so far different from structural and practical identifiability definitions (Middendorf and Aldrich, 2017a; Middendorf and Aldrich, 2017b) as the two latter cases are not distinguished. Still the practical consequence of structural or practical unidentifiability, which is usually an improper posterior, is captured. Cases of structural or practical unidentifiability which lead to a confined region of constant posterior density will be considered identified as the posterior is still normalizable thus the uncertainty quantification will still be correct, even when this finding is not sufficient to answer the research question at hand.

### Benchmarking for cPCF data against the gold standard algorithm

For the simulated time traces with an optimistically high signal-to-noise assumption, the posterior of the KF (from hereon KF denotes our Bayesian Filter) and a RE (Milescu et al., 2005) approach are compared for cPCF data (Figure 4a–d). For a brief introduction of the RE approach, see Appendix 8 . The failure to analyze PC data with moderate open-channel noise (Moffatt, 2007; Figure 3a) disqualifies the classical KF with its constant noise variance also as a useful algorithm for fluorescence data, because here the Poisson distribution of the signal generates an even stronger state dependency of the signal variance.

By “high signal-to-noise assumption” , we refer to an experimental situation with a standard deviation of the current recordings $\sigma_{ex}/i=0.5$, a low additional $\sigma_{op}/i=0.05$, and a high mean photon rate per bound ligand and frame $\lambda_{b}=5$. Additionally, we assume vanishing fluorescence background noise generated by the ligands in the bulk. The benefit of the high signal-to-noise is that the limitations of the two different approximations to the stochastic process of binding and gating can be investigated without running into the risk of being compensated or obscured by the noise from the experimental setup. For these experimental settings (Figure 4a), we calculate the Euclidean distance of the median (Equation 15) for different $N_{ch}$. For $N_{ch}<500$ (gray shaded area in Figure 4a), the Euclidean error of both algorithms is roughly the same. On the single parameter level (Figure 4b), this can be seen as an onset of correlated deviations from the true value for both algorithms. Each marginal posterior has for each $N_{ch}$ a similar deviation in magnitude and direction. That is in particular true for $k~_{32}$ and $K~_{32}$ which dominate Equation 15 . In spite of the correlation in direction of the errors of $k~_{21}$ and $K~_{21}$ their magnitude is still smaller for the KF. In summary, this indicates that in this regime the approximations to the involved multinomial distributions fail in a similar manner for both algorithms. That implies that treating the autocorrelation of the gating and binding becomes similar important compared to the error induced by normal approximations (which are used by the KF and the RE approach). For larger $N_{ch}$, the Euclidean error of the RE is on average 1.6 times larger than the corresponding error of the posterior mode of the KF, which we deduce by fitting the function $error⁡(N_{ch})=\frac{a}{\sqrt{N_{ch}}}$. On the one hand, both algorithms are better in approaching the true values than with patch-clamp data alone. On the other hand, the smaller error ratio means, that adding a second observable constrains the posterior, such that much of the overfitting is prevented for the RE approach. By overfitting, we define the adaptation of any inference algorithm to the specific details of the used data set due to experimental and intrinsic noise which is aggravated if too complex kinetic schemes are used. Similarly, (Milescu et al., 2005) showed that the over fitting tendency of the RE can be reduced if the autocorrelation of the data is eliminated. The dotted green curve derives from PC data. The Euclidean error is roughly an order of magnitude larger for $N_{ch}>2000$. Thus, in this regime the cPCF data set is equivalent to 102 fold more time traces or 102 more $N_{ch}$ in a similar PC data set. For $N_{ch}<2000$ only cPCF establishes parameter identifiability (given a data set of 10 ligand concentrations and no other prior information). In Figure 4b(1-6), we demonstrate the 0.95-HDCI (Equation 14) of all parameters and their modes vs. $N_{ch}$. Even though the Bayesian filter and the RE approach are both consistent estimators, the RE approach covers the true values with its 0.95-HDCI only occasionally. The modeling assumption of the RE approach of treating each data point as if it does not come from a Markov process but from an individual draw from a multinomial distribution with deterministically evolving mean and variance makes the parameter estimates overly confident (Figure 4b(1-6)) . A likely explanation can be found by analyzing the extreme case where data points are sampled at high frequency relative to the time scales of the channel dynamics. The RE approach treats each data point as a new draw from Equation 67 while in reality the ion channel ensemble had no time to evolve into a new state. In contrast, the KF updates its information about the ensemble state after incorporating the current data point and then predicts from this updated information the generalised multinomial distribution of the next data point. For $N_{ch}>200$, the marginal posterior of the KF usually contains the true value. Nevertheless, one might depict a bias in both algorithms, in particular (Figure 4b 2,4) for $k~_{32}$ and $K~_{32}$ for $N_{ch}<2⋅10^{3}$, similar to the findings of Moffatt, 2007 . A proper investigation of bias can be found in Figure 11 and 12 and in the Appendix. Notably, with the more realistic higher experimental noise level, in those tests the bias is hardly or not all detectable (consider the unfiltered or infinitely fast integrated data). A plausible explanation is that the bias only occurs (Figure 4 2,4) because the data are that perfect that the discrete nature of the ensemble dynamics is almost visually detectable, thus deviating from to the modeling assumption of multi-variate normal distributions.

To investigate the six one-dimensional 0.95-HDCIs simultaneously, we declare the analysis of a data set as successful if all 0.95-HDCIs include the true values. Otherwise we define it as a failure. This enables to determine the true probability at which the probability mass of the KF and the RE approach covers the true values in a binomial setting. The left blue vertical line in Figure 4c indicates $p=0.95^{6}≈0.735$ which is the lower limit and which would be the true success probability for an ideal model whose six 0.95-HDCIs are drawn from $y∼binomial⁡(0.95,6)$. This is the probability of getting 6 successes in 6 trials. The right blue vertical line equals $p=0.95$, signifying the upper limit obtained by treating the six $0.95-$ HDCIs as being drawn from $y∼binomial⁡(0.95,1)$ each, which is a rather loose approximation. All marginal distributions are computed from the same high-dimensional posterior which is formed by one data set for each trial. Thus, the six $0.95-$ HDCIs $y∼binomial⁡(0.95,1)$ must have success rates between those two extremes if the algorithm creates an accurate posterior. We next combine the binomial likelihood with the conjugated beta prior (Hines et al., 2014) for mathematical convenience. On this occasion, for the sake of the argument, $beta⁡(1,1)$ seems sufficient. A $beta⁡(1,1)$ prior is a uniform prior on the open interval $(0,1)$. The estimated true success rate of the RE approach (blue) is $≈0.15$ and therefore far away from the success probability an algorithm should have when it is based on an exact likelihood of the data. In contrast, the posterior (green) of the true success probability of the KF resides with a large probability mass between the lower and upper limit of the success probability of an optimal algorithm (given the correct kinetic scheme). As both algorithms use the same prior distribution, the different performance is not induced by the prior.

Exploiting six one-dimensional posterior distributions does not necessarily answer whether the posterior is accurate in 6 dimensions but we can refine the used binomial setting. In Figure 4d $ℙ⁢(k~_{32},K~_{43})$, we see that 2-D marginal distributions can, due to their additional degree of freedom, twist around the true value without covering it with HDCV (Equation 14) of reasonable size while simultaneously the two 1–D marginal distribution do cover it with a reasonable HDCI. In general, the KF posterior distribution has its mode much closer to the true value for various parameter combinations and it seems that the posterior is approximately multivariate normal. Further, we recognize that the probability mass of the reasonably sized HDCV of the KF posterior includes the true values whereas the HDCV from the RE does not. In 6 dimensions we lack visual representations of the posterior. Since we showed that both algorithms are consistent for a given identifiable model, we are looking for a way to ask whether the posterior is accurate (has the posterior distribution the right shape). We can answer that question by asking, how much probability mass around the mode (or around multiple modes) needs to be counted to construct a HDCV Equation 14 which includes the true values. Then we can ask for $N_{set}$ data sets how often did we find the true values inside a volume $V⁢(P)$ of a specific probability mass $P$ of the posterior distribution

$$
success∼binomial⁡(N_{set},P⁢(V))⁢.
$$

An algorithm which estimates the parameters of the true process should fulfill this property simultaneously to being consistent. Otherwise credibility volumes or confidence volumes are meaningless. Noteworthy, that this is a empirical test of how sufficient the Bayesian filter and the RE approach hold frequentist coverage property of their HDCVs (Rubin and Schenker, 1986). We explain (Appendix 8) in detail how to quantify the overall shape and $n$-dimensional posterior and comment on its geometrical meaning. One way is to use an analytical approximation via the cumulative Chi-squared distribution (Figure 5a and b), The other way is to count the probability mass of $n$-dimensional histogram bins starting with the highest value until the first bin includes the true values (Figure 5b).

Knowing how much volume/probability mass is needed to include the true rate matrix allows us to test whether all HDCVs constructed from the two probability distributions match the binomial distributions of the ideal model. For each data set and for each HDCV of a fixed probability mass, there are two possible outcomes: The true rate matrix is inside or outside of that volume. For a chosen HDCV with a fixed probability volume, as indicated by a gray space in Figure 5b , we count how many times the true matrix is included in the volume of that probability mass for each trail in a fixed amount of trials. Since the success is binomially distributed, we plot the expected mean of a perfect model $E⁢[y]=N_{trials}⁢P_{true}$ and binomial quantiles and compare them with the success rate found in our test runs (Figure 5c) for both algorithms with both methods to determine the posterior shape. The posterior of the KF distributes the probability mass in a consistent manner such that each volume includes the true rate matrix within the quantile range. In contrast, the RE approach fails for all data sets for all HDCVs (from 0 – 0.95 probability mass) and does not include the true values in one single case. Note, that all the binomial trials for each HDCV are made from the same set of data sets which explains the correlated deviation from the mean. For lower but realistic signal to noise ratios, where the fit quality decreases, for example by producing larger errors/wider posterior distributions (Figure 6a), the statistics of the HDCV from the RE approach improve but are still outperformed by the KF. In particular, in our tested case of realistic experimental noise we never find the true values within a 0.65-HDCV if the data are analyzed with a RE approach. Even for the highest noise level (Figure 6b), the probability mass of the KF posterior needed to include the true rate matrix remains almost always smaller then the posterior mass of the RE approach. That means that the posterior mass of the KF is much closer to the true value distributed than the posterior mass of the RE. With the KF we find the true rate matrix for one data set in small volume $P<0.05$ around the mode. To achieve the same with the RE approach we need at least a probability mass of 0.3.

In the inset of Figure 6a and b we do not observe a trend, thus no indication that the RE approach has a better performance for large values $N_{ch}$ in this regard. This challenges the common argument that the RE approach should be equivalent to the KF for large $N_{ch}$ because the ratio of mean signal vs. the intrinsic binding and gating noise is so large. Thus, including the autocorrelation into the analysis is important even for unrealistic large $N_{ch}$. One possible explanation is model a signal-to-noise ratio which scales $∝N_{ch}$. From the multinomial distribution both algorithms inherit mean signals which scale $∝N_{ch}$ and variances which scale in the terms dominating for large $N_{ch}$ similarly with $∝N_{ch}$. Thus, identical to the real signal, both algorithms model the scaling of the signal-to-noise ratio $∝\sqrt{N}$. It is plausible, that both algorithms remain sensitive for the occurrence of autocorrelation of the noise even for largest signal-to-noise ratios. In Figure 5c we compare the Euclidean error of the pessimistic high white noise case with an over-optimistic low noise case. We see, that when increasing $N_{ch}$ there is a regime where the Euclidean error increases faster than $\sqrt{N_{ch}}^{-1}$ which we indicate with a coarse approximate fit $∝N_{ch}^{-1}$. In that regime two effects happen simultaneously. First, the mean and the intrinsic fluctuations of the signal become more and more dominant over the experimental noise. Second, the standard deviation of intrinsic fluctuations becomes smaller relative to the mean signal. We speculate, that this produces together a learning rate which is faster than the usual asymptotic learning rate $\sqrt{N_{ch}}^{-1}$ of a regular model but relaxes asymptotically towards $\sqrt{N_{ch}}^{-1}$.

### Statistical properties of both algorithms for more complex models

We have seen in Figure 3c and Figure 4a that the RE and the KF algorithm are consistent estimators, while their error ratio (Figure 7a) seems to have no trend to approach 1 with increasing $N_{ch}$. Adding a second observable increases parameter accuracy and adds identifiability for both algorithms since less aspects of the dynamics need to be statistically inferred (Figure 4a). Furthermore, the second observable takes away much of the tendency (compare Figure 4b 1 – 6 with 8) of the RE approach to overinterpret (overfit) which leads to a shrinking of the error ratio $5.6\pm1.4$ for PC data to smaller values for cPCF data (Figure 7a) (red) which are on average still bigger than one, while the Euclidean error is reduced (Figure 4a). If we then keep the amount and quality of the PC/cPCF data but increase the complexity of the model which produced the data (Figure 7b and d) from a four-state to a five-state model (see kinetic schemes above Figure 7a–c), we see that for cPCF data the error ratio stays roughly the same (difference between Figure 7a and b). For PC data instead both algorithms deliver an unidentified k21 for $N_{ch}≦2⋅10^{3}$ (defined as an improper posterior). For larger $N_{ch}$ the KF always identifies all parameters while the RE fails at $N_{ch}\in{7000,2000,75000}$ to identify k54. Thus, the KF reduces the risk of unidentified parameters. To calculate the mean error ratio, we exclude the values were some of the parameters are unidentified in total that still amounts to $6.8\pm2.7$ thus the advantage of the KF (given all parameters are identified) might increase with model complexity for PC data. The lowest Euclidean error for this kinetic scheme has cPCF data analyzed with the KF. (Figure 7d). A 6-state-1-open-states model with cPCF data has again an error ratio of the the usual scale (Figure 7c). As expected, the Euclidean error continuously increases with model complexity (Figure 7d and e). For PC data of the 6-state-1-open-states model even the likelihood of the KF is that weak (Figure 7e) that it delivers unidentified parameters even for and we can detect heavy tailed distributions up until . Using RE on PC data alone does not lead to parameter identification, thus no error ratio can be calculated.

Consistent with our findings, fluorescence data itself, should lower the advantage of the KF compared to PC data simply by signal-to-noise arguments. The stochastic aspect of the ligand binding is usually more dominated by the noise of Photon counting and background noise than the stochastic gating is dominated in current data by experimental noise. In terms of uncertainty quantification the advantage of the KF with cPCF varies with the model complexity (see, Appendix 9).

Besides analyzing what causes the changes in the Euclidean error (Figure 7a and b) at the single parameter, we now investigate whether the posterior is a proper representation of uncertainty. Thus, we look back at the HDCIs. The HDCIs of the 4-state-1-open-state (Figure 8) of the PC data from Figure 3 reveal an exacerbated over-confidence problem of the RE approach (blue) compared to cPCF-data (Figures 4b1—6). This, underlines our conclusion of Figures 5 and 6 that the Bayesian posterior sampled by the RE approach is misshaped. As a consequence a confidence volume derived from the curvature at the ML estimate of the RE algorithm understates parameter uncertainty. A possible way for ML methods to derive correct uncertainty quantification is by using bootstrapping data methods (Joshi et al., 2006). Furthermore, the error ratios of each single parameter from its true value in the last column $k~_{43}$$K~_{43}$ strongly increased their magnitudes (insets Figure 8). Even error ratios of $5⋅10^{2}$ are possible. Note, that the way we defined Equation 15 suppresses the influence of the smaller parameter errors in the overall error ratio. Thus the advantage (error ratio) of the KF over RE approach for a single parameter can be much larger or lower compared to the error ratio derived from the Euclidean error if the respective parameter is contributing less to the Euclidean error. The posterior of the KF (green) seems to be unbiased after the transition into the regime $N_{ch}>2⋅10^{3}$ where all parameters are identified. Similarly, for the RE algorithm there is no obvious bias in the inference. If we use the RE algorithm and change from the four-state to the five-state model (PC data from Figure 7b), bias occurs (Figure 9) in many inferred parameters, even for the highest $N_{ch}$ investigated. Milescu et al., 2005 showed that one or the reason of the biased inference of the RE approach is its ignorance of autocorrelation of the intrinsic noise. We add here that the bias problem clearly aggravates with an increased model complexity. It is even present in unrealistically large patches which in principle could be generated by summing up 102 time traces with $N_{ch}=10^{3}$. In contrast, the KF algorithm reveals that its parameter inference is either unbiased or at least much less biased in the displayed $N_{ch}$ regime. Furthermore, for both algorithms the position of the HDCI relative to the true value is for some parameters highly correlated, which corresponds to the correlation between optima of the ML method of Milescu et al., 2005 ; Moffatt, 2007.

As a side note, unbiased parameter estimates are a highly desirable feature of an inference algorithm. For example, with a bias in the inference, repeated experiments do not lead to the true value if the arithmetic mean of the parameter inferences is taken. With bias even bootstrapping methods fail to produce reliable uncertainty quantification. Due to the variation of the data the k54 parameter is either identified in some neighbourhood of the true value or complete unidentified (Figure 9), if the RE algorithm is used. The unidentified k54 occurs even at high-quality data such as $N_{ch}=7.5⋅10^{4}$. Only because of the nonphysical prior (Figure 9) of k54 induced by the limits of the sampling box of the sampling algorithm the posterior appears to be proper but is in fact either unidentified or or more than two orders of magnitude away from the true value. For the same data using the KF did not result in any unidentified parameters. Note, that comparable inference pathologies such as multimodal distributions of inferred parameter were also reported for the maximum likelihood RE algorithm for low quality PC data or too simple stimulation protocols (Milescu et al., 2005).

In conclusion, the two different perspectives on parameter uncertainty: On the one hand distributions of ML estimates due to the random data (Milescu et al., 2005 ; Moffatt, 2007) and the Bayesian posterior distribution loose their tightly linked (and necessary) connection if the RE algorithm is used. Thus, KF robustifies also ML inferences of the rate matrix. Our findings are consistent with the findings for gene regulatory networks (Gillespie and Golightly, 2012) which show that RE approaches deliver a too narrow posterior in contrast to stochastic approximations which deliver an acceptable posterior compared to the true posterior (defined by a particle filter algorithm). On the data side of the inference problem adding cPCF data eliminates the bias, reduces the variance of the position of the HDCI and eliminates unidentified parameters (Appendix 9—figures 1 and 2) for both investigated algorithms. This advantage increases with model-complexity.

For the five-state and six-state model, we applied microscopic-reversibility (Colquhoun et al., 2004). We enforced it by hierarchical prior distribution (Materials and methods Equation 60) whose parameters can be chosen such that they allow only arbitrarily small violations of microscopic-reversibility. But the prior distribution can also be used to enforce some softer regularization around microscopic-reversibility. Thus, we can transfer the usually strictly applied algebraic constraint (Salari et al., 2018) of microscopic-reversibility to a constraint with scalable softness. In that way we can model the lack of information if microscopic-reversibility is exactly fulfilled (Colquhoun et al., 2004) by the given ion channel instead of enforcing the strict constraint upon the model.

### Prior critique and model complexity

In the Bayesian framework, the likelihood of the data and the prior generate the posterior. Thus, the performance of both algorithms can be influenced by appropriate prior distributions. We used a uniform prior over the rate matrix which is not optimal. Note, that uniform priors are widely used by several reasons. They appear to be unbiased, and are assumed to be a ‘no prior’ option (which they are not). This is true for location parameters like mean values. In contrast, for other parameters, such as scaling parameters like rates or variances, a uniform prior adds bias to the inference towards faster rates (Zwickl and Holder, 2004). We suspect, that for the PC data even in the simplest model discussed here the lower data quality limit below which we detected unidentified parameters (improper posteriors) is caused by the uniform prior. This lower limit for the KF also increases with the complexity of the model from $N_{ch}<2⋅10^{3}$ for the foue-state model till $N_{ch}≦2⋅10^{4}$ for 6-state-1-open-state model. Note, that it is hardly possible to fit the 6-state-1-open-state model with the RE approach for the same amount of PC data. We observe cPCF data eases this problem because the likelihood becomes more concentrated for all parameters. The likelihood dominates the uniform prior. Nevertheless, for most parts of the paper we used a uniform prior over the rates and equilibrium constants to be comparable with the usual default method: a plain ML which influences our results in data regimes in which the data is not strong enough to dominate the bias from the uniform prior. Thus, both algorithms perform better with smarter informative or at least unbiased prior choices for the rate matrix.

In principle, to rule out an influence of the prior, unbiased priors should be used for the rates. The standard concept for unbiased least informative priors is to construct a Jeffreys prior Jeffreys, 1946 for the rate matrix which is, however, beyond the scope of the paper.

### The influence of the brightness of the ligands of cPCF data on the inference

To evaluate the advantage of cPCF data Biskup et al., 2007 with respect to PC data only (Figure 10), we compare different types of ligands: Idealized ligands with brightness $\lambda_{b}$, emitting light only when bound to the channels, ‘real’ ligands which also produce background fluorescence when diffusing in the bath solution (Appendix 5) and current data alone. For datasets including fluorescence, the increased precision for the dissociation rate of the first ligand, $k_{2,1}$, is that strong that the variance of the posterior $ℙ⁢(k_{2,1},k_{3,2})$ nearly vanishes in the combined plot with the current data (nearly all probability mass is concentrated in a single point in Figure 10a). The effect on the error of the equilibrium constants $K_{i}$ is less strong. Additionally, the bias is reduced and even the estimation of $N_{ch}$ is improved. The brighter the ligands are, the more the posterior of the rates decorrelates, in particular $ℙ⁢(k_{2,1},k_{3,2})$ (Figure 10a). All median estimates of nine different cPCF data sets (Figure 10b) differ by less than a factor 1.1 from the true parameter except $k_{3,2}$, which does not profit as much from the fluorescence data as $k_{2,1}$ (Figure 10c). The 95th percentiles, l95 of $ℙ⁢(k_{2,1})$ and $ℙ⁢(K_{1})$ follow $l_{95}∼1/\sqrt{\lambda_{b}}$. Thus, with increasing magnitude of ligand brightness λ, the estimation of $k_{2,1}$ becomes increasingly better compared to that of $k_{3,2}$ (Figure 10c). The posterior of the binding and unbinding rates of the first ligand contracts with increasing $\lambda_{b}$. The l95 percentiles of other parameters exhibit a weaker dependency on the brightness ($l_{95}∼\lambda^{-0.1}$). For $\lambda_{b}=0.01$ photons per bound ligand and frame, which corresponds to a maximum mean signal of 20 photons per frame, the normal approximation to the Poisson noise hardly captures the asymmetry of photon counting noise included in the time traces. Nevertheless, l95 decreases about ten times when cPCF data are used (Figure 10c). The estimated variance of

$$
r(t_{i}):=\frac{y(t_{i})−(HE[n(t_{i})])}{\sqrt{var[y(t_{i})]}}
$$

with the mean predicted signal $H⁢E⁢[n⁢(t_{i})]$, for PC or cPCF data is $\sigma^{2}⁢(r_{i})≈1$ (Figure 10d) which means that the modeling predicts the stochastic process correctly up to the variance of the signal. Note that the mean value and covariance of the signal and the state form sufficient statistics of the process, since all involved distributions are approximately multivariate normal. The fat tails and skewness of $ℙ⁢(k_{21})$ and $ℙ⁢(k_{12})$ arises because the true model is too flexible for current data without further prior information. The KF allows to determine the variance (Figure 10e) of the open-channel current noise for $\sigma_{op}=0.1⁢i$. Adding fluorescence data has roughly the same effect on the estimation of $\sigma_{op}$ like using five times more ion channels to estimate $\sigma_{op}^{2}$.

![Figure 10.](https://cdn.elifesciences.org/articles/62714/elife-62714-fig10-v2.jpg)

**Figure 10.:** (a) Posteriors of PC data (blue), cPCF data with $\lambda_{b}=0.00375$ (orange) and cPCF data with $\lambda_{b}=0.375$ (green). For the data set with $\lambda_{b}=0.375$, we additionally accounted for the superimposing fluorescence of unbound ligands in solution. In all cases $N_{ch}=10^{3}$. The black lines represent the true values of the simulated data. The posteriors for cPCF $ℙ⁢(k_{2,1},k_{3,2})$ are centered around the true values that are hardly visible on the scale of the posterior for the PC data. The solid lines on the diagonal are kernel estimates of the probability density. (b) Accuracy and precision of the median estimates visualized by a violin plot for the parameters of the rate matrix for 5different data sets. Four of the five data sets are used a second time with different instrumental noise, with $\lambda_{b}=0.375$ and superimposing bulk signal. The blue lines represent the median, mean and the maximal and minimal extreme value. (c) The 95th percentile of the marginalized posteriors vs. $\lambda_{b}$ normalized by the true value of each parameter. A regime with $l_{95}∼1/\sqrt{\lambda}$ is shown for $k_{2,1}$ and K1, while other parameters show a weaker dependency on the ligand brightness. (d) Histograms of the residuals $r$ of cPCF with $\lambda_{b}=2.5⋅10^{-3}$ data and PC data. The randomness of the normalized residuals of the cPCF or PC data is well described by $r_{i}∼normal⁢(0,\sigma_{res}^{2}=1)$. The estimated variance is $\sigma_{res}^{2}=0.98+0.26$. Note that the fluorescence signal per frame is very low such that the normal approximation to Poisson counting statistics does not hold. e, Posterior of the open-channel noise $ℙ⁢(\sigma_{op}^{2}/\sigma_{op,true}^{2})$ for PC data with $N_{ch}=10^{3}$ (green) and $N_{ch}=10^{5}$ (blue) as well as for cPCF data with $N_{ch}=10^{3}$ (red) with $\lambda_{b}=0.375$. We assumed as prior for the instrumental variance $P(\sigma^{2})=N(1,0.01)$.

### Sensitivity towards filtering before the analog-to-digital conversion of the signal

On the one side, every analog signal to be digitized needs analog filtering for antialiasing according to the Nyquist theorem. On the other side, every analog filter does not only suppress unwanted white noise but also distorts the dynamics (Figure 11a) of the signal of interest (Silberberg and Magleby, 1993). Therefore, (Qin et al., 2000) recommend to avoid analog filtering as much as possible in single-channel analysis and let the HMM analyze the data in the rawest available form, even with simultaneous drift correction (Sgouralis and Pressé, 2017a). One can also expect that analog filtering of a macroscopic signal is harmful for the inference of the KF and the RE approach. For the CCCO model considered herein we investigated the mean behavior (accuracy and precision) of the posterior of both algorithms with seven data sets (simulated at 100 kHz to mimic an analog signal). A digital fourth-order Bessel filter (Virtanen et al., 2020) was then applied. The maximum analysing frequency fana of the KF used is $100-400$ Hz to be comparable to cPCF setups. The slower frequency at which the Bayesian filter analyzes the data is necessary because the applied Bessel filter has caused additional time correlations in the originally white noise of the signal. Thus, an all-data-points fit would immediately violate the white noise assumption of Equation 4 which we restore by analyzing at a much lower frequency. We then let the time scales of the induced time correlations become larger and larger by decreasing fcut. Physically, the absolute cut-off frequency fcut is irrelevant; what matters is the magnitude of fcut relative to fana and to the eigenvalues $\alpha_{i}$ of the ensemble (see, Appendix 3), since the eigenvalues determine the time evolution of the mean ensemble state, the autocorrelation, and Fourier spectrum of the fluctuations around the equilibrium distribution (Colquhoun et al., 1997b). The eigenvalues depend on the ligand concentration such that for a four-state model for each ligand concentration there are three relevant time scales $-1/\alpha_{i}$ (where $i=2,3,4$) plus the equilibrium solution which satisfies $\alpha_{1}=0$. For 10 different time series $3⋅10+3$ the outcome is to have different values of $\alpha_{i}$.Each eigenvalue is the inverse of the time constant of an exponential decay (see, Appendix 3). For this reason, we normalize in the following (Figure 11) the cut-off frequencies by $\alpha_{2}$ at the highest ligand concentration. We analyze the arithmetic mean from 7 different data sets of the median of the posterior of the rate matrix. The mean Euclidean error of the median (Figure 11b) and a series of quantiles demonstrate that overall the error of the mean median of the posterior KF (green) is smaller than that obtained by the RE. For unfiltered data, the accuracy of the mean median of the KF is increased by $≈1.6$. Based on the Euclidean error both algorithms benefit slightly from careful analog filtering for $f_{cut}/\alpha_{2}\geq1$ while the offset remains rather constant. A strong negative effect of analog filtering starts for both algorithms around $f_{cut}≈1⁢kHZ$. This is induced by $f_{cut}→f_{ana}$ (see, Appendix 10). In contrast, based on the level of each individual parameter of the rate matrix (Figure 11c 1–6) the bias induced by analog filtering immediately starts with $f_{cut}=70⁢kHz$ (Figure 11c 1–3). Note, that visual inspection of the signal (Figure 11a) does not reveal signal distortions $f_{cut}\geq10⁢kHz$ though they are detected by both algorithms. For unfiltered data, the maximum of the posterior for the RE approach is a biased estimate $E⁢[\theta_{ME}]\neq\theta_{true}$ for at least the parameters $k~_{21},K~_{21},K~_{32}$ of the true value $\theta_{true}$, which is explained (Milescu et al., 2005) by the fact that RE approaches ignore the autocorrelation of the intrinsic noise. Additionally, the data indicate that for $K~_{43}$ the maximum of the posterior is even for the KF a biased estimate which we interpret as limitations induced by the fact that the mean vector and covariance-matrix do not constitute sufficient statistics as soon as Poisson distributed photon counting or open-channel noise blurs the signal. For the RE approach, the additional bias induced by the analog filter on the mean maximum of all parameters of the posterior starts with $f_{cut}≈70$ kHz or, in other words, at the fastest time scale in the whole data set. The total bias in the estimate is reduced for k21 with the additional bias from the analog filtering but increased for k32 which for the Euclidean error leads at first to a small increase in accuracy. The KF is more robust towards analog filtering, as the results alter less with fcut (given a reasonable fcut), and less biased for unfiltered data in the estimates of these parameters. On the one hand, the Euclidean error shrinks for $f_{cut}>10$ kHz (Figure 11b). On the other hand, on the single-parameter level (Figure 11c 1–6), the parameter estimates pick up bias due the analog filtering even for high filter frequencies, in particular for the RE approach. Only for k43 the KF is more biased than the RE approach.

![Figure 11.](https://cdn.elifesciences.org/articles/62714/elife-62714-fig11-v2.jpg)

**Figure 11.:** High (Bayesian) sampling frequencies and minimal analog filtering does minimize bias which otherwise deteriorates parameter identification. In order to mimic an analog signal before the analog-to-digital conversion we simulated seven different 100 kHz signals which were then filtered by a digital fourth-order (4 pole) Bessel filter. The activation curves were then analyzed with the Bayesian filter at 125 Hz and the deactivation curves at sampling rates between 166-500 Hz. We chose for the analog signal $\sigma_{exp}/i=10$, $\sigma_{op}/i=0.1$, thus a stronger background noise, and we set the mean photon count per bound ligand as $\lambda_{b}=5$. For the ensemble size we choose $N_{ch}=10^{3}$. (a) Current time trace filtered with different fcut. Except for 100 Hz (red) the signal distortion is visually undetectable. Nevertheless, the invisible signal distortions from analog filtering are problematic for both algorithms. (b) Estimate of the distribution mean Euclidean error of the median of the posterior vs. the cut-off frequency of a 4 pole Bessel filter (upper scale is in units of kHz) or scaled to the channel time scale (lower scale, see text). The fastest two eigenvalues $\alpha_{1,2}/\alpha_{2}$ for the highest ligand concentration are indicated by the black vertical lines. The fastest ratios $\alpha_{1,2}/\alpha_{2}$ for the next smaller ligand concentration are indicated by the red vertical lines. The slowest eigenvalue ratio $\alpha_{3}/\alpha_{2}$ at the highest ligand concentration is beyond the left limit of the x-axis. The solid line is the mean median of five data sets of the respective RE posterior (blue) and KF posterior (green). The green shaded area indicates the 0.6 quantile (ranging from the 20th percentile till the 80th percentile), demonstrating the distribution of the error of the posterior median due to the randomness of the data. (c) 1–3, Accuracy (bias) and precision of the maxima of the posterior $k~_{max,i⁢j}$ of the posterior maxima of the rates vs. the cut-off frequency of a Bessel filter. The shaded areas indicate the 0.6 quantiles (ranging from the 20th percentile till the 80th percentile) due the variability among data sets while the error bars show the standard error of the mean. The deviation of the mean from the true value is an estimate of the accuracy of the algorithm while the quantile indicates the precision. (c) 4–6, Accuracy and precision of the maxima of the posterior $K~_{max,i⁢j}$ of the posterior maxima of the corresponding equilibria vs. the cut-off frequency of a Bessel filter.

The KF is the unique minimal variance Bayesian filter for a linear Gaussian process (Anderson and Moore, 2012) which means, given that the assumptions of the KF are fulfilled by the true process of interest, the KF is mathematically proven the best model-based filter to apply. Consequently, analog filtering does not provide an advantage unless it removes specific high frequency external noise sources (colored noise). We demonstrate (Appendix 10) this for PC data and varied fcut and fana. On the downside, increasing fana makes the results of both algorithms more fragile if $f_{cut}≫f_{ana}$ does not hold. Thus, the critical edge in Figure 11b is indeed induced by fcut approaching fana. This suggests that the white noise assumption of both algorithms is violated. On the upside, if $f_{cut}≫f_{ana}$ is given, the KF with an order of magnitude higher fana has a reduced bias of up to 20% for $f_{cut}→∞$ for individual parameters compared to the KF with lower fana. Additionally, a higher fana reduces the variance. To reduce the bias of parameter estimates to a minimum, the experimental design offers two remedies, either doing cPCF experiments with additional discussed advantages or using the KF at a high fana with even much higher fcut.

By theoretical grounds a further argument for doing less analog filtering is that this benchmark analyzes data of a finite state Markov process, which is a coarse proxy for the true process. In reality, relaxation of a protein is a high-dimensional continuous-state Markov process with infinitely many relaxation time scales (eigenvalues) (Frauenfelder et al., 1991) which, however, might be grouped in slower experimentally accessible and non-accessible faster time scales (Noé et al., 2013). With larger data sets of higher quality from better experiments, the faster time scales might become accessible if they are not distorted by analog filtering. In conclusion, deciding on a specific kinetic scheme and inferring its parameters means finding a model which accommodates in the best way to the set of observed eigenvalues. Analog filtering hampers the RE, KF or HMM forward-backward algorithm (Qin et al., 2000) to correctly describe the faster time scales.

### Error due to finite integration time of fluorescence data

So far, we idealized the fluorescence data integration time as being instantaneously relative to the time scales of ensemble dynamics. In real experiments, the fluorescence signal of cPCF data has orders of magnitude longer minimal integration time $T_{int}$ (time to record all voxels of a frame) or maximal integration frequency $f_{int}=1/T_{int}$, than the possible sampling frequency of current recordings. We mimic the finite integration time

$$
y_{digital}⁢(t_{i})=\int_{t_{start}}^{t_{i}=t_{start}+T_{int}}y_{analog}⁢(t)⁢dt≈\sumj\in[t_{start},t_{start}+T_{int}]y⁢(t_{j})⁢Δ⁢t
$$

by summing with a sliding window the 100 kHz signal including the white noise to obtain data at an effectively lower sampling frequency (Figure 12a). Additionally we set the Bessel filter for the current data to $f_{cut}/\alpha_{2}=4.59$ or $f_{cut}=90$ kHz. The fastest used analysing frequency is $f_{ana}=500⁢Hz$. We scale mean photo brightness $\lambda_{b}$ and background noise down such that the signal-to-noise ratio of the lower integration frequency data is the same as of the high-frequency data $\lambda_{b}/T_{int}=c⁢o⁢n⁢s⁢t$ . We do that in order to separate the bias from the finite integration time from other effects such as a better signal to noise ratios for each integrated point. Note that we only analyzed the plot until $f_{int}=f_{ana}$. Both algorithms incur very similar bias due to the finite integration time (Figure 12b). The KF (green) is more precise for high integration frequencies $f_{cut}/\alpha_{2}$ until $f_{cut}/\alpha_{2}≈0.08$ then the RE approach becomes more robust. Similar to Bessel-filtered current data (Figure 11b) on the single parameter level the systematic deviations start early for example $f_{int}=10$ kHz for K21 (Figure 12c4). Possibly the systematic deviations start (Figure 12c2) already at $f_{int}=50$ kHz for k32. The sudden increase of the Euclidean error (Figure 12b) of the mean median at $f_{cut}/\alpha_{2}≈0.2$ occurs in this case not due to fint approaching fcut but due to $f_{int}⪅\alpha_{1,2}$ for many ligand concentrations. To show this we plot the results of the fitting of five different data sets without including the highest 4 ligand concentrations (red) which means the largest eigenvalues are much smaller (Figure 12b,C1-6). Additionally, we keep $f_{int}=c⁢o⁢n⁢s⁢t$. Although fluctuations of the posterior medians are higher, the KF becomes more robust. Note, that the fastest eigenvalues of these reduced data sets are indicated by the blue bars (Figure 12b and c4). Based on the Euclidean error (Figures 11a and 12a) the robustness of both algorithms against the cut-off frequency is compared with the robustness against the integration frequency found to be about an order of magnitude higher. That is related to a specific detail of the model used: the binding reaction, corresponds to the fastest time scales of the overall dynamic (difference between Figure 1b and c), which is exposed by the fluorescence signal. Thus, kinetic analysis of any data should make sure that the corresponding frequency of the most dominant timescales of the time series are much slower than the respective fintfcut independently of the investigated algorithms.

![Figure 12.](https://cdn.elifesciences.org/articles/62714/elife-62714-fig12-v2.jpg)

**Figure 12.:** Thus the sampling should be faster than the fastest eigenvalues to avoid biased results. We simulated five different 100 kHz cPCF signals. All forms of noise were added and then the fluorescence signal was summed up using a sliding window to account for the integration time to produce one digital data point. The activation curves were then analyzed with the Bayesian filter at 125 Hz and the deactivation curves at $166-500$ kHz, see caption of Figure 8. We plot the 0.6-quantile (interval between the 20th and the 80th percentile) to mimic ±one standard deviation from the mean as well as the mean of the distribution of the maxima of the posterior for different data sets. (Note, this is not equivalent to the mean and quantiles of the posterior of a single data set.). The quantiles represent the randomness of the data while the error bars indicate the standard error of the mean maximum of the posterior. Blue (RE) and green (KF) indicate the two algorithms with the standard data set while red (KF) shows examples that use only the six smallest ligand concentrations for the analysis in order to limit the highest eigenvalues. a, Instantaneous probing of the ligand binding (blue) compared with a probing signal which runs at $f_{int}=1$ kHz. The integrated brightness of the bound ligand is $\lambda_{b}=5$ photons per frame. Although the red curves seem like decent measurements of the process except for the highest two shown ligand concentrations, the mean error is roughly an order of magnitude worse than for $f_{int}=10$ kHz. Note, that for visualization we plot at a higher frequency than the Kalman filter analyzed the data. b, Estimate of the distribution of the (Euclidean error of the mean median of the posterior) vs. the scaled integration frequency $f_{int}/\alpha_{2}=1/(\alpha_{2}⋅T_{integration})$. We use integration frequency instead of the integration time to make the plot comparable to the Bessel filter plot. The solid line is the mean median of five data sets of the respective KF posterior (green, red) and RE posterior (blue). The shaded areas indicate the 0.6-quantile which visualizes the spread of the distribution of point estimates. The two fastest time scales (eigenvalues) at the highest ligand concentration are indicated by the vertical black lines, the time scales of the next lower ligand concentrations with the red vertical lines. c 1–3, Accuracy (bias) and precision of the maxima of the posterior $k_{i⁢j,m⁢a⁢x}$ rates vs. the integration frequency. c 4–6, Accuracy and precision of the maxima of the posterior $K_{i⁢j,m⁢a⁢x}$ of the corresponding equilibria vs. the cut-off frequency of a Bessel filter.

### Conclusions

We generalized the filter equations (Methods Equation 37, 38d, 57, 58 and 59) of the KF for analyzing the gating and binding dynamics of ligand-gated ion channels with a realistic signal-generating model for isolated patch-clamp (PC) and confocal patch-clamp fluorometry (cPCF) data including open-channel noise, photon-counting noise and background noise. Any other type of linear kinetic scheme (e.g. for voltage-dependent channels) and signal can be applied as long as the characteristics of the signal are sufficiently described by normal distributions. Our approach is derived by approximating the chemical master equation of a first order chemical reaction network (which ion channel experiments usually are) which is exact up to the second statistical moment. For first-order chemical reaction networks, the linear noise approximation (Wallace et al., 2012) are exact up to the second moment too (Grima, 2015). Thus, we can conclude that our Bayesian filter uses a time integrated version of the linear noise approximation. To our understanding of Wallace et al., 2012 our approach is thus equivalent to approaches based on the chemical Langevin or Fokker-Planck equations (Gillespie, 2002). Consequently, this also makes the considerations of the quality of the chemical Langevin equation as an approximation (Gillespie, 2000) of the chemical master equation valid for our approach. Compared to previous attempts Moffatt, 2007, this mathematical generalization is necessary (Figure 3b) in order to use Bayesian filters on macroscopic PC or cPCF data. With our algorithm, we demonstrate (Figures 3c and 7) that the common assumption that for large ensembles of ion channels simpler deterministic modeling by RE approaches is on par with stochastic modeling, such as a KF, is wrong in terms of Euclidean error and uncertainty quantification (Figures 5a–c ,–6a–b).

Enriching the data by fluorescence-based ligand binding reveals two regimes. In one regime, the two-dimensional data increase the accuracy of the parameter estimates up to $≈10$-fold (Figure 4a and c). In the other regime of lower channel expression, enriching the data by the second observable, makes non-identified parameters to identified parameters. The second observable in cPCF data decreases the overfitting tendency (Figure 4a, b and d) of the RE approach on the true process. Thus, in this regard the advantage of the KF becomes smaller. However, by exploiting Bayesian HDCV we gain a second perspective: We show for various signal-to-noise ratios (Figures 5a–c ,–6a–b) that the posterior sampled by a RE approach never covers the true values within a reasonable HDCV. Thus, the central feature of Bayesian statistics, exact uncertainty quantification by having the full posterior, is meaningless in combination with an RE approach (considering the type of data and set of signal-to-noise ratios that we tested). This even holds true for very pessimistic signal-to-noise assumptions Figure 6b. If HDCVs based on an RE approach cannot be trusted, the same applies to confidence volumes based on the curvature of the likelihood. This is not the case for the KF which delivers properly shaped posteriors (Figures 6a–c ,–5a–c). Increasing the model complexity, at unchanged PC data quality (Figure 7) shows that the RE approach displays unidentified rates even for large ion channel ensembles while our approach identified all parameters for the same data. We also investigated the robustness of both algorithms against the cut-off frequency of a Bessel filter (Figure 11) and showed the overall superior robustness of the KF against errors of analog filtering compared to the RE approach. Analog filtering has its limitations due to distorting the higher frequencies of the Fourier spectrum of the signal. Thus, one should let the KF sample as fast as possible, with a cut-off frequency of at least one order of magnitude higher than the sampling frequency of the KF.

Similar to the Bessel filter, the KF is more robust than the RE approach against errors due to the finite integration time. Nevertheless, it is crucial for both algorithms (Figure 12), that the intrinsic time scales (1/eigenvalues) of the process to be analyzed are slower than the integration time of the data points. Otherwise the accuracy of the inference deteriorates.

Altogether, we demonstrated the performance of the generalized Kalman filter on ion channel data for inference of kinetic schemes. Nevertheless, our approach can approximate any other stochastic system and signal distributions of linear (pseudo-first-order) kinetics (Sorenson and Alspach, 1971). Prospective extensions of the Bayesian filter, for example by Bayesian Gaussian sum filters or similar numerically brute force concepts such as particle filters (Golightly and Wilkinson, 2011; Gillespie and Golightly, 2012), can overcome modeling errors at low ion channel numbers or low photon fluxes.

## Materials and methods

We simulated state evolution $s⁢(t)$ with either the software QuB (Nicolai and Sachs, 2014) for PC data or an inhouse Matlab routine (The code will be shared on request.) for cPCF data. The inhouse Matlab routine is an implementation of the Gillespie algorithm Gillespie Daniel T. (1977). Traces were summed up, defining the ensemble state vector $n⁢(t):=(n_{1},n_{2},n_{3},n_{4})^{⊤}$, which counts the number of channels in each state. At first we used a 10 kHz sampling frequency for the Gillespie algorithm but for investigating the errors induced by analog filtering the current signal and the finite integration time for each fluorescence data point the Gillespie algorithm sampled at 100 kHz. The KF, RE, and Bayesian filter routines were implemented in Stan (Carpenter et al., 2017) with the interface package PyStan and ran on a high performance computing cluster with O(100) Broadwell and SkyLake nodes. A Tutorial for Patch clamp data can be found on the git hub page https://github.com/JanMuench/Tutorial_Patch-clamp_data and for cPCF data, https://github.com/JanMuench/Tutorial_Bayesian_Filter_cPCF_data. The cPCF data simulation code can be found here: https://cloudhsm.it-dlz.de/s/QB2pQQ7ycMXEitE (Source code 1).

### Methods

Hereinafter, we derive the equations for our Bayesian filter for time series analysis of hidden linear chemical reaction networks (kinetic schemes). A detailed description of the experimental noise is provided in the Appendix 5.

### The relation of Bayesian statistics to the Kalman filter

The following conventions are generally used: Bold symbols are used for multi-dimensional objects such as vectors or matrices. Calligraphic letters are used for (some) vectorial time series and double-strike letters are used for probabilities and probability densities. Within the Bayesian paradigm (Hines, 2015; Ball, 2016), each unknown quantity, including model parameters $\theta$ and time series of occupancies of hidden states $N_{T}={n⁢(t_{i})}_{i=1}^{T}$, are treated as random variables conditioned on observed time series data $Y_{T}=y(t_{i})_{i=1}^{T}$. The prior $ℙ⁢(\theta)=\prod_{j}^{N_{par}}ℙ⁢(\theta_{j})$ or posterior distribution $P(\theta|Y_{T})$ encodes the available information about the parameter values before and after analysing the data, respectively. According to the Bayesian theorem, the posterior distribution

$$
P(\theta|Y_{T})=\frac{1}{Z(Y_{T})}L(Y_{T}|\theta)\prodjN_{par}P(\theta_{j})
$$

is a probability distribution of a parameter set $\theta$ conditioned on $Y_{T}$. The likelihood $L(Y_{T}|\theta)$ encodes the distribution of the data by modelling the intrinsic fluctuations of the protein as well as noise coming from the experimental devices. The prior provides either assumptions before measuring data or what has been learnt from previous experiments about $\theta$. The normalization constant

$$
Z(Y_{T})=\intL(Y_{T}|\theta)P(\theta)d\theta
$$

ensures that the posterior is a normalized distribution. The KF is a special class of models in the family of Bayesian filters (Ghahramani, 1997), which is a generalisation of the classical KF. Due to its linear time evolution (Equation 1), the KF is particularly useful for modeling time series data of ensembles dynamics of first order chemical networks. It delivers a set of recursive algebraic equations (Materials and methods Equation 28 and Equation 32) for each time point, which allows to express the prior $P(n(t)|Y_{t−1})$ and (after incorporating $y⁢(t)$) the posterior $P(n(t)|Y_{t})$ occupancies of hidden states $n⁢(t)$ for all $t$ given a set of parameters $\theta$. This means the KF solves the filtering problem (inference of $N_{T}$) by explicitly modeling the time evolution of $n⁢(t)$ by multivariate normal distributions. This allows us to replace $L(Y_{T}|\theta)$ of Equation 20 by the expression of Equation 9.

The Bayesian framework (as demonstrated in this article) has various properties which makes it superior to ML estimation (MLE) (McElreath, 2018). Those properties are in particular useful for the analysis of biophysical data since very often the dynamics of interest are hidden or latent in the data. Models with a hidden structure are called singular. For regular (non-singular) statistical models, maxima $\theta_{ML}$ of the posterior or likelihood converge in distribution

$$
limn→∞\sqrt{n}(\theta_{ML}−\theta_{true})∼N(0,F^{−1}(\theta_{true}))
$$

to the true value $\theta_{true}$,where $F^{-1}⁢(\theta_{true})$ is the inverse Fisher information matrix. Under those conditions it is justified to derive from the curvature of the likelihood at $\theta_{ML}$ via the Cramer-Rao-bound theorem

$$
covar⁡[\theta_{ML}]=F^{-1}⁢(\theta_{ML})
$$

a confidence volume for the inferred parameters. In contrast, consider for example the type of data investigated in this study which probes the protein dynamics by current and light. Singularity means that the Fisher information matrix of a model is not invertible leading to the breakdown of the Cramer-Rao Bound theorem. Due to the breakdown, it cannot be guaranteed that even in the asymptotic limit the log-likelihood function can be approximated by a quadratic form Watanabe, 2007. Thus, usually the MLE does not obey Equation 22. Consequently, the posterior distribution is usually not a normal distribution either (Watanabe, 2007). Using the full posterior distribution without further approximations detects the resulting problems such as deviation from normality or non-identifiability of parameters, related to the singularity. In conclusion, the posterior is still a valid representation of parameter plausibility while ML fails.

### Time evolution of a Markov Model for a single channel

In the following, we write the time $t$ as function argument rather than a subscript. Following standard approaches, we attribute to each state of the Markov model an element of a vector space with dimension $M$. At a time, a channel can only be in a single state. This implies that the set of possible states is S:=${(1,0,0,…),(0,1,0,…),…,(…,0,1)}⊂{0, 1}^{M}$. In the following, Greek subscripts refer to different states while Latin subscripts refer to different channels. By $s⁢(t)=e_{\alpha}$ we specify that the channel is in state α at time $t$. Mathematically, $e_{\alpha}$ stands for the α-th canonical unit Cartesian vector (Table 1).

**Table 1.**
 Important symbols.


<table>
  <thead>
    <tr>
      <th>Symbol</th>
      <th>Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>θ</td>
      <td>Set of all unknown model parameters for which the posterior distribution is sampled</td>
    </tr>
    <tr>
      <td>n⁢(t)</td>
      <td>Hidden ensemble occupancy vector of channel states in a specific patch at time t which is a continuous Markov state vector n(t)∈RM</td>
    </tr>
    <tr>
      <td>P⁢(t)</td>
      <td>Variance-covariance matrix of a hidden ensemble state n(t) n a specific patch at time t which contains the dispersion of the ensemble and the lacking knowledge of the algorithm about the true n(t)</td>
    </tr>
    <tr>
      <td>T</td>
      <td>Transition matrix of a single channel</td>
    </tr>
    <tr>
      <td>K</td>
      <td>Rate matrix which is the logarithm of the transition matrix</td>
    </tr>
    <tr>
      <td>H</td>
      <td>Observation matrix which projects the hidden ensemble state vector onto its mean signal.</td>
    </tr>
    <tr>
      <td>s</td>
      <td>Single-molecule Markov state vector</td>
    </tr>
    <tr>
      <td>ki,j</td>
      <td>Specific transition rate from state j to state i, [K]i,j=ki,j ,</td>
    </tr>
    <tr>
      <td>Ki</td>
      <td>Ratio of two transition rates i.e. an equilibrium constant</td>
    </tr>
    <tr>
      <td>y⁢(t)</td>
      <td>Data point at time</td>
    </tr>
    <tr>
      <td>T</td>
      <td>Number of observations in a time series</td>
    </tr>
    <tr>
      <td>YT</td>
      <td>Time series of T data points, YT=y(ti)i=1T</td>
    </tr>
    <tr>
      <td>NT</td>
      <td>Time series of T hidden ensemble states, NT={n(ti)}i=1T</td>
    </tr>
    <tr>
      <td>Nch,j</td>
      <td>Number of channels in patch number</td>
    </tr>
    <tr>
      <td>i</td>
      <td>Mean electrical current through a single-channel</td>
    </tr>
    <tr>
      <td>σm2</td>
      <td>Variance of the current including all noise from the patch and the recording system</td>
    </tr>
    <tr>
      <td>σop2</td>
      <td>Variance of the current noise generated by a single open-channel</td>
    </tr>
    <tr>
      <td>λb</td>
      <td>Mean brightness of a bound ligand</td>
    </tr>
    <tr>
      <td>λFl</td>
      <td>Mean brightness of the fluorescence signal from bulk and bound ligands</td>
    </tr>
    <tr>
      <td>σbulk2</td>
      <td>Variance of the fluorescence generated by unbound ligands after subtraction of the image obtained for the reference dye</td>
    </tr>
    <tr>
      <td>M</td>
      <td>Number of single-channel states which is the dimension of n(t)∈NM in the KF algorithm</td>
    </tr>
    <tr>
      <td>Nobs</td>
      <td>Dimensions of the observational space</td>
    </tr>
    <tr>
      <td>F(Y)</td>
      <td>True probability density of Y, i.e. the true data-generating process</td>
    </tr>
    <tr>
      <td>L(Y|θ)</td>
      <td>Likelihood function of the model parameters</td>
    </tr>
    <tr>
      <td>P(θ|Y)</td>
      <td>Posterior distribution of the model parameters</td>
    </tr>
    <tr>
      <td>Ppred(Y~|Y)</td>
      <td>Predictive distribution of the new data points</td>
    </tr>
    <tr>
      <td>O(y|n)</td>
      <td>Distribution of observables for a single time step</td>
    </tr>
    <tr>
      <td>N(⋅|μ,Σ)</td>
      <td>Normal distribution with mean μ and variance-covariance matrix ∑</td>
    </tr>
    <tr>
      <td>E[⋅]</td>
      <td>Mean value</td>
    </tr>
  </tbody>
</table>

Assuming that the state transitions can be modeled by a first order Markov process, the path probability can be decomposed as the product of conditional probabilities as follows:

$$
ℙ(path)=ℙ(s(0),s(1),…,s(T))=ℙ(s(0))⋅ℙ(s(1)∣s(0))⋅ℙ(s(2)∣s(1))⋯ℙ(s(T)∣s(T-1)).
$$

Markov models (MMs) and rate models are widely used for modeling molecular kinetics (Appendix 2). They provide an interpretation of the data in terms of a set of conformational states and the transition rates between these states. For exactness it remains indispensable to model the dynamics with a HMMs (Noé et al., 2013). The core of a hidden Markov model is a conventional Markov model, which is supplemented with a an additional observation model. We will therefore first focus on a conventional Markov model. State-to-state transitions can be equivalently described with a transition matrix $T$ in discrete time or with a rate matrix $K$ in continuous time, as follows:

$$
T_{\alpha,\beta}:=ℙ⁢(s⁢(t+1)=e_{\alpha}∣s⁢(t)=e_{\beta})=exp⁢(K⋅Δ⁢t)_{\alpha,\beta},
$$

where $exp$ is the matrix exponential. We aim to infer the elements of the rate matrix $K$, constituting a kinetic model or reaction network of the channel. Realizations of sequences of states can be produced by the Doob-Gillespie algorithm Gillespie Daniel T. (1977). To derive succinct equations for the stochastic dynamics of a system, it is beneficial to consider the time propagation of an ensemble of virtual system copies. This allows to ascribe a probability vector $p⁢(t)$ to the system, in which each element $p_{\alpha}⁢(t)$ is the probability to find the system at $t$ in state α. One can interpret the probability vector $p$ as the instantaneous expectation value of the state vector $s$.

$$
p(t)=E[s(t)]
$$

The probability vector obeys the discrete-time Master equation

$$
p⁢(t+1)=Tp⁢(t)
$$



$$
E[s(t+1)]=TE[s(t)]
$$

### Time evolution of an ensemble of identical non-interacting channels

We model the experimentally observed system as a collection of non-interacting channels. A single channel can be modeled with a first-order MM. The same applies to the ensemble of non-interacting channels. We focus on modeling the time course of extensive macroscopic observables such as the mean current and fluorescence signals as well as their fluctuations. A central quantity is the vector $n⁢(t)$ which is the occupancy of the channel states at time $t$:

$$
n⁢(t)=\sumi=1N_{ch}s_{i}⁢(t)
$$

This quantity, like $s⁢(t)$, is a random variate. Unlike $s⁢(t)$, its domain is not confined to canonical unit vectors but to $n\inℕ^{M}$. From the linearity of Equation 28 in the channel dimension and from the single-channel CME Equation 27b one can immediately derive the equation for the time evolution of the mean occupancy $n¯⁢(t)=E⁢[n⁢(t)]$:

$$
n¯_{\alpha}⁢(t+1)=\sum\betaT_{\alpha,\beta}⁢n¯_{\beta}⁢(t)
$$

with the transition matrix $T$. The full distribution $ℙ⁢(n⁢(t+1)|n⁢(t))$ is a generalized multinomial distribution. To understand the generalized multinomial distribution and how it can be constructed from the (conventional) multinomial distribution, consider the simplified case where all channels are assumed to be in the same state α. Already after one time step, the channels will have spread out over the state space. The channel distribution after one time step is parametrized by the transition probabilities in row number α of the single-channel transition matrix $T$. According to the theory of Markov models, the final distribution of channels originating from state α is the multinomial distribution

$$
ℙ⁢(n^{(\alpha)}⁢(t+1)∣n_{\alpha}⁢e_{\alpha})=ℙ⁢(n_{1},…,n_{M}∣n⁢(t)=n_{\alpha}⁢e_{\alpha})=\frac{n_{\alpha}!}{n_{1}!⁢⋯⁢n_{M}!}⁢T_{1,\alpha}^{n_{1}}⁢⋯⁢T_{M,\alpha}^{n_{M}}
$$

In general, the initial ensemble will not have only one but multiple occupied channel states. Because of the independence of the channels, one can imagine each initial sub-population spreading out over the state space independently. Each sub-population with initial state α gives rise to its own final multinomial distribution that contributes $n_{\beta}^{(\alpha)}$ transitions into state β to the total final distribution. The total number of channels at $t+1$ in each state can then be simply found by adding the number of channels transitioning out of the different states α.

$$
n⁢(t+1)=\sum\alphan^{(\alpha)}⁢(t+1)
$$

Evidently, the total number of channels is conserved during propagation. The distribution of $n⁢(t+1)$, defined by Equations 30; 31, is called the generalized multinomial distribution:

$$
n⁢(t+1)∼general-multinomial⁡(n⁢(t),T)
$$

While no simple expression exists for the generalized multinomial distribution, closed form expressions for its moments can be readily derived. For large $N_{ch}$ each $ℙ⁢(n^{(\alpha)}⁢(t+1)∣n_{\alpha}⁢e_{\alpha})$ can be approximated by a multivariate-normal distribution such that also $general-multinomial⁡(n⁢(t),T)$ has a multivariate-normal approximation. In the next section, we combine the kinetics of channel ensembles with the KF by a moment expansion of the governing equations for the ensemble probability evolution.

### Moment expansion of ensemble probability evolution

The multinomial distribution (Fredkin and Rice, 1992) has the following mean and covariance matrix

$$
n¯^{(\alpha)}⁢(t+1)=n_{\alpha}⁢T_{:,\alpha}
$$



$$
Σ^{(\alpha)}⁢(t+1)=n_{\alpha}⁢diag⁢(T_{:,\alpha})-n_{\alpha}⁢T_{:,\alpha,:}⁢T_{:,\alpha}^{⊤}
$$

where $T_{:,\alpha}$ denotes the column number α of the transition matrix and $diag⁢(T_{:,\alpha})$ describes the diagonal matrix with $T_{;,\alpha}$ on its diagonal. Combining Equation 31 with Equations 33; 34 we deduce the mean and variance of the generalized multinomial distribution:

$$
E⁢[n⁢(t+1)∣n⁢(t)]=\sum\alphan_{\alpha}⁢(t)⁢T_{:,\alpha}=Tn⁢(t)
$$



$$
cov⁢[n⁢(t+1),n⁢(t+1)∣n⁢(t)]=\sum\alphan_{\alpha}⁢(t)⁢(diag⁢(T_{:,\alpha})-T_{:,\alpha}⁢T_{:,\alpha}^{⊤})=diag⁢(Tn⁢(t))-T⁢diag⁢(n⁢(t))⁢T^{⊤}
$$

Note that Equations 35; 36 are conditional expectations that depend on the random state $n$ at the previous time $t$ and not only on the previous mean $n¯$. To find the absolute mean, the law of total expectation is applied to Equation 35, giving

$$
n¯(t+1)=E[E[n(t+1)|n(t)]]=Tn¯(t),
$$

in agreement with the simple derivation of Equation 29. We introduce a shorthand $P(t):=cov(n(t),n(t))$ for the absolute covariance matrix of $n(t+1)$. Similarly, $P(t)$ can be found by applying the law of total variance decomposition (Weiss, 2005 to Equations 35; 36), giving

$$
P(t+1)=E[cov(n(t+1),n(t+1)∣n(t))]+cov[E(n(t+1)∣n(t)),E(n(t+1)∣n(t))]
$$



$$
=diag(Tn¯(t))−Tdiag(n¯(t))T^{⊤}+cov(Tn(t),Tn(t))
$$



$$
=diag(Tn¯(t))−Tdiag(n¯(t))T^{⊤}+Tcov(n(t),n(t))T^{⊤}
$$



$$
=diag(Tn¯(t))−Tdiag(n¯(t))T^{⊤}+TP(t)T^{⊤}
$$

Equations 37, 38d dare compact analytical expressions for the mean and the covariance matrix of the occupancy vector $n$ at $t+1$ that depend on the mean $n¯$ and covariance matrix $P$ at the previous time step $t$. Chaining these equations for different time steps $t=0,…,T$ allows to model the whole evolution of a channel ensemble. Moreover, these two equations together with the output statistics of $O(y|n(t))$ are sufficient to formulate correction equations Equation 59 of the KF (Moffatt, 2007; Anderson and Moore, 2012). These equations will be used in a Bayesian context to sample the posterior distribution of the model parameters. The sampling entails repeated numerical evaluation of the model likelihood. Therefore, analytical equations for the ensemble evolution that can be quickly evaluated on a computer millions of times are indispensable. This was achieved by deriving Equation 37, Equation 38d. Comparing Equation 38d with the KF prediction equation (Anderson and Moore, 2012) for $P(t)$, we obtain the state-dependent covariance matrix of Equation 3 as

$$
Q(T,n¯(t))=diag(Tn¯(t))−Tdiag(n¯(t))T^{T}
$$

In the following section on properties of measured data and the KF, we no longer need to refer to the random variate $n(t)$. All subsequent equations can be formulated by only using the mean hidden state $n¯(t)$ and the variance-covariance matrix of the hidden state $P⁢(t)$. We therefore drop the overbar in $n¯⁢(t)$ so that the symbol $n⁢(t)$ refers from now on to the mean hidden state.

### Modeling simultaneous measurement of current and fluorescence

In the following, we develop a model for the conditional observation distribution $O(y|n(t))$ (Appendix 5 for experimental details). Together with the hidden ensemble dynamics this will enable us to derive the output statistics of the KF (see, below). Let $y⁢(t)$ be the vector of all observations at $t$. Components of the vector are the ion current and fluorescence intensity.

$$
y(t)=(fluorescence intensity(t)ion current(t))=(y_{flu}(t)y_{curr}(t))
$$

As outlined in the introduction part, in Equation 4 we model the observation by using a conditional probability distribution $O(y(t)|n(t))$ that only depends on the mean hidden state $n⁢(t)$, as well as on fixed channel and other measurement parameters. $O(y(t)|n(t))$ is modeled as a multivariate normal distribution with mean $Hn⁢(t)$ and variance-covariance matrix $Σ⁢(t)$, that can in general depend on the mean state vector $n⁢(t)$ (much like the covariance matrix of the kinetics in (Equation 38d) ). The observation matrix $H\inℝ^{N_{obs}\timesM}$ projects the hidden state vector $n⁢(t)$ onto $Hn⁢(t)\inℝ^{N_{obs}}$, the observation space. The observation distribution is

$$
O(y(t)|n(t))=N(y(t)|Hn(t),Σ(n(t)))⇔y(t)=Hn(t)+ν(t).
$$

This measurement model is very flexible and allows to include different types of signals and error sources arising from both the molecules and the instruments. A summary of the signals and sources of measurement error and their contributions to the parameters of $O(y(t)|n(t))$ is provided by Table 2. Below we address the two types of signals and four noise sources one by one. For this, we decompose the observation matrix and the observation noise covariance matrix into the individual terms:

$$
H=H_{I}+H_{binding}
$$



$$
Σ⁢(t)=Σ_{open}⁢(t)+Σ_{meas.}+Σ_{binding}⁢(t)+Σ_{back}
$$

**Table 2.**
 Summary of signals and noise sources for the exemplary CCCO model with the closed states $\alpha=1,2,3$ and the open state $\alpha=4$.The observed space is two-dimensional with $y_{F⁢l}=fluorescence$ and $y_{I}=ion current$. The fluorescence signal is assumed to be derived from the difference of two spectrally different Poisson distributed fluorescent signals. That procedure results in a scaled Skellam distribution of the noise.


<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="2">ion current</th>
      <th colspan="2">fluorescence</th>
    </tr>
    <tr>
      <th></th>
      <th>current signal</th>
      <th>measurement noise</th>
      <th>fluorescence signal</th>
      <th>background fluorescence</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Signaling states</td>
      <td>Open state</td>
      <td>-</td>
      <td>Ligand-bound states</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Error term</td>
      <td>Open-channel noise</td>
      <td>Measurement noise</td>
      <td>Photon counts</td>
      <td>Bulk noise</td>
    </tr>
    <tr>
      <td>Affected signal</td>
      <td>Current</td>
      <td>Current</td>
      <td>Fluorescence</td>
      <td>Fluorescence</td>
    </tr>
    <tr>
      <td>Distribution</td>
      <td>Normal (in4,σop2n4)</td>
      <td>Normal (0,σm2)</td>
      <td>Poisson (λb⁢ni⁢(t))</td>
      <td>Scaled Skellam</td>
    </tr>
    <tr>
      <td>Contribution to H</td>
      <td>H2,4=i</td>
      <td>-</td>
      <td>H1,:=(0,λb,2⁢λb,2⁢λb)</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Contribution to Σ</td>
      <td>Σ2,2=σop2⁢n4⁢(t)</td>
      <td>Σ2,2=σm2</td>
      <td>Σ1,1=(0,λb,2⁢λb,2⁢λb)⁢n⁢(t)</td>
      <td>Σ1,1=σback2</td>
    </tr>
  </tbody>
</table>

In the following, we report the individual matrices for the exemplary CCCO model with one open state $\alpha=4$ and three closed states $\alpha=1,2,3$. Matrices can be constructed analogously for the other models. For the definition of $Σ_{back}$ refer to (Appendix 5).

### Macroscopic current and open-channel noise

We model the current and the intrinsic fluctuations of the open-channel state $s=e_{4}$ (the open channel noise) by a state-dependent normal distribution with mean $i⁢n_{4}⁢(t)$ where $n_{4}⁢(t)$ is the number of channels in the open state at $t$ and $i$ is the single-channel current. The additional variance of the single-channel current is described by $\sigma_{open}^{2}$. The sum of the instrumental noise of the experimental setup and the open channel noise is modeled as uncorrelated (white) normally distributed noise with the mean $E⁢[ν_{I}⁢(t)]=0$ and variance $E⁢[ν_{I}^{2}⁢(t)]=\sigma_{op}^{2}⁢n_{4}⁢(t)+\sigma_{m}^{2}$. By making the open-channel noise dependent on the hidden state population $n_{4}⁢(t)$, we fully take advantage of the flexibility of Bayesian filters which admits an (explicitly or implicitly) time-dependent observation model. By tabulating the parameters of the two normal distributions into $H$ and $Σ$, we obtain

$$
H_{I}:=(0000000i)
$$



$$
Σ_{open}⁢(t)+Σ_{meas.}:=(000\sigma_{op}^{2}⁢n_{4}⁢(t)+\sigma_{m}^{2})
$$

One can now ask for the variance of a data point $y⁢(t)$ given the epistemic and aleatory uncertainty of $n⁢(t)$ encoded by $P⁢(t)$ in Equation 38d. By using the law of total variance the signal variance follows as:

$$
var⁡(y⁢(t))=E⁢[var⁡[y⁢(t)|n⁢(t)]]+var⁡[E⁢[y⁢(t)|n⁢(t)]]
$$



$$
=E⁢[\sigma_{op}^{2}⁢n_{4}⁢(t)+\sigma_{m}^{2}]+var⁡[H_{I}⁢n⁢(t)]
$$



$$
=\sigma_{op}^{2}⁢E⁢[n_{4}⁢(t)]+\sigma_{m}^{2}+(H_{I}⁢P⁢(t)⁢H_{I}^{⊤})_{2,2}
$$

See, Appendix 6 for further details.

### Fluorescence and photon-counting noise

The statistics of photon counts in the fluorescence signal are described by a Poisson distribution with emission rate $\lambda_{Fl}$

$$
y_{Fl}⁢(t)∼Pois⁢(\lambda_{Fl}⁢(t))⁢.
$$

The total emission rate $\lambda_{Fl}$ can be modeled as a weighted sum of the specific emission rates $\lambda_{b}$ of each ligand class ${0,1,2}$. The weights are given by the stoichiometric factors which reflect the number of bound ligands. In order to cast the Poisson distribution into the functional form of the observation model (Equation 41), we invoke the central limit theorem to approximate

$$
y_{Fl}∼Pois(\lambda_{Fl})≈N(\lambda_{Fl}(t),\lambda_{Fl}(t))
$$

The larger $\lambda_{Fl}$ the better is the approximation. We assume, that the confocal volume is equally illuminated. For our model of ligand fluorescence, we assume for a moment that there is no signal coming from ligands in the bulk. We will drop this assumption in the next section. With these assumptions, we arrive at the following observation matrix

$$
H_{binding}:=(0\lambda_{b}2⁢\lambda_{b}2⁢\lambda_{b}0000)
$$

The matrix $H$ aggregates the states into two conductivity classes: non-conducting and conducting and three different fluorescence classes. The first element $(Hn)_{1}$ is the mean fluorescence $\lambda_{Fl}⁢(t)=\lambda_{b}⁢[n_{2}⁢(t)+2⁢(n_{3}⁢(t)+n_{4}⁢(t))]$. The variance-covariance matrix $Σ_{binding}$ can be derived along the same lines using Equation 48. We find

$$
Σ_{binding}⁢(t):=((Hn⁢(t))_{1}000)
$$

Under these assumptions, the observation matrix can be written as follows

$$
H:=(0\lambda_{b}2⁢\lambda_{b}2⁢\lambda_{b}000i)
$$

### Output statistics of a Kalman Filter

with two-dimensional state-dependent noiseNow simultaneously measured current and fluorescence data $y\inℝ^{2}$, obtained by cPCF, are modeled. Thus, the observation matrix fulfills $H\inℝ^{2\timesM}$. One can formulate the observation distribution as

$$
y(t)=Hn(t)+ν_{m}(t)+(ν_{pois}(t)ν_{op}(t))⇔y∼N(Hn(t),Σ(t)).
$$

The vector $ν_{m}$ denotes the experimental noise, with $E⁢[ν_{m}]=0$ and variance given by the diagonal matrix $Σ_{meas}+Σ_{back}$. The second noise term arises from Poisson-distributed photon counting statistics and the open-channel noise. It has the properties

$$
E⁢[(ν_{pois}⁢(t)ν_{op}⁢(t))]=0
$$

and

$$
cov⁡((ν_{pois}⁢(t)ν_{op}⁢(t)),(ν_{pois}⁢(t)ν_{op}⁢(t)))=Σ_{open}⁢(t)+Σ_{binding}⁢(t)⁢.
$$

The matrix $Σ$ is a diagonal matrix. To derive the covariance matrix $cov⁡(y⁢(t))$ we need to additionally calculate $var⁡(y_{fluo}⁢(t))$ and $cov(y_{fluo}(t),y_{patch}(t))$. By the same arguments as above we get

$$
var⁡[y_{fluo}(t)]=E[var⁡(y(t)|n(t))]+var⁡[E(y(t)|n(t)]
$$



$$
=E[\sigma_{back}^{2}+(Hn(t))_{1}]+var(Hn(t))
$$



$$
=\sigma_{back}^{2}+(Hn(t))_{1}+(Hn(t))H^{T})_{1,1}
$$

The cross terms can be calculated by using the law of total covariance

$$
cov⁡(y_{patch},y_{fluo})=E[cov⁡(y_{patch},y_{fluo}|n)]+cov⁡(E(y_{patch}|n),E(y_{fluo}|n))
$$



$$
=0+cov⁡(H_{2,:}⁢n,H_{1,:}⁢n)
$$



$$
=H_{2,:}⁢cov⁡(n,n)⁢H_{1,:}^{⊤}=H_{2,:}⁢P⁢(t)⁢H_{1,:}^{⊤}
$$

yielding the matrix

$$
cov⁡(y,y)=HP⁢(t)⁢H^{⊤}+Σ⁢(t)
$$

We assumed that the Poisson distribution is well captured by the normal approximation. In cPCF data, the ligand binding to only a sub-ensemble of the channels is monitored, which we assume to represent the conducting ensemble such that $N_{ch,FL}=N_{ch,I}$. For real data, further refinement might be necessary to model the randomness of the sub-ensemble in the summed voxels. With the time evolution equations for the mean (Equation 35) and for the covariance matrix Equation 38d as well as with the expressions for the signal variance, we possess all parameters that are needed in the correction equation of the (Kalman, 1960; Anderson and Moore, 2012).

### The correction step

For completeness we write down the correction step (Bayesian update) of the KF, although its derivation can be found in Chen, 2003; Anderson and Moore, 2012; Moffatt, 2007. The mean ensemble state $n⁢(t)$ is corrected by the current data point

$$
n_{posterior}⁢(t)=+n_{prior}⁢(t)+K_{Kal}⁢(y⁢(t)-Hn_{prior}⁢(t))
$$

where Kalman gain matrix $K_{Kal}:=P⁢(t)_{prior}⁢H^{⊤}⁢Σ^{-1}$ evaluates the intrinsic noise against the experimental noise. How precise are my model predictions about $n⁢(t)$ compared with the information gained about $n⁢(t)$ by measuring $y⁢(t)$. The covariance $P⁢(t)$ of the ensemble state $n⁢(t)$ is corrected by

$$
P_{posterior}⁢(t)=P_{prior}⁢(t)-K_{Kal}⁢(HP_{prior}⁢(t)⁢H+Σ⁢(t))⁢K^{⊤}
$$

Equation 58,59, 37 and 38d form the filtering equations which summarize the algorithm. One initialises the first $n⁢(0)$ and $P⁢(0)$ and with an equilibrium assumption.

### Microscopic-reversibility as a hierarchical prior

We applied microscopic-reversibility (Colquhoun et al., 2004) by a hierarchical prior distribution. Usually, micro-reversibility is strictly enforced by setting the product of the rates of the clockwise loop $k_{1},k_{2},k_{3}⁢k_{4}$ equal to the anti-clockwise loop $k_{5},k_{6},k_{7},k_{8}$ and then solving for the desired rate parameter to be replaced. This means that the classical approach can be described by drawing the resulting rate from a Dirac delta distribution prior with

$$
k_{1}∼\delta⁢(k_{1}-\frac{k_{5}⁢k_{6}⁢k_{7}⁢k_{8}}{k_{2}⁢k_{3}⁢k_{4}})
$$

Following Equation 60, we can model microscopic-reversibility with any hierarchical prior distribution whose limit for a vanishing variance is Equation 60. For mathematical convenience, we defined the hierarchical prior by a sharply peaking beta distribution

$$
k_{1}^{⋆}∼beta⁡(100.01,100.01)
$$

and by rescaling and adding an offset

$$
k_{1}=\frac{k_{5}⁢k_{6}⁢k_{7}⁢k_{8}}{k_{2}⁢k_{3}⁢k_{4}}⋅0.995+0.01⋅k_{1}^{⋆}
$$

we derived a conditional prior which allows at maximum a ±0.005 relative deviation from the strict microscopic-reversibility. The ±0.005 micro-reversibility constraint is applied in (Figure 7b–d). In this way, one could model or even test possible small violation of microscopic-reversibility if smaller beta parameters such as $beta⁡(1,1)$ would be chosen.
