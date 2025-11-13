# Predicting non-linear dynamics by stable local learning in a recurrent spiking neural network

## Authors

- Aditya Gilra<sup>1</sup> ([ORCID: 0000-0002-8628-1864](https://orcid.org/0000-0002-8628-1864)) †
- Wulfram Gerstner<sup>1</sup>

### Affiliations

1. Brain-Mind Institute, School of Life Sciences École Polytechnique Fédérale de Lausanne Lausanne Switzerland
2. School of Computer and Communication Sciences École Polytechnique Fédérale de Lausanne Lausanne Switzerland

† Corresponding author

## Abstract

The brain needs to predict how the body reacts to motor commands, but how a network of spiking neurons can learn non-linear body dynamics using local, online and stable learning rules is unclear. Here, we present a supervised learning scheme for the feedforward and recurrent connections in a network of heterogeneous spiking neurons. The error in the output is fed back through fixed random connections with a negative gain, causing the network to follow the desired dynamics. The rule for Feedback-based Online Local Learning Of Weights (FOLLOW) is local in the sense that weight changes depend on the presynaptic activity and the error signal projected onto the postsynaptic neuron. We provide examples of learning linear, non-linear and chaotic dynamics, as well as the dynamics of a two-link arm. Under reasonable approximations, we show, using the Lyapunov method, that FOLLOW learning is uniformly stable, with the error going to zero asymptotically.

## Introduction

Over the course of life, we learn many motor tasks such as holding a pen, chopping vegetables, riding a bike or playing tennis. To control and plan such movements, the brain must implicitly or explicitly learn forward models (Conant and Ross Ashby, 1970) that predict how our body responds to neural activity in brain areas known to be involved in motor control (Figure 1A). More precisely, the brain must acquire a representation of the dynamical system formed by our muscles, our body, and the outside world in a format that can be used to plan movements and initiate corrective actions if the desired motor output is not achieved (Pouget and Snyder, 2000; Wolpert and Ghahramani, 2000; Lalazar and Vaadia, 2008). Visual and/or proprioceptive feedback from spontaneous movements during pre-natal (Khazipov et al., 2004) and post-natal development (Petersson et al., 2003) or from voluntary movements during adulthood (Wong et al., 2012; Hilber and Caston, 2001) are important to learn how the body moves in response to neural motor commands (Lalazar and Vaadia, 2008; Wong et al., 2012; Sarlegna and Sainburg, 2009; Dadarlat et al., 2015), and how the world reacts to these movements (Davidson and Wolpert, 2005; Zago et al., 2005, 2009; Friston, 2008). We wondered whether a non-linear dynamical system, such as a forward predictive model of a simplified arm, can be learned and represented in a heterogeneous network of spiking neurons by adjusting the weights of recurrent connections.

![Figure 1.](https://cdn.elifesciences.org/articles/28295/elife-28295-fig1-v2.jpg)

**Figure 1.:** (A) During learning, random motor commands (motor babbling) cause movements of the arm, and are also sent to the forward predictive model, which must learn to predict the joint angles and velocities (state variables) of the arm. The deviation of the predicted state from the reference state, obtained by visual and proprioceptive feedback, is used to learn the forward predictive model with architecture shown in B. (B) Motor command $u→$ is projected onto neurons with random weights $e_{l⁢\beta}^{ff}$. The spike trains of these command representation neurons $S_{l}^{ff}$ are sent via plastic feedforward weights $w_{i⁢l}^{ff}$ into the neurons of the recurrent network having plastic weights $w_{i⁢j}$ (plastic weights in red). Readout weights $d_{\alpha⁢i}$ decode the filtered spiking activity of the recurrent network as the predicted state $x^_{\alpha}⁢(t)$. The deviations of the predicted state from the reference state of the reference dynamical system in response to the motor command, is fed back into the recurrent network with error encoding weights $k⁢e_{i⁢\alpha}$. (C) A cartoon depiction of feedforward, recurrent and error currents entering a neuron $i$ in the recurrent network. (D) Spike trains of a few randomly selected neurons of the recurrent network from the non-linear oscillator example are plotted (alternate red and blue colours are for guidance of eye only). A component $x^_{2}$ of the network output during a period of the oscillator is overlaid on the spike trains to indicate their relation to the output.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/28295/elife-28295-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** The neurons in the command representation layer and the recurrent network were heterogeneous with different gain functions due to different gains and biases. (A,B) Illustrative gain functions of a few neurons as a function of $J~_{i}≡\sum_{\alpha}e~_{i⁢\alpha}⁢x~_{\alpha}$ (cf. Equation (13). The x-intercept is the rheobase input $J~_{i}=J~_{i}^{0}$. (A) Neurons with constant gain $ν=2$ used in Figure 2. (B) Neurons with firing rate uniformly between 200 and 400 Hz at $J~_{i}=1$, used in all other simulations (cf. Figure 2—figure supplement 1).

Supervised learning of recurrent weights to predict or generate non-linear dynamics, given command input, is known to be difficult in networks of rate units, and even more so in networks of spiking neurons (Abbott et al., 2016). Ideally, in order to be biologically plausible, a learning rule must be online that is constantly incorporating new data, as opposed to batch learning where weights are adjusted only after many examples have been seen; and local that is the quantities that modify the weight of a synapse must be available locally at the synapse as opposed to backpropagation through time (BPTT) (Rumelhart et al., 1986) or real-time recurrent learning (RTRL) (Williams and Zipser, 1989) which are non-local in time or in space, respectively (Pearlmutter, 1995; Jaeger, 2005). Even though Long-Short-Term-Memory (LSTM) units (Hochreiter and Schmidhuber, 1997) avoid the vanishing gradient problem (Bengio et al., 1994; Hochreiter et al., 2001) in recurrent networks, the corresponding learning rules are difficult to interpret biologically.

Our approach toward learning of recurrent spiking networks is situated at the crossroads of reservoir computing (Jaeger, 2001; Maass et al., 2002; Legenstein et al., 2003; Maass and Markram, 2004; Jaeger and Haas, 2004; Joshi and Maass, 2005; Legenstein and Maass, 2007), FORCE learning (Sussillo and Abbott, 2009, 2012; DePasquale et al., 2016; Thalmeier et al., 2016; Nicola and Clopath, 2016), function and dynamics approximation (Funahashi, 1989; Hornik et al., 1989; Girosi and Poggio, 1990; Sanner and Slotine, 1992; Funahashi and Nakamura, 1993; Pouget and Sejnowski, 1997; Chow and Xiao-Dong Li, 2000; Seung et al., 2000; Eliasmith and Anderson, 2004; Eliasmith, 2005) and adaptive control theory (Morse, 1980; Narendra et al., 1980; Slotine and Coetsee, 1986; Weiping Li et al., 1987; Narendra and Annaswamy, 1989; Sastry and Bodson, 1989; Ioannou and Sun, 2012). In contrast to the original reservoir scheme (Jaeger, 2001; Maass et al., 2002) where learning was restricted to the readout connections, we focus on a learning rule for the recurrent connections. Whereas neural network implementations of control theory (Sanner and Slotine, 1992; DeWolf et al., 2016) modified adaptive feedback weights without a synaptically local interpretation, we modify the recurrent weights in a synaptically local manner. Compared to FORCE learning where recurrent synaptic weights have to change rapidly during the initial phase of learning (Sussillo and Abbott, 2009, 2012), we aim for a learning rule that works in the biologically more plausible setting of slow synaptic changes. While previous work has shown that linear dynamical systems can be represented and learned with local online rules in recurrent spiking networks (MacNeil and Eliasmith, 2011; Bourdoukan and Denève, 2015), for non-linear dynamical systems the recurrent weights in spiking networks have typically been computed offline (Eliasmith, 2005).

Here, we propose a scheme for how a recurrently connected network of heterogeneous deterministic spiking neurons may learn to mimic a low-dimensional non-linear dynamical system, with a local and online learning rule. The proposed learning rule is supervised, and requires access to the error in observable outputs. The output errors are fed back with random, but fixed feedback weights. Given a set of fixed error-feedback weights, the learning rule is synaptically local and combines presynaptic activity with the local postsynaptic error variable.

## Results

A forward predictive model (Figure 1A) takes, at each time step, a motor command $u→⁢(t)$ as input and predicts the next observable state $x^→⁢(t+Δ⁢t)$ of the system. In the numerical implementation, we consider $Δ⁢t=1$ms, but for the sake of notational simplicity we drop the $Δ⁢t$ in the following. The predicted system state $x^→$ (e.g., the vector of joint angles and velocities of the arm) is assumed to be low-dimensional with dimensionality $N_{d}$ (4-dimensional for a two-link arm). The motor command $u→⁢(t)$ is used to generate target movements such as ‘lift your arm to a location’, with a dimensionality $N_{c}$ of the command typically smaller than the dimensionality $N_{d}$ of the system state.

The actual state of the reference system (e.g., actual joint angles and velocities of the arm) is described by a non-linear dynamical system, which receives the control input $u→(t)\inR^{N_{c}}$ and evolves according to a set of coupled differential equations

$$
\frac{d⁢x_{\alpha}⁢(t)}{d⁢t}=h_{\alpha}⁢(x→⁢(t),u→⁢(t)),
$$

where $x→$ with components $x_{\alpha}$ (where $\alpha=1,…,N_{d}$) is the vector of observable state variables, and $h→$ is a vector whose components are arbitrary non-linear functions $h_{\alpha}$. For example, the observable system state $x→⁢(t)$ could be the joint angles and velocities of the arm deduced from visual and proprioceptive input (Figure 1A). We show that, with training, the forward predictive model learns to make the error

$$
ϵ_{\alpha}≡x_{\alpha}⁢(t)-x^_{\alpha}⁢(t)
$$

between the actual state $x→⁢(t)$ and the predicted state $x^→⁢(t)$ negligible.

### Network architecture for learning the forward predictive model

In our neural network model (Figure 1B), the motor command $u→⁢(t)$ drives the spiking activity of a command representation layer of 3000 to 5000 leaky integrate-and-fire neurons via connections with fixed random weights. These neurons project, via plastic feedforward connections, to a recurrent network of also 3000 to 5000 integrate-and-fire neurons. We assume that the predicted state $x^→$ is linearly decoded from the activity of the recurrent network. Denoting the spike train of neuron $i$ by $S_{i}⁢(t)$, the component $\alpha$ of the predicted system state is

$$
x^_{\alpha}⁢(t)=\sumid_{\alpha⁢i}⁢\int_{-∞}^{t}S_{i}⁢(s)⁢κ⁢(t-s)⁢d⁢s≡\sumid_{\alpha⁢i}⁢(S_{i}*κ)⁢(t),
$$

where $d_{\alpha⁢i}$ are the readout weights. The integral represents a convolution with a low-pass filter

$$
κ⁢(t)≡exp⁡(-t/\tau_{s})/\tau_{s},
$$

with a time constant $\tau_{s}=20$ ms, and is denoted by $(S_{i}*κ)⁢(t)$.

The current into a neuron with index $l$ ($l=1,…,N$), in the command representation layer comprising $N$ neurons, is

$$
J_{l}^{ff}=\sum\alphae_{l\alpha}^{ff}u_{\alpha}+b_{l}^{ff},
$$

Where $e_{k\alpha}^{ff}$ are fixed random weights, while $b_{l}^{ff}$ is a neuron-specific constant for bias (see Materials and methods) (Eliasmith and Anderson, 2004). We use Greek letters for the indices of low-dimensional variables (such as command) and Latin letters for neuronal indices, with summations going over the full range of the indices. The number of neurons $N$ in the command representation layer is much larger than the dimensionality of the input, that is $N≫N_{c}$.

The input current to a neuron with index $i$ ($i=1,…,N$) in the recurrent network is

$$
J_{i}=\sumlw_{il}^{ff}(S_{l}^{ff}∗κ)(t)+\sumjw_{ij}(S_{j}∗κ)(t)+\sum\alphake_{i\alpha}(ϵ_{\alpha}∗κ)(t)+b_{i},
$$

where $w_{i⁢l}^{ff}$ and $w_{i⁢j}$ are the feedforward and recurrent weights, respectively, which are both subject to our synaptic learning rule, whereas $k⁢e_{i⁢\alpha}$ are fixed error feedback weights (see below). The spike trains travelling along the feedforward path $S_{l}^{ff}$ and those within the recurrent network $S_{j}$ are both low-pass filtered (convolution denoted by $*$) at the synapses with the exponential filter $κ$ defined above. The constant parameter $b_{i}$ is a neuron specific bias (see Materials and methods). The constant $k>0$ is the gain for feeding back the output error. The number of neurons $N$ in the recurrent network is much larger than the dimensionality $N_{d}$ of the represented variable $x^$, that is $N≫N_{d}$.

For all numerical simulations, we used deterministic leaky integrate and fire (LIF) neurons. The voltage $V_{l}$ of each LIF neuron indexed by $l$, was a low-pass filter of its driving current $J_{l}$:

$$
\tau_{m}⁢\frac{d⁢V_{l}}{d⁢t}=-V_{l}+J_{l},
$$

with a membrane time constant, of $\tau_{m}=20$ ms. The neuron fired when the voltage $V_{l}$ crossed a threshold $\theta=1$ from below, after which the voltage was reset to zero for a refractory period $\tau_{r}$ of 2 ms. If the voltage went below zero, it was clipped to zero. Mathematically, the spike trains $S_{l}^{ff}(t)$ in the command representation layer and $S_{l}⁢(t)$ in the recurrent network, are a sequence of events, modelled as a sum of Dirac delta-functions.

Biases and input weights of the spiking neurons vary between one neuron and the next, both in the command representation layer and the recurrent network, yielding different frequency versus input curves for different neurons (Figure 1—figure supplement 1). Since arbitrary low-dimensional functions can be approximated by linear decoding from a basis of non-linear functions (Funahashi, 1989; Girosi and Poggio, 1990; Hornik et al., 1989), such as neuronal tuning curves (Sanner and Slotine, 1992; Seung et al., 2000; Eliasmith and Anderson, 2004), we may expect that suitable feedforward weights onto, and lateral weights within, the recurrent network can be found that approximate the role of the function $h→$ in Equation (1). In the next subsection, we propose an error feedback architecture along with a local and online synaptic plasticity rule that can train these feedforward and recurrent weights to approximate this role, while the readout weights are kept fixed, so that the network output mimics the dynamics in Equation (1).

### Negative error feedback via auto-encoder enables local learning

To enable weight tuning, we make four assumptions regarding the network architecture. The initial two assumptions are related to input and output. First, we assume that, during the learning phase, a random time-dependent motor command input $u→⁢(t)$ is given to both the muscle-body reference system described by Equation (1) and to the spiking network. The random input generates irregular trajectories in the observable state variables, mimicking motor babbling (Meltzoff and Moore, 1997; Petersson et al., 2003). Second, we assume that each component $x^_{\alpha}$ of the output predicted by the spiking network is compared to the actual observable output $x_{\alpha}$ produced by the reference system of Equation (1) and their difference (the output error $ϵ_{\alpha}$; Equation (2)) is calculated, similar to supervised learning schemes such as perceptron learning (Rosenblatt, 1961).

The final two assumptions are related to the error feedback. Our third assumption is that the readout weights $d_{\alpha⁢i}$ have been pre-learned, possibly earlier in development, in the absence of feedforward and recurrent connections, so as to form an auto-encoder of gain $k$ with the fixed random feedback weights $k⁢e_{i⁢\alpha}$. Specifically, an arbitrary value $ϵ_{\alpha}$ sent via the error feedback weights to the recurrent network and read out, from its $N$ neurons, via the decoding weights gives back (approximately) $k⁢ϵ_{\alpha}$. Thus, we set the decoding weights so as to minimize the squared error between the decoded output and required output $k⁢ϵ→$ for a set of randomly chosen vectors $ϵ→$ while setting feedforward and recurrent weights to zero (see Materials and methods). We used an algorithmic learning scheme here, but we expect that these decoding weights can also be pre-learned by biologically plausible learning schemes (D'Souza et al., 2010; Urbanczik and Senn, 2014; Burbank, 2015).

Fourth, we assumed that the error $ϵ_{\alpha}=x_{\alpha}-x^_{\alpha}$ is projected back to neurons in the recurrent network through the above-mentioned fixed random feedback weights. From the third term in Equation (6) and Figure 1B–C, we define a total error input that neuron $i$ receives:

$$
I_{i}^{ϵ}≡k⁢\sum\alphae_{i⁢\alpha}⁢ϵ_{\alpha},
$$

with feedback weights $k⁢e_{i⁢\alpha}$, where $k$ is fixed at a large constant positive value.

The combination of the auto-encoder and the error feedback implies that the output stays close to the reference, as explained now. In open loop that is without connecting the output $x^→$ and the reference $x→$ to the error node, an input $ϵ→$ to the network generates an output $x^→=k⁢ϵ→$ due to the auto-encoder of gain $k$. In closed loop, that is with the output and reference connected to the error node (Figure 1B), the error input is $ϵ→=x→-x^→$, and the network output $x^→$ settles to:

$$
x^→=kϵ→=k(x→−x^→)⟹x^→=\frac{k}{k+1}x→≈x→,
$$

that is approximately the reference $x→$ for large positive $k$. The fed-back residual error $ϵ→=x→/(k+1)$ drives the neural activities and thence the network output. Thus, feedback of the error causes the output $x^_{\alpha}$ to approximately follow $x_{\alpha}$, for each component $\alpha$, as long as the error feedback time scale is fast compared to the reference dynamical system time scale, analogous to negative error feedback in adaptive control (Narendra and Annaswamy, 1989; Ioannou and Sun, 2012).

While error feedback is on, the synaptic weights $w_{il}^{ff}$ and $w_{i⁢j}$ on the feedforward and recurrent connections, respectively, are updated as:

$$
w˙_{il}^{ff}=η(I_{i}^{ϵ}∗κ^{ϵ})(S_{l}^{ff}∗κ)(t),w˙_{ij}=η(I_{i}^{ϵ}∗κ^{ϵ})(S_{j}∗κ)(t),
$$

where $η$ is the learning rate (which is either fixed or changes on the slow time scale of minutes), and $κ^{ϵ}$ is an exponentially decaying filter kernel with a time constant of 80 or 200 ms. For a postsynaptic neuron $i$, the error term $I_{i}^{ϵ}*κ^{ϵ}$ is the same for all its synapses, while the presynaptic contribution is synapse-specific.

We call the learning scheme ‘Feedback-based Online Local Learning Of Weights’ (FOLLOW), since the predicted state $x^→$ follows the true state $x→$ from the start of learning. Under precise mathematical conditions, we show in Materials and methods that the FOLLOW scheme converges to a stable solution, while simultaneously deriving the learning rule (Materials and methods).

Because of the error feedback, with constant $k≫1$, the output is close to the reference from the start of learning. However, initially the error is not exactly zero, and this non-zero error drives the weight updates via Equation (10). After a sufficiently long learning time, a vanishing error ($ϵ_{\alpha}=0$ for all components) indicates that the neuronal network now autonomously generates the desired output, so that feedback is no longer required. In the Methods section, we show that not just the low-dimensional output $x^→$, but also the spike trains $S_{i}⁢(t)$, for $i=1,…,N$, are entrained by the error feedback to be close to the ideal ones required to generate $x→$.

During learning, the error feedback via the auto-encoder in a loop serves two roles: (i) to make the error current available in each neuron, projected correctly, for a local synaptic plasticity rule, and (ii) to drive the spike trains to the target ones for producing the reference output. In other learning schemes for recurrent neural networks, where neural activities are not constrained by error feedback, it is difficult to assign credit or blame for the momentarily observed error, because neural activities from the past affect the present output in a recurrent network. In the FOLLOW scheme, the spike trains are constrained to closely follow the ideal time course throughout learning, so that the present error can be attributed directly to the weights, enabling us to change the weights with a simple perceptron-like learning rule (Rosenblatt, 1961) as in Equation (10), bypassing the credit assignment problem. In the perceptron rule, the weight change $Δ⁢w∼(pre)⋅\delta$ is proportional to the presynaptic input $(pre)$ and the error $\delta$. In the FOLLOW learning rule of Equation (10), we can identify $(S_{i}*κ)$ with $(pre)$ and $(I_{i}^{ϵ}*κ^{ϵ})$ with $\delta$. In Methods, we derive the learning rule of Equation (10) in a principled way from a stability criterion.

FORCE learning (Sussillo and Abbott, 2009, 2012; DePasquale et al., 2016; Thalmeier et al., 2016; Nicola and Clopath, 2016) also clamps the output and neural activities to be close to ideal during learning, by using weight changes that are faster than the time scale of the dynamics. In our FOLLOW scheme, clamping is achieved via negative error feedback using the auto-encoder, which allows weight changes to be slow and makes the error current available locally in the post-synaptic neuron. Other methods used feedback based on adaptive control for learning in recurrent networks of spiking neurons, but were limited to linear systems (MacNeil and Eliasmith, 2011; Bourdoukan and Denève, 2015), whereas the FOLLOW scheme was derived for non-linear systems (see Methods). Our learning rule of Equation (10) uses an error $ϵ_{\alpha}≡x_{\alpha}-x^_{\alpha}$ in the observable state, rather than an error involving the derivative $d⁢x_{\alpha}/d⁢t$ in Equation (1), as in other schemes (see Appendix 1) (Eliasmith, 2005; MacNeil and Eliasmith, 2011). The reader is referred to Discussion for detailed further comparisons. The FOLLOW learning rule is local since all quantities needed on the right-hand-side of Equation (10) could be available at the location of the synapse in the postsynaptic neuron. For a potential implementation and prediction for error-based synaptic plasticity, and for a critical evaluation of the notion of ‘local rule’, we refer to the Discussion.

### Spiking networks learn target dynamics via FOLLOW learning

In order to check whether the FOLLOW scheme would enable the network to learn various dynamical systems, we studied three systems describing a non-linear oscillator (Figure 2), low-dimensional chaos (Figure 3) and simulated arm movements (Figure 4) (additional examples in Figure 2—figure supplement 2, Figure 2—figure supplement 4 and Materials and methods). In all simulations, we started with vanishingly small feedforward and recurrent weights (tabula rasa), but assumed pre-learned readout weights matched to the error feedback weights. For each of the three dynamical systems, we had a learning phase and a testing phase. During each phase, we provided time-varying input to both the network (Figure 1B) and the reference system. During the learning phase, rapidly changing control signals mimicked spontaneous movements (motor babbling) while synaptic weights were updated according to the FOLLOW learning rule Equation (10).

![Figure 2.](https://cdn.elifesciences.org/articles/28295/elife-28295-fig2-v2.jpg)

**Figure 2.:** (A-C) Control input, output, and error are plotted versus time, before the start of learning; in the first 4 s and last 4 s of learning; and during testing without error feedback (demarcated by the vertical red lines). Weight updating and error current feedback were both turned on after the vertical red line on the left at the start of learning, and turned off after the vertical red line in the middle at the end of learning. (A) Second component of the input $u_{2}$. (B) Second component of the learned dynamical variable $x^_{2}$ (red) decoded from the network, and the reference $x_{2}$ (blue). After the feedback was turned on, the output tracked the reference. The output continued to track the reference approximately, even after the end of the learning phase, when feedback and learning were turned off. The output tracked the reference approximately, even with a very different input (Bii). With higher firing rates, the tracking without feedback improved (Figure 2—figure supplement 1). (C) Second component of the error $ϵ_{2}=x_{2}-x^_{2}$ between the reference and the output. (Cii) Trajectory $(x_{1}⁢(t),x_{2}⁢(t))$ in the phase plane for reference (red,magenta) and prediction (blue,cyan) during two different intervals as indicated by $⋆$ and $⋄$ in Bii. (D) Mean squared error per dimension averaged over 4 s blocks, on a log scale, during learning with feedback on. Learning rate was increased by a factor of 20 after 1,000 s to speed up learning (as seen by the sharp drop in error at 1000 s). (E) Histogram of firing rates of neurons in the recurrent network averaged over 0.25 s (interval marked in green in H) when output was fairly constant (mean across neurons was 12.4 Hz). (F) As in E, but averaged over 16 s (mean across neurons was 12.9 Hz). (G) Histogram of weights after learning. A few strong weights $|w_{i⁢j}|>10$ are out of bounds and not shown here. (H) Spike trains of 50 randomly-chosen neurons in the recurrent network (alternating colors for guidance of eye only). (I) Spike trains of H, reverse-sorted by first spike time after 0.5 s, with output component $x^_{2}$ overlaid for timing comparison.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/28295/elife-28295-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Layout and legend of panels A-I are analogous to Figure 2A–I, except that maximum firing rates of neurons were larger (Figure 1—figure supplement 1) yielding approximately seven times the mean firing rates (for panels E and F, mean over 0.25 s and 16 s was 86.6 Hz and 87.6 Hz respectively), but approximately one-eighth the learning time, with constant learning rate.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/28295/elife-28295-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** Layout and legend of panels (A-D) are analogous to Figure 2A–D, the green arrow in panel Cii shows the start of the trajectory of Bii. (E) A few randomly selected weights are shown evolving during learning. (F) Histogram of weights after learning. A few strong weights $|w_{i⁢j}|>6$ are out of bounds and not shown here (cf. panel E).

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/28295/elife-28295-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** (A-B) The readout weights were learned with a perceptron learning rule with the recurrent weights (A) as is after FOLLOW learning, or (B) shuffled after FOLLOW learning. A component of the output of the original FOLLOW-learned network (blue) and of the output of the network whose readout weights were trained (red) are plotted after the readout weights were trained for approximately 1,000 s. The readout weights learned if the recurrent weights were kept as is, but not if shuffled. Readout weights could also not be learned after shuffling only feedforward, and shuffling both feedforward and recurrent connections.

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/28295/elife-28295-fig2-figsupp4-v2.jpg)

**Figure 2—figure supplement 4.:** Panels A-F are interpreted similar to Figure 2—figure supplement 2A–F, except in panel A, along with the input $u_{2}⁢(t)$ (blue) to layer 1, the required non-linear transform $g_{2}⁢(u→⁢(t))/20$ is also plotted (cyan); and in panels E and F, the evolution and histogram of weights are those of the feedforward weights, that perform the non-linear transform on the input.

![Figure 2—figure supplement 5.](https://cdn.elifesciences.org/articles/28295/elife-28295-fig2-figsupp5-v2.jpg)

**Figure 2—figure supplement 5.:** The linear decaying oscillators system was learned for 10,000 s with either a non-linear or a linear feedforward transform. (A) The learned feedforward weights $w_{i⁢l}^{ff}$ were plotted for the system with the non-linear feedforward transform, versus the corresponding feedforward weights for the system with the linear feedforward transform. The feedforward weights for the two systems do not fit the identity line (coefficient of determination $R^{2}$ is negative; $R^{2}$ is not the square of a number and can be negative) showing that the learned feedforward transform is different in the two systems as expected. (B) Same as A, but for the recurrent weights in the two systems. The weights fit the identity line with an $R^{2}$ close to one showing that the learned recurrent transform is similar in the two systems as expected. Some weights fall outside the plot limits.

![Figure 3.](https://cdn.elifesciences.org/articles/28295/elife-28295-fig3-v2.jpg)

**Figure 3.:** Layout and legend of panels (A-C) are analogous to Figure 2A–C. (D) The trajectories of the reference (left panel) and the learned network (right panel) are shown in state space for 40 s with zero input during the testing phase, forming the well-known Lorenz attractor. (E) Tent map, that is local maximum of the third component of the reference signal (blue)/network output (red) is plotted versus the previous local maximum, for 800 s of testing with zero input. The reference is plotted with filtering in panels (A-C), but unfiltered for the strange attractor (panel D left) and the tent map (panel E blue).

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/28295/elife-28295-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** Panels A-E are interpreted similar to Figure 3A–E, except that the reference signal was not filtered in computing the error. Without filtering, the tent map for the network output (panel E red) shows a doubling, but the mismatch for large maxima is reduced, compared to with filtering in Figure 3.

![Figure 4.](https://cdn.elifesciences.org/articles/28295/elife-28295-fig4-v2.jpg)

**Figure 4.:** Layout and legend of panels A-C are analogous to Figure 2A–C except that: in panel (A), the control input (torque) on the elbow joint is plotted; in panel (B), reference and decoded angle $\theta_{2},\theta^_{2}$ (solid) and angular velocity $\omega_{2},\omega^_{2}$ (dotted) are plotted, for the elbow joint; in panel (C), the error $\theta_{2}-\theta^_{2}$ in the elbow angle is plotted. (Aii-Cii) The control input was chosen to perform a swinging acrobot-like task by applying small torque only on the elbow joint. (Cii) The shoulder angle $\theta_{1}⁢(t)$ is plotted versus the elbow angle $\theta_{2}⁢(t)$ for the reference (blue) and the network (red) for the full duration in Aii-Bii. The green arrow shows the starting direction. (D) Reaching task. Snapshots of the configuration of the arm, reference in blue (top panels) and network in red (bottom panels) subject to torques in the directions shown by the circular arrows. After 0.6 s, the tip of the forearm reaches the cyan target. Gravity acts downwards in the direction of the arrow. (E) Acrobot-inspired swinging task (visualization of panels of Aii-Cii). Analogous to D, except that the torque is applied only at the elbow. To reach the target, the arm swings forward, back, and forward again.

During learning, the mean squared error, where the mean was taken over the number of dynamical dimensions $N_{d}$ and over a duration of a few seconds, decreased (Figure 2D). We stopped the learning phase that is weight updating, when the mean squared error approximately plateaued as a function of learning time (Figure 2D). At the end of the learning phase, we switched the error feedback off (‘open loop’) and provided different test inputs to both the reference system and the recurrent spiking network. A successful forward predictive model should be able to predict the state variables in the open-loop model over a finite time horizon (corresponding to the planning horizon of a short action sequence) and in the closed-loop mode (with error feedback) without time limit.

#### Non-linear oscillator

Our FOLLOW learning scheme enabled a network with 3000 neurons in the recurrent network and 3000 neurons in the motor command representation layer to approximate the non-linear 2-dimensional van der Pol oscillator (Figure 2). We used a superposition of random steps as input, with amplitudes drawn uniformly from an interval, changing on two time scales, 50 ms and 4 s (see Materials and methods).

During the four seconds before learning started, we blocked error feedback. Because of zero error feedback and our initialization with zero feedforward and recurrent weights, the output $x^$ decoded from the network of spiking neurons remained constant at zero while the reference system performed the desired oscillations. Once the error feedback with large gain ($k=10$) was turned on, the feedback forced the network to roughly follow the reference. Thus, with feedback, the error dropped to a very low value, immediately after the start of learning (Figure 2B,C). During learning, the error dropped even further over time (Figure 2D). After having stopped learning at 5000 s ($∼$2 hr), we found the weight distribution to be uni-modal with a few very large weights (Figure 2G). In the open-loop testing phase without error feedback, a sharp square pulse as initial input on different 4 s long pedestal values caused the network to track the reference as shown in Figure 2Aii–Cii panels. For some values of the constant pedestal input, the phase of the output of the recurrent network differed from that of the reference (Figure 2Bii), but the shape of the non-linear oscillation was well predicted as indicated by the similarity of the trajectories in state space (Figure 2Cii).

The spiking pattern of neurons of the recurrent network changed as a function of time, with inter-spike intervals of individual neurons correlated with the output, and varying over time (Figure 2H,I). The distributions of firing rates averaged over a 0.25 s period with fairly constant output, and over a 16 s period with time-varying output, were long-tailed, with the mean across neurons maintained at approximately 12–13 Hz (Figure 2E,F). The distribution averaged over 16 s had a smaller number of neurons firing at very low and very high rates compared to the distribution over 0.25 s, consistent with the expectation that the identity of low-rate and high-rate neurons changed over time for time-varying output (Figure 2E,F). We repeated this example experiment (‘van der Pol oscillator’) with a network of equal size but with neurons that had higher firing rates, so that some neurons could reach a maximal rate of 400 Hz (Figure 1—figure supplement 1). The reference was approximated better and learning time was shorter with higher rates (Figure 2—figure supplement 1 – 10,000 s with constant learning rate) compared to the low rates here (Figure 2 – 5,000 s with 20 times the learning rate after 1,000 s). Hence, for all further simulations, we set neuronal parameters to enable peak firing rates up to 400 Hz (Figure 1—figure supplement 1B).

![Figure 5.](https://cdn.elifesciences.org/articles/28295/elife-28295-fig5-v2.jpg)

**Figure 5.:** (A) We ran our FOLLOW scheme on a network for learning one of two different implementations of the reference van der Pol oscillator: (1) differential equations, versus (2) a network realized using FOLLOW learning for 10,000 s ($∼$3 hr). We plot the evolution of the mean squared error, mean over number of dimensions $N_{d}$ and over 4 s time blocks, from the start to 100,000 s of learning, with the weights starting from zero. Mean squared error for the differential equations reference (1) is shown in black, while that for the realizable network reference (2) is in red. (B) The feedforward weights (top panel) and the recurrent weights (bottom panel) at the end of 100,000 s ($∼$28 hr) of learning, are plotted versus the corresponding weights of the realizable target network. The coefficient of determination i.e the $R^{2}$ value of the fit to the identity line ($y=x$) is also displayed for each panel. A value of $R^{2}=1$ denotes perfect equality of weights to those of the realizable network. Some weights fall outside the plot limits. (C) After 0 s, 10,000 s ($∼$3 hr), and 100,000 s ($∼$28 hr) of the learning protocol against the realizable network as reference, we show spike trains of a few neurons in the recurrent network (red) and the reference network (blue) in the top, middle and bottom panels respectively, from test simulations while providing the same control input and keeping error feedback on. With error feedback off, the low-dimensional output diverged slightly from the reference, hence the spike trains did too (not shown).

We also asked whether merely the distribution of the learned weights in the recurrent layer was sufficient to perform the task, or whether the specific learned weight matrix was required. This question was inspired from reservoir computing (Jaeger, 2001; Maass et al., 2002; Legenstein et al., 2003; Maass and Markram, 2004; Jaeger and Haas, 2004; Joshi and Maass, 2005; Legenstein and Maass, 2007), where the recurrent weights are random, and only the readout weights are learned. To answer this question, we implemented a perceptron learning rule on the readout weights initialized at zero, with the learned network’s output as the target, after setting the feedforward and/or recurrent weights to either the learned weights as is or after shuffling them. The readout weights could be approximately learned only for the network having the learned weights and not the shuffled ones (Figure 2—figure supplement 3), supporting the view that the network does not behave like a reservoir (Materials and methods).

#### Chaotic lorenz system

Our FOLLOW scheme also enabled a network with 5000 neurons each in the command representation layer and recurrent network, to learn the 3-dimensional non-linear chaotic Lorenz system (Figure 3). We considered a paradigm where the command input remained zero so that the network had to learn the autonomous dynamics characterized in chaos theory as a ’strange attractor’ (Lorenz, 1963). During the testing phase without error feedback minor differences led to different trajectories of the network and the reference which show up as large fluctuations of $ϵ_{3}⁢(t)$ (Figure 3A–C). Such a behaviour is to be expected for a chaotic system where small changes in initial condition can lead to large changes in the trajectory. Importantly, however, the activity of the spiking network exhibits qualitatively the same underlying strange attractor dynamics, as seen from the butterfly shape (Lorenz, 1963) of the attractor in configuration space, and the tent map (Lorenz, 1963) of successive maxima versus the previous maxima (Figure 3D,E). The tent map generated from our network dynamics (Figure 3E) has lower values for the larger maxima compared to the reference tent map. However, very large outliers like those seen in a network trained by FORCE (Thalmeier et al., 2016) are absent. Since we expected that the observed differences are due to the filtering of the reference by an exponentially-decaying filter, we repeated learning without filtering the Lorenz reference signal (Figure 3—figure supplement 1), and found that the mismatch for large maxima reduced, but a doubling appeared in the tent map (Figure 3—figure supplement 1E) which had been almost imperceptible with filtering (cf. Figure 3E).

### FOLLOW enables learning a two-link planar arm model under gravity

To turn to a task closer to real life, we next wondered if a spiking network can also learn the dynamics of a two-link arm via the FOLLOW scheme. We used a two-link arm model adapted from (Li, 2006) as our reference. The two links in the model correspond to the upper and fore arm, with the elbow joint in between and the shoulder joint at the top. The arm moved in the vertical plane under gravity, while torques were applied directly at the two joints, so as to coarsely mimic the action of muscles. To avoid full rotations, the two joints were constrained to vary in the range from $-90^{∘}$ to $+90^{∘}$ where the resting state is at $0^{∘}$ (see Materials and methods).

The dynamical system representing the arm is four-dimensional with the state variables being the two joint angles and two angular velocities. The network must integrate the torques to obtain the angular velocities which in turn must be integrated for the angles. Learning these dynamics is difficult due to these sequential integrations involving non-linear functions of the state variables and the input. Still, our feedforward and recurrent network architecture (Figure 1B) with 5000 neurons in each layer was able to approximate these dynamics.

Similar to the previous examples, random input torque with amplitudes of short and long pulses changing each 50 ms and 1 s, respectively, was provided to each joint during the learning phase. The input was linearly interpolated between consecutive values drawn every 50 ms. In the closed loop scenario with error feedback, the trajectory converged rapidly to the target trajectory (Figure 4). We found that the FOLLOW scheme learned to reproduce the arm dynamics even without error feedback for a few seconds during the test phase (Figure 4 and Video 1 and Video 2), which corresponds to the time horizon needed for the planning of short arm movements.

![Video 1.](https://cdn.elifesciences.org/articles/28295/elife-28295-video1.mp4.jpg)

**Video 1.:** After training the network as a forward model of the two-link arm under gravity as in Figure 4, we tested the network without feedback on a reaching task. Command input was provided to both joints of the two-link reference arm so that the tip reached the cyan square. The same command input was also provided to the network without error feedback. The state (blue, left) of the reference arm and the state predicted (red, right) by the learned network without error feedback are animated as a function of time. The directions of the circular arrows indicate the directions of the command torques at the joints. The animation is slowed $5\times$ compared to real life.

![Video 2.](https://cdn.elifesciences.org/articles/28295/elife-28295-video2.mp4.jpg)

**Video 2.:** After training the network as a forward model of the two-link arm under gravity as in Figure 4, we tested the network without feedback on a swinging task analogous to an acrobot. Command input was provided to the elbow joint of the two-link reference arm so that the tip reached the cyan square by swinging. The same command input was also provided to the network without error feedback. The state (blue, left) of the reference arm and the state predicted (red, right) by the learned network without error feedback are animated as a function of time. The directions of the circular arrows indicate the directions of the command torques at the joints. The animation is slowed $5\times$ compared to real life.

To assess the generalization capacity of the network, we fixed the parameters post learning, and tested the network in the open-loop setting on a reaching task and an acrobot-inspired swinging task (Sutton, 1996). In the reaching task, torque was provided to both joints to enable the arm-tip to reach beyond a specific $(x,y)$ position from rest. The arm dynamics of the reference model and the network are illustrated in Figure 4D and animated in Video 1. We also tested the learned network model of the 2-link arm on an acrobot-like task that is a gymnast swinging on a high-bar (Sutton, 1996), with the shoulder joint analogous to the hands on the bar, and the elbow joint to the hips. The gymnast can only apply small torques at the hip and none at the hands, and must reach beyond a specified $(x,y)$ position by swinging. Thus, during the test, we provided input only at the elbow joint, with a time course that could make the reference reach beyond the target $(x,y)$ position from rest by swinging. The control input and the dynamics (Figure 4A–C right panels, Figure 4E and Video 2) show that the network can perform the task in open-loop condition suggesting that it has learned the inertial properties of the arm model, necessary for this simplified acrobot task.

### Feedback in the FOLLOW scheme entrains spike timings

In Methods, we show that the FOLLOW learning scheme is Lyapunov stable and that the error tends to zero under certain reasonable assumptions and approximations. Two important assumptions of the proof are that the weights remain bounded and that the desired dynamics are realizable by the network architecture, that is there exist feedforward and recurrent weights that enable the network to mimic the reference dynamics perfectly. However, in practice the realizability is limited by at least two constraints. First, even in networks of $N$ rate neurons with non-linear tuning curves, the non-linear function $h→$ of the reference system in Equation (1) can in general only be approximated with a finite error (Funahashi, 1989; Girosi and Poggio, 1990; Hornik et al., 1989; Sanner and Slotine, 1992; Eliasmith and Anderson, 2004) which can be interpreted as a form of frozen noise, i.e. even with the best possible setting of the weights, the network predicts, for most values of the state variables, a next state which is slightly different than the one generated by the reference differential equation. Second, since we work with spiking neurons, we expect on top of this frozen noise the effect of shot noise caused by pseudo-random spiking. Both noise sources may potentially cause drift of the weights (Narendra and Annaswamy, 1989; Ioannou and Sun, 2012) which in turn can make the weights grow beyond any reasonable bound. Ameliorative techniques from adaptive control are discussed in Appendix 1. In our simulations, we did not find any effect of drift of weights on the error during a learning time up to 100,000 s (Figure 5A), 10 times longer than that required for learning this example (Figure 2—figure supplement 1).

To highlight the difference between a realizable reference system and non-linear differential equations as a reference system, we used, in an additional simulation experiment, a spiking network with fixed weights as the reference. More precisely, instead of using directly the differential equations of the van der Pol oscillator as a reference, we now used as a reference a spiking approximation of the van der Pol oscillator, i.e. the spiking network that was the final result after 10,000 s ($∼$3 hr) of FOLLOW learning in Figure 2—figure supplement 1. For both the spiking reference network and the to-be-trained learning network we used the same architecture, the same number of neurons, and the same neuronal parameters as in Figure 2—figure supplement 1 for the learning of the van der Pol oscillator. The readout and feedback weights of the learning network also had the same parameters as those of the spiking reference network, but the feedforward and recurrent weights of the learning network were initialized to zero and updated, during the learning phase, with the FOLLOW rule. We ran FOLLOW learning against the reference network for 100,000 s ($∼$28 hr) (Figure 5). With the realizable network as reference, learning was more rapid than with the original van der Pol oscillator as reference (Figure 5A).

We emphasize that, analogous to the earlier simulations, the feedback error $ϵ_{\alpha}$ was low-dimensional and calculated from the decoded outputs. Nevertheless, the low-dimensional error feedback was able to entrain the network spike times to the reference spike times (Figure 5C). In particular, a few neurons learned to fire only two or three spikes at very precise moments in time. For example, after learning, the spikes of neuron $i=9$ in the learning network were tightly aligned with the spike times of the neuron with the same index $i$ in the spiking reference network. Similarly, neuron $i=8$ that was inactive at the beginning of learning was found to be active, and aligned with the spikes of the reference network, after 100,000 s ($∼$28 hr) of learning. The spike trains were entrained by the low-dimensional feedback. With the feedback off, even the low-dimensional output, and hence the spike trains, diverged from the reference. It will be interesting to explore if this entrainment by low-dimensional feedback via an auto-encoder loop can be useful in supervised spike train learning (Gütig and Sompolinsky, 2006; Pfister et al., 2006; Florian, 2012; Mohemmed et al., 2012; Gütig, 2014; Memmesheimer et al., 2014; Gardner and Grüning, 2016).

Our results with the spiking reference network suggest that the error is reduced to a value close to zero for a realizable or closely-approximated system (Figure 5A) as shown in Methods, analogous to proofs in adaptive control (Ioannou and Sun, 2012; Narendra and Annaswamy, 1989). Moreover, network weights became very similar, though not completely identical, to the weights of the realizable reference network (Figure 5B), which suggests that the theorem for convergence of parameters from adaptive control should carry over to our learning scheme.

### Learning is robust to sparse connectivity, noisy error or reference, and noisy decoding weights, but not to delays

So far, our spiking networks had all-to-all connectivity. We next tested whether sparse connectivity (Markram et al., 2015; Brown and Hestrin, 2009) of the feedforward and recurrent connections was sufficient for learning low-dimensional dynamics. We ran the van der Pol oscillator learning protocol with the connectivity varying from 0.1 (10 percent connectivity) to 1 (full connectivity). Connections that were absent after the sparse initialization could not appear during learning, while the existing sparse connections were allowed to evolve according to FOLLOW learning. As shown in Figure 6A, we found that learning was slower with sparser connectivity; but with twice the learning time, a sparse network with about 25% connectivity reached similar performance as the fully connected network with standard learning time.

![Figure 6.](https://cdn.elifesciences.org/articles/28295/elife-28295-fig6-v2.jpg)

**Figure 6.:** We ran the van der Pol oscillator (A–D) or the linear decaying oscillator (F,H) learning protocol for 10,000 s for different parameter values and measured the mean squared error, over the last 400 s before the end of learning, mean over number of dimensions $N_{d}$ and time. (A) We evolved only a fraction of the feedforward and recurrent connections, randomly chosen as per a specific connectivity, according to FOLLOW learning, while keeping the rest zero. The round dots show the mean squared error for different connectivity after a 10,000 s learning protocol (default connectivity = 1 is starred); while the square dots show the same after a 20,000 s protocol. (B) Mean squared error after 10,000 s of learning versus the standard deviation of noise added to each component of the error, or equivalently to each component of the reference, is plotted. (C) We multiplied the original decoding weights (that form an auto-encoder with the error encoders) by a random factor (1 + uniform$(-χ,χ)$) drawn for each weight. The mean squared error at the end of a 10,000 s learning protocol for increasing values of $χ$ is plotted (default $χ=0$ is starred). (D) We multiplied the original decoding weights by a random factor (1 + uniform$(-χ+ξ,χ+ξ)$), fixing $χ=2$, drawn independently for each weight. The mean squared error at the end of a 10,000 s learning protocol, for a few values of $ξ$ on either side of zero, is plotted. (E,G) Architectures for learning the forward model when the reference $x⁢(t)$ is available after a sensory feedback delay $Δ$ for computing the error feedback. The forward model may be trained without a compensatory delay in the motor command path (E) or with it (G). (F,H) Mean squared error after 10,000 s of learning the linear decaying oscillator is plotted (default values are starred) versus the sensory feedback delay $Δ$ in the reference, for the architectures without and with compensatory delay, in F and H respectively.

We added Gaussian white noise to each component of the error, which is equivalent to adding it to each component of the reference, and ran the van der Pol oscillator learning protocol for 10,000 s for different standard deviations of the noise (Figure 6B). The learning was robust to noise with standard deviation up to around $0.001$, which must be compared with the error amplitude of the order of $0.1$ at the start of learning, and orders of magnitude lower later.

The readout weights have been pre-learned until now, so that, in the absence of recurrent connections, error feedback weights and decoding weights formed an auto-encoder. We sought to relax this requirement. Simulations showed that with completely random readout weights, the system did not learn to reproduce the target dynamical system. However, if the readout weights had some overlap with the auto-encoder, learning was still possible (Figure 6C). If for a feedback error $ϵ→$, the error encoding followed by output decoding yields $k⁢(1+ξ)⁢ϵ→+n→⁢(ϵ→)$, where $n→$ is a vector of arbitrary functions not having linear terms and small in magnitude compared to the first term, and $ξ$ is sufficiently greater than $-1$ so that the effective gain $k⁢(1+ξ)$ remains large enough, then the term that is linear in error can still drive the output close to the desired one (see Materials and methods).

To check this intuition in simulations, we incorporated multiplicative noise on the decoders by multiplying each decoding weight of the auto-encoder by one plus $\gamma$, where for each weight $\gamma$ was drawn independently from a uniform distribution between $-χ+ξ$ and $χ+ξ$. We found that the system was still able to learn the van der Pol oscillator up to $χ∼5$ and $ξ=0$, or $χ=2$ and $ξ$ variable (Figure 6B,C). Negative values of $ξ$ result in a lower overlap with the auto-encoder leading to the asymmetry seen in Figure 6C. Thus, the FOLLOW learning scheme is robust to multiplicative noise on the decoding weights. Alternative approaches for other noise models are discussed in Appendix 1.

We also asked if the network could handle sensory feedback delays in the reference signal. Due to the strong limit cycle attractor of the van der Pol oscillator, the effect of delay is less transparent than for the linear decaying oscillator (Figure 2—figure supplement 2), so we decided to focus on the latter. For the linear decaying oscillator, we found that learning degraded rapidly with a few milliseconds of delay in the reference, that is if $x→⁢(t-Δ)$ was provided as reference instead of $x→⁢(t)$ (Figure 6E–F). We compensated for the sensory feedback delay by delaying the motor command input by identical $Δ$ (Figure 6G), which is equivalent to time-translating the complete learning protocol, to which the learning is invariant, and thus the network would learn for arbitrary delay (Figure 6H). In the Discussion, we suggest how a forward model learned with a compensatory delay (Figure 6G) could be used in control mode to compensate for sensory feedback delays.

## Discussion

The FOLLOW learning scheme enables a spiking neural network to function as a forward predictive model that mimics a non-linear dynamical system activated by one or several time-varying inputs. The learning rule is supervised, local, and comes with a proof of stability.

It is supervised because the FOLLOW learning scheme uses error feedback where the error is defined as the difference between predicted output and the actual observed output. Error feedback forces the output of the system to mimic the reference, an effect that is widely used in adaptive control theory (Narendra and Annaswamy, 1989; Ioannou and Sun, 2012).

The learning rule is local in the sense that it combines information about presynaptic spike arrival with an abstract quantity that we imagine to be available in the postsynaptic neuron. In contrast to standard Hebbian learning, the variable representing this postsynaptic quantity is not the postsynaptic firing rate, spike time, or postsynaptic membrane potential, but the error current projected by feedback connections onto the postsynaptic neuron, similar in spirit to modern biological implementations of approximated backpropagation (Roelfsema and van Ooyen, 2005), (Lillicrap et al., 2016) or local versions of FORCE (Sussillo and Abbott, 2009) learning rules. We emphasize that the postsynaptic quantity is different from the postsynaptic membrane potential or the total postsynaptic current which would also include input from feedforward and recurrent connections.

A possible implementation in a spatially extended neuron would be to imagine that the postsynaptic error current $I_{i}^{ϵ}$ arrives in the apical dendrite where it stimulates messenger molecules that quickly diffuse or are actively transported into the soma and basal dendrites where synapses from feedfoward and feedback input could be located, as depicted in Figure 7A. Consistent with the picture of a messenger molecule, we low-pass filtered the error current with an exponential filter $κ^{ϵ}$ of time constant 80 ms or 200 ms, much longer than the synaptic time constant of 20 ms of the filter $κ$. Simultaneously, filtered information about presynaptic spike arrival $S_{j}*κ$ is available at each synapse, possibly in the form of glutamate bound to the postsynaptic receptor or by calcium triggered signalling chains localized in the postsynaptic spines. Thus the combination of effects caused by presynaptic spike arrival and error information available in the postsynaptic cell drives weight changes, in loose analogy to standard Hebbian learning.

![Figure 7.](https://cdn.elifesciences.org/articles/28295/elife-28295-fig7-v2.jpg)

**Figure 7.:** (A) A cartoon depiction of feedforward, recurrent and error currents entering a neuron $i$ in the recurrent network. The error current enters the apical dendrite and triggers an intra-cellular chemical cascade generating a signal that is available at the feedforward and recurrent synapses in the soma and basal dendrites, for weight updates. The error current must trigger a cascade isolated from the other currents, here achieved by spatial separation. (B-C) An architecture based on the Smith predictor, that can switch between learning the forward model (B), versus using the forward model for motor control (C, adapted from (Wolpert and Miall, 1996)), to compensate for the delay in sensory feedback. Active pathways are in blue and inactive ones are in red. (B) The learning architecture (blue) is identical to Figure 6G, but embedded within a larger control loop (red). During learning, when error feedback gain $k≫1$, the motor command is fed in with a compensatory delay identical to the sensory feedback delay. Thus motor command and reference state are equally delayed, hence temporally matched, and the forward model learns to produce the motor system output for given input. (C) Once the forward model is learned, the system switches to motor control mode (feedback gain $k=0$). In this mode, the forward model receives the present motor command and predicts the current state of the motor system, for rapid feedback to the controller (via loop indicated by thick lines), even before the delayed sensory feedback arrives. Of course the delayed sensory feedback can be further taken into account by the controller, by comparing it with the delayed output of the forward model, to better estimate the true state. Thus the forward model learned as in B provides a prediction of the state, even before feedback is received, acting to compensate for sensory feedback delays in motor control.

The separation of the error current from the currents at feedforward or recurrent synapses could be spatial (such as suggested in Figure 7A) or chemical if the error current projects onto synapses that trigger a signalling cascade that is different from that at other synapses. Importantly, whether it is a spatial or chemical separation, the signals triggered by the error currents need to be available throughout the postsynaptic neuron. This leads us to a prediction regarding synaptic plasticity that, say in cortical pyramidal neurons, the plasticity of synapses that are driven by pre-synaptic input in the basal dendrites, should be modulated by currents injected in the apical dendrite or on stimulation of feedback connections.

The learning scheme is provenly stable with errors converging asymptotically to zero under a few reasonable assumptions (Methods). The first assumption is that error encoding feedback weights and output decoding readout weights form an auto-encoder. This requirement can be met if, at an early developmental stage, either both sets of weights are learned using say mirrored STDP (Burbank, 2015), or the output readout weights are learned, starting with random encoding weights, via a biological perceptron-like learning rule (D'Souza et al., 2010; Urbanczik and Senn, 2014). A pre-learned auto-encoder in a high-gain negative feedback loop is in fact a specific prediction of our learning scheme, to be tested in systems-level experiments. The second assumption is that the reference dynamics $f⁢(x→)$ is realizable. This requirement can be approximately met by having a recurrent network with a large number $N$ of neurons with different parameters (Eliasmith and Anderson, 2004). The third assumption is that the state variables $x→⁢(t)$ are observable. While currently we calculate the feedback error directly from the state variables as a difference between reference and predicted state, we could soften this condition and calculate the difference in a higher-dimensional space with variables $y→⁢(t)$ as long as $y→=K⁢(x→)$ is an invertible function of $x→⁢(t)$ (Appendix 1). The fourth assumption is that the system dynamics be slower than synaptic dynamics. Indeed, typical reaching movements extend over hundreds of milliseconds or a few seconds whereas neuronal spike transmission delays and synaptic time constants can be as short as a few milliseconds. In our simulations, neuronal and synaptic time constants were set to 20 ms, yet the network dynamics evolved on the time scale of hundreds of milliseconds or a few seconds, even in the open-loop condition when error feedback was switched off (Figures 2 and 4). The fifth assumption is that weights stay bounded. Indeed, in biology, synaptic weights should not grow indefinitely. Algorithmically, a weight decay term in the learning rule can suppress the growth of large weights (see also Appendix 1), though we did not need to implement a weight decay term in our simulations.

One of the postulated uses of the forward predictive model is to compensate for delay in the sensory feedback during motor control (Wolpert and Miall, 1996; Wolpert et al., 1995) using the Smith predictor configuration (Smith, 1957). We speculate that the switch from the closed-loop learning of forward model with feedback gain $k≫1$ to open-loop motor prediction $k=0$ could also be used to switch delay lines: the system can have either a delay before the forward model as required for learning (Figure 7B), or after the forward model as required for the Smith predictor (Figure 7C). We envisage that FOLLOW learning of the forward model occurs in closed loop mode ($k≫1$) with a delay in the motor command path, as outlined earlier in Figure 6G and now embedded in the Smith predictor architecture in Figure 7B. After learning, the network is switched to motor control mode, with the forward predictive model in open loop ($k=0$), implementing the Smith predictor (Figure 7C). In this motor control mode, the motor command is fed with zero delay to the forward model. This enables to rapidly feed the estimated state back to the motor controller so as to take corrective actions, even before sensory feedback arrives. In parallel, available sensory feedback is compared with a copy of the forward model that has passed through a compensatory delay after the forward model (Figure 7C).

Simulations with the FOLLOW learning scheme have demonstrated that strongly non-linear dynamics can be learned in a recurrent spiking neural network using a local online learning rule that does not require rapid weight changes. Previous work has mainly focused on a limited subset of these aspects. For example, Eliasmith and colleagues used a local learning rule derived from stochastic gradient descent, in a network structure comprising heterogeneous spiking neurons with error feedback (MacNeil and Eliasmith, 2011), but did not demonstrate learning non-linear dynamics (Appendix 1). Denève and colleagues used error feedback in a homogeneous spiking network with a rule similar to ours, for linear dynamics only (Bourdoukan and Denève, 2015), and while this article was in review, also for non-linear dynamics (Alemi et al., 2017), but their network requires instantaneous lateral interactions and in the latter case, also non-linear dendrites.

Reservoir computing models exploit recurrent networks of non-linear units in an activity regime close to chaos where temporal dynamics is rich (Jaeger, 2001; Maass et al., 2002; Legenstein et al., 2003; Maass and Markram, 2004; Jaeger and Haas, 2004; Joshi and Maass, 2005; Legenstein and Maass, 2007). While typical applications of reservoir computing are concerned with tasks involving a small set of desired output trajectories (such as switches or oscillators), our FOLLOW learning enables a recurrent network with a single set of parameters to mimic a dynamical system over a broad range of time-dependent inputs with a large family of different trajectories in the output.

Whereas initial versions of reservoir computing focused on learning the readout weights, applications of FORCE learning to recurrent networks of rate units made it possible to also learn the recurrent weights (Sussillo and Abbott, 2009, 2012). However, in the case of a multi-dimensional target, multi-dimensional errors were typically fed to distinct parts of the network, as opposed to the distributed encoding used in our network. Moreover, the time scale of synaptic plasticity in FORCE learning is faster than the time scale of the dynamical system which is unlikely to be consistent with biology. Modern applications of FORCE learning to spiking networks (DePasquale et al., 2016; Thalmeier et al., 2016; Nicola and Clopath, 2016) inherit these issues.

Adaptive control of non-linear systems using continuous rate neurons (Sanner and Slotine, 1992; Weiping Li et al., 1987; Slotine and Coetsee, 1986) or spiking neurons (DeWolf et al., 2016) has primarily focused on learning parameters in adaptive feedback paths, rather than learning weights in a recurrent network, using learning rules involving quantities that do not appear in the pre- or post-synaptic neurons, making them difficult to interpret as local to synapses. Recurrent networks of rate units have occasionally been used for control (Zerkaoui et al., 2009), but trained either via real-time recurrent learning or the extended Kalman filter which are non-local in space, or via backpropagation through time which is offline (Pearlmutter, 1995). Recent studies have used neural network techniques to train inverse models by motor babbling, to describe behavioral data in humans (Berniker and Kording, 2015) and song birds (Hanuschkin et al., 2013), albeit with abstract networks. Optimal control methods (Hennequin et al., 2014) or stochastic gradient descent (Song et al., 2016) have also been applied in recurrent networks of neurons, but with limited biological plausibility of the published learning rules. As an alternative to supervised schemes, biologically plausible forms of reward-modulated Hebbian rules on the output weights of a reservoir have been used to learn periodic pattern generation and abstract computations (Hoerzer et al., 2014; Legenstein et al., 2010), but how such modulated Hebbian rules could be used in predicting non-linear dynamics given time-dependent control input remains open.

Additional features of the FOLLOW learning scheme are that it does not require full connectivity but also works with biologically more plausible sparse connectivity; and it is robust to multiplicative noise in the output decoders, analogous to recent results on approximate error backpropagation in artificial neural networks (Lillicrap et al., 2016). Since the low-dimensional output and all neural currents are spatially averaged over a large number of synaptically-filtered spike trains, neurons in the FOLLOW network do not necessarily need to fire at rates higher than the inverse of the synaptic time scale. In conclusion, we used a network of heterogeneous neurons as in the Neural Engineering Framework (Eliasmith and Anderson, 2004), employed a pre-learned auto-encoder to enable negative feedback of error as in adaptive control theory (Morse, 1980; Narendra et al., 1980; Slotine and Coetsee, 1986; Weiping Li et al., 1987; Narendra and Annaswamy, 1989; Sastry and Bodson, 1989; Ioannou and Sun, 2012), and derived and demonstrated a local and online learning rule for recurrent connections that learn to reproduce non-linear dynamics.

Our present implementation of the FOLLOW learning scheme in spiking neurons violates Dale’s law because synapses originating from the same presynaptic neuron can have positive or negative weights, but in a different context extensions incorporating Dale’s law have been suggested (Parisien et al., 2008). Neurons in cortical networks are also seen to maintain a balance of excitatory and inhibitory incoming currents (Denève and Machens, 2016). It would be interesting to investigate a more biologically plausible extension of FOLLOW learning that maintains Dale’s law; works in the regime of excitatory-inhibitory balance, possibly using inhibitory plasticity (Vogels et al., 2011); pre-learns the auto-encoder, potentially via mirrored STDP (Burbank, 2015); and possibly implements spatial separation between different compartments (Urbanczik and Senn, 2014). It would also be interesting for future work to see whether our model of an arm trained on motor babbling with FOLLOW, can explain aspects of human behavior in reaching tasks involving force fields (Shadmehr and Mussa-Ivaldi, 1994), uncertainty (Körding and Wolpert, 2004; Wei and Körding, 2010) or noise (Burge et al., 2008). Further directions worth pursuing include learning multiple different dynamical transforms within one recurrent network, without interference; hierarchical learning with stacked recurrent layers; and learning the inverse model of motor control so as to generate the control input given a desired state trajectory.

## Materials and methods

### Simulation software

All simulation scripts were written in python (https://www.python.org/) for the Nengo simulator (Stewart et al., 2009) (http://www.nengo.ca/, version 2.4.0) with minor custom modifications to support sparse weights. We ran the model using the Nengo GPU back-end (https://github.com/nengo/nengo_ocl) for speed. The script for plotting the figures was written in python using the matplotlib module (http://matplotlib.org/). These simulation and plotting scripts are available online at https://github.com/adityagilra/FOLLOW.

### Network parameters

#### Initialization of plastic weights

The feedforward weights $w_{il}^{ff}$ from the command representation layer to the recurrent network and the recurrent weights $w_{i⁢j}$ inside the network were initialized to zero.

#### Update of plastic weights

With the error feedback loop closed, that is with reference output $x→$ and predicted output $x→^$ connected to the error node, and feedback gain $k=10$, the FOLLOW learning rule, Equation (10), was applied on the feedforward and recurrent weights, $w_{il}^{ff}$ and $w_{i⁢j}$. The error for our learning rule was the error $ϵ_{\alpha}=x_{\alpha}-x^_{\alpha}$ in the observable output $x→$, not the error in the desired function $h→⁢(x→,u→)$ (cf. [Eliasmith, 2005; MacNeil and Eliasmith, 2011], Appendix 1). The observable reference state $x→$ was obtained by integrating the differential equations of the dynamical system. The synaptic time constant $\tau_{s}$ was 20 ms in all synapses, including those for calculating the error and for feeding the error back to the neurons (decaying exponential $κ$ with time constant $\tau_{s}$ in Equation (6)). The error used for the weight update was filtered by a 200 ms decaying exponential ($κ^{ϵ}$ in Equation (10)).

#### Random setting of neuronal parameters and encoding weights

We used leaky integrate-and-fire neurons with a threshold $\theta=1$ and time constant $\tau_{m}=20$ ms. After each spike, the voltage was reset to zero, and the neuron entered an absolute refractory period of $\tau_{r}=2$ ms. When driven by a constant input current $J$, a leaky integrate-and-fire neuron with absolute refractoriness fires at a rate $a=g⁢(J)$ where $g$ is the gain function with value $g⁢(J)=0$ for $J\leq1$ and

$$
g⁢(J)=1/(\tau_{r}+\tau_{m}⁢ln⁡\frac{J}{J-1}),for⁢J>1.
$$

Our network was inhomogeneous in the sense that different neurons had different parameters as described below. The basic idea is that the ensemble of $N$ neurons, with different parameters, forms a rich set of basis functions in the $N_{c}$ or $N_{d}$ dimensional space of inputs or outputs, respectively. This is similar to tiling the space with radial basis functions, except that here we replace the radial functions by the gain functions of the LIF neurons (Equation (11)) each having different parameters (Eliasmith and Anderson, 2004). These parameters were chosen randomly once at the beginning of a simulation and kept fixed during the simulation.

For the command representation layer, we write the current $J$ into neuron $l$, in the case of a constant input $u→$, as

$$
J_{l}^{ff}=ν_{l}^{ff}\sum\betae~_{l\beta}^{ff}u_{\beta}+b_{l}^{ff},with e_{l\beta}^{ff}≡ν_{l}^{ff}e~_{l\beta}^{ff},
$$

where $ν_{l}^{ff}$ and $b_{l}^{ff}$ are neuron-specific gains and biases, and $e~_{l\beta}^{ff}$ are ‘normalized’ encoding weights (cf. Equation (5)).

These random gains, biases and ‘normalized’ encoding weights must be chosen so that the command representation layer adequately represents the command input $u→$, whose norm is bounded in the interval $[0,R_{1}]$ (Table 1). First, we choose the ‘normalized’ encoding weight vectors on a hypersphere of radius $1/R_{1}$, so that the scalar product between the command vector and the vector of ‘normalized’ encoding weights, $\sum\betae~_{l\beta}^{ff}u_{\beta}$, lies in the normalized range $[−1,1]$. Second, the distribution of the gains sets the distribution of the firing rates in a target range. Third, we see from Equation (11) that the neuron starts to fire at the rheobase threshold $J=1$. The biases $b_{l}^{ff}$ randomly shift this rheobase threshold over an interval (see Figure 1—figure supplement 1). For the distributions used to set the fixed random gains and biases, see Table 1.

**Table 1.**
 Network and simulation parameters for example systems.$^{†}$ 4.5 for Figures 1 and 2.* 4e-2 after 1,000 s for Figures 1 and 2. 1e-4 for readout weights in Figure 2—figure supplement 3.$^{‡}$ Nengo v2.4.0 sets the gains and biases indirectly, by default. The projected input at which the neuron just starts firing (i.e. $\sum_{\alpha}e~_{i⁢\alpha}⁢x_{\alpha}=J~_{i}^{0}$) is chosen uniformly from $[-1,1)$, while the firing rate for $\sum_{\alpha}e~_{i⁢\alpha}⁢x_{\alpha}=1$ is chosen uniformly between 200 and 400 Hz. From these, $ν_{i}$ and $b_{i}$ are computed using Equations (11) and (13).


<table>
  <thead>
    <tr>
      <th></th>
      <th>Linear</th>
      <th>Van der pol</th>
      <th>Lorenz</th>
      <th>Arm</th>
      <th>Non-linear feedforward</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Number of neurons/layer</td>
      <td>2000</td>
      <td>3000</td>
      <td>5000</td>
      <td>5000</td>
      <td>2000</td>
    </tr>
    <tr>
      <td>Tp⁢e⁢r⁢i⁢o⁢d (s)</td>
      <td>2</td>
      <td>4</td>
      <td>20</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <td>Representation radius R1</td>
      <td>0.2</td>
      <td>0.2</td>
      <td>6</td>
      <td>0.2</td>
      <td>0.2</td>
    </tr>
    <tr>
      <td>Representation radius R2</td>
      <td>1</td>
      <td>5†</td>
      <td>30</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Gains νi and biases bi for command representation and recurrent layers</td>
      <td>Nengo v2.4.0 default ‡</td>
      <td>Figures 1 and 2: νi=2 and bi chosen uniformly from [-2,1). all other Figures: Nengo v2.4.0 default ‡</td>
      <td>Nengo v2.4.0 default ‡</td>
      <td>Nengo v2.4.0 default ‡</td>
      <td>Nengo v2.4.0 default‡</td>
    </tr>
    <tr>
      <td>Learning pulse ζ1</td>
      <td>R1/6</td>
      <td>R1/6,R1/2</td>
      <td>R2/10</td>
      <td>R2/0.3</td>
      <td>R1/0.6</td>
    </tr>
    <tr>
      <td>Learning pedestal ζ2</td>
      <td>R2/16</td>
      <td>R1/6, R1/2</td>
      <td>0</td>
      <td>R2/0.3</td>
      <td>R2/1.6</td>
    </tr>
    <tr>
      <td>Learning rate</td>
      <td>2e-3</td>
      <td>2e-3*</td>
      <td>2e-3</td>
      <td>2e-3</td>
      <td>2e-3</td>
    </tr>
    <tr>
      <td>Figures</td>
      <td>Figure 2—figure supplement 2</td>
      <td>Figure 1, Figure 2, Figure 2—figure supplement 1, Figure 2—figure supplement 3, Figure 5, Figure 6, Figure 7</td>
      <td>Figure 3, Figure 3—figure supplement 1</td>
      <td>Figure 4</td>
      <td>Figure 2—figure supplement 4, Figure 2—figure supplement 5</td>
    </tr>
  </tbody>
</table>

Analogously, for the recurrent network, we write the current into neuron $i$, for a constant ‘pseudo-input’ vector $x~→$ being represented in the network, as

$$
J_{i}=ν_{i}⁢\sum\alphae~_{i⁢\alpha}⁢x~_{\alpha}+b_{i},with⁢e_{i⁢\alpha}≡ν_{i}⁢e~_{i⁢\alpha},
$$

where $ν_{i}$, $b_{i}$ are neuron-specific gains and biases, and $e~_{i⁢\alpha}$ are ‘normalized’ encoding weights. We call $x~→$ a ‘pseudo-input’ for two reasons. First, the error encoding weights $k⁢e_{i⁢\alpha}$ are used to feed the error $ϵ_{\alpha}=(x_{\alpha}-x^_{\alpha})$ back to neuron $i$ in the network (cf. Equation (6)). However, $ϵ_{\alpha}=x_{\alpha}/(k+1)$, due to the feedback loop according to Equation (9). Thus, the ‘pseudo-input’ $x~→=k⁢x_{\alpha}/(k+1)$ has a similar range as $x→$, whose norm lies in the interval $[0,R_{2}]$ (see Table 1). Second, the neuron also gets feedforward and recurrent input. However, the feedforward and recurrent inputs get automatically adjusted during learning (starting from zero), so their absolute values do not matter for the initialization of parameters that we discuss here. Thus, we choose the ‘normalized’ encoding weight vectors on a hypersphere of radius $1/R_{2}$. For the distributions used to set the fixed random gains and biases, see Table 1.

#### Setting output decoding weights to form an auto-encoder with respect to error encoding weights

The linear readout weights $d_{\alpha⁢i}$ from the recurrently connected network were pre-computed algorithmically so as to form an auto-encoder with the error encoding weights $e_{i⁢\alpha}$ (for $k=1$), while setting the feedforward and recurrent weights to zero ($w_{l\beta}^{ff}=0$ and $w_{ij}=0$). To do this, we randomly selected $P$ error vectors $ϵ→^{(p)}$, that we used as training samples for optimization, with sample index $p=1,…,P$, and having vector components $ϵ_{\alpha}^{(p)}$, $\alpha=1,…,N_{d}$. Since the observable system is $N_{d}$-dimensional, we chose the training samples randomly from within an $N_{d}$-dimensional hypersphere of radius $R_{2}$. We applied each of the error vectors statically as input for the error feedback connections and calculated the activity

$$
a_{i}^{(p)}≡a_{i}(ϵ→^{(p)})=g(\sum\alphae_{i\alpha}ϵ_{\alpha}^{(p)}+b_{i}),
$$

of neuron $i$ for error vector $ϵ→^{(p)}$ using the static rate Equation (11). The decoders $d_{\alpha⁢i}$ acting on these activities should yield back the encoded points thus forming an auto-encoder. A squared-error loss function $ℒ$, with L2 regularization of the decoders,

$$
ℒ=\frac{1}{2}⁢\sumpP\sum\alphaN_{d}(\sumiNd_{\alpha⁢i}⁢a_{i}^{(p)}-ϵ_{\alpha}^{(p)})^{2}+\frac{1}{2}⁢\lambda⁢\sum\alphaN_{d}\sumiNd_{\alpha⁢i}^{2},
$$

setting $\lambda=P⁢(0.1⁢max⁡({a_{i}^{(p)}}))^{2}$ with number of samples $P=N$, was used for this linear regression (default in Nengo v2.4.0) (Eliasmith and Anderson, 2004; Stewart et al., 2009). Biologically plausible learning rules exist for auto-encoders, either by training both encoding and decoding weights (Burbank, 2015), or by training decoding weights given random encoding weights (D'Souza et al., 2010; Urbanczik and Senn, 2014), but we simply calculated and set the decoding weights as if they had already been learned.

#### Compressive and expansive auto-encoder

Classical three-layer (input-hidden-output-layer) auto-encoders come in two different flavours, viz. compressive or expansive, which have the dimensionality of the hidden layer smaller or larger respectively, than that of the input and output layers. Instead of a three-layer feedfoward network, our auto-encoder forms a loop from the neurons in the recurrent network via readout weights to the output and from there via error-encoding weights to the input. Since the auto-encoder is in the loop, we expect that it works both as a compressive one (from neurons in the recurrent network over the low-dimensional output back to the neurons) and as an expansive one (from the output through the neurons in the recurrent network back to the output).

Rather than constraining, as in Equation (15), the low-dimensional input $ϵ_{\alpha}$ and round-trip output $\sum_{i}d_{\alpha⁢i}⁢a_{i}⁢(ϵ→)$ to be equal for each component $\alpha$ (expansive auto-encoder), we can alternatively enforce the high dimensional input $I_{j}$ (projection into neuron $j$ of low-dimensional input $ϵ→$).

$$
I_{j}≡\sum\alphae_{j⁢\alpha}⁢ϵ_{\alpha}
$$

And round-trip output $I_{j}^{′}≡\sum_{i,\alpha}e_{j⁢\alpha}⁢d_{\alpha⁢i}⁢g~_{i}⁢(I_{i})$, where $g~_{i}⁢(I_{i})≡a_{i}⁢(ϵ→)$, to be equal for each neuron $j$ in the recurrent network (compressive auto-encoder) in order to optimize the decoding weights of the auto-encoder. Thus, the squared-error loss for this compressive auto-encoder becomes:

$$
ℒ^{′}=\sumpP\sumjN(\sum\alphaN_{d}e_{j\alpha}(\sumiNd_{\alphai}a_{i}^{(p)}−ϵ_{\alpha}^{(p)}))^{2}=\sumpP\sumjN(\sum\alphaN_{d}e_{j\alpha}(\sumiNd_{\alphai}a_{i}^{(p)}−ϵ_{\alpha}^{(p)}))(\sum\gammaN_{d}e_{j\gamma}(\sumlNd_{\gammal}a_{l}^{(p)}−ϵ_{\gamma}^{(p)}))=\sumpP\sumjN\sum\alphaN_{d}e_{j\alpha}^{2}(\sumiNd_{\alphai}a_{i}^{(p)}−ϵ_{\alpha}^{(p)})^{2}+\sumpP\sumjN(\sum\alpha,\gamma,\alpha\neq\gammae_{j\alpha}e_{j\gamma}(\sumiNd_{\alphai}a_{i}^{(p)}−ϵ_{\alpha}^{(p)})(\sumlNd_{\gammal}a_{l}^{(p)}−ϵ_{\gamma}^{(p)}))≈c\sumpP\sum\alphaN_{d}(\sumiNd_{\alphai}a_{i}^{(p)}−ϵ_{\alpha}^{(p)})^{2},
$$

where in the approximation, we exploit that (i) the relative importance of the term involving $\sum_{p}^{P}\sum_{j}\sum_{\alpha,\gamma,\alpha\neq\gamma}e_{j⁢\alpha}⁢e_{j⁢\gamma}$ tends to zero as $1/\sqrt{N⁢P}$, since $e_{j⁢\alpha}$ and $e_{j⁢\gamma}$ are independent random variables; and (ii) $\sum_{j}e_{j⁢\alpha}^{2}≈c$ is independent of $\alpha$. Thus, the loss function of Equation (17) is approximately proportional to the squared-error loss function of Equation (15) (not considering the L2 regularization) used for the expansive auto-encoder, showing that for an auto-encoder embedded in a loop with fixed random encoding weights, the expansive and compressive descriptions are equivalent for those $N$-dimensional inputs $I_{i}$ that lie in the $N_{d}$-dimensional sub-space spanned by ${e_{i⁢\alpha}}$ i.e. $I_{i}$ is of the form $\sum_{\alpha}e_{i⁢\alpha}⁢ϵ_{\alpha}$ where $ϵ_{\alpha}$ lies in a finite domain (hypersphere). We employed a large number $P=N$ of random low-$N_{d}$-dimensional inputs when constraining the expansive auto-encoder.

#### Command input

The command input vector $u→⁢(t)$ to the network was $N_{c}$-dimensional ($N_{c}=N_{d}$ for all systems except the arm) and time-varying. During the learning phase, input changed over two different time scales. The fast value of each command component was switched every 50 ms to a level $u_{\alpha}^{′}$ chosen uniformly between $(-ζ_{1},ζ_{1})$ and this number was added to a more slowly changing input variable $u¯_{\alpha}$ (called ’pedestal’ in the main part of the paper) which changed with a period $T_{p⁢e⁢r⁢i⁢o⁢d}$. Here $u¯_{\alpha}$ is the component of a vector of length $ζ_{2}$ with a randomly chosen direction. The value of component $\alpha$ of the command is then $u_{\alpha}=u¯_{\alpha}+u_{\alpha}^{′}$. Parameter values for the network and input for each dynamical system are provided in Table 1. Further details are noted in the next subsection.

During the testing phase without error feedback, the network reproduced the reference trajectory of the dynamical system for a few seconds, in response to the same kind of input as during learning. We also tested the network on a different input not used during learning as shown in Figures 2 and 4.

### Equations and parameters for the example dynamical systems

The equations and input modifications for each dynamical system are detailed below. Time derivatives are in units of $s^{-1}$.

#### Linear system

The equations for a linear decaying oscillator system (Figure 2—figure supplement 2) are

$$
x˙_{1}=u_{1}/0.02+(-0.2⁢x_{1}-x_{2})/0.05x˙_{2}=u_{2}/0.02+(x_{1}-0.2⁢x_{2})/0.05.
$$

For this linear dynamical system, we tested the learned network on a ramp of 2 s followed by a step to a constant non-zero value. A ramp can be viewed as a preparatory input before initiating an oscillatory movement, in a similar spirit to that observed in (pre-)motor cortex (Churchland et al., 2012). For such input too, the network tracked the reference for a few seconds (Figure 2—figure supplement 2A–C).

#### van der Pol oscillator

The equations for the van der Pol oscillator system are

$$
x˙_{1}=u_{1}/0.02+x_{2}/0.125x˙_{2}=u_{2}/0.02+(2⁢(1-x_{1}^{2})⁢x_{2}-x_{1})/0.125.
$$

Each component of the pedestal input $u¯_{\alpha}$ was scaled differently for the van der Pol oscillator as reported in Table 1.

#### Lorenz system

The equations for the chaotic Lorenz system (Lorenz, 1963) are

$$
x˙_{1}=u_{1}/0.02+10⁢(x_{2}-x_{1})x˙_{2}=u_{2}/0.02-x_{1}⁢x_{3}-x_{2}x˙_{3}=u_{3}/0.02+x_{1}⁢x_{2}-8⁢(x_{3}+28)/3.
$$

In our equations above, $Z$ of the original Lorenz equations (Lorenz, 1963) is represented by an output variable $x_{3}=Z-28$ so as to have observable variables that vary around zero. This does not change the system dynamics, just its representation in the network. For the Lorenz system, only a pulse at the start for 250 ms, chosen from a random direction of norm $ζ_{1}$, was provided to set off the system, after which the system followed autonomous dynamics.

#### Non-linearly transformed input to linear system

For the above dynamical systems, the input adds linearly on the right hand sides of the differential equations. Our FOLLOW scheme also learned non-linear feedforward inputs to a linear dynamical system, as demonstrated in Figure 2—figure supplement 4 and Figure 2—figure supplement 5. As the reference, we used the linear dynamical system above, but with its input transformed non-linearly by $g_{\alpha}⁢(u→)=10⁢((u_{\alpha}/0.1)^{3}-u_{\alpha}/0.4)$. Thus, the equations of the reference were:

$$
x˙_{1}=10⁢((u_{1}/0.1)^{3}-u_{1}/0.4)+(-0.2⁢x_{1}-x_{2})/0.05x˙_{2}=10⁢((u_{2}/0.1)^{3}-u_{2}/0.4)+(x_{1}-0.2⁢x_{2})/0.05.
$$

The input to the network remained $u→$. Thus, effectively the feedforward weights had to learn the non-linear transform $g→⁢(u→)$ while the recurrent weights learned the linear system.

#### Arm dynamics

In the example of learning arm dynamics, we used a two-link model for an arm moving in the vertical plane with damping, under gravity (see for example http://www.gribblelab.org/compneuro/5_Computational_Motor_Control_Dynamics.html and https://github.com/studywolf/control/tree/master/studywolf_control/arms/two_link), with parameters from (Li, 2006). The differential equations for the four state variables, namely the shoulder and elbow angles $\theta→=(\theta_{1},\theta_{2})^{T}$ and the angular velocities $\omega→=(\omega_{1},\omega_{2})^{T}$, given input torques $\tau→=(\tau_{1},\tau_{2})^{T}$ are:

$$
\theta→˙=\omega→
$$



$$
\omega→˙=M(\theta→)^{−1}(\tau→−C(\theta→,\omega→)−B\omega→−gD(\theta→))
$$

with

$$
M(\theta→)=(d_{1}+2d_{2}cos⁡\theta_{2}+m_{1}s_{1}^{2}+m_{2}s_{2}^{2}d_{3}+d_{2}cos⁡\theta_{2}+m_{2}s_{2}^{2}d_{3}+d_{2}cos⁡\theta_{2}+m_{2}s_{2}^{2}d_{3}+m_{2}s_{2}^{2})C(\theta→,\omega→)=(−\theta˙_{2}(2\theta˙_{1}+\theta˙_{2})\theta˙_{1}^{2})d_{2}sin⁡\theta_{2},B=(b_{11}b_{12}b_{21}b_{22}),D(\theta→)=((m_{1}s_{1}+m_{2}l_{1})sin⁡\theta_{1}+m_{2}s_{2}sin⁡(\theta_{1}+\theta_{2})m_{2}s_{2}sin⁡(\theta_{1}+\theta_{2})),d_{1}=I_{1}+I_{2}+m_{2}l_{1}^{2},d_{2}=m_{2}l_{1}s_{2},d_{3}=I_{2},
$$

where $m_{i}$ is the mass, $l_{i}$ the length, $s_{i}$ the distance from the joint centre to the centre of the mass, and $I_{i}$ the moment of inertia, of link $i$; $M$ is the moment of inertia matrix; $C$ contains centripetal and Coriolis terms; $B$ is for joint damping; and $D$ contains the gravitational terms. Here, the state variable vector $x→=[\theta_{1},\theta_{2},\omega_{1},\omega_{2}]^{T}$, but the effective torque $\tau→$ is obtained from the input torque $u→$ as follows.

To avoid any link from rotating full 360 degrees, we provide an effective torque $\tau_{\alpha}$ to the arm, by subtracting a term proportional to the input torque $u_{\alpha}$, if the angle crosses $\pm$90 degrees and $u_{\alpha}$ is in the same direction:

$$
\tau_{\alpha}=u_{\alpha}-{u_{\alpha}⁢\sigma~⁢(\theta_{\alpha})u_{\alpha}>00u_{\alpha}=0u_{\alpha}⁢\sigma~⁢(-\theta_{\alpha})u_{\alpha}<0,
$$

where $\sigma~⁢(\theta)$ increases linearly from 0 to 1 as $\theta$ goes from $\pi/2$ to $3⁢\pi/4$:

$$
\sigma~(\theta)={0\theta\leq\pi/2(\theta−\pi/2)/(\pi/4)3\pi/4>\theta>\pi/21\theta\geq3\pi/4
$$

The parameter values were taken from the human arm (Model 1) in section 3.1.1 of the PhD thesis of Li (Li, 2006) from the Todorov lab; namely $m_{1}=1.4⁢kg$, $m_{2}=1.1⁢kg$, $l_{1}=0.3⁢m$, $l_{2}=0.33⁢m$, $s_{1}=0.11⁢m$, $s_{2}=0.16⁢m$, $I_{1}=0.025⁢kg m^{2}$, $I_{2}=0.045⁢kg m^{2}$, and $b_{11}=b_{22}=0.05$, $b_{12}=b_{21}=0.025$. Acceleration due to gravity was set at $g=9.81⁢m/s^{2}$. For the arm, we did not filter the reference variables for calculating the error.

The input torque $u→⁢(t)$ for learning the two-link arm was generated, not by switching the pulse and pedestal values sharply, every 50 ms and $T_{p⁢e⁢r⁢i⁢o⁢d}$ as for the others, but by linearly interpolating in-between to avoid oscillations from sharp transitions.

The input torque $u→$ and the variables $\omega→$, $\theta→$ obtained on integrating the arm model above were scaled by $0.02$, $0.05$ and $1/2.5$ respectively, and then used as the input and reference for the spiking network. Effectively, we scaled the input torques to cover one-fifth of the representation radius $R_{2}$, the angular velocities one-half, and the angles full, as each successive variable was the integral of the previous one.

#### Learning readout weights with recurrent weights fixed

For learning the readout weights after setting either the true or shuffled set of learned recurrent weights (Figure 2—figure supplement 3), we used a perceptron learning rule.

$$
\frac{d}{d⁢t}⁢d_{\alpha⁢i}=-η_{r}⁢(\sumjd_{\alpha⁢j}⁢(S_{j}*κ)⁢(t)-x_{\alpha}⁢(t))⁢(S_{i}*κ)⁢(t)=-η_{r}⁢(x^_{\alpha}⁢(t)-x_{\alpha}⁢(t))⁢(S_{i}*κ)⁢(t),
$$

with learning rate $η_{r}=1⁢e-4$.

### Derivation and proof of stability of the FOLLOW learning scheme

We derive the FOLLOW learning rule Equation (10), while simultaneously proving the stability of the scheme. We assume that: (1) the feedback ${k⁢e_{i⁢\alpha}}$ and readout weights ${d_{\alpha⁢j}}$ form an auto-encoder with gain $k$; (2) given the gains and biases of the spiking LIF neurons, there exist feedforward and recurrent weights that make the network follow the reference dynamics perfectly (in practice, the dynamics is only approximately realizable by our network, see Appendix 1 for a discussion); (3) the state $x→$ of the dynamical system is observable; (4) the intrinsic time scales of the reference dynamics are much larger than the synaptic time scale and the time scale of the error feedback loop, and much smaller than the time scale of learning; (5) the feedforward and recurrent weights remain bounded; and (6) the input $u→$ and reference output $x→$ remain bounded.

The proof proceeds in three major steps: (1) using the auto-encoder assumption to write the evolution equation of the low-dimensional output state variable in terms of the recurrent and feedforward weights; (2) showing that output follows the reference due to the error feedback loop; and (3) obtaining the evolution equation for the error and using it in the time-derivative of a Lyapunov function $V$, to show that $V˙\leq0$ for uniform stability, similar to proofs in adaptive control theory (Narendra and Annaswamy, 1989; Ioannou and Sun, 2012).

#### Role of network weights for low-dimensional output

The filtered low-dimensional output of the recurrent network is given by Equation (3) of Results and repeated here:

$$
x^_{\alpha}=\sumjd_{\alpha⁢j}⁢(S_{j}*κ)⁢(t),
$$

where $d_{\alpha⁢j}$ are the readout weights. Since $κ$ is an exponential filter with time constant $\tau_{s}$, Equation (21) can also be written as

$$
\tau_{s}⁢x^˙_{\alpha}⁢(t)=-x^_{\alpha}⁢(t)+\sumjd_{\alpha⁢j}⁢S_{j}⁢(t),
$$

We convolve this equation with kernel $κ$, multiply by the error feedback weights, and sum over the output components $\alpha$

$$
\tau_{s}⁢\sum\alphae_{i⁢\alpha}⁢(x^˙_{\alpha}*κ)⁢(t)=-\sum\alphae_{i⁢\alpha}⁢(x^_{\alpha}*κ)⁢(t)+\sum\alphae_{i⁢\alpha}⁢\sumjd_{\alpha⁢j}⁢(S_{j}*κ)⁢(t).
$$

We would like to write Equation (23) in terms of the recurrent and feedforward weights in the network.

To do this, we exploit assumptions (1) and (4). Having shown the equivalence of the compressive and expansive descriptions of our auto-encoder in the error-feedback loop (Equation (15) and (Equation (17))), we formulate our non-linear auto-encoder as compressive: we start with a high-dimensional set of inputs $I_{j}≡J_{j}-b_{j}$ (where $J_{j}$ is the current into neuron $j$ with bias $b_{j}$, cf. Equations (5) and (6)); transform these inputs non-linearly into filtered spike trains $S_{j}*κ$; decode these filtered spike trains into a low-dimensional representation $z→$ with components $z_{\alpha}=\sum_{j}d_{\alpha⁢j}⁢(S_{j}*κ)$; and increase the dimensionality back to the original one, via weights $k⁢e_{i⁢\alpha}$, to get inputs:

$$
I_{i}^{′}=\sum\alphak⁢e_{i⁢\alpha}⁢z_{\alpha}=k⁢\sum\alpha\sumje_{i⁢\alpha}⁢d_{\alpha⁢j}⁢(S_{j}*κ).
$$

Using assumption (1) we expect that the final inputs $I_{i}^{′}$ are approximately $k$ times the initial inputs $I_{i}$:

$$
k⁢\sum\alpha\sumje_{i⁢\alpha}⁢d_{\alpha⁢j}⁢(S_{j}*κ)≈k⁢I_{i}.
$$

This is valid only if the high-$N$-dimensional input $I_{i}$ lies in the low-$N_{d}$-dimensional subspace spanned by ${e_{i⁢\alpha}}$ (Equation (17)). We show that this requirement is fulfilled in the next major step of the proof (see text accompanying Equations (31–35)).

Our assumption (4) says that the state variables of the reference dynamics change slowly compared to neuronal dynamics. Due to the spatial averaging (sum over $j$ in Equation (25)) over a large number of neurons, individual neurons do not necessarily have to fire at a rate higher than the inverse of the synaptic time scale, while we can still assume that the total round trip input $I_{i}^{′}$ on the left hand side of Equation (25) is varying only on the slow time scale. Therefore, we used firing rate equations to compute mean outputs given static input when pre-calculating the readout weights (earlier in Materials and methods).

Inserting the approximate Equation (25) into Equation (23) we find

$$
\tau_{s}⁢\sum\alphae_{i⁢\alpha}⁢(x^˙_{\alpha}*κ)⁢(t)≈-\sum\alphae_{i⁢\alpha}⁢(x^_{\alpha}*κ)⁢(t)+I_{i}⁢(t).
$$

We replace $I_{i}≡J_{i}-b_{i}$, using the current $J_{i}$ from Equation (6) for neuron $i$ of the recurrent network, to obtain

$$
\tau_{s}\sum\alphae_{i\alpha}(x^˙_{\alpha}∗κ)(t)≈−\sum\alphae_{i\alpha}(x^_{\alpha}∗κ)(t)+\sumjw_{ij}(S_{j}∗κ)(t)+\sumlw_{il}^{ff}(S_{l}^{ff}∗κ)(t)+\sum\alphake_{i\alpha}(ϵ_{\alpha}∗κ)(t).
$$

Thus, the change of the low-dimensional output $x^_{\alpha}*κ$ depends on the network weights, which need to be learned. This finishes the first step of the proof.

#### Error-feedback loop ensures that output follows reference

Because of assumption (2), we may assume that there exists a recurrent network of spiking neurons that represents the desired dynamics of Equation (1) without any error feedback. This second network serves as a target during learning and has variables and parameters indicated with an asterisk. In particular, the second network has feedforward weights $w_{i⁢l}^{ff*}$ and recurrent weights $w_{i⁢j}^{*}$. We write an equation similar to Equation (27) for the output $x_{\alpha}^{*}$ of the target network:

$$
\tau_{s}\sum\alphae_{i\alpha}(x˙_{\alpha}^{∗}∗κ)(t)=−\sum\alphae_{i\alpha}(x_{\alpha}^{∗}∗κ)(t)+\sumjw_{ij}^{∗}(S_{j}^{∗}∗κ)(t)+\sumlw_{il}^{ff∗}(S_{l}^{ff∗}∗κ)(t),
$$

where $(S_{l}^{ff∗}∗κ)(t)$ and $(S_{j}^{*}*κ)⁢(t)$ are defined as the filtered spike trains of neurons in the realizable target network. We emphasize that this target network does not need error feedback because its output is, by definition, always correct. In fact, the readout from the spike trains $S_{j}^{*}$ gives the target output which we denote by $x→^{*}$. The weights of the target network are constant and their actual values are unimportant. They are mere mathematical devices to demonstrate stable learning of the first network which has adaptable weights. For the first network, we choose the same number of neurons and the same neuronal parameters as for the second network; moreover, the input encoding weights from the command input to the representation layer and the readout weights from the recurrent network to the output are identical for both networks. Thus, the only difference is that the feedforward and recurrent weights of the target network are realized, while for the first network they need to be learned.

In view of potential generalization, we note that any non-linear dynamical system is approximately realizable due to the expansion in a high-dimensional non-linear basis that is effectively performed by the recurrent network (see Appendix 1). Approximative weights (close to the ideal ones) could in principle also be calculated algorithmically (see Appendix 1). In the following we exploit assumption (2) and assume that the dynamics is actually (and not only approximately) realized by the target network.

Our assumption (3) states that the output is observable. Therefore the error component $ϵ_{\alpha}$ can be computed directly via a comparison of the true output $x→$ of the reference with the output $x^→$ of the network: $ϵ_{\alpha}=x_{\alpha}-x^_{\alpha}.$ (In view of potential generalizations, we remark that the observable output need not be the state variables themselves, but could be a higher-dimensional non-linear function of the state variables, as shown for a general dynamical system in Appendix 1.)

As the second step of the proof, we now show that the error feedback loop enables the first network to follow the target network under assumptions (4 - 6). More precisely, we want to show that the readout and neural activities of the first network remain close to those of the target network at all times, that is $x^_{\alpha}⁢(t)≈x_{\alpha}^{*}⁢(t)$ for each component $\alpha$ and $(S_{i}*κ)⁢(t)≈(S_{i}^{*}*κ)⁢(t)$ for each neuron index $i$. To do so, we use assumption (4) and exploit that (i) learning is slow compared to the network dynamics so the weights of the first network can be considered momentarily constant, and (ii) the reference dynamics is slower than the synaptic and feedback loop time scales, so the reference output $x_{\alpha}$ can be assumed momentarily constant. Thus, we have a separation of time scales in Equation (27): for a given input (transmitted via the feedforward weights) and a given target value $x_{\alpha}^{*}$, the network dynamics settles on the fast time scale $\tau_{s}$ to a momentary fixed point $x^^{†}$ which we find by setting the derivative on the left-hand side of Equation (27) to zero:

$$
0=−\sum\alphae_{i\alpha}(x^_{\alpha}^{†}∗κ)(t)+\sumjw_{ij}(S_{j}∗κ)(t)+\sumlw_{il}^{ff}(S_{l}^{ff}∗κ)(t)+\sum\alphake_{i\alpha}((x_{\alpha}^{∗}−x^_{\alpha}^{†})∗κ)(t).
$$

We rewrite this equation in the form

$$
\sum\alphae_{i\alpha}(x^_{\alpha}^{†}∗κ)(t)=\frac{k}{k+1}\sum\alphae_{i\alpha}(x_{\alpha}^{∗}∗κ)(t)+\frac{1}{k+1}(\sumjw_{ij}(S_{j}∗κ)(t)+\sumlw_{il}^{ff}(S_{l}^{ff}∗κ)(t)).
$$

We choose the feedback gain for the error much larger than 1 ($k≫1$), such that $k/(k+1)≈1$. Using our assumption (5) that the feedforward and recurrent weights are bounded, and since the filtered spike trains remain bounded due to the refractory period, the term in parentheses multiplying $1/(k+1)$ remains bounded, by say $B_{1}$. We further use assumption (6) that the target output $x→^{*}$ is bounded by say $X$. Choosing $k≫B_{1}/X$, the second term can be made negligible compared to the first. Thus, to obtain $x^_{\alpha}^{†}≈x_{\alpha}^{*}$, we set $k≫1$ and $k≫B_{1}/X$.

To show that the momentary fixed point is stable at the fast synaptic time scale, we calculate the Jacobian $=[_{i⁢l}]$, for the dynamical system given by Equation (27). We introduce auxiliary variables $y_{i}≡\sum_{\alpha}e_{i⁢\alpha}⁢x^_{\alpha}$ to rewrite Equation (27) with the new variables in the form $y˙_{i}=F_{i}⁢(y→)$; and then we take derivative of its right hand side to obtain the elements of the Jacobian matrix at the fixed point $\sum_{\alpha}e_{i⁢\alpha}⁢x^_{\alpha}^{†}$:

$$
𝒥_{il}≡\frac{∂F_{i}(y→)}{∂y_{l}}=−(k+1)\delta_{il}\int_{−∞}^{t}κ(\tau)d\tau+\frac{∂\sumjw_{ij}(S_{j}∗κ)(t)}{∂y_{l}}|_{y_{i}=\sum\alphae_{i\alpha}x^_{\alpha}^{†}},
$$

where $\delta_{i⁢l}$ is the Kronecker delta function. We note that $\sum_{j}w_{i⁢j}⁢(S_{j}*κ)$ is a spatially and temporally averaged measure of the population activity in the network with appropriate weighting factors $w_{i⁢j}$. We assume that the population activity varies smoothly with input, which is equivalent to requiring that on the time scale $\tau_{s}$, the network fires asynchronously, i.e. there are no precisely timed population spikes. Then we can take the second term to be bounded, in absolute value, by say $B_{2}$. The Jacobian matrix $J$ is of the form $−(k+1)I+Λ$, where $I$ is the $N\timesN$ identity matrix and $Λ$ is a matrix with each element bounded in absolute value by $B_{2}$. If we set $k≫N⁢B_{2}$, then all eigenvalues of the Jacobian have negative real parts, applying the Gerschgorin circle theorem (the second term can perturb any eigenvalue from $−(k+1)$ to within a circle of radius $N⁢B_{2}$ at most), rendering the momentary fixed point asymptotically stable.

Thus, we have shown that if the initial state of the first network is close to the initial state of the target network, e.g., both start from rest, then on the slow time scale of the system dynamics of the reference $x→^{*}$, the first network output follows the target network output at all times, $x^_{\alpha}≈x_{\alpha}^{*}$.

We now show that neurons are primarily driven by inputs close to those in the target network due to error feedback, and that these lie in the low-dimensional manifold spanned by ${e_{i⁢\alpha}}$, as required for Equation (25). We compute the projected error using Equation (30):

$$
\sum\alphae_{i\alpha}(ϵ_{\alpha}∗κ)(t)=\sum\alphae_{i\alpha}((x_{\alpha}^{∗}−x^_{\alpha}^{†})∗κ)(t)=\frac{1}{k+1}\sum\alphae_{i\alpha}(x_{\alpha}^{∗}∗κ)(t)−\frac{1}{k+1}(\sumjw_{ij}(S_{j}∗κ)(t)+\sumlw_{il}^{ff}(S_{l}^{ff}∗κ)(t)),
$$

and insert it into Equation (6) to obtain the current into a neuron in the recurrent network:

$$
J_{i}=\frac{k}{k+1}\sum\alphae_{i\alpha}(x_{\alpha}^{∗}∗κ)(t)+\frac{1}{k+1}(\sumjw_{ij}(S_{j}∗κ)(t)+\sumlw_{il}^{ff}(S_{l}^{ff}∗κ)(t))+b_{i}
$$

At the start of learning, if the feedforward and recurrent weights are small, then the neural input is dominated by the fed-back error input that is the first term, making $J_{i}$ close to the ideal current

$$
J_{i}^{*}=\sum\alphae_{i⁢\alpha}⁢(x_{\alpha}^{*}*κ)⁢(t)+b_{i}.
$$

Thus, the neural input at the start of learning is of the form $\sum_{\alpha}e_{i⁢\alpha}⁢x_{\alpha}^{*}$ which lies in the low-dimensional subspace spanned by ${e_{i⁢\alpha}}$ as required for Equation (25). Furthermore, over time, the feedforward and recurrent weights get modified so that their contribution tends towards $\sum_{\alpha}e_{i⁢\alpha}⁢(x_{\alpha}^{*}*κ)$, such that the two terms of Equation (32) add to make $J_{i}$ even closer to the ideal current $J_{i}^{*}$ given by Equation (33). This is made clearer by considering the weight update rule Equation 10 as stochastic gradient descent on a loss function,

$$
ℒ^{J}=\frac{1}{2}\sumi(\sum\alphae_{i\alpha}(x_{\alpha}^{∗}∗κ)(t)−\sumlw_{il}^{ff}(S_{l}^{ff}∗κ)(t)−\sumjw_{ij}(S_{j}∗κ)(t))^{2},
$$

leading us to (for each recurrent weight $w_{i⁢j}$, and similarly for $w_{i⁢l}^{ff}$):

$$
w˙_{ij}=−η^{′}\frac{∂ℒ^{J}}{∂w_{ij}}=η^{′}(\sum\alphae_{i\alpha}(x_{\alpha}^{∗}∗κ)−\sumlw_{il}^{ff}(S_{l}^{ff}∗κ)−\sumjw_{ij}(S_{j}∗κ))(S_{j}∗κ)=η^{′}\frac{k+1}{k}(I_{i}^{ϵ}∗κ)(S_{j}∗κ),
$$

which is identical to the FOLLOW learning rule for $w_{i⁢j}$ in Equation (10) except for the time-scale of filtering of the error current (see Discussion), and a factor involving $k$ that can be absorbed into the learning rate $η^{′}$. In the last step above, we used the projected error current from Equation (31) and the definition of $I_{i}^{ϵ}$ in Equation (8). Thus, the feedforward and recurrent connections evolve to inject, after learning, the same ideal input within the low-dimensional manifold, as was provided by the error feedback during learning. Hence, the neural input remains in the low-dimensional manifold spanned by ${e_{i⁢\alpha}}$ throughout learning, as required for Equation (25), making this major step and the previous one self-consistent.

Since the driving neural currents are close to ideal throughout learning, the filtered spike trains of the recurrent neurons in the first network will also be approximately the same as those of the target network, so that $(S_{i}*κ)⁢(t)$ can be used instead of $(S_{i}^{*}*κ)⁢(t)$ in (Equation (28)). Moreover, the filtered spike trains $(S_{l}^{ff}*κ)⁢(t)$ of the command representation layer in the first network are the same as those in the target network, since they are driven by the same command input $u→$ and the command encoding weights are, by construction, the same for both networks. The similarity of the spike trains in the first and target networks will be used in the next major part of the proof.

#### Stability of learning via Lyapunov’s method

We now turn to the third step of the proof and consider the temporal evolution of the error $ϵ_{\alpha}=x_{\alpha}-x^_{\alpha}$. We exploit that the network dynamics is realized by the target network and insert Equations (27) and (28) so as to find

$$
−\tau_{s}\sum\alphae_{i\alpha}(ϵ˙_{\alpha}∗κ)(t)=\tau_{s}\sum\alphae_{i\alpha}((x^˙_{\alpha}−x˙_{\alpha})∗κ)(t)≈\tau_{s}\sum\alphae_{i\alpha}((x^˙_{\alpha}−x˙_{\alpha}^{∗})∗κ)(t)≈\sumj(w_{ij}−w_{ij}^{∗})(S_{j}∗κ)(t)+\suml(w_{il}^{ff}−w_{il}^{ff∗})(S_{l}^{ff}∗κ)(t)+(k+1)\sum\alphae_{i\alpha}(ϵ_{\alpha}∗κ)(t)≡\sumjψ_{ij}(S_{j}∗κ)(t)+\sumlϕ_{il}(S_{l}^{ff}∗κ)(t)+(k+1)\sum\alphae_{i\alpha}(ϵ_{\alpha}∗κ)(t),
$$

In the second line, we have replaced the reference output by the target network output; and in the third line we have used Equations (27) and (28), and replaced the filtered spike trains of the target network by those of the first network, exploiting the insights from the previous paragraph. In the last line, we have introduced abbreviations $ψ_{i⁢j}≡w_{i⁢j}-w_{i⁢j}^{*}$ and $ϕ_{i⁢l}≡w_{i⁢l}^{ff}-w_{i⁢l}^{ff*}$.

In order to show that the absolute value of the error decreases over time with an appropriate learning rule, we consider the candidate Lyapunov function:

$$
V⁢(ϵ~,ψ,ϕ)=\frac{1}{2}⁢\sumiϵ~_{i}^{2}+\frac{1}{2}⁢\frac{1}{η~_{1}}⁢\sumi,j(ψ_{i⁢j})^{2}+\frac{1}{2}⁢\frac{1}{η~_{2}}⁢\sumi,l(ϕ_{i⁢l})^{2},
$$

where $ϵ~_{i}≡\tau_{s}⁢\sum_{\alpha}e_{i⁢\alpha}⁢(ϵ_{\alpha}*κ)$ and $η~_{1},η~_{2}>0$ are positive constants. We use Lyapunov’s direct method to show the stability of learning. For this, we require the following properties for the Lyapunov function. (a) The Lyapunov function is positive semi-definite $V⁢(ϵ~,ψ,ϕ)\geq0$, with the equality to zero only at $(ϵ~,ψ,ϕ)=(0,0,0)$. (b) It has continuous first-order partial derivatives. Furthermore, $V$ is (c) radially unbounded since

$$
V⁢(ϵ~,ψ,ϕ)>|(ϵ~,ψ,ϕ)|^{2}/(4⁢max⁡(1,η~_{1},η~_{2})),
$$

and (d) decrescent since

$$
V⁢(ϵ~,ψ,ϕ)<|(ϵ~,ψ,ϕ)|^{2}/min⁡(1,η~_{1},η~_{2}),
$$

where $|(ϵ~,ψ,ϕ)|^{2}≡\sum_{i}(ϵ~_{i})^{2}+\sum_{i,j}(ψ_{i⁢j})^{2}+\sum_{i,k}(ϕ_{i⁢l})^{2}$ and $min/max$ take the minimum/maximum of their respective arguments.

Apart from the above conditions (a)-(d), we need to show the key property $V˙\leq0$ for uniform global stability (which implies that bounded orbits remain bounded, so the error remains bounded); or the stronger property $V˙<0$ for asymptotic global stability (see for example [Narendra and Annaswamy, 1989; Ioannou and Sun, 2012]). Taking the time derivative of $V$, and replacing $ϵ~˙_{i}$that is $\tau_{s}⁢\sum_{\alpha}e_{i⁢\alpha}⁢(ϵ˙_{\alpha}*κ)$ from (Equation (36)), we have:

$$
V˙=\sumiϵ~_{i}ϵ~˙_{i}+\frac{1}{η~_{1}}\sumi,jψ_{ij}ψ˙_{ij}+\frac{1}{η~_{2}}\sumi,lϕ_{il}ϕ˙_{il}≈−\sumiϵ~_{i}(\sumjψ_{ij}(S_{j}∗κ)(t)+\sumlϕ_{il}(S_{l}^{ff}∗κ)(t)+(k+1)\sum\alphae_{i\alpha}(ϵ_{\alpha}∗κ)(t))+\frac{1}{η~_{1}}\sumi,jψ_{ij}ψ˙_{ij}+\frac{1}{η~_{2}}\sumi,lϕ_{il}ϕ˙_{il}=\sumi,jψ_{ij}(−ϵ~_{i}(S_{j}∗κ)(t)+\frac{1}{η~_{1}}ψ˙_{ij})+\sumi,kϕ_{il}(−ϵ~_{i}(S_{l}^{ff}∗κ)(t)+\frac{1}{η~_{2}}ϕ˙_{il})−(k+1)\sumiϵ~_{i}^{2}/\tau_{s}.
$$

If we enforce the first two terms above to be zero, we derive a learning rule

$$
ψ˙_{ij}=η~_{1}ϵ~_{i}(S_{j}∗κ)(t)ϕ˙_{il}=η~_{2}ϵ~_{i}(S_{l}^{ff}∗κ)(t),
$$

and then

$$
V˙=-(k+1)⁢\sumiϵ~_{i}^{2}/\tau_{s}\leq0
$$

requiring $k>-1$, which is subsumed under $k≫1$ for the error feedback. The condition Equation 39 with $η_{1}≡η~_{1}⁢\tau_{s}$ and $η_{2}≡η~_{2}⁢\tau_{s}$, and $κ$ replaced by a longer filtering kernel $κ^{ϵ}$, is the learning rule used in the main text, Equation (10).

Thus, in the $(ϵ~,ψ,ϕ)$-system given by Equations (36) and (39), we have proven the global uniform stability of the fixed point $(ϵ~,ψ,ϕ)=(0,0,0)$, which is effectively $(ϵ,ψ,ϕ)=(0,0,0)$, choosing $η_{1},η_{2}>0$ and $k≫max⁡(1,B_{1}/X,B_{2})$, under assumptions (1 - 6), while simultaneously deriving the learning rule (Equation (39)).

This ends our proof. So far, we have shown that the system is Lyapunov stable, that is bounded orbits remain bounded, and not asymptotically stable. Indeed, with bounded firing rates and fixed readout weights, the output will remain bounded, as will the error (for a bounded reference). However, here, we also derived the FOLLOW learning rule, and armed with the inequality for the time derivative of the Lyapunov function in terms of the error, we further show in the following subsection that the error $ϵ→$ goes to zero asymptotically, so that after learning, even without error feedback, $x^→$ reproduces the dynamics of $x→$.

A major caveat of this proof is that under assumption (2) the dynamics be realizable by our network. In a real application this might not be the case. Approximation errors arising from a mismatch between the best possible network and the actual target dynamics are currently ignored. The adaptive control literature has shown that errors in approximating the reference dynamics appear as frozen noise and can cause runaway drift of the parameters (Narendra and Annaswamy, 1989; Ioannou and Sun, 2012). In our simulations with a large number of neurons, the approximations of a non-realizable reference dynamics (e.g., the Van der Pol oscillator) were sufficiently good, and thus the expected drift was possibly slow, and did not cause the error to rise during typical time-scales of learning. A second caveat is our assumption (5). While the input is under our control and can therefore be kept bounded, some additional bounding is needed to stop weights from drifting. Various techniques to address such model-approximation noise and bounding weights have been studied in the robust adaptive control literature (e.g., (Ioannou and Tsakalis, 1986; Slotine and Coetsee, 1986; Narendra and Annaswamy, 1989; Ioannou and Fidan, 2006; Ioannou and Sun, 2012)). We discuss this issue and briefly mention some of these ameliorative techniques in Appendix 1.

To summarize, the FOLLOW learning rule (Equation (39)) on the feedforward or recurrent weights has two terms: (i) a filtered presynaptic firing trace $(S_{l}^{ff}∗κ)(t)$ or $(S_{j}*κ)⁢(t)$ that is available locally at each synapse; and (ii) a projected filtered error $\sum_{\alpha}e_{i⁢\alpha}⁢(ϵ_{\alpha}*κ)⁢(t)$ used for all synapses in neuron $i$ that is available as a current in the postsynaptic neuron $i$ due to error feedback, see Equation (6). Thus the learning rule can be classified as local. Moreover, it uses an error in the observable $x→$, not in its time-derivative. While we have focused on spiking networks, the learning scheme can be easily used for non-linear rate units by replacing the filtered spikes $(S_{i}*κ)⁢(t)$ by the output of the rate units $r⁢(t)$. Our proof is valid for arbitrary dynamical transforms $h→⁢(x→,u→)$ as long as they are realizable in a network. The proof shows uniform global stability using Lyapunov’s method.

### Proof of error tending to zero asymptotically

In the above subsection, we showed uniform global stability using $V˙=-(k+1)⁢\sum_{i}(ϵ~_{i})^{2}\leq0$, with $k≫max⁡(1,B_{1}/X,B_{2})$ and $ϵ~_{i}≡\tau_{s}⁢\sum_{\alpha}e_{j⁢\alpha}⁢(ϵ_{\alpha}*κ)$. This only means that bounded errors remain bounded. Here, we show more importantly that the error tends to zero asymptotically with time. We adapt the proof in section 4.2 of (Ioannou and Sun, 2012), to our spiking network.

Here, we want to invoke a special case of Barbălat’s lemma: if $f,f˙\inℒ_{∞}$ and $f\inℒ_{p}$ for some $p\in[1,∞)$, then $f⁢(t)→0$ as $t→∞$. Recall the definitions: function $f\inℒ_{p}$ when $||x||_{p}≡(\int_{0}^{∞}|f⁢(\tau)|^{p}⁢d⁢\tau)^{1/p}$ exists (is finite); and similarly function $f\inℒ_{∞}$ when $||x||_{∞}≡sup_{t\geq0}⁡|f⁢(\tau)|$ exists (is finite).

Since $V$ is positive semi-definite ($V\geq0$) and is a non-increasing function of time ($V˙\leq0$), its $lim_{t→∞}⁡V=V_{∞}$ exists and is finite. Using this, the following limit exists and is finite:

$$
\sumi\int_{0}^{∞}(ϵ~_{i}⁢(\tau))^{2}⁢d⁢\tau=\frac{-1}{k+1}⁢\int_{0}^{∞}V˙⁢(\tau)⁢d⁢\tau=\frac{1}{k+1}⁢(V⁢(0)-V_{∞}).
$$

Since each term in the above sum $\sum_{i}$ is positive semi-definite, $\int_{0}^{∞}(ϵ~_{i}⁢(\tau))^{2}⁢d⁢\tau$ also exists and is finite $∀i$, and thus $ϵ~_{i}\inℒ_{2}⁢∀i$.

To show that $ϵ~_{i},ϵ~˙_{i}\inℒ_{∞}⁢∀i$, consider Equation (36). We use assumption (6) that the input $u→⁢(t)$ and the reference output $x→⁢(t)$ are bounded. Since network output $x^→$ is also bounded due to saturation of firing rates (as are the filtered spike trains), the error (each component) is bounded i.e. $ϵ~_{i}\inℒ_{∞}⁢∀i$. If we also bound the weights from diverging during learning (assumption (5)), then $ψ_{ij},ϕ_{il}\inℒ_{∞} ∀i,j,l$. With these reasonable assumptions, all terms on the right hand side of the Equation (36) for $ϵ~˙_{i}$ are bounded, hence $ϵ~˙_{i}\inℒ_{∞}⁢∀i$.

Since $ϵ~_{i}\inℒ_{2}⁢∀i$ and $ϵ_{i}~,ϵ~˙_{i}\inℒ_{∞}⁢∀i$, invoking Barbălat’s lemma as above, we have $ϵ~_{i}→0⁢∀i$ as $t→∞$. We have shown that the error tends to zero asymptotically under assumptions (1 - 6). In practice, the error shows fluctuations on a short time scale while the mean error over a longer time scale reduces and then plateaus, possibly due to approximate realizability, imperfections in the error-feedback, and spiking shot noise (cf. Figure 5).

We do not further require the convergence of parameters to ideal ones for our purpose, since the error tending to zero, that is network output matching reference, is functionally sufficient for the forward predictive model. In the adaptive control literature (Ioannou and Sun, 2012; Narendra and Annaswamy, 1989), the parameters (weights) are shown to converge to ideal ones if input excitation is ‘persistent’, loosely that it excites all modes of the system. It should be possible to adapt the proof to our spiking network, as suggested by simulations (Figure 5), but is not pursued here.
