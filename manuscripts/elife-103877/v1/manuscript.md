# A differentiable Gillespie algorithm for simulating chemical kinetics, parameter estimation, and designing synthetic biological circuits

## Authors

- Krishna Rijal<sup>1</sup> ([ORCID: 0000-0001-7236-7387](https://orcid.org/0000-0001-7236-7387)) †
- Pankaj Mehta<sup>1</sup> ([ORCID: 0000-0003-1290-5897](https://orcid.org/0000-0003-1290-5897))

### Affiliations

1. Department of Physics, Boston University Boston United States ([ROR:05qwgg493](https://ror.org/05qwgg493))

† Corresponding author

## Abstract

The Gillespie algorithm is commonly used to simulate and analyze complex chemical reaction networks. Here, we leverage recent breakthroughs in deep learning to develop a fully differentiable variant of the Gillespie algorithm. The differentiable Gillespie algorithm (DGA) approximates discontinuous operations in the exact Gillespie algorithm using smooth functions, allowing for the calculation of gradients using backpropagation. The DGA can be used to quickly and accurately learn kinetic parameters using gradient descent and design biochemical networks with desired properties. As an illustration, we apply the DGA to study stochastic models of gene promoters. We show that the DGA can be used to: (1) successfully learn kinetic parameters from experimental measurements of mRNA expression levels from two distinct Escherichia coli promoters and (2) design nonequilibrium promoter architectures with desired input–output relationships. These examples illustrate the utility of the DGA for analyzing stochastic chemical kinetics, including a wide variety of problems of interest to synthetic and systems biology.

## Introduction

Randomness is a defining feature of our world. Stock market fluctuations, the movement of particles in fluids, and even the change of allele frequencies in organismal populations can all be described using the language of stochastic processes. For this reason, disciplines as diverse as physics, biology, ecology, evolution, finance, and engineering have all developed tools to mathematically model stochastic processes (Van Kampen, 1992; Gardiner, 2009; Rolski et al., 2009; Wong and Hajek, 2012). In the context of biology, an especially fruitful area of research has been the study of stochastic gene expression in single cells (McAdams and Arkin, 1997; Elowitz et al., 2002; Raj and van Oudenaarden, 2008; Sanchez and Golding, 2013). The small number of molecules involved in gene expression make stochasticity an inherent feature of protein production and numerous mathematical and computational techniques have been developed to model gene expression and relate mathematical models to experimental observations (Paulsson, 2005; Wilkinson, 2018).

One prominent computational algorithm for understanding stochasticity in gene expression is the Gillespie algorithm, with its Direct Stochastic Simulation Algorithm variant being the most commonly used method (Doob, 1945; Gillespie, 1977). The Gillespie algorithm is an extremely efficient computational technique used to simulate the time evolution of a system in which events occur randomly and discretely (Gillespie, 1977). Beyond gene expression, the Gillespie algorithm is widely employed across numerous disciplines to model stochastic systems characterized by discrete, randomly occurring events including epidemiology (Pineda-Krch, 2008), ecology (Parker and Kamenev, 2009; Dobramysl et al., 2018), neuroscience (Benayoun et al., 2010; Rijal et al., 2024), and chemical kinetics (Gillespie, 1976; Gillespie, 2007).

Here, we revisit the Gillespie algorithm in light of the recent progress in deep learning and differentiable programming by presenting a ‘fully differentiable’ variant of the Gillespie algorithm we dub the differentiable Gillespie algorithm (DGA). The DGA modifies the traditional Gillespie algorithm to take advantage of powerful automatic differentiation libraries for example, PyTorch (Paszke et al., 2019), Jax (Bradbury et al., 2018), and Julia (Bezanson et al., 2017) and gradient-based optimization. The DGA allows us to quickly fit kinetic parameters to data and design discrete stochastic systems with a desired behavior. Our work is similar in spirit to other recent work that seeks to harness the power of differentiable programming to accelerate scientific simulations (Liao et al., 2019; Schoenholz and Cubuk, 2020; Wei et al., 2019; Degrave et al., 2019; Arya et al., 2022; Arya et al., 2023; Bezgin et al., 2023). The DGA’s use of differential programming tools also complements more specialized numerical methods designed for performing parameter sensitivity analysis on Gillespie simulations such as finite-difference methods (Anderson, 2012; Srivastava et al., 2013; Thanh et al., 2018), the likelihood ratio method (Glynn, 1990; McGill et al., 2012; Núñez and Vlachos, 2015), and pathwise derivative methods (Sheppard et al., 2012).

One of the difficulties in formulating a differentiable version of the Gillespie algorithm is that the stochastic systems it treats are inherently discrete. For this reason, there is no obvious way to take derivatives with respect to kinetic parameters without making approximations. As shown in Figure 1, in the traditional Gillespie algorithm both the selection of the index for the next reaction and the updates of chemical species are both discontinuous functions of the kinetic parameters. To circumnavigate these difficulties, the DGA modifies the traditional Gillespie algorithm by approximating discrete operations with continuous, differentiable functions, smoothing out abrupt transitions to facilitate gradient computation via automatic differentiation (Figure 1). This significant modification preserves the core characteristics of the original algorithm while enabling integration with modern deep learning techniques.

![Figure 1.](https://cdn.elifesciences.org/articles/103877/elife-103877-fig1-v1.jpg)

**Figure 1.:** (a) Example of kinetics with $N=3$ reactions with rates $r_{i}(i=1,2,3)$. (b) Illustration of the DGA’s approximations: replacing the non-differentiable Heaviside and Kronecker delta functions with smooth sigmoid and Gaussian functions, respectively. (c) Flow chart comparing exact and differentiable Gillespie simulations.

One natural setting for exploring the efficacy of the DGA is recent experimental and theoretical works exploring stochastic gene expression. Here, we focus on a set of beautiful experiments that explore the effect of promoter architecture on steady-state gene expression (Jones et al., 2014). An especially appealing aspect of Jones et al., 2014 is that the authors independently measured the kinetic parameters for these promoter architectures using orthogonal experiments. This allows us to directly compare the predictions of DGA to ground truth measurements of kinetic parameters. We then extend our considerations to more complex promoter architectures (Lammers et al., 2023) and illustrate how the DGA can be used to design circuits with a desired input–output relation.

## Results

### A differentiable approximation to the Gillespie algorithm

Before proceeding to discussing the DGA, we start by briefly reviewing how the traditional Gillespie algorithm simulates discrete stochastic processes. For concreteness, in our exposition, we focus on the chemical system shown in Figure 1 consisting of three species, A, B, and C, whose abundances are described by a state vector $x=(x_{1},x_{2},x_{3})$. These chemical species can undergo $N=3$ chemical reactions, characterized by rate constants, $r_{i}(x)$ where $i=1,…,3$, and a stoichiometric matrix $S_{i\alpha}$ whose ith row encodes how the abundance $x_{\alpha}$ of species $\alpha$ changes due to reaction $i$. Note that in what follows, we will often supress the dependence of the rates $r_{i}(x)$ on $x$ and simply write $r_{i}$.

In order to simulate such a system, it is helpful to discretize time into small intervals of size $Δt≪1$. The probability that a reaction $i$ with rate $r_{i}$ occurs during such an interval is simply $r_{i}Δt$. By construction, we choose $Δt$ to be small enough that $r_{i}Δt≪1$ and that the probability that a reaction occurs in any interval $Δt$ is extremely small and well described by a Poisson process. This means that naively simulating such a process is extremely inefficient because, in most intervals, no reactions will occur.

### Gillespie algorithm

The Gillespie algorithm circumnavigates this problem by: (1) exploiting the fact that the reactions are independent so that the rate at which any reaction occurs is also described by an independent Poisson process with rate $R=Σ_{i}r_{i}$ and (2) the waiting time distribution $p(\tau)$ of a Poisson process with rate $R$ is the exponential distribution $p(\tau)=Re^{−R\tau}$. The basic steps of the Gillespie algorithm are illustrated in Figure 1.

The simulation begins with the initialization of time and state variables:

$$
t=0,x=x_{0},
$$

where $t$ is the simulation time. One then samples the waiting time distribution $p(\tau)$ for a reaction to occur to determine when the next the reaction occurs. This is done by drawing a random number $u$ from a uniform distribution over $[0,1]$ and updating

$$
t→t−R^{−1}ln⁡(u).
$$

Note that this time update is a fully differentiable function of the rates $r_{i}$.

In order to determine which of the reactions $i^{′}$ occurs after a time $\tau$, we note that probability that reaction $i$ occurs is simply given by $q_{i}=r_{i}/R$. Thus, we can simply draw another random number $u^{′}$ and choose $i^{′}$ such that $i^{′}$ equals the smallest integer satisfying

$$
\sumi=1i^{′}r_{i}/R>u^{′}.
$$

The reaction abundances $x$ are then updated using the stoichiometric matrix

$$
x_{\alpha}→x_{\alpha}+S_{i^{′}\alpha}.
$$

Unlike the time update, both the choice of the reaction $i^{′}$ and the abundance updates are not differentiable since the choice of the reaction $i^{′}$ is a discontinuous function of the parameters $r_{i}$.

### Approximating updates in the Gillespie with differentiable functions

In order to make use of modern deep learning techniques and modern automatic differentiation packages, it is necessary to modify the Gillespie algorithm in such as way as to make the choice of reaction index (Equation 2) and abundance updates (Equation 3) differentiable functions of the kinetic parameters. To do so, we rewrite Equation 2 using a sum of Heaviside step function $Θ(y)$ (recall $Θ(y)=0$ if $y<0$ and $Θ(y)=1$ if $y>0)$:

$$
i^{′}=1+\sumi=1N−1Θ(u^{′}−\frac{r_{i}}{R})
$$

This formulation of index selection makes clear the source of non-differentiability. The derivative of the $i^{′}$ with respect to $r_{i}$ does not exist at the transition points where the Heaviside function jumps (see Figure 1b).

This suggests a natural modification of the Gillespie algorithm to make it differentiable – replacing the Heaviside function $Θ(y)$ by a sigmoid function of the form

$$
\sigma(y)=\frac{1}{1+e^{−\frac{y}{a}}}
$$

where we have introduced a ‘hyper-parameter’ $a$ that controls the steepness of the sigmoid and plays an analogous role to temperature in a Fermi function in statistical mechanics. A larger value of $a^{−1}$ results in a steeper slope for the sigmoid functions, thereby more closely approximating the true Heaviside functions which is recovered in the limit $a→0$ (see Figure 1b). With this replacement, the index selection equation becomes

$$
i^{′}=1+\sumi=1N−1\sigma(\frac{1}{a}(u^{′}−\frac{r_{i}}{R}))
$$

Note that in making this approximation, our index is no longer an integer, but instead can take on all real values between 0 and $N$. However, by making $a$ sufficiently small, Equation 6 still serves as a good approximation to the discrete jumps in Equation 4. In general, $a$ is a hyperparameter that is chosen to be as small as possible while still ensuring that the gradient of $i^{′}$ with respect to the kinetic parameters $r_{i}$ can be calculated numerically with high accuracy. For a detailed discussion, please see Appendix 1—figure 1 and Appendix 1.

Since the index $i^{′}$ is no longer an integer but a real number, we must also modify the abundance update in Equation 3 to make it fully differentiable. To do this, we start by rewriting Equation 3 using the Kronecker delta $\delta_{ij}$ (where $\delta_{ij}=1$ if $i=j$ and $\delta_{ij}=0$ if $i\neqj$) as

$$
x_{\alpha}→x_{\alpha}+\sumi=1N\delta_{ii^{′}}S_{i\alpha}
$$

Since $i^{′}$ is no longer an integer, we can approximate the Kronecker delta $\delta_{ii^{′}}$ by a Gaussian function, to arrive at the approximate update equation

$$
x_{\alpha}→x_{\alpha}+\sumi=1Ne^{−\frac{1}{b}(i^{′}−i)^{2}}S_{i\alpha}.
$$

The hyperparameter $b$ is generally chosen to be as small as possible while still ensuring numerical stability of gradients (Appendix 1—figure 1). Note by using an abundance update of the form Equation 8, the species abundances $x$ are now real numbers. This is in stark contrast with the exact Gillespie algorithm where the abundance update (Equation 7) ensures that the $x_{\alpha}$ are all integers.

### Combining the DGA with gradient-based optimization

The goal of making Gillespie simulations differentiable is to enable the computation of the gradient of a loss function, $L(\theta)$, with respect to the kinetics parameters $\theta$. A loss function quantifies the difference between simulated and desired values for quantities of interest. For example, when employing the DGA in the context of fitting noisy gene expression models, a natural choice for $L(\theta)$ is the difference between the simulated and experimentally measured moments of mRNA/protein expression (or alternatively, the Kullback–Leibler divergence between the experimental and simulated mRNA/protein expression distributions if full distributions can be measured). When using the DGA to design gene circuits, the loss function can be any function that characterizes the difference between the simulated and desired values of the input–output relation.

The goal of the optimization using the DGA is to find parameters $\theta$ that minimize the loss. The basic workflow of a DGA-based optimization is shown in Figure 2. One starts with an initial guess for the parameters $\theta_{0}$. One then uses DGA algorithm to simulate the systems and calculate the gradient of the loss function $∇_{\theta}L(\theta)$. One then updates the parameters, moving in the direction of the gradient using gradient descent or more advanced methods such as ADAM (Kingma and Ba, 2014; Mehta et al., 2019), which uses adaptive estimates of the first and second moments of the gradients to speed up convergence to a local minimum of the loss function.

![Figure 2.](https://cdn.elifesciences.org/articles/103877/elife-103877-fig2-v1.jpg)

**Figure 2.:** The process begins by initializing the parameters $\theta→=\theta_{0}→$. Simulations are then run using the DGA to obtain statistics ${S_{i}(\theta→)}$ like moments. These statistics are used to compute the loss $L({S_{i}})$, and the gradient of the loss $∇L$ is obtained. Finally, parameters are updated using the ADAM optimizer, and the process iterates to minimize the loss.

### The price of differentiability

A summary of the DGA is shown in Figure 1. Unsurprisingly, differentiability comes at a price. The foremost of these is that unlike the Gillespie algorithm, the DGA is no longer exact. The DGA replaces the exact discrete stochastic system by an approximate differentiable stochastic system. This is done by allowing both the reaction index and the species abundances to be continuous numbers. Though in theory, the errors introduced by these approximations can be made arbitrarily small by choosing the hyper-parameters $a$ and $b$ small enough (see Figure 1), in practice, gradients become numerically unstable when $a$ and $b$ are sufficiently small (see Appendix 1 and Appendix 1—figure 1).

In what follows, we focus almost exclusively on steady-state properties that probe the ‘bulk’, steady-state properties of the stochastic system of interest. We find the DGA works well in this setting. However, we note that the effect of the approximations introduced by the DGA may be pronounced in more complex settings such as the calculation of rare events, modeling of tail-driven processes, or dealing with non-stationary time series.

In order to better understand the DGA in the context of stochastic gene expression, we benchmarked the DGA on a simple two-state promoter model inspired by experiments in Escherichia coli (Jones et al., 2014). This simple model had several advantages that make it well suited for exploring the performance of DGA. These include the ability to analytically calculate mRNA expression distributions and independent experimental measurements of kinetic parameters.

### Two-state promoter model

Gene regulation is tightly regulated at the transcriptional level to ensure that genes are expressed at the right time, place, and in the right amount (Phillips et al., 2012). Transcriptional regulation involves various mechanisms, including the binding of transcription factors to specific DNA sequences, the modification of chromatin structure, and the influence of non-coding RNAs, which collectively control the initiation and rate of transcription (Phillips et al., 2012; Sanchez et al., 2013; Phillips et al., 2019). By orchestrating these regulatory mechanisms, cells can respond to internal signals and external environmental changes, maintaining homeostasis and enabling proper development and function.

Here, we focus on a classic two-state promoter gene regulation (Jones et al., 2014). Two-state promoter systems are commonly studied because they provide a simplified yet powerful model for understanding gene regulation dynamics. These systems, characterized by promoters toggling between active and inactive states, offer insights into how genes are turned on or off in response to various stimuli (see Figure 3a). The two-state gene regulation circuit involves the promoter region, where RNA polymerase (RNAP) binds to initiate transcription and synthesize mRNA molecules at a rate $r$. A repressor protein can also bind to the operator site at a rate $k_{on}^{R}$ and unbind at a rate $k_{off}^{R}$. When the repressor is bound to the operator, it prevents RNAP from accessing the promoter, effectively turning off transcription. mRNA is also degraded at a rate $\gamma$. An appealing feature of this model is that both mean mRNA expression and the Fano factor can be calculated analytically and there exist beautiful quantitative measurements of both these quantities (Figure 3b). For this reason, we use this two-state promoters to benchmark the efficacy of DGA below.

![Figure 3.](https://cdn.elifesciences.org/articles/103877/elife-103877-fig3-v1.jpg)

**Figure 3.:** (a) Schematic of gene regulatory circuit for transcriptional repression. RNA polymerase (RNAP) binds to the promoter region to initiate transcription at a rate $r$, leading to the synthesis of mRNA molecules (red curvy lines). mRNA is degraded at a rate $\gamma$. A repressor protein can bind to the operator site, with association and dissociation rates $k_{on}^{R}$ and $k_{off}^{R}$, respectively. (b) Experimental data from Phillips et al., 2019, showing the relationship between the mean mRNA level and the Fano factor for two different promoter constructs: lacUD5 (green squares) and 5DL1 (red squares).

### Characterizing errors due to approximations in the DGA

We begin by testing the DGA to do forward simulations on the two-state promoter system described above and comparing the results to simulations performed with the exact Gillespie algorithm (see Appendix 2 for simulation details). Figure 4a compares the probability distribution function (PDF) for the steady-state mRNA levels obtained from the DGA (in red) and the exact Gillespie simulation (in blue). The close overlap of these distributions demonstrates that the DGA can accurately replicate the results of the exact Gillespie simulation. This is also shown by the very close match of the first four moments $⟨m^{n}⟩$ of the mRNA count between the exact Gillespie and the DGA in Figure 4b, though the DGA systematically overestimates these moments. As observed in Figure 4a, the DGA also fails to accurately capture the tails of the underlying PDF. This discrepancy arises because rare events result from very frequent low-probability reaction events where the sigmoid approximation used in the DGA significantly impacts the reaction selection process and, consequently, the final simulation results.

![Figure 4.](https://cdn.elifesciences.org/articles/103877/elife-103877-fig4-v1.jpg)

**Figure 4.:** Comparison between the DGA and exact simulations for (a) steady-state mRNA distribution, (b) moments of the steady-state mRNA distribution, and (d) the probability for the promoter to be in the ‘ON’ or ‘OFF’ state. (c) Ratio of the Jensen–Shannon divergence $JSD(p_{DGA}||p_{exact}^{ss})$ between the differentiable Gillespie probability distribution function (PDF) $p_{DGA}$ and the exact steady-state PDF $p_{exact}^{ss}$, and the Shannon entropy $H(p_{exact}^{ss})$ of the exact steady-state PDF. In all of the plots, 2000 trajectories are used. The simulation time used in panels (a), (b), and (d) is marked by blue ‘x’. Parameter values: $k_{on}^{R}=0.5$, $k_{off}^{R}=1.0$, $r=10$, $\gamma=1$, $1/a=200$, and $1/b=20$.

Next, we compare the accuracy of the DGA in simulating mRNA abundance distributions across a range of simulation times (see Figure 4c). The accuracy is quantified by the ratio of the Jensen–Shannon divergence $JSD(p_{DGA}||p_{exact}^{ss})$ between the differentiable Gillespie PDF $p_{DGA}$ and the exact steady-state PDF $p_{exact}^{ss}$, and the entropy $H(p_{exact}^{ss})$ of the exact steady-state PDF. For probability distributions $P$ and $Q$ over the same discrete space $X$, the JSD and H are defined as:

$$
JSD(P∥Q)=\frac{1}{2}D_{KL}(P∥M)+\frac{1}{2}D_{KL}(Q∥M)H(P)=−\sumx\inXP(x)log⁡P(x)
$$

where $M=\frac{1}{2}(P+Q)$ and $D_{KL}$ denotes the Kullback–Leibler divergence

$$
D_{KL}(P∥Q)=\sumx\inXP(x)log⁡\frac{P(x)}{Q(x)}
$$

The ratio $\frac{JSD}{H}$ normalizes divergence by entropy, enabling meaningful comparison across systems. As expected, the $\frac{JSD}{H}$ ratio decreases with increasing simulation time, indicating convergence toward the steady-state distribution of the exact Gillespie simulation. By ‘steady-state distribution’, we mean the long-term probability distribution of states that the exact Gillespie algorithm approaches after a simulation time of 104. The saturation of the $\frac{JSD}{H}$ ratio at approximately 0.003 for long simulation times is due to the finite values of $a^{−1}$ and $b^{−1}$. In percentage terms, this ratio represents a 0.3% divergence, meaning that the DGA’s approximation introduces only a 0.3% deviation from the exact distribution, relative to the total uncertainty (entropy) in the exact system.

Finally, the bar plot in Figure 4d shows simulation results for the probability of the promoter being in the ‘OFF’ and ‘ON’ states as predicted by the DGA (in red) and the exact Gillespie simulation (in blue). The differentiable Gillespie overestimates the probability of being in the ‘OFF’ state and underestimates the probability of being in the ‘ON’ state. Nonetheless, given the discrete nature of this system, the DGA does a reasonable job of matching the results of the exact simulations.

As we will see below, despite these errors the DGA is able to accurately capture gradient information and hence works remarkably well at gradient-based optimization of loss functions.

### Parameter estimation using the DGA

In many applications, one often wants to estimate kinetic parameters from experimental measurements of a stochastic system (Tian et al., 2007; Munsky et al., 2009; Komorowski et al., 2009; Villaverde et al., 2019). For example, in the context of gene expression, biologists are often interested in understanding biophysical parameters such as the rate at which promoters switch between states or a transcription factor unbinds from DNA. However, estimating kinetic parameters in stochastic systems poses numerous challenges because the vast majority of methods for parameter estimation are designed with deterministic systems in mind. Moreover, it is often difficult to analytically calculate likelihood functions making it difficult to perform statistical inference. One attractive method for addressing these difficulties is to combine differentiable Gillespie simulations with gradient-based optimization methods. By choosing kinetic parameters that minimize the difference between simulations and experiments as measured by a loss function, one can quickly and efficiently estimate kinetic parameters and error bars.

### Loss function for parameter estimation

To use the DGA for parameter estimation, we start by defining a loss function $L(\theta)$ that measures the discrepancy between simulations and experiments. In the context of the two-state promoter model (Figure 3), a natural choice of loss function is the square error between the simulated and experimentally measured mean and standard deviations of the steady-state mRNA distributions:

$$
L(\theta)=(⟨m⟩^−⟨m⟩)^{2}+(\sigma^_{m}−\sigma_{m})^{2},
$$

where $⟨m⟩^$ and $\sigma^_{m}$ denote the mean and standard deviation obtained from DGA simulations, and $⟨m⟩$ and $\sigma_{m}$ are the experimentally measured values of the same quantities. Having specified the loss function and parameters, we then use the gradient-based optimization to minimize the loss and find the optimal parameters $\theta^$ (see Figure 2). Note that in general the solution to the optimization problem need not be unique (see below).

### Confidence intervals and visualizing loss landscapes

Given a set of learned parameters $\theta^$ that minimize $L(\theta)$, one would also ideally like to assign a confidence interval (CI) to this estimate that reflect how constrained these parameters are. One natural way to achieve this is by examining the curvature of the loss function as the parameter $\theta_{i}$ varies around its minimum value, $\theta_{i}^{min}$. Motivated by this, we define the 95% CIs for parameter $\theta_{i}$ by:

$$
CI_{\theta_{i}}=[\theta_{i}^{min}−\delta,\theta_{i}^{min}+1.96\delta_{\theta_{i}}]
$$

where

$$
\delta_{\theta_{i}}=(\sqrt{\frac{∂^{2}L}{∂\theta_{i}^{2}}})^{−1}|_{\theta_{i}=\theta_{i}^{min}}
$$

and $L(\theta_{i}^{min}−\delta)=L(\theta_{i}^{min}+1.96\delta_{\theta_{i}})$. A detailed explanation of how to numerically estimate the CIs is given in Appendix 3.

One shortcoming of Equation 13 is that it treats each parameter in isolation and ignores correlations between parameters. On a technical level, this is reflected in the observation that the CIs only know about the diagonal elements of the full Hessian $∂_{ij}^{2}L(\theta)$. This shortcoming is especially glaring when there are many sets of parameters that all optimize the loss function (Einav et al., 2018; Razo-Mejia et al., 2018). As discuss below, this is often the case in many stochastic systems including the two-state promoter architecture in Figure 3. For this reason, it is often useful to make two dimensional plots of the loss function $L(\theta)$. To do so, for each pair of parameters, we simply sample the parameters around their optimal value and forward simulate to calculate the loss function $L(\theta)$. We then use this simulations to create two-dimensional heat maps of the loss function. This allows us to identify ‘soft directions’ in parameter space, where the loss function $L(\theta)$ changes slowly, indicating weak sensitivity to specific parameter combinations.

### Parameter estimation on synthetic data

Before proceeding to experiments, we start by benchmarking the DGA’s ability to perform parameter estimation on synthetic data generated using the two-state promoter model shown in Figure 3. This model nominally has four independent kinetic parameters: the rate at which repressors bind the promoter, $k_{on}^{R}$; the rate at which the repressor unbinds from the promoter, $k_{off}^{R}$; the rate at which mRNA is produced, $r$; and the rate at which mRNA degrades, $\gamma$. Since we are only concerned with steady-state properties of the mRNA distribution, we choose to measure time in units of the off rate and set $k_{off}^{R}=1$ in everything that follows. In Appendix 4, we make use of exact analytical results for $⟨m⟩$ and $\sigma_{m}$ to show that the solution to the optimization problem specified by loss function in Equation 11 is degenerate – there are many combinations of the three parameters ${k_{on}^{R},r,\gamma}$ that all optimize $L(\theta)$. On the other hand, if one fixes the mRNA degradation rate $\gamma$, this degeneracy is lifted and there is a unique solution to the optimization problem for the two parameters ${k_{on}^{R},r}$. We discuss both these cases below.

### Generating synthetic data

To generate synthetic data, we randomly sample the three parameters: $k_{on}^{R}$, $r$, and $\gamma$ within the range $[0.1,10]$, while keeping $k_{off}^{R}$ fixed at 1. In total, we generate 20 different sets of random parameters. We then perform exact Gillespie simulations for each set of parameters. Using these simulations, we obtain the mean $⟨m⟩$ and standard deviation $\sigma_{m}$ of the mRNA levels, which are then used as input to the loss function in Equation 11. We then use the DGA to estimate the parameters using the procedure outlined above and compare the resulting predictions with ground truth values for simulations.

### Estimating parameters in the non-degenerate case

We begin by considering the case where the mRNA degradation rate $\gamma$ is known and the goal is to estimate the two other parameters: the repressor binding rate $k_{on}^{R}$ and the mRNA production rate $r$. As discussed above, in this case, the loss function in Equation 11 has a unique minima, considerably simplifying the inference task. Figure 5a shows a scatter plot of the learned and the true parameter values for wide variety of choices of $\gamma$. As can be seen, there is very good agreement between the true parameters and learned parameters. Figure 5c shows that even when the true and learned parameters differ, the DGA can predict the mean $⟨m⟩$ and standard deviation $\sigma_{m}$ of the steady-state mRNA distribution almost perfectly (see Appendix 5 for discussion of how error bars were estimated). To better understand this, we selected a set of learned parameters: $k_{on}^{R}=0.87$, $r=3.83$, and $\gamma=2.43$. We then plotted the loss function in the neighborhood of these parameters (Figure 5b). As can be seen, the loss function around the true parameters is quite flat and the learned parameters live at the edge of this flat region. The flatness of the loss function reflects the fact that the mean and standard deviation of the mRNA distribution depend weakly on the kinetic parameters.

![Figure 5.](https://cdn.elifesciences.org/articles/103877/elife-103877-fig5-v1.jpg)

**Figure 5.:** Parameters $k_{off}^{R}$ are fixed at 1, with $1/a=200$ and $1/b=20$ for a simulation time of 10. (a) Scatter plot of true versus inferred parameters ($k^_{on}^{R}$ and $r^$) with $\gamma$ constant. Error bars are 95% confidence intervals (CIs). Panel (b) plots the logarithm of the loss function near a learned parameter set (shown in red circles in (a)), showing insensitivity regions. Panel (c) compares true and predicted mRNA mean and standard deviation with 95% CIs.

### Estimating parameters for the degenerate case

We now estimate parameters for the two-state promoter model when all three parameters $k_{on}^{R}$, $r$, and $\gamma$ are unknown. As discussed above, in this case, there are many sets of parameters that all minimize the loss function in Equation 11. Figure 6a shows a comparison between the learned and true parameters along with a heat map of the loss function for one set of synthetic parameters (Figure 6b). As can be seen in the plots, though the true parameters and learned parameter values differ significantly, they do so along ‘sloppy’ directions where loss function is flat. Consistent with this intuition, we performed simulations comparing the mean $⟨m⟩^$ and standard deviation $\sigma^_{m}$ of the steady-state mRNA levels using the true and learned parameters and found near-perfect agreement across all of the synthetic data (Figure 6c).

![Figure 6.](https://cdn.elifesciences.org/articles/103877/elife-103877-fig6-v1.jpg)

**Figure 6.:** Parameters $k_{off}^{R}$ are fixed at 1, with $1/a=200$ and $1/b=20$ for a simulation time of 10. (a) Scatter plot of true versus inferred parameters ($k^_{on}^{R}$, $r^$, and $\gamma$). Error bars are 95% confidence intervals (CIs). Panel (b) plots the logarithm of the loss function near a learned parameter set (shown in red circles in (a)), showing insensitivity regions. Panel (c) compares true and predicted mRNA mean and standard deviation with 95% CIs.

### Parameter estimation on experimental data

In the previous section, we demonstrated that our DGA can effectively obtain parameters for synthetic data. However, real experimental data often contains noise and variability, which can complicate the parameter estimation process. To test the DGA in this more difficult setting, we reanalyze experiments by Jones et al., 2014 which measured how mRNA expression changes in a system well described by the two-state gene expression model in Figure 3. In these experiments, two constitutive promoters lacUD5 and 5DL1 (with different transcription rates $r$) were placed under the control of a LacI repressor through the insertion of a LacI binding site. By systematically varying LacI concentrations, the authors were able to adjust the repressor binding rate $k_{on}^{R}$. mRNA fluorescence in situ hybridization was employed to measure mRNA expression, providing data on both mean expression levels $⟨m⟩$ and the variability as quantified by the Fano factor $f=\sigma_{m}^{2}/⟨m⟩$ for both promoters (see Figure 3b).

Given a set of measurements of the mean and Fano factor ${⟨m⟩_{i},f_{i}^{m}}$ for a promoter (lacUD5 and 5DL1), we construct a loss function of the form:

$$
L=\sumi=1N(⟨m⟩_{i}^−⟨m⟩_{i})^{2}+\sumi=1N(\sigma^_{i}^{m}−\sqrt{f_{i}^{m}⟨m⟩_{i}})^{2},
$$

where $i$ runs over data points (each with a different lac repressor concentration) and $⟨m⟩_{i}^$ and $\sigma^_{i}^{m}$ are the mean and standard deviation obtained from a sample of DGA simulations. This loss function is chosen because, at its minimum, $⟨m⟩_{i}^=⟨m⟩_{i}$ and $\sigma^_{i}^{m}=\sqrt{f_{i}^{m}⟨m⟩_{i}}$ for all $i$. As above, we set $k_{off}^{R}=1$, and focus on estimating the other three parameters ${r,\gamma,k_{on}^{R}}$. When performing our gradient-based optimization, we assume that the transcription rate $r$ and the mRNA degradation rate $\gamma$ are the same for all data points $i$, while allowing $k_{on}^{R}$ to vary across data points $i$. This reflects the fact that $k_{on}^{R}$ is a function of the lac repressor concentration which, by design, is varied across data points (see Appendix 6 for details on how this optimization is implemented and calculation of error bars).

The results of this procedure are summarized in Figure 7. We find that for the lacUD5 promoter $r^=90.25$, $\gamma^=6.20$ and that $k^_{on}^{R}$ varies from a minimum value of 0.18 to a maximum value of 99.0. For the 5DL1 promoters $r^=87.48$ and $\gamma^=9.80$ and $k^_{on}^{R}$ varies between 3.64 and 99.0. Recall that we have normalized all rates to the repressor unbinding rate $k_{off}^{R}=1$. These values indicate that mRNA transcription occurs much faster compared to the unbinding of the repressor, suggesting that once the promoter is in an active state, it produces mRNA rapidly. The relatively high mRNA degradation rates indicate a mechanism for fine-tuning gene expression levels, ensuring that mRNA does not persist too long in the cell, which could otherwise lead to prolonged expression even after promoter deactivation.

![Figure 7.](https://cdn.elifesciences.org/articles/103877/elife-103877-fig7-v1.jpg)

**Figure 7.:** (a) Comparison between theoretical predictions from the DGA (solid curves) and experimental values of mean and the Fano factor for the steady-state mRNA levels are represented by square markers, along with the error bars, for two different promoters, lacUD5 and 5DL1. Solid curves are generated by using DGA to estimate $r^$, $\gamma^$, and ${k^_{on}^{R}}$ and using this as input to exact analytical formulas. (b) Comparison between the inferred values of $\frac{r^}{\gamma^}$ using DGA with experimentally measured values of this parameter from Jones et al., 2014. (c) Inferred $k^_{on}^{R}$ values as a function of the mean mRNA level.

As expected, the repressor binding rates decrease with the mean mRNA level (see Figure 7c). The broad range of repressor binding rates shows that the system can adjust its sensitivity to repressor concentration, allowing for both tight repression and rapid activation depending on the cellular context.

Figure 7a shows a comparison between the predictions of the DGA (solid curves) and the experimental data (squares) for mean mRNA levels and the Fano factor . The theoretical curves are obtained by using analytical expression for and from Gillespie, 2007 with parameters estimated from the DGA. We find that for the lacUD5 and the 5DL1 promoters, the mean percentage errors for predictions of the Fano factor are 25% and 28%, respectively (see Appendix 6).

An appealing feature of Jones et al., 2014 is that the authors performed independent experiments to directly measure the normalized transcription rate $r/\gamma$ (namely the ratio of the transcription rate and the mRNA degradation rate). This allows us to compare the DGA predictions for these parameters to ground truth measurements of kinetic parameters. In Figure 7b, the predictions of the DGA agree remarkably well for both the lacUD5 and 5DL1 promoters.

### Designing gene regulatory circuits with desired behaviors

Another interesting application of the DGA is to design stochastic chemical or biological networks that exhibit a particular behavior. In many cases, this design problem can be reformulated as identifying choices of parameter that give rise to a desired behavior. Here, we show that the DGA is ideally suited for such a task. We focus on designing the input–output relation of a four state promoter model of gene regulation (Lammers et al., 2023). We have chosen this more complex promoter architecture because, unlike the two-state promoter model analyzed above, it allows for nonequilibrium currents. In making this choice, we are inspired by numerous recent works have investigated how cells can tune kinetic parameters to operate out of equilibrium in order to achieve increased sharpness/sensitivity (Nicholson and Gingrich, 2023Lammers et al., 2023; Zoller et al., 2022; Wong and Gunawardena, 2020; Dixit et al., 2024).

### Model of nonequilibrium promoter

We focus on designing the steady-state input–output relationship of the four-state promoter model of gene regulation model shown in Figure 8a; Lammers et al., 2023. The locus can be in either an ‘ON’ state where mRNA is transcribed at a rate $r$ or an ‘OFF’ state where the locus is closed and there is no transcription. In addition, a transcription factor (assumed to be an activator) with concentration $[c]$ can bind to the locus with a concentration dependent rate $[c]k_{b}$ in the ‘OFF’ state and a rate $[c]η_{ba}k_{b}$ in the ‘ON’ rate. The activator can also unbind at a rate $k_{u}$ in the ‘OFF’ state and a rate $η_{ua}k_{u}$ in the ‘ON’ state. The average mRNA production rate (averaged over many samples) in this model is given by

$$
⟨r¯⟩=r(\pi_{2}+\pi_{3})
$$

where $\pi_{s}$ ($s=2,3$) is the steady-state probability of finding the system in each of the ‘ON’ states (see Figure 8a).

![Figure 8.](https://cdn.elifesciences.org/articles/103877/elife-103877-fig8-v1.jpg)

**Figure 8.:** (a) Schematic of four-state promoter model. (b) Target input–output relationships (solid curves) and learned input–output relationships (blue dots) between activator concentration $[c]$ and average mRNA production rate. (c) Parameters learned by DGA for the two responses in (b). (d) The sharpness of the response $\frac{d⟨r¯⟩}{d[c]}[c]$, and the energy dissipated per unit time for two responses in (b). (e) Logarithm of the loss function for the learned parameter set for Response-2, revealing directions (or curves) of insensitivity in the model’s parameter space. The red circles are the learned parameter values.

Such promoter architectures are often studied in the context of protein gradient-based development (Lammers et al., 2023; Estrada et al., 2016; Owen and Horowitz, 2023). One well-known example of such a gradient is the dorsal protein gradient in Drosophila, which plays a crucial role in determining the spatial boundaries of gene expression domains during early embryonic development. In this context, the sharpness of the response as a function of activator concentration is a critical aspect. High sharpness ensures that the transition between different gene expression domains occurs over a very narrow region, leading to well-defined and precise boundaries. Inspired by this, our objective is to determine the parameters such that the variation in $⟨r¯⟩$ as a function of the activator concentration $[c]$ follows a desired response. We consider the two target responses (shown in Figure 8b) of differing sharpness, which following Lammers et al., 2023 we quantify as $max(\frac{∂⟨r¯⟩}{∂[c]}[c])$. For simplicity, we use sixth-degree polynomials to model the input–output functions, with the x-axis plotted on a logarithmic scale. We note that our results do not depend on this choice and any other functional form works equally well.

### Loss function

In order to use the DGA to learn a desired input–output relation, we must specify a loss function that quantifies the discrepancy between the desired and actual responses of the promoter network. To construct such a loss function, we begin by discretizing the activator concentration into $N=10$ logarithmically spaced points, $[c]_{i}$, where $i=1,2,…,N$. For each $[c]_{i}$, we denote the corresponding average mRNA production rate $⟨r¯⟩_{i}$ (see Equation 15). After discretization, the loss function is simply the square error between the desired response, $⟨r¯⟩_{i}$, and the current response, $⟨r¯^(\theta)⟩_{i}$, of the circuit

$$
L=\sumi=1N(⟨r¯^(\theta)⟩_{i}−⟨r¯⟩_{i})^{2},
$$

where $⟨r¯^(\theta)⟩_{i}$ denotes the predicted average mRNA production rates obtained from the DGA simulations given the current parameters $\theta$. To compute $⟨r¯^⟩_{i}$ for a concentration $[c]_{i}$, we perform $n=600$ DGA simulations (indexed by capital letters $A=1,…,n$) using the DGA and use these simulations to calculate the fraction of time spent in transcriptionally active states (states $s=2$ and $s=3$ in Figure 8a). If we denote the fraction of time spent in state $s$ in simulation $A$ by $w_{s}^{A}$, then we can calculate the probability $\pi_{s}$ of being in state $s$ by

$$
\pi_{s}=\frac{1}{n}\sumA=1nw_{s}^{A}
$$

and use Equation 15 to calculate $⟨r¯^(\theta)⟩_{i}$

As before, we optimize this loss using gradient descent (see Figure 2). We assume that the transcription rate $r$ is known (this just corresponds to an overall scaling of mRNA numbers). Since we are concerned only with steady-state properties, we fix the activator binding rate to a constant value, $k_{b}=0.02$. This is equivalent to measuring time in units of $k_{b}^{−1}$. We then use gradient descent to optimize the remaining seven parameters governing transitions between promoter states.

### Assessing circuits found by the DGA

Figure 8b shows a comparison between the desired and learned input–output relations. This is good agreement between the learned and desired responses, showing that the DGA is able to design dose–response curves with different sensitivities and maximal values. Figure 8c shows the learned parameters for both response curves. Notably, the degree of activation resulting from transcription factor binding, denoted by $η_{ab}$, is substantially higher for the sharper response (Response-2). In contrast, the influence on transcription factor binding due to activation, represented by $η_{ba}$, is reduced for the sharper response curve. Additionally, the unbinding rate $k_{u}$ is observed to be lower for the sharper response. However, it is essential to approach these findings with caution, as the parameters are highly interdependent. These interdependencies can be visualized by plotting the loss function around the optimized parameter values. Figure 8e shows two dimensional heat maps of the loss function for Response-2. There are seven free parameters, resulting in a total of 21 possible 2D slices of the loss function within the seven-dimensional loss landscape.

The most striking feature of these plots is the central role played by the parameters $η_{ab}$ and $η_{ua}$ which must both be high, suggesting that the sharpness in Response-2 may result from creating a high-flux nonequilibrium cycle through the four promoter states (see Figure 8a). This observation is consistent with recent works suggesting that creating such nonequilibrium kinetics represents a general design principle for engineering sharp responses (Lammers et al., 2023; Zoller et al., 2022; Wong and Gunawardena, 2020; Dixit et al., 2024). To better understand if this is indeed what is happening, we quantified the energy dissipation per unit time (power consumption), $Φ$, in the nonequilibrium circuit. The energetic cost of operating biochemical networks can be quantified using ideas from nonequilibrium thermodynamics using a generalized Ohm’s law of the form (Lammers et al., 2023; Qian, 2007; Mehta and Schwab, 2012; Lan et al., 2012; Lang et al., 2014; Mehta et al., 2016)

$$
Φ=JΔ\mu
$$

where we have defined a nonequilibrium drive

$$
Δ\mu=ln⁡(\frac{η_{ab}η_{ua}}{η_{ib}η_{ba}})
$$

and the nonequilibrium flux

$$
J=\pi_{0}k_{b}[c]−\pi_{1}k_{u},
$$

where $\pi_{0}$ and $\pi_{1}$ are the probabilities of finding the system in state 0 and 1, respectively. Figure 8d shows a comparison between energy consumption and sharpness of the two learned circuits. Consistent with the results of Lammers et al., 2023, we find that the sharper response curve is achieved by consuming more energy.

## Discussion

In this paper, we introduced a fully differentiable variant of the Gillespie algorithm, the DGA. By integrating differentiable components into the traditional Gillespie algorithm, the DGA facilitates the use of gradient-based optimization techniques, such as gradient descent, for parameter estimation and network design. The ability to smoothly approximate the discrete operations of the traditional Gillespie algorithm with continuous functions facilitates the computation of gradients via both forward- and reverse-mode automatic differentiation, foundational techniques in machine learning, and has the potential to significantly expand the utility of stochastic simulations. Our work demonstrates the efficacy of the DGA through various applications, including parameter learning and the design of simple gene regulatory networks.

We benchmarked the DGA’s ability to accurately replicate the results of the exact Gillespie algorithm through simulations on a two-state promoter architecture. We found the DGA could accurately approximate the moments of the steady-state distribution and other major qualitative features. Unsurprisingly, it was less accurate at capturing information about the tails of distributions. We then demonstrated that the DGA could be accurately used for parameter estimation on both simulated and real experimental data. This capability to infer kinetic parameters from noisy experimental data underscores the robustness of the DGA, making it a potentially powerful computation tool for real-world applications in quantitative biology. Furthermore, we showcased the DGA’s application in designing biological networks. Specifically, for a complex four-state promoter architecture, we learned parameters that enable the gene regulation network to produce desired input–output relationships. This demonstrates how the DGA can be used to rapidly design complex biological systems with specific behaviors. We expect computational design of synthetic circuits with differentiable simulations to become an increasingly important tool in synthetic biology.

There remains much work still to be done. In this paper, we focused almost entirely on properties of the steady states. However, a powerful aspect of the traditional Gillespie algorithm is that it can be used to simulate dynamical trajectories. How to adopt the DGA to utilize dynamical data remains an extremely important open question. In addition, it will be interesting to see if the DGA can be adapted to understand the kinetic of rare events. It will also be interesting to compare the DGA with other recently developed approximation methods such as those based on tensor networks (Strand et al., 2022; Nicholson and Gingrich, 2023). Beyond the gene regulatory networks, extending the DGA to handle larger and more diverse datasets will be crucial for applications in epidemiology, evolution, ecology, and neuroscience. On a technical level, this may be facilitated by developing more sophisticated smoothing functions and adaptive algorithms to improve numerical stability and convergence.

The DGA could also be extended to stochastic spatial systems by incorporating reaction–diffusion master equations or lattice-based models. Its differentiability may enable efficient optimization of spatially heterogeneous reaction parameters. However, such extensions may need to address computational scalability and stability in high-dimensional spaces, especially in processes such as diffusion-driven pattern formation or spatial gene regulation.

## Materials and methods

A detailed explanation of how the DGA is implemented using PyTorch is given in the Appendix. In addition, all code for the DGA is available on Github at our Github repository https://github.com/Emergent-Behaviors-in-Biology/Differentiable-Gillespie-Algorithm (copy archived at Rijal, 2025).
