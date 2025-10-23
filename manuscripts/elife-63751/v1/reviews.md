# Peer review - Round 1

Editors:
- Tatyana O Sharpee, Salk Institute for Biological Studies United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.63751.sa1](https://doi.org/10.7554/eLife.63751.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper describes how spiking neurons can learn spatio-temporal sequences with flexible duration of intermediate states. Available methods only allowed learning of sequences where duration could not be varied broadly. The proposition put forward in this work solves this long-standing problem in a convincing and in a biologically plausible way.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Learning precise spatiotemporal sequences via biophysically realistic learning rules in a modular, spiking network" for consideration by eLife. Your article has been reviewed by a Senior Editor, a Reviewing Editor, and two reviewers. The reviewers have opted to remain anonymous.

Our decision has been reached after consultation between the reviewers. The consensus was that the manuscript raises an interesting problem and provides an interesting but partial solution to it. The reviewers described many analyses that needed to be completed prior to publication. The reviewers thought that once all of that work was completed, the manuscript would be so substantially different that it would qualify as a new submission. Therefore, the consensus decision at this stage is not to consider further this manuscript for publication in eLife.

Reviewer #1:

In this study authors note that many models of sequential activity in the brain only account for the order in which neurons spike and fail to take into account the duration for which each neuron responds. This is indeed an interesting problem. Authors provide a network architecture that can solve part of the problem.

They assume that a neural activity sequence is consisted of many events. Neuron groups are tuned to these events and spike in order as these events occur. Each neuron group (Core Neural Architecture or CNA) consists of Timer, Messenger (both excitatory) and inhibitory neurons subgroups. The recurrent connections within Timer neurons encode the duration. The Messenger neurons project to the next CNA and encode the order.

An important part of the circuit is the inhibitory neurons which stop firing before the timer neurons (even though they are driven by timer neurons) and thereby release the Messenger neurons from inhibition at the end of the duration of the event. Thus, messenger neurons firing maximizes and signals the end of the “duration”.

Authors then expand the network to have a “reservoir” network and show that their scheme can also generate non-markovian sequences in which a particular neuron group is activated multiple times in the sequence.

I think the authors have raised an interesting problem and provide a solution that at least partly solves the problem. However, there are a number of shortcomings of the work which reduce the significance of the work.

1) Here authors are assuming sequences of distinct events. But to facilitate learning it is crucial that the animal is rewarded after each event. I am not convinced that every component of a sequential behavior is rewarded.

2) The key to indicate the end of duration of a sequence component, is that the inhibitory neurons stop firing before the Timer neurons. Why should this be? Since inhibitory neurons are driven by time neurons and that typically inhibitory neurons have low spike threshold one would expect the inhibitory neurons to remain active as long as Timer neurons are active. This must require fine tuning of the circuit which is beyond synaptic changes. This particular component of the model makes it appear contrived. Authors have not provided biological motivation or evidence of robustness of the mechanism. Authors finally predict that "There will be a population of inhibitory cells within each module that have firing properties similar to Timers but that decay more quickly (Figure 2A)." But is this enough? There will also be other inhibitory neuron type which will not have this exact dynamics -- will that be a problem?

3) While it is possible to have non-Markovian sequences but still each Timer can show only a single duration. Authors only make passing remark on how this could be amended but the solution is very ad-hoc and very likely will not scale.

4) The main motivation of the work is to come up with a biologically plausible model of sequence (order and durations). But the addition of reservoir and a sparse readout makes it non-biological. Moreover, authors have not specified the properties of the reservoir, specifically how does it keeps the memory of sequence of different messengers. And if the long-term memory of the messenger sequence is already in the reservoir, then why the sparse-net readout stage is needed.

5) The whole work is presented as demonstrations of key results, there is no systematic analysis of robustness of the results. I disagree that it is beyond the scope of the current work - I think that is exactly what should have been done, after all this is a computational study.

Other questions:

- If the Timer neurons are recurrently connected with excitatory neurons, how come their activity dies out and what determines the decay time constant in a timer circuit. Recurrently connected population of only excitatory neurons (timer cells) has only two fixed points: one at maximum value (and then the activity will sustain for ever) and the zero activity fixed point. So it would require fine tuning to get to the right duration. This again goes back to the issue of the robustness of the results.

