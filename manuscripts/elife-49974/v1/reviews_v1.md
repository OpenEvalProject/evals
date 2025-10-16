# Peer review - Round 1

Editors:
- José D Faraldo-Gómez, National Heart, Lung and Blood Institute, National Institutes of Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.49974.sa1](https://doi.org/10.7554/eLife.49974.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

In this interesting paper, the authors demonstrate via a mathematical modeling approach that cooperative gating with ion channels such as Ca2+ channels can be tuned to form bistable conductances that act as a potential form of memory by integrating inputs over longer periods that would be anticipated in single channels gating independently. The authors demonstrate that the integrative memory – hysteresis – allows for persistent graded neuronal firing.

Decision letter after peer review:

Thank you for submitting your article "Clusters of cooperative ion channels enable a membrane potential-based mechanism for short-term memory" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by José D. Faraldo-Gómez as Reviewing Editor and Gary Westbrook as the Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: Colleen Clancy (Reviewer #2)

Although it is customary for eLife to condense reviewers' reports into a concise decision letter, in this case the Reviewing Editor believes it would be best to enclose these reports as originally submitted. Based on these reports, we would like to invite you to submit a revised version of your manuscript that addresses the questions and concerns raised.

Reviewer #1:

Pfeiffer et al. study the computational consequences of the cooperative on- and off-dynamics within the population of voltage-dependent ion channels. While the classic conductance-based neuron models assume that channels open and close independently, experimental evidence shows more and more cooperative effects. For example, Kim et al., 2014) has shown that potassium channel cooperativity can occur. In the present manuscript Pfeiffer et al. show a hysteresis and bistability in the gating properties of such groups of channels.

Similar to coupled magnets, a cluster of interacting ion-channels can lead to a hysteresis and a bistable opening dynamics within that cluster. On the functional level, the ion channel bistability can be exploited to implement persistent spiking in neurons that is initiated by depolarising pulse and stopped by a hypopolaring signal.

What I like about the paper is that it combines mathematical modeling with dynamic clamp experiments. Also the authors link the presence of cooperative clusters to persistent activity, something that operates at the spiking level. Somewhat counter intuitively, the cooperative coupling need not be present in the channels that are involved in the action potential generation (e.g. Na and K) but it seems that it is sufficient that cooperativity of some depolarising cationic channels in the membrane is present.

1) Can the authors comment on whether the cooperativity of depolaring channels that are involved in the AP generation leads to the same or different net-effect (bistability) as that of other depolarising cationic channels. Is there any functional difference?

2) How does the bistable switch operate in the presence of noise, are there any spontaneous switches?

How does the duration of the upper state relate to the noise level?

3) From spiking networks we know that presence or absence of bistability can depend on the size of the network. The depolaring pulse to induce a switch needs to be stronger and longer for larger networks, ~to sqrt(N). Does the size of the cluster and the size of the switch inducing pulse correlate in some way? Can the authors comment on what a realistic regime could be?

4) I think it would be a good idea to streamline the Introduction and Discussion and cut the number of figures and panels. It does seem like the last 3 figures have somewhat overlapping messages.

Reviewer #2:

In this interesting paper, the authors demonstrate via a mathematical modeling approach that cooperative gating with ion channels such as Ca2+ channels can be tuned to form bistable conductances that act as a potential form of memory by integrating inputs over longer periods that would be anticipated in single channels gating independently. The authors demonstrate that the integrative memory – hysteresis – allows for persistent graded neuronal firing.

The idea of coupling between ion channels as a form of memory is an elegant concept. I do wish the authors would take it a bit further: there are a number of channels that have demonstrated cooperative gating and more generally coupled gating. These vary widely from K currents to gap junctions with a variety of associated kinetics – fast versus slow gating, low versus high conductance, long versus short open times and latencies to opening etc. I think the authors could do a more expansive exploration of the potential memory dynamics that could be coded within such a large parameter space. Such an analysis may open more doors for future computational and experimental exploration.

Reviewer #3:

The authors propose a new intriguing mechanism that keeps short-term 'memory ' of recent (seconds) history of membrane potential changes by changing conductance states of clusters of cooperative channels. Changes of conductance states of cooperative channels, in turn, produce changes of the rate of persistent firing. The authors explore this novel mechanism in computer simulations and demonstrate that it can indeed mediate graded changes of persistent firing in dynamic clamp experiments with neurons from entorhinal cortex in slices.

In my view, the following aspects make this study especially important and of broad interest:

First, demonstration that cooperativity in a cluster of channels introduces a fundamentally new dynamics to the gating, expanding dramatically (by the orders of magnitude) the time scale on which channel clusters could keep trace of prior changes of the membrane potential.

Second, demonstration that such mechanism could mediate gradual changes of persistent activity of neurons – a feature that has important functional implications.

The proposed mechanism can help to establish an important link from basic electrophysiological properties of neurons and individual channels to cognitive mechanisms of short-term memory.

I have however several concerns that should be addressed.

1) What turns off open channels in cooperative clusters? Say in Figure 1, at V=V0.5, activation curve for strongly cooperative channels (Figure 1B) is at 1. Why would all channels close at about same time? Is their closing (inactivation?) also cooperative?

A more comprehensive analysis of opening/closing dynamics of a cluster may help here.

It is clear that a strong hyperpolarization can turn channels off, but how would this happen spontaneously?

2) Conductance through permanently open channel clusters might change the membrane potential (e.g. in Figures 4 or 5 simulations). Certainly, resulting Vm shift would depend on the ratio of conductance through channel clusters to other conductances, but since it influences firing, it might also influence the Vm.

3) Writing is often in very general terms, lacking specific details; e.g.:

– Authors talk about "channels" – which channels? If specifics of ionic conductance does not matter, this should be clearly stated in the very beginning.

– Introduction (last paragraph), it is not clear that you are talking about model simulations.

– Materials and methods: description of electrophysiological experiments is very vague. Recording from which brain area? Which cells were targeted?
