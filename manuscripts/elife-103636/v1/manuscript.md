# Elucidating the selection mechanisms in context-dependent computation through low-rank neural network modeling

## Authors

- Yiteng Zhang<sup>1</sup> ([ORCID: 0009-0001-5192-521X](https://orcid.org/0009-0001-5192-521X))
- Jianfeng Feng<sup>1</sup> ([ORCID: 0000-0001-5987-2258](https://orcid.org/0000-0001-5987-2258)) †
- Bin Min<sup>2</sup> ([ORCID: 0000-0003-1006-9629](https://orcid.org/0000-0003-1006-9629)) †

### Affiliations

1. School of Data Science, Fudan University Shanghai China ([ROR:013q1eq08](https://ror.org/013q1eq08))
2. Lingang Laboratory Shanghai China
3. Institute of Science and Technology for Brain-Inspired Intelligence, Fudan University Shanghai China ([ROR:013q1eq08](https://ror.org/013q1eq08))
4. Key Laboratory of Computational Neuroscience and Brain-Inspired Intelligence, Fudan University Shanghai China ([ROR:013q1eq08](https://ror.org/013q1eq08))

† Corresponding author

## Abstract

Humans and animals exhibit a remarkable ability to selectively filter out irrelevant information based on context. However, the neural mechanisms underlying this context-dependent selection process remain elusive. Recently, the issue of discriminating between two prevalent selection mechanisms—input modulation versus selection vector modulation—with neural activity data has been highlighted as one of the major challenges in the study of individual variability underlying context-dependent decision-making (CDM). Here, we investigated these selection mechanisms through low-rank neural network modeling of the CDM task. We first showed that only input modulation was allowed in rank-one neural networks and additional dimensions of network connectivity were required to endow neural networks with selection vector modulation. Through rigorous information flow analysis, we gained a mechanistic understanding of why additional dimensions are required for selection vector modulation and how additional dimensions specifically contribute to selection vector modulation. This new understanding then led to the identification of novel neural dynamical signatures for selection vector modulation at both single neuron and population levels. Together, our results provide a rigorous theoretical framework linking network connectivity, neural dynamics, and selection mechanisms, paving the way towards elucidating the circuit mechanisms when studying individual variability in context-dependent computation.

## Introduction

Imagine you are playing a card game. Your strategy depends not only on the cards you have but also on what your opponents are doing. As the game progresses, you adjust your moves based on their actions to increase your chances of winning. This example illustrates how much of our decision-making, both in everyday life and in more complex tasks, is influenced by the context in which we are acting (Miller and Cohen, 2001; Roy et al., 2010; Mante et al., 2013; Saez et al., 2015; Siegel et al., 2015; Bernardi et al., 2020; Takagi et al., 2021; Flesch et al., 2022; Barbosa et al., 2023). However, how the brain performs such context-dependent computation remains elusive (Fusi et al., 2016; Cohen, 2017; Badre et al., 2021; Okazawa and Kiani, 2023).

Using a monkey CDM behavioral paradigm, a recent work uncovered a novel mechanism in the brain that helps adjust decisions based on context (Mante et al., 2013). This mechanism, called ‘selection vector modulation,’ is distinct from the early sensory input modulation counterpart (Desimone and Duncan, 1995; Noudoost et al., 2010). More recently, building on this work, new research with rats supported a novel theoretical framework regarding how the brain makes context-dependent decisions and revealed how this process may vary between individuals (Pagan et al., 2025). Critically, this theoretical framework pointed out that current neurophysiological data fell short of distinguishing between selection vector modulation and sensory input modulation, calling for rethinking what kind of evidence is required for differentiating different selection mechanisms.

Here, we aim to address this challenge by using the low-rank recurrent neural network (RNN) modeling approach (Landau and Sompolinsky, 2018; Mastrogiuseppe and Ostojic, 2018; Kadmon et al., 2020; Schuessler et al., 2020; Beiran et al., 2021; Beiran et al., 2023; Dubreuil et al., 2022; Valente et al., 2022; Ostojic and Fusi, 2024). This approach allowed us to simulate and better understand the neural processes behind context-dependent computation. More importantly, endowed by the low-rank RNN theory (Beiran et al., 2021; Dubreuil et al., 2022), this approach allowed us to develop a set of analyses and derivations uncovering a previously unknown link between connectivity dimensionality, neural dynamics, and selection mechanisms. This link then led to the identification of novel neural dynamical signatures for selection vector modulation at both the single neuron and population levels. Together, our work provides a neural circuit basis for different selection mechanisms, shedding new light on the study of individual variability in neural computation underlying the ubiquitous context-dependent behaviors.

## Results

### Task paradigm, key concept, and modeling approach

The task paradigm we focused on is the pulse-based CDM task (Pagan et al., 2022), a novel rat-version CDM paradigm inspired by the previous monkey CDM work (Mante et al., 2013). In this paradigm, rats were presented with sequences of randomly-timed auditory pulses that varied in both location and frequency (Figure 1A). In alternating blocks of trials, rats were cued by an external context signal to determine the prevalent location (in the ‘LOC’ context) or frequency (in the ‘FRQ’ context). Note that compared to the continuous sensory input setting in previous works (e.g. Mante et al., 2013), this pulse-based sensory input setting allowed the experimenters to better characterize both behavioral and neural responses (Pagan et al., 2022). We will also demonstrate the unique advantage of this pulse-based input setting later in the present study (e.g. Figure 7).

![Figure 1.](https://cdn.elifesciences.org/articles/103636/elife-103636-fig1-v1.jpg)

**Figure 1.:** (A) A pulse-based context-dependent decision-making task (adapted from Pagan et al., 2022). In each trial, rats were first cued by sound to indicate whether the current context was the location (LOC) context or the frequency (FRQ) context. Subsequently, rats were presented with a sequence of randomly timed auditory pulses. Each pulse could come from either the left speaker or right speaker and could be of low frequency (6.5 kHz, light blue) or high frequency (14 kHz, dark blue). In the LOC context, rats were trained to turn right (left) if more pulses are emitted from the right (left) speaker. In the FRQ context, rats were trained to turn right (left) if there are more (fewer) high-frequency pulses compared to low-frequency pulses. (B) Two prevalent candidate mechanisms for context-dependent decision-making. Top: The input modulation mechanism. In this scenario, while the selection vector remains invariant across contexts, the stimulus input representation is altered in a way such that only the relevant stimulus input representation (i.e. the location input in the LOC context and the frequency input in the FRQ context) is well aligned with the selection vector, thereby fulfilling the requirement of context-dependent computation. Bottom: The selection vector modulation mechanism. In this scenario, although the stimulus input representation remains constant across different contexts, the selection vector itself is altered by the context input to align with the relevant sensory input. Red line: line attractor (choice axis). Green arrow: selection vector. Thick gray and blue arrows stand for the projections of the location and frequency input representation directions on the space spanned by the line attractor and selection vector, respectively. The small gray arrows stand for direction of relaxing dynamics. (C) Networks with distinct selection mechanisms may lead to similar trial-averaged neural dynamics (adapted from Pagan et al., 2022). In a model with pure input modulation, the irrelevant sensory input can still be represented by the network in a direction orthogonal to the selection vector. Therefore, using the classical targeted dimensionality reduction method (Mante et al., 2013), both the input modulation model (top) and the selection vector modulation model (bottom) would exhibit similar trial-averaged neural dynamics as shown in Pagan et al., 2022. (D) The setting of low-rank RNN modeling for the CDM task. The network has four input channels. Input 1 and input 2 represent two sensory inputs, while the other two channels indicate the context. The connectivity matrix $J$ is constrained to be low-rank, expressed as $\frac{1}{N}\sumr=1Rm_{r}n_{r}^{T}$, where $N$ is the number of neurons, $R$ is the matrix’s rank, and $m_{r}n_{r}^{T}$ is a rank-1 matrix formed by the outer product of two N-dimensional connectivity vectors $m_{r}$ and $n_{r}$.

To solve this task, rats had to select the relevant information for the downstream evidence accumulation process based upon the context. There were at least two different mechanisms capable of performing this selection operation, i.e., selection vector modulation and input modulation (Mante et al., 2013; Pagan et al., 2022). To better introduce these mechanisms, we first reviewed the classical linearized dynamical systems analysis and the concept of selection vector (Figure 1B; Mante et al., 2013; Sussillo and Barak, 2013; Maheswaranathan et al., 2019; Maheswaranathan and Sussillo, 2020; Nair et al., 2023). In the linearized dynamical systems analysis, the neural dynamics around the choice axis (Figure 1B, red line) is approximated by a line attractor model. Specifically, the dynamics in the absence of external input can be approximated by the following linear equation $\frac{dr}{dt}=Mr$, where M is a matrix with one eigenvalue being equal to 0 and all other eigenvalues having a negative real part. For brevity, let us denote the left eigenvector of the 0 eigenvalue as $s$. In this linear dynamical system, the effect of any given perturbation can be decomposed along the directions of different eigenvectors: the projection onto the $s$ direction will remain constant while the projections onto all other eigenvectors will exponentially decay to zero. Thus, for any given input $I$, only the component projecting onto the $s$ direction (i.e. $I⋅s$) can be integrated along the line attractor (see Methods for more details). In other words, $s$ serves as a vector selecting the input information, which is known as the ‘selection vector’ in the literature (Mante et al., 2013).

Two distinct selection mechanisms can then be introduced based upon the concept of selection vector (Pagan et al., 2022). Specifically, to perform the CDM task, the stimulus input (LOC input, for example) must have a larger impact on evidence accumulation in the relevant context (LOC context) than in the irrelevant context (FRQ context). That is, $I⋅s$ must be larger in the relevant context than in the irrelevant context. The difference between these two can be decomposed into two components:

$$
Δ(I⋅s)=ΔI⋅s¯+I¯⋅Δs,
$$

where the $Δ$ symbol denotes difference across two contexts (relevant – irrelevant) and the bar symbol denotes average across two contexts (see Methods for more details). The first component $ΔI⋅s¯$ is called input modulation in which the change of input information across different contexts is emphasized (Figure 1B, top). In contrast, the second component $I¯⋅Δs$ is called selection vector modulation in which the change of selection vector across contexts is instead highlighted (Figure 1B, bottom).

While these two selection mechanisms were clearly defined, recent work showed that it is actually challenging to differentiate them through neural dynamics (Pagan et al., 2022). For example, both input modulation and selection vector modulation can lead to similar trial-averaged neural dynamics through targeted dimensionality reduction (Figure 1C; Pagan et al., 2022). Take the input modulation as an example (Figure 1C, top). One noticeable aspect we can observe is that the input information (e.g. location information) is preserved in both relevant (LOC context) and irrelevant contexts (FRQ context), which seems contradictory to the definition of input modulation. What is the mechanism underlying this counterintuitive result? As Pagan et al. pointed out earlier, input modulation is not the input change ($ΔI$) per se. Rather, it means the change of input multiplied by selection vector (i.e. $ΔI⋅s¯$). Therefore, for the input modulation, while input information indeed is modulated by context along the selection vector direction, input information can still be preserved across contexts along other directions orthogonal to the selection vector, which explains the counterintuitive result and highlights the challenge of distinguishing input modulation from selection vector modulation in experiments (Pagan et al., 2022).

In this study, we sought to address this challenge using the low-rank RNN modeling approach. In contrast to the ‘black-box’ vanilla RNN approach (e.g. Mante et al., 2013), the low-rank RNN approach features both well-controlled model complexity and mechanistic transparency, potentially providing a fresh view into the mechanisms underlying the intriguing selection process. Specifically, the low-rank RNNs we studied here implemented an input-output task structure similar to the classical RNN modeling work of CDM (Figure 1D; Mante et al., 2013). More concretely, the hidden state $x$ of a low-rank RNN with $N$ neurons evolves over time according to

$$
\tau\frac{dx}{dt}=−x+Jϕ(x)+\sums=12I_{s}u_{s}(t)+\sums=12I_{s}^{ctx}u_{s}^{ctx}(t)
$$

where $J=\sumr=1Rm_{r}n_{r}^{T}/N$ is a low-rank matrix with $R$ output vectors $m_{r},r=1,⋯,R$ and R input-selection vectors $n_{r},r=1,⋯,R$, $\tau$ is the time constant of single neurons, $ϕ$ is the nonlinear activation function, $u_{s}t,s=1,2$ embedded into the network through $I_{s}$ mimic the location and frequency click inputs, and $u_{s}^{ctx}t,s=1,2$ embedded through $I_{s}^{ctx}$ indicate whether the current context is location or frequency. The output of the network is a linear projection of neural activity (see Methods for more model details). Under this general architectural setting, on one hand, through controlling the rank $R$ of the matrix $J$ during backpropagation training, we can determine the minimal rank required for performing the CDM task and reverse-engineer the underlying mechanism, which will be demonstrated in Figure 2. On the other hand, recent theoretical progress of low-rank RNNs (Beiran et al., 2021; Beiran et al., 2021; Dubreuil et al., 2022) enabled us to explicitly construct neural network models with mechanistic transparency, complementing the reverse-engineering analysis (Mante et al., 2013; Sussillo and Barak, 2013), which will be shown in Figure 3.

![Figure 2.](https://cdn.elifesciences.org/articles/103636/elife-103636-fig2-v1.jpg)

**Figure 2.:** (A) Illustration of rank-1 connectivity matrix structure. Left: a rank-1 matrix can be represented as the outer product of an output vector $m_{dv}$ and an input-selection vector $n_{dv}$, of which the input-selection vector $n_{dv}$ played the role of selecting the input information through its overlap with the input embedding vectors $I_{1}$ and $I_{2}$. The context signals are fed forward to the network with embedding vectors $I_{1}^{ctx}$ and $I_{2}^{ctx}$. Since the overlap between the context embedding vectors and input-selection vector $n_{dv}$ are close to 0, for simplicity, we omitted the context embedding vectors here. Right: an example of the trained rank-1 connectivity structure characterized by the cosine angle between every pair of connectivity vectors (see Figure 2—figure supplement 1 and Methods for details). (B) The psychometric curve of the trained rank-1 recurrent neural networks (RNNs). In context 1, input 1 strongly affects the choice, while input 2 has little impact on the choice. In context 2, the effect of input 1 and input 2 on the choice is exchanged. The shaded area indicates the standard deviation. Ctx. 1, context 1. Ctx. 2, context 2. (C) Characterizing the change of selection vector as well as input representation direction across contexts using cosine angle. The selection vector in each context is computed using linearized dynamical system analysis. The input representation direction is defined as the elementwise multiplication between the single neuron gain vector and the input embedding vector (see Methods for details). ***p<0.001, one-way ANOVA test, n=100. Inp., input. Rep., representation. (D) Characterizing the overlap between the input representation direction and the selection vector. ***p<0.001, one-way ANOVA test, n=100. Dir., direction. (E) The state space analysis, for example, trained rank-1 RNN. The space is spanned by the line attractor axis (red line) and the selection vector (green arrow). (F) Trial-averaged dynamics for example rank-1 RNN. We applied targeted dimensionality reduction (TDR) to identify the choice, input 1, and input 2 axes. The neuron activities were averaged according to input 1 strength, choice and context, and then projected onto the choice and input 1 axes to obtain the trial-averaged population dynamics (see Methods for details).

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/103636/elife-103636-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** (A) Projection of the connectivity space for the example rank-1 RNN. Each dot denotes a neuron. On each panel, the x and y coordinates of the $i$-th dot represent the $i$-th entry of the corresponding connectivity vectors.

![Figure 3.](https://cdn.elifesciences.org/articles/103636/elife-103636-fig3-v1.jpg)

**Figure 3.:** (A) Illustration of the utilized rank-3 connectivity matrix structure. Left: the rank-3 matrix can be represented as the summation of three outer products, including the one with the output vector $m_{dv}$ and the input-selection vector $n_{dv}$, the one with the output vector $m_{iv_{1}}$ and the input-selection vector $n_{iv_{1}}$, and the one with the output vector $m_{iv_{2}}$ and the input-selection vector $n_{iv_{2}}$, of which the input-selection vectors $n_{iv_{1}}$ and $n_{iv_{2}}$ played the role of selecting the input information from $I_{1}$ and $I_{2}$, respectively. Right: the connectivity structure of the handcrafted RNN model characterized by the cosine angle between every pair of connectivity vectors (see Figure 3—figure supplement 1 and Methods for more details). (B) The psychometric curve of the handcrafted rank-3 recurrent neural network (RNN) model. (C) Characterizing the change of selection vector as well as input representation direction across contexts using cosine angle. The selection vector in each context is computed using linearized dynamical system analysis. The input representation direction is defined as the elementwise multiplication between the single neuron gain vector and the input embedding vector (see Methods for details). ***p<0.001, one-way ANOVA test, n=100. (D) Characterizing the overlap between the input representation direction and the selection vector. ***p<0.001, one-way ANOVA test, n=100. (E) The state space analysis for example rank-3 RNN. The space is spanned by the line attractor axis (red line, invariant across contexts), selection vector in context 1 (green arrow, top panel), and selection vector in context 2 (green arrow, bottom panel). (F) Trial-averaged dynamics for example rank-3 RNN.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/103636/elife-103636-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** (A) Projection of the connectivity space for the example rank-3 RNN. This RNN has 30,000 neurons divided into three populations. Dots of the same color represent neurons within the same population. The inset in the top right corner shows the projection on the two context input axes. For brevity, we did not include the projections onto the context input axis and other connectivity vectors. Within each population, the context input axis is independent of the other connectivity vectors. This independence implies that the context signal only affects the average sensitivity of each neuron population, thereby serving a modulatory function.

### No selection vector modulation in rank-one models

In the literature, it was found that rank-one RNN models suffice to solve the CDM task (Dubreuil et al., 2022). Here, we further asked whether selection vector modulation can occur in rank-one RNN models. To this end, we trained many rank-1 models (see Methods for details) and found that indeed having rank-1 connectivity (e.g. with the overlap structure listed in Figure 2A; for the detailed connectivity structure, see Figure 2—figure supplement 1) is sufficient to perform the CDM task, consistent with the earlier work. As shown in Figure 2B, in context 1, the decision was made based on input-1 evidence, ignoring input-2 evidence, indicating that the network can effectively filter out irrelevant information. To answer what kind of selection mechanisms underlie this context-dependent computation, we computed the selection vector in two contexts through linearized dynamical systems analysis (Sussillo and Barak, 2013). Cosine angle analysis revealed that selection vectors kept invariant across different contexts (Figure 2C, left), indicating no selection vector modulation. This result was preserved across different hyperparameter settings (such as different regularization coefficients or activation functions). Note that this result actually can be mathematically proved (Pagan et al., 2023; Pagan et al., 2025). Therefore, our modeling result reconfirmed the limitation of rank-one models on selection vector modulation.

While the selection vector was not altered by contexts, the direction of input representations changed significantly across different contexts (Figure 2C, left; see Methods for the definition of input representation direction). Further analysis revealed that the overlap between the input representation direction and the unchanged selection vector is large in the relevant context and small in the irrelevant context, supporting the input modulation mechanism (Figure 2D). These results indicate that while a rank-1 network can perform the task, it can only achieve flexible computation through input modulation (Figure 2E). Importantly, when applying a similar targeted dimensionality reduction method to this rank-1 model, we found that the irrelevant sensory input information was indeed well-represented in neural activity state space (Figure 2F), supporting the conclusion made in the Pagan et al. paper that the presence of irrelevant sensory input in neural state space cannot be used as a reliable indicator for the absence of input modulation (Figure 1C).

In summary, we conclude that to study the mechanism of selection vector modulation, instead of limiting to the simplest model of CDM task, it is necessary to explore network models with higher ranks.

### A low-rank model with pure selection vector modulation

To study the mechanism of selection vector modulation, we designed a rank-3 neural network model, with one additional rank for each sensory input feature (i.e. $m_{iv_{1}}n_{iv_{1}}^{T}$ for input 1 and $m_{iv_{2}}n_{iv_{2}}^{T}$ for input 2; Figure 3A, left). Specifically, we ensured that $I_{1}(I_{2})$ has a positive overlap with $n_{iv_{1}}(n_{iv_{2}})$ and zero overlap with $n_{dv}$, while $m_{iv1}(m_{iv_{2}})$ has a positive overlap with $n_{dv}$ (Figure 3A, right; see Figure 3—figure supplement 1 and Methods for more details). Moreover, our rank-3 network relies on a multi-population structure, consistent with the notion that higher-rank networks still require a multi-population structure to perform flexible computations (Dubreuil et al., 2022). This configuration implies that the stimulus input 1 (2) is first selected by $n_{iv_{1}}(n_{iv_{2}})$, represented by $m_{iv_{1}}(m_{iv_{2}})$, and subsequently selected by $n_{dv}$ before being integrated by the accumulator. In principle, this sequential selection process enables more sophisticated contextual modulations.

We confirmed that a model with such a connectivity structure can perform the task (Figure 3B) and then conducted an analysis similar to that performed for rank-1 models. Unlike the rank-1 model, the selection vector for this rank-3 model changes across contexts while the input representation direction remains invariant (Figure 3C). Further analysis revealed that the overlap between the selection vector and the unchanged input representation direction is large in the relevant context and small in the irrelevant context (Figure 3D), supporting a pure selection vector modulation mechanism (Figure 3E) distinct from the input modulation counterpart shown in Figure 2D. When applying a similar targeted dimensionality reduction method to this rank-3 model, as what we expected, we found that both relevant and irrelevant sensory input information was indeed well-represented in neural activity state space (Figure 3F), which was indistinguishable from the input modulation counterpart (Figure 2F).

Together, through investigating these two extreme cases—one with pure input modulation and the other with pure selection vector modulation, we not only reconfirm the challenge of distinguishing input modulation from selection modulation based on neural activity data (Pagan et al., 2022) but also point out the previously unknown link between selection vector modulation and network connectivity dimensionality.

### Understanding context-dependent modulation in Figs. 2 and 3 through pathway-based information flow analysis

What is the machinery underlying this link between selection vector modulation and network connectivity dimensionality? One possible way to address this issue is through linearized dynamical systems analysis: first computing the selection vector and the sensory input representation direction through reverse-engineering (Sussillo and Barak, 2013) and then calculating both selection vector modulation and input modulation according to Equation 1. However, the connection between the network connectivity dimensionality and the selection vector obtained through reverse-engineering is implicit and in general non-trivial (Pagan et al., 2023), hindering further investigation of the underlying machinery. Here, by combining recent theoretical progress in low-rank RNNs (Mastrogiuseppe and Ostojic, 2018; Dubreuil et al., 2022) and linearized dynamical systems analysis (Sussillo and Barak, 2013), we introduced a novel pathway-based information flow analysis approach, providing an explicit link between network connectivity, neural dynamics, and selection mechanisms.

To start with, the low-rank RNN dynamics (i.e. Equation 2) can be described by an information flow graph, with each task variable as a node and each effective coupling between task variables as an edge (Mastrogiuseppe and Ostojic, 2018; Dubreuil et al., 2022). Take the rank-1 RNN in Figure 2 as an example. A graph with three nodes, including two input variables $κ_{p_{s}}t,s=1,2$ and one decision variable $κ_{dv}t$, suffices (Figure 4A; see Methods for more details). In this graph, the dynamical evolution of the task variable $κ_{dv}$ can be expressed as:

$$
\tau\frac{dκ_{dv}}{dt}=−κ_{dv}+E_{inp_{1}→dv}κ_{inp_{1}}+E_{inp_{2}→dv}κ_{inp_{2}}+E_{dv→dv}κ_{dv}
$$

where the effective coupling $E_{inp_{s}→dv}$ from the input variable $κ_{inp_{s}}$ to the decision variable $κ_{dv}$ is equal to the overlap between the input representation direction $I~_{s}$ (each element is defined by $I~_{s,i}=ϕ^{`}x_{i}I_{s,i}$) and the input-selection vector $n_{dv}$. More precisely, $E_{inp_{s}→dv}=⟨I∼_{s},n_{dv}⟩$, where $a,b$ is defined as $\frac{1}{N}\sum_{1}^{N}a_{i}b_{i}$ for two length-$N$ vectors. Since the input representation direction $I~_{s}$ depends on the single neuron gain $ϕ^{`}$ and the context input can modulate this gain, the effective coupling $E_{inp_{s}→dv}$ is context-dependent. Indeed, as shown in Figure 4A, Figure 4—figure supplement 1A, $E_{inp_{1}→dv}$ exhibited a large value in context 1 but was negligible in context 2, while $E_{inp_{2}→dv}$ exhibited a large value in context 2 but was negligible in context 1. In other words, information from the input variable can arrive at the decision variable only in the relevant context, which exactly is the computation required by the CDM task.

![Figure 4.](https://cdn.elifesciences.org/articles/103636/elife-103636-fig4-v1.jpg)

**Figure 4.:** (A) The information flow graph of the rank-1 model presented in Figure 2. In this graph, nodes represented task variables communicating with each other through directed connections (denoted as $E_{sender→receiver}$) between them. Note that $E_{sender→receiver}$ is the overlap between the representation direction of the sender variable (e.g. the representation directions of input variable and decision variable $I~_{inp}$ and $m~_{dv}$) and the input-selection vector of the receiver variable (e.g. the input-selection vector of decision variable $n_{dv}$). As such, $E_{sender→receiver}$ naturally inherits the context dependency from the representation direction of task variable: while $E_{inp_{1}→dv}$ exhibited a large value and $E_{inp_{2}→dv}$ was negligible in context 1, the values of these two exchanged in context 2. (B) Illustration of information flow dynamics in (A) through discretized steps. At step 1, sensory information $A_{1}$ and $A_{2}$ were placed in $inp1$ and $inp2$ slots, respectively. Depending on the context, different information contents (i.e. $E_{inp_{1}→dv}A_{1}$ in context 1 and $E_{inp_{2}→dv}A_{2}$ in context 2) entered into the $dv$ slot at step 2 and were maintained by recurrent connections in the following steps, which is desirable for the context-dependent decision-making task. (C) The information flow graph of the rank-3 model presented in Figure 3. Different from (A), here to arrive at the $dv$ slot, the input information has to first go through an intermediate slot (e.g. the $p_{1}→iv_{1}→dv$ pathway in context 1 and the $p_{2}→iv_{2}→dv$ pathway in context 2). (D) Illustration of information flow dynamics in (C) through discretized steps.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/103636/elife-103636-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** (A) Effective coupling between task variables for 100 trained rank-1 RNNs (Figure 2) in each context. Effective coupling between two task variables is defined as the overlap between the corresponding representation vector and input-selection vector. For example, the effective coupling from input 1 to decision variable $E_{inp_{1}→dv}$ is the overlap between $I~_{1}$ and $n_{dv}$ ($I~_{1},n_{dv}$). As can be seen, the effective couplings of recurrent connection ($E_{dv→dv}$) are close to 1 in both contexts. The effective coupling from input task variables to decision variable is large in the relevant context (i.e. $E_{inp_{1}→dv}$ in context 1 and $E_{inp_{2}→dv}$ in context 2) and is negligible in the irrelevant context. (B) Effective coupling between task variables for 100 trained rank-3 RNNs (Figure 3) in each context. The effective coupling for recurrent connectivity ($E_{dv→dv},i.e.$ overlap between $m~_{dv}$ and $n_{dv}$) is close to 1 in both contexts. There is no direction connectivity from the input task variable to the decision variable since $E_{inp_{s}→dv},s=1,2$ are zero in both contexts. The difference between $E_{iv_{s}→dv}$ in the two contexts leads to selection vector modulation.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/103636/elife-103636-fig4-figsupp2-v1.jpg)

**Figure 4—figure supplement 2.:** (A) Task setting for single pulse input. We study the neural activity dynamics for low-rank recurrent neural networks (RNN) when they receive pulse input. For simplicity, only the RNNs’ neural activity given a pulse from input 1 in context 1 is considered. (B) Illustration of neural activity for rank-1 RNN given pulse input. For rank-1 RNN (Figure 2), dynamics of $xt−I_{1}^{ctx}$ is always constrained in the subspace spanned by ${I_{1},m_{dv}}$ , with the corresponding coefficients being the input task variable $(k_{inp_{1}})$ and decision variable $(k_{dv})$, respectively. Moreover, the neural activity $x(t)$ is always constrained in a line (dashed line) orthogonal to the selection vector. (C) Task variable dynamics for rank-1 RNN given pulse input. We run the example RNN for a given input and project the results onto each axis to obtain the dynamics of each task variable (solid line). The analytical expressions for the dynamics of each task variable are provided in the methods section (dotted line). The simulated RNN results closely match the theoretical values. (D) Illustration of neural activity for rank-3 RNN given pulse input. For rank-3 RNN (Figure 3), dynamics of $xt−I_{1}^{ctx}$ are always constrained in the subspace spanned by ${I_{1},m_{iv},m_{dv}}$, with the corresponding coefficients being input task variable ($k_{inp_{1}}$), intermediate task variable ($k_{iv_{1}}$) and decision variable ($k_{dv}$), respectively. (E) Task variable dynamics for rank-3 RNN given pulse input. Solid lines denote task variable dynamics calculated numerically by RNN simulation and dotted lines denote theoretical results.

To get a more intuitive understanding of the underlying information flow process, we discretized the equation and followed the information flow step by step. Specifically, by discretizing Equation 3 using Euler’s method with a time step equal to the time constant $\tau$ of the system, we get

$$
κ_{dv}(t+\tau)=E_{inp_{1}→dv}κ_{inp_{1}}(t)+E_{inp_{2}→dv}κ_{inp_{2}}(t)+E_{dv→dv}κ_{dv}(t)
$$

Take context 1 as an example (Figure 4B, top panel). Initially, there is no information in the system. In step 1, pulse inputs of size $A_{1}$ and $A_{2}$ are placed in the $p_{1}$ and $p_{2}$ slots, respectively. The information from these slots, after being multiplied by the corresponding effective coupling, then flows to the $dv$ slot. In context 1, $E_{inp_{2}→dv}≈0$, meaning only the content from the $p_{1}$ slot can arrive at the $dv$ slot. Consequently, in step 2, the information content in the $dv$ slot would be $E_{inp_{1}→dv}A_{1}$. The following steps will replicate step 2 due to the recurrent connectivity of the $dv$ slot. The scenario in context 2 is similar to context 1, except that only the content from the $p_{2}$ slot arrives at the $dv$ slot (Figure 4B, bottom panel). The continuous dynamics for each task variable given pulse input is displayed in Figure 4—figure supplement 2A–C.

The same pathway-based information flow analysis can also be applied to the rank-3 model (Figure 4C and D). In this model, similar to the rank-1 models, there are input variables ($k_{inp_{1}}$ and $k_{inp_{2}}$) and decision variable $(k_{dv})$. Additionally, it includes intermediate variables ($k_{iv_{1}}$ and $k_{iv_{2}}$) corresponding to the activity along the $m_{iv_{1}}$ and $m_{iv_{2}}$ axes. In this scenario, instead of flowing directly from the input to the decision variable, the information flows first to the intermediate variables and then to the decision variable. These intermediate variables act as intermediate nodes. Introducing these nodes does more than simply increase the steps from the input variable to the decision variable. In the rank-1 case, the context signals can only modulate the pathway from the input to the decision variable. However, in the rank-3 case, context signals can modulate the system in two ways: from the input to the intermediate variables and from the intermediate variables to the decision variable.

Take the rank-3 model introduced in Figure 3 as an example. Context signals did not alter the representation of input signals, leading to constant effective couplings (i.e. constant $E_{inp_{1}→iv_{1}}$ and $E_{inp_{2}→iv_{2}}$) from input to intermediate variables across contexts. Instead, it changed the effective coupling from the intermediate variables to the decision variable (i.e. large $E_{iv_{1}→dv}$ in context 1 and near zero $E_{iv_{1}→dv}$ in context 2; Figure 4C, Figure 4—figure supplement 1B). Consider the context 1 scenario in the discrete case. In step 1, pulse inputs of size $A_{1}$ and $A_{2}$ are placed in the $p_{1}$ and $p_{2}$ slots, respectively. In step 2, information flows to the intermediate slots, with $E_{inp_{1}→iv_{1}}A_{1}$ in the $iv_{1}$ slot and $E_{inp_{2}→iv_{2}}A_{2}$ in the $iv_{2}$ slot. In step 3, only the information in the $iv_{1}$ slot flows to the $dv$ slot, with the information content being $E_{inp_{1}→iv_{1}}E_{iv_{1}→dv}A_{1}$ (Figure 4D, top panel). The scenario in context 2 is similar to context 1, except that only the content from the $iv_{2}$ slot reaches the $dv$ slot in the third step, with the content being $E_{inp_{2}→iv_{2}}E_{iv_{2}→dv}A_{2}$ (Figure 4D, bottom panel). The continuous dynamics for each task variable given pulse input is displayed in Figure 4—figure supplement 2D, E.

Together, this pathway-based information flow analysis provides an in-depth understanding of how the input information can be routed to the accumulator depending on the context, laying the foundation for a novel pathway-based information flow definition of selection vector and input contextual modulations.

### Information flow-based definition of selection vector modulation and selection vector for more general cases

Based on the understanding gained from the pathway-based information flow analysis, we now provide a novel definition of input modulation and selection vector modulation distinct from the one in Equation 1. To begin with, we first considered a model with mixed input and selection vector modulation (Figure 5, left), instead of studying extreme cases (i.e. one with pure input modulation in Figure 2 and the other with pure selection vector modulation in Figure 3). In this more general model, input information can either go directly to the decision variable (with effective coupling $E_{inp→dv}$) or first pass through the intermediate variables before reaching the decision variable (with effective coupling $E_{inp→iv}$ and $E_{iv→dv}$ respectively). Applying the same information flow analysis, we see that a pulse input of unit size will ultimately reach the $dv$ slot with a magnitude of $E_{inp→dv}+E_{inp→iv}E_{iv→dv}$ (Figure 5A, right; see Methods for more details). In other words, the total effective coupling $E_{tol}$ from the input to the decision variable is equal to $E_{inp→dv}+E_{inp→iv}E_{iv→dv}$. Now, it is straightforward to decompose the context-dependent modulation of $E_{tol}$ in terms of input or selection vector change:

$$
ΔE_{tol}=(ΔE_{inp→dv}+ΔE_{inp→iv}E¯_{iv→dv})+(E¯_{inp→iv}ΔE_{iv→dv}),
$$

in which the first component $ΔE_{inp→dv}+ΔE_{inp→iv}E¯_{iv→dv}$ stands for the change of input representation (termed as input modulation) and the second component $E¯_{inp→iv}ΔE_{iv→dv}$ is the one without changing the stimulus input representation (termed as selection vector modulation).

![Figure 5.](https://cdn.elifesciences.org/articles/103636/elife-103636-fig5-v1.jpg)

**Figure 5.:** (A) A pathway-based decomposition of contextual modulation in a model with both input and selection vector modulations. This definition is based on an explicit formula of the effective connection from the input variable to the decision variable in the model (i.e. $E_{inp→dv}+E_{inp→iv}E_{iv→dv}$; see Method for details). The input modulation component is then defined as the modulation induced by the change of the input representation direction across contexts. The remaining component is then defined as the selection vector modulation one. (B) Illustration of contextual modulation decomposition introduced in Pagan et al., 2022. In this definition, the selection vector has to be first reverse-engineered through linearized dynamical systems analysis. The input modulation component is then defined as the modulation induced by the change of input representation direction across contexts, while the selection vector modulation component is defined as the one induced by the change of the selection vector across contexts. (C) A family of handcrafted recurrent neural networks (RNNs) with both input and selection vector modulations. $\alpha,$ $\beta$, and $η$ represent the associated effective coupling between task variables. In this model family, the $inp→dv$ pathway, susceptible to the input modulation, is parameterized by $\alpha$ while the $inp→iv→dv$ pathway, susceptible to the selection vector modulation, is parameterized by $\beta$ and $η$. As such, the ratio of the input modulation to the selection vector modulation can be conveniently controlled by adjusting $\alpha,$ $\beta$, and $η$. (D) Comparison of pathway-based definition in (A) with the classical definition in (B) using the model family introduced in (C).

We then asked if this pathway-based definition is equivalent to the one in Equation 1 based on linearized dynamical system analysis (Figure 5; Pagan et al., 2022). To answer this question, we numerically compared these two definitions using a family of models with both input and selection vector modulations (Figure 5C; see Methods for model details) and found that these two definitions produced the same proportion of selection vector modulation across a wide range of parameter regimes (Figure 5D). Together with theoretical derivation of equivalence (see Methods), this consistency confirmed the validity of our pathway-based definition of contextual modulation decomposition.

Having elucidated the pathway-based definitions of input and selection vector modulation, we next provide a novel pathway-based definition of selection vector. For the network depicted in Figure 5A, the total effective coupling $E_{inp→dv}+E_{inp→iv}E_{iv→dv}$ can be rewritten as $I~,n_{tol}$, where $I~$ is the input representation direction and $n_{tol}=n_{dv}+m~_{iv},n_{dv}n_{iv}$. This reformulation aligns with the insight that the amount of input information that can be integrated by the accumulator is determined by the dot product between the input representation direction $I~$ and the selection vector. Thus, $n_{tol}$ is the selection vector of the circuit in Figure 5A.

To better understand why selection vector has such a formula, we visualized the information propagation from input to the choice axis using a low-rank matrix (Figure 6A). Specifically, it comprises two components, each corresponding to a distinct pathway. For the first component, input information is directly selected by $n_{dv}$. For the second component, input information is sent first to the intermediate variable and then to the decision variable. This pathway involves two steps: in the first step, the input representation vector is selected by $n_{iv}$, and in the second step, to arrive at the choice axis, the selected information has to be multiplied by the effective coupling $E_{iv→dv}=m~_{iv},n_{dv}$. By concatenating these two steps, information propagation from the input to the choice axis in this pathway can be effectively viewed as a selection process mediated by the vector $m~_{iv},n_{dv}n_{iv}$ (termed as the second-order selection vector component). Therefore, $n_{tol}$ provides a novel pathway-based definition of selection vector in the network. We further verified the equivalence between this pathway-based definition and the linearized-dynamical-systems-based classical definition (Mante et al., 2013) in our simple circuit through theoretical derivation (see Methods) and numerical comparison (Figure 6B).

![Figure 6.](https://cdn.elifesciences.org/articles/103636/elife-103636-fig6-v1.jpg)

**Figure 6.:** (A) Illustration of how an explicit pathway-based formula of selection vector is derived. In a model with both the first-order selection pathway (i.e. $inp→dv$) and the second-order selection pathway (i.e. $inp→iv→dv$), the second-order pathway can be reduced to a pathway with the effective selection vector $m~_{iv},n_{dv}n_{iv}$ that exhibited the contextual dependency missing in rank-1 models. (B) Comparison between this pathway-based selection vector and the classical one (Mante et al., 2013) using 1000 recurrent neural networks (RNNs) (see Methods for details). (C) The connection between our understanding and the classical understanding in neural state space. Based upon the explicit formula of selection vector in (A), the selection vector modulation has to rely on the contextual modulation of additional representation direction (i.e. $m~_{iv}$) orthogonal to both the input representation direction ($I~_{inp}$) and decision variable representation direction ($m~_{dv}$, line attractor). Therefore, it requires at least three dimensions (i.e. $I~_{inp}$, $m~_{dv}$, and $m~_{iv}$) to account for the selection vector modulation in neural state space.

To visualize the pathway-based selection vector in neural activity state space, we found that a minimum of three dimensions is required, including the input representation direction, the decision variable representation direction, and the intermediate variable representation direction (Figure 6C, left). This geometric visualization highlighted the role of extra dimensions beyond the classical two-dimensional neural activity space spanned by the line attractor and selection vector (Figure 6C, right) in accounting for the selection vector modulation. This is simply because only the second-order selection vector component, which depends on the existence of the intermediate variable, is subject to contextual modulation. In other words, without extra dimensions to support intermediate variable encoding, there will be no selection modulation.

Together, this set of analyses provided a parsimonious pathway-based understanding for both selection vector and its contextual modulation.

### Model prediction verification with vanilla RNN models

The new insights obtained from our new framework enable us to generate testable predictions for better differentiating selection vector modulation from input modulation, a major challenge unresolved in the field (Pagan et al., 2022).

First, we predict that it is more likely to have a large proportion of selection vector modulation for a neural network with high-dimensional connectivity. To better explain the underlying rationale, we can simply compare the number of potential connections contributing to the input modulation with those contributing to the selection vector modulation for a given neural network model. For example, in the network presented in Figure 5, there are three connections (including light blue, dark blue, and green ones) while only one connection (i.e. the green one) supporting selection vector modulation. For a circuit with many higher-order pathways (e.g. Figure 7A), only those connections with the input as the sender is able to support input modulation. In other words, there exist far more connections potentially eligible to support the selection vector modulation (Figure 7B), thereby leading to a large selection vector modulation proportion. We then tested this prediction on vanilla RNNs trained through backpropagation (Figure 7C; Mante et al., 2013; Song et al., 2016; Yang and Wang, 2020). Using effective dimension (see Methods for a formal definition; Rudelson and Vershynin, 2007; Sanyal et al., 2020) to quantify the dimensionality of the connectivity matrix, we found a strong positive correlation between the effective dimension of connectivity matrix and the selection vector modulation (Figure 7D, left panel and Figure 7—figure supplement 1A, see Method for details).

![Figure 7.](https://cdn.elifesciences.org/articles/103636/elife-103636-fig7-v1.jpg)

**Figure 7.:** (A) A general neural circuit model of context-dependent decision-making (CDM). In this model, there are multiple pathways capable of propagating the input information to the decision variable slot, of which the blue connections are susceptible to the input modulation while the green connections are susceptible to the selection vector modulation (see Methods for details). (B) The explicit formula of both the effective connection from the input variable to the decision variable and the effective selection vector for the model in (A). (C) The setting of vanilla RNNs trained to perform the CDM task. See Methods for more details. (D) Positive correlation between effective connectivity dimension and proportion of selection vector modulation. Given a trained RNN with matrix J, the effective connectivity dimension, defined by $\sumi=1n\sigma_{i}^{2}/\sigma_{1}^{2}$ where $\sigma_{1}\geq\sigma_{2}\geq…\geq\sigma_{n}$ are singular values of J, is used to quantify the connectivity dimensionality. Spearman’s rank correlation, r=0.919, p<1e-3, n=3892. The x-axis is displayed in log scale. (E) Single neuron response kernels for two example RNNs. The neuron response kernels were calculated using a regression method (Pagan et al., 2022; see Methods for details). For simplicity, only response kernels for input 1 are displayed. Top: Response kernels for two example neurons in the RNN with low effective dimension (indicated by a star marker in panel D). Two typical response kernels, including the decision variable profile (left) and the sensory input profile (right), are displayed. Bottom: Response kernels for three example neurons in the RNN with high effective dimension (indicated by a square marker in panel D). In addition to the decision variable profile (left) and sensory input profile (middle), there are neurons whose response kernels initially increase and then decrease (right). Gray lines, response kernels in context 1 (i.e. rel. ctx.). Blue lines, response kernels in context 2 (i.e. irrel. Ctx.). (F) Principal dynamical modes for response kernels in the population level extracted by singular value decomposition. Left: Shared dynamical modes, including one persistent choice mode (gray) and three transient modes (blue, orange, green) are identified across both RNNs. Right: For the $i$-th transient mode, the normalized percentage of explained variance (PEV) is given by $\sigma_{i}^{2}/\sum_{j=1}^{39}\sigma_{j}^{2}$, where $\sigma_{1}\geq\sigma_{2}\geq…\geq\sigma_{39}$ are singular values for each transient mode (see Methods for details). (G) Positive correlation between response-kernel-based index and proportion of selection vector modulation. For a given RNN, percentage of explained variance (PEV) of extra dynamical modes is defined as the accumulated normalized PEV of the second and subsequent transient dynamical modes (see Methods for details). Spearman’s rank correlation, r=0.902, p<1e-3, n=3892. The x-axis is displayed in log scale.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/103636/elife-103636-fig7-figsupp1-v1.jpg)

**Figure 7—figure supplement 1.:** (A) The influence of regularization coefficient on effective connectivity dimension of trained RNNs. For each regularization coefficient, we trained 100 full-rank RNNs (Figure 7, panel D). Larger regularization results in connectivity matrices with lower rank, leading to a smaller effective connectivity dimension. (B) The influence of regularization coefficient on selection vector modulation of trained RNNs. Distribution of selection vector modulation for networks trained with different regularization coefficients. Larger regularization leads to networks that favor the input modulation strategy. (C) The relationship between the proportion of explained variance (PEV) in extra dimensions and effective connectivity dimension. There is a strong positive correlation between the PEV in extra dimensions and the effective connectivity dimension in both contexts. In each panel, each dot denotes a trained RNN, with different colors denoting different regularization coefficients.

![Figure 7—figure supplement 2.](https://cdn.elifesciences.org/articles/103636/elife-103636-fig7-figsupp2-v1.jpg)

**Figure 7—figure supplement 2.:** (A) Similar results in trained vanilla RNNs with a softplus activation function. Left: Spearman’s rank correlation, r=0.945, p<1e-3, n=2564. Right: Spearman’s rank correlation, r=0.803, p<1e-3, n=2564. The x-axes are displayed in log scale for both panels. (B) Similar results in trained vanilla RNNs initialized with a variance of $1/N$. Left: Spearman’s rank correlation, r=0.973, p<1e-3, n=2630. Right: Spearman’s rank correlation, r=0.976, p<1e-3, n=2630. The x-axes are displayed in log scale for both panels.

![Figure 7—figure supplement 3.](https://cdn.elifesciences.org/articles/103636/elife-103636-fig7-figsupp3-v1.jpg)

**Figure 7—figure supplement 3.:** (A) Information flow graph for the two RNNs. The black arrows denote that the effective coupling from the head to the tail is 1. For RNN1, the closure of $p_{1}→iv_{2}$ on the pathway $p_{1}→iv_{2}→dv$ prevents $p_{1}$ from reaching $iv_{2}$ and subsequently the decision variable $(dv)$, indicating that RNN1 uses solely input modulation strategy for input 1. For RNN2, the closure of $iv_{1}→dv$ on the pathway $p_{1}→iv_{1}→dv$ means that although $p_{1}$ can reach $iv_{1}$, the subsequent step of $iv_{1}$ reading $dv$ is blocked. This indicates RNN2 uses solely the selection vector modulation strategy for input 1. (B) Connectivity weight among three example neurons in the two RNNs. Each neuron belongs to one of the three neuron populations (see Method for more details). Notice that the connectivity weights from $n_{1}$ (neuron 1) to $n_{3}$ (or $n_{2}$ to $n_{3}$) are different between the two RNNs. (C) Neural activities for the three neurons in three example trials. Orange lines denote activities for RNN1 and blue lines denote activities for RNN2. The neural activity is approximately equal between the two RNNs. (D) Histogram of the single neuron activity similarity between the two RNNs. We calculated the similarity between the activity of the $i$-th neuron in RNN1 and the $i$-th neuron in RNN2 during trial $k$ (r2_score function in the sklearn package of Python). Averaging over the batches provides the similarity between corresponding neurons (neuron $i$ in RNN1 and neuron $i$ in RNN2).

![Figure 7—figure supplement 4.](https://cdn.elifesciences.org/articles/103636/elife-103636-fig7-figsupp4-v1.jpg)

**Figure 7—figure supplement 4.:** (A) Positive correlation between response-kernel-based index and proportion of selection vector modulation in trained vanilla recurrent neural networks (RNNs). (Spearman’s rank correlation, n=75). (B) No significant correlation between these two metrics in RNNs with additional task-irrelevant variance. (Spearman’s rank correlation, n=75). (C) PEV of irrelevant activity showed a significant difference between trained vanilla RNNs and RNNs with additional task-irrelevant variance. (one-way ANOVA test, n=75, ***p<0.001).

We then asked if we could generate predictions to quantify the proportion of selection vector modulation purely based on neural activities. To this end, as what has been performed in Pagan et al., we took advantage of the pulse-based sensory input setting to calculate the single neuron response kernel (see Methods for details). For a given neuron, the associated response kernel is defined to characterize the influence of a pulse input on its firing rate in later times. For example, for a neuron encoding the decision variable, the response kernel should exhibit a profile accumulating evidence over time (Figure 7E, top left). In contrast, for a neuron encoding the sensory input, the response kernel should exhibit an exponential decay profile with time constant $\tau$ (Figure 7E, top right). For each RNN trained through backpropagation, we then examined the associated single neuron response kernels. We found that for the model with low effective dimension (denoted by a star marker in Figure 7D), there were mainly two types of response kernels, including sensory input profile and decision variable profile (Figure 7E, top). In contrast, for the model with the highest effective dimension (denoted by a square marker in Figure 7D), aside from the sensory input and decision variable profiles, richer response kernel profiles were exhibited (Figure 7E, bottom). In particular, there was a set of single neuron response kernels with peak amplitudes occurring between the pulse input onset and the choice onset (Figure 7E, bottom right). These response kernels cannot be explained by the combination of sensory input and decision variables. Instead, the existence of these response kernels signifies neural dynamics in extra dimensions beyond the subspaces spanned by the input and decision variable, the genuine neural dynamical signature of the existence of selection vector modulation (Figure 6C).

While single neuron response kernels are illustrative in highlighting the model difference, they lack explanatory power at the population level. Therefore, we employed the singular value decomposition method to extract the principal dynamical modes of response kernels at the population level (see Methods for details). We found that similar dynamical modes, including one persistent choice mode (gray) and three transient modes (blue, orange, green), were shared across both the low and high effective dimension models (Figure 7F, left). The key difference between these two models lies in the percentage of explained variance (PEV) of the second transient mode (orange): while there is near-zero PEV in the low effective dimension model (Figure 7F, top right), there is substantial PEV in the high effective dimension model (Figure 7F, bottom right), consistent with the single neuron picture shown in Figure 7E. This result led us to use the PEV of extra dynamical modes (including the orange and green ones; see Methods for details) as a simple index to quantify the amount of selection vector modulation in these models. As expected, we found that the PEV of extra dynamical modes can serve as a reliable index reflecting the proportion of selection vector modulation in these models (Figure 7G, right panel and Figure 7—figure supplement 1B and C). Similar results for vanilla RNNs trained with different hyperparameter settings are displayed in Figure 7—figure supplement 2.

Together, we identified novel neural dynamical signatures of section vector modulation at both the single neuron and population level, suggesting the potential great utility of these neural dynamical signatures in distinguishing the contribution of selection vector modulation from input modulation in experimental data.

## Discussion

Using low-rank RNNs, we provided a rigorous theoretical framework linking network connectivity, neural dynamics, and selection mechanisms, and gained an in-depth algebraic and geometric understanding of both input and selection vector modulation mechanisms, and accordingly uncovered a previously unknown link between selection vector modulation and extra dimensions in neural state space. This gained understanding enabled us to generate novel predictions linking novel neural dynamic modes with the proportion of selection vector modulation, paving the way towards addressing the intricacy of neural variability across subjects in context-dependent computation.

### A pathway-based definition of selection vector modulation

In their seminal work, Mante, Sussillo, and their collaborators developed a numerical approach to compute the selection vector for trained RNN models (Mante et al., 2013). Based on this concept of selection vector, recently, Pagan et al. proposed a new theoretical framework to decompose the solution space of context-dependent decision-making, in which input modulation and selection vector modulation were explicitly defined (i.e. Equation 1). Here, taking the theoretical advantage of low-rank RNNs (Mastrogiuseppe and Ostojic, 2018; Dubreuil et al., 2022), we went beyond numerical reverse-engineering and provided a complementary pathway-based definition of both selection vector and selection vector modulation (i.e. Equation 5). This new definition gained us a novel geometric understanding of selection vector modulation, revealed a previously unknown link between extra dimensions and selection vector modulation (Figure 6C), and eventually provided us with experimentally identifiable neural dynamical signature of selection vector modulation at both the single neuron and population levels (Figure 7, E-G).

### Individual neural variability in higher cognition

One hallmark of higher cognition is individual variability, as the same higher cognition problem can be solved equally well with different strategies. Therefore, studying the neural computations underlying individual variability is no doubt of great importance (Hariri, 2009; Parasuraman and Jiang, 2012; Keung et al., 2020; Nelli et al., 2023). Recent experimental advances enabled researchers to investigate this important issue in a systematic manner using delicate behavioral paradigms and large-scale recordings (Pagan et al., 2022). However, the computation underlying higher cognition is largely internal, requiring discovering novel neural activity patterns as internal indicators to differentiate distinct circuit mechanisms. In the example of context-dependent decision-making studied here, to differentiate selection vector modulation from input modulation, we found the PEV in extra dynamical modes is a reliable index for a wide variety of RNNs (Figure 7D, Figure 7—figure supplement 2). However, cautions have to be made here as we can conveniently construct counter-examples deviating from the picture depicted by this index. For instance, manually introducing additional dimensions that do not directly contribute to the computation can disrupt the index (Figure 7—figure supplement 4A and B). In the extreme scenario, we can construct two models with distinct circuit mechanisms (selection vector modulation and input modulation, respectively) but having the same neural activities (Figure 7—figure supplement 3), suggesting that any activity-based index alone would fail to make this differentiation. Then, why did the proposed index work for the trained vanilla RNNs shown in Figure 7D? Our lesion analysis suggests that the underlying reason is that the major variance in neural activity of vanilla RNNs learned through backpropagation is task-relevant (Figure 7—figure supplement 4C, see Methods for details). However, it is highly likely that task-irrelevant neural activity variance exists in higher brain regions, meaning the proposed index may not perform well in neural recordings. Therefore, our modeling work suggests that, to address the intricacy of individual variability of neural computations underlying higher cognition, integrative efforts incorporating not only large-scale neural activity recordings but also activity perturbations, neuronal connectivity knowledge, and computational modeling may be inevitably required.

### Beyond context-dependent decision-making

While we mainly focused on context-dependent decision-making tasks in this study, the issue of whether input or selection vector modulation prevails is not limited to the domain of decision-making. For instance, recent work by Chen et al., 2024 demonstrated that during sequence working memory control (Botvinick and Watanabe, 2007; Xie et al., 2022), sensory inputs presented at different ordinal ranks first entered into a common sensory subspace and then were routed to the corresponding rank-specific working memory subspaces in monkey frontal cortex. Here, similar to the decision-making case (Figure 1C), the same issue arises: where is the input information selected by the context (here, the ordinal rank)? Can the presence of a common sensory subspace (similar to the presence of location information in both relevant and irrelevant contexts in Figure 1C) preclude the input modulation? The pathway-based understanding of input and selection vector modulation gained from CDM in this study may be transferable to address these similar issues.

### The role of transient dynamics in extra dimensions in context-dependent computation

In this study, we linked the selection vector modulation with transient dynamics (Aoi et al., 2020; Soldado-Magraner et al., 2023) in extra dimensions. While the transient dynamics in extra dimensions are not necessary in context-dependent decision-making here (Dubreuil et al., 2022; Figure 2), more complex context-dependent computation may require its presence. For example, recent work by Tian et al., 2024 found that transient dynamics in extra subspaces is required to perform the switch operation (i.e. exchanging information in subspace 1 with information in subspace 2). Understanding how transient dynamics in extra dimensions contribute to complex context-dependent computation warrants further systematic investigation.

In summary, through low-rank neural network modeling, our work provided a parsimonious mechanistic account for how information can be selected along different pathways, making significant contributions towards understanding the intriguing selection mechanisms in context-dependent computation.

## Materials and methods

**Key resources table**


<table>
  <thead>
    <tr>
      <th>Reagent type (species) or resource</th>
      <th>Designation</th>
      <th>Source or reference</th>
      <th>Identifiers</th>
      <th>Additional information</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Software, algorithm</td>
      <td>Python</td>
      <td>https://www.python.org/</td>
      <td>RRID:SCR_008394</td>
      <td>version: 3.9</td>
    </tr>
  </tbody>
</table>

### The general form of RNNs

We investigated networks of $N$ neurons with $S$ input channels, described by the following temporal evolution equation

$$
\tau\frac{dx_{i}(t)}{dt}=−x_{i}(t)+\sumj=1NJ_{ij}ϕ(x_{j}(t))+\sums=1SI_{si}u_{s}(t)+ϵ_{i}(t).
$$

In this equation, $x_{i}t$ represents the activation of neuron $i$ at time $t$, $\tau$ denotes the characteristic time constant of a single neuron, and $ϕ$ is a nonlinear activation function. Unless otherwise specified, we use the tanh function as the activation function. The coefficient $J_{ij}$ represents the connectivity weight from neuron $j$ to neuron $i$. The input $u_{s}(t)$ corresponds to the $s$-th input channel at time $t$, with feedforward weight $I_{si}$ to neuron $i$, and $ϵ_{i}(t)$ represents white noise at time $t$. The network’s output is obtained from the neuron’s activity $ϕ(x)$ through a linear projection:

$$
z(t)=\frac{1}{N}\sumi=1Nw_{i}ϕ(x_{i}).
$$

The connectivity matrix $J$, specified as $J=J_{ij},i=1,…,N,j=1,…,N$, can be a low-rank or a full-rank matrix. In the low-rank case, $J$ is restricted to a low-rank matrix $\frac{1}{N}\sum_{r=1}^{R}m_{r}n_{r}^{T}$, in which $m_{r}$ is the $r$-th output vector, and $n_{r}$ is the $r$-th input-selection vector, with each element of $m_{r}$ and $n_{r}$ considered an independent parameter (Dubreuil et al., 2022). In this paper, we set the time constant $\tau$ to be 100 ms, and use Euler’s method to discretize the evolution equation with a time step $Δt=20ms$.

### Task setting

We modeled the click-version CDM task recently investigated by Pagan et al., 2022. The task involves four input channels $u_{1}t$, $u_{2}t$, $u_{1}^{ctx}t$, and $u_{2}^{ctx}t$, where $u_{1}t$ and $u_{2}t$ are stimulus inputs and $u_{1}^{ctx}t$ and $u_{2}^{ctx}t$ are context inputs. Initially, there is a fixation period lasting for $T_{fix}=200ms$. This is followed by a stimulus period of $T_{sti}=800ms$ and then a decision period of $T_{decision}=20ms$.

For trial $k$, at each time step, the total number of pulse inputs (#pulse) is sampled from a Poisson distribution with a mean value of $40Δt=0.8$. Each pulse has two properties: location and frequency. Location can be either left or right, and frequency can be either high or low. We randomly sample a pulse to be right with probability $p^{k}$ (hence left with probability $1−p^{k}$) and to be high with probability $p_{high}^{k}$ (hence low with probability $1−p_{high}^{k}$). The values of $p^{k}$ and $p_{high}^{k}$ are independently chosen from the set {39/40, 35/40, 25/40, 15/40, 5/40, 1/40}. The stimulus strength for the location input at trial $k$ is defined as $2\timesp^{k}−1$, and for the frequency input, it is defined as $2\timesp_{high}^{k}−1$. The input $u_{1}(t)$ represents location evidence, calculated as 0.1 times the difference between the number of right pulses and the number of left pulses (#right-#left) at time step $t$. The input $u_{2}(t)$ represents frequency evidence, calculated as 0.1 times the difference between the number of high-frequency pulses and the number of low-frequency pulses (#high-#low) at time step $t$.

The context is randomly chosen to be either the location context or the frequency context. In the location context, $u_{1}^{ctx}=1$ and $u_{2}^{ctx}=0$ throughout the entire period. The target output $z_{k}$ is defined as the sign of the location stimulus strength (1 if $p^{k}>0.5$, otherwise –1). Thus, in this context, the target output $z_{k}$ is independent of the frequency stimulus input. Conversely, in the frequency context, $u_{1}^{ctx}=0$ and $u_{2}^{ctx}=1$. The target output $z_{k}$ is defined as the sign of the frequency stimulus strength (1 if $p_{high}^{k}>0.5$, otherwise –1). Thus, in this context, the target output is independent of the location stimulus input.

### Linearized dynamical system analysis (Figure 1 and Figure 7)

To uncover the computational mechanism enabling each RNN to perform context-dependent evidence accumulation, we utilize linearized dynamical system analysis to ‘open the black box’ (Mante et al., 2013). The dynamical evolution of an RNN in context $c$ is given by:

$$
\tau\frac{dx}{dt}=−x+Jr+I_{1}u_{1}+I_{2}u_{2}+I_{c}^{ctx},
$$

where $r=ϕ(x)$ is the neuron activity. First, we identify the slow point of each RNN in each context using an optimization method (Mante et al., 2013). Let $x$ be the discovered slow point, i.e., $x≈Jr^{∗}+I_{c}^{ctx}$ where $r=ϕ(x^{∗})$. We define a diagonal matrix $G=diag(ϕ^{′}(x^{∗}))$, with the $i$-th diagonal element representing the sensitivity of the $i$-th neuron at the slow point. Near the slow point, we have $Δr=r−r^{∗}≈Gϕ^{′}(Δx)$. Then, we can derive:

$$
\tau\frac{dΔr}{dt}≈\tauG\frac{dΔx}{dt}=−Δr+GJΔr+GI_{1}u_{1}+GI_{2}u_{2}.
$$

Thus, the dynamics of neuron activity around the slow point can be approximated by a linear dynamical system:

$$
\tau\frac{dΔr}{dt}=MΔr+I∼_{1}u_{1}+I∼_{2}u_{2},
$$



$$
M=−E+GJ,
$$

where $E$ is the identity matrix, $M$ denotes the state transition matrix of the dynamical system, and $I~_{r}=GI_{r},r=1,2$ are stimulus input representation directions. Similar to previous work (Mante et al., 2013), we find that for every network, the linear dynamical system near the slow point in each context is roughly a linear attractor. Specifically, the transition matrix $M$ has a single eigenvalue close to zero, while all other eigenvalues have negative real parts. The right eigenvector of $M$ associated with the eigenvalue close to zero defines the stable direction of the dynamical system, forming the line attractor $ρ$(unit norm). The left eigenvector of $M$ associated with that eigenvalue defines the direction of the selection vector $s$. The norm of selection vector $s$ is chosen such that $s⋅ρ=1$. Previous work (Mante et al., 2013) has shown that a perturbation $Δr_{0}$ from the line attractor will eventually converge to the line attractor, with the distance from the starting point being $s⋅Δr_{0}$.

Based on linearized dynamical systems analysis, Pagan et al. recently defined input modulation and selection vector modulation (Pagan et al., 2022) as:

$$
mod_{inp}=ΔGI⋅s¯,
$$



$$
mod_{sel}=GI¯⋅Δs.
$$

Specifically, the input modulation and selection vector modulation for stimulus input 1 are defined as $(s^{ctx_{1}}+s^{ctx_{2}})/2⋅(I∼_{1}^{ctx_{1}}−I∼_{1}^{ctx_{2}})$ and $(s^{ctx_{1}}−s^{ctx_{2}})⋅(I~_{1}^{ctx_{1}}+I~_{1}^{ctx_{2}})/2$, respectively. Similarly, the input modulation and selection vector modulation for stimulus input 2 are defined as $(s^{ctx_{1}}+s^{ctx_{2}})/2⋅(I∼_{2}^{ctx_{2}}−I∼_{2}^{ctx_{1}})$ and $(s^{ctx_{2}}−s^{ctx_{1}})⋅(I~_{2}^{ctx_{1}}+I~_{2}^{ctx_{2}})/2$, respectively. Proportion for selection vector modulation (Figure 7D and G) is defined as $\frac{mod_{sel}}{mod_{inp}+mod_{sel}}$.

### Training of rank-1 RNNs using backpropagation (Figure 2)

The rank-1 RNNs in Figure 2 are trained using backpropagation-through-time with the PyTorch framework. These networks are trained to minimize a loss function defined as:

$$
L=\sumk,tM_{t}(Z^_{k,t}−Z_{k})+L_{reg}.
$$

Here, $z_{k}$ is the target output, $z^_{k,t}$ is the network output, and the indices $t$ and $k$ represent time and trial, respectively. $M_{t}$ is a temporal mask with value {0, 1}, where $M_{t}$ is 1 only during the decision period. $L_{reg}$ is the L2 regularization loss. For full-rank RNNs (Figure 7), $L_{reg}=w_{reg}\sum_{ij}J_{ij}^{2}$ and for low-rank RNNs, $L_{reg}=w_{reg}\sum_{r}(m_{r}_{2}^{2}+n_{r}_{2}^{2})$. The loss function is minimized by computing gradients with respect to all trainable parameters. We use the Adam optimizer in PyTorch with the decay rates for the first and second moments set to 0.9 and 0.99, respectively, and a learning rate of $10^{−3}$. Each RNN is trained for 5000 steps with a batch size of 256 trials.

For Figure 2, we trained 100 RNNs of $N=512$ neurons with the same training hyperparameters. The rank of the connectivity matrix is constrained to be rank-1, represented as $J=\frac{1}{N}m_{dv}n_{dv}^{T}$. We trained the elements of the input vectors $I_{1},I_{2},I_{1}^{ctx},I_{2}^{ctx}$, connectivity vector $m_{dv},n_{dv}$, and the readout vector $w$. All trainable parameters were initialized with random independent Gaussian weights with a mean of 0 and a variance of $1/N^{2}$. The regularization coefficient $w_{reg}$ is set to $10^{−4}$.

### Trial-averaged analyses (Figures 2F and 3F)

For the trial-averaged analyses shown in Figures 2f and 3f, we followed a procedure similar to Mante et al., 2013. Specifically, at each time point $t$ and for each neuron $i$, we fit the following linear regression model to characterize how different task variables contribute to that neuron’s activity:

$$
r_{i,t}(k)=\beta_{choice;i,t}choice(k)+\beta_{inp_{1};i,t}u_{1,k}+\beta_{inp_{2};i,t}u_{2,k}+\beta_{context;i,t}context(k)+\beta_{0;i,t}
$$

Here, $choicek$, $u_{1,k}$, $u_{2,k}$, and $contextk$ represent the values of the corresponding variables on trial k. Next, for each regressor (choice, input 1, input 2, context), we pooled the resulting regression coefficients across neurons to get the time-vary regression vectors $\beta_{choice;t},\beta_{inp_{1};t},\beta_{inp_{2};t,}\beta_{context;t}$. For regressor $v$, we identified the time $t_{v}^{max}$ when the regression vector $\beta_{v;t}$ has maximum norm, and got the time-independent regression vectors:

$$
t_{v}^{max}=argmax_{t}‖\beta_{v;t}‖_{2},
$$



$$
\beta_{v}=\beta_{v;t_{v}^{max}}
$$

Next, we assembled these vectors into a matrix $B=[\beta_{choice}\beta_{inp_{1}}\beta_{inp_{2}}\beta_{context}]$ and used QR decomposition to get the orthogonalized regression basis $[\beta_{choice}^{⊥},\beta_{inp_{1}}^{⊥},\beta_{inp_{2}}^{⊥},\beta_{context}^{⊥}]$. Finally, we averaged neuronal activity across trials sharing the same condition (choice, context, input 1), and then projected this average activity onto the choice and input 1 axes. This process resulted in the trial-averaged population dynamics illustrated in Figures 2F and 3F.

### Proof of no selection vector modulation in rank-1 RNNs (Figure 2)

The transition matrix of neuron activity in the rank-1 RNN is given by:

$$
M=−E+\frac{1}{N}Gm_{dv}n_{dv}.
$$

Multiplying $M^{T}$ on the right by $n_{dv}$, we obtain

$$
M^{T}n_{dv}=−n_{dv}+⟨m∼_{dv},n_{dv}⟩n_{dv}≈0,
$$

where the $⋅,⋅$ symbol is defined as $⟨a,b⟩=\frac{1}{N}\sumi=1Na_{i}b_{i}$ for two vectors of length-$N$. The requirement for the linear attractor approximation, $⟨m∼_{dv},n_{dv}⟩≈1$, is met by all our trained and handcrafted RNNs (Figure 4—figure supplement 1). This demonstrates that $n_{dv}$ is the left eigenvector of the transition matrix, and hence $\frac{1}{N}m~_{dv}_{2}n_{dv}$ is the selection vector in each context. Therefore, the direction of the selection vector is invariant across different contexts for the rank-1 model, indicating no selection vector modulation and this is consistent with the training results shown in Figure 2.

### Handcrafting rank-3 RNNs with pure selection vector modulation (Figure 3)

First, we provide the implementation details of the rank-3 RNNs used in Figure 3. The network consists of 30,000 neurons divided into three populations, each with 10,000 neurons. The first population (neurons 1–10,000) receives stimulus input, accounting for both the information flow from the stimulus input to the intermediate variables and the recurrent connection of the decision variable. The second (neurons 10,001–20,000) and third populations (neurons 20,001–30,000) handle the information flow from the intermediate variables to the decision variable and are modulated by the context signal. To achieve this, we generate three Gaussian random matrices $(M^{(1)},M^{(2)},M^{(3)})$ of shape 10,000×3. Let $M_{:,r}^{p}$ denote the $r$-th column of matrix $M^{p}$. The stimulus input $I_{1}$ is given by the concatenation of three length-10,000 vectors $M_{:,1}^{1};0;0$, 0 where  denotes a length-10,000 zero vector. The stimulus input $I_{2}$ is given by $M_{:,2}^{1};0;0$. The context input $I_{1}^{ctx}$ is given by $0;M_{:,1}^{2};0$. The context input $I_{2}^{ctx}$ is given by $0;0;M_{:,1}^{3}$. The connectivity vectors $m_{iv1},m_{iv2}$ and $m_{dv}$ are given by $0;M_{:,2}^{2};M_{:,2}^{3}$, $0;M_{:,3}^{2};M_{:,3}^{3}$ and $M_{:,3}^{1};0;0$, respectively. The input-selection vectors $n_{iv1},n_{iv2},$ and $n_{dv}$ are given by $10M_{:,1}^{1};0;0$, $10M_{:,2}^{1};0;0$, and $3M_{:,3}^{1};−gM_{:,2}^{2}+M_{:,3}^{2};M_{:,2}^{3}−gM_{:,3}^{3}$, respectively, where $g=\int_{−∞}^{+∞}\frac{1}{\sqrt{2\pi}}e^{−x^{2}/2}ϕ^{`}xdx$ represents the average gain of the second population in context 1 or the third population in context 2. The readout vector $w$ is given by $4M_{:,3}^{1};0;0$. We generate 100 RNNs based on this method to ensure that the conclusions in Figure 3 do not depend on the specific realization of random matrices. Linearized dynamical system analysis reveals that all these RNNs perform flexible computation through pure selection vector modulation. Please see the section ‘The construction of rank-3 RNN models’ for a mean-field-theory-based understanding.

### Pathway-based information flow graph analysis of low-rank RNNs (Figure 4)

The dynamical evolution equation for low-rank RNN with $R$ ranks and $S$ input channels in context c is given by

$$
\frac{dx}{dt}=−x+\frac{1}{N}\sumr=1Rm_{r}n_{r}^{T}ϕ(x)+\sums=1SI_{s}u_{s}+I_{c}^{ctx}
$$

Assuming $x(0)=I_{c}^{ctx}$ at $t=0$, the dynamics of $xt−x(0)$ are always constrained in the subspace spanned by $m_{r},r=1,…,R$ and {$I_{s},s=1,…,S}$. Therefore, $xt$ can be expressed as a linear combination of these vectors: $xt=I_{c}^{ctx}+\sum_{r=1}^{R}k_{r}tm_{r}+\sum_{s=1}^{S}k_{p_{s}}tI_{s},$ leading to the following evolving dynamics of task variables:

$$
\tau\frac{dk_{p_{s}}(t)}{dt}=−k_{p_{s}}(t)+u_{s}(t),
$$



$$
\tau\frac{dk_{r}(t)}{dt}=−k_{r}(t)+\frac{1}{N}n_{r}^{T}ϕ(I_{c}^{ctx}+\sumj=1Rk_{j}(t)m_{j}+\sums=1Sk_{p_{s}}(t)I_{s}),
$$

where $k_{p_{s}}t$ denotes activation along the $s$-th input vector, termed the input task variable and $k_{r}t$ denotes activation along the $j$-th output vector, termed the internal task variable.

### The rank-1 RNN case

Therefore, for rank-1 RNNs, the latent dynamics of decision variable (internal task variable associated with $m_{dv}$) in context $c$ is given by

$$
\tau\frac{dk_{dv}(t)}{dt}=−k_{dv}(t)+\frac{1}{N}n_{dv}^{T}ϕ(I_{c}^{ctx}+k_{dv}(t)m_{dv}+\sums=12k_{p_{s}}(t)I_{s}).
$$

Similar to the linearized dynamical systems analysis introduced earlier, we linearized Equation 15 around $I_{c}^{ctx}$, obtaining the following linearized equation:

$$
\tau\frac{dk_{dv}(t)}{dt}=−k_{dv}(t)+\frac{1}{N}(n_{dv}^{T}ϕ(I_{c}^{ctx})+n_{dv}^{T}m∼_{dv}^{ctx_{c}}k_{dv}(t)+\sums=12n_{dv}^{T}I∼_{s}^{ctx_{c}}k_{p_{s}}(t)),
$$

where $m~_{dv}^{ctx_{c}}=G_{c}m_{dv}$ (termed as the decision variable representation direction) and $I~_{s}^{ctx_{c}}=G_{c}I_{s}$ (termed as the input representation direction), with $G_{c}$ equal to $diagϕ^{`}I_{c}^{ctx}$. By denoting $\frac{1}{N}n_{dv}^{T}m~_{dv}^{ctx_{c}}$ and $\frac{1}{N}n_{dv}^{T}I~_{s}^{ctx_{c}}$ as $E_{dv→dv}^{ctx_{c}}$ and $E_{p_{s}→dv}^{ctx_{c}}$, respectively, together with the fact that $\frac{1}{N}n_{dv}^{T}ϕ(I_{c})$ is close to zero for all trained rank-1 RNNs, we obtain

$$
\tau\frac{dk_{dv}(t)}{dt}=−k_{dv}(t)+E_{dv→dv}κ_{dv}(t)+E_{p_{1}→dv}^{ctx_{c}}k_{p_{1}}(t)+E_{p_{2}→dv}^{ctx_{c}}k_{p_{2}}(t),
$$

which is Equation 3 in the main text.

### The rank-3 RNN case

Using a similar method, we can uncover the latent dynamics of rank-3 RNNs, as shown in Figure 5. Note that the rank-3 RNN in Figure 3 is a special case of this more general form. The latent dynamics for internal task variables in context $c$ can be written as:

$$
\tau\frac{dk_{iv_{s}}}{dt}=−k_{iv_{s}}(t)+\frac{1}{N}n_{iv_{s}}^{T}ϕ(I_{c}^{ctx}+k_{dv}m_{dv}+\sums=12k_{iv_{s}}m_{iv_{s}}+\sums=12k_{inp_{s}}I_{s}),
$$



$$
\tau\frac{dk_{dv}}{dt}=−k_{dv}(t)+\frac{1}{N}n_{dv}^{T}ϕ(I_{c}^{ctx}+k_{dv}m_{dv}+\sums=12k_{iv_{s}}m_{iv_{s}}+\sums=12k_{inp_{s}}I_{s}).
$$

By applying the same first-order Taylor expansion, we obtain the following equations:

$$
\tau\frac{dk_{iv_{s}}}{dt}=−k_{iv_{s}}+\frac{1}{N}n_{iv_{s}}^{T}(m∼_{dv}^{ctx_{c}}k_{dv}+\sums=12m∼_{iv_{s}}^{ctx_{c}}k_{iv_{s}}+\sums^{′}=12I∼_{s^{′}}^{ctx_{c}}k_{inp_{s^{′}}}),
$$



$$
\tau\frac{dk_{dv}}{dt}=−k_{dv}+\frac{1}{N}n_{dv}^{T}(m∼_{dv}^{ctx_{c}}k_{dv}+\sums=12m∼_{iv_{s}}^{ctx_{c}}k_{iv_{s}}+\sums=12I∼_{s}^{ctx_{c}}k_{inp_{s}}).
$$

We consider the case in which the intermediate variables ($k_{iv_{s}},s=1,2$, internal task variables associated with $m_{iv_{s}},s=1,2$, respectively) only receive information from the corresponding stimulus input, and the effective coupling of the recurrent connection is 1 in both contexts. Specifically, we assume:

$$
⟨I∼_{iv_{s^{′}}}^{ctx_{c}},n_{iv_{s}}⟩=0,s\neqs^{′},c=1,2,
$$



$$
⟨m∼_{iv_{s^{′}}}^{ctx_{c}},n_{iv_{s}}⟩=0,s,s^{′}\in{1,2},c=1,2,
$$



$$
⟨m∼_{dv}^{ctx_{c}},n_{dv}⟩=1,c=1,2.
$$

Our construction methods for rank-3 RNNs in Figures 3 and 5 guarantee these conditions when the network is large enough (for example, $N=30,000$ in our setting). Under these conditions, Equations 20 and 21 can be simplified to:

$$
\tau\frac{dk_{iv_{s}}}{dt}=−k_{iv_{s}}+E_{inp_{s}→iv_{s}}^{ctx_{c}}k_{inp_{s}},
$$



$$
\tau\frac{dk_{dv}}{dt}=E_{inp_{1}→dv}^{ctx_{c}}k_{inp_{1}}+E_{inp_{2}→dv}^{ctx_{c}}k_{inp_{2}}+E_{iv_{1}→dv}^{ctx_{c}}k_{iv_{1}}+E_{iv_{2}→dv}^{ctx_{c}}k_{iv_{2}}.
$$

Suppose at $t=0,$ the network receives a pulse from input 1 with size $A_{1}$ and a pulse from input 2 with size $A_{2}$, which correspond to $u_{1}t=A_{1}\tau\delta(t)$, $u_{2}t=A_{2}\tau\delta(t)$. Under this condition, the expression for $k_{dv}$ is given by

$$
k_{dv}(t)=\sums=12A_{s}(E_{inp_{s}→dv}^{ctx_{c}}(1−e^{−t/\tau})+E_{inp_{s}→iv_{s}}^{ctx_{c}}E_{iv_{s}→dv}^{ctx_{c}}(1−e^{−t/\tau}−\frac{t}{\tau}e^{−t/\tau})).
$$

From Equation 27, as $t→∞$, $k_{dv}$ will converge to $\sums=12A_{s}(E_{inp_{s}→dv}^{ctx_{c}}+E_{inp_{s}→iv_{s}}^{ctx_{c}}E_{iv_{s}→dv}^{ctx_{c}})$, providing a theoretical basis for the pathway-based information flow formula presented in Figures 4 and 5.

### Building rank-3 RNNs with both input and selection vector modulations (Figure 5)

#### Understanding low-rank RNNs in the mean-field limit

The dynamics of task variables in low-rank RNNs can be mathematically analyzed under the mean-field limit ($N→+∞$) when each neuron’s connectivity component is randomly drawn from a multivariate Gaussian mixture model (GMM) (Beiran et al., 2021; Dubreuil et al., 2022). Specifically, we assume that, for the $i$-th neuron, the connectivity component vector ${I_{s}^{i},s=1,…,S,I_{c}^{ctx}^{(i)},c=1,2,m_{r}^{(i)},r=1,…,R,n_{r}^{(i)},r=1,…,R}$ is drawn independently from a GMM with $P$ components. The weight for the $j$-th component is $\alpha_{j}$, and this component is modeled as a Gaussian distribution with mean zero and covariance matrix $Σ^{(j)}$. Let $Σ_{ℑ}^{(j)}$ denote the upper-left $S+R+2\timesS+R+2$ submatrix of $Σ^{(j)}$, which represents the covariance matrix of ${I_{s}^{i},s=1,…,S,I_{c}^{ctx}^{(i)},c=1,2,m_{r}^{i},r=1,…,R}$ within the $j$-th component. Let $\sigma_{ab}^{(p)},a,b\inI_{s},s=1,…,S,I_{c}^{ctx},c=1,2,m_{r},r=1,…,R,n_{r},r=1,…,R$ denote the covariance of $a^{(i)}$ and $b^{(i)}$, where the $i$-th neuron belongs to the $p$-th component.

Given these assumptions, under the mean-field limit ($N→+∞$), Equation 14 can be expressed as

$$
\tau\frac{dk_{r}(t)}{dt}∧−k_{r}(t)+\sumj=1R\sump=1P\alpha_{p}⟨ϕ^{′}⟩_{p}\sigma_{m_{j}n_{r}}^{(p)}k_{j}(t)+\sums=1S\sump=1P\alpha_{p}⟨ϕ^{′}⟩_{p}\sigma_{I_{s}n_{r}}^{(p)}k_{inp_{s}}+\sump=1P\alpha_{p}⟨ϕ^{′}⟩_{p}\sigma_{I_{c}^{ctx}n_{r}}^{(p)},
$$



$$
⟨ϕ^{′}⟩_{p}=\int_{−∞}^{∞}\frac{1}{\sqrt{2\pi}}e^{\frac{−x^{2}}{2}}ϕ^{′}(Δ_{p}x)dx,
$$



$$
Δ_{p}^{2}=[k_{inp_{1}},…,k_{inp_{S}},k_{ctx_{1}},k_{ctx_{2}},k_{1},…,k_{R}]Σ_{ℑ}^{(p)}[k_{inp_{1}},…,k_{inp_{S}},k_{ctx_{1}},k_{ctx_{2}},k_{1},…,k_{R}]^{T},
$$

where $k_{ctx_{i}}=1$ if $i=c$, otherwise $k_{ctx_{i}}=0.$ Under the condition of small task variables ($k_{p_{s}},s=1,…,S$ and $k_{r},r=1,…,R$), $Δ_{p}^{2}$ is approximately equal to $\sigma_{I_{c}^{ctx},I_{c}^{ctx}}^{(p)}$ and the quantities $ϕ^{`}_{p},p=1,…,P$ are determined solely by the covariance of the context $c$ signal input within each population. Clearly, the effective coupling from the input task variable $k_{p_{s}}$ to the internal task variable $k_{r}$ is given by $\sum_{p=1}^{P}\alpha_{p}ϕ^{`}_{p}\sigma_{I_{s}n_{r}}^{p}$, and the effective coupling between the internal task variables $k_{j}$ and $k_{r}$ is given by $\sum_{p=1}^{P}\alpha_{p}ϕ^{`}_{p}\sigma_{m_{j}n_{r}}^{p}$.

### Mean-field-theory-based model construction

Utilizing this theory, we can construct RNNs tailored to any given ratio of input modulation to selection vector modulation by properly setting the connectivity vectors $(I_{1},I_{2},I_{1}^{ctx},I_{2}^{ctx},m_{iv1},m_{iv2},m_{dv},n_{iv1},n_{iv2},andn_{dv})$. The RNN we built consists of 30,000 neurons divided into three populations. The first population (neurons 1–10,000) receives the stimulus input, accounting for information flow from stimulus input to intermediate variables (the connection strength is controlled by $\beta$) and the recurrent connection of the decision variable. The second (neurons 10,001–20,000) and third populations (neurons 20,001–30,000) receive the stimulus input, accounting for the information flow from the stimulus input to the decision variable (the connection strength is controlled by $\alpha$), and the information flow from the intermediate variables to the decision variable (the connection strength is controlled by $η$), and are modulated by contextual input. To achieve this, we generate three Gaussian random matrices $(M^{(1)},M^{(2)},M^{(3)})$ of shape 10,000 × 3, 10,000 × 5  and 10,000 × 5, respectively. Let $M_{:,r}^{p}$ denote the $r$-th column of matrix $M^{p}$. The stimulus input $I_{1}$ is given by the concatenation of three length-10,000 vectors $M_{:,1}^{1};M_{:,1}^{2};M_{:,1}^{3}$. The stimulus input $I_{2}$ is given by $M_{:,2}^{1};M_{:,2}^{2};M_{:,2}^{3}$. The context input $I_{1}^{ctx}$ is given by $[0;M_{:,3}^{(2)};0]$. The context input $I_{2}^{ctx}$ is given by $[0;0;M_{:,3}^{(3)}]$. The connectivity vectors $m_{iv1},m_{iv2},$ and $m_{dv}$ are given by $[0;M_{:,4}^{(2)};M_{:,4}^{(3)}]$, $[0;M_{:,5}^{(2)};M_{:,5}^{(3)}]$ and $[M_{:,3}^{(1)};0;0]$, respectively. The input-selection vectors $n_{iv_{1}}$ and $n_{iv_{2}}$ are given by $[3\betaM_{:,1}^{(1)};0;0]$, $[3\betaM_{:,2}^{(1)};0;0]$, respectively. $n_{dv}$ is given by $[3M_{:,3}^{(1)};−\frac{3\alphag}{1−g^{2}}M_{:,1}^{(2)}$ $+\frac{3\alpha}{1−g^{2}}M_{:,2}^{(2)}$ $−\frac{3ηg}{1−g^{2}}M_{:,4}^{(2)}$ $+\frac{3η}{1−g^{2}}M_{:,5}^{(2)};\frac{3\alpha}{1−g^{2}}M_{:,1}^{(3)}$ $−\frac{3\alphag}{1−g^{2}}M_{:,2}^{(3)}$ $+\frac{3η}{1−g^{2}}M_{:,4}^{(3)}$ $−\frac{3ηg}{1−g^{2}}M_{:,5}^{(3)}]$, where $g=\int_{−∞}^{+∞}\frac{1}{\sqrt{2\pi}}e^{−x^{2}/2}ϕ^{`}xdx$ is the average gain of the second population in context 1 or third population in context 2. The readout vector $w$ is given by $[4M_{:,3}^{(1)};0;0]$.

For the network, in context 1, $ϕ^{`}_{p}$ is only determined by the covariance of the context 1 signal. That is,

$$
⟨ϕ^{′}⟩_{p}=\int_{−∞}^{∞}\frac{1}{\sqrt{2\pi}}e^{\frac{−x^{2}}{2}}ϕ^{′}(\sqrt{\sigma_{I_{1}^{ctx}I_{1}^{ctx}}^{(p)}}x)dx.
$$

Our construction method guarantees that $\sigma_{I_{1}^{ctx}I_{1}^{ctx}}^{(p)}=0,1,0$ for $p=1,2,3$, respectively. Hence, $ϕ^{`}_{p}=1,g,1$ for $p=1,2,3$, respectively. Then the effective coupling from input variable $k_{p_{1}}$ to $k_{iv_{1}}$ in context 1 is given by

$$
E_{inp_{1}→iv_{1}}^{ctx_{1}}=\sump=1P\frac{1}{3}⟨ϕ^{′}⟩_{p}\sigma_{I_{1}n_{iv_{1}}}^{(p)}=\frac{1}{3}\times3\times\beta=\beta.
$$

Similarly, we can get that:

$$
E_{inp_{2}→iv_{2}}^{ctx_{1}}=\beta,
$$



$$
E_{inp_{1}→dv}^{ctx_{1}}=\alpha,E_{inp_{2}→dv}^{ctx_{1}}=0,
$$



$$
E_{iv_{1}→dv}^{ctx_{1}}=η,E_{iv_{2}→dv}^{ctx_{1}}=0.
$$

Other unmentioned effective couplings are zero. Similarly, the effective couplings in context 2 are given by

$$
E_{inp_{1}→iv_{2}}^{ctx_{2}}=E_{inp_{2}→iv_{2}}^{ctx_{2}}=\beta,
$$



$$
E_{inp_{1}→dv}^{ctx_{2}}=0,E_{inp_{2}→dv}^{ctx_{2}}=\alpha,
$$



$$
E_{iv_{1}→dv}^{ctx_{2}}=0,E_{iv_{2}→dv}^{ctx_{2}}=η.
$$

Thus, for each input, the input modulation is $\alpha$ and the selection vector modulation is $\beta\timesη$. Therefore, any given ratio of input modulation to selection vector modulation can be achieved by varying the parameters $\alpha,\beta,$ and $η$. The example in Figure 3 with pure selection vector modulation is a special case with $\alpha=0,\beta=\frac{10}{3},$ and $η=(1−g^{2})/3$.

### Pathway-based definition of selection vector (Figure 6)

Next, we will consider the rank-3 RNN with latent dynamics depicted in Equations 18 and 19. The input representation produced by a pulse input $u_{s}=\tauA_{s}\deltat,s=1,2$ in a certain context at $t=0$ is given by $A_{1}I∼_{1}+A_{2}I∼_{2}$. We have proven that this pulse input will ultimately reach the $dv$ slot with a magnitude of $\sum_{s=1}^{2}A_{s}E_{p_{s}→dv}+E_{p_{s}→iv_{s}}E_{iv_{s}→dv}$. This equation can be rewritten as

$$
\frac{1}{N}(A_{1}I∼_{1}+A_{2}I∼_{2})⋅(n_{dv}+E_{iv_{1}→dv}n_{iv_{1}}+E_{iv_{2}→dv}n_{iv_{2}})
$$

Therefore, we define $n_{tol}=n_{dv}+E_{iv_{1}→dv}n_{iv_{1}}+E_{iv_{2}→dv}n_{iv_{2}}$ as the pathway-based definition of the selection vector. Through calculations, we can prove that this pathway-based definition of the selection vector is equivalent to the classical definition based on linearized dynamical systems. In fact, the transition matrix of neuron activity in this rank-3 RNN is given by:

$$
M=−E+\frac{1}{N}G(m_{iv_{1}}n_{iv_{1}}^{T}+m_{iv_{2}}n_{iv_{2}}^{T}+m_{dv}n_{dv}^{T})−E+\frac{1}{N}(m∼_{iv_{1}}n_{iv_{1}}^{T}+m∼_{iv_{2}}n_{iv_{2}}^{T}+m∼_{dv}n_{dv}^{T}).
$$

Multiplying $M^{T}$ on the right by $n_{tol}$, we obtain:

$$
M^{T}n_{tol}=0.
$$

Moreover, under the condition that the choice axis is invariant across contexts, i.e., $m∼_{dv}$ is invariant across contexts (Mante et al., 2013; Pagan et al., 2022),

$$
\frac{m∼_{dv}}{‖m∼_{dv}‖_{2}}⋅(\frac{1}{N}‖m∼_{dv}‖_{2}n_{tol})=⟨m∼_{dv},n_{tol}⟩=1.
$$

This demonstrates that $\frac{1}{N}‖m∼_{dv}‖_{2}n_{tol}$ is indeed the left eigenvector of the transition matrix as well as the classical selection vector of the linearized dynamical systems.

### The equivalence between two definitions of selection vector modulation (Figure 5)

Here, we use the rank-3 RNN and input 1 as an example to explain why there is an equivalence between our definition of selection vector modulation and the classical one (Pagan et al., 2022). In the previous section, we have proven that the input representation direction and selection vector are given by $I∼_{1}$ and $s=\frac{1}{N}‖m∼_{dv}‖_{2}(n_{dv}+E_{iv_{1}→dv}n_{iv_{1}}+E_{iv_{2}→dv}n_{iv_{2}})$, respectively. According to the classical definition (Pagan et al., 2022), the input modulation and selection vector modulation are given by $mod_{inp}=ΔI∼_{1}⋅s¯$ and $mod_{sel}=I∼_{1}¯⋅Δs$, respectively. Since $m∼_{dv},n_{iv_{1}},n_{iv_{2}}$, and $n_{dv}$ are invariant across different contexts, we have:

$$
s¯=\frac{1}{N}‖m∼_{dv}‖_{2}(n_{dv}+E¯_{iv_{1}→dv}n_{iv_{1}}+E¯_{iv_{2}→dv}n_{iv_{2}}),
$$



$$
Δs=\frac{1}{N}‖m∼_{dv}‖_{2}(ΔE_{iv_{1}→dv}n_{iv_{1}}+ΔE_{iv_{2}→dv}n_{iv_{2}}).
$$

Substituting these into Equations 7 and 8 yields:

$$
mod_{inp}=‖m∼_{dv}‖_{2}(ΔE_{inp_{1}→dv}+ΔE_{inp_{1}→iv_{1}}E¯_{iv_{1}→dv}),
$$



$$
mod_{sel}=‖m∼_{dv}‖_{2}(E¯_{inp_{1}→iv_{1}}ΔE_{iv_{1}→dv}),
$$

a result fully consistent with the pathway-based definition in Equation 5 of the main text.

### Comparison between the pathway-based selection vector and the classical one (Figure 6)

We generate 1000 RNNs according to the procedure in Figure 5C (see Method ‘Mean-field-theory-based model construction’ for details), with each RNN defined by parameters $\alpha$, $\beta$ and $\gamma$ independently sampled from a Uniform (0, 1) distribution. For each RNN, we computed the selection vector for the RNN in a given context (e.g. context 1 or 2) in two ways:

via linearized dynamical system analysis following Mante et al., 2013, producing the selection vector $sv^{classical}$ (classical in Figure 6B), using the theoretical derivation $sv=n_{dv}+ηn_{iv_{1}}$ (‘our’s’ in Figure 6B).

We repeated this process 1000 times and measured the cosine angle between these two selection vectors and plotted the resulting distribution for context 1 (gray) and context 2 (blue) in Figure 6B.

### Pathway-based analysis of higher order low-rank RNNs (Figure 7A and B)

In this section, we will consider RNNs with more intermediate variables (Figure 7A). Here, we consider only one stimulus modality for simplicity and use the same notation convention as in the previous sections. The network consists of one input variable $k_{inp}$, $L$ intermediate variables $k_{iv_{i}},i=1,…,L$, and one decision variable $k_{dv}$. For simplicity, we let $k_{iv_{0}}$ be an alias for the input variable and $k_{iv_{L+1}}$ be an alias for the decision variable. We use the shorthand $E_{i→j}$ and $E_{i→dv}$ to denote the effective coupling $E_{iv_{i}→iv_{j}}$ and $E_{iv_{i}→dv}$, respectively. The dynamics of these task variables are given by

$$
\tau\frac{dk_{inp}}{dt}=−k_{inp}+u,
$$



$$
\tau\frac{dk_{iv_{i}}}{dt}=−k_{iv_{i}}+\sumj=0i−1E_{j→i}k_{iv_{j}},i=1,…,L,
$$



$$
\tau\frac{dk_{dv}}{dt}=\sumj=0LE_{j→L+1}k_{iv_{j}}.
$$

Consider the case when, at time $t=0$, the network receives a pulse input with unit size (i.e. $ut=\tau\delta(t)$). Then, we have

$$
k_{inp}=e^{\frac{−t}{\tau}},
$$



$$
k_{iv_{i}}=\sumj=1i\frac{K_{j}^{i}}{j!}e^{\frac{−t}{\tau}}(\frac{t}{\tau})^{j}i=0,…,n,
$$



$$
k_{dv}=k_{iv_{L+1}}=\sumj=1L+1K_{j}^{L+1}(1−\frac{Γ(j,\frac{t}{\tau})}{(j−1)!}),
$$

where $K_{j}^{i}=\sum0=a_{1}<a_{2}<…<a_{j}<iE_{a_{1}→a_{2}}⋅E_{a_{2}→a_{3}}⋅…⋅E_{a_{j}→i}$. In Equation 52, $Γ$ stands for the incomplete Gamma function and $Γj,\frac{t}{\tau}=\int_{t/\tau}^{∞}x^{j−1}e^{−x}dx$. These expressions tell us that, as time goes to infinity, all intermediate task variables $k_{iv_{i}},i=1,…,L$ will decay to zero and the decision variable will converge to $\sum_{j=1}^{L+1}K_{j}^{L+1}$, which means that a pulse input of unit size will ultimately reach the $dv$ slot with a magnitude of $\sum_{j=1}^{L+1}K_{j}^{L+1}$. Therefore, we define the total effective coupling from the input variable to the decision variable in this higher-order graph as

$$
E_{tol}=\sumj=1L+1\sum0=a_{1}<a_{2}<…<a_{j}\leqLE_{a_{1}→a_{2}}⋅E_{a_{2}→a_{3}}⋅…⋅E_{a_{j}→dv}.
$$

The difference of the total effective coupling between relevant context and irrelevant context can be decomposed into:

$$
ΔE_{tol}=\sumj=1L+1\sum0=a_{1}<a_{2}<…<a_{j}\leqLΔ(E_{a_{1}→a_{2}})⋅E_{a_{2}→a_{3}}⋅…⋅E_{a_{j}→dv}¯+\sumj=1L+1\sum0=a_{1}<a_{2}<…<a_{j}\leqLE_{a_{1}→a_{2}}¯⋅Δ(E_{a_{2}→a_{3}}⋅…⋅E_{a_{j}→dv}).
$$

The first term, caused by changing a stimulus input representation, is defined as the input modulation. The second term, the one without changing the stimulus input representation, is defined as the selection vector modulation.

Using a similar method in rank-3 RNNs, the selection vector for RNNs of higher order is given by:

$$
n_{dv}+\sumj=1L\sum0<a_{1}<…<a_{j}\leqL(E_{a_{1}→a_{2}}⋅…⋅E_{a_{j}→dv})n_{iv_{a_{1}}}.
$$

### Training of full-rank vanilla RNNs using backpropagation (Figure 7)

For Figure 7, we trained full-rank RNNs of $N=128$ neurons. We trained the elements of the input vectors, the connectivity matrix, and the readout vector. We tested a large range of regularization coefficients ranging from 0 to 0.1. For each $r_{reg}$ chosen from the set {0, 0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.007, 0.008, 0.009, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1}, we trained 100 full-rank RNNs. A larger $w_{reg}$ value results in a trained connectivity matrix $J$ with lower rank, making the network more similar to a rank-1 RNN. All trainable parameters were initialized with random independent Gaussian weights with a mean of 0 and variance of $1/N^{2}$. Only trained RNNs with their largest eigenvalue of the activity transition matrix falling within the –0.05–0.05 range in both contexts were selected for subsequent analysis.

To ensure that the conclusions drawn from Figure 7 are robust and not dependent on specific hyperparameter settings, we conducted similar experiments under different model hyperparameter settings. First, we trained RNNs with the softplus activation function and regularization coefficients chosen from {0.1, 0.09, 0.08, 0.07, 0.06, 0.05, 0.04, 0.03, 0.02, 0.01, 0.008, 0.004, 0.002, 0.001} (Figure 7—figure supplement 2A). Unlike tanh, softplus does not saturate on the positive end. Additionally, we tested the initialization of trainable parameters with a variance of $1/N$ (Figure 7—figure supplement 2B). Together, these experiments confirmed that the main results do not depend on the specific model hyperparameter settings.

#### Estimating matrix dimension and extra dimension (Figure 7)

##### Effective dimension of connectivity matrix (Figure 7D)

Let $\sigma_{1}\geq\sigma_{2}\geq…\geq\sigma_{n}$ be the singular values of the connectivity matrix. The matrix’s rank is the number of nonzero singular values. However, rank alone can overlook differences in how quickly those singular values decay. To capture this, we define the effective dimension as its stable rank (Sanyal et al., 2020):

$$
edim(J)=\sumi=1n\frac{\sigma_{i}^{2}}{\sigma_{1}^{2}}.
$$

Each term lies between 0 and 1, so the effective dimension satisfies $0\leqedimJ\leqrankJ$. When all nonzero singular values are equal, $edimJ$ equals the matrix rank. But if some singular values are much smaller than others, effective dimension will be closer to 1.

##### Single neuron response kernel for pulse input (Figure 7E)

We apply pulse-based linear regression (Pagan et al., 2022) to assess how pulse input affects neuron activity. The activity of neuron $i$ in trial $k$ at time step $t$ is given by:

$$
r_{i,t}(k)=\beta_{choice;i,t}choice(k)+\beta_{context;i,t}context(k)+\beta_{time;i,t}+\beta_{inp_{1},ctx_{c};i}∗u_{1,k}+\beta_{inp_{2},ctx_{c};i}∗u_{2,k},
$$

where $choice(k)$ is the RNN’s choice on trial $k$ defined as the sign of its output during the decision period, $context(k)$ is the context of trial $k$ (1 for context 1 and 0 for context 2), $u_{i,k}$ indicates signed input $i$ evidence as defined previously in Methods. The first three regression coefficients, $\beta_{choice;i,t}$, $\beta_{context;i,t}$ and $\beta_{time;i,t}$, capture the influence of choice, context, and time on the neuron’s activity at each time step, each being a 40-dimension vector. The remaining coefficient, $\beta_{inp_{1},ctx_{1};i}$, $\beta_{inp_{1},ctx_{2};i}$, $\beta_{inp_{2},ctx_{1};i}$, and $\beta_{inp_{2},ctx_{2};i}$, reflect the impact of pulse input on the neuron activity in a specific context, each also a 40-dimension vector. The asterisk (*) indicates the convolution operation between the response kernel and input evidence, described by:

$$
(\beta_{inp_{1},ctx_{c};i}∗u_{1,k})(t)=\sums=1tu_{1,k}(s)\beta_{inp_{1},ctx_{c};i}(t−s).
$$

Therefore, there are a total of 280 regression coefficients for each neuron. We obtained these coefficients using ridge regression with 1000 trials for each RNN. The coefficient $\beta_{inp_{i},ctx_{c};i}(t)$ is termed the single neuron response kernel for input $i$ in context $c$ (Figure 7E).

##### Response kernel modes and normalized percentage of explained variance (PEV) (Figure 7F)

For each RNN, we construct a matrix $B$ with shape $N_{t}\times(2N)$ from neuron response kernels for input 1 (or input 2) across both contexts, where $N_{t}=40$ represents time steps and $N$ is the number of neurons, with each column as a neuron’s response kernel in a context. Then we apply singular value decomposition (SVD) to the matrix:

$$
B=USV^{T}
$$

where $S$ is a diagonal square matrix of size $N_{t}$, with diagonal element $\sigma_{1}\geq\sigma_{2}\geq…\geq\sigma_{N_{t}}$ being the singular value of the matrix. The first column of U serves as a persistent mode (mode 0), while the second and following columns are transient modes (transient dynamical modes 1, 2, etc.). The normalized PEV of transient dynamical mode $r,r\geq1$ is defined as:

$$
PEV_{mode_{r}}=\frac{\sigma_{r+1}^{2}}{\sumi=240\sigma_{i}^{2}}.
$$

##### PEV of extra dynamical modes

The PEV of extra dynamical modes for input 1 (or 2) is defined based on the normalized PEV of transient dynamical mode:

$$
PEV_{ED}(inp_{1})=\sumr=1N_{t}−1PEV_{mode_{r}}.
$$

### The counterintuitive extreme example (Figure 7—figure supplement 3)

We can manually construct two models (RNN1 and RNN2) with distinct circuit mechanisms (input modulation versus selection vector modulation) but showing the same neural activities. Specifically, we generated three Gaussian random matrices ($M^{1},M^{2},M^{3}$) of shape 10,000 × 5, 10,000 × 5 and 10,000 × 1, respectively. Let $M_{:,r}^{p}$ denote the $r$-th column of matrix $M^{p}$. The two models have the same input vectors, output vectors, and input-selection vectors for intermediate task variables ($n_{iv_{1}}$ and $n_{iv_{2}}$), given by:

$$
I_{1}=[M_{:,1}^{(1)};M_{:,1}^{(2)};0],I_{2}=[M_{:,2}^{(1)};M_{:,2}^{(2)};0]
$$



$$
I_{1}^{ctx}=[M_{:,5}^{(1)};0;0],I_{2}^{ctx}=[0;M_{:,5}^{(2)};0]
$$



$$
m_{iv_{1}}=[M_{:,3}^{(1)};M_{:,3}^{(2)};0],m_{iv_{2}}=[M_{:,4}^{(1)};M_{:,4}^{(2)};0],m_{dv}=[0;0;M_{:,1}^{(3)}]
$$



$$
n_{iv_{1}}=[\frac{3}{1+g}M_{:,1}^{(1)};\frac{3}{1+g}M_{:,1}^{(2)};0],n_{iv_{2}}=[\frac{−3g}{1−g^{2}}M_{:,1}^{(1)};\frac{3}{1−g^{2}}M_{:,1}^{(2)};0],
$$

where $g=\int_{−∞}^{+∞}\frac{1}{\sqrt{2\pi}}e^{−x^{2}/2}ϕ^{`}xdx$. The difference between these two RNNs lies in their input-selection vector $n_{dv}$ for the decision variable. For RNN1, $n_{dv}$ is given by

$$
n_{dv}=[\frac{3}{1+g}M_{:,4}^{(1)};\frac{3}{1+g}M_{:,4}^{(2)};0]+[\frac{3}{1−g^{2}}M_{:,2}^{(1)};\frac{−3g}{1−g^{2}}M_{:,2}^{(2)};0]+[0;0;3M_{:,1}^{(3)}].
$$

For RNN2, $n_{dv}$ is given by:

$$
n_{dv}=[\frac{−3g}{1−g^{2}}M_{:,3}^{(1)};\frac{3}{1−g^{2}}M_{:,3}^{(2)};0]+[\frac{3}{1−g^{2}}M_{:,2}^{(1)};\frac{−3g}{1−g^{2}}M_{:,2}^{(2)};0]+[0;0;3M_{:,1}^{(3)}].
$$

In this construction, the information flow graphs from input 1 to the decision variable ($dv$) in each context for the two RNNs are shown in Figure 7—figure supplement 3A.

Although the connectivity matrices of the two networks are different (Figure 7—figure supplement 3B), when provided with the same input, the neuron activity of the $i$-th neuron in RNN1 is exactly the same as that of the $i$-th neuron in RNN2 at the same time point (Figure 7—figure supplement 3C). The statistical results of similarity between all neuron pairs are given in Figure 7—figure supplement 3D.

### Manually adding redundant structure and PEV of irrelevant activity (Figure 7—figure supplement 4)

#### Redundant RNN (Figure 7—figure supplement 4B and C)

To see if the currently proposed method can work when there is a significant amount of neural activity variance irrelevant to the task, we manually added irrelevant neural activity into the trained RNNs (termed as redundant RNNs). Specifically, we randomly choice $K=75$ trained vanilla RNNs (Figure 7D–G). To add irrelevant additional dimensions to the network without affecting the original function, for each RNN with N neurons, we build a larger RNN with $2N$ neurons equally divided into two populations. The input embeddings, readout vector, and the connectivity strengths between neurons within the first population (the first to the $N$-th neurons) are the same as the original RNN. As for the second population (the $N+1$-th to the $2N$-th neurons), the input embeddings are sampled with Gaussian noise, with the standard deviation equal to that of the original RNN input embeddings and the readout vector is set to 0. The connectivity strengths within the second population are sampled with Gaussian noise, with the standard deviation chosen such that the average sum of square activity of the two populations is nearly equal. Moreover, there is no connectivity between the two populations. The resulting RNN, compared to the original network, introduces adding task-irrelevant neural activity (neural activity in the second population). At the same time, it performs the CDM task in the same way as the original network, with the identical selection vector modulation value.

#### PEV of irrelevant activity (Figure 7—figure supplement 4C)

We hypothesize that the proportion of explained variance (PEV) in extra dynamical modes performs reliably for trained RNNs (Figure 7G) because task-irrelevant neural activity is minimal in these networks. To test this possibility, we conducted in-silico lesion experiments for the trained RNNs. The main idea is that if an RNN contains a large portion of task-irrelevant variance, there will exist a subspace (termed as task-irrelevant subspace) that captures this part of variance and removing this task-irrelevant subspace will not affect the network’s behavior.

Based on this idea, we developed an optimization method to identify such a task-irrelevant subspace for any given RNN. The main idea is to find a lesion subspace such that removing all neural activity within this subspace does not affect the network’s behavior, while capturing as much variance in neural activity caused by pulse inputs as possible. Specifically, for any given RNN, we constructed a new RNN with its connectivity matrix defined as $J^{`}=JE−QQ^{T}$, where $J$ is the connectivity matrix of the original RNN, $E$ is the identity matrix, and $Q$ is the orthogonal basis of the lesion subspace. Here, $Q$ is of shape $N\timesr$, where $r$ is the dimension of the subspace ($r=10$ in Figure 7—figure supplement 4). For the new RNN, the matrix $E−QQ^{T}$ removes all components of neural activity within the lesion subspace. We try to find the best $Q$ by minimizing:

$$
ℓ=\lambda\frac{(Z_{40}−Z^_{40})^{2}}{(Z^_{40})^{2}}+(1−\frac{∥f^Q∥_{2}^{2}}{∥f^∥_{2}^{2}})
$$

where $z_{40}$ is the network’s output at the last time step for pulse input at the beginning, $z^_{40}$ is the output without lesion, $f^$ is a $40\timesN$ matrix, indicating the neuron activities caused by a pulse input for the RNN without lesion, $\lambda=10$ is a hyperparameter balancing the two parts. We only consider input 1 under condition one for simplicity. The first part ensures that after removing neural activity in the $Q$ subspace, the network’s output in response to unit pulse remains unchanged. The second part aims to maximize the variance of neuron activity captured by lesion subspace. The orthogonal basis $Q$ is parameterized using the Cayley transform: $Q=E+A−A^{T}E−A+A^{T}^{−1}$. Matrix $A$ is optimized using gradient descent with the Adam optimizer with a learning rate of $10^{−5}$. The training process lasts for 2000 steps and the maximum of $\frac{f^Q_{2}^{2}}{f^_{2}^{2}}$ under the condition of $\frac{(Z_{40}−Z^_{40})^{2}}{(Z^_{40})^{2}}<10^{−3}$ is defined as the network’s PEV of irrelevant activity (Figure 7—figure supplement 4C).
