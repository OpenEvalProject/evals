# Peer review - Round 1

Editors:
- Stephanie E Palmer, University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.59715.sa1](https://doi.org/10.7554/eLife.59715.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Understanding the connectivity patterns observed in the brain and how these connectivity patterns emerge from local, cell-to-cell plasticity is a grand challenge in modern neuroscience. This manuscript describes conditions under which synaptic plasticity can organize excitatory/inhibitory networks in the brain into assemblies in which both kinds of neurons have structured connectivity, as observed in real networks. The work makes predictions about what kinds of plasticity can give rise to this and accounts for recent experimental findings about manipulating inhibitory neurons and, thereby, the stimulus-dependence of their connectivity. It will be of interest to both the experimental and theoretical neuroscience community, and asks and answers a deep question about how the brain self-organizes its detailed connectivity patterns.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Learning excitatory-inhibitory neuronal assemblies in recurrent networks" for consideration by eLife. Your article has been reviewed by two peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Senior Editor. The reviewers have opted to remain anonymous.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

The work detailed here explores model of recurrent cortical networks and shows that synaptic plasticity must be present in both excitatory to inhibitory neurons and vice versa to produce the known E/I assemblies found in cortex. There are some interesting findings about the consequences of assemblies formed in this way. A major claim in the manuscript (that argues for the broad impact of the work) is that this shows for the first time how a local approximation rule can instantiate feedback in a biologically plausible way.

While the reviewers found the work to be solid and interesting, they failed to find that the work was appropriate for eLife, specifically because of other recent papers that show that a biologically plausible alternative to backpropagation can be instantiated in recurrent neural nets, e.g. a paper published here last year by J. Murray, Local online learning in recurrent networks with random feedback. It's understood that the authors were focusing here on the E/I interactions, but in that case it seems that the novelty of the result needs to be somewhat reframed.

The reviewers were also concerned about the exposition in the introduction and some results that could have been added to a few figures, and had questions about why exactly a BCM rule did not work in this model. Those technical concerns along with doubts about the strong novelty claim led to this decision.

Reviewer #1:

The manuscript investigates the situations in which stimulus-specific assemblies can emerge in a recurrent network of excitatory (E) and inhibitory (I, presumed parvalbumin-positive) neurons. The authors combine (1) Hebbian plasticity of I->E synapses that is proportional to the difference between the E neuron's firing rate and a homeostatic target and (2) plasticity of E->I synapses that is proportional to the difference between the total excitatory input to the I neuron and a homeostatic target. These are sufficient to produce E/I assemblies in a network in which only the excitatory recurrence exhibits tuning at the initial condition. While the full implementation of the plasticity rules, derived from gradient descent on an objective function, would rely on nonlocal weight information, local approximations of the rules still lead to the desired results.

Overall the results make sense and represent a new unsupervised method for generating cell assemblies consisting of both excitatory and inhibitory neurons. My main concerns are that the proposed rule ends up predicting a rather nonstandard form of plasticity for certain synapses, and that the results could be fleshed out more.

1) The main text would benefit from greater exposition of the plasticity rule and the distinction between the full expression and the approximation. While the general idea of backpropagation may be familiar to a good number of readers, here it is being used in a nonstandard way (to implement homeostasis), and this should be described more fully, with a few key equations.

Additionally, the point that, for a recurrent network, the proposed rules are only related to gradient descent under the assumption that the network adiabatically follows the stimulus, seems important enough to state in the main text.

2) The paper has a clear and simple message, but not much exploration of that message or elaboration on the results. Figure 2 and Figure 3 do not convey much information, other than the fact that blocking either form of plasticity fails to produce the desired effects. This seems somewhat obvious -- almost by definition one can't have E/I assemblies if E->I or I->E connections are forced to remain random. I would think this point deserves at most one figure, or maybe even just a few panels.

