# Interrogating theoretical models of neural computation with emergent property inference

## Authors

- Sean R Bittner<sup>1</sup> ([ORCID: 0000-0002-6773-5402](https://orcid.org/0000-0002-6773-5402))
- Agostina Palmigiano<sup>1</sup>
- Alex T Piet<sup>2</sup> ([ORCID: 0000-0002-6529-1414](https://orcid.org/0000-0002-6529-1414))
- Chunyu A Duan<sup>5</sup> ([ORCID: 0000-0002-3095-8653](https://orcid.org/0000-0002-3095-8653))
- Carlos D Brody<sup>2</sup> ([ORCID: 0000-0002-4201-561X](https://orcid.org/0000-0002-4201-561X))
- Kenneth D Miller<sup>1</sup>
- John Cunningham<sup>7</sup> †

### Affiliations

1. Department of Neuroscience, Columbia University New York United States
2. Princeton Neuroscience Institute Princeton United States
3. Princeton University Princeton United States
4. Allen Institute for Brain Science Seattle United States
5. Institute of Neuroscience, Chinese Academy of Sciences Shanghai China
6. Howard Hughes Medical Institute Chevy Chase United States
7. Department of Statistics, Columbia University New York United States

† Corresponding author

## Abstract

A cornerstone of theoretical neuroscience is the circuit model: a system of equations that captures a hypothesized neural mechanism. Such models are valuable when they give rise to an experimentally observed phenomenon -- whether behavioral or a pattern of neural activity -- and thus can offer insights into neural computation. The operation of these circuits, like all models, critically depends on the choice of model parameters. A key step is then to identify the model parameters consistent with observed phenomena: to solve the inverse problem. In this work, we present a novel technique, emergent property inference (EPI), that brings the modern probabilistic modeling toolkit to theoretical neuroscience. When theorizing circuit models, theoreticians predominantly focus on reproducing computational properties rather than a particular dataset. Our method uses deep neural networks to learn parameter distributions with these computational properties. This methodology is introduced through a motivational example of parameter inference in the stomatogastric ganglion. EPI is then shown to allow precise control over the behavior of inferred parameters and to scale in parameter dimension better than alternative techniques. In the remainder of this work, we present novel theoretical findings in models of primary visual cortex and superior colliculus, which were gained through the examination of complex parametric structure captured by EPI. Beyond its scientific contribution, this work illustrates the variety of analyses possible once deep learning is harnessed towards solving theoretical inverse problems.

## Introduction

The fundamental practice of theoretical neuroscience is to use a mathematical model to understand neural computation, whether that computation enables perception, action, or some intermediate processing. A neural circuit is systematized with a set of equations – the model – and these equations are motivated by biophysics, neurophysiology, and other conceptual considerations (Kopell and Ermentrout, 1988; Marder, 1998; Abbott, 2008; Wang, 2010; O'Leary et al., 2015). The function of this system is governed by the choice of model parameters, which when configured in a particular way, give rise to a measurable signature of a computation. The work of analyzing a model then requires solving the inverse problem: given a computation of interest, how can we reason about the distribution of parameters that give rise to it? The inverse problem is crucial for reasoning about likely parameter values, uniquenesses and degeneracies, and predictions made by the model (Gutenkunst et al., 2007; Erguler and Stumpf, 2011; Mannakee et al., 2016).

Ideally, one carefully designs a model and analytically derives how computational properties determine model parameters. Seminal examples of this gold standard include our field’s understanding of memory capacity in associative neural networks (Hopfield, 1982), chaos and autocorrelation timescales in random neural networks (Sompolinsky et al., 1988), central pattern generation (Olypher and Calabrese, 2007), the paradoxical effect (Tsodyks et al., 1997), and decision making (Wong and Wang, 2006). Unfortunately, as circuit models include more biological realism, theory via analytical derivation becomes intractable. Absent this analysis, statistical inference offers a toolkit by which to solve the inverse problem by identifying, at least approximately, the distribution of parameters that produce computations in a biologically realistic model (Foster et al., 1993; Prinz et al., 2004; Achard and De Schutter, 2006; Fisher et al., 2013; O'Leary et al., 2014; Alonso and Marder, 2019).

Statistical inference, of course, requires quantification of the sometimes vague term computation. In neuroscience, two perspectives are dominant. First, often we directly use an exemplar dataset: a collection of samples that express the computation of interest, this data being gathered either experimentally in the lab or from a computer simulation. Although a natural choice given its connection to experiment (Paninski and Cunningham, 2018), some drawbacks exist: these data are well known to have features irrelevant to the computation of interest (Niell and Stryker, 2010; Saleem et al., 2013; Musall et al., 2019), confounding inferences made on such data. Related to this point, use of a conventional dataset encourages conventional data likelihoods or loss functions, which focus on some global metric like squared error or marginal evidence, rather than the computation itself.

Alternatively, researchers often quantify an emergent property (EP): a statistic of data that directly quantifies the computation of interest, wherein the dataset is implicit. While such a choice may seem esoteric, it is not: the above ‘gold standard’ examples (Hopfield, 1982; Sompolinsky et al., 1988; Olypher and Calabrese, 2007; Tsodyks et al., 1997; Wong and Wang, 2006) all quantify and focus on some derived feature of the data, rather than the data drawn from the model. An emergent property is of course a dataset by another name, but it suggests different approach to solving the same inverse problem: here, we directly specify the desired emergent property – a statistic of data drawn from the model – and the value we wish that property to have, and we set up an optimization program to find the distribution of parameters that produce this computation. This statistical framework is not new: it is intimately connected to the literature on approximate bayesian computation (Beaumont et al., 2002; Marjoram et al., 2003; Sisson et al., 2007), parameter sensitivity analyses (Raue et al., 2009; Karlsson et al., 2012; Hines et al., 2014; Raman et al., 2017), maximum entropy modeling (Elsayed and Cunningham, 2017; Savin and Tkačik, 2017; Młynarski et al., 2020), and approximate bayesian inference (Tran et al., 2017; Gonçalves et al., 2019); we detail these connections in Section 'Related approaches'.

The parameter distributions producing a computation may be curved or multimodal along various parameter axes and combinations. It is by quantifying this complex structure that emergent property inference offers scientific insight. Traditional approximation families (e.g. mean-field or mixture of gaussians) are limited in the distributional structure they may learn. To address such restrictions on expressivity, advances in machine learning have used deep probability distributions as flexible approximating families for such complicated distributions (Rezende and Mohamed, 2015; Papamakarios et al., 2019a) (see Section 'Deep probability distributions and normalizing flows'). However, the adaptation of deep probability distributions to the problem of theoretical circuit analysis requires recent developments in deep learning for constrained optimization (Loaiza-Ganem et al., 2017), and architectural choices for efficient and expressive deep generative modeling (Dinh et al., 2017; Kingma and Dhariwal, 2018). We detail our method, which we call emergent property inference (EPI) in Section 'Emergent property inference via deep generative models'.

Equipped with this method, we demonstrate the capabilities of EPI and present novel theoretical findings from its analysis. First, we show EPI’s ability to handle biologically realistic circuit models using a five-neuron model of the stomatogastric ganglion (Gutierrez et al., 2013): a neural circuit whose parametric degeneracy is closely studied (Goldman et al., 2001). Then, we show EPI’s scalability to high dimensional parameter distributions by inferring connectivities of recurrent neural networks that exhibit stable, yet amplified responses – a hallmark of neural responses throughout the brain (Murphy and Miller, 2009; Hennequin et al., 2014; Bondanelli et al., 2019). In a model of primary visual cortex (Litwin-Kumar et al., 2016; Palmigiano et al., 2020), EPI reveals how the recurrent processing across different neuron-type populations shapes excitatory variability: a finding that we show is analytically intractable. Finally, we investigated the possible connectivities of a superior colliculus model that allow execution of different tasks on interleaved trials (Duan et al., 2021). EPI discovered a rich distribution containing two connectivity regimes with different solution classes. We queried the deep probability distribution learned by EPI to produce a mechanistic understanding of neural responses in each regime. Intriguingly, the inferred connectivities of each regime reproduced results from optogenetic inactivation experiments in markedly different ways. These theoretical insights afforded by EPI illustrate the value of deep inference for the interrogation of neural circuit models.

## Results

### Motivating emergent property inference of theoretical models

Consideration of the typical workflow of theoretical modeling clarifies the need for emergent property inference. First, one designs or chooses an existing circuit model that, it is hypothesized, captures the computation of interest. To ground this process in a well-known example, consider the stomatogastric ganglion (STG) of crustaceans, a small neural circuit which generates multiple rhythmic muscle activation patterns for digestion (Marder and Thirumalai, 2002). Despite full knowledge of STG connectivity and a precise characterization of its rhythmic pattern generation, biophysical models of the STG have complicated relationships between circuit parameters and computation (Goldman et al., 2001; Prinz et al., 2004).

A subcircuit model of the STG (Gutierrez et al., 2013) is shown schematically in Figure 1A. The fast population (f1 and f2) represents the subnetwork generating the pyloric rhythm and the slow population (s1 and s2) represents the subnetwork of the gastric mill rhythm. The two fast neurons mutually inhibit one another, and spike at a greater frequency than the mutually inhibiting slow neurons. The hub neuron couples with either the fast or slow population, or both depending on modulatory conditions. The jagged connections indicate electrical coupling having electrical conductance $g_{el}$, smooth connections in the diagram are inhibitory synaptic projections having strength $g_{synA}$ onto the hub neuron, and $g_{synB}=5$ nS for mutual inhibitory connections. Note that the behavior of this model will be critically dependent on its parameterization – the choices of conductance parameters $𝐳=[g_{el},g_{synA}]$.

![Figure 1.](https://cdn.elifesciences.org/articles/56265/elife-56265-fig1-v2.jpg)

**Figure 1.:** (A) Conductance-based subcircuit model of the STG. (B) Spiking frequency $\omega⁢(𝐱;𝐳)$ is an emergent property statistic. Simulated at $g_{el}=4.5$ nS and $g_{synA}=3$ nS. (C) The emergent property of intermediate hub frequency. Simulated activity traces are colored by log probability of generating parameters in the EPI distribution (Panel E). (D) For a choice of circuit model and emergent property, EPI learns a deep probability distribution of parameters $𝐳$. (E) The EPI distribution producing intermediate hub frequency. Samples are colored by log probability density. Contours of hub neuron frequency error are shown at levels of 0.525, 0.53, … 0.575 Hz (dark to light gray away from mean). Dimension of sensitivity $𝐯_{1}$ (solid arrow) and robustness $𝐯_{2}$ (dashed arrow). (F) (Top) The predictions of the EPI distribution. The black and gray dashed lines show the mean and two standard deviations according the emergent property. (Bottom) Simulations at the starred parameter values.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/56265/elife-56265-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) Two-dimensional linear dynamical system model, where real entries of the dynamics matrix $A$ are the parameters. (B) The EPI distribution for a two-dimensional linear dynamical system with $\tau=1$ that produces an average of 1 Hz oscillations with some small amount of variance. Dashed lines indicate the parameter axes. (C) Entropy throughout the optimization. At the beginning of each augmented lagrangian epoch ($i_{max}=2,000$ iterations), the entropy dipped due to the shifted optimization manifold where emergent property constraint satisfaction is increasingly weighted. (D) Emergent property moments throughout optimization. At the beginning of each augmented lagrangian epoch, the emergent property moments adjust closer to their constraints.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/56265/elife-56265-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** (A) Probability contours in the $a_{1,1}$-$a_{2,2}$ plane were derived from the relationship to emergent property statistic of growth/decay factor $real⁢(\lambda_{1})$. (B) Probability contours in the $a_{1,2}$-$a_{2,1}$ plane were derived from the emergent property statistic of oscillation frequency $2⁢\pi⁢imag⁢(\lambda_{1})$.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/56265/elife-56265-fig1-figsupp3-v2.jpg)

**Figure 1—figure supplement 3.:** Sampled dynamical systems $𝐳∼q_{𝜽}⁢(𝐳∣𝒳)$ and their simulated activity from $𝐱(t=0)=[\frac{\sqrt{2}}{2},-\frac{\sqrt{2}}{2}]$ colored by log probability.(A) Each dimension of the simulated trajectories throughout time. (B) The simulated trajectories in phase space.

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/56265/elife-56265-fig1-figsupp4-v2.jpg)

**Figure 1—figure supplement 4.:** (A) Entropy throughout optimization. (B) The emergent property statistic means and variances converge to their constraints at 25,000 iterations following the fifth augmented lagrangian epoch.

Second, once the model is selected, one must specify what the model should produce. In this STG model, we are concerned with neural spiking frequency, which emerges from the dynamics of the circuit model (Figure 1B). An emergent property studied by Gutierrez et al. is the hub neuron firing at an intermediate frequency between the intrinsic spiking rates of the fast and slow populations. This emergent property (EP) is shown in Figure 1C at an average frequency of 0.55 Hz. To be precise, we define intermediate hub frequency not strictly as 0.55 Hz, but frequencies of moderate deviation from 0.55 Hz between the fast (.35Hz) and slow (.68Hz) frequencies.

Third, the model parameters producing the emergent property are inferred. By precisely quantifying the emergent property of interest as a statistical feature of the model, we use emergent property inference (EPI) to condition directly on this emergent property. Before presenting technical details (in the following section), let us understand emergent property inference schematically. EPI (Figure 1D) takes, as input, the model and the specified emergent property, and as its output, returns the parameter distribution (Figure 1E). This distribution – represented for clarity as samples from the distribution – is a parameter distribution constrained such that the circuit model produces the emergent property. Once EPI is run, the returned distribution can be used to efficiently generate additional parameter samples. Most importantly, the inferred distribution can be efficiently queried to quantify the parametric structure that it captures. By quantifying the parametric structure governing the emergent property, EPI informs the central question of this inverse problem: what aspects or combinations of model parameters have the desired emergent property?

### Emergent property inference via deep generative models

EPI formalizes the three-step procedure of the previous section with deep probability distributions (Rezende and Mohamed, 2015; Papamakarios et al., 2019a). First, as is typical, we consider the model as a coupled set of noisy differential equations. In this STG example, the model activity (or state) $𝐱=[x_{f1},x_{f2},x_{hub},x_{s1},x_{s2}]$ is the membrane potential for each neuron, which evolves according to the biophysical conductance-based equation:

$$
C_{m}\frac{dx(t)}{dt}=−h(x(t);z)+dB
$$

where $C_{m}$ = 1nF, and $𝐡$ is a sum of the leak, calcium, potassium, hyperpolarization, electrical, and synaptic currents, all of which have their own complicated dependence on activity $𝐱$ and parameters $𝐳=[g_{el},g_{synA}]$, and $d⁢𝐁$ is white gaussian noise (Gutierrez et al., 2013; see Section 'STG model' for more detail).

Second, we determine that our model should produce the emergent property of ‘intermediate hub frequency’ (Figure 1C). We stipulate that the hub neuron’s spiking frequency – denoted by statistic $\omega_{hub}⁢(𝐱)$ – is close to a frequency of 0.55 Hz, between that of the slow and fast frequencies. Mathematically, we define this emergent property with two constraints: that the mean hub frequency is 0.55 Hz,

$$
E_{z,x}[\omega_{hub}(x;z)]=0.55
$$

and that the variance of the hub frequency is moderate

$$
Var_{z,x}[\omega_{hub}(x;z)]=0.025^{2}.
$$

In the emergent property of intermediate hub frequency, the statistic of hub neuron frequency is an expectation over the distribution of parameters $𝐳$ and the distribution of the data $𝐱$ that those parameters produce. We define the emergent property $𝒳$ as the collection of these two constraints. In general, an emergent property is a collection of constraints on statistical moments that together define the computation of interest.

Third, we perform emergent property inference: we find a distribution over parameter configurations $𝐳$ of models that produce the emergent property; in other words, they satisfy the constraints introduced in Equations 2 and 3. This distribution will be chosen from a family of probability distributions $𝒬={q_{𝜽}⁢(𝐳):𝜽\inΘ}$, defined by a deep neural network (Rezende and Mohamed, 2015; Papamakarios et al., 2019a; Figure 1D, EPI box). Deep probability distributions map a simple random variable $𝐳_{0}$ (e.g. an isotropic gaussian) through a deep neural network with weights and biases $𝜽$ to parameters $𝐳=g_{𝜽}⁢(𝐳_{0})$ of a suitably complicated distribution (see Section 'Deep probability distributions and normalizing flows' for more details). Many distributions in $𝒬$ will respect the emergent property constraints, so we select the most random (highest entropy) distribution, which also means this approach is equivalent to bayesian variational inference (see Section 'EPI as variational inference'). In EPI optimization, stochastic gradient steps in $𝜽$ are taken such that entropy is maximized, and the emergent property $𝒳$ is produced (see Section 'Emergent property inference (EPI)'). We then denote the inferred EPI distribution as $q_{𝜽}⁢(𝐳∣𝒳)$, since the structure of the learned parameter distribution is determined by weights and biases $𝜽$, and this distribution is conditioned upon emergent property $𝒳$.

The structure of the inferred parameter distributions of EPI can be analyzed to reveal key information about how the circuit model produces the emergent property. As probability in the EPI distribution decreases away from the mode of $q_{𝜽}⁢(𝐳∣𝒳)$ (Figure 1E yellow star), the emergent property deteriorates. Perturbing $𝐳$ along a dimension in which $q_{𝜽}⁢(𝐳∣𝒳)$ changes little will not disturb the emergent property, making this parameter combination robust with respect to the emergent property. In contrast, if $𝐳$ is perturbed along a dimension with strongly decreasing $q_{𝜽}⁢(𝐳∣𝒳)$, that parameter combination is deemed sensitive (Raue et al., 2009; Raman et al., 2017). By querying the second-order derivative (Hessian) of $log⁡q_{𝜽}⁢(𝐳∣𝒳)$ at a mode, we can quantitatively identify how sensitive (or robust) each eigenvector is by its eigenvalue; the more negative, the more sensitive and the closer to zero, the more robust (see Section 'Hessian sensitivity vectors'). Indeed, samples equidistant from the mode along these dimensions of sensitivity ($𝐯_{1}$, smaller eigenvalue) and robustness ($𝐯_{2}$, greater eigenvalue) (Figure 1E, arrows) agree with error contours (Figure 1E contours) and have diminished or preserved hub frequency, respectively (Figure 1F activity traces). The directionality of $𝐯_{2}$ suggests that changes in conductance along this parameter combination will most preserve hub neuron firing between the intrinsic rates of the pyloric and gastric mill rhythms. Importantly and unlike alternative techniques, once an EPI distribution has been learned, the modes and Hessians of the distribution can be measured with trivial computation (see Section 'Deep probability distributions and normalizing flows').

In the following sections, we demonstrate EPI on three neural circuit models across ranges of biological realism, neural system function, and network scale. First, we demonstrate the superior scalability of EPI compared to alternative techniques by inferring high-dimensional distributions of recurrent neural network connectivities that exhibit amplified, yet stable responses. Next, in a model of primary visual cortex (Litwin-Kumar et al., 2016; Palmigiano et al., 2020), we show how EPI discovers parametric degeneracy, revealing how input variability across neuron types affects the excitatory population. Finally, in a model of superior colliculus (Duan et al., 2021), we used EPI to capture multiple parametric regimes of task switching, and queried the dimensions of parameter sensitivity to characterize each regime.

### Scaling inference of recurrent neural network connectivity with EPI

To understand how EPI scales in comparison to existing techniques, we consider recurrent neural networks (RNNs). Transient amplification is a hallmark of neural activity throughout cortex and is often thought to be intrinsically generated by recurrent connectivity in the responding cortical area (Murphy and Miller, 2009; Hennequin et al., 2014; Bondanelli et al., 2019). It has been shown that to generate such amplified, yet stabilized responses, the connectivity of RNNs must be non-normal (Goldman, 2009; Murphy and Miller, 2009), and satisfy additional constraints (Bondanelli and Ostojic, 2020). In theoretical neuroscience, RNNs are optimized and then examined to show how dynamical systems could execute a given computation (Sussillo, 2014; Barak, 2017), but such biologically realistic constraints on connectivity (Goldman, 2009; Murphy and Miller, 2009; Bondanelli and Ostojic, 2020) are ignored for simplicity or because constrained optimization is difficult. In general, access to distributions of connectivity that produce theoretical criteria like stable amplification, chaotic fluctuations (Sompolinsky et al., 1988), or low tangling (Russo et al., 2018) would add scientific value to existing research with RNNs. Here, we use EPI to learn RNN connectivities producing stable amplification, and demonstrate the superior scalability and efficiency of EPI to alternative approaches.

We consider a rank-2 RNN with $N$ neurons having connectivity $W=U⁢V^{⊤}$ and dynamics

$$
\tau⁢𝐱˙=-𝐱+W⁢𝐱,
$$

where $U=[𝐔_{1}𝐔_{2}]+g⁢χ^{(U)}$, $V=[𝐕_{1}𝐕_{2}]+g⁢χ^{(V)}$, $𝐔_{1}⁢𝐔_{2},𝐕_{1},𝐕_{2}\in[-1,1]^{N}$, and $χ_{i,j}^{(U)},χ_{i,j}^{(V)}∼𝒩⁢(0,1)$. We infer connectivity parameters $𝐳=[𝐔_{1},𝐔_{2},𝐕_{1},𝐕_{2}]$ that produce stable amplification. Two conditions are necessary and sufficient for RNNs to exhibit stable amplification (Bondanelli and Ostojic, 2020): $real⁢(\lambda_{1})<1$ and $\lambda_{1}^{s}>1$, where $\lambda_{1}$ is the eigenvalue of $W$ with greatest real part and $\lambda^{s}$ is the maximum eigenvalue of $W^{s}=\frac{W+W^{⊤}}{2}$. RNNs with $real⁢(\lambda_{1})=0.5\pm0.5$ and $\lambda_{1}^{s}=1.5\pm0.5$ will be stable with modest decay rate ($real⁢(\lambda_{1})$ close to its upper bound of 1) and exhibit modest amplification ($\lambda_{1}^{s}$ close to its lower bound of 1). EPI can naturally condition on this emergent property

$$
𝒳:E_{z,x}[real(\lambda_{1})\lambda_{1}^{s}]=[0.51.5]Var_{z,x}[real(\lambda_{1})\lambda_{1}^{s}]=[0.25^{2}0.25^{2}].
$$

Variance constraints predicate that the majority of the distribution (within two standard deviations) are within the specified ranges.

For comparison, we infer the parameters $𝐳$ likely to produce stable amplification using two alternative simulation-based inference approaches. Sequential Monte Carlo approximate bayesian computation (SMC-ABC) (Sisson et al., 2007) is a rejection sampling approach that uses SMC techniques to improve efficiency, and sequential neural posterior estimation (SNPE) (Gonçalves et al., 2019) approximates posteriors with deep probability distributions (see Section 'Related approaches'). Unlike EPI, these statistical inference techniques do not constrain the predictions of the inferred distribution, so they were run by conditioning on an exemplar dataset $𝐱_{0}=𝝁$, following standard practice with these methods (Sisson et al., 2007; Gonçalves et al., 2019). To compare the efficiency of these different techniques, we measured the time and number of simulations necessary for the distance of the predictive mean to be less than 0.5 from $𝝁=𝐱_{0}$ (see Section 'Scaling EPI for stable amplification in RNNs').

As the number of neurons $N$ in the RNN, and thus the dimension of the parameter space $𝐳\in[-1,1]^{4⁢N}$, is scaled, we see that EPI converges at greater speed and at greater dimension than SMC-ABC and SNPE (Figure 2A). It also becomes most efficient to use EPI in terms of simulation count at $N=50$ (Figure 2B). It is well known that ABC techniques struggle in parameter spaces of modest dimension (Sisson et al., 2018), yet we were careful to assess the scalability of SNPE, which is a more closely related methodology to EPI. Between EPI and SNPE, we closely controlled the number of parameters in deep probability distributions by dimensionality (Figure 2—figure supplement 1), and tested more aggressive SNPE hyperparameter choices when SNPE failed to converge (Figure 2—figure supplement 2). In this analysis, we see that deep inference techniques EPI and SNPE are far more amenable to inference of high dimensional RNN connectivities than rejection sampling techniques like SMC-ABC, and that EPI outperforms SNPE in both wall time (elapsed real time) and simulation count.

![Figure 2.](https://cdn.elifesciences.org/articles/56265/elife-56265-fig2-v2.jpg)

**Figure 2.:** (A) Wall time of EPI (blue), SNPE (orange), and SMC-ABC (green) to converge on RNN connectivities producing stable amplification. Each dot shows convergence time for an individual random seed. For reference, the mean wall time for EPI to achieve its full constraint convergence (means and variances) is shown (blue line). (B) Simulation count of each algorithm to achieve convergence. Same conventions as A. (C) The predictive distributions of connectivities inferred by EPI (blue), SNPE (orange), and SMC-ABC (green), with reference to $𝐱_{0}=𝝁$ (gray star). (D) Simulations of networks inferred by each method ($\tau=100⁢m⁢s$). Each trace (15 per algorithm) corresponds to simulation of one $z$. (Below) Ratio of obtained samples producing stable amplification, stable monotonic decay, and instability.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/56265/elife-56265-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Number of parameters in deep probability distribution architectures of EPI (blue) and SNPE (orange) by RNN size ($N$).

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/56265/elife-56265-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** SNPE convergence was enabled by increasing $n_{round}$, not $n_{atom}$.(A) Difference of mean predictions $𝐱_{0}$ throughout optimization at $N=50$ with by simulation count (left) and wall time (right) of SNPE with $n_{round}=5,000$ (light orange), SNPE with $n_{round}=25,000$ (dark orange), and EPI (blue). Each line shows an individual random seed. (B) Same conventions as A at $N=100$ of SNPE with $n_{atom}=100$ (light orange) and $n_{atom}=1,000$ (dark orange). (C) Same conventions as A at $N=100$ of SNPE with $n_{round}=25,000$ (light orange) and $n_{round}=250,000$ (dark orange).

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/56265/elife-56265-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** (A) Predictive distribution of EPI (blue) and SNPE (orange) inferred connectivity of RNNs exhibiting stable amplification with $N=2$ (top), $N=10$ (bottom), $g=0.01$ (left), and $g=0.1$ (right). (B) Entropy of parameter distribution approximations throughout optimization with $N=2$ (top), $N=10$ (bottom), $g=0.1$ (dark shade), and $g=0.01$ (light shade). (C) Validation log probabilities throughout SNPE optimization. Same conventions as B. (D) Adherence to EPI constraints. Same conventions as B.

No matter the number of neurons, EPI always produces connectivity distributions with mean and variance of $real⁢(\lambda_{1})$ and $\lambda_{1}^{s}$ according to $𝒳$ (Figure 2C, blue). For the dimensionalities in which SMC-ABC is tractable, the inferred parameters are concentrated and offset from the exemplar dataset $𝐱_{0}$ (Figure 2C, green). When using SNPE, the predictions of the inferred parameters are highly concentrated at some RNN sizes and widely varied in others (Figure 2C, orange). We see these properties reflected in simulations from the inferred distributions: EPI produces a consistent variety of stable, amplified activity norms $|𝐱⁢(t)|$, SMC-ABC produces a limited variety of responses, and the changing variety of responses from SNPE emphasizes the control of EPI on parameter predictions (Figure 2D). Even for moderate neuron counts, the predictions of the inferred distribution of SNPE are highly dependent on $N$ and $g$, while EPI maintains the emergent property across choices of RNN (see Section 'Effect of RNN parameters on EPI and SNPE inferred distributions').

To understand these differences, note that EPI outperforms SNPE in high dimensions by using gradient information (from $\nabla_{𝐳}[real(\lambda_{1}),\lambda_{1}^{s}]^{⊤}$). This choice agrees with recent speculation that such gradient information could improve the efficiency of simulation-based inference techniques (Cranmer et al., 2020), as well as reflecting the classic tradeoff between gradient-based and sampling-based estimators (scaling and speed versus generality). Since gradients of the emergent property are necessary in EPI optimization, gradient tractability is a key criteria when determining the suitability of a simulation-based inference technique. If the emergent property gradient is efficiently calculated, EPI is a clear choice for inferring high dimensional parameter distributions. In the next two sections, we use EPI for novel scientific insight by examining the structure of inferred distributions.

### EPI reveals how recurrence with multiple inhibitory subtypes governs excitatory variability in a V1 model

Dynamical models of excitatory (E) and inhibitory (I) populations with supralinear input-output function have succeeded in explaining a host of experimentally documented phenomena in primary visual cortex (V1). In a regime characterized by inhibitory stabilization of strong recurrent excitation, these models give rise to paradoxical responses (Tsodyks et al., 1997), selective amplification (Goldman, 2009; Murphy and Miller, 2009), surround suppression (Ozeki et al., 2009), and normalization (Rubin et al., 2015). Recent theoretical work (Hennequin et al., 2018) shows that stabilized E-I models reproduce the effect of variability suppression (Churchland et al., 2010). Furthermore, experimental evidence shows that inhibition is composed of distinct elements – parvalbumin (P), somatostatin (S), VIP (V) – composing 80% of GABAergic interneurons in V1 (Markram et al., 2004; Rudy et al., 2011; Tremblay et al., 2016), and that these inhibitory cell types follow specific connectivity patterns (Figure 3A; Pfeffer et al., 2013). Here, we use EPI on a model of V1 with biologically realistic connectivity to show how the structure of input across neuron types affects the variability of the excitatory population – the population largely responsible for projecting to other brain areas (Felleman and Van Essen, 1991).

![Figure 3.](https://cdn.elifesciences.org/articles/56265/elife-56265-fig3-v2.jpg)

**Figure 3.:** (A) Four-population model of primary visual cortex with excitatory (black), parvalbumin (blue), somatostatin (red), and VIP (green) neurons (excitatory and inhibitory projections filled and unfilled, respectively). Some neuron-types largely do not form synaptic projections to others ($|(W_{\alpha_{1},\alpha_{2}})|<0.025$). Each neural population receives a baseline input $𝐡_{b}$, and the E- and P-populations also receive a contrast-dependent input $𝐡_{c}$. Additionally, each neural population receives a slow noisy input $ϵ$. (B) Transient network responses of the SSSN model. Traces are independent trials with varying initialization $𝐱⁢(0)$ and noise $ϵ$. (C) Mean (solid line) and standard deviation $s_{E}⁢(𝐱;𝐳)$ (shading) across 100 trials. (D) EPI distribution of noise parameters $𝐳$ conditioned on E-population variability. The EPI predictive distribution of $s_{E}⁢(𝐱;𝐳)$ is show on the bottom-left. (E) (Top) Enlarged visualization of the $\sigma_{E}$-$\sigma_{P}$ marginal distribution of EPI $q_{𝜽}⁢(𝐳∣𝒳⁢(5⁢Hz))$ and $q_{𝜽}⁢(𝐳∣𝒳⁢(10⁢Hz))$. Each black dot shows the mode at each $\sigma_{P}$. The arrows show the most sensitive dimensions of the Hessian evaluated at these modes. (F) The predictive distributions of $\sigma_{E}^{2}+\sigma_{P}^{2}$ of each inferred distribution $q_{𝜽}⁢(𝐳∣𝒳⁢(5⁢Hz))$ and $q_{𝜽}⁢(𝐳∣𝒳⁢(10⁢Hz))$.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/56265/elife-56265-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** EPI inferred distribution for $𝒳⁢(10⁢Hz)$.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/56265/elife-56265-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** (A) Entropy throughout optimization. (B) The emergent property statistic means and variances converge to their constraints at 8000 iterations following the fourth augmented lagrangian epoch.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/56265/elife-56265-fig3-figsupp3-v2.jpg)

![Figure 3—figure supplement 4.](https://cdn.elifesciences.org/articles/56265/elife-56265-fig3-figsupp4-v2.jpg)

We considered response variability of a nonlinear dynamical V1 circuit model (Figure 3A) with a state comprised of each neuron-type population’s rate $𝐱=[x_{E},x_{P},x_{S},x_{V}]^{⊤}$. Each population receives recurrent input $W⁢𝐱$, where $W$ is the effective connectivity matrix (see Section 'Primary visual cortex') and an external input with mean $𝐡$, which determines population rate via supralinear nonlinearity $ϕ(⋅)=[⋅]_{+}^{2}$. The external input has an additive noisy component $ϵ$ with variance $𝝈^{2}=[\sigma_{E}^{2},\sigma_{P}^{2},\sigma_{S}^{2},\sigma_{V}^{2}]$. This noise has a slower dynamical timescale $\tau_{noise}>\tau$ than the population rate, allowing fluctuations around a stimulus-dependent steady-state (Figure 3B). This model is the stochastic stabilized supralinear network (SSSN) (Hennequin et al., 2018)

$$
\tau⁢\frac{d⁢𝐱}{d⁢t}=-𝐱+ϕ⁢(W⁢𝐱+𝐡+ϵ),
$$

generalized to have multiple inhibitory neuron types. It introduces stochasticity to four neuron-type models of V1 (Litwin-Kumar et al., 2016). Stochasticity and inhibitory multiplicity introduce substantial complexity to the mathematical treatment of this problem (see Section 'Primary visual cortex: Mathematical intuition and challenges') motivating the analysis of this model with EPI. Here, we consider fixed weights $W$ and input $𝐡$ (Palmigiano et al., 2020), and study the effect of input variability $𝐳=[\sigma_{E},\sigma_{P},\sigma_{S},\sigma_{V}]^{⊤}$ on excitatory variability.

We quantify levels of E-population variability by studying two emergent properties

$$
𝒳(5Hz):E_{z,x}s_{E}(x;z)=5Hz𝒳(10Hz):E_{z,x}s_{E}(x;z)=10HzVar_{z,x}s_{E}(x;z)=1Hz^{2}Var_{z,x}s_{E}(x;z)=1Hz^{2},
$$

where $s_{E}(x;z)$ is the standard deviation of the stochastic $E$-population response about its steady state (Figure 3C). In the following analyses, we select 1 Hz2 variance such that the two emergent properties do not overlap in $s_{E}⁢(𝐳;𝐱)$.

First, we ran EPI to obtain parameter distribution $q_{𝜽}⁢(𝐳∣𝒳⁢(5⁢Hz))$ producing E-population variability around 5 Hz (Figure 3D). From the marginal distribution of $\sigma_{E}$ and $\sigma_{P}$ (Figure 3D, top-left), we can see that $s_{E}⁢(𝐱;𝐳)$ is sensitive to various combinations of $\sigma_{E}$ and $\sigma_{P}$. Alternatively, both $\sigma_{S}$ and $\sigma_{V}$ are degenerate with respect to $s_{E}⁢(𝐱;𝐳)$ evidenced by the unexpectedly high variability in those dimensions (Figure 3D, bottom-right). Together, these observations imply a curved path with respect to $s_{E}⁢(𝐱;𝐳)$ of 5 Hz, which is indicated by the modes along $\sigma_{P}$ (Figure 3E).

Figure 3E suggests a quadratic relationship in E-population fluctuations and the standard deviation of E- and P-population input; as the square of either $\sigma_{E}$ or $\sigma_{P}$ increases, the other compensates by decreasing to preserve the level of $s_{E}⁢(𝐱;𝐳)$. This quadratic relationship is preserved at greater level of E-population variability $𝒳⁢(10⁢Hz)$ (Figure 3E and Figure 3—figure supplement 1). Indeed, the sum of squares of $\sigma_{E}$ and $\sigma_{P}$ is larger in $q_{𝜽}⁢(𝐳∣𝒳⁢(10⁢Hz))$ than $q_{𝜽}⁢(𝐳∣𝒳⁢(5⁢Hz))$ (Figure 3F, $p<1\times10^{-10}$), while the sum of squares of $\sigma_{S}$ and $\sigma_{V}$ are not significantly different in the two EPI distributions (Figure 3—figure supplement 3, $p=.40$), in which parameters were bounded from 0 to 0.5. The strong interaction between E- and P-population input variability on excitatory variability is intriguing, since this circuit exhibits a paradoxical effect in the P-population (and no other inhibitory types) (Figure 3—figure supplement 4), meaning that the E-population is P-stabilized. Future research may uncover a link between the population of network stabilization and compensatory interactions governing excitatory variability.

EPI revealed the quadratic dependence of excitatory variability on input variability to the E- and P-populations, as well as its independence to input from the other two inhibitory populations. In a simplified model ($\tau=\tau_{noise}$), it can be shown that surfaces of equal variance are ellipsoids as a function of $𝝈$ (see Section 'Primary visual cortex: Mathematical intuition and challenges'). Nevertheless, the sensitive and degenerate parameters are intractable to predict mathematically, since the covariance matrix depends on the steady-state solution of the network (Hennequin et al., 2018; Gardiner, 2009), and terms in the covariance expression increase quadratically with each additional neuron-type population (see also Section 'Primary visual cortex: Mathematical intuition and challenges'). By pointing out this mathematical complexity, we emphasize the value of EPI for gaining understanding about theoretical models when mathematical analysis becomes onerous or impractical.

### EPI identifies two regimes of rapid task switching

It has been shown that rats can learn to switch from one behavioral task to the next on randomly interleaved trials (Duan et al., 2015), and an important question is what neural mechanisms produce this computation. In this experimental setup, rats were given an explicit task cue on each trial, either Pro or Anti. After a delay period, rats were shown a stimulus, and made a context (task) dependent response (Figure 4A). In the Pro task, rats were required to orient toward the stimulus, while in the Anti task, rats were required to orient away from the stimulus. Pharmacological inactivation of the SC impaired rat performance, and time-specific optogenetic inactivation revealed a crucial role for the SC on the cognitively demanding Anti trials (Duan et al., 2021). These results motivated a nonlinear dynamical model of the SC containing four functionally defined neuron-type populations. In Duan et al., 2021, a computationally intensive procedure was used to obtain a set of 373 connectivity parameters that qualitatively reproduced these optogenetic inactivation results. To build upon the insights of this previous work, we use the probabilistic tools afforded by EPI to identify and characterize two linked, yet distinct regimes of rapid task switching connectivity.

![Figure 4.](https://cdn.elifesciences.org/articles/56265/elife-56265-fig4-v2.jpg)

**Figure 4.:** (A) Rapid task switching behavioral paradigm (see text). (B) Model of superior colliculus (SC). Neurons: LP - Left Pro, RP - Right Pro, LA - Left Anti, RA - Right Anti. Parameters: $s⁢W$ - self, $h⁢W$ - horizontal, $v⁢W$ -vertical, $d⁢W$ - diagonal weights. (C) The EPI inferred distribution of rapid task switching networks. Red/purple parameters indicate modes $𝐳^{*}⁢(s⁢W)$ colored by $s⁢W$. Sensitivity vectors $𝐯_{1}⁢(𝐳^{*})$ are shown by arrows. (Bottom-left) EPI predictive distribution of task accuracies. (D) Mean and standard error ($N_{test}$ = 25, bars not visible) of accuracy in Pro (top) and Anti (bottom) tasks after perturbing connectivity away from mode along $𝐯_{1}⁢(𝐳^{*})$ (left), $𝐯_{task}$ (middle), and $𝐯_{diag}$ (right).

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/56265/elife-56265-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A) Same pairplot as Figure 4C colored by Pro-task accuracy. (B) Same as A colored by Anti-task accuracy. (C) Connectivity parameters of EPI distributions versus task accuracies. β is slope coefficient of linear regression, $r$ is correlation, and $p$ is the two-tailed p-value.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/56265/elife-56265-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** (A) Simulations in network regime 1: $𝐳^{*}(sW=-0.75)$. (B) Simulations in network regime 2: $𝐳^{*}(sW=0.75)$.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/56265/elife-56265-fig4-figsupp3-v2.jpg)

**Figure 4—figure supplement 3.:** (A) Invariant eigenvectors of connectivity matrix $W$. (B) Accuracies for connectivity perturbations when changing $\lambda_{all}$ and $\lambda_{side}$ ($\lambda_{task}$ and $\lambda_{diag}$ shown in Figure 4D).

![Figure 4—figure supplement 4.](https://cdn.elifesciences.org/articles/56265/elife-56265-fig4-figsupp4-v2.jpg)

**Figure 4—figure supplement 4.:** (A) Entropy throughout optimization. (B) The emergent property statistic means and variances converge to their constraints at 20,000 iterations following the tenth augmented lagrangian epoch.

![Figure 4—figure supplement 5.](https://cdn.elifesciences.org/articles/56265/elife-56265-fig4-figsupp5-v2.jpg)

**Figure 4—figure supplement 5.:** (A) Rapid task switching SC connectivities obtained from random sampling. (B) Task accuracies of the inferred distributions from random sampling (top) and EPI (bottom).

In this SC model, there are Pro- and Anti-populations in each hemisphere (left (L) and right (R)) with activity variables $𝐱=[x_{L⁢P},x_{L⁢A},x_{R⁢P},x_{R⁢A}]^{⊤}$ (Duan et al., 2021). The connectivity of these populations is parameterized by self $s⁢W$, vertical $v⁢W$, diagonal $d⁢W$ and horizontal $h⁢W$ connections (Figure 4B). The input $𝐡$ is comprised of a positive cue-dependent signal to the Pro- or Anti-populations, a positive stimulus-dependent input to either the Left or Right populations, and a choice-period input to the entire network (see Section 'SC model'). Model responses are bounded from 0 to 1 as a function $ϕ$ of an internal variable $𝐮$

$$
\tau\frac{du}{dt}=−u+Wx+h+dBx=ϕ(u).
$$

The model responds to the side with greater Pro neuron activation; for example the response is left if $x_{L⁢P}>x_{R⁢P}$ at the end of the trial. Here, we use EPI to determine the network connectivity $𝐳=[s⁢W,v⁢W,d⁢W,h⁢W]^{⊤}$ that produces rapid task switching.

Rapid task switching is formalized mathematically as an emergent property with two statistics: accuracy in the Pro task $p_{P}⁢(𝐱;𝐳)$ and Anti task $p_{A}⁢(𝐱;𝐳)$. We stipulate that accuracy be on average 0.75 in each task with variance $.075^{2}$

$$
𝒳:E_{z}[p_{P}(x;z)p_{A}(x;z)]=[.75.75]Var_{z}[p_{P}(x;z)p_{A}(x;z)]=[.075^{2}.075^{2}].
$$

Seventy-five percent accuracy is a realistic level of performance in each task, and with the chosen variance, inferred models will not exhibit fully random responses (50%), nor perfect performance (100%).

The EPI inferred distribution (Figure 4C) produces Pro- and Anti-task accuracies (Figure 4C, bottom-left) consistent with rapid task switching (Equation 9). This parameter distribution has rich structure that is not captured well by simple linear correlations (Figure 4—figure supplement 1). Specifically, the shape of the EPI distribution is sharply bent, matching ground truth structure indicated by brute-force sampling (Figure 4—figure supplement 5). This is most saliently observed in the marginal distribution of $s⁢W$-$h⁢W$ (Figure 4C top-right), where anticorrelation between $s⁢W$ and $h⁢W$ switches to correlation with decreasing $s⁢W$. By identifying the modes of the EPI distribution $𝐳^{*}⁢(s⁢W)$ at different values of $s⁢W$ (Figure 4C red/purple dots), we can quantify this change in distributional structure with the sensitivity dimension $𝐯_{1}⁢(𝐳)$ (Figure 4C red/purple arrows). Note that the directionality of these sensitivity dimensions at $𝐳^{*}⁢(s⁢W)$ changes distinctly with $s⁢W$, and are perpendicular to the robust dimensions of the EPI distribution that preserve rapid task switching. These two directionalities of sensitivity motivate the distinction of connectivity into two regimes, which produce different types of responses in the Pro and Anti tasks (Figure 4—figure supplement 2).

When perturbing connectivity along the sensitivity dimension away from the modes

$$
𝐳=𝐳^{*}⁢(s⁢W)+\delta⁢𝐯_{1}⁢(𝐳^{*}⁢(s⁢W)),
$$

Pro-accuracy monotonically increases in both regimes (Figure 4D, top-left). However, there is a stark difference between regimes in Anti-accuracy. Anti-accuracy falls in either direction of $𝐯_{1}$ in regime 1, yet monotonically increases along with Pro accuracy in regime 2 (Figure 4D, bottom-left). The sharp change in local structure of the EPI distribution is therefore explained by distinct sensitivities: Anti-accuracy diminishes in only one or both directions of the sensitivity perturbation.

To understand the mechanisms differentiating the two regimes, we can make connectivity perturbations along dimensions that only modify a single eigenvalue of the connectivity matrix. These eigenvalues $\lambda_{all}$, $\lambda_{side}$, $\lambda_{task}$, and $\lambda_{diag}$ correspond to connectivity eigenmodes with intuitive roles in processing in this task (Figure 4—figure supplement 3A). For example, greater $\lambda_{task}$ will strengthen internal representations of task, while greater $\lambda_{diag}$ will amplify dominance of Pro and Anti pairs in opposite hemispheres (Section 'Connectivity eigendecomposition and processing modes'). Unlike the sensitivity dimension, the dimensions $𝐯_{a}$ that perturb isolated connectivity eigenvalues $\lambda_{a}$ for $a\in{all,side,task,diag}$ are independent of $𝐳^{*}⁢(s⁢W)$ (see Section 'Connectivity eigendecomposition and processing modes'), e.g.

$$
𝐳=𝐳^{*}⁢(s⁢W)+\delta⁢𝐯_{task}.
$$

Connectivity perturbation analyses reveal that decreasing $\lambda_{task}$ has a very similar effect on Anti accuracy as perturbations along the sensitivity dimension (Figure 4D, middle). The similar effects of perturbations along the sensitivity dimension $𝐯_{1}⁢(𝐳^{*})$ and reduction of task eigenvalue (via perturbations along $-𝐯_{task}$) suggest that there is a carefully tuned strength of task representation in connectivity regime 1, which if disturbed results in random Anti-trial responses. Finally, we recognize that increasing $\lambda_{diag}$ has opposite effects on Anti-accuracy in each regime (Figure 4D, right). In the next section, we build on these mechanistic characterizations of each regime by examining their resilience to optogenetic inactivation.

### EPI inferred SC connectivities reproduce results from optogenetic inactivation experiments

During the delay period of this task, the circuit must prepare to execute the correct task according to the presented cue. The circuit must then maintain a representation of task throughout the delay period, which is important for correct execution of the Anti-task. Duan et al. found that bilateral optogenetic inactivation of SC during the delay period consistently decreased performance in the Anti-task, but had no effect on the Pro-task (Figure 5A; Duan et al., 2021). The distribution of connectivities inferred by EPI exhibited this same effect in simulation at high optogenetic strengths γ, which reduce the network activities $𝐱⁢(t)$ by a factor $1-\gamma$ (Figure 5B) (see Section 'Modeling optogenetic silencing').

![Figure 5.](https://cdn.elifesciences.org/articles/56265/elife-56265-fig5-v2.jpg)

**Figure 5.:** (A) Mean and standard error (bars) across recording sessions of task error following delay period optogenetic inactivation in rats. (B) Mean and standard deviation (bars) of task error induced by delay period inactivation of varying optogenetic strength γ across the EPI distribution. (C) (Left) Mean and standard error of Pro and Anti error from regime 1 to regime 2 at $\gamma=0.675$. (Right) Correlations of connectivity eigenvalues with Anti error from regime 1 to regime 2 at $\gamma=0.675$. (D) (Left) Mean and standard deviation (shading) of responses of the SC model at the mode of the EPI distribution to delay period inactivation at $\gamma=0.85$. Accuracy in Pro (top) and Anti (bottom) task is shown as a percentage. (Right) Anti-accuracy following delay period inactivation at $\gamma=0.85$ versus accuracy in the Pro-task across connectivities in the EPI distribution.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/56265/elife-56265-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (Left) Mean and standard error of Pro- and Anti-error from regime 1 to regime 2 at $\gamma=0.85$.(Right) Correlations of connectivity eigenvalues with Anti-error from regime 1 to regime 2 at $\gamma=0.85$.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/56265/elife-56265-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** (Left) Mean and standard deviation (shading) of responses of the SC model at the mode of the EPI distribution to delay period inactivation at $\gamma=0.675$.Accuracy in Pro (top) and Anti (bottom) task is shown as a percentage. (Right) Anti-accuracy following delay period inactivation at $\gamma=0.675$ versus accuracy in the Pro-task across connectivities in the EPI distribution.

To examine how connectivity affects response to delay period inactivation, we grouped connectivities of the EPI distribution along the continuum linking regimes 1 and 2 of Section 'EPI identifies two regimes of rapid task switching'. $Z⁢(s⁢W)$ is the set of EPI samples for which the closest mode was $𝐳^{*}⁢(s⁢W)$ (see Section 'Mode identification with EPI'). In the following analyses, we examine how error, and the influence of connectivity eigenvalue on Anti-error change along this continuum of connectivities. Obtaining the parameter samples for these analysis with the learned EPI distribution was more than 20,000 times faster than a brute force approach (see Section 'Sample grouping by mode').

The mean increase in Anti-error of the EPI distribution is closest to the experimentally measured value of 7% at $\gamma=0.675$ (Figure 5B, black dot). At this level of optogenetic strength, regime 1 exhibits an increase in Anti-error with delay period silencing (Figure 5C, left), while regime 2 does not. In regime 1, greater $\lambda_{task}$ and $\lambda_{diag}$ decrease Anti-error (Figure 5C, right). In other words, stronger task representations and diagonal amplification make the SC model more resilient to delay period silencing in the Anti-task. This complements the finding from Duan et al., 2021 (Duan et al., 2021) that $\lambda_{task}$ and $\lambda_{diag}$ improve Anti accuracy.

At roughly $\gamma=0.85$ (Figure 5B, gray dot), the Anti-error saturates, while Pro-error remains at zero. Following delay period inactivation at this optogenetic strength, there are strong similarities in the responses of Pro- and Anti-trials during the choice period (Figure 5D, left). We interpreted these similarities to suggest that delay period inactivation at this saturated level flips the internal representation of task (from Anti to Pro) in the circuit model. A flipped task representation would explain why the Anti-error saturates at 50%: the average Anti-accuracy in EPI inferred connectivities is 75%, but average Anti accuracy would be 25% (100% - $E_{z}[p_{P}]$) if the internal representation of task is flipped during the delay period.This hypothesis prescribes a model of Anti-accuracy during delay period silencing of $p_{A,opto}=100%-p_{P}$, which is fit closely across both regimes of the EPI inferred connectivities (Figure 5D, right). Similarities between Pro- and Anti-trial responses were not present at the experiment-matching level of $\gamma=0.675$ (Figure 5—figure supplement 2 left) and neither was anticorrelation in $p_{P}$ and $p_{A,opto}$ (Figure 5—figure supplement 2 right).

In summary, the connectivity inferred by EPI to perform rapid task switching replicated results from optogenetic silencing experiments. We found that at levels of optogenetic strength matching experimental levels of Anti-error, only one regime actually exhibited the effect. This connectivity regime is less resilient to optogenetic perturbation, and perhaps more biologically realistic. Finally, we characterized the pathology in Anti-error that occurs in both regimes when optogenetic strength is increased to high levels, leading to a mechanistic hypothesis that is experimentally testable. The probabilistic tools afforded by EPI yielded this insight: we identified two regimes and the continuum of connectivities between them by taking gradients of parameter probabilities in the EPI distribution, we identified sensitivity dimensions by measuring the Hessian of the EPI distribution, and we obtained many parameter samples at each step along the continuum at an efficient rate.

## Discussion

In neuroscience, machine learning has primarily been used to reveal structure in neural datasets (Paninski and Cunningham, 2018). Careful inference procedures are developed for these statistical models allowing precise, quantitative reasoning, which clarifies the way data informs beliefs about the model parameters. However, these statistical models often lack resemblance to the underlying biology, making it unclear how to go from the structure revealed by these methods, to the neural mechanisms giving rise to it. In contrast, theoretical neuroscience has primarily focused on careful models of neural circuits and the production of emergent properties of computation, rather than measuring structure in neural datasets. In this work, we improve upon parameter inference techniques in theoretical neuroscience with emergent property inference, harnessing deep learning towards parameter inference in neural circuit models (see Section 'Related approaches').

Methodology for statistical inference in circuit models has evolved considerably in recent years. Early work used rejection sampling techniques (Beaumont et al., 2002; Marjoram et al., 2003; Sisson et al., 2007), but EPI and another recently developed methodology (Gonçalves et al., 2019) employ deep learning to improve efficiency and provide flexible approximations. SNPE has been used for posterior inference of parameters in circuit models conditioned upon exemplar data used to represent computation, but it does not infer parameter distributions that only produce the computation of interest like EPI (see Section 'Scaling inference of recurrent neural network connectivity with EPI'). When strict control over the predictions of the inferred parameters is necessary, EPI uses a constrained optimization technique (Loaiza-Ganem et al., 2017) (see Section 'Augmented lagrangian optimization') to make inference conditioned on the emergent property possible.

A key difference between EPI and SNPE, is that EPI uses gradients of the emergent property throughout optimization. In Section 'Scaling inference of recurrent neural network connectivity with EPI', we showed that such gradients confer beneficial scaling properties, but a concern remains that emergent property gradients may be too computationally intensive. Even in a case of close biophysical realism with an expensive emergent property gradient, EPI was run successfully on intermediate hub frequency in a five-neuron subcircuit model of the STG (Section 'Motivating emergent property inference of theoretical models'). However, conditioning on the pyloric rhythm (Marder and Selverston, 1992) in a model of the pyloric subnetwork model (Prinz et al., 2004) proved to be prohibitive with EPI. The pyloric subnetwork requires many time steps for simulation and many key emergent property statistics (e.g. burst duration and phase gap) are not calculable or easily approximated with differentiable functions. In such cases, SNPE, which does not require differentiability of the emergent property, has proven useful (Gonçalves et al., 2019). In summary, choice of deep inference technique should consider emergent property complexity and differentiability, dimensionality of parameter space, and the importance of constraining the model behavior predicted by the inferred parameter distribution.

In this paper, we demonstrate the value of deep inference for parameter sensitivity analyses at both the local and global level. With these techniques, flexible deep probability distributions are optimized to capture global structure by approximating the full distribution of suitable parameters. Importantly, the local structure of this deep probability distribution can be quantified at any parameter choice, offering instant sensitivity measurements after fitting. For example, the global structure captured by EPI revealed two distinct parameter regimes, which had different local structure quantified by the deep probability distribution (see Section 'Superior colliculus'). In comparison, bayesian MCMC is considered a popular approach for capturing global parameter structure (Girolami and Calderhead, 2011), but there is no variational approximation (the deep probability distribution in EPI), so sensitivity information is not queryable and sampling remains slow after convergence. Local sensitivity analyses (e.g. Raue et al., 2009) may be performed independently at individual parameter samples, but these methods alone do not capture the full picture in nonlinear, complex distributions. In contrast, deep inference yields a probability distribution that produces a wholistic assessment of parameter sensitivity at the local and global level, which we used in this study to make novel insights into a range of theoretical models. Together, the abilities to condition upon emergent properties, the efficient inference algorithm, and the capacity for parameter sensitivity analyses make EPI a useful method for addressing inverse problems in theoretical neuroscience.

### Code availability statement

All software written for this study is available at https://github.com/cunningham-lab/epi (copy archived at swh:1:rev:38febae7035ca921334a616b0f396b3767bf18d4), Bittner, 2021.

## Materials and methods

### Emergent property inference (EPI)

Solving inverse problems is an important part of theoretical neuroscience, since we must understand how neural circuit models and their parameter choices produce computations. Recently, research on machine learning methodology for neuroscience has focused on finding latent structure in large-scale neural datasets, while research in theoretical neuroscience generally focuses on developing precise neural circuit models that can produce computations of interest. By quantifying computation into an emergent property through statistics of the emergent activity of neural circuit models, we can adapt the modern technique of deep probabilistic inference towards solving inverse problems in theoretical neuroscience. Here, we introduce a novel method for statistical inference, which uses deep networks to learn parameter distributions constrained to produce emergent properties of computation.

Consider model parameterization $𝐳$, which is a collection of scientifically meaningful variables that govern the complex simulation of data $𝐱$. For example (see Section 'Motivating emergent property inference of theoretical models'), $𝐳$ may be the electrical conductance parameters of an STG subcircuit, and $𝐱$ the evolving membrane potentials of the five neurons. In terms of statistical modeling, this circuit model has an intractable likelihood $p⁢(𝐱∣𝐳)$, which is predicated by the stochastic differential equations that define the model. From a theoretical perspective, we are less concerned about the likelihood of an exemplar dataset $𝐱$, but rather the emergent property of intermediate hub frequency (which implies a consistent dataset $𝐱$).

In this work, emergent properties $𝒳$ are defined through the choice of emergent property statistic $f⁢(𝐱;𝐳)$ (which is a vector of one or more statistics), and its means $𝝁$, and variances $𝝈^{2}$:

$$
𝒳:𝔼_{𝐳,𝐱}⁢[f⁢(𝐱;𝐳)]=𝝁,Var_{𝐳,𝐱}⁢[f⁢(𝐱;𝐳)]=𝝈^{2}.
$$

In general, an emergent property may be a collection of first-, second-, or higher-order moments of a group of statistics, but this study focuses on the case written in Equation 12. In the STG example, intermediate hub frequency is defined by mean and variance constraints on the statistic of hub neuron frequency $\omega_{hub}⁢(𝐱;𝐳)$ (Equations 2 and 3). Precisely, the emergent property statistics $f⁢(𝐱;𝐳)$ must have means $𝝁$ and variances $𝝈^{2}$ over the EPI distribution of parameters ($𝐳∼q_{𝜽}⁢(𝐳)$) and the data produced by those parameters ($𝐱∼p⁢(𝐱∣𝐳)$), where the inferred parameter distribution $q_{𝜽}⁢(𝐳)$ itself is parameterized by deep network weights and biases $𝜽$.

In EPI, a deep probability distribution $q_{𝜽}⁢(𝐳)$ is optimized to approximate the parameter distribution producing the emergent property $𝒳$. In contrast to simpler classes of distributions like the gaussian or mixture of gaussians, deep probability distributions are far more flexible and capable of fitting rich structure (Rezende and Mohamed, 2015; Papamakarios et al., 2019a). In deep probability distributions, a simple random variable $𝐳_{0}∼q_{0}⁢(𝐳_{0})$ (we choose an isotropic gaussian) is mapped deterministically via a sequence of deep neural network layers (g1, . gl) parameterized by weights and biases $𝜽$ to the support of the distribution of interest:

$$
z=g_{\theta}(z_{0})=g_{l}(...g_{1}(z_{0}))∼q_{\theta}(z).
$$

Such deep probability distributions embed the inferred distribution in a deep network. Once optimized, this deep network representation of a distribution has remarkably useful properties: fast sampling and probability evaluations. Importantly, fast probability evaluations confer fast gradient and Hessian calculations as well.

Given this choice of circuit model and emergent property $𝒳$, $q_{𝜽}⁢(𝐳)$ is optimized via the neural network parameters $𝜽$ to find a maximally entropic distribution $q_{𝜽}^{*}$ within the deep variational family $𝒬={q_{𝜽}⁢(𝐳):𝜽\inΘ}$ that produces the emergent property $𝒳$:

$$
q_{\theta}(z∣𝒳)=q_{\theta}^{∗}(z)argmaxq_{\theta}\inQ H(q_{\theta}(z))s.t. 𝒳  :  E_{z,x}[f(x;z)]=\mu,Var_{z,x}[f(x;z)]=\sigma^{2},
$$

where $H⁢(q_{𝜽}⁢(𝐳))=𝔼_{𝐳}⁢[-log⁡q_{𝜽}⁢(z)]$ is entropy. By maximizing the entropy of the inferred distribution $q_{𝜽}$, we select the most random distribution in family $𝒬$ that satisfies the constraints of the emergent property. Since entropy is maximized in Equation 14, EPI is equivalent to bayesian variational inference (see Section 'EPI as variational inference'), which is why we specify the inferred distribution of EPI as conditioned upon emergent property $𝒳$ with the notation $q_{𝜽}⁢(𝐳∣𝒳)$. To run this constrained optimization, we use an augmented lagrangian objective, which is the standard approach for constrained optimization (Bertsekas, 2014), and the approach taken to fit Maximum Entropy Flow Networks (MEFNs) (Loaiza-Ganem et al., 2017). This procedure is detailed in Section 'Augmented lagrangian optimization' and the pseudocode in Algorithm 'Augmented lagrangian optimization'.

In the remainder of Section 'Emergent property inference (EPI)', we will explain the finer details and motivation of the EPI method. First, we explain related approaches and what EPI introduces to this domain (Section 'Related approaches'). Second, we describe the special class of deep probability distributions used in EPI called normalizing flows (Section 'Deep probability distributions and normalizing flows'). Then, we establish the known relationship between maximum entropy distributions and exponential families (Section 'Maximum entropy distributions and exponential families'). Next, we explain the constrained optimization technique used to solve Equation 14 (Section 'Augmented lagrangian optimization'). Then, we demonstrate the details of this optimization in a toy example (Section 'Example: 2D LDS'). Finally, we explain how EPI is equivalent to variational inference (Section 'EPI as variational inference').

#### Related approaches

When bayesian inference problems lack conjugacy, scientists use approximate inference methods like variational inference (VI) (Saul and Jordan, 1998) and Markov chain Monte Carlo (MCMC) (Metropolis et al., 1953; Hastings, 1970). After optimization, variational methods return a parameterized posterior distribution, which we can analyze. Also, the variational approximation is often chosen such that it permits fast sampling. In contrast MCMC methods only produce samples from the approximated posterior distribution. No parameterized distribution is estimated, and additional samples are always generated with the same sampling complexity. Inference in models defined by systems of differential has been demonstrated with MCMC (Girolami and Calderhead, 2011), although this approach requires tractable likelihoods. Advancements have introduced sampling (Calderhead and Girolami, 2011), likelihood approximation (Golightly and Wilkinson, 2011), and uncertainty quantification techniques (Chkrebtii et al., 2016) to make MCMC approaches more efficient and expand the class of applicable models.

Simulation-based inference (Cranmer et al., 2020) is model parameter inference in the absence of a tractable likelihood function. The most prevalent approach to simulation-based inference is approximate bayesian computation (ABC) (Beaumont et al., 2002), in which satisfactory parameter samples are kept from random prior sampling according to a rejection heuristic. The obtained set of parameters do not have a probabilities, and further insight about the model must be gained from examination of the parameter set and their generated activity. Methodological advances to ABC methods have come through the use of Markov chain Monte Carlo (MCMC-ABC) (Marjoram et al., 2003) and sequential Monte Carlo (SMC-ABC) (Sisson et al., 2007) sampling techniques. SMC-ABC is considered state-of-the-art ABC, yet this approach still struggles to scale in dimensionality (Sisson et al., 2018; Figure 2). Still, this method has enjoyed much success in systems biology (Liepe et al., 2014). Furthermore, once a parameter set has been obtained by SMC-ABC from a finite set of particles, the SMC-ABC algorithm must be run again from scratch with a new population of initialized particles to obtain additional samples.

For scientific model analysis, we seek a parameter distribution represented by an approximating distribution as in variational inference (Saul and Jordan, 1998): a variational approximation that once optimized yields fast analytic calculations and samples. For the reasons described above, ABC and MCMC techniques are not suitable, because they only produce a set of parameter samples lacking probabilities and have unchanging sampling rate. EPI infers parameters in circuit models using the MEFN (Loaiza-Ganem et al., 2017) algorithm with a deep variational approximation. The deep neural network of EPI (Figure 1E) defines the parametric form (with weights and biases as variational parameters $𝜽$) of the variational approximation of the inferred parameter distribution $q_{𝜽}⁢(𝐳∣𝐱)$. The EPI optimization is enabled using stochastic gradient techniques in the spirit of likelihood-free variational inference (Tran et al., 2017). The analytic relationship between EPI and variational inference is explained in Section 'EPI as variational inference'.

We note that, during our preparation and early presentation of this work (Bittner et al., 2019a; Bittner et al., 2019b), another work has arisen with broadly similar goals: bringing statistical inference to mechanistic models of neural circuits (Nonnenmacher et al., 2018; Michael et al., 2019; Gonçalves et al., 2019). We are encouraged by this general problem being recognized by others in the community, and we emphasize that these works offer complementary neuroscientific contributions (different theoretical models of focus) and use different technical methodologies (ours is built on our prior work [Loaiza-Ganem et al., 2017], theirs similarly [Lueckmann et al., 2017]).

The method EPI differs from SNPE in some key ways. SNPE belongs to a ‘sequential’ class of recently developed simulation-based inference methods in which two neural networks are used for posterior inference. This first neural network is a deep probability distribution (normalizing flow) used to estimate the posterior $p⁢(𝐳∣𝐱)$ (SNPE) or the likelihood $p⁢(𝐱∣𝐳)$ (sequential neural likelihood (SNL) [Papamakarios et al., 2019b]). A recent approach uses an unconstrained neural network to estimate the likelihood ratio (sequential neural ratio estimation (SNRE) [Hermans et al., 2020]). In SNL and SNRE, MCMC sampling techniques are used to obtain samples from the approximated posterior. This contrasts with EPI and SNPE, which use deep probability distributions to model parameters, which facilitates immediate measurements of sample probability, gradient, or Hessian for system analysis. The second neural network in this sequential class of methods is the amortizer. This unconstrained deep network maps data $𝐱$ (or statistics $f⁢(𝐱;𝐳)$ or model parameters $𝐳$) to the weights and biases of the first neural network. These methods are optimized on a conditional density (or ratio) estimation objective. The data used to optimize this objective are generated via an adaptive procedure, in which training data pairs ($𝐱_{i}$, $𝐳_{i}$) become sequentially closer to the true data and posterior.

The approximating fidelity of the deep probability distribution in sequential approaches is optimized to generalize across the training distribution of the conditioning variable. This generalization property of the sequential methods can reduce the accuracy at the singular posterior of interest. Whereas in EPI, the entire expressivity of the deep probability distribution is dedicated to learning a single distribution as well as possible. The well-known inverse mapping problem of exponential families (Wainwright and Jordan, 2008) prohibits an amortization-based approach in EPI, since EPI learns an exponential family distribution parameterized by its mean (in contrast to its natural parameter, see Section 'Maximum entropy distributions and exponential families'). However, we have shown that the same two-network architecture of the sequential simulation-based inference methods can be used for amortized inference in intractable exponential family posteriors when using their natural parameterization (Bittner and Cunningham, 2019).

Finally, one important differentiating factor between EPI and sequential simulation-based inference methods is that EPI leverages gradients $\nabla_{𝐳}⁡f⁢(𝐱;𝐳)$ during optimization. These gradients can improve convergence time and scalability, as we have shown on an example conditioning low-rank RNN connectivity on the property of stable amplification (see Section 'Scaling inference of recurrent neural network connectivity with EPI'). With EPI, we prove out the suggestion that a deep inference technique can improve efficiency by leveraging these emergent property gradients when they are tractable. Sequential simulation-based inference techniques may be better suited for scientific problems where $\nabla_{𝐳}⁡f⁢(𝐱;𝐳)$ is intractable or unavailable, like when there is a nondifferentiable emergent property. However, the sequential simulation-based inference techniques cannot constrain the predictions of the inferred distribution in the manner of EPI.

Structural identifiability analysis involves the measurement of sensitivity and unidentifiabilities in scientific models. Around a single parameter choice, one can measure the Jacobian. One approach for this calculation that scales well is EAR (Karlsson et al., 2012). A popular efficient approach for systems of ODEs has been neural ODE adjoint (Chen et al., 2018) and its stochastic adaptation (Li et al., 2020). Casting identifiability as a statistical estimation problem, the profile likelihood works via iterated optimization while holding parameters fixed (Raue et al., 2009). An exciting recent method is capable of recovering the functional form of such unidentifiabilities away from a point by following degenerate dimensions of the fisher information matrix (Raman et al., 2017). Global structural non-identifiabilities can be found for models with polynomial or rational dynamics equations using DAISY (Pia Saccomani et al., 2003), or through mean optimal transformations (Hengl et al., 2007). With EPI, we have all the benefits given by a statistical inference method plus the ability to query the first- or second-order gradient of the probability of the inferred distribution at any chosen parameter value. The second-order gradient of the log probability (the Hessian), which is directly afforded by EPI distributions, produces quantified information about parametric sensitivity of the emergent property in parameter space (see Section 'Emergent property inference via deep generative models').

#### Deep probability distributions and normalizing flows

Deep probability distributions are comprised of multiple layers of fully connected neural networks (Equation 13). When each neural network layer is restricted to be a bijective function, the sample density can be calculated using the change of variables formula at each layer of the network. For $𝐳_{i}=g_{i}⁢(𝐳_{𝐢-𝟏})$,

$$
p⁢(𝐳_{i})=p⁢(g_{i}^{-1}⁢(𝐳_{i}))⁢|det⁡\frac{\partial⁡g_{i}^{-1}⁢(𝐳_{i})}{\partial⁡𝐳_{i}}|=p⁢(𝐳_{i-1})⁢|det⁡\frac{\partial⁡g_{i}⁢(𝐳_{i-1})}{\partial⁡𝐳_{i-1}}|^{-1}.
$$

However, this computation has cubic complexity in dimensionality for fully connected layers. By restricting our layers to normalizing flows (Rezende and Mohamed, 2015; Papamakarios et al., 2019a) – bijective functions with fast log determinant Jacobian computations, which confer a fast calculation of the sample log probability. Fast log probability calculation confers efficient optimization of the maximum entropy objective (see Section 'Augmented lagrangian optimization').

We use the real NVP (Dinh et al., 2017) normalizing flow class, because its coupling architecture confers both fast sampling (forward) and fast log probability evaluation (backward). Fast probability evaluation facilitates fast gradient and Hessian evaluation of log probability throughout parameter space. Glow permutations were used in between coupling stages (Kingma and Dhariwal, 2018). This is in contrast to autoregressive architectures (Papamakarios et al., 2017; Kingma et al., 2016), in which only one of the forward or backward passes can be efficient. In this work, normalizing flows are used as flexible parameter distribution approximations $q_{𝜽}⁢(𝐳)$ having weights and biases $𝜽$. We specify the architecture used in each application by the number of real NVP affine coupling stages, and the number of neural network layers and units per layer of the conditioning functions.

When calculating Hessians of log probabilities in deep probability distributions, it is important to consider the normalizing flow architecture. With autoregressive architectures (Kingma et al., 2016; Papamakarios et al., 2017), fast sampling and fast log probability evaluations are mutually exclusive. That makes these architectures undesirable for EPI, where efficient sampling is important for optimization, and log probability evaluation speed predicates the efficiency of gradient and Hessian calculations. With real NVP coupling architectures, we get both fast sampling and fast Hessians making both optimization and scientific analysis efficient.

#### Maximum entropy distributions and exponential families

The inferred distribution of EPI is a maximum entropy distribution, which have fundamental links to exponential family distributions. A maximum entropy distribution of form:

$$
p^{∗}(z)=argmaxp\in℘ H(p(z))s.t. E_{z∼p}[T(z)]=\mu_{opt},
$$

where $T⁢(𝐳)$ is the sufficient statistics vector and $𝝁_{opt}$ a vector of their mean values, will have probability density in the exponential family:

$$
p^{*}⁢(𝐳)∝exp⁡(𝜼^{⊤}⁢T⁢(𝐳)).
$$

The mappings between the mean parameterization $𝝁_{opt}$ and the natural parameterization $𝜼$ are formally hard to identify except in special cases (Wainwright and Jordan, 2008).

In this manuscript, emergent properties are defined by statistics $f⁢(𝐱;𝐳)$ having a fixed mean $𝝁$ and variance $𝝈^{2}$ as in Equation 12. The variance constraint is a second moment constraint on $f⁢(𝐱;𝐳)$:

$$
Var_{𝐳,𝐱}⁢[f⁢(𝐱;𝐳)]=𝔼_{𝐳,𝐱}⁢[(f⁢(𝐱;𝐳)-𝝁)^{2}].
$$

As a general maximum entropy distribution (Equation 16), the sufficient statistics vector contains both first and second order moments of $f⁢(𝐱;𝐳)$

$$
T⁢(𝐳)=[𝔼_{𝐱∼p⁢(𝐱∣𝐳)}⁢[f⁢(𝐱;𝐳)]𝔼_{𝐱∼p⁢(𝐱∣𝐳)}⁢[(f⁢(𝐱;𝐳)-𝝁)^{2}]],
$$

which are constrained to the chosen means and variances

$$
𝝁_{opt}=[𝝁𝝈^{2}].
$$

Thus, $𝝁_{opt}$ is used to denote the mean parameter of the maximum entropy distribution defined by the emergent property (all constraints), while $𝝁$ is only the mean of $f⁢(𝐱;𝐳)$. The subscript ‘opt’ of $𝝁_{opt}$ is chosen since it contains all the constraint values to which the EPI optimization algorithm must adhere.

#### Augmented lagrangian optimization

To optimize $q_{𝜽}⁢(𝐳)$ in Equation 14, the constrained maximum entropy optimization is executed using the augmented lagrangian method. The following objective is minimized:

$$
L⁢(𝜽;𝜼_{opt},c)=-H⁢(q_{𝜽})+𝜼_{opt}^{⊤}⁢R⁢(𝜽)+\frac{c}{2}⁢||R⁢(𝜽)||^{2}
$$

where there are average constraint violations

$$
R⁢(𝜽)=𝔼_{𝐳∼q_{𝜽}⁢(𝐳)}⁢[T⁢(𝐳)-𝝁_{opt}],
$$

$𝜼_{opt}\inℝ^{m}$ are the lagrange multipliers where $m$ is the number of total constraints

$$
m=|𝝁_{opt}|=|T⁢(𝐳)|=2⁢|f⁢(𝐱;𝐳)|,
$$

and $c$ is the penalty coefficient. The mean parameter $𝝁_{opt}$ and sufficient statistics $T⁢(𝐳)$ are determined by the means $𝝁$ and variances $𝝈^{2}$ of the emergent property statistics $f⁢(𝐱;𝐳)$ defined in Equation 14. Specifically, $T⁢(𝐳)$ is a concatenation of the first and second moments (Equation 19) and $𝝁_{opt}$ is a concatenation of their constraints $𝝁$ and $𝝈^{2}$ (Equation 20). (Although, note that this algorithm is written for general $T⁢(𝐳)$ and $𝝁_{opt}$ to satisfy the more general class of emergent properties.) The lagrange multipliers $𝜼_{opt}$ are closely related to the natural parameters $𝜼$ of exponential families (see Section 'EPI as variational inference'). Weights and biases $𝜽$ of the deep probability distribution are optimized according to Equation 21 using the Adam optimizer with learning rate 10−3 (Kingma and Ba, 2015).

The gradient with respect to entropy $H⁢(q_{𝜽}⁢(𝐳))$ can be expressed using the reparameterization trick as an expectation of the negative log density of parameter samples $𝐳$ over the randomness in the parameterless initial distribution $q_{0}(𝐳_{0}$):

$$
H⁢(q_{𝜽}⁢(𝐳))=\int-q_{𝜽}⁢(𝐳)⁢log⁡(q_{𝜽}⁢(𝐳))⁢d⁢𝐳=𝔼_{𝐳∼q_{𝜽}}⁢[-log⁡(q_{𝜽}⁢(𝐳))]=𝔼_{𝐳_{0}∼q_{0}}⁢[-log⁡(q_{𝜽}⁢(g_{𝜽}⁢(𝐳_{0})))].
$$

Thus, the gradient of the entropy of the deep probability distribution can be estimated as an average of gradients with respect to the base distribution $𝐳_{0}$:

$$
\nabla_{𝜽}⁡H⁢(q_{𝜽}⁢(𝐳))=𝔼_{𝐳_{0}∼q_{0}}⁢[-\nabla_{𝜽}⁡log⁡(q_{𝜽}⁢(g_{𝜽}⁢(𝐳_{0})))].
$$

The gradients of the log density of the deep probability distribution are tractable through the use of normalizing flows (see Section 'Deep probability distributions and normalizing flows').

The full EPI optimization algorithm is detailed in Algorithm 1. The lagrangian parameters $𝜼_{opt}$ are initialized to zero and adapted following each augmented lagrangian epoch, which is a period of optimization with fixed ($𝜼_{opt}$, $c$) for a given number of stochastic gradient descent (SGD) iterations. A low value of $c$ is used initially, and conditionally increased after each epoch based on constraint error reduction. The penalty coefficient is updated based on the result of a hypothesis test regarding the reduction in constraint violation. The p-value of $𝔼⁢[||R⁢(𝜽_{k+1})||]>\gamma⁢𝔼⁢[||R⁢(𝜽_{k})||]$ is computed, and $c_{k+1}$ is updated to $\beta⁢c_{k}$ with probability $1-p$. The other update rule is $𝜼_{opt,k+1}=𝜼_{opt,k}+c_{k}⁢\frac{1}{n}⁢\sum_{i=1}^{n}(T⁢(𝐳^{(i)})-𝝁_{opt})$ given a batch size $n$ and $𝐳^{(i)}∼q_{𝜽}⁢(𝐳)$. Throughout the study, $\gamma=0.25$, while β was chosen to be either 2 or 4. The batch size of EPI also varied according to application.

<table>
  <thead>
    <tr>
      <th>Algorithm 1. Emergent property inference</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1 initialize 𝜽 by fitting q𝜽 to an isotropic gaussian of mean 𝝁init and variance 𝝈init2 2 initialize c0&gt;0 and 𝜼opt,0=. 3 for Augmented lagrangian epoch k=1,…,kmax do 4     for SGD iteration i=1,…,imax do 5          Sample 𝐳0(1),…,𝐳0(n)∼q0, get transformed variable 𝐳(j)=g𝜽⁢(𝐳0(j)), j=1,…,n 6          Update 𝜽 by descending its stochastic gradient (using ADAM optimizer [Kingma and Ba, 2015]).           ∇θL(θ;ηopt,k,c)=1n∑j=1n∇θlog⁡qθ(z(j))+1n∑j=1n∇θ(T(z(j))−μopt)ηopt,k+ck2n∑j=1n2∇θ(T(z(j))−μopt)⋅2n∑j=n2+1n(T(z(j))−μopt) 7     end 8     Sample 𝐳0(1),…,𝐳0(n)∼q0, get transformed variable 𝐳(j)=g𝜽⁢(𝐳0(j)), j=1,…,n 9     Update 𝜼opt,k+1=𝜼opt,k+ck⁢1n⁢∑j=1n(T⁢(𝐳(j))-𝝁opt). 10     Update ck+1&gt;ck (see text for detail). 11 end</td>
    </tr>
  </tbody>
</table>

In general, $c$ and $𝜼_{opt}$ should start at values encouraging entropic growth early in optimization. With each training epoch in which the update rule for $c$ is invoked, the constraint satisfaction terms are increasingly weighted, which generally results in decreased entropy (e.g. see Figure 1—figure supplement 1C). This encourages the discovery of suitable regions of parameter space, and the subsequent refinement of the distribution to produce the emergent property. The momentum parameters of the Adam optimizer are reset at the end of each augmented lagrangian epoch, which proceeds for $i_{max}$ iterations. In this work, we used a maximum number of augmented lagrangian epochs $k_{max}\geq5$.

Rather than starting optimization from some $𝜽$ drawn from a randomized distribution, we found that initializing $q_{𝜽}⁢(𝐳)$ to approximate an isotropic gaussian distribution conferred more stable, consistent optimization. The parameters of the gaussian initialization were chosen on an application-specific basis. Throughout the study, we chose isotropic Gaussian initializations with mean $𝝁_{init}$ at the center of the support of the distribution and some variance $𝝈_{init}^{2}$, except for one case, where an initialization informed by random search was used (see Section 'Stomatogastric ganglion'). Deep probability distributions were fit to these gaussian initializations using 10,000 iterations of stochastic gradient descent on the evidence lower bound (as in Bittner and Cunningham, 2019) with Adam optimizer and a learning rate of $10^{-3}$.

To assess whether the EPI distribution $q_{𝜽}⁢(𝐳)$ produces the emergent property, we assess whether each individual constraint on the means and variances of $f⁢(𝐱;𝐳)$ is satisfied. We consider the EPI to have converged when a null hypothesis test of constraint violations $R⁢(𝜽)_{i}$ being zero is accepted for all constraints $i\in{1,…,m}$ at a significance threshold $\alpha=0.05$. This significance threshold is adjusted through Bonferroni correction according to the number of constraints $m$. The p-values for each constraint are calculated according to a two-tailed nonparametric test, where 200 estimations of the sample mean $R⁢(𝜽)^{i}$ are made using $N_{test}$ samples of $𝐳∼q_{𝜽}⁢(𝐳)$ at the end of the augmented lagrangian epoch. Of all $k_{max}$ augmented lagrangian epochs, we select the EPI inferred distribution as that which satisfies the convergence criteria and has greatest entropy.

When assessing the suitability of EPI for a particular modeling question, there are some important technical considerations. First and foremost, as in any optimization problem, the defined emergent property should always be appropriately conditioned (constraints should not have wildly different units). Furthermore, if the program is underconstrained (not enough constraints), the distribution grows (in entropy) unstably unless mapped to a finite support. If overconstrained, there is no parameter set producing the emergent property, and EPI optimization will fail (appropriately).

#### Example: 2D LDS

To gain intuition for EPI, consider a two-dimensional linear dynamical system (2D LDS) model (Figure 1—figure supplement 1A):

$$
\tau⁢\frac{d⁢𝐱}{d⁢t}=A⁢𝐱
$$

with

$$
A=[a_{1,1}a_{1,2}a_{2,1}a_{2,2}].
$$

To run EPI with the dynamics matrix elements as the free parameters $𝐳=[a_{1,1},a_{1,2},a_{2,1},a_{2,2}]$ (fixing $\tau=1$ s), the emergent property statistics $f⁢(𝐱;𝐳)$ were chosen to contain parts of the primary eigenvalue of $A$, which predicate frequency, $imag⁢(\lambda_{1})$, and the growth/decay, $real⁢(\lambda_{1})$, of the system

$$
f⁢(𝐱;𝐳)≜[real⁢(\lambda_{1})⁢(𝐱;𝐳)imag⁢(\lambda_{1})⁢(𝐱;𝐳)]
$$

$\lambda_{1}$ is the eigenvalue of greatest real part when the imaginary component is zero, and alternatively that of positive imaginary component when the eigenvalues are complex conjugate pairs. To learn the distribution of real entries of $A$ that produce a band of oscillating systems around 1 Hz, we formalized this emergent property as $real⁢(\lambda_{1})$ having mean zero with variance $0.25^{2}$, and the oscillation frequency $\frac{imag⁢(\lambda_{1})}{2⁢\pi}$ having mean 1 Hz with variance 0.1 Hz2:

$$
𝒳:E_{z,x}[f(x;z)]≜E_{z,x}[real(\lambda_{1})(x;z)imag(\lambda_{1})(x;z)]=[02\pi]≜\muVar_{z,x}[f(x;z)]≜Var_{z,x}[real(\lambda_{1})(x;z)imag(\lambda_{1})(x;z)]=[0.25^{2}(\frac{\pi}{5})^{2}]≜\sigma^{2}.
$$

To write the emergent property $𝒳$ in the form required for the augmented lagrangian optimization (Section 'Augmented lagrangian optimization'), we concatenate these first and second moment constraints into a vector of sufficient statistics $T⁢(𝐳)$ and constraint values $𝝁_{opt}$.

$$
𝔼_{𝐳}⁢[T⁢(𝐳)]≜𝔼_{𝐳}⁢[𝔼_{𝐱∼p⁢(𝐱∣𝐳)}⁢[real⁢(\lambda_{1})⁢(𝐱;𝐳)]𝔼_{𝐱∼p⁢(𝐱∣𝐳)}⁢[imag⁢(\lambda_{1})⁢(𝐱;𝐳)]𝔼_{𝐱∼p⁢(𝐱∣𝐳)}⁢[(real⁢(\lambda_{1})⁢(𝐱;𝐳)-0)^{2}]𝔼_{𝐱∼p⁢(𝐱∣𝐳)}⁢[(imag⁢(\lambda_{1})⁢(𝐱;𝐳)-2⁢\pi)^{2}]]=[02⁢\pi0.25^{2}(\frac{\pi}{5})^{2}]≜𝝁_{opt}.
$$

From now on in all scientific applications (Sections 'Stomatogastric ganglion', 'Scaling EPI for stable amplification in RNNs', 'Primary visual cortex', 'Superior colliculus'), we specify how the EPI optimization was setup by specifying $f⁢(𝐱;𝐳)$, $𝝁$, and $𝝈^{2}$.

Unlike the models we presented in the main text, this model admits an analytical form for the mean emergent property statistics given parameter $𝐳$, since the eigenvalues can be calculated using the quadratic formula:

$$
\lambda=\frac{(\frac{a_{1,1}+a_{2,2}}{\tau})\pm\sqrt{(\frac{a_{1,1}+a_{2,2}}{\tau})^{2}+4⁢(\frac{a_{1,2}⁢a_{2,1}-a_{1,1}⁢a_{2,2}}{\tau})}}{2}.
$$

We study this example, because the inferred distribution is curved and multimodal, and we can compare the result of EPI to analytically derived contours of the emergent property statistics.

Despite the simple analytic form of the emergent property statistics, the EPI distribution in this example is not simply determined. Although $𝔼_{𝐳}⁢[T⁢(𝐳)]$ is calculable directly via a closed form function, the distribution $q_{𝜽}^{*}⁢(𝐳∣𝒳)$ cannot be derived directly. This fact is due to the formally hard problem of the backward mapping: finding the natural parameters $𝜼$ from the mean parameters $𝝁$ of an exponential family distribution (Wainwright and Jordan, 2008). Instead, we used EPI to approximate this distribution (Figure 1—figure supplement 1B). We used a real NVP normalizing flow architecture three coupling layers and two-layer neural networks of 50 units per layer, mapped onto a support of $z_{i}\in[-10,10]$. (see Section 'Deep probability distributions and normalizing flows').

Even this relatively simple system has nontrivial (although intuitively sensible) structure in the parameter distribution. To validate our method, we analytically derived the contours of the probability density from the emergent property statistics and values. In the $a_{1,1}$-$a_{2,2}$ plane, the black line at $real⁢(\lambda_{1})=\frac{a_{1,1}+a_{2,2}}{2}=0$, dashed black line at the standard deviation $real⁢(\lambda_{1})=\frac{a_{1,1}+a_{2,2}}{2}\pm0.25$, and the dashed gray line at twice the standard deviation $real⁢(\lambda_{1})=\frac{a_{1,1}+a_{2,2}}{2}\pm0.5$ follow the contour of probability density of the samples (Figure 1—figure supplement 2A). The distribution precisely reflects the desired statistical constraints and model degeneracy in the sum of $a_{1,1}$ and $a_{2,2}$. Intuitively, the parameters equivalent with respect to emergent property statistic $real⁢(\lambda_{1})$ have similar log densities.

To explain the bimodality of the EPI distribution, we examined the imaginary component of $\lambda_{1}$. When $real⁢(\lambda_{1})=a_{1,1}+a_{2,2}=0$ (which is the case on average in $𝒳$), we have 

$$
imag⁢(\lambda_{1})={\sqrt{\frac{a_{1,1}⁢a_{2,2}-a_{1,2}⁢a_{2,1}}{\tau}},if ⁢a_{1,1}⁢a_{2,2}<a_{1,2}⁢a_{2,1}0otherwise .
$$

In Figure 1—figure supplement 2B, we plot the contours of $imag⁢(\lambda_{1})$ where $a_{1,1}⁢a_{2,2}$ is fixed to 0 at one standard deviation ($\frac{\pi}{5}$, black dashed) and two standard deviations ($\frac{2⁢\pi}{5}$, gray dashed) from the mean of $2⁢\pi$. This validates the curved multimodal structure of the inferred distribution learned through EPI. Subtler combinations of model and emergent property will have more complexity, further motivating the use of EPI for understanding these systems. As we expect, the distribution results in samples of two-dimensional linear systems oscillating near 1 Hz (Figure 1—figure supplement 3).

#### EPI as variational inference

In variational inference, a posterior approximation $q_{𝜽}^{*}$ is chosen from within some variational family $𝒬$ to be as close as possible to the posterior under the KL divergence criteria

$$
q_{\theta}^{∗}(z)=argmaxq_{\theta}\in𝒬KL(q_{\theta}(z)∣∣p(z∣x)).
$$

This KL divergence can be written in terms of entropy of the variational approximation:

$$
KL(q_{𝜽}(𝐳)∣∣p(𝐳∣𝐱))=𝔼_{𝐳∼q_{𝜽}}[log(q_{𝜽}(𝐳))]-𝔼_{𝐳∼q_{𝜽}}[log(p(𝐳∣𝐱))]
$$



$$
=-H⁢(q_{𝜽})-𝔼_{𝐳∼q_{𝜽}}⁢[log⁡(p⁢(𝐱∣𝐳))+log⁡(p⁢(𝐳))-log⁡(p⁢(𝐱))]
$$

Since the marginal distribution of the data $p⁢(𝐱)$ (or ‘evidence’) is independent of $𝜽$, variational inference is executed by optimizing the remaining expression. This is usually framed as maximizing the evidence lower bound (ELBO)

$$
argmaxq_{\theta}\in𝒬KL(q_{\theta}∣∣p(z∣x))=argmaxq_{\theta}\in𝒬H(q_{\theta})+E_{z∼q_{\theta}}[log⁡(p(x∣z))+log⁡(p(z))].
$$

Now, we will show how the maximum entropy problem of EPI is equivalent to variational inference. In general, a maximum entropy problem (as in Equation 16) has an equivalent lagrange dual form: 

$$
argmaxq\in𝒬 H(q(z))⟺argmaxq\in𝒬 H(q(z))+η^{∗⊤}E_{z∼q}[T(z)],s.t. E_{z∼q}[T(z)]=0
$$

with lagrange multipliers $𝜼^{*}$. By moving the lagrange multipliers within the expectation

$$
q^{∗}=argmaxq\in𝒬H(q(z))+E_{z∼q}[η^{∗⊤}T(z)],
$$

inserting a $log⁡exp⁡(⋅)$ within the expectation,

$$
q^{∗}=argmaxq\in𝒬H(q(z))+E_{z∼q}[log⁡exp⁡(η^{∗⊤}T(z))],
$$

and finally choosing $T⁢(⋅)$ to be likelihood averaged statistics as in EPI

$$
q^{∗}=argmaxq\in𝒬H(q(z))+E_{z∼q}[log⁡exp⁡(η^{∗⊤}[E_{x∼p(x∣z)}[ϕ_{1}(x;z)]...E_{x∼p(x∣z)}[ϕ_{m}(x;z)]])],
$$

we can compare directly to the objective used in variational inference (Equation 36). We see that EPI is exactly variational inference with an exponential family likelihood defined by sufficient statistics $T⁢(𝐳)=𝔼_{𝐱∼p⁢(𝐱∣𝐳)}⁢[ϕ⁢(𝐱;𝐳)]$, and where the natural parameter $𝜼^{*}$ is predicated by the mean parameter $𝝁_{opt}$. Equation 40 implies that EPI uses an improper (or uniform) prior, which is easily changed.

This derivation of the equivalence between EPI and variational inference emphasizes why defining a statistical inference program by its mean parameterization $𝝁_{opt}$ is so useful. With EPI, one can clearly define the emergent property $𝒳$ that the model of interest should produce through intuitive selection of $𝝁_{opt}$ for a given $T⁢(𝐳)$. Alternatively, figuring out the correct natural parameters $𝜼^{*}$ for the same $T⁢(𝐳)$ that produces $𝒳$ is a formally hard problem.

### Stomatogastric ganglion

In Section 'Motivating emergent property inference of theoretical models' and 'Emergent property inference via deep generative models', we used EPI to infer conductance parameters in a model of the stomatogastric ganglion (STG) (Gutierrez et al., 2013). This five-neuron circuit model represents two subcircuits: that generating the pyloric rhythm (fast population) and that generating the gastric mill rhythm (slow population). The additional neuron (the IC neuron of the STG) receives inhibitory synaptic input from both subcircuits, and can couple to either rhythm dependent on modulatory conditions. There is also a parametric regime in which this neuron fires at an intermediate frequency between that of the fast and slow populations (Gutierrez et al., 2013), which we infer with EPI as a motivational example. This model is not to be confused with an STG subcircuit model of the pyloric rhythm (Marder and Selverston, 1992), which has been statistically inferred in other studies (Prinz et al., 2004; Gonçalves et al., 2019).

#### STG model

We analyze how the parameters $𝐳=[g_{el},g_{synA}]$ govern the emergent phenomena of intermediate hub frequency in a model of the stomatogastric ganglion (STG) (Gutierrez et al., 2013) shown in Figure 1A with activity $𝐱=[x_{f1},x_{f2},x_{hub},x_{s1},x_{s2}]$, using the same hyperparameter choices as Gutierrez et al. Each neuron’s membrane potential $x_{\alpha}⁢(t)$ for $\alpha\in{f1,f2,hub,s1,s2}$ is the solution of the following stochastic differential equation:

$$
C_{m}⁢\frac{d⁢x_{\alpha}}{d⁢t}=-[h_{l⁢e⁢a⁢k}⁢(𝐱;𝐳)+h_{C⁢a}⁢(𝐱;𝐳)+h_{K}⁢(𝐱;𝐳)+h_{h⁢y⁢p}⁢(𝐱;𝐳)+h_{e⁢l⁢e⁢c}⁢(𝐱;𝐳)+h_{s⁢y⁢n}⁢(𝐱;𝐳)]+d⁢B.
$$

The input current of each neuron is the sum of the leak, calcium, potassium, hyperpolarization, electrical and synaptic currents. Each current component is a function of all membrane potentials and the conductance parameters $𝐳$. Finally, we include gaussian noise $d⁢B$ to the model of Gutierrez et al. so that the model stochastic, although this is not required by EPI.

The capacitance of the cell membrane was set to $C_{m}=1⁢n⁢F$. Specifically, the currents are the difference in the neuron’s membrane potential and that current type’s reversal potential multiplied by a conductance: 

$$
h_{l⁢e⁢a⁢k}⁢(𝐱;𝐳)=g_{l⁢e⁢a⁢k}⁢(x_{\alpha}-V_{l⁢e⁢a⁢k})
$$



$$
h_{e⁢l⁢e⁢c}⁢(𝐱;𝐳)=g_{el}⁢(x_{\alpha}^{p⁢o⁢s⁢t}-x_{\alpha}^{p⁢r⁢e})
$$



$$
h_{s⁢y⁢n}⁢(𝐱;𝐳)=g_{s⁢y⁢n}⁢S_{∞}^{p⁢r⁢e}⁢(x_{\alpha}^{p⁢o⁢s⁢t}-V_{s⁢y⁢n})
$$



$$
h_{C⁢a}⁢(𝐱;𝐳)=g_{C⁢a}⁢M_{∞}⁢(x_{\alpha}-V_{C⁢a})
$$



$$
h_{K}⁢(𝐱;𝐳)=g_{K}⁢N⁢(x_{\alpha}-V_{K})
$$



$$
h_{h⁢y⁢p}⁢(𝐱;𝐳)=g_{h}⁢H⁢(x_{\alpha}-V_{h⁢y⁢p}).
$$

The reversal potentials were set to $V_{l⁢e⁢a⁢k}=-40⁢m⁢V$, $V_{C⁢a}=100⁢m⁢V$, $V_{K}=-80⁢m⁢V$, $V_{h⁢y⁢p}=-20⁢m⁢V$, and $V_{s⁢y⁢n}=-75⁢m⁢V$. The other conductance parameters were fixed to $g_{leak}=1\times10^{−4}\muS$. $g_{Ca}$, $g_{K}$, and $g_{h⁢y⁢p}$ had different values based on fast, intermediate (hub) or slow neuron. The fast conductances had values $g_{C⁢a}=1.9\times10^{-2}$, $g_{K}=3.9\times10^{-2}$, and $g_{h⁢y⁢p}=2.5\times10^{-2}$. The intermediate conductances had values $g_{C⁢a}=1.7\times10^{-2}$, $g_{K}=1.9\times10^{-2}$, and $g_{h⁢y⁢p}=8.0\times10^{-3}$. Finally, the slow conductances had values $g_{C⁢a}=8.5\times10^{-3}$, $g_{K}=1.5\times10^{-2}$, and $g_{h⁢y⁢p}=1.0\times10^{-2}$.

Furthermore, the Calcium, Potassium, and hyperpolarization channels have time-dependent gating dynamics dependent on steady-state gating variables $M_{∞}$, $N_{∞}$ and $H_{∞}$, respectively:

$$
M_{∞}=0.5⁢(1+tanh⁡(\frac{x_{\alpha}-v_{1}}{v_{2}}))
$$



$$
\frac{d⁢N}{d⁢t}=\lambda_{N}⁢(N_{∞}-N)
$$



$$
N_{∞}=0.5⁢(1+tanh⁡(\frac{x_{\alpha}-v_{3}}{v_{4}}))
$$



$$
\lambda_{N}=ϕ_{N}⁢cosh⁡(\frac{x_{\alpha}-v_{3}}{2⁢v_{4}})
$$



$$
\frac{d⁢H}{d⁢t}=\frac{(H_{∞}-H)}{\tau_{h}}
$$



$$
H_{∞}=\frac{1}{1+exp⁡(\frac{x_{\alpha}+v_{5}}{v_{6}})}
$$



$$
\tau_{h}=272-(\frac{-1499}{1+exp⁡(\frac{-x_{\alpha}+v_{7}}{v_{8}})}).
$$

where we set $v_{1}=0⁢m⁢V$, $v_{2}=20⁢m⁢V$, $v_{3}=0⁢m⁢V$, $v_{4}=15⁢m⁢V$, $v_{5}=78.3⁢m⁢V$, $v_{6}=10.5⁢m⁢V$, $v_{7}=-42.2⁢m⁢V$, $v_{8}=87.3⁢m⁢V$, $v_{9}=5⁢m⁢V$, and $v_{t⁢h}=-25⁢m⁢V$.

Finally, there is a synaptic gating variable as well:

$$
S_{∞}=\frac{1}{1+exp⁡(\frac{v_{t⁢h}-x_{\alpha}}{v_{9}})}.
$$

When the dynamic gating variables are considered, this is actually a 15-dimensional nonlinear dynamical system. The gaussian noise $d⁢𝐁$ has variance $(1\times10^{-12})^{2}$ A2, and introduces variability in frequency at each parameterization $𝐳$.

#### Hub frequency calculation

In order to measure the frequency of the hub neuron during EPI, the STG model was simulated for $T=300$ time steps of $d⁢t=25⁢ms$. The chosen $d⁢t$ and $T$ were the most computationally convenient choices yielding accurate frequency measurement. We used a basis of complex exponentials with frequencies from 0.0 to 1.0 Hz at 0.01 Hz resolution to measure frequency from simulated time series

$$
Φ=[0.0,0.01,...,1.0]^{⊤}.
$$

To measure spiking frequency, we processed simulated membrane potentials with a relu (spike extraction) and low-pass filter with averaging window of size 20, then took the frequency with the maximum absolute value of the complex exponential basis coefficients of the processed time-series. The first 20 temporal samples of the simulation are ignored to account for initial transients.

To differentiate through the maximum frequency identification, we used a soft-argmax Let $X_{\alpha}\in𝒞^{|Φ|}$ be the complex exponential filter bank dot products with the signal $x_{\alpha}\inℝ^{N}$, where $\alpha\in{f1,f2,hub,s1,s2}$. The soft-argmax is then calculated using temperature parameter $\beta_{ψ}=100$

$$
ψ_{\alpha}=softmax⁢(\beta_{ψ}⁢|X_{\alpha}|⊙i),
$$

where $i=[0,1,…,100]$. The frequency is then calculated as

$$
\omega_{\alpha}=0.01⁢ψ_{\alpha}⁢Hz.
$$

Intermediate hub frequency, like all other emergent properties in this work, is defined by the mean and variance of the emergent property statistics. In this case, we have one statistic, hub neuron frequency, where the mean was chosen to be 0.55 Hz,(Equation 2) and variance was chosen to be 0.0252 Hz2 (Equation 3).

#### EPI details for the STG model

EPI was run for the STG model using 

$$
f⁢(𝐱;𝐳)=\omega_{hub}⁢(𝐱;𝐳),
$$



$$
𝝁=[0.55],
$$

and

$$
𝝈^{2}=[0.025^{2}]
$$

(see Sections 'Maximum entropy distributions and exponential families', 'Augmented lagrangian optimization', and example in Section 'Example: 2D LDS'). Throughout optimization, the augmented lagrangian parameters η and $c$, were updated after each epoch of $i_{max}=5,000$ iterations (see Section 'Augmented lagrangian optimization'). The optimization converged after five epochs (Figure 1—figure supplement 4).

For EPI in Figure 1E, we used a real NVP architecture with three coupling layers and two-layer neural networks of 25 units per layer. The normalizing flow architecture mapped $𝐳_{0}∼𝒩⁢(,I)$ to a support of $𝐳=[g_{el},g_{synA}]\in[4,8]\times[0.01,4]$, initialized to a gaussian approximation of samples returned by a preliminary ABC search. We did not include $g_{synA}<0.01$, for numerical stability. EPI optimization was run with an augmented lagrangian coefficient of $c_{0}=10^{5}$, hyperparameter $\beta=2$, a batch size $n=400$, and we simulated one $𝐱^{(i)}$ per $𝐳^{(i)}$. The architecture converged with criteria $N_{test}=100$.

#### Hessian sensitivity vectors

To quantify the second-order structure of the EPI distribution, we evaluated the Hessian of the log probability $\frac{\partial^{2}⁡log⁡q⁢(𝐳∣𝒳)}{\partial⁡𝐳𝐳^{⊤}}$. The eigenvector of this Hessian with most negative eigenvalue is defined as the sensitivity dimension $𝐯_{1}$, and all subsequent eigenvectors are ordered by increasing eigenvalue. These eigenvalues are quantifications of how fast the emergent property deteriorates via the parameter combination of their associated eigenvector. In Figure 1D, the sensitivity dimension v1 (solid) and the second eigenvector of the Hessian v2 (dashed) are shown evaluated at the mode of the distribution. Since the Hessian eigenvectors have sign degeneracy, the visualized directions in 2-D parameter space were chosen to have positive $g_{synA}$. The length of the arrows is inversely proportional to the square root of the absolute value of their eigenvalues $\lambda_{1}=-10.7$ and $\lambda_{2}=-3.22$. For the same magnitude perturbation away from the mode, intermediate hub frequency only diminishes along the sensitivity dimension $𝐯_{1}$ (Figure 1E–F).

### Scaling EPI for stable amplification in RNNs

#### Rank-2 RNN model

We examined the scaling properties of EPI by learning connectivities of RNNs of increasing size that exhibit stable amplification. Rank-2 RNN connectivity was modeled as $W=U⁢V^{⊤}$, where $U=[𝐔_{1}𝐔_{2}]+g⁢χ^{(W)}$, $V=[𝐕_{1}𝐕_{2}]+g⁢χ^{(V)}$, and $χ_{i,j}^{(W)},χ_{i,j}^{(V)}∼𝒩⁢(0,1)$. This RNN model has dynamics

$$
\tau⁢𝐱˙=-𝐱+W⁢𝐱.
$$

In this analysis, we inferred connectivity parameterizations $𝐳=[𝐔_{1}^{⊤},𝐔_{2}^{⊤},𝐕_{1}^{⊤},𝐕_{2}^{⊤}]^{⊤}\in[-1,1]^{(4⁢N)}$ that produced stable amplification using EPI, SMC-ABC (Sisson et al., 2007), and SNPE (Gonçalves et al., 2019) (see Section Related methods).

#### Stable amplification

For this RNN model to be stable, all real eigenvalues of $W$ must be less than 1: $real⁢(\lambda_{1})<1$, where $\lambda_{1}$ denotes the greatest real eigenvalue of $W$. For a stable RNN to amplify at least one input pattern, the symmetric connectivity $W^{s}=\frac{W+W⊤}{2}$ must have an eigenvalue greater than 1: $\lambda_{1}^{s}>1$, where $\lambda^{s}$ is the maximum eigenvalue of $W^{s}$. These two conditions are necessary and sufficient for stable amplification in RNNs (Bondanelli and Ostojic, 2020).

#### EPI details for RNNs

We defined the emergent property of stable amplification with means of these eigenvalues (0.5 and 1.5, respectively) that satisfy these conditions. To complete the emergent property definition, we chose variances ($0.25^{2}$) about those means such that samples rarely violate the eigenvalue constraints. To write the emergent property of Equation 5 in terms of the EPI optimization, we have

$$
f⁢(𝐱;𝐳)=[real⁢(\lambda_{1})⁢(𝐱;𝐳)\lambda_{1}^{s}⁢(𝐱;𝐳)],
$$



$$
𝝁=[0.51.5],
$$

and

$$
𝝈^{2}=[0.25^{2}0.25^{2}]
$$

(see Sections 'Maximum entropy distributions and exponential families', 'Augmented lagrangian optimization', and example in Section 'Example: 2D LDS'). Gradients of maximum eigenvalues of Hermitian matrices like $W^{s}$ are available with modern automatic differentiation tools. To differentiate through the $real⁢(\lambda_{1})$, we solved the following equation for eigenvalues of rank-2 matrices using the rank reduced matrix $W^{r}=V^{⊤}⁢U$

$$
\lambda_{\pm}=\frac{Tr⁢(W^{r})\pm\sqrt{Tr⁢(W^{r})^{2}-4⁢Det⁢(W^{r})}}{2}.
$$

For EPI in Figure 2, we used a real NVP architecture with three coupling layers of affine transformations parameterized by two-layer neural networks of 100 units per layer. The initial distribution was a standard isotropic gaussian $𝐳_{0}∼𝒩⁢(,I)$ mapped to the support of $𝐳_{i}\in[-1,1]$. We used an augmented lagrangian coefficient of $c_{0}=10^{3}$, a batch size $n=200$, $\beta=4$, and we simulated one $𝐖^{(i)}$ per $𝐳^{(i)}$. We chose to use $i_{max}=500$ iterations per augmented lagrangian epoch and emergent property constraint convergence was evaluated at $N_{test}=200$ (Figure 2B blue line, and Figure 2C–D blue). It was fastest to initialize the EPI distribution on a Tesla V100 GPU, and then subsequently optimize it on a CPU with 32 cores. EPI timing measurements accounted for this initialization period.

#### Methodological comparison

We compared EPI to two alternative simulation-based inference techniques, since the likelihood of these eigenvalues given $𝐳$ is not available. Approximate bayesian computation (ABC) (Beaumont et al., 2002) is a rejection sampling technique for obtaining sets of parameters $𝐳$ that produce activity $𝐱$ close to some observed data $𝐱_{0}$. Sequential Monte Carlo approximate bayesian computation (SMC-ABC) is the state-of-the-art ABC method, which leverages SMC techniques to improve sampling speed. We ran SMC-ABC with the pyABC package (Klinger et al., 2018) to infer RNNs with stable amplification: connectivities having eigenvalues within an $ϵ$-defined $l$−2 distance of

$$
𝐱_{0}=[real⁢(\lambda_{1})\lambda_{1}^{s}]=[0.51.5].
$$

SMC-ABC was run with a uniform prior over $𝐳\in[-1,1]^{(4⁢N)}$, a population size of 1000 particles with simulations parallelized over 32 cores, and a multivariate normal transition model.

SNPE, the next approach in our comparison, is far more similar to EPI. Like EPI, SNPE treats parameters in mechanistic models with deep probability distributions, yet the two learning algorithms are categorically different. SNPE uses a two-network architecture to approximate the posterior distribution of the model conditioned on observed data $𝐱_{0}$. The amortizing network maps observations $𝐱_{i}$ to the parameters of the deep probability distribution. The weights and biases of the parameter network are optimized by sequentially augmenting the training data with additional pairs ($𝐳_{i}$, $𝐱_{i}$) based on the most recent posterior approximation. This sequential procedure is important to get training data $𝐳_{i}$ to be closer to the true posterior, and $𝐱_{i}$ to be closer to the observed data. For the deep probability distribution architecture, we chose a masked autoregressive flow with affine couplings (the default choice), three transforms, 50 hidden units, and a normalizing flow mapping to the support as in EPI. This architectural choice closely tracked the size of the architecture used by EPI (Figure 2—figure supplement 1). As in SMC-ABC, we ran SNPE with $𝐱_{0}=\mu$. All SNPE optimizations were run for a limit of 1.5 days, or until two consecutive rounds resulted in a validation log probability lower than the maximum observed for that random seed. It was always faster to run SNPE on a CPU with 32 cores rather than on a Tesla V100 GPU.

To compare the efficiency of these algorithms for inferring RNN connectivity distributions producing stable amplification, we develop a convergence criteria that can be used across methods. While EPI has its own hypothesis testing convergence criteria for the emergent property, it would not make sense to use this criteria on SNPE and SMC-ABC which do not constrain the means and variances of their predictions. Instead, we consider EPI and SNPE to have converged after completing its most recent optimization epoch (EPI) or round (SNPE) in which the distance $|𝔼_{𝐳,𝐱}⁢[f⁢(𝐱;𝐳)]-𝝁|_{2}$ is less than 0.5. We consider SMC-ABC to have converged once the population produces samples within the $ϵ=0.5$ ball ensuring stable amplification.

When assessing the scalability of SNPE, it is important to check that alternative hyperparamterizations could not yield better performance. Key hyperparameters of the SNPE optimization are the number of simulations per round $n_{round}$, the number of atoms used in the atomic proposals of the SNPE-C algorithm (Greenberg, 2019), and the batch size $n$. To match EPI, we used a batch size of $n=200$ for $N\leq25$, however we found $n=1,000$ to be helpful for SNPE in higher dimensions. While $n_{round}=1,000$ yielded SNPE convergence for $N\leq25$, we found that a substantial increase to $n_{round}=25,000$ yielded more consistent convergence at $N=50$ (Figure 2—figure supplement 2A). By increasing $n_{round}$, we also necessarily increase the duration of each round. At $N=100$, we tried two hyperparameter modifications. As suggested in Greenberg, 2019, we increased $n_{atom}$ by an order of magnitude to improve gradient quality, but this had little effect on the optimization (much overlap between same random seeds) (Figure 2—figure supplement 2B). Finally, we increased $n_{round}$ by an order of magnitude, which yielded convergence in one case, but no others. We found no way to improve the convergence rate of SNPE without making more aggressive hyperparameter choices requiring high numbers of simulations. In Figure 2C–D, we show samples from the random seed resulting in emergent property convergence at greatest entropy (EPI), the random seed resulting in greatest validation log probability (SNPE), and the result of all converged random seeds (SMC).

#### Effect of RNN parameters on EPI and SNPE inferred distributions

To clarify the difference in objectives of EPI and SNPE, we show their results on RNN models with different numbers of neurons $N$ and random strength $g$. The parameters inferred by EPI consistently produces the same mean and variance of $real⁢(\lambda_{1})$ and $\lambda_{1}^{s}$, while those inferred by SNPE change according to the model definition (Figure 2—figure supplement 3A). For $N=2$ and $g=0.01$, the SNPE posterior has greater concentration in eigenvalues around $𝐱_{0}$ than at $g=0.1$, where the model has greater randomness (Figure 2—figure supplement 3B top, orange). At both levels of $g$ when $N=2$, the posterior of SNPE has lower entropy than EPI at convergence (Figure 2—figure supplement 3B top). However at $N=10$, SNPE results in a predictive distribution of more widely dispersed eigenvalues (Figure 2—figure supplement 3A bottom), and an inferred posterior with greater entropy than EPI (Figure 2—figure supplement 3B bottom). We highlight these differences not to focus on an insightful trend, but to emphasize that these methods optimize different objectives with different implications.

Note that SNPE converges when it’s validation log probability has saturated after several rounds of optimization (Figure 2—figure supplement 3C), and that EPI converges after several epochs of its own optimization to enforce the emergent property constraints (Figure 2—figure supplement 3D blue). Importantly, as SNPE optimizes its posterior approximation, the predictive means change, and at convergence may be different than $𝐱_{0}$ (Figure 2—figure supplement 3D orange, left). It is sensible to assume that predictions of a well-approximated SNPE posterior should closely reflect the data on average (especially given a uniform prior and a low degree of stochasticity); however, this is not a given. Furthermore, no aspect of the SNPE optimization controls the variance of the predictions (Figure 2—figure supplement 3D orange, right).

### Primary visual cortex

#### V1 model

E-I circuit models, rely on the assumption that inhibition can be studied as an indivisible unit, despite ample experimental evidence showing that inhibition is instead composed of distinct elements (Tremblay et al., 2016). In particular three types of genetically identified inhibitory cell-types – parvalbumin (P), somatostatin (S), VIP (V) – compose 80% of GABAergic interneurons in V1 (Markram et al., 2004; Rudy et al., 2011; Tremblay et al., 2016), and follow specific connectivity patterns (Figure 3A; Pfeffer et al., 2013), which lead to cell-type-specific computations (Mossing et al., 2021; Palmigiano et al., 2020). Currently, how the subdivision of inhibitory cell-types, shapes correlated variability by reconfiguring recurrent network dynamics is not understood.

In the stochastic stabilized supralinear network (Hennequin et al., 2018), population rate responses $𝐱$ to mean input $𝐡$, recurrent input $W⁢𝐱$ and slow noise $ϵ$ are governed by

$$
\tau⁢\frac{d⁢𝐱}{d⁢t}=-𝐱+ϕ⁢(W⁢𝐱+𝐡+ϵ),
$$

where $ϕ(⋅)=[⋅]_{+}^{2}$, and the noise is an Ornstein-Uhlenbeck process $ϵ∼O⁢U⁢(\tau_{noise},𝝈)$

$$
\tau_{noise}⁢d⁢ϵ_{\alpha}=-ϵ_{\alpha}⁢d⁢t+\sqrt{2⁢\tau_{noise}}⁢\sigma~_{\alpha}⁢d⁢B
$$

with $\tau_{noise}=5⁢ms>\tau=1⁢ms$. The noisy process is parameterized as

$$
\sigma~_{\alpha}=\sigma_{\alpha}⁢\sqrt{1+\frac{\tau}{\tau_{noise}}},
$$

so that $𝝈$ parameterizes the variance of the noisy input in the absence of recurrent connectivity ($W=$). As contrast $c\in[0,1]$ increases, input to the E- and P-populations increases relative to a baseline input $𝐡=𝐡_{b}+c⁢𝐡_{c}$. Connectivity ($W_{fit}$) and input ($𝐡_{b,fit}$ and $𝐡_{c,fit}$) parameters were fit using the deterministic V1 circuit model (Palmigiano et al., 2020)

$$
W_{fit}=[W_{E⁢E}W_{E⁢P}W_{E⁢S}W_{E⁢V}W_{P⁢E}W_{P⁢P}W_{P⁢S}W_{P⁢V}W_{S⁢E}W_{S⁢P}W_{S⁢S}W_{S⁢V}W_{V⁢E}W_{V⁢P}W_{V⁢S}W_{V⁢V}]=[2.18-1.19-.594-.2291.66-.651-.680-.242.895-5.22\times10^{-3}-1.51\times10^{-4}-.7613.34-2.31-.254-2.52\times10^{-4}],
$$



$$
𝐡_{b,fit}=[.416.429.491.486],
$$

and

$$
𝐡_{c,fit}=[.359.40300].
$$

To obtain rates on a realistic scale (100-fold greater), we map these fitted parameters to an equivalence class

$$
W=[W_{E⁢E}W_{E⁢P}W_{E⁢S}W_{E⁢V}W_{P⁢E}W_{P⁢P}W_{P⁢S}W_{P⁢V}W_{S⁢E}W_{S⁢P}W_{S⁢S}W_{S⁢V}W_{V⁢E}W_{V⁢P}W_{V⁢S}W_{V⁢V}]=[.218-.119-.0594-.0229.166-.0651-.068-.0242.0895-5.22\times10^{-4}-1.51\times10^{-5}-.0761.334-.231-.0254-2.52\times10^{-5}],
$$



$$
𝐡_{b}=[h_{b,E}h_{b,P}h_{b,S}h_{b,V}]=[4.164.294.914.86],
$$

and

$$
𝐡_{c}=[h_{c,E}h_{c,P}h_{c,S}h_{c,V}]=[3.594.0300].
$$

Circuit responses are simulated using $T=200$ time steps at $d⁢t=0.5⁢ms$ from an initial condition drawn from $𝐱⁢(0)∼U⁢[10⁢Hz,25⁢Hz]$. Standard deviation of the E-population $s_{E}⁢(𝐱;𝐳)$ is calculated as the square root of the temporal variance from $t_{s⁢s}=75⁢ms$ to $T⁢d⁢t=100⁢ms$

$$
s_{E}⁢(𝐱;𝐳)=\sqrt{𝔼_{t>t_{s⁢s}}⁢[(x_{E}⁢(t)-𝔼_{t>t_{s⁢s}}⁢[x_{E}⁢(t)])^{2}]}.
$$

#### EPI details for the V1 model

To write the emergent properties of Equation 7 in terms of the EPI optimization, we have 

$$
f⁢(𝐱;𝐳)=s_{E}⁢(𝐱;𝐳),
$$



$$
𝝁=[5]
$$

(or $𝝁=[10]$), and

$$
𝝈^{2}=[1^{2}]
$$

(see Sections 'Maximum entropy distributions and exponential families', 'Augmented lagrangian optimization', and example in Section 'Example: 2D LDS').

For EPI in Figure 3D–E and Figure 3—figure supplement 1, we used a real NVP architecture with three coupling layers and two-layer neural networks of 50 units per layer. The normalizing flow architecture mapped $z_{0}∼𝒩⁢(,I)$ to a support of $𝐳=[\sigma_{E},\sigma_{P},\sigma_{S},\sigma_{V}]\in[0.0,0.5]^{4}$. EPI optimization was run using three different random seeds for architecture initialization $𝜽$ with an augmented lagrangian coefficient of $c_{0}=10^{-1}$, $\beta=2$, a batch size $n=100$, and simulated 100 trials to calculate average $s_{E}⁢(𝐱;𝐳)$ for each $𝐳^{(i)}$. We used $i_{max}=2,000$ iterations per epoch. The distributions shown are those of the architectures converging with criteria $N_{test}=100$ at greatest entropy across three random seeds. Optimization details are shown in Figure 3—figure supplement 2. The sums of squares of each pair of parameters are shown for each EPI distribution in Figure 3—figure supplement 3. The plots are histograms of 500 samples from each EPI distribution from which the significance p-values of Section 'EPI reveals how recurrence with multiple inhibitory subtypes governs excitatory variability in a V1 model' are determined.

#### Sensitivity analyses

In Figure 3E, we visualize the modes of $q_{𝜽}⁢(𝐳∣𝒳)$ throughout the $\sigma_{E}$-$\sigma_{P}$ marginal. At each local mode $𝐳^{*}⁢(\sigma_{P})$, where $\sigma_{P}$ is fixed, we calculated the Hessian and visualized the sensitivity dimension in the direction of positive $\sigma_{E}$.

#### Testing for the paradoxical effect

The paradoxical effect occurs when a populations steady state rate is decreased (or increased) when an increase (decrease) in current is applied to that population (Tsodyks et al., 1997). To see which, if any, populations exhibited a paradoxical effect, we examined responses to changes in input to individual neuron-type populations, where the initial condition was the steady state response to $h$ (Figure 3—figure supplement 4). Input magnitudes were chosen so that the effect is salient (0.002 for E and P, but 0.02 for S and V). Only the P-population exhibited the paradoxical effect at this connectivity $W$ and input $𝐡$.

#### Primary visual cortex: Mathematical intuition and challenges

We write the original Equations 68 and 69 in the following way:

$$
dx=\frac{1}{\tau}(−x+f(Wx+h+ϵ))dtdϵ=−\frac{dt}{\tau_{noise}}ϵ+\frac{\sqrt{2}}{\sqrt{\tau_{noise}}}Σ_{ϵ}dW
$$

where in this paper we chose $Σ_{ϵ}$, the covariance of the noise to be

$$
Σ_{ϵ}=\tau_{noise}⁢[\sigma~_{E}0000\sigma~_{P}0000\sigma~_{S}0000\sigma~_{V}]
$$

where $\sigma~_{\alpha}$ is the reparameterized standard deviation of the noise for population α from Equation 70.

We are interested in computing the covariance of the activity. For that, first we define $v=\omegax+h+ϵ$, the total input to each cell type, and the matrix $S$, the negative Jacobian $S=I−\omegaf^{′}(v)$. Then, Equation 81 can be written as an 8-dimensional system. Linearizing around the fixed point of the system without fluctuations, we find the equations that describe the fluctuations of the input to each cell type:

$$
d(\deltavϵ)=−(S−\frac{\tau_{noise}−\tau}{\tau\tau_{noise}}I0\frac{1}{\tau_{noise}}I)(\deltavϵ)dt+(0\frac{\sqrt{2}}{\sqrt{\tau_{noise}}}Σ_{ϵ}0\frac{\sqrt{2}}{\sqrt{\tau_{noise}}}Σ_{ϵ})dW
$$

where $d⁢𝐖$ is a vector with the private noise of each variable. The $d⁢𝐖$ term is multiplied by a non-diagonal matrix, because the noise that the voltage receives is the exact same as the one that comes from the OU process and not another process. The covariance of the inputs $Λ_{v}=⟨\deltav\deltav^{T}⟩$ can be found as the solution the following Lyapunov equation (Hennequin et al., 2018; Gardiner, 2009):

$$
(S−\frac{\tau_{noise}−\tau}{\tau\tau_{noise}}I0\frac{1}{\tau_{noise}}I)(Λ_{v}Λ_{c}Λ_{c}^{T}Λ_{ϵ})+(Λ_{v}Λ_{c}Λ_{c}^{T}Λ_{ϵ})(S^{T}0−\frac{\tau_{noise}−\tau}{\tau\tau_{noise}}I\frac{1}{\tau_{noise}}I)=(\frac{2}{\tau_{noise}}Λ_{ϵ}\frac{2}{\tau_{noise}}Λ_{ϵ}\frac{2}{\tau_{noise}}Λ_{ϵ}\frac{2}{\tau_{noise}}Λ_{ϵ})
$$

Where $Λ_{c}=⟨\deltav\deltaϵ^{T}⟩$ can be eliminated by solving this block matrix multiplication:

$$
SΛ_{v}+Λ_{v}S^{T}=\frac{2Λ_{ϵ}}{\tau_{noise}}+\frac{\tau_{noise}^{2}−\tau^{2}}{(\tau\tau_{noise})^{2}}((\frac{1}{\tau_{noise}}I+S)^{−1}Λ_{ϵ}+Λ_{ϵ}(\frac{1}{\tau_{noise}}I+S^{T})^{−1})
$$

The equation above is another Lyapunov Equation, now in 4 dimensions. In the simplest case in which $\tau_{noise}=\tau$, the voltage is directly driven by white noise, and $Λ_{v}$ can be expressed in powers of $S$ and $S^{T}$. Because $S$ satisfies its own polynomial equation (Cayley Hamilton theorem), there will be four coefficients for the expansion of $S$ and four for $S^{T}$, resulting in 16 coefficients that define $Λ_{v}$ for a given $S$. Due to symmetry arguments (Gardiner, 2009), in this case the diagonal elements of the covariance matrix of the voltage will have the form:

$$
Λ_{v_{i⁢i}}=\sumi={E,P,S,V}g_{i}⁢(S)⁢\sigma_{i⁢i}^{2}
$$

These coefficients $g_{i}⁢(S)$ are complicated functions of the Jacobian of the system. Although expressions for these coefficients can be found explicitly, only numerical evaluation of those expressions determine which components of the noisy input are going to strongly influence the variability of excitatory population. Showing the generality of this dependence in more complicated noise scenarios (e.g. $\tau_{noise}>\tau$ as in Section 'EPI reveals how recurrence with multiple inhibitory subtypes governs excitatory variability in a V1 model'), is the focus of current research.

### Superior colliculus

#### SC model

The ability to switch between two separate tasks throughout randomly interleaved trials, or ‘rapid task switching,’ has been studied in rats, and midbrain superior colliculus (SC) has been show to play an important in this computation (Duan et al., 2015). Neural recordings in SC exhibited two populations of neurons that simultaneously represented both task context (Pro or Anti) and motor response (contralateral or ipsilateral to the recorded side), which led to the distinction of two functional classes: the Pro/Contra and Anti/Ipsi neurons (Duan et al., 2021). Given this evidence, Duan et al. proposed a model with four functionally-defined neuron-type populations: two in each hemisphere corresponding to the Pro/Contra and Anti/Ipsi populations. We study how the connectivity of this neural circuit governs rapid task switching ability.

The four populations of this model are denoted as left Pro (LP), left Anti (LA), right Pro (RP) and right Anti (RA). Each unit has an activity ($x_{\alpha}$) and internal variable ($u_{\alpha}$) related by

$$
x_{\alpha}=ϕ⁢(u_{\alpha})=(\frac{1}{2}⁢tanh⁡(\frac{u_{\alpha}-a}{b})+\frac{1}{2}),
$$

where $\alpha\in{L⁢P,L⁢A,R⁢A,R⁢P}$, $a=0.05$ and $b=0.5$ control the position and shape of the nonlinearity. We order the neural populations of $x$ and $u$ in the following manner

$$
𝐱=[x_{L⁢P}x_{L⁢A}x_{R⁢P}x_{R⁢A}] 𝐮=[u_{L⁢P}u_{L⁢A}u_{R⁢P}u_{R⁢A}],
$$

which evolve according to

$$
\tau⁢\frac{d⁢𝐮}{d⁢t}=-𝐮+W⁢𝐱+𝐡+d⁢𝐁.
$$

with time constant $\tau=0.09⁢s$, step size 24 ms and Gaussian noise $d⁢𝐁$ of variance $0.2^{2}$. These hyperparameter values are motivated by modeling choices and results from Duan et al., 2021.

The weight matrix has four parameters for self $s⁢W$, vertical $v⁢W$, horizontal $h⁢W$, and diagonal $d⁢W$ connections:

$$
W=[s⁢Wv⁢Wh⁢Wd⁢Wv⁢Ws⁢Wd⁢Wh⁢Wh⁢Wd⁢Ws⁢Wv⁢Wd⁢Wh⁢Wv⁢Ws⁢W].
$$

We study the role of parameters $𝐳=[s⁢W,v⁢W,h⁢W,d⁢W]^{⊤}$ in rapid task switching.

The circuit receives four different inputs throughout each trial, which has a total length of 1.8 s.

$$
𝐡=𝐡_{constant}+𝐡_{P,bias}+𝐡_{rule}+𝐡_{choice-period}+𝐡_{light}.
$$

There is a constant input to every population,

$$
𝐡_{constant}=I_{constant}⁢[1,1,1,1]⊤,
$$

a bias to the Pro populations

$$
𝐡_{P,bias}=I_{P,bias}⁢[1,0,1,0]⊤,
$$

rule-based input depending on the condition

$$
𝐡_{P,rule}⁢(t)={I_{P,rule}⁢[1,0,1,0]^{⊤},if ⁢t\leq1.2⁢s0,otherwise
$$



$$
𝐡_{A,rule}⁢(t)={I_{A,rule}⁢[0,1,0,1]^{⊤},if ⁢t\leq1.2⁢s0,otherwise,
$$

a choice-period input

$$
𝐡_{choice}⁢(t)={I_{choice}⁢[1,1,1,1]^{⊤},if ⁢t>1.2⁢s0,otherwise,
$$

and an input to the right or left-side depending on where the light stimulus is delivered

$$
𝐡_{light}⁢(t)={I_{light}⁢[1,1,0,0]^{⊤},if ⁢1.2⁢s<t<1.5⁢s⁢and LeftI_{light}⁢[0,0,1,1]^{⊤},if ⁢1.2⁢s<t<1.5⁢s⁢and Right0,otherwise.
$$

The input parameterization was fixed to $I_{constant}=0.75$, $I_{P,bias}=0.5$, $I_{P,rule}=0.6$, $I_{A,rule}=0.6$, $I_{choice}=0.25$, and $I_{light}=0.5$.

#### Task accuracy calculation

The accuracies of the Pro- and Anti-tasks are calculated as

$$
p_{P}⁢(𝐱;𝐳)=𝔼_{𝐱∼p⁢(𝐱∣𝐳)}⁢[d_{P}⁢(𝐱;𝐳)]
$$

and 

$$
p_{A}⁢(𝐱;𝐳)=𝔼_{𝐱∼p⁢(𝐱∣𝐳)}⁢[d_{A}⁢(𝐱;𝐳)]
$$

where $d_{P}⁢(𝐱;𝐳)$ and $d_{A}⁢(𝐱;𝐳)$ calculate the decision made in each trial (approximately 1 for correct and 0 for incorrect choices). Specifically, 

$$
d_{P}(𝐱;𝐳)=Θ[x_{L⁢P}(t=1.8s)-x_{R⁢P}(t=1.8s)]
$$

in Pro-trials where the stimulus is on the left side, and Θ approximates the Heaviside step function. Similarly,

$$
d_{A}(𝐱;𝐳)=Θ[x_{R⁢P}(t=1.8s)-x_{L⁢P}(t=1.8s)]
$$

in Anti-trials where the stimulus was on the left side. Our accuracy calculation only considers one stimulus presentation (Left), since the model is left-right symmetric. The accuracy is averaged over 200 independent trials, and the Heaviside step function is approximated as

$$
Θ⁢(𝐱)=sigmoid⁢(\beta_{Θ}⁢𝐱),
$$

where $\beta_{Θ}=100$.

#### EPI details for the SC model

To write the emergent properties of Equation 9 in terms of the EPI optimization, we have

$$
f⁢(𝐱;𝐳)=[d_{P}⁢(𝐱;𝐳)d_{A}⁢(𝐱;𝐳)]
$$



$$
𝝁=[.75.75],
$$

and

$$
𝝈^{2}=[.075^{2}.075^{2}]
$$

(see Sections 'Maximum entropy distributions and exponential families', 'Augmented lagrangian optimization', and example in Section 'Example: 2D LDS').

Throughout optimization, the augmented lagrangian parameters η and $c$, were updated after each epoch of $i_{max}=2,000$ iterations (see Section 'Augmented lagrangian optimization'). The optimization converged after ten epochs (Figure 4—figure supplement 4).

For EPI in Figure 4C, we used a real NVP architecture with three coupling layers of affine transformations parameterized by two-layer neural networks of 50 units per layer. The initial distribution was a standard isotropic gaussian $𝐳_{0}∼𝒩⁢(,I)$ mapped to a support of $𝐳_{i}\in[-5,5]$. We used an augmented lagrangian coefficient of $c_{0}=10^{2}$, a batch size $n=100$, and $\beta=2$. The distribution was the greatest EPI distribution to converge across five random seeds with criteria $N_{test}=25$.

The bend in the EPI distribution is not a spurious result of the EPI optimization. The structure discovered by EPI matches the shape of the set of points returned from brute-force random sampling (Figure 4—figure supplement 5A) These connectivities were sampled from a uniform distribution over the range of each connectivity parameter, and all parameters producing accuracy in each task within the range of 60% to 90% were kept. This set of connectivities will not match the distribution of EPI exactly, since it is not conditioned on the emergent property. For example, the parameter set returned by the brute-force search is biased toward lower accuracies (Figure 4—figure supplement 5B).

#### Mode identification with EPI

We found one mode of the EPI distribution for fixed values of $s⁢W$ from 1 to −1 in steps of 0.25. To begin, we chose an initial parameter value from 500 parameter samples $𝐳∼q_{𝜽}⁢(𝐳∣𝒳)$ that had closest $s⁢W$ value to 1. We then optimized this estimate of the mode (for fixed $s⁢W$) using probability gradients of the deep probability distribution for 500 steps of gradient ascent with a learning rate of $5\times10^{-3}$. The next mode (at $s⁢W=0.75$) was found using the previous mode as the initialization. This and all subsequent optimizations used 200 steps of gradient ascent with a learning rate of $1\times10^{-3}$, except at $s⁢W=-1$ where a learning rate of $5\times10^{-4}$ was used. During all mode identification optimizations, the learning rate was reduced by half (decay = 0.5) after every 100 iterations.

#### Sample grouping by mode

For the analyses in Figure 5C and Figure 5—figure supplement 1, we obtained parameters for each step along the continuum between regimes 1 and 2 by sampling from the EPI distribution. Each sample was assigned to the closest mode $𝐳^{*}⁢(s⁢W)$. Sampling continued until 500 samples were assigned to each mode, which took 2.67 s (5.34 ms/sample-per-mode). It took 9.59 min to obtain just five samples for each mode with brute force sampling requiring accuracies between 60% and 90% in each task (115 s/sample-per-mode). This corresponds to a sampling speed increase of roughly 21,500 once the EPI distribution has been learned.

#### Sensitivity analysis

At each mode, we measure the sensitivity dimension (that of most negative eigenvalue in the Hessian of the EPI distribution) $𝐯_{1}⁢(𝐳^{*})$. To resolve sign degeneracy in eigenvectors, we chose $𝐯_{1}⁢(𝐳^{*})$ to have negative element in $h⁢W$. This tells us what parameter combination rapid task switching is most sensitive to at this parameter choice in the regime.

#### Connectivity eigendecomposition and processing modes

To understand the connectivity mechanisms governing task accuracy, we took the eigendecomposition of the connectivity matrices $W=Q⁢Λ⁢Q^{-1}$, which results in the same eigenmodes $𝐪_{i}$ for all $W$ parameterized by $𝐳$ (Figure 4—figure supplement 3A). These eigenvectors are always the same, because the connectivity matrix is symmetric and the model also assumes symmetry across hemispheres, but the eigenvalues of connectivity (or degree of eigenmode amplification) change with $𝐳$. These basis vectors have intuitive roles in processing for this task, and are accordingly named the all eigenmode - all neurons co-fluctuate, side eigenmode - one side dominates the other, task eigenmode - the Pro or Anti-populations dominate the other, and diag mode - Pro- and Anti-populations of opposite hemispheres dominate the opposite pair. Due to the parametric structure of the connectivity matrix, the parameters $𝐳$ are a linear function of the eigenvalues $𝝀=[\lambda_{all},\lambda_{side},\lambda_{task}⁢\lambda_{diag}]^{⊤}$ associated with these eigenmodes.

$$
𝐳=A⁢𝝀
$$



$$
A=\frac{1}{4}⁢[11111-1-1111-1-11-11-1].
$$

We are interested in the effect of raising or lowering the amplification of each eigenmode in the connectivity matrix by perturbing individual eigenvalues λ. To test this, we calculate the unit vector of changes in the connectivity $𝐳$ that result from a change in the associated eigenvalues

$$
𝐯_{a}=\frac{\frac{\partial⁡𝐳}{\partial⁡\lambda_{a}}}{|\frac{\partial⁡𝐳}{\partial⁡\lambda_{a}}|_{2}},
$$

where

$$
\frac{\partial⁡𝐳}{\partial⁡\lambda_{a}}=A⁢𝐞_{a},
$$

and for example $𝐞_{all}=[1,0,0,0]^{⊤}$. So $𝐯_{a}$ is the normalized column of A corresponding to eigenmode $a$. The parameter dimension $𝐯_{a}$ ($a\in{all,side,task,and diag}$) that increases the eigenvalue of connectivity $\lambda_{a}$ is $𝐳$-invariant (Equation 109) and $𝐯_{a}⟂𝐯_{b\neqa}$. By perturbing $𝐳$ along $𝐯_{a}$, we can examine how model function changes by directly modulating the connectivity amplification of specific eigenmodes, which have interpretable roles in processing in each task.

#### Modeling optogenetic silencing

We tested whether the inferred SC model connectivities could reproduce experimental effects of optogenetic inactivation in rats (Duan et al., 2021). During periods of simulated optogenetic inactivation, activity was decreased proportional to the optogenetic strength $\gamma\in[0,1]$

$$
x_{\alpha}=(1-\gamma)⁢ϕ⁢(u_{\alpha}).
$$

Delay period inactivation was from $0.8<t<1.2$.
