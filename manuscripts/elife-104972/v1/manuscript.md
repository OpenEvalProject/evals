# A stochastic explanation for observed local-to-global foraging states in Caenorhabditis elegans

## Authors

- Andrew Margolis<sup>1</sup> ([ORCID: 0009-0006-9817-7147](https://orcid.org/0009-0006-9817-7147))
- Andrew Gordus<sup>1</sup> ([ORCID: 0000-0002-5550-0286](https://orcid.org/0000-0002-5550-0286)) †

### Affiliations

1. Department of Biology, Johns Hopkins University Baltimore United States ([ROR:00za53h95](https://ror.org/00za53h95))
2. David Geffen School of Medicine, University of California Los Angeles United States ([ROR:046rm7j60](https://ror.org/046rm7j60))
3. Solomon H. Snyder Department of Neuroscience, Johns Hopkins University Baltimore United States ([ROR:00za53h95](https://ror.org/00za53h95))

† Corresponding author

## Abstract

Abrupt changes in behavior can often be associated with changes in underlying behavioral states. When placed off food, the foraging behavior of C. elegans can be described as a change between an initial local-search behavior characterized by a high rate of reorientations, followed by a global-search behavior characterized by sparse reorientations. This is commonly observed in individual worms, but when numerous worms are characterized, only about half appear to exhibit this behavior. We propose an alternative model that predicts both abrupt and continuous changes to reorientation that do not rely on behavioral states. This model is inspired by molecular dynamics modeling that defines the foraging reorientation rate as a decaying parameter. By stochastically sampling from the time interval probability distribution defined by this rate, both abrupt and gradual changes to reorientation rates can occur, matching experimentally observed results. Crucially, this model does not depend on behavioral states or information accumulation. Even though abrupt behavioral changes do occur, they are not necessarily indicative of abrupt changes in behavioral states, especially when abrupt changes are not universally observed in the population.

## Introduction

The search for food in the absence of informative sensory cues is an essential animal behavior (Reiss and Rankin, 2021). A foraging strategy that is observed in nearly all animals is the Area Restricted Search (ARS) (Dorfman et al., 2022). In ARS, animals randomly forage for food (Codling et al., 2008), but appetitive sensory cues (like an encounter with food) will cause the animal to restrict their search area by reorienting more frequently, thus increasing the likelihood of food encounters. Conversely, when removed from food, animals will decrease their reorientation rate to increase dispersal (Reiss and Rankin, 2021; Klein et al., 2017). Caenorhabditis elegans and Drosophila melanogaster larvae appear to progressively increase their diffusion constant while foraging off of food by decreasing their rates of reorientation (Klein et al., 2017). However, in separate studies (López-Cruz et al., 2019; Calhoun et al., 2014), individual worms appear to make an abrupt change from a high to low rate of reorientation. This behavior has been described as a switch from a local to global search strategy that relies on evidence accumulation to trigger the behavioral switch (Calhoun et al., 2014).

A central challenge with defining these possible state transitions is the stochastic nature of the behavior itself. Reorientations are random and follow Poisson statistics (Pierce-Shimomura et al., 1999; Zhao et al., 2003; Stephens et al., 2011; Flavell et al., 2013; Gordus et al., 2015; Roberts et al., 2016; Iino and Yoshida, 2009). This is very similar to the temporal behavior of individual molecules in solution (Singh et al., 2022). Individual molecules defined by the same reaction kinetics can stochastically produce long or short time intervals between reaction events, not because one molecule is inherently faster than the other, but because they are stochastically sampling from the same probability distribution. The diversity of times between individual worm reorientations is very similar to this. The exponentially decaying reorientation rate emerges from the average of trajectories that do not necessarily conform to this curve individually. However, even those that produce abrupt switches in reorientation rates could still emerge from a simple exponential decay strategy. Since reorientations occur stochastically, the abrupt changes in reorientation rates could simply be the result of stochastic sampling of an underlying decay phenomenon (Srivastava et al., 2009). Here, we show that a simple, stochastic model that does not rely on switches in behavioral state is sufficient to reproduce the reorientation kinetics observed in experimental data.

## Results

### Local-to-global behavioral transitions are inconsistently observed

In López-Cruz et al., 2019, the foraging behaviors of individual worms were tracked for 45 min after being removed from food. As observed previously (Klein et al., 2017), the reorientation rate from this study followed an exponential decay (Figure 1a). It was reported that roughly half the worms appeared to make a sudden single switch from local to global search as observed in Calhoun et al., 2014, however, the other half appeared to produce no discernible change in search strategy or exhibited multiple switches (Figure 1b–d). Whether or not a worm performed a single decision was defined in López-Cruz et al., 2019 by fitting individual reorientation data to two lines using the MATLAB function findchangepts (Figure 1b; Killick et al., 2012). This function divides each trace into two regions that are defined by minimizing the sum of the residual squared error of two local linear regressions. The location of the transition point is varied until the total residual error attains a minimum (Figure 1b). A large change in slope indicates a sudden change in reorientation rate, and the intersection between the two lines determines the decision time (López-Cruz et al., 2019; Figure 1b). A worm was identified as making a sudden local-to-global foraging switch based on visually assessing the magnitude of the slope difference, therefore, the conclusion that 50% of the worms produced a single transition is fairly subjective. To evaluate this property more objectively, we assessed the distributions of slope differences (s1-s2) and transition times to see whether two densities were clearly distinguishable. The resulting distributions for the experimental data were continuous, with no clear boundary between deciders and non-deciders (Figure 1e).

![Figure 1.](https://cdn.elifesciences.org/articles/104972/elife-104972-fig1-v1.jpg)

**Figure 1.:** (a) Average experimental population reorientation rate (black line) in a rolling 2 min window. Blue bins represent probability of observed reorientation rate. (b) Abrupt transitions were identified by performing two linear regressions on observed reorientation curves. Transition times (trans) were defined by the intersection of the regressions (dashed line). The slopes of the two regressions are s1 and s2. (c) An example of an experimental reorientation curve with an abrupt reorientation transition (marked by vertical line). (d) An example of an experimental reorientation curve that lacked an abrupt reorientation transition. (e) Distribution of slope differences and transition times from regressions fit to the experimental data. Individual data points are individual reorientation data for each worm. Insets are individual examples of experimental cumulative reorientation curves. Number of worms (N)=1631. Dashed line represents the median slope difference. All data curated from López-Cruz et al., 2019.

Why do some worms appear to make a decision, while others do not? In aggregate, the reorientation rate decays (Figure 1a). Despite the population average conforming to a gradual decay, individual trajectories produce a wide diversity of trajectories which sometimes conform to an apparent drop in reorientation rate (Figure 1c), while others do not (Figure 1d). If the worms are executing a decision, this would seem to indicate only a fraction of the worms decide to switch from local to global foraging strategies, while others use a different strategy. An alternative hypothesis is that sudden changes in reorientation are random events that do not occur due to an underlying change in strategy, but because of the inherently random nature of the behavior itself (Pierce-Shimomura et al., 1999; Zhao et al., 2003; Stephens et al., 2011; Flavell et al., 2013; Gordus et al., 2015; Roberts et al., 2016; Iino and Yoshida, 2009).

### A stochastic model generates abrupt and gradual changes in search strategy

We tested this hypothesis by modeling individual worms by stochastic sampling of a decaying reorientation rate with the Gillespie algorithm (Figure 2a), a common strategy used to model the kinetics of individual molecules (Gillespie, 1977). With this strategy, the time between chemical events is modeled by randomly sampling from the time-interval distributions defined by the reaction rates. Although the algorithm was originally developed to model discrete molecular events based on known kinetic parameters, it can be used to generate time trajectories for any discrete events when the kinetics are known. A behavioral example of this is the Lotka-Volterra predator-prey competition model where predator and prey populations fluctuate out of phase due to predation. Stochastic fluctuations of predator and prey populations can be modeled using the Gillespie algorithm (Palombi et al., 2020; Reichenbach et al., 2006; Constable and McKane, 2015).

![Figure 2.](https://cdn.elifesciences.org/articles/104972/elife-104972-fig2-v1.jpg)

**Figure 2.:** (a) Outline of the Gillespie algorithm. Step 1: Two random numbers (r1 and r2) are drawn from a uniform distribution [0,1]. Step 2: The time interval for a new event (τ) is randomly assigned based on the total propensities (a0) and r1. Step 3: The event i (either a decay of M (M←M-1) or a new reorientation (Ω←Ω+1)) at t + τ is determined by the probability (P(i)) of the event i occurring. This probability is determined by the relative propensity (ai/a0) of the event i. (b) (Top) The parameters α, β, and γ are assigned based on fitting a decay curve (red) to the observed average reorientation rate (blue). Dashed lines are + and – standard deviation. (Bottom) Average model population reorientation rate (black line) in a rolling 2 min window. Red bins represent the probability of observed reorientation rate. N=1631, α=1.49 min–1, β=0.1937 min–1, γ=0.11 min–1. (c) (Top) An example of a modeled abrupt reorientation transition. (Bottom) An example of a modeled reorientation curve that lacked an abrupt reorientation transition. Red data are cumulative reorientations and orange data are M. (d) Distribution of slope differences and transition times from regressions fit to the experimental (blue) and modeled (red) data. Individual data points are individual reorientation data for experimental (blue) or in silico (red) worms. Insets are individual examples of experimental and modeled cumulative reorientation curves. Dashed line represents the median experimental slope difference. (e) Examples of experimental (blue) and modeled (red) cumulative reorientation curves for individual worms, with similar stochastic dynamics. For each example drawn from experiments (blue), the in silico worm with the highest correlation from N=1631 iterations is shown (red). Sudden changes in rate are indicated with arrows. M for each example is shown in orange. (f) Examples of modeled data when the reorientation rate is constant ($\alpha$=1.5). Sudden changes in rate are indicated with arrows.

Experimentally, reorientation rate is measured as the number of reorientation events that occurred in an observational window. However, these are discrete stochastic events, so we can describe them in terms of propensity, i.e., the probability of observing a transitional event in an infinitesimal time interval dt (in this case, a reorientation) is:

$$
\frac{dP(Ω+1,t)}{dt}=a_{1}P(Ω,t)
$$

Here, Ω is cumulative reorientation number,  P(Ω + 1, t) is the probability of observing Ω + 1 cumulative reorientations at time t (i.e. the probability of observing the number of reorientations advance from Ω to Ω + 1), and a1 is the propensity for this event to occur, i.e., the likelihood that a particular reaction will occur in the next infinitesimal time interval. In bulk chemical kinetics, this is analogous to the rate of the reaction. Observationally, the frequency of reorientations observed decays over time. This means that the propensity is not constant, so we can define the propensity as decaying in time:

$$
a_{1}=\alphae^{−\gammat}+\beta
$$

Where α + β is the initial propensity at t=0, and β is the propensity at t = ∞.

The propensities for the Gillespie algorithm are state-dependent; the algorithm is modeling discrete events based on the current state of the system. A time-varying propensity implies it is coupled to a state variable that is changing in time. Since the propensity a1 decays exponentially, it implies it is coupled to a first-order decay process. We can model this decay as the reorientation propensity coupled to a decaying factor (M):

$$
\frac{dP(M−1,t)}{dt}=a_{2}P(M,t)
$$

Where the propensity of this event (a2) is a first-order decay:

$$
a_{2}=−\gammaM
$$

Since M is a first-order decay process, when integrated, the M observed at time t is:

$$
M(t)=M(0)e^{−\gammat}
$$

We can couple the probability of observing a reorientation to this decay by redefining a1 as:

$$
a_{1}=\frac{\alpha}{M_{0}}M+\beta
$$

In this way, the propensity a1 is explicitly tied to the state M, which is decaying, so that now:

$$
\frac{dP(Ω+1,t)}{dt}=(\alphae^{−\gammat}+\beta)P(Ω,t)
$$

A critical detail should be noted. While reorientations are modeled as discrete events, the amount of M at time t=0 is chosen to be large (M0 ← 1,000), so that over the timescale of 40 minutes, the decay in M is practically continuous. This ensures that sudden changes in reorientation rate are not due to sudden changes in M, but due to the inherent stochasticity of reorientations.

To model both processes, we can create the master equation:

$$
\frac{dP(Ω,M,t)}{dt}=a_{1}P(Ω−1,M,t)−a_{1}P(Ω,M,t)+a_{2}P(Ω,M+1,t)−a_{2}P(Ω,M,t)
$$

Since these are both Poisson processes, the probability density function for a state change i (Ω+1: i=1, M-1: i=2) occurring at time t is:

$$
P(t|a_{i})=a_{i}e^{−a_{i}t}
$$

The probability that a state change will not occur for propensity ai in time interval τ is:

$$
P(t>\tau|a_{i})=\int_{\tau}^{∞}P(t|a_{i})dt=e^{−a_{i}\tau}
$$

The probability that no state changes will occur for ALL propensities in this time interval is:

$$
P(t>\tau|a_{1})P(t>\tau|a_{2})=\prodie^{−a_{i}\tau}=exp[−\tau\sumia_{i}]
$$

We can draw a random number (r1 ∈ [0,1]) that represents the probability of no events in time interval τ, so that this time interval can be assigned by rearranging Equation 11:

$$
\tau←\frac{−ln(r_{1})}{a_{0}}
$$

where:

$$
a_{0}=\sumia_{i}
$$

This is the time interval for any event (Ω+1 or M-1) happening at t + τ. The probability of which event occurs is proportional to its propensity:

$$
P(eventi)=\frac{a_{i}}{a_{0}}
$$

We can draw a second number (r2 ∈ [0,1]) that represents this probability, so that which event occurs at time t + τ is determined by the smallest n that satisfies:

$$
r_{2}⋅a_{0}\leq\sumi=1na_{i}
$$

so that:

$$
eventi←min{n|r_{2}⋅a_{0}\leq\sumi=1na_{i}}
$$

For example, if the propensity a1 is 10% of a0 at time t, then there is a 10% chance that the resulting reaction will occur at time t. The elegant efficiency of the Gillespie algorithm is twofold. First, it models all transitions simultaneously, not separately. Second, it provides floating-point time resolution. Rather than drawing a random number, and using a cumulative probability distribution of interval times to decide whether an event occurs at discrete steps in time, the Gillespie algorithm uses this distribution to draw the interval time itself. The time resolution of the prior approach is limited by step size, whereas the Gillespie algorithm’s time resolution is limited by the floating-point precision of the random number that is drawn.

In this way, the Gillespie algorithm enables the simultaneous modeling of numerous reactions in parallel with machine-precision time resolution. To ensure the reorientation rate itself is a smooth decay, a large value of M is used to approximate a continuous function. The underlying assumptions are:

In our approach, we fit the exponential curve in Equation 2 to the average reorientation rate from the experimental data from López-Cruz (López-Cruz et al., 2019; Figure 2b), and then used these parameters (α, β, γ) to model 1631 individual worms (the same number of animals in the experimental data). Even though the initial average rates of reorientation are ~1.5 events/minute, there is considerable variance in observed initial rates (Figure 1a). To address this variance, starting values of M were assigned based on randomly drawing a rate from the observed experimental rates at t=0, and adjusting M so that the starting rate for that in silico worm j matched the initial rate of the randomly drawn experimental worm:

$$
M_{j}←\frac{M_{0}(r−\beta)}{\alpha}
$$

where r is an initial rate randomly drawn from the experimental data.

In silico reorientation curves generated produced single-transition and multi/absent transition curves, as observed experimentally (Figure 2c). When plotted along with the experimental data, the in silico data produced a distribution of linear regression parameters comparable to the experimental worms (Figure 2d). The simulation was able to produce individual trajectories that demonstrated switching behavior, despite the lack of a switching mechanism in the model (Equations 2 and 3). Furthermore, our model demonstrated a continuum of switching to non-switching behavior that was observed in experimental results (Figure 2d).

The experimental transition distribution was shifted slightly earlier, however, it is important to note that the experimental data were drawn from experiments where 10–15 animals were tracked together. Collisions occurred, but were excluded from analysis, and so would not contribute to this observation. However, in addition to collisions, animals also reorient in response to pheromones when they cross the tracks left by other animals, which is more likely early in the recording when the animals are in close proximity (Hong et al., 2017; Dal Bello et al., 2021). This, in turn, may contribute to a higher initial rate early in the experimental observations, which would delay the observed decay in reorientations. Since this dataset does not have information about when and where worms crossed pheromone tracks from other animals, this effect cannot be excluded.

This exception aside, modeling worm foraging behavior with a simple exponential decay of reorientations was sufficient to capture most experimentally observed dynamics, both switch and non-switch-like. Sudden switches between fast and slow reorientation rates were observed in both the experimental and modeled data (Figure 2e), despite the model not relying on a switch strategy, and the decay in M being continuous. Sometimes the experimental data produced switch-like behavior (Figure 2e, upper left panel), while other times the reorientation rate appeared to be constant (Figure 2e, lower right panel). The stochastic model produced reorientation data with similar dynamics, despite not relying on a decision paradigm.

It is important to emphasize that the model was not explicitly designed to match the sudden changes in reorientation rates observed in the experimental data. Kinetic parameters were simply chosen to match the average population behavior. Sudden changes in reorientation rate were not due to sudden changes in the underlying model; stochastic behavior naturally produces sudden bunching of random events. Even if the reorientation rate is set to a constant value, stochastic sampling will still produce sudden changes in rate, even though the rate has no time-dependence (Figure 2f).

### Discrete changes in M are inconsistent with experimental data

A large initial value for M0 (M0=1000) was initially chosen to ensure a smooth change in reorientation rate, so that sudden changes in reorientation number were not necessarily due to sudden changes in M. To test how sensitive the model was to stochastic changes in M, the initial value of M was tested at M0=1000, 100, 10, or 1. On average, all values of M0 were sufficient to reproduce the average reorientation decay observed in experimental data (Figure 3a). The distributions of transition times and slope differences were also comparable for M0=1000, 100, or 10, indicating that the model is not particularly sensitive to initial values of M0.

![Figure 3.](https://cdn.elifesciences.org/articles/104972/elife-104972-fig3-v1.jpg)

**Figure 3.:** (a) Average reorientation rates for experiments (blue), and models where M0=1000 (red), M0=100 (plum), M0=10 (magenta), or M0=1 (cyan). Dashed lines indicate standard deviation. (b) Distribution of slope differences and transition times from regressions fit to the experimental data (blue), and models where M0=1000 (red), M0=100 (plum), M0=10 (magenta), or M0=1 (cyan). Number of worms for both experiment and models (N)=1631. Dashed line represents the median slope difference for the experimental data. (c) The Jensen-Shannon divergence between the experimental distribution for slope difference and transition time in (b), and the distributions generated from models where M0=1,000 (red), M0=100 (plum), M0=10 (magenta), or M0=1 (cyan). Twenty distributions were generated for each M0 model. Quartiles represented by box and whiskers. P-values calculated using Tukey’s range test: <0.001: ***.

However, despite producing a similar average decay in reorientation rates, the distribution of slope differences was distinctly bimodal for M0=1 (Figure 3b). This was not surprising, since when M0=1, the model is by definition a two-state system. Either the worm has a reorientation rate of α+β (M=1), or a reorientation rate of β (M=0). The probability of switching from M=1 to M=0 increases with a timescale of γ (γ=0.11 min–1). The bimodal slope and transition time distributions for M0=1 were distinctly different from those observed for the experimental or M0=1000, 100, 10 models.

Since the slope and transition time distributions were generated from a recursive algorithm rather than a purely analytical model, the model distribution for these metrics was compared to the experimental distribution using the Jensen-Shannon divergence (JSD):

$$
JSD(P||Q)=\frac{1}{2}D(P||M)+\frac{1}{2}D(Q||M)
$$

where D is the Kullback-Leibler divergence:

$$
D(P‖Q)=\sumxP(x)ln⁡(\frac{P(x)}{Q(x)})
$$

and P(x) and Q(x) are the two probability distributions being compared. M(x) is a mixture distribution of P and Q. This metric provides a useful, parameter-free measure for comparing distributions using mutual information. A short distance between two distributions indicates they are more similar than two distributions separated by a longer distance.

To compare how similar the different models (M0=1000, 100, 10, 1) compared to the experimental distribution of transition times and slope differences, we ran the model twenty times for each M0, and calculated the JSD between the model and experimental distributions (Figure 3c). The non-binary models (M0≠ 1) all produced comparable distances, but the binary models (M0=1) were significantly more distant than the rest, indicating this model was more dissimilar than the others when compared to the experimental data. A continuous decline in reorientation rate is more consistent with experimental observations than a discrete change in reorientation rate.

## Discussion

The lack of a decision simplifies the dispersal strategy for C. elegans. Rather than relying on the accumulation of evidence to make a discrete decision, the worm relies on a decaying signal in the absence of food that drives the reorientation rate. This strategy increases the diffusion constant of the worm, and ensures a more efficient search strategy to find food (Klein et al., 2017). The stochastic nature of this search is consistent with prior characterizations of worm behavior and neuronal dynamics (Pierce-Shimomura et al., 1999; Zhao et al., 2003; Stephens et al., 2011; Flavell et al., 2013; Gordus et al., 2015; Roberts et al., 2016; Iino and Yoshida, 2009), and implies that any individual worm would exhibit all the variability of the population if allowed to perform this task multiple times. We consider this to be a null model: simple stochastic models should be sufficient to explain observable stochastic behaviors.

The decay in M can be considered the memory timescale of the last food encounter. With an observed γ of 0.07 min–1, this would mean a memory τ1/2 of ~10 min. In principle, M should rise in the presence of food to increase the reorientation rate, on a timescale that is not addressed here. In López-Cruz et al., 2019, the starting reorientation rate correlated with food density prior to food removal, which would be consistent with the amplitude of M correlating with food density/quality. The reliance of the reorientation rate while foraging for food on a decaying factor (M) implies that the rate is influenced by a signaling factor which decays in time. It is well established that the reorientation rate is influenced by numerous signaling factors and is the basis of the biased random walk that drives taxis in shallow gradients (Pierce-Shimomura et al., 1999; Zhao et al., 2003; Stephens et al., 2011; Flavell et al., 2013; Gordus et al., 2015; Roberts et al., 2016; Iino and Yoshida, 2009).

A decay in reorientation rate, rather than a sudden change, is consistent with observations made by López-Cruz et al., 2019. They found that the neurons AIA and ADE redundantly suppress reorientations, and that silencing either one was sufficient to restore the large number of reorientations during early foraging. This implies that the timescale of the variable M may represent the timescales of AIA and ADE activities. AIA and ADE synapse onto several neurons that drive reorientations (López-Cruz et al., 2019; Gray et al., 2005), and their output was inhibited over long timescales (tens of minutes) by presynaptic glutamate binding to MGL-1, a slow G-protein coupled receptor expressed in AIA and ADE. Their results support a model where sensory neurons suppress the synaptic output of AIA and ADE, which in turn leads to a large number of reorientations early in foraging. As time passes, glutamatergic input from the sensory neurons decreases, which leads to disinhibition of AIA and ADE and a subsequent suppression of reorientations.

The sensory inputs into AIA and ADE are sequestered into two separate circuits, with AIA receiving chemosensory input and ADE receiving mechanosensory input. Since the suppression of either AIA or ADE is sufficient to increase reorientations, the decay in reorientations is likely due to the suppression of both of these neurons decaying in time. This correlates with an observed decrease in sensory neuron activity as well, so the timescale of reorientation decay could be tied to the timescale of sensory neuron activity, which in turn is influencing the timescale of AIA/ADE reorientation suppression. This implies that our factor ‘M’ is likely the sum of several different sensory inputs decaying in time.

The molecular basis of which sensory neuron signaling factors contribute to decreased AIA and ADE activity is made more complicated by the observation that the glutamatergic input provided by the sensory neurons was not essential, and that additional factors besides glutamate contribute to the signaling to AIA and ADE. In addition to this, it is not simply the sensory neuron activity that decays in time, but also the sensitivity of AIA and ADE to sensory neuron input that decays in time. Simply depolarizing sensory neurons after the animals had starved for 30 min was insufficient to rescue the reorientation rates observed earlier in the foraging assay. This observation could be due to decreased presynaptic vesicle release and/or decreased receptor localization on the postsynaptic side.

In summary, there are two neuronal properties that appear to be decaying in time. One is sensory neuron activity, and the other is decreased potentiation of presynaptic input onto AIA and ADE. Our factor ‘M’ is a phenomenological manifestation of these numerous decaying factors. Altered ionotropic glutamate signaling and dopamine release also influence foraging kinetics (Hills et al., 2004), as well as neuropeptides (Campbell et al., 2016). The signaling factor M could be the result of one or all of these factors decaying in time. Further work will be needed to reveal how the kinetics of reorientations emerge explicitly from these underlying signaling kinetics.
