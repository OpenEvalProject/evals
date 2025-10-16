# Peer review - Round 1

Editors:
- Martin Vinck, https://ror.org/01hhn8329 Ernst Strüngmann Institute (ESI) for Neuroscience in Cooperation with Max Planck Society Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77594.sa0](https://doi.org/10.7554/eLife.77594.sa0)

The microcircuit has a canonical composition and the interactions among distinct classes of excitatory and GABAergic neurons are fundamental to our understanding of sensory processing and neuronal synchronization. The authors investigate emerging dynamics in laminar models of the visual cortex, consisting of distinct GABAergic cell types, with a connectivity model based on the latest anatomical findings. The authors identify bistable circuit switches emerging from the interactions between different cell types and these are characterized by inhibited and disinhibited states accompanied by low- and high-frequency oscillations, respectively. These findings suggest a canonical, non-linear circuit motif that can explain multiple experimental observations and adds significantly to our understanding of microcircuit dynamics.


---

# Peer review - Round 1

Editors:
- Martin Vinck, https://ror.org/01hhn8329 Ernst Strüngmann Institute (ESI) for Neuroscience in Cooperation with Max Planck Society Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77594.sa1](https://doi.org/10.7554/eLife.77594.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review. Please note the reviewers have opted to remain anonymous. ]

Thank you for submitting your work entitled "Computational Properties of the Visual Microcircuit" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Thilo Womelsdorf (Reviewer #2).

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife. Although the reviewers expressed interest in the study, with some mixed enthusiasm, major issues were identified. Reviewers agreed that these preclude publication in eLife at present and would require a substantial amount of additional work to improve the manuscript. The main issues identified were the lack of input layers in the model, the dynamics of different neuron types and their impact on the system, and the idealization of the circuit as a single column. If you are able to address these points and the other points raised by the reviewers, eLife would welcome re-submission of this paper: This would be treated as a new submission, but would likely go to the same reviewers if it were to be sent out for review.

Reviewer #1:

In this study, the authors build a microcircuit of mouse primary visual cortex using connectivity data between four cell types (PV, SSt, Pyr, VIP) in two laminar compartments (superficial and deep). The authors then examine the influence of (1) Global increase in coupling (G), and (2) Specific drive to particular neurons. This basic microcircuit appears to capture some basic features of physiology, namely: (1) Increased high-frequency power in superficial layers and increased low-frequency power in deep layers (Figure 1), (2) Enhanced firing rates in deep layers. The main finding of the authors is that when they enhance drive to the VIP cells, there is a steep transition in the firing of SST cells, which they characterize as a bi-stable system. Overall, this study has merit in providing a quite extensive characterization of a canonical microcircuit, and the authors do a great job in linking their manipulations to experimental findings.

Concerns:

1) The authors describe the effect of driving VIP interneurons as disinhibitory. I'm confused. Figure 3 shows that the effect of driving VIP interneurons in pyramidal firing rates in superficial layers is largely suppressive, which seems to go against their main conclusion and experimental findings.

2) Noisy oscillations should be better defined. Are these noisy limit cycles or quasi oscillations?

3) The model provided by the authors has a stochastic drive and therefore exhibits noisy oscillations. It should be discussed whether similar results would have been obtained when using stochastic Wilson-Cowan models where each population consists of multiple neurons and the neurons have spiking output.

4) A limitation of the study is that Layer 4 is not modelled, and that the application of external drive appears somewhat arbitrary. In reality the external drive on PV and Pyramidal cells will likely be matched/balanced to some extent. However, Figure 5 applies a constant input to either PV or VIP cells which does not seem a realistic assumption. It would be hard to make reasonable assumptions on how the input drive to VIP cells looks like.

5) Related to this, the authors identify that the bi-stable switch appears to emerge in a particular regime of G. However, do we have any idea what the value of "G" in an actual circuit would be? Furthermore, should one not examine how the strength of external drive modulates the ability of the circuit to switch?

6) A very relevant study, Di Poppa et al. by Ken Harris lab, is only marginally discussed in this paper. However, that paper also provided a model of interactions between these cell classes and reports many findings on disinhibition and covariation between the cell types.

7) The authors should stress that this is a model of the MOUSE primary visual cortex. We know that the monkey visual cortex has quite different properties in terms of cell types, connectivity, lamination etc. It's unclear whether the mouse work bears any relevance for the monkey. The authors mix references to mice and monkey studies, but this should be made clear at all point. For instance, γ oscillations in monkeys have quite different signatures from the mouse in terms of frequencies. We can't really compare those in a straightforward way.

8) The study relies on the octo-patch data. However, that dataset was criticized quite severely in a commentary. Can references be made to other studies e.g. from Scanziani confirming some of these connectivity patterns?

Reviewer #2:

This is an excellent, innovative, well written and comprehensive modeling study. The paper is made possible with detailed anatomical data that is only available recently about connectivity matrices and cell type distributions across layers. The study systematically shows how drive to VIP (feedback type) and PV (feedforward type) cell modulate a SST cell dependent inhibited and a PV dependent disinhibited state. The study mechanistically tracks down the source for the two separable states asymmetric self-inhibition and show how state transitions can be induced ('toggled'). The paper provides strong quantifiable predictions which is attractive for empirical people.

