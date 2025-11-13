# Visualization of currents in neural models with similar behavior and different conductance densities

## Authors

- Leandro M Alonso<sup>1</sup> ([ORCID: 0000-0001-8211-2855](https://orcid.org/0000-0001-8211-2855)) †
- Eve Marder<sup>1</sup> ([ORCID: 0000-0001-9632-5448](https://orcid.org/0000-0001-9632-5448))

### Affiliations

1. Volen Center and Biology Department Brandeis University Waltham United States

† Corresponding author

## Abstract

Conductance-based models of neural activity produce large amounts of data that can be hard to visualize and interpret. We introduce visualization methods to display the dynamics of the ionic currents and to display the models’ response to perturbations. To visualize the currents’ dynamics, we compute the percent contribution of each current and display them over time using stacked-area plots. The waveform of the membrane potential and the contribution of each current change as the models are perturbed. To represent these changes over a range of the perturbation control parameter, we compute and display the distributions of these waveforms. We illustrate these procedures in six examples of bursting model neurons with similar activity but that differ as much as threefold in their conductance densities. These visualization methods provide heuristic insight into why individual neurons or networks with similar behavior can respond widely differently to perturbations.

## Introduction

Experimental and computational studies have clearly demonstrated that neurons and circuits with similar behaviors can, nonetheless, have very different values of the conductances that control intrinsic excitability and synaptic strength. Using a model of the crustacean stomatogastric ganglion (STG), Prinz et al. (2004) showed that similar network activity can arise from widely different sets of membrane and synaptic conductances. Recent experimental measurements have shown two- to six-fold variability in individual components in the same identified neurons (Schulz et al., 2006; Schulz et al., 2007; Roffman et al., 2012; Swensen and Bean, 2005). The use of RNA sequencing and other molecular measurements have shown significant cell-to-cell variability in the expression of ion channels (Temporal et al., 2012; Temporal et al., 2014; Tobin et al., 2009). Together these results suggest that similar activities arise from different cellular and network mechanisms. Here, we use conductance-based models to explore how different these mechanisms are and how they respond to perturbation.

Because of the intrinsic variability, canonical models that capture the mean behavior of a set of observations are not sufficient to address these issues (Golowasch et al., 2002; Balachandar and Prescott, 2018). To incorporate intrinsic biophysical variability Prinz et al. (2004) introduced an ensemble modeling approach. They constructed a database with millions of model parameter combinations, analyzed their solutions to assess network function, and screened for conductance values for which the activity resembled the data (Calabrese, 2018). An alternative was used by Achard and De Schutter (2006). They combined evolutionary strategies with a fitness function based on a phase-plane analysis of the models’ solutions to find parameters that reproduce complex features in electrophysiological recordings of neuronal activity, and applied their procedure to obtain 20 very different computational models of cerebellar Purkinje cells. Here, we adopt a similar approach and apply evolutionary techniques to optimize a different family of landscape functions that rely on thresholds or Poincaré sections to characterize the models’ solutions.

In some respects, biological systems are a black-box because one cannot read out the values over time of all their underlying components. In contrast, computational models allow us to inspect how all the components interact and this can be used to develop intuitions and predictions about how these systems will respond to perturbations. Despite this, much modeling work focuses on the variables of the models that are routinely measured in experiments, such as the membrane potential. While in the models we have access to all state variables, this information can be hard to represent when many conductances are at play. Similarly, the effect of perturbations – such as the effect of partially or completely blocking or removing a particular channel – can be complex and also hard to display in a compact fashion. Here, we address these difficulties and illustrate two novel visualization methods. We represent the currents in a model neuron using stacked area plots: at each time step, we display the shared contribution of each current to the total current through the membrane. This representation is useful to visualize which currents are most important at each instant and allows the development of insight into how these currents behave when the system is perturbed. Perturbation typically results in drastic changes of the waveform of the activity and these changes depend on the kind of perturbation under consideration. Additionally, we developed a novel representation that relies on computing the probability of $V⁢(t)$, which allows a visualization of these changes. We illustrate the utility of these procedures using models of single neuron bursters or oscillators.

## Results

### Finding parameters: landscape optimization

The numerical exploration of conductance-based models of neurons is a commonplace approach to address fundamental questions in neuroscience (Dayan and Abbott, 2001). These models can display much of the phenomenology exhibited by intracellular recordings of single neurons and have the major advantage that many of their parameters correspond to measurable quantities (Herz et al., 2006). However, finding parameters for these models so that their solutions resemble experimental observations is a difficult task. This difficulty arises because the models are nonlinear, they have many state variables and they contain a large number of parameters (Bhalla and Bower, 1993). These models are complex, and we are not aware of a general procedure that would allow the prediction of how an arbitrary perturbation in any of the parameters will affect their solutions. The problem of finding sets of parameters so that a nonlinear system will display a target behavior is ubiquitous in the natural sciences. A general approach to this problem consists of optimizing a score function that compares features of the models’ solutions to a set of target features. Consequently, landscape-based optimization techniques for finding parameters in compartmental models of neurons have been proposed before (Achard and De Schutter, 2006; Druckmann et al., 2007; Ben-Shalom et al., 2012). Here, we employ these ideas to develop a family of score functions that are useful to find parameters so that their activities reach a desired target.

In this work, we started with a well-studied model of neural activity described previously (Liu et al., 1998; Goldman et al., 2001; Prinz et al., 2004; O'Leary et al., 2014). The neuron is modeled according to the Hodgkin-Huxley formalism using a single compartment with eight currents. Following Liu et al. (1998), the neuron has a sodium current, $I_{N⁢a}$; transient and slow calcium currents, $I_{C⁢a⁢T}$ and $I_{C⁢a⁢S}$; a transient potassium current, $I_{A}$; a calcium-dependent potassium current, $I_{K⁢C⁢a}$; a delayed rectifier potassium current, $I_{K⁢d}$; a hyperpolarization-activated inward current, $I_{H}$; and a leak current $I_{l⁢e⁢a⁢k}$.

We explored the space of solutions of the model using landscape optimization. The procedure consists of three steps. First, we generate voltage traces by integration of Equation 5 (Materials and methods). We then score the traces using an objective or landscape function that defines a target activity. Finally, we attempt to find minima of the objective function. The procedures used to build objective functions whose minima correspond to sets of conductances that yield the target activities are shown in Figure 1. Voltage traces were generated by integration of Equation 5 and were then scored according to a set of simple measures. The procedure is efficient in part because we chose measures that require little computing power and yet are sufficient to build successful target functions. For example, we avoid the use of Spike Density Functions (SDF) and Fourier transforms when estimating burst frequencies and burst durations. In this section, we describe target functions whose minima correspond to bursting and tonic activity in single compartment models. This approach can also be applied to the case of small circuits of neurons (Prinz et al., 2004).

![Figure 1.](https://cdn.elifesciences.org/articles/42722/elife-42722-fig1-v2.jpg)

**Figure 1.:** (A) Example model bursting neuron. The activity is described by the burst frequency and the burst duration in units of the period (duty cycle). The spikes detection threshold (red line) is used to determine the spike times. The ISI threshold (cyan) is used to determine which spikes are bursts starts (bs) and bursts ends (be). The slow wave threshold (blue line) is used to ensure that slow wave activity is separated from spiking activity. (B) Example model spiking neuron. We use thresholds as before to measure the frequency and the duty cycle of the cell. The additional slow wave thresholds (purple) are used to control the waveform during spike repolarization.

We begin with the case of bursters (Figure 1A). We targeted this type of activity by measuring the bursting frequency, the duty cycle, and the number of crossings at a threshold value to ensure that spiking activity is well separated from slow wave activity. To measure the burst frequency and duty cycle of a solution, we first compute the time stamps at which the cell spikes. Given the sequence of values $V={V_{n}}$ we determine that a spike occurs every time that $V$ crosses the spike detection threshold $T_{sp}=−20mV$ (red in Figure 1). We build a sequence of spike times $S={s_{i}}$ by going through the sequence of voltages ${V_{n}}$ and keeping the values of $n$ for which $V_{n}\leqT_{sp}andV_{n+1}>T_{sp}$ (we consider upward crossings). Each element $s_{i}$ of the sequence $S$ contains the time step at which the i-th spike is detected. Bursts are determined from the sequence of spike times $S$; if two spikes happen within a temporal interval shorter than $\delta_{s⁢p⁢t}=100⁢m⁢s⁢e⁢c$ they are part of a burst. Using this criterion we can find which of the spike times in $S$ correspond to the start and end of bursts. The starts (bs) and ends (be) of bursts are used to estimate the duty cycle and burst frequency. We loop over the sequence of spike times and determine that a burst starts at $s_{i}$ if $s_{i+1}−s_{i}<\delta_{spt}ands_{i}−s_{i−1}>\delta_{spt}$. After a burst starts, we define the end of the burst at $s_{k}$ if $s_{k+1}−s_{k}>\delta_{spt}ands_{k}−s_{k−1}<\delta_{spt}$. When a burst ends we can measure the burst duration as $\delta_{b}=s_{k}-s_{i}$ and since the next burst starts (by definition) at $s_{k+1}$ we also can measure the ‘period’ (if periodic) of the oscillation as $\tau_{b}=\delta_{b}+(s_{k+1}-s_{k})$. Every time a burst starts and ends we get an instance of the burst frequency $f_{b}=\frac{1}{\tau_{b}}$ and the duty cycle $d_{c}=\frac{\delta_{b}}{\tau_{b}}$. We build distributions of these quantities by looping over the sequence $S$ and define the burst frequency and duty cycle as the mean values $<f_{b}>$ and $<dc>$. Finally, we count downward crossings in the sequence $V_{n}$ with two slow wave thresholds $#_{s⁢w}$ (with $t_{s⁢w}=-50\pm1⁢m⁢V$) and the total number of bursts $#_{b}$ in $S$.

For any given set of conductances, we simulated the model for $20$ s and dropped the first $10$ s to mitigate the effects of transient activity. We then computed the burst frequency $<f_{b}>$, the duty cycle $<dc>$, the number of crossings with the slow wave thresholds $#_{s⁢w}$ and the number of bursts $#_{b}$. We discard unstable solutions; a solution is discarded if $std({f_{b}})\geq(<f_{b}>\times0.1)$ or $std({dc})\geq(<dc>\times0.2)$. If a solution is not discarded, we can use the following quantities to measure how close it is to the target behavior,

$$
E_{f}=(f_{tg}−<f_{b}>_{i})^{2}E_{dc}=(dc_{tg}−<dc>_{i})^{2}E_{sw}=(\frac{#_{sw}}{2}−#_{b})^{2}
$$

Here, $E_{f}$ measures the mismatch of the bursting frequency of the model cell with a target frequency $f_{t⁢g}$ and $E_{d⁢c}$ accounts for the duty cycle. $E_{s⁢w}$ measures the difference between the number of bursts and the number of crossings with the slow wave thresholds $t_{s⁢w}=-50\pm1⁢m⁢V$. Because we want a clear separation between slow wave activity and spiking activity, we ask that $#_{s⁢w}=#_{b}$. Note that if during a burst $V$ goes below $t_{s⁢w}$ this solution would be penalized (factor $\frac{1}{2}$ accounts for using two slow wave thresholds). Let $g$ denote a set of parameters, we can then define an objective function

$$
E(g)=\alphaE_{f}+\betaE_{dc}+\gammaE_{sw},
$$

where the weights $(\alpha,\beta,\gamma)$ determine the relative importance of the different sources of penalties. In this work we used $\alpha=1$, $\beta=100$, $\gamma=1$, and the penalties $E_{i}$ were calculated using $T=10$ seconds with $d⁢t=0.1$ msecs. The target behavior for bursters was defined by $d⁢c_{t⁢g}=0.2$ (duty cycle $20%$) ($d⁢c_{t⁢g}=0.2$) and bursting frequency $f_{t⁢g}=1⁢H⁢z$.

We can use similar procedures to target tonic spiking activity. Note that the procedure we described previously to determine bursts from the sequence of spike times $S$ is also useful in this case. If a given spike satisfies the definition of burst start and it also satisfies the definition of burst end then it is a single spike and the burst duration is zero. Therefore, we compute the bursts and duty cycles as before and ask that the the target duty cycle is zero.

There are multiple ways to produce tonic spiking in this model and some solutions display very different slow wave activity. To further restrict the models, we placed a middle threshold at $t_{m⁢i⁢d}=-35⁢m⁢V$ and detected downward crossings at this value. We defined $E_{l⁢a⁢g}$ as the lag between the upward crossings at the spiking threshold ($t_{s⁢p⁢k}=-20⁢m⁢V$) and downward crossings at $t_{mid}.$ $E_{lag}$ is useful because it takes different values for tonic spikers than it does for single-spike bursters even though their spiking patterns can be identical. Finally, we found that the model attempts to minimize $E_{l⁢a⁢g}$ at the expense of hyperpolarizing the membrane beyond $-50⁢m⁢V$ and introducing a wiggle that can be different in different solutions. To penalize this we included additional thresholds between $-35⁢m⁢V$ and $-45⁢m⁢V$, counted the number of downward crossings at these values $#_{m⁢i⁢d_{i}}$, and asked that these numbers are equal to the number of spikes $#_{s}$. With these definitions, we define the partial errors as before,

$$
E_{f}=(f_{tg}−<f_{b}>_{i})^{2}E_{dc}=(dc_{tg}−<dc>_{i})^{2}E_{mid}=\sumi(#_{mid_{i}}−#_{s})^{2}E_{sw}=(#_{sw})^{2}.
$$

The total error as a function of the conductances reads as follows,

$$
E(g)=\alphaE_{f}+\betaE_{dc}+\gammaE_{mid}+\deltaE_{sw}+ηE_{lag}.
$$

The values $\alpha=1000$, $\beta=1000$, $\gamma=100$, $\delta=100$ and $η=1$, produce solutions that are almost identical to the one displayed in Figure 1B.

In all cases, evaluation of the objective functions requires that the models are simulated for a number of seconds and this is the part of the procedure that requires most computing power. Longer simulations will provide better estimations for the burst frequency and duty cycle of the cells, but will linearly increase the time it takes to evaluate the objective function. If the simulations are shorter, evaluations of the objective function are faster but the minimization may be more difficult due to transient behaviors and its minima may not correspond to stable solutions. In this work, we minimized the objective function using a standard genetic algorithm (Holland, 1992; Goldberg and Holland, 1988). The choice of the optimization routine and the choice of the numerical scheme for the simulations are independent of the functions. See Materials and methods for details on the how we performed this optimization. The same functions can be utilized to estimate parameters in models with different channel types.

### Visualizing the dynamics of ionic currents: currentscapes

Most modeling work focuses on the variables of the models that are routinely measured in experiments such as the membrane potential as is shown in Figure 2A for a bursting neuron. While in the models we have access to all state variables, this information can be hard to represent when several current types are at play. One difficulty is that some currents like $N⁢a$ and $K⁢d$ vary over several orders of magnitude, while other currents like the $l⁢e⁢a⁢k$ and $H$ span smaller ranges. Additionally, the relative contribution of each current to the total flux through the membrane varies over time. Here, we introduce a novel representation that is simple and permits displaying the dynamics of the currents in a cohesive fashion.

![Figure 2.](https://cdn.elifesciences.org/articles/42722/elife-42722-fig2-v2.jpg)

**Figure 2.:** A simple visualization of the dynamics of ionic currents in conductance-based model neurons. (A) Membrane potential of a periodic burster. (B) Percent contribution of each current type to the total inward and outward currents displayed as pie charts and bars at times $T_{1}$ and $T_{2}$ (C) Percent contribution of each current to the total outward and inward currents at each time stamp. The black filled curves on the top and bottom indicate total inward outward currents respectively on a logarithmic scale. The color curves show the time evolution of each current as a percentage of the total current at that time. For example, at $t=T_{1}$ the total outward current is $≈2.5⁢n⁢A$ and the orange shows a large contribution of $K⁢C⁢a$. At $t=T_{2}$ the total outward current has increased to $≈4⁢n⁢A$ and the $K⁢C⁢a$ current is contributing less to the total.

At any given time stamp, we can compute the total inward and outward currents. We can then express the values of each current as a percentage of this quantity. The normalized values of the currents at any time can be displayed as a pie chart representing the share of each current type (Figure 2B). Because we want to observe how these percentages change in time, we display the shares in a bar instead of a disk. The currentscapes are constructed by applying this procedure to all time stamps and stacking the bars. These types of plots are known as stacked area plots and their application to this problem is novel. Figure 2C shows the currentscape of a periodically bursting model neuron over one cycle. The shares of each current type to the total inward and outward currents are displayed in colors, and the total inward and outward currents are represented by the filled black curves in logarithmic scale in the top and bottom.

### Visualizing changes in the waveforms as a parameter is changed

To visualize changes in the activity as a conductance is gradually removed we computed the distribution of membrane potential $V$ values. This reduction contains information about the waveform of the membrane potential, while all temporal information such as frequency can no longer be recovered. The number of times that a given value of $V$ is sampled is proportional to the time the system spends at that value. Figure 3A shows the distribution of $V$ for a periodic burster with $f_{b}≈1⁢H⁢z$ and $d_{c}≈20%$ sampled from $30$ s of simulation. The count is larger than $10^{4}$ for values between $-52⁢m⁢V$ and $-40⁢m⁢V$, and smaller than $10^{3}$ for $V$ between $-35⁢m⁢v$ and $20⁢m⁢V$. The areas of the shaded regions are proportional to the probability that the system will be observed at the corresponding $V$ range (Figure 3B). Note that the area of the dark gray region is $10^{5}$ while the light gray is $0.5\times10^{4}$, so the probability that the cell is, at any given time, in a hyperpolarized state is more than $20$ times larger than the probability that the cell is spiking.

![Figure 3.](https://cdn.elifesciences.org/articles/42722/elife-42722-fig3-v2.jpg)

**Figure 3.:** Membrane potential $V$ distributions.(A) Distribution of membrane potential $V$ values. The total number of samples is $N=2.2\times10^{6}$. Y-axis scale is logarithmic. The area of the dark shaded region can be used to estimate of the probability that the activity is sampled between $-50⁢m⁢V$ and $-40⁢m⁢V$, and the area of the light shaded region is proportional to the probability that $V⁢(t)$ is sampled between $-30⁢m⁢V$ and $20⁢m⁢V$. The area of the dark region is $20$ times larger than the light region. (B) The same distribution in (A) represented as a graded bar. (C) Distribution of $V$ as a function of $V$ and $g⁢N⁢a$, and waveforms for several $g⁢N⁢a$ values.The symbols indicate features of the waveforms and their correspondence to the ridges of the distribution of $V$. (D) Waveforms under two conditions and their correspondence to the ridges of the distribution of $V$. The ridges were enhanced by computing the derivative of the distribution along the $V$ direction.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/42722/elife-42722-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) The black trace corresponds to the membrane potential $V(t)$ during a spike within a burst (total time $5.4msec$). The y-axis is split into four equally sized bins (in colors) that span the full range of V values ($min(V)≈−60mV$ and $max(V)≈28mV$). The probability that $V(t)$ is observed in a given bin at a random instant is proportional to the total time $V(t)$ spends at that bin. This is indicated in colors by the preimage of each bin. (B) The total time spent in each bin can be interpreted as a coarse-grained probability distribution of $V(t)$. (C) (top) Membrane potential $V$, more bins and their pre-images. (bottom) Probability distribution of $V$. (D) Idem for $50$ bins. Note that the probability distribution of $V(t)$ displays sharp peaks for values of $V$ where local maxima (or minima) in time occur. This effect is more noticeable as the number of bins is increased.

The distribution of $V$ features sharp peaks. In many cases, the peaks in these distributions correspond to features of the waveform, such as the amplitudes of the individual spikes, or the minimum membrane potential (see Figure 3—figure supplement 1). This happens because every time the membrane potential reaches a maxima or minima (in time) the derivative $\frac{d⁢V}{d⁢t}$ is close to zero. The system spends more time close to values of $V$ where the velocity $\frac{d⁢V}{d⁢t}$ is small than in regions where $\frac{d⁢V}{d⁢t}$ is large, as it occurs during the flanks of spikes. Therefore, when we sample a solution at a random instant, it is more likely that $V$ corresponds to the peak of a spike than to either flank of the spike, while the most likely outcome is that $V$ is in the hyperpolarized range ($<-40⁢m⁢V$). In this particular burster, there are $12$ spikes in the burst but there are only $7$ peaks in the distribution (between $10⁢m⁢V$ and $20⁢m⁢V$); some spikes have similar amplitudes so they add to a larger peak in the distribution. The overall or total amplitude of the oscillation can be read from the distribution since the count of $V$ is zero outside a range ($-52⁢m⁢V$ to $20⁢m⁢V$). These distributions can also be represented by a graded bar as shown in Figure 3B. As conductances are gradually removed the waveform of the activity changes and so does the distribution of $V$ values.

Figure 3C shows how the distribution of $V$ changes as $g⁢N⁢a$ is decreased. The waveforms at a few values of $g⁢N⁢a$ are shown for reference. For each value in the range ($100%⁢g⁢N⁢a$ to $0%⁢g⁢N⁢a$ with $N=1001$ values) we computed the count $p⁢(V,g⁢N⁢a)$ and display $l⁢o⁢g_{10}⁢(p⁢(V,g⁢N⁢a)+1)$ in gray scales. In this example, the cell remains in a bursting regime up to $≈85%⁢g⁢N⁢a$ and transitions abruptly into a single-spike bursting mode for further decrements ($%80gNa$). The spikes produce thin ridges in the distribution that show how their individual amplitudes change. The colored symbols indicate the correspondence between features in the waveform and ridges in the distribution. In this example, the peak amplitudes of the spikes are similar for values of $g⁢N⁢a$ greater than $%85gNa$. After the transition, the amplitudes of the spikes are very different; two spikes go beyond $0⁢m⁢V$ and the rest accumulate near $-25⁢m⁢V$. As $g⁢N⁢a→0$ the oscillations collapse onto a small band at $≈-20⁢m⁢V$ and only one spike is left.

The distributions allow the visualization of the amplitudes of the individual spikes, the slow waves, and other features as the parameter $g⁢N⁢a$ is changed. To highlight ridges in the distributions, the center panel in Figure 3D shows the derivative $\partial_{V}⁡l⁢o⁢g_{10}⁢(p⁢(V))$ in color. This operation is similar to performing a Sobel filtering (Sobel and Feldman, 1968) of the image in Figure 3C. The traces on each side of this panel correspond to the control (left) and $80%⁢g⁢N⁢a$ conditions. Notice how the amplitudes of each spike, features of the slow wave, and overall amplitude correspond to features in the probability distribution. This representation permits displaying how the features of the waveform change for many values of the perturbation parameter $g⁢N⁢a$.

### The maximal conductances do not fully predict the currentscapes

We explored the solutions of a classic conductance-based model of neural activity using landscape optimization and found many sets of parameters that produce similar bursting activity. Inspired by intracellular recording performed in the Pyloric Dilator ($P⁢D$) neurons in crabs and lobsters we targeted bursters with frequencies $f_{b}≈1⁢H⁢z$ and duty cycles $d⁢c≈20%$. We built $1000$ bursting model neurons and visually inspected the dynamics of their currents using their currentscapes. Based on this, we selected six models that display similar membrane activity via different current compositions for further study. Because the models are nonlinear, the relationship between the dynamics of a given current type and the value of its maximal conductance is non-trivial. Figure 4 shows the values of the maximal conductances in the models (top) and their corresponding activity together with their currentscapes (bottom).

![Figure 4.](https://cdn.elifesciences.org/articles/42722/elife-42722-fig4-v2.jpg)

**Figure 4.:** (top) Maximal conductances of all model bursters. (bottom) The panels show the membrane potential of the cell and the percent contribution of each current over two cycles.

It can be difficult to predict the currentscapes based on the values of the maximal conductances. In most cases, it appears that the larger the value of the maximal conductance, the larger the contribution of the corresponding current. However, this does not hold in all cases. For example, burster (f) shows the largest $A$ current contribution, but bursters (c) and (e) have larger values of $g⁢A$. The maximal conductance of the $C⁢a⁢S$ current is low in model (f) but the contribution of this current to the total is similar to that in models (a) and (b). The values of $g⁢K⁢C⁢a$ are similar for bursters (e) and (f) but the contribution of this current is visibly different in each model.

### Response to current injection

The models produce similar activity with different current dynamics. To further reveal differences in how these activities are generated, we subjected the models to simple perturbations. We begin describing the response to constant current injections in Figure 5. Figure 5A and Figure 5B show the membrane potential of model (a) for different values of injected current. In control, the activity corresponds to regular bursting and larger depolarizing currents result in a plethora of different regimes. The distributions of inter-spike intervals (ISI) provide a means to characterize these regimes (Figure 5C). When the cell is bursting regularly such as in control and in the $0.8⁢n⁢A$ condition, the interspike interval distributions consist of one large value that corresponds to the interburst interval ($≈640⁢m⁢s⁢e⁢c$ in control) and several smaller values around $10⁢m⁢s⁢e⁢c$ which correspond to the ISI within a burst. There are values of current for which the activity appears irregular and correspondingly, the ISI values are more diverse. Figure 5B shows the response of the model to larger depolarizing currents. The activity undergoes a sequence of interesting transitions that result in tonic spiking. When $I_{e}=3.45⁢n⁢A$ the activity is periodic and there are $4$ ISI values. Larger currents result in $2$ ISI values and tonic spiking produces one ISI value. Figure 5C shows the ISI distributions (y-axis, logarithmic scale) for each value of injected current (x-axis).

![Figure 5.](https://cdn.elifesciences.org/articles/42722/elife-42722-fig5-v2.jpg)

**Figure 5.:** (A) (top) Control traces (no current injected $0nA$), regular bursting ($0.8nA$), irregular bursting $1.95nA$. (B) (top) Fast regular bursting ($f_{b}≈6Hz$), quadruplets ($3.45nA$), doublets ($3.75nA$) and singlets ($4.5nA$) (tonic spiking). (C) ISI distributions over a range of injected current.

All these bursters transition into tonic spiking regimes for depolarizing currents larger than $5⁢n⁢A$ but they do so in different ways. To explore these transitions in detail, we computed the inter-spike interval (ISI) distributions over intervals of $60⁢s⁢e⁢c$ for different values of the injected current. Figure 6 shows the ISI distributions for the six models at $N=1001$ equally spaced values of injected current over the shown range. The y-axis shows the values of all ISIs on a logarithmic scale and the x-axis corresponds to injected current. In the control, the ISI distribution consists of a few small values ($<100⁢m⁢s⁢e⁢c$) that correspond to the ISIs of spikes within a burst, and a single larger value ($>100⁢m⁢s⁢e⁢c$) that corresponds to the interval between the last spike of a burst and the first spike of the next burst. When the cell fires tonically the ISI distributions consist of a single value. The ISI distributions exhibit complicated dependences on the control parameter that result in beautiful patterns. For some current values, the cells produce small sets of ISI values indicating that the activity is periodic. However, this activity is quite different across regions. Interspersed with the regions of periodicity there are regions where the ISI distributions densely cover a band of values indicating non-periodic activity. Overall the patterns feature nested forking structures that are reminiscent of classical period doubling routes to chaos (Feigenbaum, 1978; Canavier et al., 1990).

![Figure 6.](https://cdn.elifesciences.org/articles/42722/elife-42722-fig6-v2.jpg)

**Figure 6.:** The panels show all ISI values of each model burster over a range on injected currents (vertical axis is logarithmic). All bursters transition into tonic spiking regimes for injected currents larger than $5nA$ and the details of the transitions are different across models.

### Extracting insights from these visualization tools

Detailed conductance-based models show complex and rich behaviors in response to all kinds of perturbations. There is a vast amount of information that can be seen in these models and their visualizations in Figures 7 - 15. It is entirely impossible for us to point out even a fraction of what can be seen or learned from these figures. Nonetheless, we will illustrate a few examples of what can be seen using these methods, knowing that these details will be different for models that are constructed in the future and analyzed using these and similar methods.

### Perturbing the models with gradual decrements of the maximal conductances

Figures 7 and 8 show the effects of gradually decreasing each of the currents in these bursters from $100%$ to $0%$ for all six models. This type of analysis might be relevant to some kinds of pharmacological manipulations or studies of neuromodulators that decrease a given current. The figures show $3$ s of data for each condition. In all panels, the top traces correspond to the control condition ($100%$) and the traces below show the activity that results from decreasing the maximal conductance. The dashed lines are placed for reference at $-50⁢m⁢V$ and $0⁢m⁢V$. Each panel shows the traces for $11$ values of the corresponding maximal conductance equally spaced between $100%$ (control) and $0%$ (completely removed). Each row of panels corresponds to a current type and the columns correspond to the different model bursters. Figure 7 displays the perturbations for the inward currents and Figure 8 shows the outward and leak currents.

![Figure 7.](https://cdn.elifesciences.org/articles/42722/elife-42722-fig7-v2.jpg)

**Figure 7.:** The figure shows the membrane potential $V$ of all model cells as the maximal conductance $g_{i}$ of each current is gradually decreased from $100%$ to $0%$ . Each panel shows $11$ traces with a duration of 3 s. Dashed lines are placed at $0mV$ and $−50mV$. The shading indicates values of maximal conductance for which the activity the models differs the most.

![Figure 8.](https://cdn.elifesciences.org/articles/42722/elife-42722-fig8-v2.jpg)

**Figure 8.:** The figure shows the membrane potential $V$ of all model cells as the maximal conductance $g_{i}$ of each current is gradually decreased from $100%$ to $0%$. Each panel shows $11$ traces with a duration of 3 s. Dashed lines are placed at $0mV$ and $−50mV$. The shading indicates values of maximal conductance for which the activity the models differs the most.

Taken together Figures 7 and 8 illustrate that each model (a-f) changes its behavior differently in response to decreases in each current. Additionally, decreases in some currents have only relatively small effects but decreases in others have much more profound effects. Because the description of all that can be seen in these figures is beyond the scope of this paper, we chose to focus on the effects of decreasing the $C⁢a⁢T$ because it has rich and unexpected behaviors.

The effect of decreasing the $C⁢a⁢T$ conductance is quite diverse across models. The activities of the models at the intermediate values of $g⁢C⁢a⁢T$ shows visible differences. When $g⁢C⁢a⁢T→0.7⁢g⁢C⁢a⁢T$ models (a), (b) and (c) show bursting activity at different frequencies and with different duty cycles. Models (d), (e) and (f) become tonic spikers at this condition, but their frequencies are different. Note that in the case of model (e) the spiking activity is not regular and the ISIs take several different values. When $g⁢C⁢a⁢T→0.2⁢g⁢C⁢a⁢T$ most models spike tonically but now (e) is regular and (f) shows doublets. When $C⁢a⁢T$ is completely removed, most models transition into a tonic spiking regime with the exception of model (a), that displays a low frequency bursting regime with duty cycle $≈0.5$.

### Gradually removing one current impacts the dynamics of all currents

Decreasing any conductance can trigger qualitative changes in the waveform of the membrane potential and in the contributions of each current to the activity. In Figure 9 we plot currentscapes for the effects of decreasing $C⁢a⁢T$ in model (f). This allows us to examine at higher resolution the changed contributions of currents that give rise to the interesting dynamics seen in Figure 7. Each panel in Figure 9 corresponds to a different decrement value and shows the membrane potential on top, and the currentscapes at the bottom. The top panels show $1$ second of data and correspond to the $100%⁢g⁢C⁢a⁢T$ (control), $90%⁢g⁢C⁢a⁢T$ and $80%⁢g⁢C⁢a⁢T$ conditions. The center panels show $0.1$ s of data for decrements ranging from $70%$ to $20%$ and the bottom panels show $2$ s for the $10%$ and $0%$ conditions. As $C⁢a⁢T$ is gradually removed the activity transitions from a bursting regime to a tonic spiking regime.

![Figure 9.](https://cdn.elifesciences.org/articles/42722/elife-42722-fig9-v2.jpg)

**Figure 9.:** Decreasing $CaT$ in model (f).The figure shows the traces and the currentscapes of model (f) as $CaT$ is gradually decreased. Top panels show $1$ second of data, center panels show $0.1$ seconds and the bottom panels show $2$ seconds (see full traces in Figure 8).

When $g⁢C⁢a⁢T→90%⁢g⁢C⁢a⁢T$ the neuron produces bursts but these become irregular and their durations change. Decreasing the conductance to $80%⁢g⁢C⁢a⁢T$ results in completely different activity. The spiking pattern appears to be periodic but there are at least three different ISI values. It is hard to see changes in the $C⁢a⁢T$ contribution across these conditions, but changes in other currents are more discernible. The contribution of the $A$ current that is large in the control and $90%⁢g⁢C⁢a⁢T$ conditions, is much smaller in the $80%⁢g⁢C⁢a⁢T$ condition. Additionally, the $N⁢a$ and $K⁢C⁢a$ currents show larger contributions, the $C⁢a⁢S$ current contributes less and the $H$ current is negligible. Further increments in simulated blocker concentration result in tonic spiking regimes with frequencies ranging from $≈20⁢H⁢z$ to $≈10⁢H⁢z$. The center panels in Figure 9 show the currentscapes for these conditions on a different time scale to highlight the contributions of $C⁢a⁢T$. The leftmost panel shows the $70%⁢g⁢C⁢a⁢T$ condition. In this panel, we placed vertical lines indicating the time stamps at which the peak of the spike and the minimum occur. Notice the large contribution of the $N⁢a$ current prior to the peak of the spike, and the large contribution of the $K⁢d$ current for the next $≈10⁢m⁢s⁢e⁢c$. When the membrane potential is at its minimum value the $C⁢a⁢T$ current dominates the inward currents and remains the largest contributor for the next $≈10⁢m⁢s⁢e⁢c$. The $C⁢a⁢T$ current reduces its share drastically by the time the $N⁢a$ current is visible and $C⁢a⁢S$ takes over. The contribution of $C⁢a⁢T$ remains approximately constant during repolarization and vanishes as the membrane becomes depolarized and the $N⁢a$ current becomes dominant. The effect of removing $C⁢a⁢T$ is visible on this scale. The waveform of the contribution remains qualitatively the same: largest at the minimum voltage and approximately constant until the next spike. However, the contribution of $C⁢a⁢T$ during repolarization becomes smaller, and for larger conductance decrements results in a thinner band. Finally, the bottom panels show the cases $10%⁢g⁢C⁢a⁢T$ and $0%⁢g⁢C⁢a⁢T$ which correspond to a two-spike burster and a tonic spiker, respectively. Note that even though the contribution of $C⁢a⁢T$ is barely visible, complete removal of this current results in a very different pattern. The activity switched from bursting to spiking and the current composition is different; $K⁢C⁢a$ disappeared in the $0%$ condition and the $A$ current takes over. Notice also the larger contribution of the $H$ current.

### Modeling current deletions

There has been a great deal of work studying the effects of genetic and/or pharmacological deletions of currents. One of the puzzles is why some currents, known to be physiologically important, can have relatively little phenotype in some, or all individuals. For this reason in Figures 10 and 11, we show the effects of deletion of each current in all six models. Each panel shows $2$ seconds of data. The inward currents are portrayed in Figure 10 and the outward and leak currents are shown in Figure 11.

![Figure 10.](https://cdn.elifesciences.org/articles/42722/elife-42722-fig10-v2.jpg)

**Figure 10.:** The figure shows the traces and currentscapes for all bursters when one current is completely removed.

![Figure 11.](https://cdn.elifesciences.org/articles/42722/elife-42722-fig11-v2.jpg)

**Figure 11.:** The figure shows the traces and currentscapes for all bursters when one current is completely removed.

Removal of some currents has little obvious phenotype differences across the population although the currentscapes are different, such as seen for the $g⁢N⁢a$ and $g⁢C⁢a⁢S$ cases. Removal of some currents produces similar phenotypes in most, but not all of the six models as seen in the $g⁢H$ and $g⁢A$ cases. Removal of $K⁢d$ had virtually identical effects both on the phenotype and the currents. For other currents, such as $K⁢C⁢a$ and the $L⁢e⁢a⁢k$, we find two types of responses with nearly half of the models for each case (the exception is model (d) $L⁢e⁢a⁢k$). In the case of the $C⁢a⁢T$ current both the phenotype and the currents composition are very diverse across models.

### Changes in waveform as conductances are gradually decreased

A fuller description of the behavior/phenotype of all of the models for all values of conductance decrements can be seen in Figures 12 and 13. These figures use the probability scheme described in Figure 3 and Figure 3—figure supplement 1. Using these methods, it is possible to see exactly how the waveforms change and the boundaries of activity for each model and each conductance. The panels show the ridges of the probability distributions $p⁢(V)$ of the membrane potential $V⁢(t)$ for $1001$ values of maximal conductance values (see Materials and methods). The probability of $V⁢(t)$ was computed using 30 s of data after dropping a transient period of $120$ s. It was estimated using $N_{b}=1001$ bins in the range $(-70,35)⁢m⁢v$ and $N≈2\times10^{6}$ samples for each maximal conductance value. The system spends more time in regions where $\frac{d⁢V}{d⁢t}≈0$ and is sampled more at those values. Therefore, features such as the amplitudes of the spikes appear as sharp peaks in the probability distributions. To highlight these peaks and visualize how they change as currents are gradually decreased, we plot the derivative or sharpness of the distribution in colors (see color scale in Figure 3D). Overall, these plots show that for any given current, there are ranges of the conductance values where a small change results in a smooth deformation of the waveform, and there are specific values at which abrupt transitions take place. As before there is too much detail to describe everything in these figures so we will discuss a subset of the features highlighted by this representation.

![Figure 12.](https://cdn.elifesciences.org/articles/42722/elife-42722-fig12-v2.jpg)

**Figure 12.:** Inward currents. The figure shows the ridges of the probability distribution of $V(t)$ as a function of $V$ and each maximal conductance $p(V,g_{i})$. The ridges of the probability distributions appear as curves and correspond to values of $V$ where the system spends more time, such as extrema. The panels show how different features of the waveform such as total amplitude, and the amplitude of each spike, change as each current is gradually decreased.

![Figure 13.](https://cdn.elifesciences.org/articles/42722/elife-42722-fig13-v2.jpg)

**Figure 13.:** Outward and leak currents. The figure shows the ridges of the probability distribution of $V(t)$ as a function of $V$ and each maximal conductance $p(V,g_{i})$. See Figure 12.

The top rows in Figure 12 correspond to removing the $N⁢a$ current in the models. Note that the minimum value of $V$ in control (left) is close to $-50⁢m⁢V$ and a small decrement in $g⁢N⁢a$ results in larger amplitude. The colored curves inside the envelopes correspond to the spikes’ amplitudes and features of the slow waves. For instance, when the $N⁢a$ current is completely removed (right) the amplitude of the oscillation is $≈40⁢m⁢V$ and the activity corresponds to a single-spike bursting mode. The spike amplitude is given by the top edge of the colored region and the curve near $≈-20⁢m⁢V$ indicates the burst ‘belly’: the membrane hyperpolarizes slowly after spike termination and there is a wiggle at this transition.

Removing $C⁢a⁢T$ in model (a) does not disrupt bursting activity immediately. Notice that the amplitude of the bursts remains approximately constant over a range of $g⁢C⁢a⁢T$ values. The dim red and yellow lines at $≈20⁢m⁢V$ show that the amplitudes of the spikes are different and have different dependences with $g⁢C⁢a⁢T$. When the model transitions into a tonic spiking regime, the amplitude of the spikes is the same and there is only one amplitude value. This value stays constant over a range but the minimum membrane potential decreases and the overall amplitude therefore increases. The model returns to a bursting regime for values of $g⁢C⁢a⁢T$ smaller than $30%⁢g⁢C⁢a⁢T$. Notice that in model (a) the membrane potential during bursts goes below $-50⁢m⁢V$, unlike in the control condition. Notice that the waveform of the membrane potential changes abruptly as $g⁢C⁢a⁢T$ is reduced and the models transition into a spiking regime. Model (f) is less resilient to this perturbation and this transition takes place at lower conductance values.

Removing $C⁢a⁢S$ does not much change the waveform, but it alters the temporal properties of the activity. The models remain bursting up to a critical value and the amplitude of the spikes was changed little. The features of the slow wave do not much change either except in model (f). Model (c) is less resilient to this perturbation since it becomes quiescent for lower decrements of the maximal conductance than the other models. The effect of gradually removing $H$ appears similar to $C⁢a⁢S$ in this representation. In this case again, the morphology of the waveform is less altered than its temporal properties (except in model (e) where a transition takes place).

Figure 13 shows the same plots for the outward and leak currents. The $A$ current in model (a) is very small ($g⁢A≈10⁢\mu⁢S$) and its removal has little effect on the activity. This translates into curves that appear as parallel lines indicating spikes with different amplitudes that remain unchanged. The rest of the models exhibit a transition into a different regime. The waveforms of this regime appears similar to the waveforms which result from removing $g⁢N⁢a$ (see Figure 7) but in this representation it is easier to observe differences such as the overall amplitude of the oscillation. The amplitude decreases as $g⁢N⁢a$ is decreased and increases as $g⁢A$ is decreased. Removing $K⁢C⁢a$ has a similar effect to removing $g⁢C⁢a⁢T$ in that the models transition into tonic spiking regimes. The difference is that the spiking regimes that result from removing $K⁢C⁢a$ have smaller amplitudes and also correspond to more depolarized states.

All models are very sensitive to removing $K⁢d$ and low values result in single-spike bursting modes with large amplitudes. Model (c) is least fragile to this perturbation and exhibits a visible range ($∼100%$ to $∼90%$) with bursting modes. These oscillations break down in a similar way to the $N⁢a$ case and display similar patterns. However, an important difference is that unlike in the $g⁢N⁢a$ case, the overall amplitude of the oscillation increases as $g⁢K⁢d$ is decreased. As before, the top edge corresponds to the amplitude of the large spike and the curves in the colored region correspond to extrema of the oscillation. After spiking, the membrane remains at a constant depolarized value ($≈-20⁢m⁢V$) for a long period and produces a high-frequency oscillation before hyperpolarization. The amplitude of this oscillation increases as $K⁢d$ is further decreased, and this results in a white curve that starts above $0⁢m⁢V$ and ends above $0⁢m⁢V$. The beginning of this curve corresponds to a high-frequency oscillation that occurs after spike termination. This type of activity is termed plateau oscillations and was reported in models of leech heart interneurons (Cymbalyuk and Calabrese, 2000) and in experiments in lamprey spinal neurons (Wang et al., 2014). These features are hardly visible in the traces in Figure 8 and are highlighted by this representation. Finally, the $L⁢e⁢a⁢k$ case appears similar to mixture of the $N⁢a$ and $A$ cases. The cells remain bursting over a range of values and some of them transition into a single-spike bursting mode that is different from the $K⁢C⁢a$ case.

### Changes in current contributions as conductances are gradually decreased

The key to the visualization method in Figures 12 and 13 is to consider $V⁢(t)$ not as a time series but as a stochastic variable with a probability distribution (see Figure 3 and supplement). The same procedure can be applied to the time series of each current. However, because the contributions of the currents are different at different times, and at different decrements of conductance values, it is not possible to display this information using the same scale for all channels. To overcome this, we proceed as in the currentscapes and instead focus on the normalized currents or shares to the total inward and outward currents (the rows of matrices $C^^{+}$ and $C^^{-}$, see Materials and methods). The current shares $C_{i}^⁢(t)$ correspond to the width of the color bands in the currentscapes and can also be represented by a time series that is normalized to the interval $[0,1]$. The probability distribution of $C_{i}^⁢(t)$ permits displaying changes in the contributions of each current to the activity as one current is gradually removed. Interpreting these distributions is straightforward as before: the number of times the system is sampled in a given current share configuration is proportional to the time the system spends there. The aim of plotting these distributions is to visualize how the currentscapes would change for all values of the conductance decrement. To illustrate this procedure, we return to $C⁢a⁢T$ to explore further the causes of the complex behavior of model (f) (see Figure 9).

Figure 14 shows the probability distributions of the current shares as $C⁢a⁢T$ is gradually decreased in model (f) (see also Figure 9 and Figure 14—figure supplement 1). The panels show the share of each current as $C⁢a⁢T$ is gradually decreased and the probability is indicated in colors. In control the $N⁢a$ and $C⁢a⁢T$ current shares are distributed in a similar way. Both currents can at times be responsible for $≈90%$ of the inward current, but most of the time they contribute $≈20%$. The $N⁢a$ current is larger right before spike repolarization and the $C⁢a⁢T$ amounts to $≈90%$ of the small ($≈5⁢n⁢A$) total inward current. For larger decrements, the system transitions into tonic spiking and the contribution of the $N⁢a$ current is more evenly distributed over a wider range. The contribution of the $C⁢a⁢T$ current is predominantly $≈15%$ and trends to zero as $g⁢C⁢a⁢T→0$. Note also that as the contribution of $C⁢a⁢T$ decreases, the contribution of $C⁢a⁢S$ increases to values larger than $75%$ while in control it contributes with $≈50%$. The contribution of the $H$ current is small ($\leq25%$) between $100%⁢g⁢C⁢a⁢T$ and $≈80%⁢g⁢C⁢a⁢T$; it becomes negligible between $≈80%⁢g⁢C⁢a⁢T$ and $≈20%⁢g⁢C⁢a⁢T$ and becomes dominant after $20%⁢g⁢C⁢a⁢T$. The $A$ current behaves similarly to the $H$. It contributes $≈90%$ of the (small $≈2⁢n⁢A$) total outward current before burst initiation and its contribution decreases drastically when the system transitions into tonic spiking. As $C⁢a⁢T$ is removed further the $A$ current is more likely to contribute with a larger share. The contribution of the $K⁢C⁢a$ current decreases as $g⁢C⁢a⁢T$ is decreased and some of it persists even when $g⁢C⁢a⁢T$ is completely removed. In contrast, the contribution of the $K⁢d$ current does not appear to change much and nor does its role in the activity.

![Figure 14.](https://cdn.elifesciences.org/articles/42722/elife-42722-fig14-v2.jpg)

**Figure 14.:** The panels show the probability distribution of the share of each current $C_{i}^(t)$ for model (f) as $CaT$ is decreased (see Figure 14—figure supplement 1).

![Figure 14—figure supplement 1.](https://cdn.elifesciences.org/articles/42722/elife-42722-fig14-figsupp1-v2.jpg)

**Figure 14—figure supplement 1.:** The Figure shows the relationship between the currentscapes and the distributions of current shares. (A) Distribution of $A$ current share to the total outward current for $1001$ values of $gCaT$ between $0%$ and $100%$. (B) Share of $A$ current as a time series. The $A$ current contributes with more than $50%$ of the outward current for most of the time. At $70%gCaT$ the cell spikes tonically and the $A$ contributes $50%$ of the outward current most of the time. The symbols indicate features in the waveform that are mapped to ridges in the distribution. (C) Currentscapes. (D) Idem (B) but for $KCa$. Notice the share of $KCa$ decreasing as $gCaT→0$. (E) Distribution of $KCa$ current share to the total outward current for $1001$ values of $gCaT$ between $0%$ and $100%$.

Performing the same analysis for all conductances results in a large amount of information. Despite this and because we are plotting the normalized currents or current shares, our representation allows us to display this information in a coherent fashion. As an example, in Figure 15 we show the effect of gradually decreasing each current on all the currents in model (c). The rows indicate which conductance is decreased and the columns show the effect of this perturbation on the corresponding current. The first row shows how the shares of each current change as the $N⁢a$ current is decreased. For instance, the effect of decreasing $g⁢N⁢a$ on the $N⁢a$ current (indicated by *) is as expected, with the maxima of the distribution trending to zero as $g⁢N⁢a→0$. The effect of removing $g⁢N⁢a$ on the other currents is non-trivial and is displayed along the same row. Notice that while the effect of removing a current on that same current (diagonal panels) is relatively predictable, the rest of the currents become rearranged in complicated ways.

![Figure 15.](https://cdn.elifesciences.org/articles/42722/elife-42722-fig15-v2.jpg)

**Figure 15.:** The panels show the probability distribution of the share of each current $C_{i}^(t)$ for model (c) as each current is decreased.

Again, a full description of these diagrams is beyond the scope of this work so we will only make some observations. When the pertubations are negligible or weak ($100%$ to $≈90%$) all currents play a role because there are periods of time in which they contribute to at least $≈20%$ of the total current. There are ranges of the conductances over which small changes result in smooth transformations of the current configuration, there are specific values at which sharp transitions take place, and these values are different depending on the current that is decreased. While some of this information can also be extracted from Figures 12 and 13, the diagrams in Figure 15 show how the currents get reorganized at these transitions. In addition, this arrangement is convenient for comparing the effect of decreasing each conductance on a given current. For example, the contributions of the $N⁢a$ and $K⁢d$ currents change little for most perturbations (except when these conductances are decreased). In contrast, the contributions of $C⁢a⁢T$, $C⁢a⁢S$, $H$, $K⁢C⁢a$, and the $l⁢e⁢a⁢k$ change more noticeably. Finally, the contribution of the $A$ current increases for most conductance decrements of any type, except at the transition values where it can grow or shrink in an abrupt manner.

## Discussion

There is an ever larger availability of experimental data to inform detailed models of identified neuron types (McDougal et al., 2017). Experimenters have determined the kinetics of many channel types, both in vertebrate and invertebrate neurons. There are also model databases with thousands of parameters which permit the development of large scale models of neural tissue (Bezaire et al., 2016). One difficulty in ensemble modeling is the necessity of incorporating the biological variability observed in some of the parameters – such as the conductances – at the same time that we require the models to capture some target activity. In other words, we may be interested in modeling a type of cell that displays some sterotypical behavior, and would like to obtain many different versions of such models. Two main approaches to this problem were introduced in the past. One consists of building a database of model solutions over a search domain and screening for target solutions: this considers all possible value combinations within an allowed range up to a numerical resolution and then applies quantitative criteria to determine which solutions correspond to the target activity (Prinz et al., 2004). An alternative approach consists of designing a target function that assigns a score to the models’ solutions in such a way that lower scores correspond to solutions that meet the targets, and then optimizing these functions (Achard and De Schutter, 2006; Druckmann et al., 2007; Ben-Shalom et al., 2012).

Both approaches have advantages and shortcomings. In the case of the database approach, trying all posible parameter combinations in a search range becomes prohibitively expensive as more parameters are allowed to vary. One advantage of this approach is that it provides a notion of how likely it is to find conductances within a search range that will produce the activity. In the landscape approach, we find solutions by optimization and – without further analysis – we do not know how likely a given solution type is. This approach has the advantage that it can be scaled to include large numbers of parameters. Additionally, if a particular solution is interesting, we can use genetic algorithms on successful target functions to ‘breed’ as many closely related models as desired. Ultimately, any optimization heuristic requires blind testing random combinations of the parameters, and developing quantitative criteria for screening solutions in a database results in some sort of score function, so the two approaches are complementary. A successful target function can determine if a random perturbation results in disruption of the activity and this can be used to perform population-based sensitivity analyses (Devenyi and Sobie, 2016).

Regardless of the optimization approach, most work is devoted to the design of successful target functions. Different modeling problems require different target functions (Roemschied et al., 2014; Fox et al., 2017; Migliore et al., 2018) and one challenge in their design is that sometimes we do not know a priori if the model contains solutions that will produce good minima. In addition, a poorly constrained target function can feature multiple local minima that could make the optimization harder, so even if there are good minima they may be hard to find. One difference between the landscape functions in Achard and De Schutter (2006) and the ones utilized here is that in their setup model solutions are compared to a target time series via a phase-plane method. The functions introduced in this work use an analysis based on Poincaré sections or thresholds to characterize the waveform and to define an error or score. Instead of targeting a particular waveform, we ask that some features of the waveform – such as the frequency and the burst duration – are tightly constrained, while other features – such as the concavity of the slow waves – can be diverse. This is motivated by the fact that across individuals and species, the activity of the pyloric neurons can be diverse but the neurons always fire in the same sequence and the burst durations have a well-defined mean. Our approach is successful in finding hundreds of models that display a target activity in minutes using a commercially available desktop computer. Application of evolutionary techniques to optimize these functions provides a natural means to model the intrinsic variability observed in biological populations.

One of the main benefits of computational modeling is that once a behavior of interest is successfully captured we then possess a mechanistic description of the phenomena that can be used to test ideas and inform experiments (Coggan et al., 2011; Lee et al., 2016; Devenyi and Sobie, 2016; Gong and Sobie, 2018). As the models gain biophysical detail these advantages wane in the face of the complexity imposed by larger numbers of variables and parameters. Conductance-based models of neural activity generate large amounts of data that can be hard to visualize and interpret. The development of novel visualization procedures has the potential to assist intuition into the details of how these models work (Gutierrez et al., 2013). Here, we introduced a novel representation of the dynamics of the ionic currents in a single compartment neuron. Our representation is simple and displays in a concise way the contribution of each current to the activity. This representation is easily generalizable to multi-compartment models and small networks, and to any type of electrically excitable cell, such as models of cardiac cells (Britton et al., 2017).

We employed these procedures to build many similar bursting models with different conductance densities and to study their response to perturbations. The responses of the models to current injections and gradual decrements of their conductances can be diverse and complex. Inspection of the ISI distributions revealed wide ranges of parameter values for which the activity appears irregular, and similar regimes can be attained by gradually removing some of the currents. Period doubling routes to chaos in neurons have been observed experimentally and in conductance-based models (Hayashi et al., 1982; Hayashi and Ishizuka, 1992; Szücs et al., 2001; Canavier et al., 1990; Xu et al., 2017). The sort of bifurcation diagrams displayed by these models upon current injection are qualitatively similar to those exhibited by simplified models of spiking neurons for which further theoretical insight is possible (Touboul and Brette, 2008). Period doubling bifurcations and low dimensional chaos arise repeatedly in neural models of different natures including rate models (Ermentrout, 1984; Alonso, 2017). The bursters studied here are close (in parameter space) to aperiodic or irregular regimes suggesting that such regimes are ubiquitous and not special cases.

We showed that in these model neurons similar membrane activities can be attained by multiple mechanisms that correspond to different current compositions. Because the dynamical mechanisms driving the activity are different in different models, perturbations can result in qualitatively different scenarios. Our visualization methods allow us to gather intuition on how different these responses can be and to explore the contribution of each current type to the neural activity. Even in the case of single compartment bursters, the response to perturbations of a population can be diverse and hard to describe. To gain intuition into the kind of behaviors the models display upon perturbation, we developed a representation based on the probability of the membrane potential $V$. This representation permits displaying changes in the waveform of $V$ as each current is blocked. This representation shows that the models respond to perturbations in different ways, but that there are also similarities among their responses. A concise representation of the effect of a perturbation is a necessary step towards developing a classification scheme for the responses.

## Materials and methods

Numerical data and data analysis and plotting code, sufficient to reproduce the figures in the paper are available on Dryad Digital Repository (https://dx.doi.org/10.5061/dryad.d0779mb).

### Model equations

The membrane potential $V$ of a cell containing $N$ channels and membrane capacitance $C$ is given by:

$$
C⁢\frac{d⁢V}{d⁢t}=I_{e}-\sumi=18I_{i}.
$$

Each term in the sum corresponds to a current $I_{i}=g_{i}⁢m^{p_{i}}⁢h^{q_{i}}⁢(V-E_{i})$ and $I_{e}$ is externally applied current. The maximal conductance of each channel is given by $g_{i}$, $m$ and $h$ are the activation and inactivation variables, the integers $p_{i}$ and $q_{i}$ are the number of gates in each channel, and $E_{i}$ is the reversal potential of the ion associated with the i-th current. The reversal potential of the Na, K, H and leak currents were kept fixed at $E_{N⁢a}=30⁢m⁢V$, $E_{K}=-80⁢m⁢V$, $E_{H}=-20⁢m⁢V$ and $E_{l⁢e⁢a⁢k}=-50⁢m⁢V$ while the calcium reversal potential $E_{C⁢a}$ was computed dynamically using the Nernst equation assuming an extracellular calcium concentration of $3\times10^{3}⁢\mu⁢M$. The kinetic equations describing the seven voltage-gated conductances were modeled as in Liu et al. (1998),

$$
\tau_{m_{i}}(V)\frac{dm_{i}}{dt}=m_{∞_{i}}(V)−m_{i}\tau_{h_{i}}(V)\frac{dh_{i}}{dt}=h_{∞_{i}}(V)−h_{i}.
$$

The functions $\tau_{m_{i}}⁢(V)$, $m_{∞_{i}}⁢(V)$, $\tau_{h_{i}}⁢(V)$ and $h_{∞_{i}}⁢(V)$ are based on the experimental work of Turrigiano et al., 1995 and are listed in refs. (Liu et al., 1998; Turrigiano et al., 1995). The activation functions of the $K_{C⁢a}$ current require a measure of the internal calcium concentration $[C⁢a^{+2}]$ (Liu et al., 1998). This is an important state variable of the cell and its dynamics are given by,

$$
\tau_{C⁢a}⁢\frac{d⁢[C⁢a^{+2}]}{d⁢t}=-C⁢a_{F}⁢(I_{C⁢a⁢T}+I_{C⁢a⁢S})-[C⁢a^{+2}]+C⁢a_{0}.
$$

Here, $Ca_{F}=0.94\frac{\muM}{nA}$ is a current-to-concentration factor and $Ca_{0}=0.05\muM$. These values were originally taken from Liu et al. and were kept fixed. Finally, $C=10⁢n⁢F$. The number of state variables or dimension of the model is $13$. We explored the solutions of this model in a range of values of the maximal conductances and calcium buffering time scales. The units for voltage are $m⁢V$, the conductances are expressed in $\mu⁢S$ and currents in $n⁢A$. Voltage traces were obtained by numerical integration of Equation 5 using a Runge-Kutta order $4$ (RK4) method with a time step of $d⁢t=0.1⁢m⁢s⁢e⁢c$ (Press et al., 1988). We used the same set of initial conditions for all simulations in this work $V=-51⁢m⁢V$, $m,h_{i}=0$ and $[C⁢a^{+2}]=5⁢\mu⁢M$. For some values of the parameters, the system (Equation 5) can display multistability (Cymbalyuk et al., 2002; Shilnikov et al., 2005).

### Optimization of target function

Optimization of the objective function Equation 2 is useful to produce sets of parameters $g$ that result in bursting regimes. In this work, the optimization was performed over a search space of allowed values listed here: we searched for $g_{N⁢a}\in[0,2\times10^{3}]$ ([$\mu⁢S$]), $g_{C⁢a⁢T}\in[0,2\times10^{2}]$, $g_{C⁢a⁢S}\in[0,2\times10^{2}]$, $g_{A}\in2\times[0,10^{2}]$, $g_{K⁢C⁢a}\in[0,2\times10^{3}]$, $g_{K⁢d}\in[0,2\times10^{2}]$, $g_{H}\in[0,2\times10^{2}]$, $g_{L}\in[0,2\times10]$, $\tau_{C⁢a}\in[0,10^{3}]$ ([msecs]). We minimized the objective function using a standard genetic algorithm Holland (1992). This is optimization technique is useful to produce large pools of different solutions and is routinely utilized to estimate parameters in biophysical models (see for example Assaneo and Trevisan, 2010). The algorithm was started with a population of $1000$ random seeds that were evolved for $≈10000$ generations. The mutation rate was $5%$. Fitter individuals were chosen more often to breed new solutions (elitism parameter was $1.2$ with $1$ corresponding to equal breeding probability). The computation was performed on a multicore desktop computer ($32$ threads) and takes about $≈1$ hr to produce good solutions.

### Currentscapes

The currentscapes are stacked area plots of the normalized currents. Although it is easy to describe their meaning, a precise mathematical definition of the images in Figure 2 can appear daunting in a first glance. Fortunately, the implementation of this procedure results in simple python code.

The time series of the $8$ currents can be represented by a matrix $C$ with $8$ rows and $n_{s⁢e⁢c⁢s}\times\frac{1}{d⁢t}=N$ columns. For simplicity, we give a formal definition of the currentscapes for positive currents. The definition is identical for both current signs and is applied independently for each. We construct a matrix of positive currents $C^{+}$ by setting all negative elements of $C$ to zero, $C_{i,j}^{+}=C_{i,j}∣C_{i,j}>0$ and $C_{i,j}^{+}=0∣C_{i,j}\leq0$. Summing $C^{+}$ over rows results in a normalization vector $n^{+}$ with $N$ elements $n_{j}^{+}=\sum_{i}C_{i,j}^{+}$. The normalized positive currents can be obtained as $C^^{+}=C^{+}/n^{+}$ (element by element or entry-wise product). Matrix $C^^{+}$ is hard to visualize as it is. The columns of $C^^{+}$ correspond to the shares of each positive current and can be displayed as pie charts (see Figure 2). Here, instead of mapping the shares to a pie we map them to a segmented vertical ‘churro’. The currentscapes are generated by constructing a new matrix $C_{S}$ whose number of rows is given by a resolution factor $R=2000$, and the same number of columns $N$ as $C$. Each column $j$ of $C^^{+}$ produces one column $j$ of $C_{S}$. Introducing the auxiliary variable $p_{i,j}=C^_{i,j}^{+}*R$ we can define the currentscape as,

$$
C_{S_{i,j}}=k∣\summkp_{m,j}\leqi<p_{k+1,j}+\summkp_{m,j}.
$$

The current types are indexed by $k\in[0,7]$ and we assume $\summk=0p_{m,j}=0$. The black filled curve in Figure 2B corresponds to the normalization vector $n^{+}$ plotted in logarithmic scale. We placed dotted lines at $5⁢n⁢A$, $50⁢n⁢A$ and $500⁢n⁢A$ for reference throughout this work. The currentscapes for the negative currents are obtained by applying definition (Equation 8) to a matrix of negative $C^{-}$ currents defined in an analogous way as $C^{+}$. Finally, note that matrices $C^^{+}$ and $C^^{-}$ are difficult to visualize as they are. The transformation given by definition (Equation 8) is useful to display their contents.

### ISI distributions

We inspected the effects of injecting currents in our models by computing the inter-spike interval ISI distributions. For this, we started the models from the same initial condition and simulated them for $580$ s. We dropped the first $240$ s to remove transient activity and kept the last $240$ s for analysis. Spikes were detected as described before. We collected ISI values for $N=1001$ values of injected current equally spaced between $-1⁢n⁢A$ and $5⁢n⁢A$.

### V distributions

To sample the distributions of $V$ we simulated the system with high temporal resolution ($d⁢t=0.001⁢m⁢s⁢e⁢c$ ) for $30$ s, after dropping the first $120$ s to remove transients. We then sampled the numerical solution at random time stamps and kept $2\times10^{6}$ samples $V={V_{i}}$ for each percent value. We took $1001$ values between $1$ and 0.

### Parameters

Model parameters used in this study are listed in Table 1.

**Table 1.**
 Parameters used in this study and error value.


<table>
  <thead>
    <tr>
      <th></th>
      <th>gNa</th>
      <th>gCaT</th>
      <th>gCaS</th>
      <th>gA</th>
      <th>gKCa</th>
      <th>gKd</th>
      <th>gH</th>
      <th>gL</th>
      <th>τC⁢a</th>
      <th>E(g)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>model (a)</td>
      <td>1076.392</td>
      <td>6.4056</td>
      <td>10.048</td>
      <td>8.0384</td>
      <td>17.584</td>
      <td>124.0928</td>
      <td>0.11304</td>
      <td>0.17584</td>
      <td>653.5</td>
      <td>0.051</td>
    </tr>
    <tr>
      <td>model (b)</td>
      <td>1165.568</td>
      <td>6.6568</td>
      <td>9.5456</td>
      <td>54.5104</td>
      <td>16.328</td>
      <td>110.7792</td>
      <td>0.0628</td>
      <td>0.10676</td>
      <td>813.88</td>
      <td>0.053</td>
    </tr>
    <tr>
      <td>model (c)</td>
      <td>1228.368</td>
      <td>7.0336</td>
      <td>11.0528</td>
      <td>117.5616</td>
      <td>16.328</td>
      <td>111.2816</td>
      <td>0.13816</td>
      <td>0.10676</td>
      <td>605.98</td>
      <td>0.027</td>
    </tr>
    <tr>
      <td>model (d)</td>
      <td>1203.248</td>
      <td>6.6568</td>
      <td>10.5504</td>
      <td>59.5344</td>
      <td>16.328</td>
      <td>111.4072</td>
      <td>0.0</td>
      <td>0.10676</td>
      <td>653.5</td>
      <td>0.471</td>
    </tr>
    <tr>
      <td>model (e)</td>
      <td>1210.784</td>
      <td>8.164</td>
      <td>6.28</td>
      <td>113.04</td>
      <td>12.56</td>
      <td>118.4408</td>
      <td>0.1256</td>
      <td>0.0314</td>
      <td>393.13</td>
      <td>0.109</td>
    </tr>
    <tr>
      <td>model (f)</td>
      <td>1245.952</td>
      <td>7.7872</td>
      <td>6.7824</td>
      <td>84.6544</td>
      <td>12.56</td>
      <td>113.9192</td>
      <td>0.02512</td>
      <td>0.0</td>
      <td>174.34</td>
      <td>0.047</td>
    </tr>
    <tr>
      <td>model (Figure 2)</td>
      <td>1228.368</td>
      <td>7.0336</td>
      <td>11.0528</td>
      <td>117.5616</td>
      <td>16.328</td>
      <td>110.7792</td>
      <td>0.13816</td>
      <td>0.10048</td>
      <td>605.98</td>
      <td>0.007</td>
    </tr>
    <tr>
      <td>model (Figure 3)</td>
      <td>895.528</td>
      <td>3.8936</td>
      <td>16.5792</td>
      <td>116.4312</td>
      <td>21.352</td>
      <td>115.6776</td>
      <td>0.0</td>
      <td>0.08792</td>
      <td>828.73</td>
      <td>0.058</td>
    </tr>
  </tbody>
</table>