3) The derived plasticity rule for E->I synapses, which requires modulation of I synapses based on a difference from a target value for the excitatory subcomponent of the input current, does not take a typical form for biologically plausible learning rules (which usually operate on firing rates or voltages, for example). The authors should explore and discuss in more depth this assumption. Is there experimental evidence for it? It seems like it might be a difficult quantity to signal to the synapse in order to guide plasticity. The authors note in the discussion that BCM-type rules fail here -- are there other approaches that would work? What about a more local form of plasticity that involves only the excitatory current local to a dendrite, for example?

4) Does the initial structure in excitatory recurrence play a role, or is it just there to match the data?

Reviewer #2:

In this work, the authors simulated a rate-based recurrent network with 512 excitatory and 64 inhibitory neurons. The authors use this model to investigate which forms of synaptic plasticity are needed to reproduce the stimulus-specific interactions observed between pyramidal neurons and parvalbumin-expressing (PV) interneurons in mouse V1. When there is homeostatic synaptic plasticity from both excitatory to inhibitory and reciprocally from inhibitory to excitatory neurons in the simulated networks, they showed that the emergent E/I assemblies are qualitatively similar to those observed in mouse V1, i.e., stronger synapses for neurons responding to similar stimuli. They also identified that synaptic plasticity must be present in both directions (from pyramidal neurons to PV neurons and vice versa) to produce such E/I assemblies. Furthermore, they identified that these E/I assemblies enable the excitatory population in their simulations to show feature-specific suppression. Therefore, the author claimed that they found evidence that these inhibitory circuits do not provide a "blanket of inhibition", but rather a specific, activity-dependent sculpting of the excitatory response. They also claim that the learning rule they developed in this model shows for the first time how a local approximation rule can instantiate feedback alignment in their network, which is a method for achieving an approximation to a backpropagation-like learning rule in realistic neural networks.

1) The authors claim that their synaptic plastic rule implements a recurrent variant of feedback alignment. Namely, "When we compare the weight updates the approximate rules perform to the updates that would occur using the gradient rule, the weight updates of the local approximations align to those of the gradient rules over learning". They also claim that this is the first time feedback alignment is demonstrated in a recurrent network. It seems that the weight replacement in this synaptic plastic rule is uniquely motivated by E/I balance, but the feedback alignment in [Lillicrap et al., 2016] is much more general. Thus, the precise connections between feedback alignment and this work remains a bit unclear.

It would be good if the following things about this major claim of the manuscript could be expanded and/or clarified:

i) In Figure 1—figure supplement 3 (upper, right vs. left), it is surprising that the Pyr->PV knock-out seems to produce a better alignment in PV->Pyr. Comparing the upper right of Figure 1—figure supplement 3 and the bottom figure of Figure 1G, it seems that the Pyr->PV knock-out performs equally well with a local approximation for the output connections of PV interneurons. Is this a special condition in this model that results in the emergence of the overall feedback alignment?

ii) In the feedback alignment paper [Lillicrap et al., 2016], they introduced a "Random Feedback Weights Support": this uses a random matrix B to replace the transpose of the backpropagation weight matrix. Here, the alignment seems to be based on the intuition that "The excitatory input connections onto the interneurons serve as a proxy for the transpose of the output connections," and "the task of balancing excitation by feedback inhibition favours symmetric connection." It seems synaptic plasticity here is mechanistically different; it is only similar to the feedback alignment [Lillicrap et al., 2016] because both reach a final balanced state. Please clarify how the results here are interpreted as an instantiation of feedback alignment – if it is simply that the end state is similar or if the mechanism is thought to be more deeply connected.

iii) The feedback alignment [Lillicrap et al., 2016] works when the weight matrix has its entries near zero (e^TWBe>0). Are there any analogous conditions for the synaptic plastic rule to succeed?

iv) In the Appendix, the local approximation rule is developed using a 0th-order truncation of Equations 15a and 15b. Is it noted that "If synapses are sufficiently weak.…, this approximation can be substituted into Equation 15a and yields an equation that resembles a backpropagation rule in a feedforward network (E -> I -> E) with one hidden layer -- the interneurons." It would be helpful if the authors can discuss how this learning rule works in a general recurrent network, or if it will work for any network with sufficiently weak synapses.

