# Epidemiological dynamics of Ebola outbreaks

## Authors

- Thomas House<sup>1</sup> †

### Affiliations

1. Warwick Mathematics Institute University of Warwick Coventry United Kingdom
2. Warwick Infectious Disease Epidemiology Research Centre University of Warwick Coventry United Kingdom

† Corresponding author

## Abstract

10.7554/eLife.03908.001 Ebola is a deadly virus that causes frequent disease outbreaks in the human population. In this study, we analyse its rate of new introductions, case fatality ratio, and potential to spread from person to person. The analysis is performed for all completed outbreaks and for a scenario where these are augmented by a more severe outbreak of several thousand cases. The results show a fast rate of new outbreaks, a high case fatality ratio, and an effective reproductive ratio of just less than 1. DOI: http://dx.doi.org/10.7554/eLife.03908.001

## Introduction

Ebola virus disease is an often fatal disease of humans that is not vaccine-preventable and has no specific treatment. A total of 25 outbreaks, believed to have arisen due to zoonotic transmission from wild mammals, have occurred since the first observed cases in humans in 1976 (World Health Organisation, 2014a). The current epidemic is the largest to date (World Health Organisation, 2014b). This gives particular urgency to quantitative estimation of epidemiological quantities relevant to Ebola, such as case fatality ratio, timing of new outbreaks, and the strength of human-to-human transmission.

The most important epidemiological quantity to estimate for an infectious disease is typically the basic reproductive ratio, R0, defined as the expected number of secondary cases produced per primary case early in the epidemic (Diekmann et al., 1990). When R0 is greater than 1, the expectation is that a new epidemic will eventually infect a significant percentage of the population if it is not stopped by interventions or chance extinction; conversely, when R0 is less than 1, chance events may lead to a large number of cases, but these are always expected to be much less numerous than the total population size.

Previous attempts to estimate R0 for Ebola have found values between 1.34 and 3.65 by fitting compartmental epidemic models to the incidence over time of the large outbreaks in the Democratic Republic of Congo in 1995 and Uganda in 2000 (Chowell et al., 2004; Ferrari et al., 2005; Legrand et al., 2007), with similar results obtained for the ongoing outbreak (Althaus, 2014). This leads to the question of why all completed outbreaks numbered at most several hundreds, with the typical answer being that the medical and social response to an outbreak reduces transmission, leading to an effective reproductive ratio Rt<R0 (Chowell et al., 2004; Legrand et al., 2007), although it is also important to note that heterogeneity in transmission can lead to extremely high probabilities of an outbreak becoming extinct even if Rt is slightly greater than 1 (Lloyd-Smith et al., 2005).

## Results

