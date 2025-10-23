# Peer review - Round 1

Editors:
- Fred Rieke, University of Washington United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.99808.4.sa0](https://doi.org/10.7554/eLife.99808.4.sa0)

This paper explores how diverse forms of inhibition impact firing rates in models for cortical circuits. In particular, the paper studies how the network operating point affects the balance of direct inhibition from SOM inhibitory neurons to pyramidal cells, and disinhibition from SOM inhibitory input to PV inhibitory neurons. This is an important issue as these two inhibitory pathways have largely been studied in isolation. A combination of analytical calculations and direct numerical simulations provides convincing evidence that the interplay of these inhibitory circuits can separately control network gain and stability.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.99808.4.sa1](https://doi.org/10.7554/eLife.99808.4.sa1)

Summary:

This paper explores how diverse forms of inhibition impact firing rates in models for cortical circuits. In particular, the paper studies how the network operating point affects the balance of direct inhibition from SOM inhibitory neurons to pyramidal cells, and disinhibition from SOM inhibitory input to PV inhibitory neurons. This is an important issue as these two inhibitory pathways have largely been studies in isolation. A combination of analytical calculations and direct numerical simulations provide convincing evidence that the interplay of these inhibitory circuits can separately control network gain and stability.

Strengths

The paper has improved in revision, and the intuitive summary statements added to the end of each results section are quite helpful. The addition of numerical simulations to extend the conclusions beyond the linear range of network behavior are also quite helpful.

Weaknesses

None


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.99808.4.sa2](https://doi.org/10.7554/eLife.99808.4.sa2)

Summary:

Bos and colleagues address the important question of how two major inhibitory interneuron classes in the neocortex differentially affect cortical dynamics. They address this question by studying Wilson-Cowan-type mathematical models. Using a linearized fixed point approach, and subsequent simulations of neural circuits operating in the dynamic stochastically-driven regime, they provide compelling evidence that the existence of multiple interneuron classes can explain the counterintuitive finding that inhibitory modulation can increase the gain of the excitatory cell population while also increasing the stability of the circuit's state to minor perturbations. This effect depends on the connection strengths within their circuit model, providing important guidance as to when and why it arises.

Overall, I find this study to have substantial merit. The authors have also done a commendable job of revising the paper in light of the critiques raised by myself and the other reviewers.

Strengths:

(1) The thorough investigation of how changes in the connectivity structure affect the gain-stability relationship is a major strength of this work. It provides an opportunity to understand when and why gain and stability will or will not both increase together. It also provides a nice bridge to the experimental literature, where different gain-stability relationships are reported from different studies.

(2) The simplified and abstracted mathematical model has the benefit of facilitating our understanding of this puzzling phenomenon. It is not easy to find the right balance between biologically-detailed models vs simple but mathematically tractable ones, and I think the authors struck an excellent balance in this study.

(3) While the fixed-point analysis has potentially substantial limitations for understanding cortical computations away from the steady-state, the authors used simulations to verify that their main findings hold in the stochastically-driven regime that more closely reflects the dynamics observed in in vivo neuroscience experiments.

Weaknesses:

(1) As the authors note in their Discussion, it would be worthwhile to study this effect in chaotic and/or oscillatory regimes, in addition to the ones they included here. I agree with their assessment that those investigations should be left for a future study.

(2) The analysis is limited to paths within this simple E,PV,SOM circuit. This misses more extended paths (like thalamocortical loops) that involve interactions between multiple brain areas. Including those paths in the expansion in Eqs. 11-14 (Fig. 1C) may be an important direction for future work.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.99808.4.sa3](https://doi.org/10.7554/eLife.99808.4.sa3)

Summary:

Bos et al study a computational model of cortical circuits with excitatory (E) and two subtypes of inhibition - parvalbumin (PV) and somatostatin (SOM) expressing interneurons. They perform stability and gain analysis of simplified models with nonlinear transfer functions when SOM neurons are perturbed. Their analysis suggests that in a specific setup of connectivity, instability and gain can be untangled, such that SOM modulation leads to both increase in stability and gain, in contrast to the typical direction in neuronal networks where increased gain results in decreased stability.

Strengths:

- Analysis of the canonical circuit in response to SOM perturbations. Through numerical simulations and mathematical analysis, the authors have provided a rather comprehensive picture of how SOM modulation may affect response changes.

- Shedding light on two opposing circuit motifs involved in the canonical E-PV-SOM circuitry - namely, direct inhibition (SOM -> E) vs disinhibition (SOM -> PV -> E). These two pathways can lead to opposing effects, and it is often difficult to predict which one results from modulating SOM neurons. In simplified circuits, the authors show how these two motifs can emerge and depend on parameters like connection weights.

- Suggesting potentially interesting consequences for cortical computation. The authors suggest that certain regimes of connectivity may lead to untangling of stability and gain, such that increases in network gain are not compromised by decreasing stability. They also link SOM modulation in different connectivity regimes to versatile computations in visual processing in simple models.

Weaknesses:

- Computationally, the analysis is solid, but it's very similar to previous studies (del Molino et al, 2017). Many studies in the past few years have done the perturbation analysis of a similar circuitry with or without nonlinear transfer functions (some of them listed in the references). This study applies the same framework to SOM perturbations, which is a useful computational analysis, in view of the complexity of the high-dimensional parameter space.

- A general weakness of the paper is a lack of direct comparison to biological parameters or experiments. How different experiments can be reconciled by the results obtained here, and what new circuit mechanisms can be revealed? In its current form, the paper reads as a general suggestion that different combinations of gain modulation and stability can be achieved in a circuit model equipped with many parameters (12 parameters). This is potentially interesting but not surprising, given the high dimensional space of possible dynamical properties. A more interesting result would have been to relate this to biology, by providing reasoning why it might be relevant to certain circuits (and not others), or to provide some predictions or postdictions, which are currently not very strong in the manuscript.

- Tuning curves are simulated for an individual orientation (same for all neurons), not considering the heterogeneity of neuronal networks with multiple orientation selectivity (and other visual features) - making the model too simplistic.
