# Peer review - Round 1

Editors:
- Jeffrey C Smith, National Institute of Neurological Disorders and Stroke United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.105842.4.sa0](https://doi.org/10.7554/eLife.105842.4.sa0)

This important computational study investigates homeostatic plasticity mechanisms that neurons may employ to achieve and maintain stable target activity patterns. The work extends previous analyses of calcium-dependent homeostatic mechanisms based on ion channel density by considering activity-dependent shifts in channel activation and inactivation properties that operate on faster and potentially variable timescales. The model simulations convincingly demonstrate the potential functional importance of these mechanisms.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.105842.4.sa1](https://doi.org/10.7554/eLife.105842.4.sa1)

This revision of the computational study by Mondal et al addresses several issues that I raised in the previous round of reviews and, as such, is greatly improved. The manuscript is more readable, its findings are more clearly described, and both the introduction and the discussion sections are tighter and more to the point. And thank you for addressing the three timescales of half activation/inactivation parameters. It makes the mechanism clearer.

Some issues remain that I bring up below.

Comment:

I still have a bone to pick with the claim that "activity-dependent changes in channel voltage-dependence alone are insufficient to attain bursting". As I mentioned in my previous comment, this is also the case for the gmax values (channel density). If you choose the gmax's to be in a reasonable range, then the statement above is simply cannot be true. And if, in contrast, you choose the activation/inactivation parameters to be unreasonable, then no set of gmax's can produce proper activity. So I remain baffled what exactly is the point that the authors are trying to make.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.105842.4.sa2](https://doi.org/10.7554/eLife.105842.4.sa2)

Summary:

In this study, Mondal and co-authors present the development of a computational model of homeostatic plasticity incorporating activity-dependent regulation of gating properties (activation, inactivation) of ion channels. The authors show that, similar to what has been observed for activity-dependent regulation of ion channel conductances, implementing activity-dependent regulation of voltage sensitivity participates in the achievement of a target phenotype (bursting or spiking). The results however suggest that activity-dependent regulation of voltage sensitivity is not sufficient to allow this and needs to be associated with the regulation of ion channel conductances in order to reliably reach target phenotype. Although the implementation of this biologically relevant phenomenon is undeniably relevant, a few important questions are left unanswered.

Strengths:

(1) Implementing activity-dependent regulation of gating properties of ion channels is biologically relevant.

(2) The modeling work appears to be well performed and provides results that are consistent with previous work performed by the same group.

Weaknesses:

(1) The main question not addressed in the paper is the relative efficiency and/or participation of voltage-dependence regulation compared to channel conductance in achieving the expected pattern of activity. Is voltage-dependence participating to 50% or 10%. Although this is a difficult question to answer (and it might even be difficult to provide a number), it is important to determine whether channel conductance regulation remains the main parameter allowing the achievement of a precise pattern of activity (or its recovery after perturbation).

(2) Another related question is whether the speed of recovery is significantly modified by implementing voltage-dependence regulation (it seems to be the case looking at Figure 3). More generally, I believe it would be important to give insights into the overall benefit of implementing voltage-dependence regulation, beyond its rather obvious biological relevance.

(3) Along the same line, the conclusion about how voltage-dependence regulation and channel conductance regulation interact to provide the neuron with the expected activity pattern (summarized and illustrated in Figure 6) is rather qualitative. Consistent with my previous comments, one would expect some quantitative answers to this question, rather than an illustration that approximately places a solution in parameter space.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.105842.4.sa3](https://doi.org/10.7554/eLife.105842.4.sa3)

Mondal et al. use computational modeling to investigate how activity-dependent shifts in voltage-dependent (in)activation curves can complement changes in ion channel conductance to support homeostatic plasticity. While it is well established that the voltage-dependent properties of ion channels influence neuronal excitability, their potential role in homeostatic regulation, alongside conductance changes, has remained largely unexplored. The results presented here demonstrate that activity-dependent regulation of voltage dependence can interact with conductance plasticity to enable neurons to attain and maintain target activity patterns, in this case, intrinsic bursting. Notably, the timescale of these voltage-dependent shifts influences the final steady-state configuration of the model, shaping both channel parameters and activity features such as burst period and duration. A major conclusion of the study is that altering this timescale can seamlessly modulate a neuron's intrinsic properties, which the authors suggest may be a mechanism for adaptation to perturbations.

While this conclusion is largely well-supported, additional analyses could help clarify its scope. For instance, the effects of timescale alterations are clearly demonstrated when the model transitions from an initial state that does not meet the target activity pattern to a new stable state. However, Fig. 6 and the accompanying discussion appear to suggest that changing the timescale alone is sufficient to shift neuronal activity more generally. It would be helpful to clarify that this effect primarily applies during periods of adaptation, such as neurodevelopment or in response to perturbations, and not necessarily once the system has reached a stable, steady state. As currently presented, the simulations do not test whether modifying the timescale can influence activity after the model has stabilized. In such conditions, changes in timescale are unlikely to affect network dynamics unless they somehow alter the stability of the solution, which is not shown here. That said, it seems plausible that real neurons experience ongoing small perturbations which, in conjunction with changes in timescale, could allow gradual shifts toward new solutions. This possibility is not discussed but could be a fruitful direction for future work.

Editor's note: The authors have adequately addressed the concerns raised in the public reviews above, as well as the previous recommendations, and revised the manuscript where necessary.
