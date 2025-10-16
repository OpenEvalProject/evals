# Peer review - Round 1

Editors:
- Anne-Florence Bitbol, Ecole Polytechnique Federale de Lausanne (EPFL) Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.103877.3.sa0](https://doi.org/10.7554/eLife.103877.3.sa0)

This important study introduces a fully differentiable variant of the Gillespie algorithm as an approximate stochastic simulation scheme for complex chemical reaction networks, allowing kinetic parameters to be inferred from empirical measurements of network outputs using gradient descent. The concept and algorithm design are convincing and innovative. While the proofs of concept are promising, some questions are left open about implications for more complex systems that cannot be addressed by existing methods. This work has the potential to be of significant interest to a broad audience of quantitative and synthetic biologists.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.103877.3.sa1](https://doi.org/10.7554/eLife.103877.3.sa1)

Summary:

This work introduces the differentiable Gillespie algorithm, DGA, which is a differentiable variant of the celebrated (and exact) Gillespie algorithm commonly used to perform stochastic simulations across numerous fields, notably in the life sciences. The proposed DGA approximates the exact Gillespie algorithm using smooth functions yielding a suitable approximate differentiable stochastic system as a proxy for the underlying discrete stochastic system, where DGA stochastic reactions have continuous reaction index and the species abundances. To illustrate their methodology, the authors specifically consider in detail the case of a well-studied two-state promoter gene regulation system that they analyze using a machine learning approach, and by combining simulation data with analytical results. For the two-state promoter gene system, the DGA is benchmarked by accurately reproducing the results of the exact Gillespie algorithm. For this same simple system, the authors also show how the DGA can be used for estimating kinetic parameters of both simulated and real noisy experimental data. This lets them argue convincingly that the DGA can become a powerful computation tool for applications in quantitative and synthetic biology. In order to argue that the DGA can be employed to design circuits with ad-hoc input-output relations, these considerations are then extended to a more complex four-state promoter model of gene regulation. The main strength of the paper is its clarity and its pedagogical presentation of the simulation methods.

Strengths:

The main strength of the paper is its clarity and its pedagogical presentation of the simulation methods.

Weaknesses:

It would have been useful to have a brief discussion, based on a concrete example, of what can be achieved with the DGA and is totally beyond the reach of the Gillespie algorithm and the numerous existing stochastic simulation methods. A more comprehensive and quantitative analysis of the limitations of the DGA, e.g. for rare events, and how it might be used for stochastic spatial systems would have also been helpful. However, this is arguably beyond the scope of this study whose primary goal is to introduce the DGA and demonstrate that it can achieve tasks like parameter estimation and network design.

Comments on revisions:

The authors have made a sound effort to address many of the comments raised in the previous reports. This has helped improve the clarity of the discussion.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.103877.3.sa2](https://doi.org/10.7554/eLife.103877.3.sa2)

Summary:

In this work, the authors present a differentiable version of the widely-used Gillespie Algorithm. The Gillespie Algorithm has been used for decades to simulate the behavior of stochastic biochemical reaction networks. But while the Gillespie Algorithm is a powerful tool for the forward simulation of biochemical systems given some set of known reaction parameters, it cannot be used for reverse process, i.e. inferring reaction parameters given a set of measured system characteristics. The Differentiable Gillespie Algorithm ("DGA") overcomes this limitation by approximating two discontinuous steps in the Gillespie Algorithm with continuous functions. This makes it possible to calculate of gradients for each step in the simulation process which, in turn, allows the reaction parameters to be optimized via powerful backpropagation techniques. In addition to describing the theoretical underpinnings of DGA, the authors demonstrate different potential use-cases for the algorithm in the context of simple models of stochastic gene expression.

Overall, the DGA represents an important conceptual step forward for the field and should lay the groundwork for exciting innovations in the analysis and design of stochastic reaction networks. At the same time, significantly more work is needed to establish when the approximations made by DGA are valid and to demonstrate the viability of the algorithm in the context of complicated reaction networks.

Strengths:

This work makes an important conceptual leap by introducing a version of the Gillespie Algorithm that is end-to-end differentiable. This idea alone has the potential to drive a number of exciting innovations in the analysis, inference, and design of biochemical reaction networks. Beyond the theoretical adjustments, the authors also implement their algorithm in a Python-based codebase that combines DGA powerful optimization libraries like PyTorch. This codebase has the potential to be of interest to a wide range of researchers, even if the true scope of the method's applicability remains to be fully determined.

The authors also demonstrate how DGA can be used in practice both to infer reaction parameters from real experimental data (Figure 7) and to design networks with user-specified input-output characteristics (Figure 8). These illustrations should provide a nice roadmap for researchers interested in applying DGA to their own projects/systems.

Finally, although it does not stem directly from DGA, the exploration of pairwise parameter dependencies in different network architectures provides an interesting window into the design constraints (or lack thereof) that shape the architecture of biochemical reaction networks.

Weaknesses:

While it is clear that the DGA represents an important conceptual advancement, the authors do not do enough in the present manuscript to (i) validate the robustness of DGA inference and (ii) demonstrate that DGA inference works in the kinds of complex biochemical networks where it would actually be of legitimate use.

It is to the authors' credit that they are open and explicit about the potential limitations of DGA due to breakdowns in its continuous approximations. However they do not provide the reader with nearly enough empirical (i.e. simulation-based) or theoretical context to assess when, why, and to what extent DGA will fail in different situations. In Figure 2, they compare DGA to GA (i.e. ground-truth) in the context of a simple two state model of a stochastic transcription. Even in this minimal system, we see that DGA deviates notably from ground-truth both in the simulated mRNA distributions (Figure 2A) and in the ON/OFF state occupancy (Figure 2C). This begs the question of how DGA will scale to more complicated systems, or systems with non-steady state dynamics. Will the deviations become more severe? This is important because, in practice, there is really not much need for using DGA with a simple 2 state system-we have analytic solutions for this case. It is the more complex systems where DGA has the potential to move the needle.

A second concern is that the authors' present approach for parameter inference and error calculation does not seem to be reliable. For example, in Figure 5A, they show DGA inference results for the ON rate of a two-state system. We see substantial inference errors in this case, even though the inference problem should be non-degenerate in this case. One reason for this seems to be that the inference algorithm does not reliably find the global minimum of the loss function (Figure 2B). To turn DGA into a viable approach, it is paramount that the authors find some way to improve this behavior, perhaps by using multiple random initializations to better search the loss space.

Finally, the authors do a good job of illustrating how DGA might be used to infer biological parameters (Figure 7) and design reaction networks with desired input-output characteristics (Figure 8). However, analytic solutions exist for both of the systems they select for examples. This means that, in practice, there would be no need for DGA in these contexts, since one could directly optimize, e.g., the expressions for the mean and Fano Factor of the system in Figure 7A. I still believe that it is useful to have these examples, but it seems critical to add a use-case where DGA is the only option.

Comments on revisions:

I am concerned that the results in Figure 8D may not be correct, or that the authors may be mis-interpreting them. From my reading of the paper they cite (Lammers & Flamholz 2023), the equilibrium sharpness limit for the network they consider in Figure 8 should be 0.25. But both solutions shown in Figure 8D fall below this limit, which means that they have sharpness levels that could have been achieved with no energy expenditure. If this is the case, then it would imply that while both systems do dissipate energy, they are not doing so productively; meaning that the same results could be achieved while holding Phi=0.

I acknowledge that this could be due to a difference in how they measure sharpness, but wanted to raise it here in case it is, in fact, a genuine issue with the analysis.

There should be an easy fix for this: just set the sharper "desired response" curve in 8b to be such that it demands non-equilibrium sharpness levels (0.25)


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.103877.3.sa3](https://doi.org/10.7554/eLife.103877.3.sa3)

Summary:

This manuscript introduces a differentiable variant of the Gillespie algorithm (DGA) that allows gradient calculation using backpropagation. The most significant contribution of this work is the development of the DGA itself, a novel approach to making stochastic simulations differentiable. This is achieved by replacing discontinuous operations in the traditional Gillespie algorithm with smooth, differentiable approximations using sigmoid and Gaussian functions. This conceptual advance opens up new avenues for applying powerful gradient-based optimization techniques, prevalent in machine learning, to studying stochastic biological systems.

The method was tested on a simple two-state promoter model of gene expression. The authors found that the DGA accurately captured the moments of the steady-state distribution and other major qualitative features. However, it was less accurate at capturing information about the distribution's tails, potentially because rare events result from frequent low-probability reaction events where the approximations made by the DGA have a greater impact. The authors also used the DGA to design a four-state promoter model of gene regulation that exhibited a desired input-output relationship. The DGA could learn parameters that produced a sharper response curve, which was achieved by consuming more energy.

The authors conclude that the DGA is a powerful tool for analyzing and designing stochastic systems. The discussion lays several open questions in the field and constructively addresses shortcomings of the proposed method as well as potential ways forward.

Strengths:

The DGA allows gradient-based optimization techniques to estimate parameters and design networks with desired properties.

The DGA efficacy in estimating kinetic parameters from both synthetic and experimental data. This capability highlights the DGA's potential to extract meaningful biophysical parameters from noisy biological data.

The DGA's ability to design a four-state promoter architecture exhibits a desired input-output relationship. This success indicates the potential of the DGA as a valuable tool for synthetic biology, enabling researchers to engineer biological circuits with predefined behaviours.

Weaknesses:

The study primarily focuses on analysing the steady-state properties of stochastic systems.

Comments on revisions:

Thank you for addressing all the points raised. I am looking forward to seeing the next steps in DGAs development and performance!