![Figure 1.](https://cdn.elifesciences.org/articles/03908/elife-03908-fig1-v2.jpg)

**Figure 1.:** A shows empirical data and 95% CI (black lines) together with fitted distribution and 95% CI (red lines) for rate of new outbreaks. B shows empirical data and 95% CI (black lines) together with fitted distribution and 95% CI (red lines) for case fatality ratio. C shows the posterior density for rate of new outbreaks λ, while D and E show the posterior density for the beta distribution parameters α and β, respectively.DOI: http://dx.doi.org/10.7554/eLife.03908.003

![Figure 2.](https://cdn.elifesciences.org/articles/03908/elife-03908-fig2-v2.jpg)

**Figure 2.:** (A and B) Model (solid red line) and 95% CI (dash-dot red line) vs data (black circles) and 95% CI (solid black lines) for different axis scales. (C) Posterior for values of the reproductive ratio . (RtD) Posterior for the geometric parameter p.DOI: http://dx.doi.org/10.7554/eLife.03908.004

While the model is designed not to depend explicitly on the temporal dynamics of Ebola virus disease,

![Figure 3.](https://cdn.elifesciences.org/articles/03908/elife-03908-fig3-v2.jpg)

**Figure 3.:** (A) Real-time model simulations, with change in colour denoting a new outbreak. (B) Likelihood contours (black lines and values multiplied by an unimportant constant) together with parameters used to simulate (red cross), showing that the parameters are identifiable from such data.DOI: http://dx.doi.org/10.7554/eLife.03908.005

![Figure 4.](https://cdn.elifesciences.org/articles/03908/elife-03908-fig4-v2.jpg)

**Figure 4.:** (A) Model (solid red line) and 95% CI (dash-dot red line) vs data (black circles) and 95% CI (solid black lines). (B) Posterior for the probability of the large uncertain outbreak. (C) Posterior for values of the reproductive ratio . (RtD) Posterior for the geometric parameter p.DOI: http://dx.doi.org/10.7554/eLife.03908.006

## Discussion

The results obtained point to the following conclusions about Ebola transmission dynamics. (i) The rate of new epidemics and CFR are both high, but with significant variability from outbreak to outbreak. (ii) The effective reproductive ratio Rt for person-to-person transmission is just below 1. (iii) There is extremely large variability in the final size of outbreaks.

It is also important to consider the sensitivity of these conclusions. A larger final size for the current outbreak (but still significantly less than the population size of a country) as suggested by the analysis above will tend to lead to a narrower posterior about a value of Rt closer to 1; this can be understood from general properties of branching processes (Athreya and Ney, 1992). Such a finely tuned constant value of Rt would, however, become increasingly difficult to interpret as a fundamental property of the outbreak and a modelling approach in which Rt was allowed to vary in time—along with the public health and behavioural responses—would be preferred.

Also, it is possible that a number of small outbreaks were not recorded by the WHO. This could be addressed through incorporation of additional variability into the model through introduction of explicit overdispersal parameters as in the study by Lloyd-Smith et al. (Lloyd-Smith et al., 2005) and Blumberg and Lloyd-Smith (Blumberg and Lloyd-Smith, 2013), although for the data currently available there was no strong evidence for overdispersal beyond that implied by the geometric distributions.

All of these conclusions suggest no reason for complacency and give support to appeals for greater resources to respond to the ongoing epidemic (Médecins Sans Frontières, 2014).

## Materials and methods

## Description

In this study, a different approach is taken based on using the time between outbreaks, number of deaths, and final number of cases, for all 24 completed Ebola outbreaks reported by the World Health Organisation (World Health Organisation, 2014a). Full mathematical details of the approach are given below.

First, we model the start of new outbreaks as a ‘memoryless’ Poisson process with a rate λ. Secondly, we assume that each new outbreak has a case fatality ratio (CFR—the probability that a case will die) picked from a beta distribution. Thirdly, the final size model involves two components: (i) a geometrically distributed number of cases, A, which includes cases arising from animal-to-human and pre-control transmission; (ii) a branching process model of human-to-human transmission (Athreya and Ney, 1992; Ball and Donnelly, 1995), whose offspring distribution has mean Rt, generating Z cases. The final size is then K=A+Z|A. This quantity should be interpreted as arising from a combination of Rt, R0, and timing of interventions.

Bayesian MCMC with uninformative priors was used to fit all models (Gilks et al., 1995). Since doubts have been raised in the literature about the use of final size data for emerging diseases (Drake, 2005), a simulation study was also performed to test identifiability, although a recent study by Blumberg and Lloyd-Smith (Blumberg and Lloyd-Smith, 2013) of joint identifiability of two parameters in a related model is also highly relevant in this context.

Finally, the final size data were augmented by an outbreak of unknown size in the range 1000–5000 (with mathematical details given by Equation. (5), below) and the model was refitted. Due to the significant uncertainty in the severity of the current outbreak, this is not intended to be a real-time analysis, but rather to show how the modelling approach responds to such a scenario in general.

## Technical details

## Transmission model

Each outbreak has an initial number of cases A and a secondary number of cases Z. The total outbreak size is K=A+Z|A. We model the number of initial cases as a shifted geometric distribution,(1)Pr[A=a|p]=(1−p)a−1p.

We then model the number of secondary cases as the total progeny of a Galton–Watson branching process with A initial individuals and offspring distribution given by a geometrically distributed random variable ξ with mean Rt≕(1−q)/q. We adapt the results from Ball and Donnelly (Ball and Donnelly, 1995) to our model, giving(2)Pr[Z=z|A=a,q]=aa+z(2z+a−1z)qz+a(1−q)z

This gives a formula for the total size of the outbreak of(3)Pr[K=k|p,q]=∑a=1kPr[A=a|p]Pr[Z=(k−a)|A=a,q].

If the data D consists of a set of ki (which is the size of outbreak i, with N the total number of outbreaks) then the likelihood function for the transmission model is(4)L(D|p,q)=∏iPr[K=ki|p,q].

When the data D′ consists of the set of ki augmented by an outbreak of size between κ1 and κ2, we use likelihood function(5)L(D′|p,q)=L(D|p,q)∑k=κ1κ2 Pr[K=k|p,q].

## New outbreak model

We model the start of new outbreaks in the human population as a Poisson process of rate λ. If the time period over which N outbreaks is observed is T years, then the likelihood is(6)L(D|λ)=(λT)Ne−λTN!.

We estimate λ=0.67[0.45,0.98], with posterior distribution given in Figure 1C. The probability density function for t being the next outbreak time is(7)f(t)=λe−λt,which is shown in Figure 1A.

## Case fatality model

We let Ci be a random variable for the probability of fatality for a given case in outbreak i. We assume a parametric model in which this is drawn from a beta distribution, meaning that the probability density function is(8)Beta(c|α,β)=cα−1(1−c)β−1B(α,β), B(α,β):=∫01xα−1(1−x)β−1dx.

Then if di≤ki is the number of fatalities in outbreak i, treating each fatality as independent, conditioned on infection, gives(9)Pr[di|ki,α,β]=(kidi)B(α+di,β+ki−di)B(α,β).

Then the likelihood is(10)L(D|α,β)=∏iPr[di|ki,α,β].

We estimate α=6.1[2.8,11] and β=3.1[1.5,5.9], with posterior distributions given in Figure 1D,E.

## Statistical methodology

The MCMC methodology used was Random-walk Metropolis–Hastings with thinning to produce 103 uncorrelated samples, with each posterior ultimately derived from one long chain. The parameter spaces involved are low-dimensional enough that large-scale sweeps can be performed to check for multimodality, which was not observed, and convergence of the chains was observed to be fast and independent of initial conditions.

For the simulation study, the real-time incidence curves are produced by modelling the geometric distributions as arising from Poissonian transmission with exponentially distributed rates. The times between new introductions are not explicitly modelled or shown.

## Code

MATLAB code to reproduce the analysis of this paper is available at: https://github.com/thomasallanhouse/elife-ebola-code.
