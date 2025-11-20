# Emergent periodicity in the collective synchronous flashing of fireflies

## Authors

- Raphael Sarfati<sup>1</sup> ([ORCID: 0000-0003-4944-0632](https://orcid.org/0000-0003-4944-0632)) †
- Kunaal Joshi<sup>2</sup> ([ORCID: 0000-0002-8001-1230](https://orcid.org/0000-0002-8001-1230)) †
- Owen Martin<sup>1</sup>
- Julie C Hayes<sup>3</sup>
- Srividya Iyer-Biswas<sup>2</sup> ([ORCID: 0000-0002-1587-6780](https://orcid.org/0000-0002-1587-6780)) †
- Orit Peleg<sup>1</sup> ([ORCID: 0000-0001-9481-7967](https://orcid.org/0000-0001-9481-7967)) †

### Affiliations

1. BioFrontiers Institute, University of Colorado Boulder Boulder United States ([ROR:02ttsq026](https://ror.org/02ttsq026))
2. Department of Physics and Astronomy, Purdue University West Lafayette United States ([ROR:02dqehb95](https://ror.org/02dqehb95))
3. Department of Computer Science, University of New Mexico Albuquerque United States ([ROR:05fs6jp91](https://ror.org/05fs6jp91))
4. Santa Fe Institute Santa Fe United States ([ROR:01arysc35](https://ror.org/01arysc35))

† Corresponding author

## Abstract

In isolation from their peers, Photinus carolinus fireflies flash with no intrinsic period between successive bursts. Yet, when congregating into large mating swarms, these fireflies transition into predictability, synchronizing with their neighbors with a rhythmic periodicity. Here we propose a mechanism for emergence of synchrony and periodicity and formulate the principle in a mathematical framework. Remarkably, with no fitting parameters, analytic predictions from this simple principle and framework agree strikingly well with data. Next, we add further sophistication to the framework using a computational approach featuring groups of random oscillators via integrate-and-fire interactions controlled by a tunable parameter. This agent-based framework of P. carolinus fireflies interacting in swarms of increasing density also shows quantitatively similar phenomenology and reduces to the analytic framework in the appropriate limit of the tunable coupling strength. We discuss our findings and note that the resulting dynamics follow the style of a decentralized follow-the-leader synchronization, where any of the randomly flashing individuals may take the role of the leader of any subsequent synchronized flash burst.

## Introduction

Physical systems consisting of several interacting entities often exhibit large-scale properties which are distinct from the capabilities of each entity taken individually: this is the well-known concept of emergence. Emergence has been observed and studied in both inanimate and animate systems, including famously groups of animals (Kelley and Ouellette, 2013; Attanasi et al., 2014). Animal collective behavior broadly designates dynamical patterns that are unsupervised consequences of the accumulation of low-level interactions between neighboring individuals (Ouellette, 2022; Ballerini et al., 2008; Couzin, 2009). One simple yet compelling manifestation of emergence in the natural world is in the form of firefly flash synchronization (Faust, 2010; Buck and Buck, 1966; Sarfati et al., 2020; Sarfati et al., 2021; Sarfati et al., 2022). For example, when sufficiently many Photinus carolinus fireflies congregate into a mating swarm (lek), they start to align their flashes on the same tempo, creating a mesmerizing display that has captivated the curious minds of many. This possibly serves to strengthen their species-specific signal and heighten the ability for conspecific males and females to identify one another (Faust, 2010; Moiseff and Copeland, 2010; Stanger-Hall and Lloyd, 2015). In addition to collective synchrony, a more careful examination of P. carolinus’ flashing pattern further reveals another non-trivial signature: emergent periodicity. Indeed, in their natural habitat, these fireflies produce periodic bursts of flashes occurring with great regularity, with a temperature-dependent period generally around 12 s (Faust, 2010; Moiseff and Copeland, 2010). Surprisingly, when put in isolation, a single firefly does not appear to show any regularity about when it emits its flash trains (Sarfati et al., 2020), where intervals between flash trains vary between a few seconds to a few minutes apart. How, then, can a multitude of interacting fireflies exhibit a specific frequency that does not appear to be encoded in any single one of them?

Synchronization is traditionally thought of as the adjustment of rhythms of self-sustained oscillators due to coupling (Mirollo and Strogatz, 1990; Strogatz, 1997; Strogatz, 2000; Pikovsky et al., 2001; Ramírez Ávila et al., 2003; Ramírez Ávila et al., 2019). The Kuramoto model and other such traditional models addressing synchrony in systems such as Pteroptyx malaccae fireflies model individuals as oscillators firing highly regularly in isolation, often with different periods. The question these models are primed to answer is, how do oscillators with different individual periods and starting from different phases, come together to oscillate synchronously? This is fundamentally different from the problem posed by our system, in which the individuals, which fire highly irregularly, seem to use synchrony through coupling with other individuals as a tool to achieve greater regularity in their firing period. While traditional models of limit-cycle oscillators are also capable of modeling systems in which isolated individuals do not oscillate periodically but collective oscillations occur only above a certain threshold density, in those models the individuals are generally inherently oscillatory and their periodic oscillations are suppressed through a sufficiently strong coupling with the surroundings. (De Monte et al., 2007; Taylor et al., 2009). We instead present a stochastic theoretical framework based on a simple, intuitive mechanism by which inherently non-oscillating individuals are able to oscillate synchronously in a group, and apply this to P. carolinus fireflies, successfully explaining the convergence towards a common, well-defined period between flash bursts as the number $N$ of fireflies increases.

## Results

### Behavioral experiments

A P. carolinus lek in its natural habitat contains several thousands of fireflies of which the males display a robust collective flash pattern. They flash over the course of periodic bursts separated by a few seconds of total darkness (Figure 1A, over a few seconds). Collective bursts in the swarm have a well-defined period (peak-to-peak) of about 12 s (Sarfati et al., 2020). One could think, then, that each individual firefly also emits flash trains with about the same time period, and that the effect of visual interactions is to align these individual trains on the same tempo. In other words, the swarm could be a set of coupled oscillators converging to a common phase, as has been described in previous models (Mirollo and Strogatz, 1990; Strogatz, 1997; Strogatz, 2000; Ermentrout, 1991; Rodrigues et al., 2016). Crucially, however, when a single firefly is taken out of the lek and placed in a large (2 m3) enclosing volume visually insulated from the rest of the group, all periodicity in the occurrence of flash trains is lost. The single firefly continues to emit sporadic bursts (Figure 1B and C), but the time between successive flash bursts varies between a few seconds and a few minutes (Figure 1B and Sarfati et al., 2020). This suggests that individual interburst intervals (IBIs) occur at random, and may thus depend on a variety of behavioral factors. When collecting measurements from 10 different fireflies recorded for several minutes under the same conditions, we are able to outline the distribution of interburst intervals for a single firefly in isolation (Figure 1D, purple). (The underlying assumption here is that all fireflies have the same distribution of interburst intervals.) Interestingly, as the number of fireflies within the enclosing volume is increased, a regularity in the time between bursts starts to emerge. At about $N=15$, the distribution of interburst intervals becomes very similar to that observed in the natural habitat (Sarfati et al., 2020). For $N=20$, it is clear that there is a very strong collective periodicity in the emission of flash bursts of about 12 s, similar to that of the undisturbed swarm flashing just outside the tent (Figures 1D and E and Figure 2).

![Figure 1.](https://cdn.elifesciences.org/articles/78908/elife-78908-fig1-v3.jpg)

**Figure 1.:** (A) Long exposure photograph illustrating flashes in a P. carolinus natural swarm. (B) Overlaid time series of three isolated individual fireflies emitting flash bursts which appear random. The inset (C) shows the burst-like nature of P. carolinus flash events. (D) Interburst distributions $b(t)$ for one firefly (purple) and 20 fireflies (blue) insulated from the rest of the swarm. (E) Twenty P. carolinus fireflies flashing in a tent exhibiting the periodic nature of their collective flashing.

![Figure 2.](https://cdn.elifesciences.org/articles/78908/elife-78908-fig2-v3.jpg)

**Figure 2.:** (A) A schematic of the flashing pattern of a single isolated firefly. State 0 corresponds to no flashes, and state 1 corresponds to a burst of consecutive flashes. The durations between bursts of single isolated fireflies are highly irregular. (B) In a system with more than one firefly, if a non-flashing firefly sees another one flash, it too starts flashing. Thus, for a system with two fireflies, their bursts are synchronized. After each burst, the time to next burst is determined by which firefly flashes first. Thus, on average, the interburst interval is lower, and hence slightly more regular, than that for a single isolated firefly. (C) As the number of fireflies increases, the probability increases that at least one of them will flash with an interburst interval near the minimum of the distribution for isolated fireflies. This minimum value is expected to be set by the refractory period of the fireflies, which is expected to be similar for all fireflies. Thus, the overall behavior becomes highly periodic with a period approaching this minimum value.

### Proposed principle of emergent periodicity, its theoretical formulation, and analytic fitting-free predictions

Here we propose the following paradigm, derive its mathematical formulation, and validate its predictions against experimental data: (1) Each time a firefly has finished a burst of flashing, it waits a random time $t$, drawn from a distribution $b(t)$, before flashing again. (2) Upon flashing, a firefly instantly triggers all other fireflies to also flash. (3) After flashing, each firefly resets its internal waiting time to another random $t$.

The distribution $b(t)$ here is the distribution of interburst intervals exhibited by the firefly in a solitary, isolated environment. We denote by $T_{b}$ the collective interburst interval, that is the time between any two successive bursts of flashes produced in the swarm. The probability distribution $P_{N}(T_{b})$ of the interburst interval $T_{b}$ of a group of $N$ fireflies can be calculated as the probability distribution that one of the $N$ fireflies emits its first flash at time $T_{b}$ after the last collective burst, while the rest $(N−1)$ fireflies have not flashed until then.

If all fireflies have different IBI distributions such that the interburst interval for the $i^{th}$ firefly in isolation is drawn from the distribution $b_{i}$, then the probability density for $i^{th}$ firefly flashing first in a group of $N$ fireflies at time $T_{b}$ is given by

$$
P_{i}(T_{b})=b_{i}(T_{b})\prodj\neqi[\int_{T_{b}}^{∞}b_{j}(t)dt],
$$

where the first term on the right is the probability density of the $i^{th}$ firefly flashing at time $T_{b}$ , and the second term is the probability that the remaining fireflies do not flash before time $T_{b}$. The probability density for any firefly in the group of $N$ fireflies flashing first at time $T_{b}$ is simply the sum of the probability densities of the individual fireflies flashing first at this time, thus,

$$
P_{N}(T_{b})=\sumi=1Nb_{i}(T_{b})\prodj\neqi[\int_{T_{b}}^{∞}b_{j}(t)dt].
$$

As the number of fireflies increases, this distribution converges to a distribution bounded by the minimum and maximum values of the minimum interburst intervals $T_{0}$ of the individual fireflies. To show this, we first label the minimum interburst interval for $i^{th}$ firefly in isolation by $T_{0,i}$, Thus $b_{i}(T_{b}<T_{0,i})=0$. Hence, from Equation 2, as $N→∞$, for $T_{b}<mini(T_{0,i})$, $P_{N}(T_{b})=0$ because each $b_{i}(T_{b})$ is 0. Also,

$$
P_{N}(T_{b})=\sumi=1Nb_{i}(T_{b})\prodj\neqi[\int_{T_{b}}^{∞}b_{j}(t)dt]\leqNmaxi[b_{i}(T_{b})]{maxj[\int_{T_{b}}^{∞}b_{j}(t)dt]}^{N−1}.
$$

For $T_{b}>maxi(T_{0,i})$ , as $N→∞$, $P(T_{b})→0$ because the right-most integral is less than 1. Thus, as $N→∞$ , $P_{N}(T_{b})$ is bounded by the minimum and maximum values that $T_{0,i}$ can take. We expect these minimum values to be set by physiological constraints (the refractory period), and thus be similar for all fireflies. In this case $(T_{0,i}=T_{0}∀i)$, the group interburst interval distribution converges to the Dirac Delta function in the large $N$ limit,

$$
limN→∞P_{N}(T_{b})=\delta(T_{b}−T_{0}).
$$

The theoretical predictions are consistent with the intuitive result that the shortest possible interburst interval is the only one that occurs in large, fully connected, and instantaneously stimulated groups of fireflies. We expect such a threshold minimum time to exist owing to physiological constraints, which prevent the fireflies from flashing continuously forever without pause. Intuitively, as the number of fireflies increases, there is a greater probability that at least one of those fireflies will flash at an interval close to the minimum.

In the following sections, due to the paucity of available data and limited statistical precision in the data available to accurately quantify the IBI distributions for isolated fireflies, we have pooled together the isolated fireflies’ data under the assumption that their interburst interval distributions are sufficiently close, so that they can be approximately considered identical $(b_{i}=b∀i)$. Thus, the interburst interval distribution for $N$ fireflies reduces to

$$
P_{N}(T_{b})=N[\int_{T_{b}}^{∞}b(t)dt]^{N−1}b(T_{b})
$$

Thus we have set up a mathematical framework which takes as its input the experimentally observed interburst distribution and makes specific predictions with no fine-tuning fitting parameters.

Conceptually, in the idealization that at $N→∞$ this distribution converges to a Dirac Delta function, which tends to make the flashing patterns perfectly periodic with no variation. However, for a finite number $N$ of fireflies, the distribution peaks at a value greater than $T_{0}$, and has a specific non-zero width that decreases with increasing $N$ (see section ‘Theoretical framework’). These specific predictions are spectacularly borne out by the experimental data. With no fine-tuning fitting parameter, and the experimentally observed single firefly distribution (Figure 3A) as the only input to the mathematical framework, we see an excellent match between the $N$-dependent experimentally observed interburst distributions and the corresponding prediction from analytic theory (Figure 3B–E). Moreover, the corresponding sharpening of the peak of the distribution (resulting in decreasing noise) with increasing $N$ also quantitatively matches with the trend predicted by theory — see the plot of standard deviation vs. $N$ in panel Figure 3F. Through these compelling matches between predictions from the theory, without fitting parameters, and the experimental observations, we establish the validity of the proposed principle for emergent synchrony and periodicity.

![Figure 3.](https://cdn.elifesciences.org/articles/78908/elife-78908-fig3-v3.jpg)

**Figure 3.:** Experimental data vis-à-vis results from analytic theory (no fitting parameters) and computational approach (wherein $\beta$ is a fitting parameter as explained in accompanying text).Experimental data for each value of N come from three repetitions of experiments at that density. (A) The experimentally measured single firefly interburst distribution (Figure 1D, purple, represented here also in purple). The smoothed version of this distribution (blue curve, detailed methods outlined in the Methods Section) is used as an input in analytical theory and, in conjunction with $\beta$ values, in the computational approach. The inset shows the region between 0–160 s within which most firefly values lie. (B–E) show the interburst distributions for different numbers of fireflies. Our theoretical framework accurately predicts the sharpening of the interburst distribution as $N$ increases, without the need of fitting parameters. The $\beta$ value atop each figure is fit by minimizing the two-sided Kolmogorov-Smirnov test between the simulation and experimental distributions (see Figure 7 for a full sensitivity analysis). (F) demonstrates that the standard deviation of the interburst interval distribution decreases with N as predicted by analytic theory (no fitting parameter; see theory section) and the computational approach (using the respective value of best-fit $\beta$ shown with the corresponding distribution in B–E).

Furthermore, using the analytic framework, the following rigorous results can be generally proved to hold for any input single firefly distribution: As the number $N$ of fireflies increases, along with the variance, all the moments of the interburst distribution monotonically decrease. In addition, the left-most mode shifts further towards the left with increasing $N$ until it reaches $T_{0}$. Taken together, what these predictions show is that for any input distribution shape, we are guaranteed to get emergent periodicity and synchrony through the proposed mechanism. We have provided detailed derivations of these predictions in Methods Section (Theoretical Framework).

### Computational approach: Agent-based simulation

In the preceding section, we have articulated a principle of emergent periodicity, its theoretical formulation, and provided concrete fitting-free predictions which are spectacularly borne out by data. Here we attempt to build on the success of theory with an agent-based simulation.

At the outset, we clarify that our attempts at agent-based simulation, which simply tweak extant models, such as Kuramoto or integrate-and-fire (IF), without incorporation of the insights offered by the theory principle, framework, and predictions, fail to reproduce the basic phenomenology observed in data. Instead, we use the insight from theory as an integral building block to reconstruct a computational approach which reduces to the theory in the appropriate limit but leverages the addition of a fitting parameter to incorporate more nuanced considerations. In particular, we now relax the assumption that all fireflies immediately start flashing upon seeing any other one flash, since in practice there could be some time delay or imperfect information transfer, which could be made shorter if the firefly sees additional fireflies flashing too. The rate at which this delay is shortened in proportion to the number of flashing fireflies is given by the behavioral coupling between the fireflies, labeled $\beta$. When $\beta→∞$, this limit represents the idealization derived in the theory section: the strongly correlated limit, wherein a single firefly’s flashing is sufficient to immediately stimulate all others to also start flashing, while $\beta=0$ represents completely non-interacting fireflies.

The important distinction between this computational approach and traditional IF models is that as the system becomes more non-interacting (i.e., $\beta$ decreases), the individual behavior becomes more non-oscillatory and sporadic. Thus, incorporating the theoretical framework built up in previous sections is essential to give rise to emergent periodicity despite having non-oscillating individuals.

#### Formulation

We propose a simple numerical simulation based on the mechanism previously described. Following previous computational models (Ramírez Ávila et al., 2011; Ramírez Ávila et al., 2003; Ramírez Ávila et al., 2019), we implement a group of $N$ fireflies whose flashing dynamics is governed by charging and discharging processes which represent the time between two bursts and the duration of a burst, respectively. Here, for the sake of simplicity, we simulate bursts of only one flash in length. These processes are determined by both an agent’s internal characteristics and its interactions with the group. Specifically, the internal state of firefly i is characterized by variables $V$ and $𝜖$ whose evolution follows (Figure 4):

$$
\frac{dV_{i}(t)}{dt}=\frac{1}{T_{s_{i}}}ϵ_{i}(t)−\frac{1}{T_{d_{i}}}[1−ϵ_{i}(t)]+ϵ_{i}(t)\sumj=1N\beta_{ij}\delta_{ij}[1−ϵ_{j}(t)],
$$

which is a standard equation for the IF scheme. Here, $ϵ_{i}$ is a binary variable that is 1 when an individual is charging (quiet) and 0 when an individual is discharging (flashing). The state of $𝜖_{i}$ changes to 0 when reaching the threshold voltage $V=1$ , and switches back to 1 when the firefly has finished discharging at the threshold $(V=0)$. The time $T_{d}_{i}$ represents the flash length and is drawn directly from observed data, and the time $T_{s}_{i}$ represents the end-to-start interflash interval (Figure 4A). This value comes directly from the data in the following way: $T_{s}_{i}=T_{b}_{i}−T_{d}_{i}$ , where $T_{b}_{i}$ represents the start-to-start inter-flash interval for firefly $i$ , drawn directly from the input distribution envelope in Figure 3A. The firefly may be ‘pulled’ toward flashing sooner if detecting the flashes of neighboring fireflies, which is represented in the framework by the third term (Figure 4B). Here $\delta_{ij}\in{0,1}$ represents connectivity between agents and $\beta_{ij}$ is the coupling strength. For simplicity, here we use all-to-all connectivity ($\delta_{ij}=1$, $∀(i,j)$) and vary the common interaction $\beta_{ij}=\frac{\beta}{N}$ . The crucial difference with prior IF implementations is the introduction of stochasticity: $T_{b}_{i}$ is a random variable whose value is drawn from our experimental distributions of interburst intervals (Figure 3A), and $T_{d}_{i}$ is a random variable whose value is drawn from our previously published data illustrating the distribution of firefly flash lengths, as seen in Sarfati et al., 2020 (their Figure 7a). Each of these variables resets, for each agent, every time they switch state. In this stochastic IF framework, the variability between flashes is accounted for, while maintaining the overall structure of the IF model.

![Figure 4.](https://cdn.elifesciences.org/articles/78908/elife-78908-fig4-v3.jpg)

**Figure 4.:** The dynamics proceed as follows: for each flashing firefly $i$, follow three simple steps at each timestep. (1) Update $𝜖_{i}$ according to voltage value. If  $V_{i}$ == 1, update  $𝜖_{i}$ = 0; if $V_{i}$ is 0, update $𝜖_{i}$ is 1. (2) If  $𝜖_{i}$ = 0, flash. (3) Update their own voltage based on Equation 6. (A) A single firefly $i$’s dynamics. Dark bars indicate voltage values from 0 to 1. The start-to-start interflash interval $T_{b}_{i}$, end-to-start interflash interval $T_{s}_{i}$, and quiet period $T_{d}_{i}$, each of which is a random variable for each individual and subject to resampling after each flash event, are indicated below the trace. Flashing state $𝜖_{i}$ is indicated above, along with the times at which a flash is being actively emitted by the firefly. (B) Schematic of a second firefly $j$, with different parameters, interacting with firefly $i$ via integrate-and-fire $\beta$ donation. For simplicity, we only show a one-way interaction here, where donations occur from firefly $i$ to firefly $j$ and not the reverse. Note the non-linearity in the voltage trace as a flash by firefly $i$ triggers a larger gain in voltage between t=4 and t=5 and t=5 and t=6, indicated by the green bars. Firefly $i$’s second flash is ignored by firefly $j$ since it is already flashing (t=11, t=12).

#### Transition to periodicity

This simulation exhibits a transition to group periodicity as interactions between agents are increased. We define the group interburst interval as the time between one flash and the next flash produced by any other firefly in the swarm. For example, consider the case of $N=20$ (Figure 5D). When $\beta=0$ each firefly behaves purely individually and interburst intervals tend to aggregate towards small values due to the random unsynchronized flashing of the $N$ fireflies each with a flashing behavior typical of isolated individuals. This remains the case until the coupling strength, $\beta$, becomes large enough that there is enough of collective entrainment to align the flashes of the group. In these regimes, when one firefly flashes, it quickly triggers all others. All agents then reset their charging time at roughly the same moment, and the smallest $T_{b}$ selected by any individual firefly defines the duration between this flash and the group’s next flash. As a consequence, interburst intervals of the collective, $T_{b}$, shift to a larger value corresponding to the smallest time between flashes for an individual firefly ($t_{b0}$). This behavior can be seen easily in Figure 5, where wide distributions give way to progressively tighter shapes as $\beta$ and $N$ increase. We can quantify this transition by examining the characteristic peaks in the $T_{b}$ distribution. Peaks with a value below the minimum of the input distribution occur when beta is small, and pulsatile coupling is thus weakly pulling the flashes towards each other. At each value of $N$, however, Figure 5 shows a sharp transition wherein the beta value becomes high enough to cause enough coupling gain to produce synchronous flashes and the alignment of the start of the next burst. This drives the pace of the flashing to be set by the first flasher, which as $N$ increases becomes more likely to be on the lower end of the input distribution. The high-coupling peak is also naturally sharper at increasing $N$: at larger $N$, the probability that some $T_{b,i}$ approaches the minimum possible $T_{b}$ is higher, resulting in more regularity the collective flashing pattern (Figures 3E and 6).

![Figure 5.](https://cdn.elifesciences.org/articles/78908/elife-78908-fig5-v3.jpg)

**Figure 5.:** (A–E) Visual demonstration of the emergence of a collective periodicity above $T_{b_{0}}$ as $\beta$ ranges between 0–1 for each value of N, including (E) $N=100$, a value outside the scope of our experimental observations but that is relevant for the theoretical analysis.The lack of coupling in the first few rows produces noisy and cluttered collective interburst intervals as flashes from any individual are uncorrelated with those from its neighbors. As the coupling constant increases, a consistent interburst interval emerges at the peak of each distribution. (F) The relationship between the most probable interburst interval (the distribution peak) as $\beta$ and $N$ vary. The shaded regions represent the standard error of the distributions for each density. For small values of beta, the collective produces noisy distributions where the pulsatile coupling of flashes is not quite enough to pull the starts of bursts into alignment. However, as the coupling constant $\beta$ increases, individual flashes begin to trigger subsequent flashes in neighboring fireflies, causing the quiet periods of the individuals to line up and the emergence of a collective frequency at the fastest interval in each burst cycle. Each higher density simulated causes the peak of the distribution to both shift slightly downwards and become less variant, as it is progressively more likely for one individual in the swarm to drive the collective frequency towards intervals on the short end of the input distribution. A cartoon of this effect is shown in .

![Figure 6.](https://cdn.elifesciences.org/articles/78908/elife-78908-fig6-v3.jpg)

**Figure 6.:** Schematic illustration demonstrating the evolution of the collective burst distribution, i.e., the distribution of time intervals between collective bursts, $P_{N}(T)$, with increasing number of fireflies, $N$.$N=1$ corresponds to the intrinsic burst distribution of a single firefly, $b$. Evidently, the distribution of time intervals between collective bursts becomes a sharply peaked distribution with maximum probability peaked at a value larger than $T^{∗}$.

As our simulation has a single fitting parameter, namely the coupling strength $\beta$, we conduct a detailed comparison of the simulation and experimental data to infer the most likely value of $\beta$ for the P. carolinus system. A systematic parameter sweep over the values of $\beta$ and $N$ provides a set of $T_{b}$ interval distributions (Figures 5 and 7). We statistically compare the distributions generated by simulation with those obtained experimentally at each swarm density and find that the optimal values of $\beta$ to match the empirical distributions cluster around 0.15 when $N\leq15$ (and holds a higher value when $N=20$). This also corresponds with the transition point in the location of the mode of the distributions, as can be seen in Figure 5F.

![Figure 7.](https://cdn.elifesciences.org/articles/78908/elife-78908-fig7-v3.jpg)

**Figure 7.:** Two-sided Kolmogorov–Smirnov test results between the simulation results and experimental results at each $\beta$ and $N$.For the two-sided Kolmogorov–Smirnov test, the null hypothesis states that the two compared distributions can be drawn from the same underlying distribution: effectively, accepting the null hypothesis accepts the statistical probability that the distributions do not differ. All distributions were generated from ten simulations, each of 200000 simulation timesteps/30 min of real time. The best values for each $N=5,10,15,20$ are $\beta=0.16,\beta=0.16,\beta=0.20,\beta=0.30$.

## Discussion

In this work, we have proposed a synchronization mechanism that produces emergent periodicity and demonstrated its remarkable quantitative applicability to the synchronous periodic flashing of P. carolinus fireflies as observed in natural settings. In other, more commonly studied firefly species such as the P. frontalis, individuals are intrinsically oscillatory (Moiseff and Copeland, 2000), and thus can be modeled by traditional Kuramoto-like models which do not apply to species like ours. More recently, a new model based on the concept of elliptic bursters has been successful at producing many aspects of P. carolinus’ collective flashing, notably the intermittent (burst-type) synchrony. Yet, this model still assumes intrinsic periodicity between flash bursts (McCrea et al., 2022). In systems following our principle, individuals may behave erratically without any periodicity in their behavior, yet when brought together as a collective, their behavioral patterns become highly synchronized and periodic. Moreover, this effect increases with the number of fireflies present through a simple and intuitive behavioral pattern. Using this principle, we successfully predict the qualitative sharpening of the peak of the distribution of interval between flashes by simply using the interval between flashes of isolated individual fireflies and without requiring any fitting parameter. Further, our computational approach quantitatively builds on the predictions of the theory by letting the strength of coupling between fireflies vary and provides added insights.

Specifically, we have shown that the simple theoretical behavioral framework presented in this paper successfully reproduces the experimental distributions of interburst intervals for groups of $N$ fireflies (Figure 3B and E). All the input parameters for application of the framework as well as the computational approach come directly from experimental results in Sarfati et al., 2020 and subsequent field season results from the Great Smoky Mountains: the wide distribution of interburst intervals for single isolated fireflies, the two timescales required by the computational approach of charging time and discharging time are both data-driven from Sarfati et al., 2020. The only fitted parameter for the computational approach is the coupling strength $\beta$, which demonstrates a transition in the dynamics of the system where $\beta>0.1$ (Figure 5).

As shown in Figure 3, the chosen values for beta, the additional fitting parameter introduced in the agent-based simulation, are: $\beta=$ 0.16, 0.16, 0.20 and 0.30 respectively for $N=$ 5, 10, 15, 20. Perhaps it is intriguing that the optimum beta clusters around similar values for $N=$ 5, 10, 15, while the optimum beta for $N=$ 20 is significantly different. While we do not currently have an explanation for why the fitted parameter values are what they are, we note that the fitting curve is flat, implying that several beta values could possibly achieve a satisfactory fit. Further agent-based simulations could explore these findings more systematically and provide useful insights.

If the number of fireflies increases indefinitely, or if there are visual obstacles in the environment, the assumption that each firefly can practically immediately perceive when another firefly starts flashing will no longer hold. In this case, a finite time delay in perceiving the onset of the flashing could lead to an interburst interval that is greater than what is expected for the ideal case. The resulting interburst interval distribution will consequently be shifted to the right compared to the distribution given by Equation 5. While the general ideas underlying the theory framework will continue to hold, the mathematical formulation will need more sophistication to take these subtler effects into account.

Existing mathematical models on synchronous periodic behavior generally consider individuals to be intrinsically oscillatory, which either oscillate periodically in isolation or have their oscillations suppressed at low numbers through a sufficiently strong coupling with the environment. These models generally introduce variability through varying the frequencies of individual oscillators, and synchronization emerges spontaneously once the number or density of these coupled oscillators crosses some specific threshold. Conversely, in our proposed framework, individuals that are intrinsically non-oscillatory make use of the synchronization through coupling with other individuals to produce emergent oscillatory behavior, which becomes more regular as more individuals are added.

Existing mathematical models designed for emergent synchronization of individual oscillators could be extended to account for such behavior by replacing individual oscillators with stochastic sporadically firing individuals. Our framework is simply the simplest version and a starting point for such models. For example, systems of oscillators interacting with Kuramoto-style mean field and limit cycle oscillators such as those used in dynamical quorum sensing models tend to converge on the mean frequency of the heterogeneous group (Pikovsky et al., 2001; De Monte et al., 2007). However, observations of the P. carolinus fireflies show convergence on the fastest frequency in the repertoire of isolated individual fireflies and a synchronization of relaxation periods also seen in some coupled IF units (Bottani, 1996) which have been applied to many biological systems such as the synchronization of pacemaker cells in the mammalian heart (Jongsma et al., 1983; Jalife and Michaels, 1989). Yet the difference lies in the nature of this ‘fastest frequency’. In typical coupled IF units, this is the frequency of the individual oscillator with the fastest frequency. But in our system, the individuals fire sporadically, thus there is no specific frequency associated with any individual. Instead, the ‘fastest frequency’ is an emergent phenomenon in large groups, formed from the collective minimum interburst intervals of the individuals. While individual behavior may appear as extremely complex, collective behavior based on simple and credible behavioral rules converges towards a simple emergent phenomenon as we have demonstrated. This wait-and-start phenomenon might be observable in different biological systems as well.

The mathematical implementation of the proposed paradigm results in an interburst interval distribution that converges towards a unique possible value corresponding to the lower bound of the individual IB distribution, at increasing $N$. That means that in the limit of an infinitely large and entirely connected swarm, the smallest IBI always occurs. This is at odds with two empirical observations: (1) while most of the smallest IBI from an isolated firefly peak at 12 s and more, there are some residual values between 5 s and 12 s; (2) natural swarms comprising thousands of fireflies do not exhibit a 5 s period. We propose some explanation to reconcile these two facts.

First, fireflies are known to produce annex flash patterns, for instance, for alarm, in addition to the primary courtship phase. It is possible that isolated fireflies in a confining volume switch to different behavioral modes that produce atypical flash trains with intervals less than what they would typically do in an unobstructed environment with responding peers. Secondly, it is possible that the swarm buffers against unusual perturbations. More than finite-size effects, the main caveat here is that the swarm is not all-to-all connected, as we showed previously (Sarfati et al., 2021). In this case, the dynamics of the system would depend upon the speed of propagation of information across the swarm.

It is easy to imagine extensions of this work that leverage the spatial positions of individuals in the system using distance- or sight-dependent coupling to modify the adjacency matrix and add further complexity to the system, and this framework makes implementation of this idea ripe for a future endeavor. To provide direct evidence for the underlying mechanistic principles, further experiments are needed. A promising avenue consists of artificially and controllably tuning the interactions within the group, for example, artificial flash entrainment with an LED should be able to decrease the inter-burst interval.

## Materials and methods

### Experimental data

The individual and collective flashing of P. carolinus fireflies was recorded during 10 nights of field experiments in June 2020 in Great Smoky Mountains National Park (Tennessee, USA). The experimental protocol had been developed and implemented the previous year (Sarfati et al., 2020). In the natural swarm with hundreds to thousands of interacting fireflies, collective flashing consists of synchronous flashes every $T_{f}≃0.5s$, during periodic bursts $T_{b}≃12s$ (Figure 1C). However, it has been observed previously that individual fireflies in visual isolation do not exhibit burst periodicity. To characterize the onset of burst flashing, we performed experiments in a controlled environment. Fireflies were gently collected using insect nets, then placed individually in small plastic boxes, where species and sex were verified. Males were subsequently introduced into a secluded cuboid tent (approximately $1.5\times2\times1.5m^{3}$) made of breathable black fabric and covered by a black plastic tarp to ensure optimal visual isolation from fireflies on the outside. A GoPro Fusion 360° camera placed inside the tent recorded the entire volume at 30 or 60 frames-per-second (fps). Flashes were detected in video processing by intensity thresholding. Bursts were identified as (temporal) connected components of flashes less than 2 s apart. Interburst intervals $\tau_{b}$ were calculated as the duration between the first times of successive bursts. Tent experiments allow us to observe the collective behavior of a small and known number of fireflies in interaction, while providing enough space for them to fly, hence reducing experimental artifacts from excessive confinement. We observed the flashing behavior of both individual fireflies in isolation and groups of 5, 10, 15, and 20 fireflies. We observed 10 individual fireflies alone in the tent, over durations between 5 min and 85 min. We observed that although these fireflies produced flash trains at a frequency of about 2 Hz, the delay between successive trains was apparently randomly distributed, from a few seconds to tens of minutes. Then, we carried out three sets of experiments with 5, 10, 15, and 20 fireflies, using the segments between 9 min and 15 min. As previously reported, collective burst flashing only appears at about 15 fireflies.

### Experimental data correction

After the paper’s acceptance, a small subset of data points was updated for the reasons described in the correction notice (Sarfati et al., 2025). We repeated all analyses and confirmed that the findings are unaffected. Both the original and corrected datasets are publicly available.

### Theoretical framework

#### Behavior of moments and variance

For the following sections, we assume that individual isolated fireflies have identical interburst interval distributions. We show that as the number of fireflies ($N$) increases, the variance and all the moments of the interburst interval distribution decrease and the distribution eventually converges to a Dirac Delta function. From Equation 5, the $m^{th}$ moment for $N$ fireflies is

$$
⟨T_{N}^{m}⟩=N\int_{0}^{∞}[\int_{t}^{∞}b(t^{′})dt^{′}]^{N−1}t^{m}b(t)dt.
$$

Let the function $\gamma$ be defined as

$$
\gamma(t)=\int_{t}^{∞}b(t^{′})dt^{′},
$$

thus,

$$
⟨T_{N}^{m}⟩=−N\int_{t=0}^{∞}\gamma^{N−1}(t)t^{m}d(\gamma(t))=−\gamma^{N}(t)t^{m}|_{0}^{∞}+m\int_{0}^{∞}\gamma^{N}(t)t^{m−1}dt.
$$

We expect the distribution of inter-burst intervals to terminate at some large value and not go on to infinity (at most, they are limited by the finite lifespan of the fireflies), thus,

$$
⟨T_{N}^{m}⟩=m\int_{0}^{∞}\gamma^{N}(t)t^{m−1}dt.
$$

Now, at any given value of $t$ , $\gamma^{N}(t)\leq\gamma^{N−1}(t)$ . This inequality is strict whenever $0<\gamma(t)<1$ . Such a region exists unless $b(t)$ is a Dirac Delta function. If $b(t)$ is a Dirac Delta function, then $P_{N}(T_{b})=b(T_{b})$ . Otherwise,

$$
\int_{0}^{∞}\gamma^{N}(t)t^{m−1}dt<\int_{0}^{∞}\gamma^{N−1}(t)t^{m−1}dt,
$$



$$
⇒⟨T_{N}^{m}⟩<⟨T_{N−1}^{m}⟩.
$$

Thus, all moments strictly decrease as $N$ increases. From Equation 10, the variance for $N$ fireflies is

$$
V_{N}=2\int_{0}^{∞}\gamma^{N}(t)tdt−[\int_{0}^{∞}\gamma^{N}(t)dt]^{2}
$$

Writing the second term initially as a multiple integral over the entire $t,t^{′}>0$ plane,

$$
[\int_{0}^{∞}\gamma^{N}(t)dt]^{2}=∬\gamma^{N}(t)\gamma^{N}(t^{′})dtdt^{′}=2∬_{t>t^{′}}\gamma^{N}(t)\gamma^{N}(t^{′})dtdt^{′}.
$$

In the preceding step, we have used the symmetry of the integrand under $t↔t^{′}$ . The second term of Equation 13 can be similarly written down:

$$
2\int_{0}^{∞}\gamma^{N}(t)tdt=2∬_{t>t^{′}}\gamma^{N}(t)dtdt^{′}.
$$

Combining,

$$
V_{N}=2∬_{t>t^{′}}\gamma^{N}(t)(1−\gamma^{N}(t^{′}))dtdt^{′}.
$$

Thus,

$$
V_{N+1}−V_{N}=2∬_{t>t^{′}}[\gamma^{N+1}(t)(1−\gamma^{N+1}(t^{′}))−\gamma^{N}(t)(1−\gamma^{N}(t^{′}))]dtdt^{′}.
$$

The two $\gamma$ functions in the above integrand satisfy: $0\leq\gamma(t)\leq\gamma(t^{′})\leq1$, using the properties of the cumulant function. Thus,

$$
\gamma(t^{′})\gamma(t)\leq\gamma(t),⇒1−\gamma(t)\geq1−\gamma(t)\gamma(t^{′})\geq\gamma^{N}(t^{′})[1−\gamma(t)\gamma(t^{′})],⇒\gamma^{N}(t)[1−\gamma(t)]\geq\gamma^{N}(t)\gamma^{N}(t^{′})[1−\gamma(t)\gamma(t^{′})],⇒\gamma^{N}(t)−\gamma^{N+1}(t)\geq\gamma^{N}(t)\gamma^{N}(t^{′})−\gamma^{N+1}(t)\gamma^{N+1}(t^{′}).
$$

Rearranged, this tells us that the integrand in Equation 17 is non-positive (i.e., $\leq0$) everywhere. Thus, we have proved that $V_{N+1}\leqV_{N}$. In other words, the variance of the flashing distribution monotonically decreases with increasing number of fireflies.

Further, as $N→∞$, $\gamma^{N}(t)→0$ for all $t$ above $T_{0}$ (which is the maximum value of $t$ below which $b(t)$ is 0). For values of $t$ below $T_{0}$, $\gamma^{N}(t)=1$ irrespective of $N$. Thus, from Equation 10,

$$
limN→∞⟨T_{N}^{m}⟩=m\int_{0}^{T_{0}}t^{m−1}dt=T_{0}^{m},
$$

which represents moments of the Dirac Delta function $P_{N→∞}(T)=\delta(T−T_{0})$ . Thus, as the number of fireflies tends to infinity, the distribution of interburst intervals tends to a Dirac Delta function peaked at $T_{0}$.

#### Behavior of mode

For a single firefly interburst interval distribution $b(t)$ that is continuous for $t\geqT_{0}$ and differentiable for $t>T_{0}$ (where $T_{0}$ is the maximum value of $t$ below which $b(t)$ is 0), we show that the left-most mode shifts to the left as the number of fireflies ($N$) increases, unless it reaches $T_{0}$, in which case it stays at $T_{0}$ on increasing $N$.

The mode would be the local maximum of distribution $P_{N}$. Differentiating Equation 5,

$$
P_{N}^{′}(t)=N\gamma^{N−2}(t)[\gamma(t)b^{′}(t)−(N−1)b^{2}(t)].
$$

Let the left-most mode of $P_{N}$ be located at $t=t_{N}^{∗}$. If  $t_{N}^{∗}=T_{0}$, we have

$$
limt→T_{0}^{+}\gamma(t)b^{′}(t)−(N−1)b^{2}(t)<0.
$$

Now, on increasing the number of fireflies by 1, we still have

$$
limt→T_{0}^{+}\gamma(t)b^{′}(t)−Nb^{2}(t)<0⇒limt→T_{0}^{+}P_{N+1}^{′}(t)<0.
$$

Thus, the mode stays at $T_{0}$ . On the other hand, if $t_{N}^{∗}>T_{0}$ , we have

$$
\gamma(t_{N}^{∗})b^{′}(t_{N}^{∗})−(N−1)b^{2}(t_{N}^{∗})=0.
$$

Now, on increasing the number of fireflies by 1, we get

$$
\gamma(t_{N}^{∗})b^{′}(t_{N}^{∗})−Nb^{2}(t_{N}^{∗})<0⇒P_{N+1}^{′}(t_{N}^{∗})<0.
$$

Thus, $P_{N+1}$ increases toward the left of $t_{N}^{∗}$, i.e., $T_{0}\leqt_{N+1}^{∗}<t_{N}^{∗}$ . Thus, the left-most mode shifts to the left as the number of fireflies $(N)$ increases, unless it reaches $T_{0}$ , in which case it stays at $T_{0}$.

#### Numerical demonstration

We use numerical calculations to demonstrate how synchronized periodicity arises in an arbitrary system which follows the extreme-value statistics used in our theory. Here, we take an arbitrary probability distribution (given by $N=1$ label in Figure 6) and plot the distribution of the minimum of $N$ samples obtained from the $N=1$ distribution. The distributions for arbitrary $N$ are described by Equation 5 as derived previously. As $N$ increases, these distributions become sharply peaked with maximum probability peaked at a value larger than the minimum of the $N=1$ distribution. For a system in which these quantities represent the interval between events, for large $N$, those events would become highly periodic as the width of the distribution narrows.

### Agent-based simulations implementation details

#### Preparing input for the simulations

The input distribution for the simulations’ inter-burst interval $T_{b}$ is sampled directly from envelope distributions that encapsulate observations of one firefly’s inter-burst interval. These envelope distributions were generated using an interpolating $\beta$-spline between bin centers of the histogram of the distribution, normalized so that the area underneath the envelope sums to 1. The protocol for generating this envelope distribution is as follows:

#### Simulation parameters

All experiments carried out with this agent-based framework were conducted via simulation. The simulation outputs a time series of flashes and their positions. For each set of parameters, we ran simulations for thirty trials of 200,000 timesteps each. Parameters can be varied run-by-run via command-line arguments, which made a grid search parameter sweep over coupling strength $\beta$ and number of fireflies $N$ easily parallelizable. All other values required for the synchronization dynamics are instantiated from experimental observations as explained in the main text.