- In a computational study like this it is very important to show the parameter ranges in which the demonstrated phenomenon is observed. Here it is also important to show under what conditions we can get a wide range of timings. Authors have chosen equal number of timer, messenger and inhibitory neurons - how crucial is this? Could we still get the same results if we assume 80-20 ratio of excitatory/inhibitory neurons?

- What is the min. and maximum duration for each event in the sequence that can be learned and recalled? (This goes back to the issue of the parameter ranges).

- What happens when the sequence parts overlap?

- Does the learning automatically stop or it has to be manually stopped.

- Since the three-stage model is more general, I guess that should be the one implemented in the brain. So I think authors should make predictions at that level? Where are reservoir and sparse net located and how would be the activity in these two modules.

Reviewer #2:

In the manuscript "Learning precise spatiotemporal sequences via biophysically realistic learning rules in a modular, spiking network," the authors propose a plastic spiking network model that learns selective temporal sequences with variable timing.

The authors propose a novel and tractable plasticity model with separate eligibility traces for LTD and LTP. The normative fixed point approach the authors employ to solve the temporal learning problem is elegant. Further, the writing is clear, the question well-motivated, and relevant literature cited correctly. However, the manuscript lacks a closer comparison to existing experimental data, and several open questions remain related to the network’s temporal dynamics and the robustness of the proposed learning mechanism.

1) From where do the long time scales in the network model come?

A crucial property of the timer cells is their slowly decaying firing rate which is the basis of the adjustable decays, presumably linked to the learning of the recurrent connections. It was not entirely clear what causes these slowly decaying rates in the model. The question arises because slow working memory like dynamics are non-trivial to get, especially, in spiking neural networks with physiological time constants. A body of literature tackled this issue with, for instance, attractor models (Amit and Brunel, 1997; Yakovlev et al., 1998), non-normal network dynamics (Goldman, 2009; Hennequin et al., 2012), or negative derivative feedback (Lim and Goldman, 2013). However, the present model does not seem to contain any intrinsically slow time constants. Perhaps the unusual combination of slow excitation ~80ms vs. fast inhibition (~10ms) results in some form of negative derivative feedback? This choice is opposite to the usual fast AMPA vs. slower GABA dynamics. While several potential mechanisms could underlie such slow ramping activity, it is essential to clarify this point and, perhaps, illustrate that the proposed learning scheme is robust to other slow timescale mechanisms.

2) How plausible is the delay activity state in the network model?

Although the authors used spiking neural network models for part of the study, the spiking network activity is neither shown nor characterized. How does the spiking activity look like in the present model? The firing rates seems rather high, which raises the question of how compatible the network activity is with cortical networks. For instance, the firing rates during the onset phase of the timer cell do look relatively high (>80Hz). Whereas, in many sensory areas spiking activity is relatively low and asynchronous irregular, possibly linked to a balanced state.

How does the activity in the present model compare to such balanced models? Would balance and the associated activity pose a problem? The manuscript would benefit if the mechanism proves robust to such presumably more realistic activity regimes.

3) Comparison to experimental data

One misses a more detailed treatment of how the proposed learning algorithm can be further verified with experimental data. Although inspired by experiments (Gavornik and Bear, 2014), a closer and perhaps more quantitative comparison to experimentally observable network activity in sensory cortices is desirable. Such verification may be challenging to accomplish solely based on LFP recordings. Maybe there are specific salient dynamical signatures that the present model predicts? One of the strong assumptions of the model is that there are two functionally different excitatory populations (timers and messengers) with a stereotypical interplay in time. How easily can such populations be recovered from (simulated) data?

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Learning precise spatiotemporal sequences via biophysically realistic learning rules in a modular, spiking network" for consideration by eLife. Your article has been reviewed by Ronald Calabrese as the Senior Editor, a Reviewing Editor, and three reviewers. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional simulations are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

This manuscript addresses the problem of learning sequences of events with variable durations. This is an important problem. The revised manuscript was reviewed by two new reviewers and one previous reviewer. The consensus was that the manuscript will be suitable for publication after the following two points are addressed:

1) Time constants of inhibitory neurons:

The choice of synaptic time constants (80ms for exc. and 10ms for inhibition) is very odd. There is no justification provided for these values.

