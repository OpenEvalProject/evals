# A neuronal least-action principle for real-time learning in cortical circuits

## Authors

- Walter Senn<sup>1</sup> ([ORCID: 0000-0003-3622-0497](https://orcid.org/0000-0003-3622-0497)) †
- Dominik Dold<sup>1</sup> ([ORCID: 0000-0001-7626-9960](https://orcid.org/0000-0001-7626-9960))
- Akos F Kungl<sup>1</sup>
- Benjamin Ellenberger<sup>1</sup> ([ORCID: 0000-0002-4787-0471](https://orcid.org/0000-0002-4787-0471))
- Jakob Jordan<sup>1</sup>
- Yoshua Bengio<sup>6</sup>
- João Sacramento<sup>7</sup>
- Mihai A Petrovici<sup>1</sup> ([ORCID: 0000-0003-2632-0427](https://orcid.org/0000-0003-2632-0427))

### Affiliations

1. Department of Physiology, University of Bern Bern Switzerland ([ROR:02k7v4d05](https://ror.org/02k7v4d05))
2. Kirchhoff-Institute for Physics, Heidelberg University Heidelberg Germany ([ROR:038t36y30](https://ror.org/038t36y30))
3. European Space Research and Technology Centre, European Space Agency Noordwijk Netherlands ([ROR:03h3jqn23](https://ror.org/03h3jqn23))
4. Insel Data Science Center, University Hospital Bern Bern Switzerland ([ROR:01q9sj412](https://ror.org/01q9sj412))
5. Electrical Engineering, Yale University New Haven United States ([ROR:03v76x132](https://ror.org/03v76x132))
6. MILA, University of Montreal Montreal Canada ([ROR:0161xgx34](https://ror.org/0161xgx34))
7. Department of Computer Science, ETH Zurich Zurich Switzerland ([ROR:05a28rw58](https://ror.org/05a28rw58))

† Corresponding author

## Abstract

One of the most fundamental laws of physics is the principle of least action. Motivated by its predictive power, we introduce a neuronal least-action principle for cortical processing of sensory streams to produce appropriate behavioral outputs in real time. The principle postulates that the voltage dynamics of cortical pyramidal neurons prospectively minimizes the local somato-dendritic mismatch error within individual neurons. For output neurons, the principle implies minimizing an instantaneous behavioral error. For deep network neurons, it implies the prospective firing to overcome integration delays and correct for possible output errors right in time. The neuron-specific errors are extracted in the apical dendrites of pyramidal neurons through a cortical microcircuit that tries to explain away the feedback from the periphery, and correct the trajectory on the fly. Any motor output is in a moving equilibrium with the sensory input and the motor feedback during the ongoing sensory-motor transform. Online synaptic plasticity reduces the somatodendritic mismatch error within each cortical neuron and performs gradient descent on the output cost at any moment in time. The neuronal least-action principle offers an axiomatic framework to derive local neuronal and synaptic laws for global real-time computation and learning in the brain.

## Introduction

Wigner’s remark about the ‘unreasonable effectiveness’ of mathematics in allowing us to understand physical phenomena Wigner, 1960 is famously contrasted by Gelfand’s quip about its ‘unreasonable ineffectiveness’ in doing the same for biology (Borovik, 2021). Considering the component of randomness that is inherent to evolution, this may not be all that surprising. However, while this argument holds just as well for the brain at the cellular level, ultimately brains are computing devices. At the level of computation, machine learning, and neuroscience have revealed near-optimal strategies for information processing and storage, and evolution is likely to have found similar principles through trial and error (Hassabis et al., 2017). Thus, we have reason to hope for the existence of fundamental principles of cortical computation that are similar to those we have found in the physical sciences. Eventually, it is important for such approaches to relate these principles back to brain phenomenology and connect function to structure and dynamics.

In physics, a fundamental measure of ‘effort’ is the action of a system, which nature seeks to ‘minimize.’ Given an appropriate description of interactions between the system’s constituents, the least-action principle can be used to derive the equations of motion of any physical system (Feynman et al., 2011; Coopersmith, 2017). Here, we suggest that in biological information processing, a similar principle holds for prediction errors, which are of obvious relevance for cognition and behavior.

Based on such errors, we formulate a neuronal least-action (NLA) principle which can be used to derive neuronal dynamics and map them to observed dendritic morphologies and cortical microcircuits. Within this framework, local synaptic plasticity at basal and apical dendrites can be derived by stochastic gradient descent on errors. The errors that are minimized refer to the errors in output neurons that are typically thought to represent motor trajectories, planned and encoded in cortical motor areas and ultimately in the spinal cord and muscles. In the context of motor control, a phenomenological ‘minimal action principle’ has previously been proposed that guides the planning and execution of movements (Feldman and Levin, 2009). Our neuronal least-action principle reformulates and formalizes the classical equilibrium point hypothesis (Latash, 2010) in a dynamical setting, linking it to optimality principles in sensory-motor control (Todorov, 2004).

Other attempts exist to link biological information processing and neural networks with the least-action principle, for instance by directly learning to reproduce a given trajectory (Amirikian and Lukashin, 1992), by minimizing the physical action for the muscle force generation by motor unit recruitment (Senn et al., 1995), minimizing cognitive prediction errors (Alonso et al., 2012), minimizing output errors with a weight-change regularization (Betti and Gori, 2016), minimizing psychomotor work (Fox and Kotelba, 2018), minimizing data transport through a network (Karkar et al., 2021), minimizing the discrimination information (Summers, 2021), or minimizing the free energy (Friston, 2010; Friston et al., 2022). Apart from the latter, however, these attempts remain far from the biology that seems to resist a formalization with the tool of physics – at least, when applied too strictly.

The fundamental novelty of our NLA principle is the way it deals with time. In physics, bodies interact based on where they are now, irrespective of what happens in the future. Living systems, instead, interact based on what could happen in the near future, and react early to stay alive. This difference is also mirrored in the way our NLA principle looks for an error-minimizing trajectory of brain states. We postulate that the brain trades with near-future states and seeks for a path that minimizes errors of these future states at any moment in time. Looking ahead towards what will likely happen allows the network for correcting the internal trajectory of deep neurons early enough so that the delayed output moves along the desired path. The notion of looking into the future to gate a dynamical system is also central in optimal control theory (as expressed by the Bellman equation, see e.g. Todorov, 2006). Yet, starting with a neuronal action is more principled as it includes the derivation of the dynamical system itself that will be optimally controlled.

The insight into the time structure of biological information processing allows us to express a simple form of a total ‘mismatch energy’ for our cortical neuronal networks, from which we derive the dynamic neuronal and synaptic laws.In short, the mismatch energy within a single pyramidal neuron is the squared prediction error between basal dendrites and the soma, together with the apical dendrites receiving a top-down feedback. The apical dendrites calculate a local prospective prediction error that looks ahead in time and overcomes neuronal integration delays (Figure 1a). As a consequence, the output neurons are corrected on the fly by the prospective error processing, pushing them in real time closer to the desired path. In addition, the prospective errors are suited for gradient learning of the sensory synapses on the basal dendrites. This gradient learning is proven to reduce the error in the output neurons at any moment in time.

![Figure 1.](https://cdn.elifesciences.org/articles/89674/elife-89674-fig1-v1.jpg)

**Figure 1.:** (a1) Sketch of a cross-cortical network of pyramidal neurons described by NLA. (a2) Correspondence between elements of NLA and biological observables such as membrane voltages and synaptic weights. (b1) The NLA principle postulates that small variations $\delta𝒖~$ (dashed) of the trajectories $𝒖~$ (solid) leave the action invariant, $\deltaA=0$. It is formulated in the look-ahead coordinates $𝒖~$ (symbolized by the spyglass) in which `hills' of the Lagrangian (shaded gray zones) are foreseen by the prospective voltage so that the trajectory can turn by early enough to surround them. (b2) In the absence of output nudging ($\beta=0$), the trajectory $𝒖(t)$ is solely driven by the sensory input, and prediction errors and energies vanish ($L=0$, outer blue trajectory at bottom). When nudging the output neurons towards a target voltage ($\beta>0$), somatodendritic prediction errors appear, the energy increases (red dashed arrows symbolising the growing ‘volcano’) and the trajectory $𝒖(t)$ moves out of the $L=0$ hyperplanes, riding on top of the `volcano' (red trajectory). Synaptic plasticity $W˙$ reduces the somatodendritic mismatch along the trajectory by optimally ‘shoveling down the volcano’ (blue dashed arrows) while the trajectory settles in a new place on the $L=0$ hyperplane (inner blue trajectory at bottom).

The NLA principle builds on and integrates various ingredients from existing work and theories. Output neurons, be they motor neurons or decision-making neurons, are postulated to be ‘nudged’ towards the desired target time course by additional synaptic input to the soma or the proximal apical dendrite, as described by Urbanczik and Senn, 2014. The cortical microcircuit with lateral ‘inhibition’ that seeks to cancel the top-down feedback in order to extract the apical error is inspired by Sacramento et al., 2018 and Haider et al., 2021. The energy-based approach for describing error-backpropagation for weak nudging is borrowed from the Equilibrium Propagation algorithm (Scellier and Bengio, 2017) that we generalize from a steady-state algorithm to real-time computation in cross-cortical microcircuits. Our theory covers both cases of weak and strong output nudging. For strong nudging, it likewise generalizes the least-control principle (Meulemans et al., 2022) and the prospective configuration algorithm (Song et al., 2024) from a steady-state to a dynamic real-time version, linking to optimal feedback control (Todorov and Jordan, 2002). Finally, the apical activity of our pyramidal neurons can be seen in the tradition of predictive coding (Rao and Ballard, 1999), where cortical feedback connections try to explain away lower-level activities. Yet, different from classical predictive coding, our prediction errors are integrated with the soma, and these errors are prospective in time. The errors extrapolate from current to future activities, so that their integration improves the network output in real time. The combination of an energy-based model with prospective coding in which neuronal integration delays are compensated on the fly enters also in Haider et al., 2021.

The paper is organized as follows: we first define the prospective somatodendritic mismatch error, construct out of this the mismatch energy of a network, and ‘minimize’ this energy to obtain the error-corrected, prospective voltage dynamics of the network neurons. We then show that the prospective error coding leads to an instantaneous and joint processing of low-pass filtered input signals and backpropagated errors. Applied to motor control, the instantaneous processing is interpreted as a moving equilibrium hypothesis according to which sensory inputs, network state, motor commands, and muscle feedback are in a self-consistent equilibrium at any point of the movement. We then derive a local learning rule that globally minimizes the somato-dendritic mismatch errors across the network, and show how this learning can be implemented through error-extracting cortical microcircuits and dendritic predictive plasticity.

## Results

### Somato-dendritic mismatch errors and the Lagrangian of cortical circuits

We consider a network of neurons – identified as pyramidal cells – with firing rates $r_{i}(t)$ in continuous time $t$. The somatic voltage $u_{i}$ of pyramidal neuron $i$ is driven by the close-by basal input current, $\sum_{j}W_{ij}r_{j}$, with presynaptic rates $r_{j}$ and synaptic weights $W_{ij}$, and an additional distal apical input $e_{i}$ that will be learned to represent a prospective prediction error at any moment in time (Figure 1a). While in classical rate-based neuron models the firing rate $r_{i}$ of a neuron is a function of the somatic voltage, $ρ(u_{i})$, the NLA principle implies that the effective firing rate of a cortical neuron is prospective. More concretely, the formalism derives a firing rate that linearly extrapolates from $ρ(u_{i})$ into the future with the temporal derivative, $r_{i}=ρ(u_{i})+\tauρ˙(u_{i})$, where $ρ˙(u_{i})$ represents the temporal derivative of $ρ(u_{i}(t))$. There is experimental evidence for such prospective coding in cortical pyramidal neurons where the instantaneous rate $r_{i}$ is in fact not only a function of the underlying voltage, but also a function of how quickly that voltage increases (see Figure 2a).

![Figure 2.](https://cdn.elifesciences.org/articles/89674/elife-89674-fig2-v1.jpg)

**Figure 2.:** (a1) The instantaneous spike rate of cortical pyramidal neurons (top) in response to sinusoidally modulated noisy input current (bottom) is phase-advanced with respect to the input adapted from Köndgen et al., 2008. (a2) Similiarly, in neuronal least-action (NLA), the instantaneous firing rate of a model neuron ($r=ρ(u)+\tauρ˙(u)$, black) is phase-advanced with respect to the underlying voltage ($u$, red, postulating that the low-pass filtered rate is a function of the voltage, $r‾=ρ(u)$). (b) Dendritic input in the apical tree (here called $e‾$) is instantaneously causing a somatic voltage modulation ($u$, modeling data from Ulrich, 2002). The low-pass filtering with $\tau$ along the dendritic shaft is compensated by a lookahead mechanism in the dendrite ($e=e‾+\taue‾˙$). In (Ulrich, 2002) a phase advance is observed even with respect to the dendritic input current, not only the dendritic voltage, although only for slow modulations (as here). (c) While the voltage of the first neuron ($u_{1}$) integrates the input rates $r_{in}$ from the past (bottom black upward arrows), the output rate $r_{1}$ of that first neuron looks ahead in time, $r_{1}=ρ(u_{1})+\tauρ˙(u_{1})$ (red dashed arrows pointing into the future). The voltage of the second neuron ($u_{2}$) integrates the prospective rates $r_{1}$ (top black upwards arrows). By doing so, it inverts the lookahead operation, resulting in an instantaneous transfer from $u_{1}(t)$ to $u_{2}(t)$ (blue arrow and circles).

The second central notion of the theory is the prospective error $e_{i}$, that we interpret as prospective somato-dendritic mismatch error in the individual network neurons, $e_{i}=(u_{i}+\tauu˙_{i})−\sum_{j}W_{ij}r_{j}$ . It is defined as a mismatch between the prospective voltage, $u_{i}+\tauu˙_{i}$, and the weighted prospective input rates, $\sum_{j}W_{ij}r_{j}$. In the same way, as the firing rates $r_{j}$ linearly extrapolate into the future given the current-voltages $u_{j}$ of the presynaptic neurons $j$, the postsynaptic error is based on the linear extrapolation of its current voltage $u_{i}$ using its temporal derivative, $u_{i}+\tauu˙_{i}$ . If the prospective error $e_{i}$ is low-pass filtered with time constant $\tau$, it takes the form $e‾_{i}=u_{i}−\sum_{j}W_{ij}r‾_{j}$, where $r‾_{j}$ is the corresponding low-pass filtered firing rate of the presynaptic neuron $j$ (that becomes a function of the presynaptic voltage, $r‾_{j}=ρ(u_{j})$ , see Methods, Sect. Euler-Lagrange equations as inverse low-pass filters). We refer to $e‾_{i}$ as a somato-dendritic mismatch error of neuron that, as compared to $e_{i}$, is non-prospective and instantaneous.

We next interpret the mismatch error $e‾_{i}$ in terms of the morphology and biophysics of pyramidal neurons with basal and apical dendrites. While the error $e_{i}$ is formed in the apical dendrite, this error is low-pass filtered and added to the somatic voltage $u_{i}$, that is also driven by the low-pass filtered basal input $\sum_{j}W_{ij}r‾_{j}$, so that  $u_{i}=\sum_{j}W_{ij}r‾_{j}+e‾_{i}$. From the perspective of the basal dendrites, the low-pass filtered apical error $e‾_{i}$ can be calculated as the difference between the somatic voltage and the own local low-pass filtered input, $e‾_{i}=u_{i}−\sum_{j}W_{ij}r‾_{j}$. The somatic voltage $u_{i}$ is assumed to be sampled in the basal dendrite by the backpropagating acting potentials (Urbanczik and Senn, 2014; Spicher et al., 2017). The apical error now appears as a ‘somato-basal’ mismatch error, that both are summarized as a somato-dendritic mismatch error. It tells the difference between ‘what a neuron does,’ which is based on the somatic voltage $u_{i}$, and ‘what the basal inputs think it should do,’ which is based on its own input $\sumW_{ij}r‾_{j}$ (Figure 1a2). The two quantities may deviate because neuron $i$ get additional ‘unpredicted’ apical inputs from higher-area neurons that integrate with the somatic voltage $u_{i}$. What cannot be predicted in $u_{i}$ by the sensory-driven basal input remains as somato-basal (somato-dendritic) mismatch error $e‾_{i}$.

Associated with this mismatch error is the somatodendritic mismatch energy defined for each network neuron $i\inN$ as the squared mismatch error,

$$
E_{i}^{M}=\frac{1}{2}e¯_{i}^{2}=\frac{1}{2}(u_{i}−\sum_{j}W_{ij}r¯_{j})^{2}.
$$

On a subset of output neurons of the whole network, $O⊆N$, a cost is defined as a function of the somatic voltage and some instructive reference signal such as targets or a reward. When a target trajectory $u_{o}^{*}(t)$ is available, the cost is defined at each time point as a squared target error,

$$
C_{o}=\frac{1}{2}(e¯_{o}^{∗})^{2}=\frac{1}{2}(u_{o}^{∗}−u_{o})^{2}
$$

Much more general mismatch energies and cost functions are conceivable, for instance, errors of the form $e‾_{i}=u_{i}−f_{i}(𝒖,t)$ for general functions $f_{i}$ of the voltage vector $𝒖$ and of time, encompassing conductance-based neurons, but also further dynamic variables can be included such as threshold adaptation (see Appendix 6). The cost represents a performance measure for the entire network that produces the output voltages $u_{o}(t)$ in response to some input rates $𝒓_{in}(t)$. The cost directly relates to behavioral or cognitive measures such as the ability of an animal or human to perform a particular task in real time. The target could be provided by explicit external supervision, for example, target movements in time encoded by $u_{o}^{*}(t)$, it could represent an expected reward signal, or it could arise via self-supervision from other internal prediction errors.

We define the Lagrangian (or ‘total energy’) of the network as a sum across all mismatch energies and costs, weighted by the nudging strength $\beta$ of the output neurons,

$$
L=\sumi\inNE_{i}^{M}+\beta\sumo\inOC_{o}=\frac{1}{2}\sumi\inN(u_{i}−\sum_{j}W_{ij}r¯_{j})^{2}+\frac{\beta}{2}\sumo\inO(u_{o}^{∗}−u_{o})^{2}.
$$

The low-pass filtered presynaptic rates, $r‾_{j}$, also encompass the external input neurons. While in classical energy-based approaches, $L$ is called the total energy, we call it the ‘Lagrangian’ because it will be integrated along real and virtual voltage trajectories as done in variational calculus (leading to the Euler-Lagrange equations, see below and Appendix 6). We ‘prospectively’ minimize $L$ locally across a voltage trajectory, so that, as a consequence, the local synaptic plasticity for $W_{ij}$ will globally reduce the cost along the trajectory (Theorem 1 below).

Due to the prospective coding, the Lagrangian can be minimal at any moment in time while the network dynamics evolve. This is different from the classical predictive coding (Rao and Ballard, 1999) and energy-based approaches (Scellier and Bengio, 2017; Song et al., 2024), where a stimulus needs to be fixed in time while the network relaxes to a steady state, and only there the prediction error is minimized (see Appendix 3).

### The least-action principle expressed for prospective firing rates

Motivated by the prospective firing in pyramidal neurons, we postulate that cortical networks strive to look into the future to prevent instantaneous errors. Each neuron tries to move along a trajectory that minimizes its own mismatch error $e‾_{i}$ across time (Figure 1b). The ‘neuronal currency’ with which each neuron ‘trades’ with others to choose its own error-minimizing trajectory is the future discounted membrane potential,

$$
u~(t)=\frac{1}{\tau}\int_{t}^{∞}u(t^{′})e^{−\frac{t^{′}−t}{\tau}}dt^{′}.
$$

The prospective voltages $u~$ are the ‘canonical coordinates’ entering the NLA principle, and in these prospective coordinates the overall network searches for a ‘least-action trajectory’. Since from $u~$ we can recover the instantaneous voltage via $u=u~−\tauu~˙$ (see Appendix 2), we can replace $u$ in the Lagrangian and obtain $L$ as a function of our new prospective coordinates $u~$ and the ‘velocities’ $u~˙$, i.e.,$L=L[𝒖~,𝒖~˙]$, where bold fonts represent vectors. Inspired by the least-action principle from physics, we define the neuronal action $A$ as a time-integral of the Lagrangian,

$$
A=\int_{t_{1}}^{t_{2}}L[𝒖~(t),𝒖~˙(t)]dt.
$$

The NLA principle postulates that the trajectory $𝒖~(t)$ keeps the action $A$ stationary with respect to small variations $\delta𝒖~$ (Figure 1b1). In other words, nature chooses a trajectory such that, when deviating a little bit from it, say by $\delta𝒖~$, the value of $A$ will not change (or at most up to second order in the variation), formally $\deltaA=0$. The motivation to search for a trajectory that keeps the action stationary is borrowed from physics. The motivation to search for a stationary trajectory by varying the near-future voltages $𝒖~$, instead of $𝒖$, is assigned to the evolutionary pressure in biology to ‘think ahead of time.’ To not react too late, internal delays involved in the integration of external feedback need to be considered and eventually need to be overcome. In fact, only for the ‘prospective coordinates’ defined by looking ahead into the future, even when only virtually, will a real-time learning from feedback errors become possible (as expressed by our Theorems below).

The equations of motion that keep the action stationary with respect to these prospective coordinates are known to satisfy the Euler-Lagrange equations.

$$
\frac{∂L}{∂u~_{i}}−\frac{d}{dt}\frac{∂L}{∂u~˙_{i}}=0.
$$

Applying these equations to our Lagrangian yields a prospective version of the classical leaky integrator voltage dynamics, with rates $𝒓$ and errors $𝒆$ that are looking into the future (Methods, Sects. Euler-Lagrange equations as inverse low-pass filters, Deriving the network dynamics from the Euler-Lagrange equations),

$$
\tauu˙=−u+Wr+e,
$$



$$
e¯=r¯_{net}^{′}⋅W_{net}^{T}e¯+\betae¯^{∗}.
$$

The ‘$⋅$’ denotes the component-wise product, and the weight matrix splits into weights from input neurons and weights from network neurons, $𝑾=(𝑾_{in},𝑾_{net})$. While for output neurons a target error can be defined, $e‾_{o}^{*}=u_{o}^{*}−u_{o}$, for non-output neurons i no target exists and we hence set $e‾_{i}^{*}=0$. In a control theoretic framework, the neuronal dynamics (Equation 7a) represent the state trajectory, and the adjoint error dynamics Equation 7b represent the integrated costate trajectory (Todorov, 2006).

From the point of view of theoretical physics, where the laws of motion derived from the least-action principle contain an acceleration term (as in Newton’s law of motion, like $mx¨=−x+F$ for a harmonic oscillator), one may wonder why no second-order time derivative appears in the NLA dynamics. As an intuitive example, consider driving into a bend. Looking ahead in time helps us to reduce the lateral acceleration by braking early enough, as opposed to braking only when the lateral acceleration is already present. This intuition is captured by minimizing the neuronal action $A$ with respect to the discounted future voltages $u~_{i}$ instead of the instantaneous voltages $u_{i}$. Keeping up an internal equilibrium in the presence of a changing environment requires looking ahead and compensating early for the predicted perturbations. Technically, the acceleration disappears because the Euler-Lagrange operator (Equation 6) turns into a lookahead-gradient operator, $\frac{∂}{∂u~_{i}}−\frac{d}{dt}\frac{∂}{∂u~˙_{i}}=(1+\frac{d}{dt})\frac{∂}{∂u_{i}}$, since the $u~¨_{i}$ is absorbed via $u~˙_{i}−\tauu~¨_{i}=u˙_{i}$ (see Methods, Sect. Euler-Lagrange equations as inverse low-pass filters, and Appendix 6 for the link to the least-action principle in physics).

Mathematically, the voltage dynamics in Equation 7a specifies an implicit differential equation since $𝒖˙(t)$ also appears on the right-hand side. This is because the prospective rates $𝒓=ρ(𝒖)+\tauρ˙(𝒖)$ include $𝒖˙$ through $ρ˙(u)=ρ^{′}(u)⋅u˙$. Likewise, the prospective errors $𝒆=𝒆‾+\tau𝒆‾˙$, with $𝒆‾$ given in Equation 7b and plugged into Equation 7a, imply $𝒖˙$ through $e¯˙(u)=e¯^{′}(u)⋅u˙$. Nevertheless, the voltage dynamics can be stably run by replacing $𝒖˙(t)$ on the right-hand side of Equation 7a with the temporal derivative $𝒖˙(t−dt)$ from the previous time step (technically, the Hessian $(1−𝑾𝝆^{′}−𝒆‾^{′})$ is required to be strictly positive definite, see Methods Sect. From implicit to explicit differential equations and Appendix 3). This ensures that the voltage dynamics of Equation 7a, Equation 7b can be implemented in cortical neurons with a prospective firing and a prospective dendritic error (see Figure 2).

The error expression in Equation 7b is reminiscent of error backpropagation Rumelhart et al., 1986 and can in fact be related (Methods, Sect. Deriving the error backpropagation formula). Formally, the errors are backpropagated via transposed network matrix, $𝑾_{net}^{T}$, modulated by $r‾_{i}^{′}$, the derivative of $r‾_{i}=ρ(u_{i})$ with respect to the underlying voltage. While the transpose can be constructed with various local methods see Akrout et al., 2019; Max et al., 2022 in our simulations we mainly adhere to the phenomenon of feedback alignment (Lillicrap et al., 2016) and consider fixed and randomized feedback weights $𝑩$ (unless stated differently). Recent control theoretical work is exploiting the same prospective coding technique as expressed in Equation 7a, Equation 7b to tackle general time-varying optimization problems see Simonetto et al., 2020 for a review and Appendix 3 for the detailed connection.

### Prospective coding in neurons and instantaneous propagation

The prospective rates and errors entering via $𝒓$ and $𝒆$ in the NLA (Equation 7a) are consistent with the prospective coding observed in cortical pyramidal neurons in vitro (Köndgen et al., 2008). Upon sinusoidal current injection into the soma, the somatic firing rate is advanced with respect to its voltage (Figure 2a), effectively compensating for the delay caused by the current integration. Likewise, sinusoidal current injection in the apical tree causes a lag-less voltage response in the soma (Figure 2b, Ulrich, 2002). While the rates and errors in general can be reconstructed from their low-pass filterings via $𝒓=𝒓‾+\tau𝒓‾˙$ and $𝒆=𝒆‾+\tau𝒆‾˙$, they become prospective in time because $𝒓‾$ and $𝒆‾$ are themselves instantaneous functions of the voltage $𝒖$, and hence $𝒓$ and $𝒆$ depend on $𝒖˙$. The derivative of the membrane potential implicitly also appears in the firing mechanism of Hodgkin-Huxley-type conductances, with a quick depolarization leading to a stronger sodium influx due to the dynamics of the gating variables (Hodgkin and Huxley, 1952). This advances the action potential as compared to a firing that would only depend on $𝒖$, not $𝒖˙$, giving an intuition of how such a prospective coding may arise. A similar prospective coding has been observed for retinal ganglion cells (Palmer et al., 2015) and cerebellar Purkinje cells (Ostojic et al., 2015), making a link from the visual input to the motor control.

To understand the instantaneous propagation through the network, we low-pass filter the dynamic equation $𝒖+\tau𝒖˙=𝑾𝒓+𝒆$ (obtained by rearranging Equation 7a), with $𝒆‾$ given by Equation 7b, to obtain the somatic voltage $𝒖=𝑾𝒓‾(𝒖)+𝒆‾(𝒖)$. At any point in time, the voltage is in a moving equilibrium between forward and backpropagating inputs. Independently of the network architecture, whether recurrent or not, the output is an instantaneous function of the low-pass filtered input and a putative correction towards the target, $𝒖_{𝒐}(t)=𝑭_{W}(𝒓‾_{in}(t),𝒆‾_{𝒐}^{*}(t))$, see Figure 2C and Methods, Sect. Proving theorem 1 (rt-DeEP). The mapping again expresses an instantaneous propagation of voltages throughout the network in response to both, the low-pass filtered input $𝒓‾_{in}$ and feedback error $𝒆‾_{𝒐}^{*}$. This instantaneity is independent of the network size, and in a feed-forward network is independent of its depths (see also Haider et al., 2021, where the instantaneity is on the rates, not the voltages). In the absence of the look-ahead activity, each additional layer would slow down the network relaxation time.

Notice that an algorithmic implementation of the time-continuous dynamics of a $N$-layer feedforward network would still need $N$ calculation steps until information from layer 1 reaches layer $N$. However, this does not imply that an analog implementation of the prospective dynamics will encounter delays. To see why, consider a finite step-change $Δ𝒖_{1}$ in the voltage of layer 1. In the absence of the look-ahead, $Δ𝒖_{1}$ was mapped within the infinitesimal time interval $dt$ to an infinitesimal change $d𝒖_{2}$ in the voltages of layer 2. But with a prospective firing rate, $r_{1}=ρ(u_{1})+\tauρ^{′}(u_{1})⋅u˙_{1}$, a step-change $Δ𝒖_{1}$ translates to a delta-function in $𝒓_{1}$, this in turn to a step-change in the low-pass filtered rates $Δ𝒓‾_{1}$, and therefore within $dt$ to a step-change $Δ𝒖_{2}$ in the voltages $𝒖_{2}$ of the postsynaptic neurons (Figure 2c). Iterating this argument, a step-change $Δ𝒖_{1}$ propagates ‘instantaneously’ through $N$ layers within the ‘infinitesimal’ time interval $Ndt$ to a step-change $Δ𝒖_{N}$ in the last layer. When run in a biophysical device in continuous time that exactly implements the dynamical Equation 7a, the implementation becomes an instantaneous computation (since $dt→0$). Yet, in a biophysical device, information has to be moved across space. This typically introduces further propagation delays that may not be captured in our formalism where low-pass filtering and prospective coding cancel each other exactly. Nevertheless, analog computation in continuous time, as formalized here, offers an idea to ‘instantaneously’ realize an otherwise time-consuming numerical recipe run on time-discrete computing systems that operate with a finite clock cycle.

### Prospective control and the moving equilibrium hypothesis

Crucially, at the level of the voltage dynamics (Equation 7a) the correction is based on the prospective error $𝒆$. This links our framework to optimal control theory and motor control where delays are also taken into account, so that a movement can be corrected early enough (Wolpert and Ghahramani, 2000; Todorov and Jordan, 2002; Todorov, 2004). The link between energy-based models and optimal control was recently drawn for strong nudging ($\beta→∞$) to learn individual equilibrium states (Meulemans et al., 2022). Our prospective error $𝒆(t)$ appears as a ‘controller’ that, when looking at the output neurons, pushes the voltage trajectories toward the target trajectories. Depending on the nudging strength $\beta$, the control is tighter or weaker. For infinitely large $\beta$, the voltages of the output neurons are clamped to the time-dependent target voltages, $u_{o}=u_{o}^{*}$ (implying $e_{o}^{*}=0$), while their errors, $e‾_{o}=u_{o}−(𝑾𝒓‾)_{o}$, instantaneously correct all network neurons. For small $\beta$, the output voltages are only weakly controlled, and they are dominated by the forward input, $u_{o}≈(W𝒓‾)_{o}$.

To show how the NLA principle with the prospective coding globally maps to cortico-spinal circuits we consider the example of motor control. In the context of motor control, our network mapping $𝒖_{𝒐}=𝑭_{W}(𝒓‾_{in},𝒆‾_{𝒐}^{*})$ can be seen as a forward internal model that quickly calculates an estimate of the future muscle length $𝒖_{𝒐}$ based on some motor plans, sensory inputs, and the current proprioceptive feedback (Figure 3a). Forward models help to overcome delays in the execution of the motor plan by predicting the outcome, so that the intended motor plans and commands can be corrected on the fly (Kawato, 1999; Wolpert and Ghahramani, 2000).

![Figure 3.](https://cdn.elifesciences.org/articles/89674/elife-89674-fig3-v1.jpg)

**Figure 3.:** (a) A voluntary movement trajectory can be specified by the target length of the muscles in time, $𝒖_{𝒐}^{*}$, encoded through the $\gamma$-innervation of muscle spindles, and the deviation of the effective muscle lengths from the target, $𝒖_{𝒐}−𝒖_{𝒐}^{*}=−𝒆‾_{𝒐}^{*}$. The $I_{a}$-afferents emerging from the spindles prospectively encode the error, so that their low-pass filtering is roughly proportional to the length deviation, truncated at zero (red). The moving equilibrium hypothesis states that the low-pass filtered input $𝒓‾_{in}$, composed of the movement plan $𝒓‾_{in}^{plan}$ and the sensory input (here encoding the state of the plant e.g., through visual and proprioceptive input, $𝒓‾_{in}^{vis}$ and $𝒓‾_{in}^{prop}$), together with the low-pass filtered error feedback from the spindles, $𝒆‾_{𝒐}^{*}$, instantaneously generate the muscle lengths, $𝒖_{𝒐}=𝑭_{W}(𝒓‾_{in},𝒆‾_{𝒐}^{*})$, and are thus at any point in time in an instantaneous equilibrium (defined by Equation 7a, Equation 7b). (b1) Intracortical intracortical electroencephalogram (iEEG) activity recorded from 56 deep electrodes and projected to the brain surface. Red nodes symbolize the 56 iEEG recording sites modeled alternately as input or output neurons, and blue nodes symbolize the 40 ‘hidden’ neurons for which no data is available, but used to reproduce the iEEG activity. (b2) Corresponding NLA network. During training, the voltages of the output neurons were nudged by the iEEG targets (black input arrows, but for all red output neurons). During testing, nudging was removed for 14 out of these 56 neurons (here, represented by neurons 1, 2, 3). (c1) Voltage traces for the 3 example neurons in a2, before (blue) and after (red) training, overlaid with their iEEG target traces (gray). (c2) Total cost, integrated over a window of 8 s of the 56 output nodes during training with sequences of the same duration. The cost for the test sequences was evaluated on a 8 s window not used during training.

The observation that muscle spindles prospectively encode the muscle length and velocity (Dimitriou and Edin, 2010) suggests that the prospective coding in the internal forward model mirrors the prospective coding in the effective forward pathway. This forward pathway leads from the motor plan to the spindle feedback, integrating also cerebellar and brainstem feedback (Kawato, 1999). Based on the motor plans, the intended spindle lengths and the effective muscle innervation are communicated via a descending pathway to activate the $\gamma$- and $\alpha$-motoneurons, respectively (Li et al., 2015). The mapping from the intended arm trajectory to the intended spindle lengths via $\gamma$-innervation is mainly determined by the joint geometry. The mapping from the intended arm trajectory to the force-generating $\alpha$-innervation, however, needs to also take account of the internal and external forces, and this is engaging our network $𝑾$.

When we prepare an arm movement, spindles in antagonistic muscle pairs that measure the muscle length are tightened or relaxed before the movement starts (Papaioannou and Dimitriou, 2021). According to the classical equilibrium-point hypothesis (Feldman and Levin, 2009; Latash, 2010), top-down input adjusts the activation threshold of the spindles through ($\gamma$-) innervation from the spinal cord so that slight deviations from the equilibrium position can be signaled (Figure 3a). We postulate that this $\gamma$-innervation acts also during the movement, setting an instantaneous target $𝒖_{𝒐}^{*}(t)$ for the spindle lengths. The effective lengths of the muscle spindles is $𝒖_{𝒐}$, and the spindles are prospectively signaling back the deviation from the target through the $I_{a}$-afferents (Dimitriou and Edin, 2010; Dimitriou, 2022). The low-pass filtered $I_{a}$-afferents may be approximated by a threshold-nonlinearity, $I_{a}=\beta⌊𝒖_{𝒐}−𝒖_{𝒐}^{*}⌋^{+}$, with $\beta$ being interpreted as spindle gain (Latash, 2018). Combining the feedback from agonistic and antagonistic muscle pairs allows for extracting the scaled target error $\beta𝒆‾_{𝒐}^{*}=\beta(𝒖_{𝒐}^{*}−𝒖_{𝒐})$. Taking account of the prospective feedback, we postulate the moving equilibrium hypothesis according to which the instructional inputs, $𝒓‾_{in}$, the spindle feedback, $\beta𝒆‾_{𝒐}^{*}$, and the muscle lengths, $𝒖_{𝒐}$, are at any point of the movement in a dynamic equilibrium. The moving equilibrium hypothesis extends the classical equilibrium-point hypothesis from the spatial to the temporal domain (for a formal definition of a moving equilibrium see Methods, Sect. From implicit to explicit differential equations).

Prediction errors are also reduced when motor units within a muscle are recruited according to the size principle (Senn et al., 1997), which itself was interpreted in terms of the physical least-action principle (Senn et al., 1995). With regard to the interpretation of the prospective feedback error $𝒆_{𝒐}^{*}$ as spindle activity, it is worth noticing that in humans the spindle activity is not only ahead of the muscle activation (Dimitriou and Edin, 2010), but also share the property of a motor error (Dimitriou, 2016). The experiments show that during the learning of a gated hand movement, spindle activity is initially stronger when making movement errors, and it returns back to baseline with the success of learning. This observation is consistent with the NLA principle, saying that the proprioceptive prediction errors are minimized through the movement learning. We next address how the synaptic strengths $𝑾$ involved in producing the muscle length can be optimally adapted to capture this learning.

### Local plasticity at basal synapses minimizes the global cost in real time

The general learning paradigm starts with input time series $r_{in(t),i}$ and target time series $u_{o}^{*}(t)$, while assuming that the target series are an instantaneous function of the low-pass filtered input series, $𝒖_{𝒐}^{*}(t)=𝑭^{*}(𝒓_{in}(t))$. The low-pass filtering in the individual inputs could be with respect to any time constant $\tau_{in,i}^{*}$ (that may also be learned, see Appendix 2). Yet, for simplicity, we assume the same time constant $\tau$ for low-pass filtering the rates of the network neurons and input neurons. The goal of learning is to adapt the synaptic strengths $𝑾$ in the student network so that this moves towards the target mapping, $𝑭_{W}→𝑭^{*}$. The local synaptic plasticity will also reduce the global cost $C$ defined on the output neurons $o$ in terms of the deviation of the voltage from the target, $u_{o}^{*}−u_{o}$ (Equation 2).

The problem of changing synaptic weights to correct the behavior of downstream neurons, potentially multiple synapses away, is typically referred to as the credit assignment problem and is notoriously challenging in physical or biological substrates operating in continuous time. A core aspect of the NLA principle is how it relates the global cost $C$ to the Lagrangian $L$ and eventually to somato-dendritic prediction errors $𝒆‾$ that can be reduced through local synaptic plasticity $𝑾˙$. We define this synaptic plasticity as a partial derivative of the Lagrangian with respect to the weights, $𝑾˙∝−\frac{∂L}{∂𝑾}=𝒆‾𝒓‾^{T}$. Since the somatodendritic mismatch error is $𝒆‾=𝒖−𝑾𝒓‾$, this leads to the local learning rule of the form ‘postsynaptic error times low-pass filtered presynaptic rate’,

$$
W˙=η(u−Wr¯)r¯^{T}.
$$

The plasticity rule runs simultaneously to the neuronal dynamics in the presence of a given nudging strength $\beta$ that tells how strongly the voltage of an output neuron is pushed towards the target, $u_{o}→u_{o}^{*}$. The learning rule is local in space since $𝑾𝒓‾$ is represented as a voltage of the basal dendrites, and the somatic voltage $𝒖$ may be read out at the synaptic site on the basal dendrite from the backpropagating action potentials that sample $𝒖$ at a given time (Urbanczik and Senn, 2014). The basal voltage $𝑾𝒓‾$ becomes the dendritic prediction of the somatic activity $𝒖$, interpreting Equation 8 as ‘dendritic predictive plasticity’.

We have derived the neuronal dynamics as a path that keeps the action stationary. Without an external teaching signal, the errors vanish, and the voltage trajectory wriggles on the bottom of the energy landscape ($L=0$, Figure 1b2). If the external nudging is turned on, $\beta>0$, errors emerge and hills grow out of the landscape. The trajectory still tries to locally minimize the action, but it is lifted upwards on the hills ($L>0$, Figure 1b2). Synaptic plasticity reshapes the landscape so that, while keeping $\beta$ fixed, the errors are reduced and the landscape again flattens. The transformed trajectory settles anew in another place (inside the ‘volcano’ in 1b2). Formally, the local plasticity rule (Equation 8) is shown to perform gradient descent on the Lagrangian and hence on the action. In the energy landscape picture, plasticity ‘shovels off’ energy along the voltage path so that this is lowered most efficiently. The error that is back-propagated through the network tells at any point on the voltage trajectory how much to ‘dig’ in each direction, i.e., how to adapt the basal input in each neuron in order to optimally lower the local error.

The following theorem tells that synaptic plasticity $𝑾˙$ pushes the network mapping $𝒖_{𝒐}=𝑭_{W}(𝒓‾_{in})$ towards the target mapping $𝒖_{𝒐}^{*}=𝑭^{*}(𝒓‾_{in})$ at any moment in time. The convergence of the mapping is a consequence of the fact the plasticity reduces the Lagrangian $L=E^{M}+\betaC$ along its gradient.

### Theorem 1 (real-time dendritic error propagation, rt-DeEP)

Consider an arbitrary network $𝑾$ with voltage and error dynamics following Equation 7a, Equation 7b. Then the local plasticity rule $𝑾˙∝𝒆‾𝒓‾^{T}$ Equation 8, acting at each moment along the voltage trajectories, is gradient descent

The gradient statements hold at any point in time (long enough after initialization), even if the input trajectories $𝒓_{in}(t)$ contain delta functions and the target trajectories $𝒖_{𝒐}^{*}(t)$ contain step functions.

Loosely speaking, the NLA enables the network to localize in space and time an otherwise global problem: what is good for a single neuron (the local plasticity) becomes good for the entire network (the gradient on the global cost). Learning is possible at any point in time along the trajectory because the NLA inferred a prospective voltage dynamics expressed in prospective firing rates $r_{i}$ and prospective errors $e_{i}$ of the network neurons. In the limit of strong nudging ($\beta→∞$), the learning rule performs gradient descent on the mismatch energies $E^{M}_{i}$ in the individual neurons. If the network architecture is powerful enough so that after learning all the mismatch energies vanish, $E^{M}_{i}=0$, then the cost will also vanish, $C=\frac{1}{2}‖𝒖_{𝒐}^{*}−𝒖_{𝒐}‖^{2}=0$. This is because for the output neurons, the mismatch error includes the target error (Equation 7b). In the limit of weak nudging ($\beta→0$), the learning rule performs gradient descent on $C$, and with this also finds a local minimum of the mismatch energies.

In the case of weak nudging and a single steady-state equilibrium, the NLA algorithm reduces to the Equilibrium Propagation algorithm (Scellier and Bengio, 2017) that minimizes the cost $C$ for a constant input and a constant target. In the case of strong nudging and a single steady-state equilibrium, the NLA principle reduces to the Least-Control Principle (Meulemans et al., 2022) that minimizes the mismatch energy $E^{M}$ for a constant input and a constant target, with the apical prediction error becoming the prediction error from standard predictive coding (Rao and Ballard, 1999). While in the Least-Control Principle, the inputs and outputs are clamped to fixed values, the output errors are backpropagated and the network equilibrates in a steady state where the corrected network activities reproduce the clamped output activities. This state is called the ‘prospective configuration’ in Song et al., 2024 because neurons deep in the network are informed about the distal target already during the inference, and are correspondingly adapted to be consistent with this distal target. In the NLA principle, after an initial transient, the network always remains in the moving equilibrium due to the prospective coding. While inputs and targets dynamically change, the network moves along a continuous sequence of prospective configurations.

In the motor control example, the theorem tells that a given target motor trajectory $𝒖_{𝒐}^{*}(t)$ is learned to be reproduced with the forward model $𝒖_{𝒐}(t)=𝑭_{W}(𝒓‾_{in}(t))$, by applying the dendritic predictive plasticity for the network neurons (Equation 8). We next exemplify the theory by looking into the brain, reproducing cortical activity, and showing how a multi-layer cortical network can learn a sensory-motor mapping while staying in a moving equilibrium throughout the training.

### Reproducing intracortical EEG recordings and recognizing handwritten digits

As an illustration, we consider a recurrently connected network that learns to represent intracortical electroencephalogram (iEEG) data from epileptic patients (Figure 3b). For each electrode, we assign a neuron within this network to represent the activity of the cell cluster recorded in the corresponding iEEG signal via its membrane potential. During learning, a randomly selected subset of electrode neurons are nudged towards the target activity from recorded data while learning to be reproduced by the other neurons. After learning, we can present only a subset of electrode neurons with previously unseen recordings and observe how the activity of the other neurons closely matches the recordings of their respective electrodes (Figure 3c). The network derived from NLA is thus able to learn complex correlations between signals evolving in real-time by embedding them in a recurrent connectivity structure.

As an example of sensory-motor processing in the NLA framework, we next consider a well-studied image recognition task, here reformulated in a challenging time-continuous setting, and interpreted as a motor task where 1 out of 10 fingers has to be bent upon seeing a corresponding visual stimulus (see Figure 3). In the context of our moving equilibrium hypothesis, we postulate that during the learning phase, but not the testing phase, an auditory signal identifies the correct finger and sets the target spindle lengths of 10 finger flexors, $𝒖_{𝒐}^{*}(t)$. The target spindle length encodes the desired contraction of a flexor muscle in the correct finger upon the visual input $𝒓_{in}(t)$, and a corresponding relaxation for the nine incorrect fingers.

We train a hierarchical three-layer network on images of handwritten digits (MNIST, LeCun, 1998), with image presentation times between $0.5\tau$ (=5 ms) and $20\tau$ (=200 ms, with $\tau=10$ the membrane time constant). Figure 4a-c depict the most challenging scenario with the shortest presentation time. Synaptic plasticity is continuously active, despite the network never reaching a temporal steady state (Figure 4b1). Due to the lookahead firing rates in the NLA, the mismatch errors $e‾_{i}(t)$ represent the correct gradient and propagate without lag throughout the network. As a consequence, our mismatch errors are almost equal to the errors obtained from classical error backpropagation applied at each time step to the purely forward network (i.e. the network that suppresses the error-correction $𝒆‾$ of the voltage and instead considers the ‘classical’ voltage $𝒖_{l}=𝑾_{l}ρ(𝒖_{l−1})$ only, see blue dots in Figure 4b2). The network eventually learned to implement the mapping $𝒖_{𝒐}=𝑭_{W}(𝒓‾_{in})≈𝒖_{𝒐}^{*}$ with a performance comparable to error-backpropagation at each $dt$, despite the short presentation time of only 5 ms (Figure 4c1). The approximation is due to the fact that the NLA learns an instantaneous mapping from the low-pass filtered input rates $𝒓‾_{in}$ to the output voltage $𝒖_{𝒐}$, while the mapping from the original input rates $𝒓_{in}$ to the voltages $𝒖_{1}$ of the first-layer neurons (and hence also to the output voltages $𝒖_{𝒐}$) is delayed by $\tau_{in}$. Since in the simulations, the target voltages $𝒖_{𝒐}^{*}$ were switched instantaneously with $𝒓_{in}$ (and not with $𝒓‾_{in}$), however, a mismatch error between $𝒖_{𝒐}$ and $𝒖_{𝒐}^{*}$ remains for stimulus presentation times shorter than $\tau_{in}$ (Figure 4c2). The Latent Equilibrium (Haider et al., 2021) avoids these temporal limitations by implementing an instantaneous mapping on the rates instead on the voltages (Methods, Sect. From implicit to explicit differential equations).

![Figure 4.](https://cdn.elifesciences.org/articles/89674/elife-89674-fig4-v1.jpg)

**Figure 4.:** (a) Functionally feedforward network with handwritten digits as visual input ($𝒓_{in}^{(2)}(t)$ in Figure 3a, here from the MNIST data set, 5 ms presentation time per image), backprojections enabling credit assignment, and activity of the 10 output neurons interpreted as commands for the 10 fingers (forward architecture: 784×500×10 neurons). (b) Example voltage trace (b1) and local error (b2) of a hidden neuron in neuronal least-action (NLA) (red) compared to an equivalent network without lookahead rates (orange). Note that neither network achieves a steady state due to the extremely short input presentation times. Errors are calculated via exact backpropagation, i.e., by using the error backpropagation algorithm on a pure feedforward NLA network at every simulation time step (with output errors scaled by $\beta$), shown for comparison (blue dots). (c) Comparison of network models during and after learning. Color scheme as in (b). (c1) The test error under NLA evolves during learning on par with classical error backpropagation performed each Euler $dt$ based on the feedforward activities. In contrast, networks without lookahead rates are incapable of learning such rapidly changing stimuli. (c2) With increasing presentation time, the performance under NLA further improves, while networks without lookahead rates stagnate at high error rates. This is caused by transient, but long-lasting misrepresentation of errors following stimulus switches: when plasticity is turned off during transients and is only active in the steady state, comparably good performance can be achieved (dashed orange). (d) Receptive fields of 6 hidden-layer neurons after training, demonstrating that even for very brief image presentation times (5ms), the combined neuronal and synaptic dynamics are capable of learning useful feature extractors such as edge filters.

The instantaneous voltage propagation relieves an essential constraint of previous models of bio-plausible error backpropagation (e.g. Scellier and Bengio, 2017; Whittington and Bogacz, 2017; Sacramento et al., 2018), with reviews (Richards et al., 2019; Whittington and Bogacz, 2019; Lillicrap et al., 2020): without lookahead firing rates, networks need much longer to correctly propagate errors across layers, with each layer roughly adding another membrane time constant of 10 ms, and thus cannot cope with realistic input presentation times. In fact, in networks without lookahead output, learning is only successful if plasticity is switched off while the network dynamics did not reach a stationary state during a stimulus presentation interval (Figure 4c2). Notice also that the prospective coding is necessary to keep the network activity stable for an instantaneous processing of the sensory input. If, in the absence of prospective coding, we would only shrink the membrane time constant to 0, the recurrent error processing would become unstable (see Appendix 3).

### Implementation in cortical microcircuits

So far, we did not specify how errors $𝒆$ appearing in the differential equation for the voltage (Equation 7a) are transmitted across the network in a biologically plausible manner. Building on Sacramento et al., 2018, we propose a cortical microcircuit to enable this error transport, with all neuron dynamics evolving according to the NLA principle. Although the idea applies to arbitrarily connected networks, we use the simpler case of functionally feedforward networks to illustrate the flow of information in these microcircuits (Figure 5a).

![Figure 5.](https://cdn.elifesciences.org/articles/89674/elife-89674-fig5-v1.jpg)

**Figure 5.:** (a) Microcircuit with ‘top-down’ input (originating from peripheral motor activity, blue line) that is explained away by the lateral input via interneurons (dark red), with the remaining activity representing the error $e‾_{l}$. Plastic connections are denoted with a small red arrow and nudging with a dashed line. (b1) Simulated network with 784-300-10 pyramidal-neurons and a population of 40 interneurons in the hidden layer used for the MNIST learning task where the handwritten digits have to be associated with the 10 fingers. (b2) Test errors for rt-DeEL with joint tabula rasa learning of the forward and lateral weights of the microcircuit. A similar performance is reached as with classical error backpropagation. For comparability, we also show the performance of a shallow network (dashed line). (b3) Angle derived from the Frobenius norm between the lateral pathway $𝑾^{IP}_{l}𝑾^{PI}_{l}$ and the feedback pathway $𝑩_{l}𝑾_{l+1}$. During training, both pathways align to allow correct credit assignment throughout the network. Indices are dropped in the axis label for readability.

For such an architecture, pyramidal neurons in area $l$ (that is a ‘layer’ of the feedforward network) are accompanied by a pool of interneurons in the same layer (area). The dendrites of the interneurons integrate in time (with time constant $\tau$) lateral input from pyramidal neurons of the same layer ($𝒓_{l}$) through plastic weights $𝑾^{IP}_{l}$. Additionally, interneurons receive ‘top-down nudging’ from pyramidal neurons in the next layer through randomly initialized and fixed back projecting synapses $𝑩^{IP}_{l}$ targeting the somatic region, and interneuron nudging strength $\beta^{I}$. The notion of ‘top-down’ originates from the functionally feed-forward architecture leading from sensory to ‘higher cortical areas.’ In the context of motor control, the highest ‘area’ is the last stage controlling the muscle lengths, being at the same time the first stage for the proprioceptive input (Figure 3a).

According to the biophysics of the interneuron, the somatic membrane potential becomes a convex combination of the two types of afferent input (Urbanczik and Senn, 2014),

$$
u_{l}^{I}=(1−\beta^{I})W_{l}^{IP}r¯_{l}+\beta^{I}B_{l}^{IP}u_{l+1}.
$$

In the biological implementation, the feedback input is mediated by the low-pass filtered firing rates $𝒓‾_{l+1}=ρ(𝒖_{l+1})$, not by $𝒖_{l+1}$ as expressed in the above equation. Yet, we argue that for a threshold-linear $ρ$ the ‘top-down nudging’ by the rate $𝒓‾_{l+1}$ is effectively reduced to a nudging by the voltage $𝒖_{l+1}$. This is because errors are only backpropagated when the slope of the transfer function is positive, $𝒓_{l+1}^{′}>0$, and hence when the upper-layer voltage is in the linear regime. For more general transfer functions, we argue that short-term synaptic depression may invert the low-pass filtered presynaptic rate back to the presynaptic membrane potential, $𝒓‾_{l+1}→𝒖_{l+1}$, provided that the recovery time constant $\tau$ matches the membrane time constant (see end of Results and Appendix 1).

Apical dendrites of pyramidal neurons in each layer receive top-down input from the pyramidal population in the upper layer through synaptic weights $𝑩_{l}$. These top-down weights could be learned to predict the lower-layer activity (Rao and Ballard, 1999) or to become the transposed of the forward weight matrix ($𝑩_{l}=𝑾_{l+1}^{T}$, Max et al., 2022), but for simplicity, we randomly initialized them and keep them fixed (Lillicrap et al., 2020). Besides the top-down projections, the apical dendrites also receive lateral input via an interneuron population in the same layer through synaptic weights $−𝑾^{PI}_{l}$ that are plastic and will be learned to obtain suitable dendritic errors. The ‘-’ sign is suggestive of these interneurons to subtract away the top-down input entering through $𝑩_{l}$ (while the weights can still be positive or negative). Assuming again a conversion of rates to voltages, also for the inhibitory neurons that may operate in a linear regime, the overall apical voltage becomes

$$
e¯_{l}^{A}=B_{l}u_{l+1}−W_{l}^{PI}u_{l}^{I}.
$$

What cannot be explained away from the top-down input $𝑩_{l}𝒖_{l+1}$ by the lateral feedback, $−𝑾^{PI}_{l}𝒖^{I}_{l}$, remains as dendritic prediction error $𝒆‾_{l}^{A}$ in the apical tree (Figure 5a). If the top-down and lateral feedback weights are learned as outlined next, these apical prediction errors take the role of the backpropagated errors in the classical backprop algorithm.

To adjust the interneuron circuit in each layer (‘area’), the synaptic strengths from pyramidal-to-interneurons, $𝑾^{IP}_{l}$, are learned to minimize the interneuron mismatch energy, $E_{l}^{IP}=\frac{1}{2}‖u_{l}^{I}−W_{l}^{IP}r¯_{l}‖^{2}$. The interneurons, while being driven by the lateral inputs $𝑾^{IP}_{l}𝒓‾_{l}$, learn to reproduce the upper-layer activity that also nudges the interneuron voltage. Learning is accomplished if the upper-layer activity, in the absence of an additional error on the upper layer, is fully reproduced in the interneurons by the lateral input.

Once the interneurons learn to represent the ‘error-free’ upper-layer activity, they can be used to explain away the top-down activities that also project to the apical trees. The synaptic strengths from the inter-to-pyramidal neurons, $𝑾^{PI}_{l}$, are learned to minimize the apical mismatch energy, $E_{l}^{PI}=\frac{1}{2}‖e¯_{l}^{A}‖^{2}=\frac{1}{2}‖B_{l}u_{l+1}−W_{l}^{PI}u_{l}^{I}‖^{2}$. While in the absence of an upper-layer error, the top-down activity $𝑩_{l}𝒖_{l+1}$ can be fully cancelled by the interneuron activity $𝑾^{PI}_{l}𝒖^{I}_{l}$, a neuron-specific error will remain in the apical dendrites of the lower-level pyramidal neurons if there is an error endowed in the upper-layer neurons. Gradient descent learning on these two energies results in the learning rules for the P-to-I and I-to-P synapses,

$$
W˙_{l}^{IP}=η^{IP}(u_{l}^{I}−W_{l}^{IP}r¯_{l})r¯_{l}^{T}andW˙_{l}^{PI}=η^{PI}(B_{l}u_{l+1}−W_{l}^{PI}u_{l}^{I})u_{l}^{I^{T}}.
$$

The following theorem on dendritic error learning tells that the plasticity in the lateral feedback loop leads to an appropriate error representation in the apical dendrites of pyramidal neurons.

### Theorem 2 (real-time dendritic error learning, rt-DeEL)

Consider a cortical microcircuit composed of pyramidal and interneurons, as illustrated in Figure 5a, with more interneurons in layer (‘cortical area’) $l$ than pyramidal neurons in layer $l+1$, and with adaptable pyramidal-to-inhibitory weights $𝑾^{IP}_{l}$ within the same layer that are nudged through top-down weights $𝑩^{IP}_{l}$, see Methods, Sect. Proving theorem 2 (rt-DeEL). Then, for suitable top-down nudging, learning rates, and initial conditions, the inhibitory-to-pyramidal synapses $𝑾^{PI}_{l}$ within each layer $l$ (Equation 11) evolve such that the lateral feedback circuit aligns with the bottom-up-top-down feedback circuit,

$$
W_{l}^{PI}W_{l}^{IP}=B_{l}W_{l+1}.
$$

After this horizontal-to-vertical circuit alignment, the apical voltages $𝒆‾_{l}^{A}=𝑩_{l}𝒖_{l+1}−𝑾^{PI}_{l}𝒖^{I}_{l}$ of the layer-$l$ pyramidal neurons (Equation 13) represent the ‘$B$-backpropagated’ errors, $𝒆‾_{l}^{A}=𝑩_{l}𝒆‾_{l+1}$. When modulated by the postsynaptic rate derivatives, $𝒓‾_{l}^{′}=𝝆^{′}(𝒖‾_{l})$, the apical voltages yield the appropriate error signals

$$
e¯_{l}=u_{l}−W_{l}r¯_{l−1}=r¯_{l}^{′}⋅e¯_{l}^{A}=r¯_{l}^{′}⋅B_{l}e¯_{l+1}
$$

for learning the forward weights $𝑾_{l}$ according to $𝑾˙_{l}∝𝒆‾_{l}𝒓‾_{l−1}^{T}$ Equation 8.

The back projecting weights can also be learned by a local real-time learning rule to become transpose of the forward weights, $𝑩_{l}=𝑾_{l+1}^{T}$ (Max et al., 2022). In this case, the error signals $𝒆‾_{l}$ learned in the apical dendrites according to the above Theorem (Equation 13) represent the gradient errors $𝒆‾$ appearing in the real-time dendritic error propagation (rt-DeEP, Theorem 1). There, the errors $𝒆‾$ drive the gradient plasticity of the general weight matrix $𝑾$, split up here into the forward weights $𝑾_{l}$ to a layer $l$ (for $l=1,..,N$).

### Simultaneously learning apical errors and basal signals

Microcircuits following these neuronal and synaptic dynamics are able to learn the classification of hand-written digits from the MNIST dataset while learning the apical signal representation (Figure 5b1, b2). In this case, feedforward weights $𝑾_{l}$ and lateral weights $W_{l}^{PI}$ and $W_{l}^{IP}$ are all adapted simultaneously. Including the $W_{l}^{IP}˙$-plasticity (by turning on the interneuron nudging from the upper layer, $\beta^{I}>0$ in Equation 9), greatly speeds up the learning.

With and without $W_{l}^{IP}˙$-plasticity, the lateral feedback via interneurons (with effective weight $W_{l}^{IP}W_{l}^{PI}$) learns to align with the forward-backward feedback via upper layer pyramidal neurons (with effective weight $𝑩_{l}𝑾_{l+1}$, Figure 5b3). The microcircuit extracts the gradient-based errors (Equation 13), while the forward weights use these errors to reduce these errors to first minimize the neuron-specific mismatch errors, and eventually the output cost.

Since the apical voltage $𝒆‾_{l}^{A}$ appears as a postsynaptic factor in the plasticity rule for the interneurons ($W_{l}^{PI}˙$), this I-to-P plasticity can be interpreted as Hebbian plasticity of inhbitory neurons, consistent with earlier suggestions (Vogels et al., 2011; Bannon et al., 2020). The plasticity $W_{l}^{IP}˙$ of the P-to-I synapses, in the same way as the plasticity for the forward synapses $𝑾˙_{l}$, can be interpreted as learning from the dendritic prediction of somatic activity (Urbanczik and Senn, 2014).

Crucially, by choosing a large enough interneuron population, the simultaneous learning of the lateral microcircuit and the forward network can be accomplished without fine-tuning of parameters. As an instance in case, all weights shared the same learning rate. Such stability bolsters the biophysical plausibility of our NLA framework and improves over the previous, more heuristic approach (Sacramento et al., 2018; Mesnard et al., 2019). The stability may be related to the nested gradient descent learning according to which somatic and apical mismatch errors in pyramidal neurons, and somatic mismatch errors in inhibitory neurons are minimized.

Finally, since errors are defined at the level of membrane voltages (Equation 11), synapses need a mechanism by which they can recover the presynaptic voltage errors from their afferent firing rates. While for threshold-linear transfer functions the backpropagated voltage errors translate into rate errors (Appendix 1), more general neuronal nonlinearities must be matched by corresponding synaptic nonlinearities. Pfister et al., 2010 have illustrated how spiking neurons can leverage short-term synaptic depression to estimate the membrane potential of their presynaptic partners. Here, we assume a similar mechanism in the context of our rate-based neurons. The monotonically increasing neuronal activation function, $𝒓‾_{l+1}=ρ(𝒖_{l+1})$, can be approximately compensated by a vesicle release probability that monotonically decreases with the low-pass filtered presynaptic rate $𝒓‾_{l+1}$ (see Appendix 1 and Appendix 1—figure 1). If properly matched, this leads to a linear relationship between the presynaptic membrane potential $𝒖_{l+1}$ and the postsynaptic voltage contribution.

## Discussion

We introduced a least-action principle to neuroscience for deriving the basic laws of the voltage and synaptic dynamics in networks of cortical neurons. The approach is inspired by the corresponding principle in physics where basic laws of motion are derived across the various scales. While in physics the action is defined as the time-integral of the kinetic minus potential energy, we define the action as the time-integral of instantaneous somatodendritic mismatch errors across network neurons plus a behavioral error. The ‘kinetics’ of a voltage trajectory only arises because we postulate that the action along a trajectory is minimized with respect to future voltages, not the instantaneous voltage, as would be done in physics. The postulate implies a prospective voltage dynamics that look ahead in time, together with prospective local errors, in order to minimize the action and hence the somatodendritic mismatch errors. The prospective errors nudge the firing of pyramidal neurons deep in the brain, so that motor neurons improve the output of the network right in time. A putative behavioral error, encoded in the motor feedback, propagates back through the network and produces prospective corrections of the pyramidal neuron activities that effectively manifest in instantaneous corrections of the motor trajectory. Through this prospective coding, the sensory stream, the deep network activity, and the motor feedback are in sync at any moment in time. We formulated the dynamic synchronization as a ‘moving equilibrium hypothesis’, referring to the classical equilibrium point hypothesis for motor control (Feldman and Levin, 2009; Latash, 2010). More generally, the brain activity formed by the prospective firing of cortical pyramidal neurons is in a moving equilibrium while converting sensory input streams into motor outputs, consistent with prospective sensory processing in the human cortex (Blom et al., 2020).

Because the neuronal dynamics derived from the global NLA principle is in a moving equilibrium, the prospective dendritic errors that globally correct the output trajectory are also suited to instruct local synapatic plasticity in the dendrites. In fact, working down the apical errors by adapting the sensory-driven synapses on the basal dendrites reduces the global output errors in real time. The apical errors are extracted from the top-down feedback via lateral ‘inhibition’ that tries to cancel the top-down signal. This top-down feedback includes activity from a putative erroneous motor output that was not foreseen by the local inhibition and thus survives as a local apical error. Given the prospective coding of the pyramidal neurons, the dendritic errors are also prospective and thus able to induce the correct error-minimizing plasticity online, while stimuli and targets continuously change.

### The NLA principle as a bottom-up theory from neurons to behavior

To show that the NLA principle offers a viable program for a formalization of neuroscience following the example of physics, we exemplified its ramifications in dendritic computation, cortical microcircuits, synaptic plasticity, motor control, and sensory-based decision-making. The crucial point of our axiomatization is that it connects the local neuronal errors to the global behavioral errors right in the formulation of the principle, eventually leading to local gradient-based plasticity rules. Because the formulation builds upon computations that can be realized in single neurons and dendrites to produce a behavioral output, the NLA principle can be seen as a bottom-up theory of behavior. It is articulated in terms of apical and basal dendrites, somatic firing, network connectivity and behavioral outputs that jointly minimize their errors. This contrasts the related free energy principle, for instance, that leads to a top-down theory of behavior by starting with the statistical, but the more universal, notion of a free energy. It postulates that any self-organizing system, that is at a statistical equilibrium with its environment, must minimize its free energy (Friston, 2010; Friston et al., 2022), and from there work down its way to neurons and dendrites (Bastos et al., 2012; Kiebel and Friston, 2011).

Starting with a single Lagrangian function that specifies the form of the somatodendritic prediction errors leaves some freedom for the interpretation and the implementation of the emerging dynamical equations for the voltages. We interpret errors to be represented in the apical dendrites of pyramidal neurons while sensory input targets the basal dendrites, but other dendritic configurations are conceivable (Mikulasch et al., 2023) that apply also to non-pyramidal neurons. We have chosen a specific interneuron circuitry to extract our apical errors, but other microcircuits or error representations might also be considered (Keller and Mrsic-Flogel, 2018). On the other hand, the derived gradient-based synaptic plasticity is tightly linked to the specific form of the somatodendritic prediction errors expressed in the Lagrangian and its interpretation, making specific predictions for synaptic plasticity (as outlined below). The ‘external’ feedback entering through the cost function offers additional freedom to model behavioral interactions. We considered an explicit time course of a target voltage in motor neurons, for instance imposed by the feedback from muscle spindles that are themselves innervated by a prospective top-down signal to control muscle lengths (Papaioannou and Dimitriou, 2021; Dimitriou, 2022). But the cost may also link to reinforcement learning and express a delayed reward feedback delivered upon a behavioral decision of an agent acting in a changing environment (Friedrich et al., 2011; Friedrich and Senn, 2012).

A fundamental difficulty arises when the neuronal implementation of the Euler-Lagrange equations requires an additional microcircuit with its own dynamics. This is the case for the suggested microcircuit extracting the local errors. Formally, the representation of the apical feedback errors first needs to be learned before the errors can teach the feedforward synapses on the basal dendrites. We showed that this error learning can itself be formulated as minimizing an apical mismatch energy. What the lateral feedback through interneurons cannot explain away from the top-down feedback remains an apical prediction error. Ideally, while the network synapses targetting the basal tree are performing gradient descent on the global cost, the microcircuit synapses involved in the lateral feedback are performing gradient descent on local error functions, both at any moment in time. The simulations show that this intertwined system can in fact learn simultaneously with a common learning rate that is properly tuned. The cortical model network of inter- and pyramidal neurons learned to classify handwritten digits on the fly, with 10-digit samples presented per second. Yet, the overall learning is more robust if the error learning in the apical dendrites operates in phases without output teaching but with corresponding sensory activity, as may arise during sleep (see e.g., Deperrois et al., 2022; Deperrois et al., 2024).

### The NLA principle integrates classical theories for cortical processing and learning

The prospective variational principle introduced with the NLA allows for integrating previous ideas on formalizing the processing and learning in cortical networks. Four such classical lines of theories come together. ($i$) The first line refers to the use of an energy function to jointly infer the neuronal dynamics and synaptic plasticity, originally formulated for discrete-time networks (Hopfield, 1982; Ackley et al., 1985), and recently extended to continuous-time networks (Scellier and Bengio, 2017). ($ii$) The second line refers to understanding error-backpropagation in the brain (Rumelhart et al., 1986; Xie and Seung, 2003; Whittington and Bogacz, 2017; Whittington and Bogacz, 2019; Lillicrap et al., 2020). ($iii$) The third line refers to dendritic computation and the use of dendritic compartmentalization for various functions such as nonlinear processing (Schiess et al., 2016; Poirazi and Papoutsi, 2020) and deep learning (Guerguiev et al., 2017; Sacramento et al., 2018; Haider et al., 2021). ($iv$) The fourth line refers to predictive coding (Rao and Ballard, 1999) and active inference (Pezzulo et al., 2022) to improve the sensory representation and motor output, respectively.

### The NLA integrates and predicts features of synapses, dendrites, and circuits

Motivated by the predictive power of the least-action principle in physics, we ask about experimental confirmation and predictions of the NLA principle. Given its axiomatic approach, it appears astonishing to find various preliminary matches at the dendritic, somatic, interneuron, synaptic, and even behavioral levels. Some of these are:

More experimental and theoretical work is required to substantiate these links and test specific predictions, such as the apical error representation in cortical pyramidal neurons.

Overall, our approach adapts the least-action principle from physics to be applied to neuroscience, and couples it with a normative perspective on the prospective processing of neurons and synapses in global cortical networks and local microcircuits. Given its physical underpinnings, the approach may inspire the rebuilding of computational principles of cortical neurons and circuits in neuromorphic hardware (Bartolozzi et al., 2022). A step in this direction, building on the instantaneous computational capabilities by slowly integrating neurons, has made done by Haider et al., 2021. Given its aspiration for a theoretical framework in neurobiology, a next challenge would be to generalize the NLA principle to spiking neurons (Gerstner and Kistler, 2002; Brendel et al., 2020) with their potential for hardware implementation (Zenke and Ganguli, 2018; Göltz et al., 2021; Cramer et al., 2022), to include attentional mechanisms in terms of dendritic gain modulation (Larkum et al., 2004) with a putative link to self-attention in artificial intelligence (Vaswani et al., 2017), to add second-order errors to cope with certainties (Granier et al., 2023), and to incorporate longer temporal processing as, for instance, offered by neuronal adaptation processes (La Camera et al., 2006) or realistically modelled dendrites (Chavlis and Poirazi, 2021).

## Methods

### Euler-Lagrange equations as inverse low-pass filters

The theory is based on the look-ahead of neuronal quantities. In general, the look-ahead of a trajectory $x(t)$ is defined via lookahead operator applied to $x$,

$$
(1+\tau\frac{d}{dt})x=x+\taux˙.
$$

The lookahead operator is the inverse of the low-pass filter operator denoted by a bar,

$$
x‾(t)=\frac{1}{\tau}\int_{−∞}^{t}x(t^{′})e^{−\frac{t−t^{′}}{\tau}}dt^{′}.
$$

This low-pass filtering can also be characterized by the differential equation $\taux‾˙(t)=−x‾(t)+x(t)$, see Appendix 2. Hence, applying the low-pass filtering to $x$ and then the lookahead operator $(1+\tau\frac{d}{dt})$ to $x‾(t)$, and using the Leibnitz rule for differentiating an integral, we calculate $(1+\tau\frac{d}{dt})x‾(t)=x(t)$. In turn, applying first the lookahead, and then the low-pass filtering, also yields the original trace back, $(1+\tau\frac{d}{dt})x=x‾+\taux‾˙=x$.

We consider an arbitrary network architecture with network neurons that are recurrently connected and that receive external input through an overall weight matrix $𝑾=(𝑾_{in},𝑾_{net})$, aggregated column-wise. The instantaneous presnyaptic firing rates are $𝒓=(𝒓_{in},𝒓_{net})^{T}$, interpreted as a single-column vector. A subset of network neurons are output neurons, $O⊆N$, for which target voltages $𝒖^{*}$ may be imposed. Rates and voltages may change in time $t$. Network neurons are assigned a voltage $𝒖$, generating the low-pass filtered rate $𝒓‾_{net}=ρ(𝒖)$, and a low-pass filtered error $𝒆‾=𝒖−𝑾𝒓‾$. We further define output errors $e‾_{o}^{*}=u_{o}^{*}−u_{o}$ for $o\inO$, and $e‾_{i}^{*}=0$ for non-output neurons $i\inN∖O$. With this, the Lagrangian from Equation 3 takes the form

$$
L=\frac{1}{2}‖e¯‖^{2}+\frac{\beta}{2}‖e¯^{∗}‖^{2}.
$$

We next use that $𝒖=𝒖~−\tau𝒖~˙$, with the $.~$ operator defined in Equation 4, to write out the Lagrangian $L$ in the canonical coordinates $(𝒖~,𝒖~˙)$ as (see also Equation 3)

$$
L=\frac{1}{2}\sumi\inN[u~_{i}−\tauu~˙_{i}−\sum_{j}W_{ij}ρ(u~_{j}−\tauu~˙_{j})]^{2}+\frac{\beta}{2}\sumo\inO[u_{o}^{*}−(u~_{o}−\tauu~˙_{o})]^{2}.
$$

The neuronal dynamics is derived from requiring a stationary action (see Equation 5), which is generally solved by the Euler-Lagrange equations $\frac{∂L}{∂u~_{i}}−\frac{d}{dt}\frac{∂L}{∂u~˙_{i}}=0$ (see Equation 6). Because $u~$ only arises in $L$ in the compound $u~−\tauu~˙$, the derivative of $L$ with respect to $u~$ is identical to the derivative with respect to $\tauu~˙$,

$$
\frac{∂L}{∂u~˙_{i}}=−\tau\frac{∂L}{∂u~_{i}}.
$$

Using the lookahead operator Equation 14, the Euler-Lagrange equations can then be rewritten as

$$
\frac{∂L}{∂u~_{i}}+\tau\frac{d}{dt}\frac{∂L}{∂u~_{i}}=(1+\tau\frac{d}{dt})\frac{∂L}{∂u~_{i}}=0.
$$

Since $L(𝒖~,𝒖~˙)=L(𝒖)$ and $𝒖=𝒖~−\tau𝒖~˙$, the derivative of $L$ with respect to $𝒖~$ is the same as the derivative of $L$ with respect to $𝒖$,

$$
\frac{∂L}{∂u~_{i}}=\frac{∂L}{∂u_{i}}.
$$

Plugging this into Equation 19, the Euler-Lagrange equations become a function of $𝒖$ and $𝒖˙$,

$$
(1+\tau\frac{d}{dt})\frac{∂L}{∂u_{i}}=0.
$$

Notice that, if we had directly calculated $\frac{∂L}{∂u~_{i}}−\frac{d}{dt}\frac{∂L}{∂u~˙_{i}}=0$, the second-order time derivative $u~¨_{i}$ of the discounted future voltage would be absorbed in a first-order time derivative of the voltage. The reason is that $u~˙_{i}−\tauu~¨_{i}=u˙_{i}$, and $u~¨_{i}$ only arises in this combination because the Lagrangian $L=L(𝒖)$ is only a function of $𝒖$ and not of $𝒖˙$. Hence, the acceleration term $u~¨_{i}$ disappears, while a voltage derivative $u˙_{i}$ appears.

The solution of this differential Equation 20 is $\frac{∂L}{∂u_{i}}=c_{i}e^{−\frac{t−t_{0}}{\tau}}$, and hence any trajectory $(u~_{i},u~˙_{i})$ which satisfy the Euler-Lagrange equations will hence cause $\frac{∂L}{∂u_{i}}$ to converge to zero with a characteristic time scale of $\tau$. Since we require that the initialisation is at $t_{0}=−∞$, we conclude that $\frac{∂L}{∂u_{i}}=0$, as required in the rt-DeEP Theorem. For a table with all the mathematical abbreviations see Methods-Table 1.

**Table 1.**
 Mathematical symbols.


<table>
  <thead>
    <tr>
      <th>Mathematical expression</th>
      <th>Naming</th>
      <th>Comment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ui</td>
      <td>Instantaneous (somatic) voltage</td>
      <td>only for network neurons</td>
    </tr>
    <tr>
      <td>ri=ρ⁢(ui)+τ⁢ρ˙⁢(ui)</td>
      <td>Instantaneous firing rate of neuron i</td>
      <td>that looks linearly ahead in time</td>
    </tr>
    <tr>
      <td>r¯⁢(t)=1τ⁢∫-∞tr⁢(t′)⁢e-t-t′τ⁢dt′</td>
      <td>Definition of low-pass filtering</td>
      <td>See Equation 15</td>
    </tr>
    <tr>
      <td>r¯i=ρ⁢(ui)=ri+τ⁢r˙i¯</td>
      <td>Low-pass filtered firing rate</td>
      <td>postulated to be a function of ui</td>
    </tr>
    <tr>
      <td>𝒓=𝒓¯+τ⁢𝒓¯˙</td>
      <td>Self-consistency eq.</td>
      <td>for low-pass filtered rate</td>
    </tr>
    <tr>
      <td>𝒓in</td>
      <td>Input rate vector, column</td>
      <td>projects to selected neurons</td>
    </tr>
    <tr>
      <td>𝒓¯in</td>
      <td>Low-pass filter input rates</td>
      <td>instantaneously propagates</td>
    </tr>
    <tr>
      <td>ei=(ui+τu˙i)−∑jWijrj</td>
      <td>Prospective error of neuroni</td>
      <td>in apical dendrite</td>
    </tr>
    <tr>
      <td>e¯i=ui−∑jWijr¯j</td>
      <td>Error of neuroni</td>
      <td>in soma</td>
    </tr>
    <tr>
      <td>EMi=12e¯i2=12(ui−∑jWijr¯j)2</td>
      <td>Mismatch energy in neuron i</td>
      <td>between soma and basal dendrite</td>
    </tr>
    <tr>
      <td>uo*</td>
      <td>Target voltage for output neuron o</td>
      <td>could impose target on ro or r¯o</td>
    </tr>
    <tr>
      <td>e¯o*=uo*-uo</td>
      <td>Error of output neuron o</td>
      <td>also called target error</td>
    </tr>
    <tr>
      <td>Co=12⁢(e¯o*)2</td>
      <td>Cost contribution of output neuron o</td>
      <td>between soma and basal dendrite</td>
    </tr>
    <tr>
      <td>L=∑i∈NEMi+β∑o∈OCo</td>
      <td>Lagrangian</td>
      <td>output ⁢O⊂network ⁢N</td>
    </tr>
    <tr>
      <td>u~⁢(t)=1τ⁢∫t∞u⁢(t′)⁢𝒆(t-t′)/τ⁢d⁢t′</td>
      <td>Discounted future voltage</td>
      <td>prospective coordinates for NLA</td>
    </tr>
    <tr>
      <td>𝒖=𝒖~-τ⁢𝒖~˙</td>
      <td>Self-consistency eq.</td>
      <td>for discounted future voltage</td>
    </tr>
    <tr>
      <td>A=∫t1t2L⁢[𝒖~⁢(t),𝒖~˙⁢(t)]⁢d⁢t</td>
      <td>Neuronal Least Action (NLA)</td>
      <td>expressed in prospect. coordinates</td>
    </tr>
    <tr>
      <td>∂⁡L∂⁡u~i-dd⁢t⁢∂⁡L∂⁡u~˙i=(1+dd⁢t)⁢∂∂⁡ui⁢L=0</td>
      <td>Euler-Lagrange equations</td>
      <td>turned into lookahead operator</td>
    </tr>
    <tr>
      <td>𝑾in</td>
      <td>weights from input neurons 𝒓in</td>
      <td>dim⁢(N)×dim⁢(𝒓in), most0</td>
    </tr>
    <tr>
      <td>𝑾net</td>
      <td>weights between network neurons</td>
      <td>dim⁢(N)×dim⁢(N)</td>
    </tr>
    <tr>
      <td>𝑾=(𝑾in,𝑾net)</td>
      <td>total weight matrix</td>
      <td>dim⁢(N)×(dim⁢(𝒓in)+dim⁢(N))</td>
    </tr>
    <tr>
      <td>𝒓=(𝒓in,𝒓net)T</td>
      <td>instantaneous firing rate vector</td>
      <td>column (indicated by transpose)</td>
    </tr>
    <tr>
      <td>𝑾˙∝𝒆¯⁢𝒓¯T</td>
      <td>Plasticity of 𝑾</td>
      <td>e¯ is a column, 𝒓¯T a row vector</td>
    </tr>
    <tr>
      <td>𝒖𝒐*⁢(t)=𝑭*⁢(𝒓¯in⁢(t))</td>
      <td>Target function formulated for r¯in(t)</td>
      <td>a functional of 𝒓in⁢(t)</td>
    </tr>
    <tr>
      <td>𝒖𝒐⁢(t)=𝑭W⁢(𝒓¯in⁢(t),𝒆¯𝒐*⁢(t))</td>
      <td>Func. implemented by forward network</td>
      <td>instant. func. of 𝒓¯in⁢(t) , not 𝒓in⁢(t)</td>
    </tr>
    <tr>
      <td>N</td>
      <td>Layers in forward network, w/o rin</td>
      <td>Last-layer voltages:𝒖N=𝒖𝒐</td>
    </tr>
    <tr>
      <td>WlIP</td>
      <td>Weights from pyr to interneurons</td>
      <td>lateral, within layer l</td>
    </tr>
    <tr>
      <td>WlPI</td>
      <td>Weights from inter- to pyr’neurons</td>
      <td>lateral, within layer l</td>
    </tr>
    <tr>
      <td>𝑾l</td>
      <td>Bottom-up weights from layerl–1 tol</td>
      <td>between pyramidal neurons</td>
    </tr>
    <tr>
      <td>𝑩l</td>
      <td>Top-down weights from layerl+1 tol</td>
      <td>between pyramidal neurons</td>
    </tr>
    <tr>
      <td>e¯lA=Blul+1−WPIluIl</td>
      <td>Low-pass filtered apical error in layerl</td>
      <td>top-down minus lateral feedback</td>
    </tr>
    <tr>
      <td>e¯l=r¯l′⋅e¯lA=r¯l′⋅Ble¯l+1</td>
      <td>Somato-basal prediction error</td>
      <td>is correct error for learning</td>
    </tr>
    <tr>
      <td>ElIP=12‖ulI−WlIPr¯l‖2</td>
      <td>Interneuron mismatch energy</td>
      <td>minimized to learn WlIP</td>
    </tr>
    <tr>
      <td>ElPI=12‖Blul+1−WPIluIl‖2</td>
      <td>Apical mismatch energy</td>
      <td>minimized to learn WlPI</td>
    </tr>
    <tr>
      <td>η,ηIP,ηPI</td>
      <td>Learning rates for plasticity of…</td>
      <td>…Wl;WlIP;WlPI</td>
    </tr>
    <tr>
      <td>𝑯=∂2⁡L∂⁡𝒖2=𝟏-𝑾net⁢𝝆′-𝒆¯′</td>
      <td>Hessian,∂2⁡L∂⁡𝒖2=∂⁡𝒇∂⁡𝒖. If pos. definite</td>
      <td>⇒ stable dynamics</td>
    </tr>
    <tr>
      <td>𝒇⁢(𝒖,t)=∂⁡L∂⁡𝒖=𝒖-𝑾⁢𝒓¯⁢(𝒖)-𝒆¯⁢(𝒖)</td>
      <td>Corrected error</td>
      <td>becomes 0 with τ</td>
    </tr>
    <tr>
      <td>𝒇⁢(𝒖,t)+τ⁢𝒇˙⁢(𝒖,t)=0</td>
      <td>Euler-Lagrange equations</td>
      <td>satisfy f(u,t)=f0e−(t−t0)/τ</td>
    </tr>
    <tr>
      <td>𝒇⁢(𝒖,t)=0</td>
      <td>Always the case after transient</td>
      <td>exponentially decaying with τ</td>
    </tr>
    <tr>
      <td>𝒖˙=-1τ⁢𝑯-1⁢(𝒖)⁢(𝒇⁢(𝒖)+τ⁢∂⁡𝒇∂⁡t)</td>
      <td>Explicit diff. eq.</td>
      <td>obtained by solving for 𝒖˙</td>
    </tr>
    <tr>
      <td>𝒈⁢(𝒖,t)=-1τ⁢𝑯-1⁢(𝒖)⁢(𝒇⁢(𝒖)+τ⁢∂⁡𝒇∂⁡t)</td>
      <td>Used to write the explicit diff. eq.</td>
      <td>𝒖˙=𝒈⁢(𝒖,t)</td>
    </tr>
    <tr>
      <td>𝑮⁢(𝒚,𝒖˙)=(1+τ⁢dd⁢t)⁢∂⁡L∂⁡𝒖=𝒇+τ⁢𝒇˙</td>
      <td>Used for contraction anaylsis, Equation 53</td>
      <td>𝒚=(𝒓in,𝒖𝒐*,𝒖)</td>
    </tr>
    <tr>
      <td>𝑴,𝑲</td>
      <td>Used to iteratively converge to𝒖˙</td>
      <td>see Equation 46</td>
    </tr>
    <tr>
      <td>𝒖˘=𝒖+τ⁢𝒖˙</td>
      <td>Linear lookahead voltage</td>
      <td>Latent Equilibrium, Appendix 4</td>
    </tr>
  </tbody>
</table>

### Deriving the network dynamics from the Euler-Lagrange equations

We now derive the equations of motion from the Euler-Lagrange equations. Noticing that $𝒖$ enters in $𝒆‾=𝒖−𝑾𝒓‾$ twice, directly and through $𝒓‾_{net}=ρ(𝒖)$, and once in the output error $𝒆‾^{*}$, we calculate from 16, using $𝒓‾(𝒖)=(𝒓‾_{in},ρ(𝒖))^{T}$ and $𝑾=(𝑾_{in},𝑾_{net})$,

$$
\frac{∂L}{∂u}=e¯−ϵ¯−\betae¯^{∗}, with ϵ¯=r¯_{net}^{′}⋅W_{net}^{T}e¯.
$$

Remember that for non-output neurons i no target exists, and for those we set $𝒆‾_{i}^{*}=0$. Next, we apply the lookahead operator to this expression, as required by the Euler-Lagrange Equation 19. In general $(1+\tau\frac{d}{dt})𝒙‾=𝒙‾+\tau𝒙‾˙=x$, and we set for $𝒙‾$ the expression on the right-hand side of Equation 21, $𝒙‾=𝒆‾−𝝐‾−\beta𝒆‾^{*}$, which at the same time is $𝒙‾=\frac{∂L}{∂𝒖}$. Hence, the Euler-Lagrange equations in the form of Equation 20, $(1+\tau\frac{d}{dt})x‾=0$, translate into

$$
(1+\tau\frac{d}{dt})\frac{∂L}{∂u}=0⟺e−ϵ−\betae^{∗}=0⟺\tauu˙=−u+Wr+e.
$$

To move from the middle to the last equality we replaced $𝒆$ with  $𝒆=(1+\tau\frac{d}{dt})𝒆‾=𝒖+\tau𝒖˙−𝑾𝒓$. In the last equality we interpret $𝒆$ as the sum of the two errors, $𝒆=𝝐+\beta𝒆^{*}$, again using the middle equality. This proves Equation 7a, Equation 7b.

Notice that the differential equation $\tau𝒖˙=...$ in Equation 22 represents an implicit ordinary differential equation as on the right-hand side not only $𝒖$, but also $𝒖˙$ appears (in $𝒓$ and $𝒆$). The uniqueness of the solution $𝒖(t)$ for a given initial condition is only guaranteed if it can be converted into an explicit ordinary differential equation (see Sect. Appendix 3).

In taking the temporal derivative we assumed small learning rates such that terms including $W˙_{ij}$ can be neglected. The derived dynamics for the membrane potential of a neuron $u_{i}$ in Equation 22 show the usual leaky behavior of biological neurons. However, both presynaptic rates $r‾_{i}$ and prediction errors $e‾_{i}$ enter the equation of motion with lookaheads, i.e., they are advanced ($r_{i}=r‾_{i}+\taur‾˙_{i}$ and $e_{i}=e‾_{i}+\taue‾˙_{i}$), cancelling the low-pass filtering. Since $r‾˙_{i}=ρ^{′}(u_{i})u˙_{i}$, the rate and error, $r_{i}$ and $e_{i}$, can also be seen as nonlinear extrapolations from the voltage and its derivative into the future.

The instantaneous transmission of information throughout the network at the level of the voltages can now be seen by low-pass filtering Equation 22 with initialization far back in the past,

$$
𝒖=𝒖+\tau𝒖˙=𝑾𝒓+𝒆=𝑾𝒓‾(𝒖)+𝒆‾,
$$

with column vector $𝒓‾(𝒖)=(𝒓‾_{in},ρ(𝒖))^{T}$ and $𝒆‾=𝒓‾_{net}^{′}⋅𝑾_{net}^{T}𝒆‾+\beta𝒆‾^{*}$. Hence, solving the voltage dynamics for $𝒖$ (Equation 7a), with apical voltage $𝒆=𝒆‾+\tau𝒆‾˙$ derived from Equation 7b, yields the somatic voltage $𝒖$ satisfying the self-consistency Equation 23 at any time. In other words, $𝒖$ and $𝒆‾$‘propagate instantaneously’.

### Deriving the error backpropagation formula

For clarity, we derive the error backpropagation algorithm for layered networks here. These can be seen as a special case of a general network with membrane potentials $𝒖$ and all-to-all weight matrix $𝑾$ (as introduced in Appendix 8), where the membrane potentials decompose into layerwise membrane potential vectors $𝒖_{l}$ and the weight matrix into according to block diagonal matrices $𝑾_{l}$ (with $𝑾_{l}$ being the weights that project into layer $l$).

Assuming a network with $N$ layers, by low-pass filtering the equations of motion we get

$$
u_{l}=W_{l}r¯_{l−1}+e¯_{l},
$$

for all $l\in1,..,N$, with the output error $𝒆‾_{𝒐}$ of the general recurrent network becoming the error in the last layer, that itself is the target error, $𝒆‾_{𝒐}=𝒆‾_{N}=\beta𝒆‾^{*}=\beta(𝒖_{N}^{*}−𝒖_{N})$. The error $𝒆‾=𝝐‾+\beta𝒆‾^{*}$, that we obtain from the general dynamics with $𝝐‾=𝒓‾_{net}^{′}⋅𝑾_{net}^{T}𝒆‾$, see Equations 21 and 22, translates to an iterative formula for the error at the current layer $l$ given the error at the downstream layer $l+1$, inherited from the drive $𝒓‾_{l}=ρ(𝒖_{l})$ of that downstream layer via $𝑾_{l+1}$,

$$
e¯_{l}=r¯_{l}^{′}⋅W_{l+1}^{T}e¯_{l+1}   for   l<N.
$$

and $𝒆‾_{N}=\beta𝒆‾^{*}$ for the output layer. The learning rule that reduces $𝒆‾_{l}$ by gradient descent is proportional to this error and the presynaptic rate, as stated by Theorem 1, is

$$
W˙_{l}∝(u_{l}−W_{l}r¯_{l−1})r¯_{l−1}^{T}=e¯_{l}r¯_{l−1}^{T},
$$

for $l=1...N$. Equations 25 and 26 together take the form of the error backpropagation algorithm, where an output error is iteratively propagated through the network and used to adjust the weights in order to reduce the output cost $C$. From this, it is easy to see that without output nudging (i.e. $\beta=0$), the output error vanishes and consequently all other prediction errors vanish as well, $𝒆‾_{l}=𝒖_{l}−𝑾_{l}𝒓‾_{l}=0$ for all $l\leqN$. This also means that in the absence of nudging, no weight updates are performed by the plasticity rule.

The learning rule for arbitrary connectivities is obtained in the same way by dropping the layer-wise notation. In this case, low-pass filtering the equations of motion yields $𝒖=𝑾𝒓‾+𝒆‾$, as calculated in 23, and the low-pass filtered error $𝒆‾=𝝐‾+\beta𝒆‾^{*}=𝒓‾_{net}^{′}⋅𝑾_{net}^{T}𝒆‾+\beta𝒆‾^{*}$, as inferred from Equations 21 and 22. Hence, the plasticity rule in general reads

$$
W˙∝(u−Wr¯)r¯^{T}=e¯r¯^{T}, with e¯=r¯_{net}^{′}⋅W_{net}^{T}e¯+\betae¯^{∗}.
$$

### Proving theorem 1 (rt-DeEP)

The implicit assumption in Theorem 1 is that $𝒖˙$ exists in the distributional sense for $t>−∞$, which is the case for delta-functions in $𝒓_{in}$ and step-functions in $𝒖^{*}$. Both parts (i) and (ii) of the Theorem are based on the requirement of stationary action $\deltaA=0$, and hence on $𝒖$ satisfying the Euler-Lagrange equations in the form of Equation 22, $(1+\tau\frac{d}{dt})\frac{∂L}{∂𝒖}=0$. From the solution $\frac{∂L}{∂u_{i}}=ce^{−\frac{t−t_{0}}{\tau}}$ we conclude that for initialization at $t_{0}=−∞$ we have $\frac{∂L}{∂𝒖}=0$ for all $t$. It is the latter stronger condition that we require in the proof. With this, the main ingredient of the proof follows is the mathematical argument of Scellier and Bengio, 2017, according to which the total and partial derivative of $L$ with respect to $𝑾$ are identical, and this in our case is true for any time $t$,

$$
\frac{dL}{dW}=\frac{∂L}{∂u}^{T}\frac{du}{dW}+\frac{∂L}{∂W}=\frac{∂L}{∂W},
$$

For convenience we considered $\frac{∂L}{∂𝒖}$ to be a column vector, deviating from the standard notations (see tutorial end of sec:Integration). Analogously to Equation 28, we infer $\frac{dL}{d\beta}=\frac{∂L}{∂\beta}$. Reading Equation 28 from the right to the left, we conclude that the learning rule $𝑾˙∝−\frac{∂L}{∂𝑾}=𝒆‾𝒓‾^{T}$ for all $\beta>0$ is gradient descent on $L$, i.e., $𝑾˙∝−\frac{dL}{d𝑾}$. This total derivative of $L$ can be analyzed for large and small $\beta$.

(i) We show that in the limit of large $\beta$, $𝑾˙$ becomes gradient descent on the mismatch energy $E^{M}=\frac{1}{2}‖𝒆‾‖^{2}$. For this we first show that there is a solution of the self-consistency equation $𝒖=𝑭(𝒖)=𝑾𝒓‾+𝒓‾_{net}^{′}⋅𝑾_{net}^{T}𝒆‾+\beta𝒆‾^{*}$ that is uniformly bounded for all $t$ and $\beta$. For this we assume that the transfer function $ρ(u)$ is non-negative, monotonically increasing, and bounded, that its derivative $ρ^{′}(u)$ is bounded too, and that the input rates $𝒓_{in}$ and the target potentials $𝒖_{𝒐}^{*}$ are also uniformly bounded. To show that under these conditions we always find a uniformly bounded solution $𝒖(t)$, we first consider the case where the output voltages are clamped to the target, $𝒖_{𝒐}=𝒖_{𝒐}^{*}$ such that $𝒆‾^{*}=0$. For simplicity, we assume that $ρ^{′}(u)=0$ for $|u|\geqc_{0}$. For voltages $𝒖$ with $𝒖_{i}\leqc_{0}$ the recurrent input current $𝑾𝒓‾$ is bounded, say $|(𝑾𝒓‾)_{j}|\leqc_{1}$ for some $c_{1}>c_{0}$. When including the error term $𝒓‾_{net}^{′}⋅𝑾_{net}^{T}𝒆‾$, the total current still remains uniformly bounded, say $|𝑭(𝒖)_{j}|\leqc_{2}$ for all $𝒖$ with $𝒖_{i}\leqc_{0}$. Because for larger voltages $𝒖_{i}>c_{0}$ the error term vanishes due to a vanishing derivative $ρ^{′}(𝒖_{i})=0$, the mapping $𝑭(𝒖)$ maps the $c_{2}$-box $𝒖$ (for which $|𝒖_{i}|\leqc_{2}$) onto itself. Brouwer’s fixed point theorem then tells us that there is a fixed point $𝒖=𝑭(𝒖)$ within the $c_{2}$-box. The theorem requires the continuity of $𝑭$, and this is assured if the neuronal transfer function $r‾=ρ(u)$ is continuous.

We next relax the voltages of the output neurons from their clamped stage, $𝒖_{𝒐}=𝒖_{𝒐}^{*}$. Remember that these voltages satisfy $𝒖_{𝒐}=(𝑾𝒓‾+𝒓‾_{net}^{′}⋅𝑾_{net}^{T}𝒆‾+\beta𝒆‾^{*})_{𝒐}=𝑭(𝒖)_{𝒐}$ at any time $t$. We determine the correction term $\beta𝒆‾_{𝒐}^{*}$ such that in the limit $\beta→∞$ we get $𝒖_{𝒐}=𝑭(𝒖)_{𝒐}=𝒖_{𝒐}^{*}$. The correction remains finite, and in the limit must be equal to $lim\beta→∞⁡\beta𝒆‾_{𝒐}^{*}=𝒖_{𝒐}^{*}−(𝑾𝒓‾+𝒓‾_{net}^{′}⋅𝑾_{net}^{T}𝒆‾)_{𝒐}$. For arbitrary large nudging strength $\beta$, the output voltage $𝒖_{𝒐}$ deviates arbitrary little from the target voltage, $𝒖_{𝒐}=𝒖_{𝒐}^{*}+o(1/\beta)$, with target error $𝒆‾_{𝒐}^{*}=\frac{1}{\beta}(𝒖−𝑾𝒓‾−𝒓‾_{net}^{′}⋅𝑾_{net}^{T}𝒆‾)_{𝒐}$ shrinking like $c_{2}/\beta$. Likewise, also for non-output neurons i, the self-consistency solution $𝒖_{i}=𝑭(𝒖)_{i}$ deviates arbitrarily little from the solution of the clamped state. To ensure the smooth drift of the fixed point while $1/\beta$ deviates from 0 we require that the Jacobian of $𝑭$ at the fixed point is invertible.

Because the output $𝒆‾_{𝒐}^{*}$ shrinks with $1/\beta$, the cost shrinks quadratically with increasing nudging strength, $C=\frac{1}{2}‖𝒆‾^{*}‖^{2}=o(\frac{1}{\beta^{2}})$, and hence the cost term $\frac{\beta}{2}‖𝒆‾^{*}‖^{2}$ that enters in $L=E^{M}+\frac{\beta}{2}‖𝒆‾^{*}‖^{2}$ vanishes in the limit $\beta→∞$. In this large $\beta$ limit, where $𝒆‾_{𝒐}^{*}=0$ and hence the outputs are clamped, $𝒖_{𝒐}=𝒖_{𝒐}^{*}$, the Lagrangian reduces to the mismatch energy, $L=E^{M}$. Along the least-action trajectories, we, therefore, get $𝑾˙∝−\frac{∂L}{∂𝑾}=−\frac{dL}{d𝑾}=−\frac{dE^{M}}{d𝑾}$. The first equality uses Equation 28, and the second uses $L=E^{M}$ just derived for $\beta=∞$. This is a statement ($i$) of Theorem 1. In the case of successful learning, $E^{M}=0$, we also conclude that the cost vanishes, $C=0$. This is the case because $E^{M}=0$ implies $E^{M}_{o}=0$ for all output neurons $o$. Since $E^{M}_{o}=\frac{1}{2}𝒆‾_{o}^{2}=\frac{1}{2}(𝒓‾_{net}^{′}⋅𝑾_{net}^{T}𝒆‾+\beta𝒆‾^{*})_{o}^{2}$, we conclude that $𝒆‾_{o}=0$, and if the output neurons do not feed back to the network (which we can assume without loss of generality), we conclude that $𝒆‾_{o}^{*}=0$.

(ii) To consider the case of small $\beta$, we use that the cost $C$ can be expressed as $C=\frac{∂L}{∂\beta}$. This is a direct consequence of how $C$ enters in $L=\frac{1}{2}‖𝒆‾‖^{2}+\frac{\beta}{2}C$, see Equation 16 and Scellier and Bengio, 2017. We now put this together with Equation 28 and the finding that $\frac{∂L}{∂\beta}=\frac{dL}{d\beta}$. Since for the Lipschitz continuous function $L$ in $u$, $W$, and $\beta$ ($L$ is even smooth in these arguments), the total derivatives interchange (which is a consequence of the Moore-Osgood theorem applied to the limits of the difference quotients), we then get at any $t$,

$$
\frac{dC}{dW}=\frac{d}{dW}\frac{∂L}{∂\beta}=\frac{d}{dW}\frac{dL}{d\beta}=\frac{d}{d\beta}\frac{dL}{dW}=\frac{d}{d\beta}\frac{∂L}{∂W}=−\frac{d}{d\beta}e¯r¯^{T}.
$$

The last expression is calculated from the specific form of the Lagrangian Equation 17, using that by definition $𝒆‾=𝒖−𝑾𝒓‾$.

Finally, in the absence of output nudging, $\beta=0$, we can assume vanishing errors, $𝒆‾=0$, as they solve the self-consistency equation, $𝒆‾=𝒓‾_{net}^{′}⋅𝑾_{net}^{T}𝒆‾$ for all $t$, see Equation 27. For these solutions we have $𝒆‾𝒓‾^{T}|_{\beta=0}=0$. Writing out the total derivative of the function $𝒈(\beta)=𝒆‾𝒓‾^{T}$ with respect to $\beta$ at $\beta=0$ as limit of the difference quotient, $\frac{d𝒈(\beta)}{d\beta}|_{\beta=0}=lim\beta→0⁡\frac{1}{\beta}(𝒈(\beta)−𝒈(0))=lim\beta→0⁡\frac{1}{\beta}𝒈(\beta)$, using that $𝒈(0)=0$, we calculate at any $t$,

$$
\frac{de¯r¯^{T}}{d\beta}|_{\beta=0}=lim\beta→0\frac{1}{\beta}(e¯r¯^{T}−e¯r¯^{T}|_{\beta=0})=lim\beta→0\frac{1}{\beta}e¯r¯^{T}.
$$

Here, we assume that $𝒆‾𝒓‾^{T}$ is evaluated at $\beta>0$ (that itself approaches 0), while $𝒆‾𝒓‾^{T}|_{\beta=0}$ is evaluated at $\beta=0$. Combining Equations 29 and 30 yields the cost gradient at any $t$,

$$
−\frac{dC}{dW}=lim\beta→0\frac{1}{\beta}e¯r¯^{T}.
$$

This justifies the gradient learning rule $𝑾˙$ in Equation 27. Learning is stochastic gradient descent on the expected cost, where stochasticity enters in the randomization of the stimulus and target sequences $𝒓_{in}(t)$ and $𝒖^{*}(t)$. For the regularity statement, see ‘From implicit to explicit differential equations’ in the sec:Integration. Notice that this proof works for a very general form of the Lagrangian $L$, until the specific expression for $\frac{∂L}{∂𝑾}$. For a proof in terms of partial derivatives only, see Appendix 8, and for a primer on partial and total derivatives see Appendix 7.

### Instantaneous gradient descent on C(𝒖𝒐*,𝒓in)

The cost $C=\frac{1}{2}‖𝒖_{𝒐}^{*}−𝒖_{𝒐}‖^{2}$ at each time $t$ is a function of the voltage $𝒖_{𝒐}$ of the output neurons and the corresponding targets. In a feedforward network, due to the instantaneity of the voltage propagation Equation 23, $𝒖_{𝒐}$ is in the absence of output nudging ($\beta=0$) an instantaneous function of the voltage at the first layer, $𝒖_{1}(t)=𝑾_{in}𝒓_{in}(t)+𝒖_{1}(t_{0})e^{−\frac{t−t_{0}}{\tau}}$. For initialisation at $t_{0}=−∞$, the second term vanishes for all $t$ and hence $𝒖_{1}(t)=𝑾_{in}𝒓_{in}(t)$. The output voltage $𝒖_{𝒐}(t)$, therefore, becomes a function $𝑭_{W}$ of the low-pass filtered input rate $𝒓_{in}(t)$ that captures the instantaneous network mapping, $𝒖_{𝒐}(t)=𝑭_{W}(𝒓_{in}(t))$, and with this the cost also becomes an instantaneous function of $𝒓_{in}$ and $𝒖_{𝒐}^{*}$, namely $C(t)=\frac{1}{2}‖𝒖_{𝒐}^{*}(t)−𝒖_{𝒐}(t)‖^{2}=\frac{1}{2}‖𝒖_{𝒐}^{*}(t)−𝑭_{W}(𝒓_{in}(t))‖^{2}$.

For a general network, again assuming $t_{0}=−∞$, the voltage is determined by the vanishing gradient $\frac{∂L}{∂𝒖}=𝒇(𝒖,t)=𝒖−𝑾𝒓‾(𝒖)−𝒆‾(𝒖)=0$ with $𝒆‾=𝝐‾−\beta𝒆‾^{*}$, see Equation 21. For the inclusive treatment of the initial transient see Appendix 3 and Appendix 4. Remember that $𝒓‾=(𝒓‾_{in},𝒓‾_{net}(𝒖))^{T}$ and $𝒆‾^{*}=𝒖_{𝒐}^{*}−𝒖_{𝒐}$. For a given $𝒓‾_{in}$ and $𝒖_{𝒐}^{*}$ at time $t$, the equation $𝒇(𝒖,t)=0$ can be locally solved for $𝒖$ if the Hessian $𝑯=\frac{∂^{2}L}{∂𝒖^{2}}=\frac{∂𝒇}{∂𝒖}=1−𝑾_{net}𝝆^{′}−𝒆‾^{′}$ is invertible, $𝒖=𝑭(𝒓‾_{in},𝒖_{𝒐}^{*})$. This mapping can be restricted to the output voltages $𝒖_{𝒐}$ on the left-hand side, while replacing $𝒖_{𝒐}^{*}=𝒖_{𝒐}+𝒆‾_{𝒐}^{*}$ in the argument on the right-hand side (even if this again introduces $𝒖_{𝒐}$ there). With this, we obtain the instantaneous mapping $𝒖_{𝒐}(t)=𝑭_{W}(𝒓_{in}(t),𝒆‾_{𝒐}^{*}(t))$ from the low-pass filtered input and the output error to the output itself. Notice that for functional feedforward network, the network weight matrix $𝑾_{net}$ is lower triangular, and for small enough $\beta$ the Hessian $𝑯$ is, therefore, always positive definite (see also Methods, Sect. From implicit to explicit differential equations).

### Proving theorem 2 (rt-DeEL)

Here, we restrict ourselves to layered network architectures. To prove Theorem 2 first assume that interneurons receive no nudging ($\beta^{I}=0$) and only the lateral interneuron-to-pyramidal weights $𝑾^{PI}_{l}$ are plastic. This is already sufficient to prove the rt-DeEL theorem. Yet, simulations showed that learning the lateral pyramidal-to-interneuron weights $𝑾^{IP}_{l}$ via top-down nudging, so that the interneuron activity mimics the upper layer pyramidal neuron activity, helps in learning a correct error representation. We consider this case of learning $𝑾^{IP}_{l}$ later.

If the microcircuits is ought to correctly implement error backpropagation, all local prediction errors $𝒆‾_{l}$ must vanish in the absence of output nudging ($\beta=0$) as there is no target error. Consequently, any remaining errors in the network are caused by a misalignment of the lateral microcircuit. We show how learning the interneuron-to-pyramidal weights $𝑾^{PI}_{l}$ corrects for such misalignments.

To define the gradient descent plasticity of the weights $W^{PI}_{l}$ from the interneurons to the pyramidal neurons, we consider the apical error formed by the difference of top-down input and interneuron input, $𝒆‾_{l}^{A}=𝑩_{l}𝒖_{l+1}−𝑾^{PI}_{l}𝒖^{I}_{l}$, and define the apical mismatch energy as $E_{l}^{PI}=\frac{1}{2}‖𝒆‾_{l}^{A}‖^{2}$. Gradient descent along this energy with respect to $W^{PI}_{l}$ yields

$$
W˙_{l}^{PI}=η^{PI}e_{l}^{A}u_{l}^{IT}=η^{PI}(B_{l}u_{l+1}−W_{l}^{PI}u_{l}^{I})u_{l}^{IT}
$$

evaluated online while presenting input patterns from the data distribution to the network. We assume that the apical contribution to the somatic voltage is further modulated by the somatic spike rate, $𝒓‾_{l}^{′}⋅𝒆‾_{l}^{A}$. After successful learning, the top-down input $𝑩_{l}𝒖_{l+1}$ is fully subtracted away by the lateral input in the apical compartment, and we have

$$
B_{l}u_{l+1}=W_{l}^{PI}u_{l}^{I}.
$$

Once this condition is reached, the network achieves a state where, over the activity space spanned by the data, top-down prediction errors throughout the network vanish,

$$
e¯_{l}=r¯_{l}^{′}⋅e¯_{l}^{A}=r¯_{l}^{′}⋅(B_{l}u_{l+1}−W_{l}^{PI}u_{l}^{I})=0.
$$

We show that this top-down prediction error, after the successful learning of the microcircuit, shares the properties of error-backpropagation for a suitable backprojection weights $𝑩$.

Due to the vanishing prediction errors, pyramidal cells only receive bottom-up input $𝒖_{l+1}=𝑾_{l+1}𝒓‾_{l}$. Using this expression as well as the expression for interneuron membrane potentials without top-down nudging ($\beta^{I}=0$ in Equation 9), $𝒖^{I}_{l}=𝑾^{IP}_{l}𝒓‾_{l}$, and plugging both into Equation 33, we get

$$
B_{l}W_{l+1}r¯_{l}=W_{l}^{PI}W_{l}^{IP}r¯_{l}.
$$

Assuming that $𝑾^{IP}_{l}$ has full rank, and the low-pass filtered rates $𝒓‾_{l}$ span the full $n_{l}$ dimensions of layer $l$ when sampled across the data set, we conclude that

$$
B_{l}W_{l+1}=W_{l}^{PI}W_{l}^{IP}.
$$

In other words, the loop via upper layer and back is learned to be matched by a lateral loop through the interneurons.

Equation 36 imposes a restriction on the minimal number of interneurons $n_{l}^{I}$ at layer $l$. In fact, the matrix product $𝑩_{l}𝑾_{l+1}$ maps a $n_{l}$-dimensional space onto itself via $n_{l+1}$-dimensional space. The maximal rank of the this matrix product is limited by the smallest dimension, i.e., $rank(𝑩_{l}𝑾_{l+1})\leqmin(n_{l},n_{l+1})$. Analogously, $rank(𝑾^{PI}_{l}𝑾^{IP}_{l})\leqmin(n_{l},n_{l}^{I})$. But since the two ranks are the same according to Equation 36, we conclude that in general $n_{l}^{I}\geqmin(n_{l},n_{l+1})$ must hold, i.e., there should be at least as many interneurons at layer $l$ as the lowest number of pyramidal neurons at either layer $l$ or $l+1$. Note that by choosing $n_{l}^{I}=n_{l+1}$ as in Sacramento et al., 2018 (or $n_{l}^{I}>n_{l+1}$ as in this work), the conditions is fulfilled.

With $𝒖^{I}_{l}=𝑾^{IP}_{l}𝒓‾_{l}$ and Equation 36, the top-down prediction error from Equation 34, in the presence of output nudging ($\beta>0$), can be written in the backpropagation form

$$
e¯_{l}=r¯_{l}^{′}⋅(B_{l}u_{l+1}−W_{l}^{PI}u_{l}^{I})=r¯_{l}^{′}⋅(B_{l}u_{l+1}−W_{l}^{PI}W_{l}^{IP}r¯_{l})
$$



$$
=r¯_{l}^{′}⋅(B_{l}u_{l+1}−B_{l}W_{l+1}r¯_{l})=r¯_{l}^{′}⋅B_{l}(u_{l+1}−W_{l+1}r¯_{l})
$$



$$
=r¯_{l}^{′}⋅B_{l}e¯_{l+1}=r¯_{l}^{′}⋅B_{l}r¯_{l+1}^{′}⋅e¯_{l+1}^{A}.
$$

Finally, the simulations showed that learning the lateral weights in the microcircuit greatly benefits from also adapting the pyramidal-to-interneuron weights $𝑾^{IP}$ by gradient descent on $E^{IP}=\frac{1}{2}\suml‖𝒖^{I}_{l}−𝑾^{IP}_{l}𝒓‾_{l}‖^{2}$, using top-down nudging of the inhibitory neurons ($\beta^{I}>0$),

$$
W˙_{l}^{IP}=η^{IP}(u_{l}^{I}−W_{l}^{IP}r¯_{l})r¯_{l}^{T}.
$$

After learning we have $𝒖^{I}_{l}=𝑾^{IP}_{l}𝒓‾_{l}$, and plugging in $𝒖^{I}_{l}=(1−\beta^{I})𝑾^{IP}_{l}𝒓‾_{l}+\beta^{I}𝑩^{IP}_{l}𝒖_{l+1}$ (Equation 9), we obtain $𝑾^{IP}_{l}𝒓‾_{l}=𝑩^{IP}_{l}𝒖_{l+1}$. Since $𝒖_{l+1}=𝑾_{l+1}𝒓‾_{l}$, we conclude as before,

$$
W_{l}^{IP}=B_{l}^{IP}W_{l+1}.
$$

The top-down weights $B^{IP}_{l}$ that nudge the lower-layer interneurons has randomized entries and may be considered as full rank. If there are less pyramidal neurons in the upper layer than interneurons in the lower layer, $B^{IP}_{l}$ selects a subspace in the interneuron space of dimension $n_{l+1}<n_{l}^{I}$. This seems to simplify the learning of the interneuron-to-pyramidal cell connections $W^{PI}$. In fact, this learning now has only to match the $n_{l+1}$-dimensional interneuron subspace embedded in $n_{l}^{I}$ dimensions to an equal ($n_{l+1}$-)dimensional pyramidal cell subspace emedded in $n_{l}$ dimensions.

Learning of the interneuron-to-pyramidal cell connections works with the interneuron nudging as before, and combining Equations 36 with 39 yields the ‘loop consistency’

$$
B_{l}W_{l+1}=W_{l}^{PI}B_{l}^{IP}W_{l+1}.
$$

The learning of the microcircuit was described in the absence of output nudging. Conceptually, this is not a problem as one could introduce a pre-learning phase where the lateral connections are first correctly aligned before learning of the feedforward weights begins. In simulations we find that both the lateral connections as well as the forward connections can be trained simultaneously, without the need for such a pre-learning phase. We conjecture that this is due to the fact that our plasticity rules are gradient descent on the energy functions $L$, $E^{PI}$, and $E^{IP}$, respectively.

### From implicit to explicit differential equations

The voltage dynamics is solved by a forward-Euler scheme $𝒖(t+dt)=𝒖(t)+𝒖˙(t)dt$. The derivative $𝒖˙(t)$ is calculated either through (i) the implicit differential Equation 7a yielding $\tau𝒖˙(t)=𝒉(𝒖(t),𝒖˙(t−dt))$, or (ii) by isolating $𝒖˙(t)$ and solving for the explicit differential equation $\tau𝒖˙(t)=𝒈(𝒖(t))$, as explained in Appendix 3 (after Equation 51).

(i) The implicit differential equation, $\tau𝒖˙(t)=−𝒖(t)+𝑾𝒓(t)+𝒆(t)$, see Equation 22, is iteratively solved by assigning $𝒓(t)=ρ(𝒖(t))+ρ^{′}(𝒖(t))⋅𝒖˙(t−dt)$ and calculating the error $𝒆(t)=𝒆‾(t)+\tau𝒆‾˙(t)$ with $𝒆‾(𝒖)=ρ^{′}(𝒖)⋅𝑾_{net}^{T}(𝒖−𝑾_{net}ρ(𝒖)−𝑾_{in}𝒓‾_{in})+\beta𝒆‾^{*}$ and $𝒆‾˙(t)=𝒆‾^{′}(𝒖(t))⋅𝒖˙(t−dt)$.

This iteration exponentially converges to a fixed point $u˙(t)$ on a time scale $\frac{dt}{1−k}$, where $1−k>0$ is the smallest Eigenvalue of the Hessian $𝑯=\frac{∂^{2}L}{∂𝒖^{2}}=1−𝑾_{net}𝝆^{′}−𝒆‾^{′}$, see Appendix 3.

(ii) The explicit differential equation is obtained by eliminating the $𝒖˙$ from the right-hand side of the implicit differential equation. Since $𝒖˙$ enters linearly we get $\tau𝑯𝒖˙=−𝒇−\tau\frac{∂𝒇}{∂t}$ with $𝒇(𝒖,t)=\frac{∂L}{∂𝒖}=𝒖−𝑾𝒓‾−𝝐‾−\beta𝒆‾^{*}$. The explicit form is obtained by matrix inversion, $𝒖˙=𝒈(𝒖,t)=−\frac{1}{\tau}𝑯^{−1}(𝒇+\tau\frac{∂𝒇}{∂t})$, as the Hessian is invertible if it is strictly positive definite (which is typically the case, see Appendix 3, after Equation 48). The external input and the target enter through $\frac{∂𝒇}{∂t}=𝑾_{in}𝒓‾˙_{in}+\beta𝒖˙_{𝒐}^{*}$, where the derivative of the target voltage is only added for the output neurons $𝒐$. This explicit differential equation is shown to be contractive in the sense that for each input trajectory $𝒓_{in}(t)$ and target trajectory $𝒖^{*}(t)$, the voltage trajectory $𝒖(t)$ is locally attracting for neighbouring trajectories. This local attracting trajectory is the vanishing-gradient trajectory $𝒇(𝒖,t)=0$, and the gradient remains 0 even if the input contains delta-functions, see Appendix 4.

#### Moving and latent equilibria: a formal definition

We showed that the motor output ($𝒖_{𝒐}$), together with the low-pass filtered sensory input ($𝒓‾_{in}$) and the motor feedback ($𝒆‾_{𝒐}^{*}$) is in a moving equilibrium, $𝒖_{𝒐}=𝑭_{W}(𝒓‾_{in},𝒆‾_{𝒐}^{*})$, see Figure 3a. In general, a dynamical system in $𝒖$ that is given in an implicit form $𝑮(𝒙,𝒙˙,𝒖,𝒖˙)=0$ with external inputs $(𝒙,𝒙˙)$ is said to be in a moving equilibrium if the variable $𝒖$ is an instantaneous function of the input $𝒙$ at any point in time, $𝒖=𝑭(𝒙)$. The fact that the implicit differential equation $𝑮=0$ represents a dynamical system in $𝒖$ implies that, in principle, it has a representation in the explicit form $𝒖˙=𝒈(𝒖,𝒙,𝒙˙)$, guaranteed by an invertible Jacobian $\frac{∂𝑮}{∂𝒖˙}$.

Our example is obtained from $𝑮=(1+𝝉⋅\frac{d}{dt})𝒇$ with $𝒇(𝒖,𝒙)=\frac{∂L}{∂𝒖}$ and $𝒙=(𝒓‾_{in},𝒆‾_{𝒐}^{*})$, leading to $𝒙+𝝉⋅𝒙˙=(𝒓_{in},𝒆_{𝒐}^{*})$. Given the paramterization of $𝑮$ by the weights, we get the parametrized function $𝒖=𝑭_{W}(𝒙)$, and this is restricted to the output components $𝒖_{𝒐}$ of $𝒖$. The condition on the Jacobian translates to $\frac{∂𝑮}{∂𝒖˙}=\frac{∂𝒇}{∂𝒖}=\frac{∂^{2}L}{∂𝒖^{2}}$ being invertible. Crucially, the description of the dynamics in the biological or physical substrate is not given in its explicit form $𝒖˙=𝒈(𝒖,𝒙,𝒙˙)$. However, it is given in an implicit form expressed as $𝒖˙=𝒉(𝒙,𝒙˙,𝒖,𝒖˙)$, where $𝒖˙$ still appears on the right-hand side. This ‘hybrid’ form is directly solved either in real time by the biophysical substrate itself, or by the forward-Euler scheme on clocked hardware, see ($i$) above. Notice that moving equilibria $𝒖=𝑭_{W}(𝒙)$ with $𝒙=(𝒓‾_{in},𝒆‾_{𝒐}^{*})$ are able to capture complex temporal processing of the instantaneous input $𝒓_{in}$. In fact, the low-pass filtering $𝒓‾_{in}$ can be obtained on various time scales through different $\tau_{in}$’s, and $𝑭_{W}$ for a general network $𝑾$ can be arbitrary complex. The task is to adapt $𝑾$ such that the ‘hybrid’ dynamical system eventually implements the target mapping $𝒖_{𝒐}^{*}=𝑭^{*}(𝒙)$.

The Latent Equilibrium (Haider et al., 2021) can be analogously formalized as a dynamical system in $𝒖$, implicitly given by $𝑮(𝒙,𝒖,𝒖˙)=0$, and having a solution of the form $𝒖+𝝉⋅𝒖˙=𝑭(𝒙)$. Abbreviating again $𝒇(𝒖,𝒙)=\frac{∂L}{∂𝒖}$ with the same Lagrangian $L=\frac{1}{2}‖𝒖−𝑾ρ(𝒖)‖^{2}+\frac{\beta}{2}C$ as in the present NLA, the Latent Equilibrium is obtained for $𝑮(𝒙,𝒖,𝒖˙)=𝒇(𝒖+𝝉⋅𝒖˙,𝒙)$. The solution implies that the rate $𝒓=ρ(𝒖+𝝉⋅𝒖˙)=ρ(𝑭(𝒙))$ is an instantaneous function of $𝒙=(𝒓_{in},𝒆_{𝒐}^{*})$, here without low-pass filtering. As for moving equilibria, the crucial point is that the biophysical substrate implements a hybrid form of the dynamical system, now $𝒖˙=𝒉(𝒙,𝒖,𝒖˙)$, that is implicitly solved by the analog substrate, and also allows for a solution in clocked hardware. For an extended stability analysis of the moving and latent equilibria see Appendix 4.

### Simulation details

Solving the explicit differential equation seems to be more robust when the learning rate for $𝑾˙$ gets larger. The explicit form is also less sensitive to large Euler steps $dt$, see Appendix 3. By this reason, the ordinary differential equations (ODE) were solved in the explicit form when including plasticity $𝑾˙$. The algorithms are summarized as follows, once without interneurons (Algorithm 1), and once with interneurons (Algorithm 2):

<table>
  <thead>
    <tr>
      <th>Algorithm 1. with projection neurons only, for Figures 3 and 4 (using the explicit ODE, i.e., Step 12 instead of 11)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1: current state: u(t), W(t)2: # consider full vectors and matrices (padded with 0’s for feedforward networks)3:# drop time argument (t) for convenience4: r¯net←ρ(u), r¯←(r¯in,r¯net)T , W←(Win,Wnet)5: calculate weight derivatives6: W˙←η(u−Wr¯)r¯T7: calculate low-pass-filtered errors8: e¯o∗←uo∗−uo, e¯i∗=0 for non-output neurons9: e¯←r¯net′⋅WnetT(u−Wr¯)+βe¯∗10: calculate temporal voltage derivatives either implicitly (11) or explicitly (12)11: Implicit:  τu˙←−u+W(r¯+τr¯˙)+(e¯+τe¯˙)12: Explicit: f←u−Wr¯−e¯ , H←∂f∂u , u˙← solve τH(u)u˙=−f−τ∂f∂t via Cholesky decomposition13: update voltage and weights14: u←u+u˙⋅dt, W←W+W˙⋅dt</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Algorithm 2. including plastic interneurons, for Figure 5 (using the explicit ODE, i.e., Step 13 instead of 12)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1: current state: u(t), W(t),uI(t),WPI(t),WIP(t)2: # consider full vectors and matrices and drop time argument as in Algorithm 13: r¯←(r¯in,ρ(u))T4: calculate weight derivatives5: W˙←η(u−Wr¯)r¯T6: W˙PI←ηPI(Bu−WPIuI)uIT7: W˙IP←ηIP(uI−WIPr¯)r¯T8: calculate low-pass filtered errors9: e¯o∗←uo∗−uo (e¯i∗=0 for non-output neurons i)10: e¯←Bu−WPIuI+βe¯∗ (Bo,:=Wo,:PI=0 for output neurons o)11: calculate temporal voltage derivatives either implicitly (12) or explicitly (13)12: Implicit: τu˙←−u+W(r¯+τr¯˙)+(e¯+τe¯˙)13: Explicit: f←u−Wr¯−e¯ , H←∂f∂u , u˙← solve τH(u)u˙=−f−τ∂f∂t via Cholesky decomposition14: update network state \ForX∈{u,W,WPI,WIP}15: X←X+X˙dt End For16: uI←(1−βI)WIPr¯+βIBIPu</td>
    </tr>
  </tbody>
</table>

#### Details for Figure 3b

Color coded snapshot of cortical local field potentials (LFPs) in a human brain from 56 deep iEEG electrodes at various locations, converted with the sigmoidal voltage-to-rate function $r‾(u)=\frac{1}{1+e^{−u}}$ and plotted onto a standard Talairach Brain (Talairach and Tournoux, 1988). The iEEG data is from a patient with pharmacoresistant epilepsy and electrodes implanted during presurgical evaluation, extracted from the data release of Burrello et al., 2019. The locations of the electrodes are chosen in accordance with plausibilty, as the original positions of the electrodes were omitted due to ethical standards to prevent patient identification.

#### Details for Figure 3c

Simulations of the voltage dynamics (Equation 7a) and weight dynamics (Equation 8), with learning rate $η=10^{−3}$, step size $dt=$ 1ms for the forward Euler integration, membrane time constant  $\tau=10ms$ and logistic activation function. Weights were initialized randomly from a normal distribution $N(0,0.1^{2})$ with a cut-off at ± 0.3. The number of neurons in the network $N$ was $n=96$, among them 56 output neurons $O⊂N$ that were simultaneously nudged, and 40 hidden neurons. During training, all output neurons were nudged simultaneously (with $\beta=0.1$), whereas during testing, only 42 out of 56 neurons were nudged, the remaining 14 left to reproduce the traces. Data points of the iEEG signal were sampled with a frequency of 512 Hz. For simplicity, we, therefore, assumed that successive data points are separated by 2ms, and up-sampled the signal via simple interpolation to 1 ms resolution as required by our integration scheme. Furthermore, the raw values were normalized by dividing them by a factor of 200 to ensure that they are approximately in a range of ±1–2. Training and testing was done on two separate 8 s traces of the iEEG recording. Same data as in Figure 3b1.

#### Details for Figure 4

Simulation of the neuronal and synaptic dynamics as given by Equation 8, Equation 7a, Equation 7b. For 5 ms, 10 ms, and 50 ms presentation time, we used an integration step size of $dt=0.05ms$, $dt=0.1ms$ and $dt=0.5ms$, respectively (and $dt=1ms$ otherwise). As an activation function, we used the step-linear function (hard sigmoidal) with $r‾(u)=0$ for $u\leq0$, $r‾(u)=1$ for $u\geq1$ and $r‾(u)=u$ in between. The learning rate was initially set to $η=10^{−3}$ and then reduced to $η=10^{−4}$ after 22,000 s. The nudging strength was $\beta=0.1$ and the membrane time constant $\tau=10ms$. In these simulations (and only for these) we assumed that at each presynaptic layer $l=0,1,..,n−1$ there is a first neuron indexed by 0 that fires with constant rate $r‾_{l,0}=1$, effectively allowing the postsynaptic neurons $𝒓‾_{l+1}$ to learn a bias through the first column of the weight matrix $𝑾_{l+1}$. Weights were initialized randomly from a normal distribution $N(0,0.01^{2})$ with a cut-off at ±0.03. For an algorithmic conversion see the scheme below. In Figure 4c1, ‘rt-DeEP w/o lookahead’ is based on the dynamics $\tau𝒖˙=−𝒖+𝑾𝒓‾+𝒆‾$. For ‘$𝒖˙$ w/o error + backprop,’ we use $\tau𝒖˙=−𝒖+𝑾𝒓$ as the forward model (so without error terms on the membrane potential, but a prospective $𝒓$), and calculate weight updates using error backpropagation. In 4c2, we provide three controls: the test error for (i) a standard shallow artificial neural network trained on MNIST (black dashed line), (ii) rt-DeEP without prospective coding (as in Figure 4c1), but in Figure 4c2 with plasticity only turned on when the network is completely stationary, i.e., after waiting for several 100ms, such that synaptic weights are not changed during transients (orange dashed line, denoted by ‘w/o transients’), and (iii) an equivalent artificial neural network, $𝒖_{l}=𝑾_{l}𝒓‾_{l−1}$, trained using error backpropagation (black dashed line, ‘standard backprop’).

#### Details for Figure 5

Simulation of neuronal and synaptic dynamics with plastic microcircuit, i.e., the pyramidal-to-interneuron and lateral weights of the microcircuit learned during training.

For the results shown in Figure 5c2, the following parameters were used. As an activation function, we used a hard sigmoid function and the membrane time constant was set to $\tau=10$ ms. Image presentation time is 100ms. Forward, pyramidal-to-interneuron and interneuron-to-pyramidal weights were initialized randomly from a normal distribution $N(0,0.01^{2})$ with a cut-off at ±0.03. All learning rates were chosen equal $η=10^{−3}$ and were subsequently reduced to $η=10^{−4}$ after 22,000 s training time. The nudging parameters were set to $\beta=0.1$ and $\beta^{I}=\frac{0.1}{1.1}$. The feedback connections $𝑩_{l}$ and the nudging matrices $𝑩_{l}^{IP}$ were initialized randomly from a normal distribution $5⋅N(0,0.01^{2})$ with a cut-off at ±0.15. The used integration step size was $dt=0.25$ ms. All weights were trained simultaneously. For an algorithmic conversion see the scheme below. The interneuron membrane potential was calculated by Equation 9 with a linear transfer function.
