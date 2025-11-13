# Optimal plasticity for memory maintenance during ongoing synaptic change

## Authors

- Dhruva V Raman<sup>1</sup> ([ORCID: 0000-0002-8992-1353](https://orcid.org/0000-0002-8992-1353)) †
- Timothy O'Leary<sup>1</sup> ([ORCID: 0000-0002-1029-0158](https://orcid.org/0000-0002-1029-0158)) †

### Affiliations

1. Department of Engineering, University of Cambridge Cambridge United Kingdom

† Corresponding author

## Abstract

Synaptic connections in many brain circuits fluctuate, exhibiting substantial turnover and remodelling over hours to days. Surprisingly, experiments show that most of this flux in connectivity persists in the absence of learning or known plasticity signals. How can neural circuits retain learned information despite a large proportion of ongoing and potentially disruptive synaptic changes? We address this question from first principles by analysing how much compensatory plasticity would be required to optimally counteract ongoing fluctuations, regardless of whether fluctuations are random or systematic. Remarkably, we find that the answer is largely independent of plasticity mechanisms and circuit architectures: compensatory plasticity should be at most equal in magnitude to fluctuations, and often less, in direct agreement with previously unexplained experimental observations. Moreover, our analysis shows that a high proportion of learning-independent synaptic change is consistent with plasticity mechanisms that accurately compute error gradients.

## Introduction

Learning depends upon systematic changes to the connectivity and strengths of synapses in neural circuits. This has been shown across experimental systems (Moczulska et al., 2013; Lai et al., 2012; Hayashi-Takagi et al., 2015) and is assumed by most theories of learning (Hebb, 1949; Bienenstock et al., 1982; Gerstner et al., 1996).

Neural circuits are required not only to learn, but also to retain previously learned information. One might therefore expect synaptic stability in the absence of an explicit learning signal. However, many recent experiments in multiple brain areas have documented substantial ongoing synaptic modification in the absence of any obvious learning or change in behaviour (Attardo et al., 2015; Pfeiffer et al., 2018; Holtmaat et al., 2005; Loewenstein et al., 2015; Yasumatsu et al., 2008; Loewenstein et al., 2011).

This ongoing synaptic flux is heterogeneous in its magnitude and form. For instance, the expected lifetime of dendritic spines in mouse CA1 hippocampus has been estimated as 1–2 weeks (Attardo et al., 2015). Elsewhere in the brain, over 70% of spines in mouse barrel cortex are found to persist for 18 months (Zuo et al., 2005), although these persistent spines exhibited large deviations in size over the imaging period (on average, a >25% deviation in spine head diameter).

The sources of these ongoing changes remain unaccounted for, but are hypothesised to fall into systematic changes associated with learning, development and homeostatic maintenance, and unsystematic changes due to random turnover (Rule et al., 2019; Mongillo et al., 2017; Ziv and Brenner, 2018). A number of experimental studies have attempted to disambiguate and quantify the contributions of different biological processes to overall synaptic changes, either by directly interfering with synaptic plasticity, or by correlating changes to circuit-wide measurements of ongoing physiological activity (Nagaoka et al., 2016; Quinn et al., 2019; Yasumatsu et al., 2008; Minerbi et al., 2009; Dvorkin and Ziv, 2016). Consistently, these studies find that the total rate of ongoing synaptic change is reduced by only 50% or less in the absence of neural activity or when plasticity pathways are blocked.

Thus, the bulk of steady-state synaptic changes seem to arise from fluctuations that are independent of activity patterns at pre/post synaptic neurons or known plasticity induction pathways. As such, it seems unlikely that their source is some external learning signal or internal reconsolidation mechanism. This is surprising, because maintenance of neural circuit properties and learned behaviour would intuitively require changes across synapses to be highly co-ordinated. To our knowledge, there is no theoretical account or model prediction that explains these observations.

One way of reconciling stable circuit function with unstable synapses is to assume that ongoing synaptic changes are localised to ‘unimportant’ synapses, which do not affect circuit function. While this may hold in particular circuits and contexts (Mongillo et al., 2017), at least some of the ongoing synaptic changes are likely associated with ongoing learning, which must somehow affect overall circuit function to be effective (Rule et al., 2020). Furthermore, this model does not account for the dominant contribution of fluctuations among those synapses that do not remain stable over time.

In this work we explore another, non-mutually exclusive hypothesis that active plasticity mechanisms continually maintain the overall function of a neural circuit by compensating changes that degrade memories and learned task performance. This fits within the broad framework of memory maintenance via internal replay and reconsolidation, a widely hypothesised class of mechanisms for which there is widespread evidence (Carr et al., 2011; Foster, 2017; Nader and Einarsson, 2010; Tronson and Taylor, 2007).

Compensatory plasticity can be induced by external reinforcement signals (Kappel et al., 2018), interactions between different brain areas and circuits (Acker et al., 2018), or spontaneous, network-level reactivation events (Fauth and van Rossum, 2019). Either way, we can conceptually divide plasticity processes into two types: those that degrade previously learned information, and those that protect against such degradation. We will typically refer to memory-degrading processes as ‘fluctuations’. While these may be stochastic in origin, for example due to intrinsic molecular noise in synapses, we do not demand that this is the case. Fluctuations will therefore account for any synaptic change, random or systematic, that disrupts stored information.

The central question we address in this work is how compensatory plasticity should act in order to optimally maintain stored information at the circuit level, in the presence of ongoing synaptic fluctuations. To do this, we develop a general modelling framework and conduct a first-principles mathematical analysis that is independent of specific plasticity mechanism and circuit architectures. We find that the rate of compensatory plasticity should not exceed that of the synaptic fluctuations, in direct agreement with experimental measurements. Moreover, fluctuations should dominate as the precision of compensatory plasticity mechanisms increases, where ‘precision’ is defined as the quality of approximation of an error gradient. This provides a potential means of accounting for differences in relative magnitudes of fluctuations in different neural circuits. We validate our theoretical predictions through simulation. Together, our results explain a number of consistent but puzzling experimental findings by developing the hypothesis that synaptic plasticity is optimised for dynamic maintenance of learned information.

## Results

### Review of key experimental findings

To motivate the main analysis in this paper we begin with a brief survey of quantitative, experimental measurements of ongoing synaptic dynamics. These studies, summarised in Table 1, provide quantifications of the rates of systematic/activity-dependent plasticity relative to ongoing synaptic fluctuations.

**Table 1.**
 Synaptic plasticity rates across experimental models, and the effect of activity suppression.


<table>
  <thead>
    <tr>
      <th>Reference</th>
      <th>Experimental system</th>
      <th>Total baseline synaptic change</th>
      <th>% synaptic change that is activity / learning-independent</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Pfeiffer et al., 2018</td>
      <td>Adult mouse hippocampus</td>
      <td>40% turnover over 4 days</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>Loewenstein et al., 2011</td>
      <td>Adult mouse auditory cortex</td>
      <td>&gt;70% of spines changed size by &gt;50% over 20 days</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>Zuo et al., 2005</td>
      <td>Adult mouse (barrel, primary motor, frontal) cortex</td>
      <td>3–5% turnover over 2 weeks for all regions. 73.9 ± 2.8% of spines stable over 18 months (barrel cortex)</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>Nagaoka et al., 2016</td>
      <td>Adult mouse visual cortex</td>
      <td>8% turnover per 2 days in visually deprived environment. 15% in visually enriched environment. 7–8% in both environments under pharmacological suppression of spiking.</td>
      <td>≈50% (turnover)</td>
    </tr>
    <tr>
      <td>Quinn et al., 2019</td>
      <td>Glutamatergic synapses, dissociated rat hippocampal culture</td>
      <td>28 ± 3.7% of synapses formed over 24 hr period. 28.6 ± 2.3% eliminated. Activity suppression through tetanus neurotoxin -light chain. Plasticity rate unmeasured.</td>
      <td>≈75% (turnover)</td>
    </tr>
    <tr>
      <td>Yasumatsu et al., 2008</td>
      <td>CA1 pyramidal neurons, primary culture, rat hippocampus</td>
      <td>Measured rates of synaptic turnover and spine-head volume change. Baseline conditions vs activity suppression (NMDAR inhibitors). Turnover rates: 32.8 ± 3.7% generation/elimination per day (control) vs 22.0 ± 3.6% (NMDAR inhibitor). Rate of spine-head volume change:</td>
      <td>≈67±17% (turnover). Size-dependent, but consistently &gt;50% (spine-head volume)</td>
    </tr>
    <tr>
      <td>Dvorkin and Ziv, 2016</td>
      <td>Glutamatergic synapses in cultured networks of mouse cortical neurons</td>
      <td>Partitioned commonly innervated (CI) synapses sharing same axon and dendrite, and non-CI synapses. Quantified covariance in fluorescence change for CI vs non-CI synapses to estimate relative contribution of activity histories to synaptic remodelling</td>
      <td>62–64% (plasticity)</td>
    </tr>
    <tr>
      <td>Minerbi et al., 2009</td>
      <td>Rat cortical neurons in primary culture</td>
      <td>Created ‘relative synaptic remodeling measure’ (RRM) based on frequency of changes in the rank ordering of synapses by fluorescence. Compared baseline RRM to when neural activity was suppressed by tetrodotoxin (TTX). RRM: 0.4 (control) vs 0.3 (TTX) after 30 hr.</td>
      <td>≈75% (plasticity)</td>
    </tr>
    <tr>
      <td>Kasthuri et al., 2015</td>
      <td>Adult mouse neocortex (Three-dimensional post mortem reconstruction using electron microscopy).</td>
      <td>Data on 124 pairs of ‘redundant’ synapses sharing a pre/post-synaptic neuron was analysed in Dvorkin and Ziv, 2016. They calculated the correlation coefficient of spine volumes and post-synaptic density sizes between redundant pairs. This should be one if pre/post-synaptic activity history perfectly explains these variables.</td>
      <td>77% (post-synaptic density, r2=0.23). 66% (spine volume, r2=0.34)</td>
    </tr>
    <tr>
      <td>Ziv and Brenner, 2018</td>
      <td>Literature review across multiple systems</td>
      <td>‘Collectively these findings suggest that the contributions of spontaneous processes and specific activity histories to synaptic remodeling are of similar magnitudes’</td>
      <td>≈50%</td>
    </tr>
  </tbody>
</table>

We focused on studies that measured ‘baseline’ synaptic changes that occur outside of any behavioural learning paradigm, and which controlled for stimuli that may induce widespread changes in synaptic strength. The approaches fall into two categories:

The studies in Table 1 consistently report that the the main component (more than 50%) of baseline synaptic dynamics is due to synaptic fluctuations that are independent of neural activity and/or easily identifiable plasticity signals. This is surprising because such a large contribution of fluctuations might be expected to disrupt circuit function. A key question that we address in this study is whether such a large relative magnitude of fluctuations can be accounted for from first principles, assuming that neural circuits need to protect overall function against perturbations.

The hypothesis we assumed is that some active plasticity mechanism compensates for the degradation of a learned memory trace or circuit function caused by ongoing synaptic fluctuations. We will thus express overall plasticity as a combination of synaptic fluctuations (task-independent processes that degrade memory quality) and compensatory plasticity, which counteracts this effect. There are various ways such a compensatory mechanism might access information on the integrity of overall circuit function, memory quality or ’task performance’. It could use external reinforcement signals (Kappel et al., 2018; Rule et al., 2020). Alternatively, such information could come from another brain region, as hypothesised in for example Acker et al., 2018, where cortical memories are stabilised by hippocampal replay events. Spontaneous, network-level reactivation events internal to the neural circuit itself could also plausibly induce performance-increasing plasticity (Fauth and van Rossum, 2019). Regardless, the decomposition of total ongoing plasticity into fluctuations and systematic plasticity allows us to derive relationships between both that are independent of the underlying mechanisms, which are not the focus of this study.

We must acknowledge that it is difficult, experimentally, to pin down and control for all physiological factors that regulate synaptic changes, or indeed to measure such changes accurately. However, even if one does not take the observations in Table 1 – or their interpretation – at face value, the conceptual question we ask remains relevant for any neural circuit that needs to retain information in the face of ongoing synaptic change.

### Modelling setup

Suppose a neural circuit is maintaining previously learned information on a task. The circuit is subject to task-independent synaptic fluctuations which can degrade the quality of learned information. Meanwhile, some compensatory plasticity mechanism counteracts this degradation. Throughout this paper, we treat ‘memory’ and ‘task performance’ as interchangeable because our framework analyses the effect of synaptic weight change on overall circuit function. In this context, we ask:

if a network optimally maintains learned task performance, what rate of compensatory plasticity is required relative to the rate of synaptic fluctuations?

By ‘rate’ we mean magnitude of change in a given time interval. Our setup is depicted in Figure 1. We make the following assumptions, which are also stated mathematically in Box 1:

![Figure 1.](https://cdn.elifesciences.org/articles/62912/elife-62912-fig1-v2.jpg)

**Figure 1.:** (a) We consider a network attempting to retain previously learned information that is subject to ongoing synaptic changes due to synaptic fluctuations and compensatory plasticity. (b) Simulations performed in this study use an abstract, rate based neural network (described in section Motivating example). The rate of synaptic fluctuations is constant over time. By iteratively increasing the compensatory plasticity rate in steps we observe a ‘sweet-spot’ compensatory plasticity rate, which is lower than that of the synaptic fluctuations, and which best controls task error. (c) A snapshot of the simulation described in b, at the point where the rates of synaptic fluctuations and compensatory plasticity are matched. Even as task error fluctuates around a mean value, individual weights experience systematic changes.

The magnitude and direction of plasticity may or may not change continually over time. Correspondingly, we may pick an appropriately small time interval, $Δ⁢t$, (which is not necessarily infinitesimally small) over which the directions of plasticity can be assumed constant, and write

$$
Δ⁢𝐰⁢(t)=Δ⁢𝐜⁢(t)+Δ⁢ϵ⁢(t),
$$

where for any time-dependent variable $x⁢(t)$, we use the notation $Δ⁢x⁢(t):=x⁢(t+Δ⁢t)-x⁢(t)$. We regard $Δ⁢𝐜⁢(t)$ and $Δ⁢ϵ⁢(t)$ as coming from unknown probability distributions, which obey the following constraints:

### Motivating example

Having described a generic modelling framework, we next uncover a key observation using a simple simulation.

Figure 1 depicts an abstract, artificial neural network trying to maintain a given input-output mapping over time, which is analogous to preservation of a memory trace or learned task. At every timestep, synaptic fluctuations corrupt the weights, and a compensatory plasticity mechanism acts to reduce any error in the input-output mapping (see Equation (1)). We fix the rate (i.e. magnitude per timestep) of synaptic fluctuations throughout. We increase the compensatory plasticity rate in stages, ranging from a level far below the synaptic fluctuation rate, to a level far above it. Each stage is maintained so that task error can settle to a steady state.

Two interesting phenomena emerge. The task error of the network is smallest when the compensatory plasticity rate is smaller than the synaptic fluctuation rate (Figure 1b). Meanwhile, individual weights in the network continually change even as overall task error remains stable due to redundancy in the weight configuration (Figure 1c), (see e.g. Rule et al., 2019 for a review).

In this simple simulation, we made a number of arbitrary and non-biologically motivated choices. In particular, we used an abstract, rate-based network, and synthesised compensatory plasticity directions using the biologically questionable backpropagation rule (see Materials and methods for full simulation details). Nevertheless, Figure 1 highlights a phenomenon that we claim is more general:

The ‘sweet-spot’ compensatory plasticity rate that leads to optimal, steady-state retention of previously learned information is at most equal to the rate of synaptic fluctuations, and often less.

In the remainder of the results section, we will build intuition as to when and why this claim holds. We will also explore factors influence the precise ‘sweet-spot’ compensatory plasticity rate.

### The loss landscape

In order to analyse a general learning scenario that can accommodate biologically relevant assumptions about synaptic plasticity, we will develop a few general mathematical constructs that will allow us to draw conclusions about how synaptic weights affect the overall function of a network.

We first describe the ‘loss landscape’: a conceptually useful, geometrical visualisation of task error $F⁢[𝐰]$ (see also Figure 2). Every point on the landscape corresponds to a different network state $𝐰$. Whereas any point on a standard three-dimensional landscape has two lateral (xy) co-ordinates, any point on the loss landscape has $N$ co-ordinates representing each synaptic strength. Plasticity changes $𝐰$, and thus corresponds to movement on the landscape. Any movement $Δ⁢𝐰$ has both a direction $Δ⁢𝐰^$ (where hats denote normalised vectors), and a magnitude $∥Δ⁢𝐰∥_{2}$. Meanwhile, the elevation of a point $𝐰$ on the landscape represents the degree of task error, $F⁢[𝐰]$. Compensatory plasticity improves task error, and thus moves downhill, regardless of the underlying plasticity mechanism.

![Figure 2.](https://cdn.elifesciences.org/articles/62912/elife-62912-fig2-v2.jpg)

**Figure 2.:** (a) Task error is visualised as the height of a ‘landscape’. Lateral co-ordinates represent the values of different synaptic strengths (only two are visualisable in 3D). Any point on the landscape defines a network state, and the height of the point is the associated task error. Both compensatory plasticity and synaptic fluctuations alter network state, and thus task error, by changing synaptic strengths. Compensatory plasticity reduces task error by moving ‘downwards’ on the landscape. (b) Eventually, an approximate steady state is reached where the effect of the two competing plasticity sources on task error cancel out. The synaptic weights wander over a rough level set of the landscape. (c) The effect of synaptic fluctuations on task error depends on local curvature in the landscape. Top: a flat landscape without curvature. Even though the landscape is sloped, synaptic fluctuations have no effect on task error in expectation: up/downhill directions are equally likely. Bottom: Although up/downhill synaptic fluctuations are still equally likely, most directions are upwardly curved. Thus, uphill directions increase task error more, and downhill directions decrease task error less. So in expectation, synaptic fluctuations wander uphill.

### Understanding curvature in the loss landscape

Intuitively, one would expect task-independent synaptic fluctuations to increase task error. This is true even if fluctuations are unbiased in moving in an uphill or downhill direction on the loss landscape (see Equation (3a)) due to the curvature of the landscape (see Figure 2C). For instance, the slope (mathematically represented by the gradient $\nabla⁡F⁢[𝐰]$) at the bottom of a valley is zero. However, every direction is positively curved, and thus moves uphill. More generally, consider a fluctuation that is unbiased in selecting uphill or downhill directions, at a network state $𝐰$. The fluctuation will increase task error in expectation if the total curvature of the upwardly curved directions at $𝐰$ exceeds that of the downwardly curved directions, as illustrated in Figure 2c. We refer to such a state as partially trained. If all directions are upwardly curved, such as at/near the bottom of a valley, we refer to the state as highly trained. Mathematical definitions for these terms are provided in Box 2.

Comparison of the upward curvature of different plasticity directions plays an important role in the remainder of the section. Therefore, we introduce the following operator:

$$
Q_{w}[v]=v^^{T}∇^{2}F[w]v^.
$$

$Q_{𝐰}⁢[𝐯]$ is mathematical shorthand for the degree of curvature in the direction $𝐯$, at point $𝐰$ on the loss landscape, and is depicted in Figure 3a. Note that $Q_{𝐰}⁢[𝐯]$ depends solely upon the direction, and not the magnitude, of $𝐯$.

![Figure 3.](https://cdn.elifesciences.org/articles/62912/elife-62912-fig3-v2.jpg)

**Figure 3.:** (a) Geometrical intuition behind the operator $Q_{𝐰}$. The operator charts the degree to which a (normalised) direction is upwardly curved (i.e. lifts off the tangent plane depicted in grey). The red, shaded areas filling the region between the tangent plane and the upwardly curved directions are proportional to $Q_{𝐰}⁢[v_{1}]$, and $Q_{𝐰}⁢[v_{2}]$, respectively. (b) Compensatory plasticity points in a direction of locally decreasing task-error. Excessive plasticity in this direction can be detrimental, due to upward curvature (‘overshoot’). The optimal magnitude for a given direction is smaller if upward curvature (i.e. the $Q$-value) is large, as for cases (i) and (ii), and if the initial slope is shallow, as for case (ii). It is greater if the initial slope is steep, as for case (iii). This intuition underlies Equation (6) for the optimal magnitude of a given compensatory plasticity direction, which includes as a coefficient the ratio of slope to curvature. (c) Equation (11) depends upon the ratio of the upward curvatures in the two plasticity directions, $Δ⁢𝐜$, and $Δ⁢ϵ$. As illustrated, steep downhill directions often exhibit more upward curvature than arbitrary directions. In such cases, the optimal magnitude of compensatory plasticity should be outcompeted by synaptic fluctuations.

### An expression for the optimal degree of compensatory plasticity during learning

The rates of compensatory plasticity and synaptic fluctuations, at time $t$, are $𝐜˙⁢(t)$ and $ϵ˙⁢(t)$, respectively. These rates may change continually over time. Let’s temporarily assume they are fixed over a small time interval $[t,t+Δ⁢t]$. Thus,

$$
Δc=c˙(t)ΔtΔϵ=ϵ˙(t)Δt.
$$

What magnitude of compensatory plasticity, $∥Δ⁢𝐜∥_{2}$, most decreases task error over $Δ⁢t$? The answer is

$$
‖Δc‖_{2}^{∗}=\frac{−Δc^^{T}∇F^[w]}{Q_{w}[Δc]}‖∇F[w]‖_{2}.
$$

A mathematical derivation is contained in Box 3, with geometric intuition in Figure 3b. Note that our answer turns out to be independent of the synaptic fluctuation rate $ϵ˙⁢(t)$. Here,

For now, Equation (6) is valid only if the compensatory plasticity direction is fixed during $Δ⁢t$. If we want Equation (6) to also be compatible with continually changing compensatory plasticity directions, it needs to be valid for an arbitrarily small $Δ⁢t$. However, enacting a non-negligible magnitude $∥Δ⁢𝐜∥_{2}^{*}$ of plasticity over an arbitrarily small time interval $Δ⁢t$ would require an unattainable, ‘infinitely-fast’ plasticity rate.

In fact, we show in the next section that our expression for $∥Δ⁢𝐜∥_{2}^{*}$ does become compatible with continuously changing plasticity at the end of learning, when task-error is stable.

### Characterising the optimal rate of compensatory plasticity at steady state

Consider a scenario where task error is approximately stable. In this case, $Δ⁢F≈0$ over $Δ⁢t$. In this scenario, Equation (6) simplifies to

$$
\frac{‖Δc‖_{2}^{∗2}}{‖Δϵ‖_{2}^{2}}=\frac{Q_{w}[Δϵ]}{Q_{w}[Δc]},
$$

as derived in Box 4 and illustrated geometrically in Figure 3c. We see that the magnitude $∥Δ⁢𝐜∥_{2}^{*}$ is proportional to $∥Δ⁢ϵ∥_{2}$, which is itself proportional to $Δ⁢t$ from Equation (5), given some fixed rate of synaptic fluctuations. Thus, $∥Δ⁢𝐜∥_{2}^{*}$ is attainable even as $Δ⁢t$ shrinks to zero, and is thus compatible with continually changing compensatory plasticity directions. In this case, Equation (9) can be rewritten as

$$
\frac{‖c˙(t)‖_{2}^{∗,2}}{‖ϵ˙(t)‖_{2}^{2}}=\frac{Q_{w}[ϵ˙(t)]}{Q_{w}[c˙(t)]}.
$$

Equation (9) is a key result of the paper. It applies regardless of the underlying plasticity mechanisms that induced $Δ⁢𝐜$ and $Δ⁢ϵ$. It is compatible with continually or occasionally changing directions of compensatory plasticity (i.e. infinitesimal or non-infinitesimal $Δ⁢t$). It says that the optimal compensatory plasticity rate, relative to the rate of synaptic fluctuations, depends on the relative upward curvature of these two plasticity directions on the loss landscape.

A corollary is that the optimal rate of compensatory plasticity is greater during learning than at steady state. If we substitute the steady-state requirement: $𝔼⁢[Δ⁢F]=0$, with the condition for learning: $𝔼⁢[Δ⁢F]<0$, in the derivation of Box 4, then we get

$$
\frac{‖Δc‖_{2}^{∗2}}{‖Δϵ‖_{2}^{2}}\geq\frac{Q_{w}[Δϵ]}{Q_{w}[Δc]}.
$$

Indeed, the faster the optimal potential learning rate $𝔼⁢[Δ⁢F]$, the greater the optimal compensatory plasticity rate. Thus $∥Δ⁢𝐜∥_{2}^{*}$ decreases as learning slows to a halt, eventually reaching the level of Equation (9b).

#### Main claim

We now claim that generically, the optimal compensatory plasticity rate should not outcompete the rate of synaptic fluctuations at steady state error. We will first provide geometric intuition for our claim, before bolstering with analytical arguments and making precise our notion of ‘generically’.

From Equation (9), our main claim holds if

$$
Q_{w}[Δc]\geqQ_{w}[Δϵ],
$$

that is, $Δ⁢𝐜$ points in a more upwardly curved direction than $Δ⁢ϵ$. When would this be true?

First consider $Δ⁢ϵ$. Statistical independence from the task error means it should point in an ‘averagely’ curved direction. Mathematically (see SI secton 2.1), this means

$$
E[Q_{w}[Δϵ]]=\frac{Tr(∇^{2}F[w])}{N}.
$$

Our assumption of ‘average’ curvature fails if synaptic fluctuations are specialised to ‘unimportant’ synapses whose changes have little effect on task error. In this case $Q_{𝐰}⁢[Δ⁢ϵ]$ would be even smaller, since $Δ⁢ϵ$ would be constrained to consistently shallow, less-curved directions. Thus, this possibility does not interfere with our main claim.

For Equation (11) to hold, $Δ⁢𝐜$ should point in directions of ‘more-than-average’ upward curvature. This follows intuitively because a steep downhill direction, which effectively reduces task error, will usually have higher upward curvature than an arbitrary direction (see Figure 3c for intuition). It remains to formalise this argument mathematically, and consider edge cases where it doesn’t hold.

### Dependence of the optimal magnitude of steady-state, compensatory plasticity on the mechanism

Compensatory plasticity is analogous to learning, since it acts to reduce task error. We do not yet know the algorithms that neural circuits use to learn, although constructing biologically plausible learning algorithms is an active research area. Nevertheless, all the potential learning algorithms we are aware of fit into three broad categories. For each category, we shall show why and when our main claim holds. We will furthermore investigate quantitative differences in the optimal compensatory plasticity rate, across and within categories. A full mathematical justification of all the assertions we make is found in SI section 1.3.

We first highlight a few general points:

Learning algorithms attempt to move to the bottom of the loss landscape. But they are blind. Spying a distant valley equates to ‘magically’ predicting that a very different network state will have very low task error. How do they find their way downhill? There are three broad strategies (Raman and O'Leary, 2021):

Table 2 shows the categories for which our main claim holds.

**Table 2.**
 Table elements highlighted in teal correspond to scenarios in which our main claim holds, as Equation (11) is satisfied.


<table>
  <thead>
    <tr>
      <th></th>
      <th>Quadratic F⁢[𝐰]</th>
      <th>Nonlinear F⁢[𝐰], low steady-state error</th>
      <th>Nonlinear F⁢[𝐰], high steady-state error</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0th order algorithm</td>
      <td>Q⁢[Δ⁢𝐜]≈Q⁢[Δ⁢ϵ]</td>
      <td>Q⁢[Δ⁢𝐜]≈Q⁢[Δ⁢ϵ]</td>
      <td>Q⁢[Δ⁢𝐜]≈Q⁢[Δ⁢ϵ]</td>
    </tr>
    <tr>
      <td>0st order algorithm</td>
      <td>Q⁢[Δ⁢𝐜]≥Q⁢[Δ⁢ϵ]</td>
      <td>Q⁢[Δ⁢𝐜]≥Q⁢[Δ⁢ϵ]</td>
      <td>Q⁢[Δ⁢𝐜]≈Q⁢[Δ⁢ϵ]</td>
    </tr>
    <tr>
      <td>0nd order algorithm</td>
      <td>Q⁢[Δ⁢𝐜]≈Q⁢[Δ⁢ϵ]</td>
      <td>Q⁢[Δ⁢𝐜]≈Q⁢[Δ⁢ϵ]</td>
      <td>Q⁢[Δ⁢𝐜]≤Q⁢[Δ⁢ϵ]</td>
    </tr>
  </tbody>
</table>

We first consider the simplest case of a quadratic loss function $F⁢[𝐰]$. Here, directions of curvature in any direction are constant (mathematically, the hessian $\nabla^{2}⁡F⁢[𝐰]$ does not vary with network state). Moreover, the gradient obeys a consistent relationship with the hessian:

$$
∇F[w]=∇^{2}F[w^{∗}](w−w^{∗}).
$$

Components of $(𝐰-𝐰^{*})$ with high upward curvature are magnified under the transformation $\nabla^{2}⁡F⁢[𝐰^{*}]$, since they correspond to eigenvectors of $\nabla^{2}⁡F⁢[𝐰^{*}]$ with high eigenvalue. Conversely, components with low upward curvature are shrunk. As the gradient $\nabla⁡F⁢[𝐰]$ is the output of such a transformation from Equation (13), this suggests it is biased towards directions of high upward curvature. Indeed, we can quantify this bias. Let ${\lambda_{i}}$ be the eigenvalues of $\nabla^{2}⁡F⁢[𝐰^{*}]$, and ${c_{i}}$ the projections of the corresponding eigenvectors onto $𝐰-𝐰^{*}$. Then

$$
Q_{w}[∇F[w]]=\frac{\sumi=1Nc_{i}^{2}\lambda_{i}^{3}}{\sumi=1Nc_{i}^{2}\lambda_{i}^{2}}.
$$

The value of Equation (14) depends on the values ${c_{i}}$. In the ‘average’ case, where they are equal, and $𝐰-𝐰^{*}$ is thus a direction of ‘average’ curvature, $Q_{𝐰}⁢[\nabla⁡F⁢[𝐰]]\geqQ_{𝐰}⁢[Δ⁢ϵ]$ holds. This inequality gap widens with increasing anisotropy in the curvature of different directions (i.e. with a wider spread of eigenvalues $\lambda_{i}$, corresponding to more elliptical/less circular level sets in the illustration of Figure 4b). Indeed, simulation results in Figure 5—figure supplement 1 (top row) show how the ratio $∥Δ⁢𝐜∥_{2}:∥Δ⁢ϵ∥_{2}$ that optimises steady-state task error is significantly less than one, in a quadratic error function where compensatory plasticity accurately follows the gradient, and for different synaptic fluctuation rates.

![Figure 4.](https://cdn.elifesciences.org/articles/62912/elife-62912-fig4-v2.jpg)

**Figure 4.:** Colours depict level sets of the loss landscape. Elliptical level sets correspond to a quadratic loss function (which approximates any loss function in the neighbourhood of a local minimum). In c and d, we depict compensatory plasticity and synaptic fluctuations as sequential, alternating processes for illustrative purposes, although they are modelled as concurrent throughout the paper. (a) Compensatory plasticity directions locally decrease task error, so point from darker to lighter colours. Optimal magnitude is reached when the vectors ‘kiss’ a smaller level set, that is, intersect that level set while running parallel to its border. Increasing magnitude past this past this point increases task error, by moving network state to a higher-error level set. (b) If compensatory plasticity is parallel to the gradient (i.e. it enacts gradient descent), then it runs perpendicular to the border of the level set on which it lies (i.e. the tangent plane). This is shown explicitly for the ‘exact gradient’ direction of plasticity. The optimal magnitude of plasticity in this direction is smaller than that of a corrupted gradient descent direction, even though the former is more effective in reducing task error, because the exact gradient points in a more highly curved direction. (c) Synaptic fluctuations of a certain magnitude perturb the network state. The optimal magnitude of compensatory plasticity (in the exact gradient descent direction, for this example) is significantly smaller than that of the synaptic fluctuations, using the geometric heuristic explained in (a). If the magnitude of compensation increased to match the synaptic fluctuation magnitude there would be overshoot, and task error would converge to a higher steady state. (d) If compensatory plasticity mechanisms can perfectly calculate both the local gradient and hessian (curvature) of the loss landscape, then network state will move in the direction of the ‘Newton step’. In the quadratic case (elliptical level sets), this will directly ‘backtrack’ the synaptic fluctuations. Thus, the optimal magnitude of compensatory plasticity will be equal to that of the synaptic fluctuations. However, time delays in the sensing of synaptic fluctuations and limited precision of the compensatory plasticity mechanism will preclude this.

![Figure 5.](https://cdn.elifesciences.org/articles/62912/elife-62912-fig5-v2.jpg)

**Figure 5.:** Each $(x,y)$ value on a given graph corresponds to an 8000 timepoint nonlinear neural network simulation (see ‘Methods’ for details). The $y$ value gives the steady-state task error (average task error of the last 500 timepoints) of the simulation, while the $x$ value gives the ratio of the magnitudes of the compensatory plasticity and synaptic fluctuations terms. Steady state error is averaged across 8 simulation repeats; shading depicts one standard deviation. Between graphs, we change simulation parameters. Down rows, we increase the proportionate noise corruption of the compensatory plasticity term (see Materials and methods section for details). Across columns, we increase the magnitude of synaptic fluctuations.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/62912/elife-62912-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** The description of this figure is identical to that of Figure 5. The only difference is the choice of network. Here, we use the linear networks as described in Methods.

What about the case of a nonlinear loss function? Close to a minimum $𝐰^{*}$, the relationship of Equation (13) approximately holds (the loss function is locally quadratic). So if steady-state error is very low, we can directly transport the intuition of the quadratic case. However when steady state error increases, Equation (13) becomes increasingly approximate. In the limiting case, we could consider $\nabla⁡F⁢[𝐰]$ as being completely uncorrelated from $\nabla^{2}⁡F⁢[𝐰]$, in which case $Q_{𝐰}⁢[\nabla⁡F⁢[𝐰]]≈Q_{𝐰}⁢[Δ⁢ϵ]$ would hold. Numerical results in Figure 5 supports this assertion in nonlinear networks: the optimal ratio satisfies $∥Δ⁢𝐜∥_{2}:∥Δ⁢ϵ∥_{2}≈1$ in conditions where steady-state task error is high, and $∥Δ⁢𝐜∥_{2}:∥Δ⁢ϵ∥_{2}\leq1$ in conditions where it is low.

Overall, we see that if $Δ⁢𝐜∝-\nabla⁡F⁢[𝐰]$ (i.e. compensatory plasticity enacts gradient descent), then we would expect compensatory plasticity to be outcompeted by synaptic fluctuations to maintain optimal steady-state error.

Even if compensatory plasticity does not move in the steepest direction of error decrease (i.e. the error gradient), it must move in an approximate downhill direction to improve task error (see e.g. Raman et al., 2019). Furthermore, the worse the quality of the gradient approximation, the larger the optimal level of compensatory plasticity (illustrated conceptually in Figure 4b–c, and numerically in Figure 5 and Figure 5—figure supplement 1). Why? We can rewrite such a learning rule as

$$
Δ⁢𝐜∝-\nabla⁡F⁢[𝐰]+ν,
$$

where $ν$ represents systematic error in the gradient approximation. The upward curvature in the direction $Δ⁢𝐜$ becomes a (nonlinear) interpolation of the upward curvatures in the directions $\nabla⁡F⁢[𝐰]$ and $ν$ (see Equation (A6) of the SI). As long as $ν$ is less biased towards high curvature directions than $\nabla⁡F⁢[𝐰]$ itself, then this decreases the upward curvature in the direction $Δ⁢𝐜^$, and thus increases the optimal compensatory plasticity rate. Indeed Figure 5 shows in simulation that this rate increases for more inaccurate compensatory plasticity mechanisms.

We now turn to zero-order learning algorithms, such as REINFORCE. These do not explicitly approximate a gradient, but generate random plasticity directions, which are retained/opposed based upon their observed effect on task error. We would expect randomly generated plasticity directions to have ‘average’ upward curvature, similarly to synaptic fluctuations. In this case, we would therefore get $Q_{𝐰}⁢[Δ⁢𝐜]≈Q_{𝐰}⁢[Δ⁢ϵ]$, and compensatory plasticity should thus equal synaptic fluctuations in magnitude.

Finally, we consider second-order learning algorithms, and in particular the Newton update:

$$
\nabla^{2}⁡F⁢[𝐰]⁢Δ⁢𝐜=-\nabla⁡F⁢[𝐰].
$$

As previously discussed, we assume that learning algorithms that require detailed information about the Hessian are biologically implausible. As such, our treatment is brief, and mainly contained in SI section 2.2.2.

In a linear network, the Newton update corresponds to compensatory plasticity making a direct ‘beeline’ for $𝐰^{*}$ (see Figure 4d). As such $Q_{𝐰}⁢[Δ⁢𝐜]=Q_{𝐰}⁢[Δ⁢ϵ]$ and the optimal magnitude of compensatory plasticity should match synaptic fluctuations. The same is true for a nonlinear network in a near-optimal state. However if steady-state task error is high in a nonlinear network, then compensatory plasticity should outcompete synaptic fluctuations. This case does not contradict our central claim however, since high task error at steady state implies that the task is not truly learned.

Together our results and analyses show that the magnitude of compensatory plasticity, at steady state task error, should be less or equal to that of synaptic fluctuations. This conclusion does not depend upon circuit architecture, or choice of biologically plausible learning algorithm.

## Discussion

A long-standing question in neuroscience is how neural circuits maintain learned memories while being buffeted by synaptic fluctuations from noise and other task-independent processes (Fusi et al., 2005). There are several hypotheses that offer potential answers, none of which are mutually exclusive. One possibility is that fluctuations only occur in a subset of volatile connections that are relatively unimportant for learned behaviours (Moczulska et al., 2013; Chambers and Rumpel, 2017; Kasai et al., 2003). Following this line of thought, circuit models have been proposed that only require stability in a subset of synapses for stable function (Clopath et al., 2017; Mongillo et al., 2018; Susman et al., 2018).

Another hypothesis is that any memory degradation due to fluctuations is counteracted by restorative plasticity processes that allow circuits to continually ‘relearn’ stored associations. The information source directing this restorative plasticity could come from an external reinforcement signal (Kappel et al., 2018), from interactions with other circuits (Acker et al., 2018), or spontaneous, network-level reactivation events (Fauth and van Rossum, 2019). A final possibility is that ongoing synaptic fluctuations are accounted for by behavioural changes unrelated to learned task performance .

All these hypotheses share two core assumptions that we make, and several include a third that our results depend on:

We extracted mathematical consequences of these three assumptions by building a general framework. We first modelled the the degree of degradation of previously learned information in terms of an abstract, scalar-valued, task error function or ‘loss landscape’. The brain may not have, and in any case does not require, explicit representation of such a function for a specific task. All that is required is error feedback from the environment and/or some internal prediction.

We then noted that compensatory plasticity should act to decrease task error, and thus point in a downhill direction on the ‘loss landscape’. We stress that we do not assume a gradient-based learning rule such as the backpropagation algorithm, the plausibility of which is an ongoing debate (Whittington and Bogacz, 2019).

Our results do not depend on whether synaptic changes during learning are gradual, or occur in large, abrupt steps. Although most theory work assumes plasticity to be gradual, there is evidence that plasticity can proceed in discrete jumps. For instance, abrupt potentiation of synaptic inputs that lead to the formation of place fields in mouse CA1 hippocampal neurons can occur within seconds as an animal explores a new environment (Bittner et al., 2017). Even classical plasticity paradigms that depend upon millisecond level precision in the relative timing of pre/post synaptic spikes follow a paradigm where there is a short ‘induction phase’ of a minute or so, following which there is a large and sustained change in synaptic efficacy (e.g. Markram et al., 1997; Bi and Poo, 1998). It is therefore an open question as to whether various forms of synaptic plasticity are best accounted for as an accumulation of small changes or a threshold phenomenon that results in a stepwise change. Our analysis is valid in either case. We quantify plasticity rate by picking a (large or small) time interval over which the net plasticity direction is approximately constant, and evaluate the optimal, steady-state magnitude of compensatory plasticity over this interval, relative to the magnitude of synaptic fluctuations.

A combination of learning-induced and learning-independent plasticity should lead to an eventual steady state level of task error, at which point the quality of stored information does not decay appreciably over time. The absolute quality of this steady state depends upon both the magnitude of the synaptic fluctuations, and the effectiveness of the compensatory plasticity.

Our main finding was that the quality of this steady state is optimal when the rate of compensatory plasticity does not outcompete that of the synaptic fluctuations. This result, which is purely mathematical in nature, is far from obvious. While it is intuitively clear that retention of circuit function will suffer when compensatory plasticity is absent or too weak, it is far less intuitive that the same is true generally when compensatory plasticity is too strong.

We also found that the precision of compensatory plasticity influenced its optimal rate. When ‘precision’ corresponds to the closeness of an approximation to a gradient-based compensatory plasticity rule, an increase in precision resulted in the optimal rate of compensatory plasticity being strictly less than that of fluctuations. In other words, sophisticated learning rules need to do less work to optimally overcome the damage done by learning-independent synaptic fluctuations. Indeed experimental estimates (see Table 1) suggest that activity-independent synaptic fluctuations can significantly outcompete systematic, activity-dependent changes in certain experimental contexts. Tentatively, this means that the high degree of synaptic turnover in these systems is in fact evidence for the operation of precise synaptic plasticity mechanisms as opposed to crude and imprecise mechanisms.

Our results are generic, in that they follow from fundamental mathematical relationships in optimisation theory, and hence are not dependent on particular circuit architectures or plasticity mechanisms. We considered cases in which synaptic fluctuations were distributed across an entire neural circuit. However, the basic framework easily extends, allowing for predictions in more specialised cases. For instance, recent theoretical work (Clopath et al., 2017; Mongillo et al., 2018; Susman et al., 2018) have hypothesised that synaptic fluctuations could be restricted to ‘unimportant’ synapses. These correspond to low curvature (globally insensitive) directions in the ‘loss landscape’. Our framework (Equation (9) in particular) immediately predicts that the optimal rate of compensatory plasticity will decrease proportionately with this curvature.

Precise experimental isolation/elimination of the plasticity sources attributable to learning and retention of memories remains challenging. Nevertheless, in conventional theories of learning (e.g. Hebbian learning), neural networks learn through plasticity induced by patterns of pre- and postsynaptic neural activity. A reasonable approximation, therefore, is to equate the ‘compensatory/learning-induced’ plasticity of our paper with ‘activity-dependent’ plasticity in experimental setups. With this assumption, our results provide several testable predictions.

Firstly, our results show that that the rate of compensatory (i.e. learning-dependent) plasticity is greater when a neural circuit is in a phase of active learning, as opposed to maintaining previously learned information (see Equation (10) and the surrounding discussion). Consequently, the relative contribution of synaptic fluctuations to the overall plasticity rate should be lower in this case. It would be interesting to test whether this were indeed the case, by comparing brain circuits in immature vs mature organisms, and in neural circuits thought to be actively learning vs those thought to be retaining previously learned information. One way to do this would be to measure the covariance of functional synaptic strengths at coinnervated synapses using EM reconstructions of neural tissue. A higher covariance implies a lower proportion of activity-dependent (i.e. compensatory) plasticity, since co-innervated synapses share presynaptic activity histories. Interestingly, two very similar experiments (Bartol et al., 2015) and (Dvorkin and Ziv, 2016) did indeed examine covariance in EM reconstructions of hippocampus and neocortex, respectively. This covariance appears to be much lower in hippocampus (compare Figure 1 of Bartol et al., 2015 to Figure 8 of Dvorkin and Ziv, 2016). Many cognitive theories characterise hippocampus as a continual learner and neocortex as a consolidator of previously learned information (e.g. O'Reilly and Rudy, 2001). Our analysis provides support for this hypothesis at a mechanistic level by linking low covariance in coinnervated hippocampal synapses to continual learning.

Secondly, a number of experimental studies (Nagaoka et al., 2016; Quinn et al., 2019; Yasumatsu et al., 2008; Minerbi et al., 2009; Dvorkin and Ziv, 2016) note a persistence of the bulk of synaptic plasticity in the absence of activity-dependent plasticity or other correlates of an explicit learning signal, as explained in our review of key experimental findings. However, there are two important caveats for relating our work to these experimental observations:

Thus, while our results offer a surprising agreement with a number of experimental observations, we believe it is important to further replicate measurements of synaptic modification in a variety of settings, both in vivo and in vitro. We hope our analysis provides an impetus for this difficult experimental work by offering a first-principles theory for the volatility of connections in neural circuits.

## Materials and methods

### Simulations

We simulated two types of network, which we refer to as linear (Figure 5—figure supplement 1) and nonlinear (Figures 1 and 5) respectively. We ran our simulations in the Julia programming language (version 1.3), and in particular used the Flux.jl software package (version 0.9) to construct and update networks. Source code is available at https://github.com/Dhruva2/OptimalPlasticityRatios (copy archived at swh:1:rev:fcb1717a822f90b733c49d62bfc2f970155b7364, Raman, 2021).

### Nonlinear networks

Networks were rate-based, with the firing rate $r⁢(t)$ of a given neuron defined as

$$
r⁢(t)=\sigma⁢(w^{T}⁢(t)⁢u⁢(t)),
$$

where $w$ is the vector of presynaptic strengths, $u$ represents the firing rate of the associated presynaptic neurons, and $\sigma⁢(x):=\frac{1}{1+exp⁡(-x)}$ is the sigmoid function. Initial weight values were generated randomly, according to the standard Xavier distribution (Glorot and Bengio, 2010). Networks were organised into three layers, containing 12, 20, and 10 neurons, respectively. Any given neuron was connected to all neurons in the previous layer. For the first layer, the firing rates of the ‘previous layer’ corresponded to the network inputs.

### Linear networks

Networks were organised into an input layer of 12 neurons, and an output layer of 10 neurons. Each output neuron was connected to all input layer neurons. Networks were rate-based, with the firing rate $r⁢(t)$ of a given neuron defined as

$$
r⁢(t)=w^{T}⁢(t)⁢u⁢(t),
$$

where $u_{i}⁢(t)$ corresponds to the $i^{t⁢h}$ input (input-layer neuron) or the firing rate of the $i^{t⁢h}$ input-layer neuron (output-layer neuron). Initial weight values were generated randomly, according to the Xavier distribution (Glorot and Bengio, 2010).

### Task error

For each network, we generated 1000 different, random, input vectors. Each component of the vector was generated from a unit Gaussian distribution. Task error, at the $t^{t⁢h}$ timestep, was taken as the mean squared error of the network in recreating the outputs of the initial ($t=0$) network, in response to the suite of inputs. Mathematically, this equates to

$$
F[w(t)]=\frac{1}{|𝒰|}\sumu\in𝒰‖y(w(t),u)−y(w(0),u)‖_{2}^{2},
$$

where $y⁢(𝐰⁢(t),u)$ denotes the output of the network given the synaptic strengths at time $t$, in response to input $u\in𝒰$. Note that this task error recreates the ‘student-teacher’ framework of e.g. (Levin et al., 1990; Seung et al., 1992), where a fixed copy of the initial network is the teacher.

### Weight dynamics

At each simulation timestep, synaptic weights were updated as

$$
Δw_{t+1}=Δc_{t}+Δϵ_{t}.
$$

We took the synaptic fluctuations term, $Δ⁢ϵ_{t}$, as scaled white noise, that is,

$$
Δ⁢ϵ_{t}∝𝒩⁢(0,𝕀)
$$

The constant of proportionality was calculated so that the magnitude $∥Δ⁢ϵ∥_{2}$ conformed to a pre-specified value. This magnitude was 2 in the simulation of Figure 1, and was a graphed variable in the simulations of Figure 5 and Figure 5—figure supplement 1.

The compensatory plasticity term, $Δ⁢𝐜_{t}$, was calculated in two stages. First we applied the backpropagation algorithm, using $y⁢(𝐰⁢(0),u)$ as the ideal network outputs to train against. This generated an ‘ideal’ direction of compensatory plasticity , proportional to the negative gradient $\nabla⁡F⁢[𝐰⁢(t)]$. For Figure 5 and Figure 5—figure supplement 1 we then corrupted this gradient with a tunable proportion of white noise. Overall, this gives,

$$
Δ⁢𝐜_{t}=-\gamma_{1}⁢\nabla⁡F^⁢[𝐰]_{t}+\gamma_{2}⁢ν^_{t},
$$

where $ν_{t}∼𝒩⁢(0,𝕀)$ is the noise corruption term, and $\gamma_{1},\gamma_{2}>0$ are tunable hyperparameters. The higher the ratio $\gamma_{2}:\gamma_{1}$, the greater the noise corruption. Meanwhile, $\sqrt{\gamma_{1}^{2}+\gamma_{2}^{2}}$ sets the overall magnitude of compensatory plasticity . By tuning $\gamma_{1}$ and $\gamma_{2}$, we can therefore independently modify the magnitude and precision of the compensatory plasticity term. In Figure 1, we set $\gamma_{2}=0$.