The solution that was proposed by the reviewers is that to solve this issue by redifining the time scale by, say division by 5. So that what now is 80 milliseconds becomes 16 milliseconds. This has to be done consistently throughout the paper, but new simulations are not absolutely necessary. The point can be addressed by careful re-definition of time scales throughout the manuscript, if this is what the authors prefer.

2) The emergence of CNA and fine tuning of the model:

Another crucial parameter is the connections from timer-->messenger and inhibitory neurons--> messenger neurons. These have to be tuned such that messengers only fire when inhibition has gone down. These synapses do not appear to have been learned using the TTL in this model. This point can be addressed by testing robustness with respect to changes in the synaptic weights: what happens if connection weights are change by +/- 29 percent. New simulations are necessary here.

Reviewer 1:

One of the main points raised in the previous review was that of the fine tuning of the parameters. In this revision authors have not done much to address that concern (see below for my comments on their reply). So for now, I maintain that the model is contrived and rests on very strong assumptions for which there is little experimental evidence.

1) The issue of rewards:

Authors write: We have assumed that on every transition between external stimuli, a “novelty” signal causes a global release of a neuromodulator, which acts as a reinforcement signal (see Materials and methods).

This is a big assumption. Clearly, we don’t just make sequences of novel events. Familiar events are also added in sequences with novel events.

2) Time constants of inhibitory neurons:

The choice of synaptic time constants (80ms for exc. and 10ms for inh) is very odd as also noted by the second reviewer - but this is also crucial to the model. But there is no justification provided for these values.

3) The emergence of CNA and fine tuning of the model:

Another crucial parameter is the connections from timer-->messenger and inh neurons--> messenger neurons. These have to be tuned such that messenger only fire when inhibition has gone down - I do not think these synapses have been learned using the TTL in this model.

Authors argue that these synaptic weights can be learned as they have shown in Huerta et al. But CNA architecture is different from the model studied in Huerta et al. Three types of cells in Huerta et al., are all excitatory and there is a global inhibitory population. But for the CNA here we need two excitatory populations and one inhibitory. Moreover, the third inhibitory population cannot serve the function of global inhibition that may give rise to the timer/messenger cells (e.g. following Huerta et al.,). Furthermore, in the Huerta paper number of messenger cells are way too low but here authors have assumed that there are equal number of timer and messenger cells. Therefore, authors’ claim that they have provided a putative mechanism for the emergence of the CNA structure is not correct.

Since authors argue that "there are a number of degenerate sets of parameters" they should show some of those. In addition, since the choice of synaptic time constants is so odd, they should show that the model works when exc. synaptic time constant is smaller than inh time constant - or how close these two time constants can be. When a model has so many parameters it is important to question the robustness of the model.

Authors have shown the robustness of the learning algorithm (Figure 5—figure supplement 1) but there are other parameters in the model that are not associated with plastic synapses. How crucial are they? At the outset it is obvious that the synaptic time constant are crucial and for some reason exc. syn time constant has to be longer than inhibitory time constant. Similarly, the connectivity from timer-->messenger and inh-neurons-->messenger needs to be tuned very carefully.

4) The issue of other inhibitory neurons:

My question was not about the detectability. My concern is that besides the inh neurons in the CNA there will be other inhibitory neurons in the network e.g. those needed for the emergence of time/messenger populations. Would their activity cause problems?

5) Biological realism:

I agree with the authors that they have a local learning rule and the rule is biologically plausible. My concern was about using reservoir network (which is fine) and still calling the model (Figure 5) biologically realistic. I also do not understand the use of the term “reservoir”. To me it seems like an attractor network. As the authors know, in reservoir computing we need to train the readout of the “reservoir” to get a specific pattern in response to an input.Reviewer 4:

The paper addresses the problem of learning sequences composed of events of variable duration. This is an important problem and solution using messenger and timer cells is interesting and novel. I am less convinced of the utility of relying on reservoir computing to solve non-Markovian sequences. I wonder whether this can be done using connections between different CAN.

It is not clear whether the primary visual cortex (or a primary sensory area) is the best brain area to draw parallels with the proposed framework. Perhaps hippocampus would be more appropriate. In any case, layer 4 and 5 of primary sensory areas have very different properties and assigning them the same properties detracts from biological plausibility. There is some sequence learning in the visual cortex, but this is not the main effect in primary sensory processing.