A weakness is that many assumptions are implicit and key findings are difficult to find in the large amount of data.

1. It is difficult to get a good understanding which G values are realistic for invite states and what they mean. There is a rate and power change for G of < 100 (Figure 1), but then various interesting effects are occurring at G >200 (effects of cell silencing).

What are the underling characteristics / mechanisms that determine g changes, i.e. changes in effective coupling strength? describing this more explicitly early in the results would enhance comprehensibility

2. The presentation of the key contributions of SOM and PV is ideally improved. Going through Figure 2 is highly interesting but time consuming because the many panels make this a dense figure. Can the two key results of the effects of PV silencing and SOM silencing be shown as a power vs frequency plot – identical to Figure 2C and D. So far, we only see the peak frequencies across G but this does not easily allow to appreciate the power spectral shape at a low (e.g. 50) or high (e.g. 450) G. In its current form it is not possible to confirm how wide the power spectral density peaks are.

3. The results are describing average effects and are surprisingly non-quantitative. There is not a single statistic used and error bars are lacking. While this seems justified in many cases it leaves the impression that there is no noise in the results and that they would be perfectly reproducible and robust across may conditions. How realistic is this and what would change if realistic noise is introduced?

When the authors address this question, it would be important to see an explicit definition of what a 'state' refers to. The paper describes many simulations where inputs are switched on constantly and with no apparent fluctuations. Is that realistically happening in real feedforward /feedbacK signal dynamics?

Reviewer #3:

Using a Wilson-Cowen model, the authors look at the coupling between 8 neuronal populations (excitatory + 3 inhibitory) based on experimental connectivity of the L2/3 and L5 populations. They do a very thorough analysis of the oscillatory properties of this system under a set of assumptions. Even though they do not address computations directly, the results are interesting, and link to several hypotheses in the field on the generation of oscillatory behavior. However, I am not convinced that following the choices of parameters and approximations the model is a useful approximation of the biological circuit. I believe the authors need to do considerably more work to justify the choices of parameters and the implicit approximations used (or that they are irrelevant for the behaviours described).

Simplified models which abstract away a lot of the details are needed for theoretical understanding in neuroscience. However, arguments need to be made that the simplified model still maintains relevance for the system studied.

1. While the experimental results for connectivity included in the model are very detailed, they are not a complete description of the microcircuit. Most importantly, they lack a L4, which is the primary target of thalamic inputs, which is important if one studies studying evoked responses. They also lack a L6.

2. It is unclear how much of a cortical tissue would the model represent. If it is a small column, the authors need to justify the validity of studying it in isolation (rather than as a set of coupled microcircuits). If it corresponds to a significant fraction of an area, the authors need to justify the relevance of homogeneity assumption (that all neurons behave like the mean), or switch to methods representing heterogeneous populations.

3. While care was taken on the connectivity between individual populations, the input/output transformation is assumed identical. One would imagine that the effects studied of the circuit depend significantly on the intrinsic properties of the different cell types.

4. An unexpected choice for parameters for intrinsic time scales for the neurons involved which was only in the supplemental material on page 54: while the time scale for SST neurons is 30ms, for PV 7ms the time scale for the excitatory neurons is 3ms. I did try to follow the papers cited for this, but most are modeling papers, and in the experimental paper I did not find this justification. Much better referencing to the exact source of such data is needed. These choices are very different from the intrinsic membrane time constant for these cells.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Rate and Oscillatory Switching Dynamics of a Multilayer Visual Microcircuit Model" for further consideration by eLife. Your revised article has been evaluated by Floris de Lange (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues identified by the first reviewer that need to be addressed, as outlined below:

Reviewer #1 (Recommendations for the authors):

The authors addressed reasonably 4 out of the 5 original points.

Points 1 (lack of layers 4/6) and 2 (homogeneity of inputs/connections) are addressed, and they point to limitations of the model. Layer 4 is discussed but only as an input (while biologically it is strongly recurrently connected) and Layer 6 seems not to be discussed. Given the experimental data available I believe nothing needs to be studied in the results, but a small Discussion section with limitations could help put the work in context.

However, the point about time scales remains incredibly confusing to me.

A critical point is the reply from the authors:

"To test the impact of such time constant differences, we systematically varied the synaptic time constants across different neuron types and examined the network oscillation frequency after VIP input (see the newly added Figures 5e-h, lines 355-375). The notable result was that the transition between a slow and high frequency oscillation remained clearly visible even when all neuron types had the same time constant. This supports the conclusion that the frequency switch is already engrained in the connectivity of the network and is only modified by differences in time constants."

Yet looking at figure 5h, for the same time constants (orange line) the transition is not clearly visible to me.

Another point which is somewhat confusing: looking at equation 1, $\tau$ seems to be better mapped to the membrane time constant and looking at equation 2 the synapses are instantaneous. Yet the authors point to choices of $\tau$ to synaptic not membrane time constants.

If I am interpreting correctly figure 5h, it seems that an important effect described disappears when the time constant for pyramidal neurons reaches 10ms, which is on the low end for the membrane time constant for excitatory neurons. A clear explanation why $\tau$ in equation 1 is mapped by the authors to synaptic rather than membrane time constant, and why the membrane time constant can be ignored when it is longer than the synaptic time constant is needed to understand the applicability of the model for biological circuits.
