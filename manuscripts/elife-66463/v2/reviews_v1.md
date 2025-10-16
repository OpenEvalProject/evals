# Peer review - Round 1

Editors:
- Tatyana O Sharpee, Salk Institute for Biological Studies United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66463.sa1](https://doi.org/10.7554/eLife.66463.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper demonstrates through theoretical modelling how the switch from excitatory to inhibitory signaling occurring in new born neurons can aid the integration of new neurons into the existing neural circuit. The modelling analysis also analyzes how this can aid the temporal integration of relevant memories.

Decision letter after peer review:

Thank you for submitting your article "A functional model of adult dentate gyrus neurogenesis" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and John Huguenard as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Paul Miller (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential Revisions:

1. Provide analysis of the model where mature neurons also exhibit plasticity but at reduced levels.

2. Examine how network behaves when inputs have different statistics.

Reviewer #1:

The authors propose a role for newborn cells in the dentate gyrus that relies upon their input from interneurons being initially excitatory before switching to inhibitory as the cells mature. The computational modeling and accompanying analyses show how, when receiving only excitatory input, the newborn cells become responsive to stimuli similar to those that already cause high responses in other cells, but then, following the developmental switch such that they receive inhibitory input, those cells then gain responses to novel, but similar, inputs. In a simplified model, the authors are able to quantify the criterion of "sufficient similarity", such that if the novel inputs are not similar enough to the original ones the newborn cells to not gain responses to them. The authors demonstrate that such only when newborn cells are incorporated into the network and respond to the novel stimuli, can those stimuli be categorized by the network, as necessary for them to be recognized.

A major achievement of the paper is to identify a role in information processing for the developmental shift in reversal potential of chloride ions. Such a role is well supported by the results in the paper.

As in all modeling papers, some choices must be made so as to simplify the system to render it tractable and its behavior understandable. Some of the choices could be better justified or discussed, as highlighted below.

The normalization of inputs such that the L2-norm is fixed seems rather unusual, and is not clearly the actual impact of feedforward inhibition. It would be nice to know whether this feature of the input vector is important. Would it matter if the L1-norm were used for normalization, or if normalization were not precise? Perhaps a comment on the importance of this could be made, as well as a justification for the choice.

Throughout the manuscript, the authors employ a homeostatic term in the postsynaptic firing rate. The term is called "heterosynaptic" by the authors, but strictly it is not, since it does not depend on other presynaptic inputs. Rather, the plasticity rule effects "firing rate homeostasis" and is implemented in a manner similarly to Renart, Song, and Wang, (2003). I think this should be mentioned at a minimum and perhaps entirely renamed throughout the manuscript.

The authors consider the ability of the network to discriminate novel patterns as the newborn cells gain responses to the novel patterns. I assume that the formation of new responses arises when the novel patterns are presented randomly amidst the set of previously learned patterns. It would be valuable to see if there are prediction of any differences in behavior if the novel patterns were presented alone, or if there are any impacts of different manners of interspersing learned patterns with novel patterns.

Lines 68-91 contain a lot of details of the circuitry, many of which are not included in the model. It would be helpful to have a figure showing the full circuit based on the information written (which is rather hard to take in through one reading) and beside it to include a figure of the model circuit so the reader can easily see what is being simplified and omitted.

Lines 118-119: I think you should mention here or in the Discussion that you have selected a specific set of synapses to undergo plasticity-that is, if I understand correctly, you have ignored any plasticity with the Dentate Gyrus.

Line 167-8, Equation 1: This equation appears to be different from that of Equation6 in the methods. In particular the "HET" function depends on postsynaptic rate-cubed, not just the difference between rate and threshold as suggested here. Why not just write the exact equation and indicate/describe the behavior of each term?

Line 260-261: The terminology is a bit confusing, as activation is not clearly a "change in membrane potential" but a change in firing rate, so has different units to the reversal potential. Especially as the membrane potential must be venturing above threshold to produce some spiking activity. Perhaps the criterion is equivalent to "the activity is low enough that the mean membrane potential remains below the reversal potential of the chloride channels"?

Line 272-3: The statement about the switch in excitability here assumes we already know it, though it is described in the methods much later. Perhaps this sort of issue is inevitable in journals where methods are placed after results, but it would be better if the order were reversed!

Line 320: I see no justification for a one-way t-test. I think they should be two-way unless it is only possible a priori for a change in one direction.

Line 338: The mention of fixing one set of inputs arises out of nowhere without justification – though that justification comes later as this is just one of two controls. I think it would be better with the order reversed. Or, at least when it is first mentioned here, please be clear why this was chosen, as – I assume – the feedforward weights to selective cells are not fixed in the main set of results. If feedforward weights to selective cells are fixed in the earlier sections, then it should be clearly mentioned, as I did not notice it.

Line 364: Following the previous comment, this line suggests that feedforward weights are not fixed in your primary results with good discrimination. Please clarify if this statement is constrained to the networks without neurogenesis.

Reviewer #2:

Gozel and Gerstner investigated the functional role of adult neurogenesis in the dentate gyrus using simulations and mathematical analysis of a computational model. The novelty of the paper compared to numerous previous studies in the field is the inclusion of the GABAergic switch from excitation to inhibition of new neurons during the maturation process. So far this has been overlooked in the computational literature. G&G propose an elegant and potentially interesting idea for how the two phase maturation process could be functionally beneficial for an animal tasked with discriminating stimuli, and would be the first to recapitulate the experimental finding of adult neurogenesis contributing to pattern separation of similar but not distinct stimuli.

However, my assessment is that the current model simulations and analysis are not sufficient to support for the claims made in the paper. Furthermore, the main experimental finding that can be understood based on this modeling work is emergence pattern separation for similar but not distinct stimuli. While interesting, this is rather technical, and may depend quite strongly on the details of the model.

1. The input stimuli from the MNIST dataset presented to the network are low dimensional to a very good approximation ("3", "4", "5"), in contrast to the type of stimuli a real network would be presented with which are expected to be high-dimensional.

1.1. In the model analyzed, the narrowness of the distribution of synaptic weight vector norms is important for network stability. This narrow distribution could at least in part be inherited from the low dimensionality of stimuli (all "3's" have large overlap with the "average 3"). If the overlaps of different stimuli are broadly distributed, so will the distribution of how many input patterns each neuron is a "winner" in. It is important to test this stability in more realistic stimulus ensembles, perhaps by controlling the width of the overlap distribution using the binary model the authors present towards the end of the paper.

1.2. The authors claim that synapses of newborn DGCs starting the maturation process from 0 is important for solving the problem of unresponsive neurons. The reason is that during this phase the synaptic weight vector becomes aligned with a specific direction of the input space. It is possible that unresponsive neurons are stuck in a local minimum (like the case with no neurogenesis) precisely because stimuli (and overlaps) are narrowly distributed around the mean. If stimuli are more broadly distributed (~higher dimension), the basins of attraction are expected to be more numerous and more shallow. Therefore one may expect the problem of the system getting stuck in a local minimum to be far less severe in this case, and for "control 2" networks to learn well.

2. Setting no plasticity (eta = 0) for mature cells is a very strong assumption. Some protocols (e.g., TBS2 in Schmidt-Hieber, 2004; and others in Ge 2007) lead to ~2 fold increase in plasticity in young vs. mature neurons. Since mature neurons significantly outnumber young neurons, the effect of plasticity in mature neurons cannot be neglected altogether, especially since the paper's main focus is on the integration of newborn neurons into the circuit. Given the actual degree of synaptic plasticity in mature neurons (according to the papers that the authors themselves cite) I expect the behavior of the authors model to be much closer to "control 3". To support their claims, I think the authors should show that their network compares favorably to control 3 even if DGCs remain plastic throughout (but to a lesser extent). In this scenario I expect the fraction of neurons that are new at any given time to be much more important than the current model, since the mature part of the network is fixed. Therefore this fraction should also be matched to experiments.

3. It is not clear to me how the two phase maturation process of DGCs would be affected in a scenario where at any given point some DGCs are in the excitatory phase of GABA and others are in the inhibitory phase. This would be expected if there is a continuous stream of new neurons. Would the plasticity of the neurons in the inhibitory phase not interfere with aligning the activity to similar stimuli due to plasticity of neurons in the excitatory phase? If there is interference, would the authors then predict that neurogenesis occurs in waves (i.e., some kind of global signal would coordinate transition from phase 1 to 2 across synapses)?

Is there evidence supporting that?

It seems to me that the calculation in the section "Analytical computation of the L2-norm and angle"--at least in principle--be extended to estimate the interference: the competition due to plasticity of neurons in the inhibitory phase increases the angle phi, and thus slows down the alignment of the weights due to plasticity of neurons in the excitatory phase.

107, Review of functional role of DGCs.

Aljadeff et al., 2015,

Shani-Narkiss et al., 2020

suggest a dynamical role for new neurons.

312, It would be interesting if the advantage of adding newborn neurons stimulated with "5" to a network pretrained with "3" and "4" over a network pretrained with "3", "4", and "5" would persist if some amount of plasticity remains in mature neurons (Figure 3d).

614, It would be good to discuss the possibility that neurotransmitter switch (without neurogenesis) has the same functional role as GABA switch in the current model. See e.g., Li et al., (2020) J Neuroscience.

Furthermore, can this model teach us anything about neurogenesis in the olfactory bulb? Is there an E to I switch there too?

725, Miller and Fumarola may not be the right reference to cite here. This specific nonlinearity (rectified tanh) is not standard and is not included in that paper.

778, Definition of quasi orthogonal is not clear. The inhibitory rates can have fluctuations and temporal dynamics of their own even if the network is assumed to be silent when each stimulus is presented. Therefore inputs might be quasi-orthogonal at one time but not at another. If in this is used just to qualitatively understand the network behavior, this somewhat sloppy definition is ok, but I think this caveat should be mentioned to avoid confusion.