v) This synaptic plasticity rule seems to be closely related to another local approximation of backpropagation in recurrent neural network: e-prop in (Bellec et al., 2020, https://www.nature.com/articles/s41467-020-17236-y) and broadcast alignment (Nøkland, 2016, Samadi et al., 2017). These previous works do not consider E/I balance in their approximations, but is E/I balance necessary for successful local approximation to these rules?

2) In the Discussion, it reads as if the BCM rule cannot apply to this recurrent network because of the limited number of interneurons in the simulation ("parts of stimulus space are not represented by any interneurons"). Is this a limitation of the size of the model? Would scaling up the simulation change how applicable the BCM learning rule is? It would be helpful if the authors offer a more detailed discussion on why Hebbian forms of plasticity in interneurons fail to produce stimulus specificity.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Learning excitatory-inhibitory neuronal assemblies in recurrent networks" for consideration by eLife. Your article has been reviewed by two peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Richard Ivry as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

The manuscript describes conditions under which synaptic plasticity can organize excitatory/inhibitory networks into assemblies in which both neurons have structured connectivity. The work makes predictions about what kinds of plasticity can give rise to this and accounts for recent experimental findings about manipulating inhibitory neurons and the stimulus-dependence of their connectivity.

While recurrent networks in which connections between excitatory (E) neurons are structured into neural "assemblies" are a classic model for the cortex (e.g. the Hopfield model), inhibitory (I) neurons are often assumed to be unstructured in computational models. This simplification is at odds with the observation of E/I connectivity that is organized with respect to stimulus preference and the results of experiments in which activity of I neurons are perturbed. In brain regions spatially organized according to stimulus preference this may be a consequence of local connectivity, but in regions like mouse V1 that lack an obvious topography, it may arise from experience-dependent synaptic plasticity.

The manuscript investigates the situations in which stimulus-specific assemblies can emerge through synaptic plasticity in a recurrent network of E and I (presumed parvalbumin-positive) neurons. The authors combine (1) Hebbian plasticity of I->E synapses that is proportional to the difference between the E neuron's firing rate and a homeostatic target and (2) plasticity of E->I synapses that is proportional to the difference between the total excitatory input to the I neuron and a homeostatic target. These are sufficient to produce E/I assemblies in a network in which only the excitatory recurrence exhibits tuning at the initial condition. While the full implementation of the plasticity rules, derived from gradient descent on an objective function, would rely on nonlocal weight information, local approximations of the rules still lead to the desired results.

The manuscript makes predictions about the results of blocking plasticity of E->I or I->E synapses as well as accounting for the results of experiments in which activating a pyramidal neuron suppresses similarly tuned neurons through recurrent inhibition.

An interesting prediction of the analysis, that is derived through the approximation to the gradient-based weight update, is that synaptic plasticity rules depend on the deviation of recurrent excitatory input current to a neuron from a target value. This quantity is different from those often used in computational models of synaptic plasticity, such as firing rates or voltages. Experiments targeting this quantity and its influence on the results of synaptic plasticity protocols would be an interesting direction for future study.

Essential revisions:

The modifications the authors have made have improved the manuscript. Addressing the following points will further enhance the clarity of the presentation, and will make the work suitable for publication in eLife.

1) Could the authors please expand on the negative result about developing selectivity in PV neurons through quenched random connections? Would it be possible to adjust the parameters of the model, such as the weight distribution or number of connections onto PV neurons, so that they would exhibit enough selectivity?

2) Relatedly, the text around Figure 3D says that, "Because of the poor stimulus tuning of the interneurons, output plasticity cannot generate stimulus-specific inhibitory inputs to the Pyr neurons (Figure 3D)." But it looks like there is a definite stimulus-specific inhibitory input that emerges. The authors should clarify what they mean.

3) It would be good if the Abstract could be revised to be accessible to a broader audience of readers.
