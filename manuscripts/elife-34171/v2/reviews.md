# Peer review - Round 1

Editors:
- Upinder Singh Bhalla, National Centre for Biological Sciences, Tata Institute of Fundamental Research India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.34171.027](https://doi.org/10.7554/eLife.34171.027)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for sending your article entitled "Recurrent network model for learning goal-directed sequences through reverse replay" for peer review at eLife. Your article is being evaluated by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation is being overseen by Michael Frank as the Senior Editor.

The reviewers felt that the topic of the paper, to obtain reverse replay through modified STDP rules, was interesting and led to some potentially significant predictions of network behavior. However, there were numerous concerns with the study, particularly relating to clarification of figures and results, and consistency with the literature.

Given the list of essential revisions, which could conceivably involve extensive new work, the editors and reviewers invite you to respond within the next two weeks with an action plan and timetable for the completion of the additional work. We plan to share your responses with the reviewers and then issue a binding recommendation.

1). The authors must clear up several points of confusion in data presentation. a) Figure 6 is confusing in many respects and can be interpreted in differentways from the authors. b) The section on theta modulation and sequences is unclear and must beclarified.

2) The authors must address concerns about apparent inconsistency with the experimental literature. These include the time-course of excitatory input, the presence of forward replays in many studies, the conjunctive coding of space and direction of motion by place cells on linear tracks, and whether replay should correlate with previous experience or future navigation. There are also concerns about whether the learning rules are appropriate for hippocampus, and whether the firing patterns in the model look like in-vivo place cell patterns.

3) The authors should make some more testable predictions, for example, the effect of NMDA knockdown on reverse replay.

These concerns and other suggestions from the reviewers are attached to help the authors.

Reviewer #1:

In this study, the authors show that one can obtain reverse replay in 1 and 2-D networks. This relies on symmetric STDP in combination with various forms of STP or postsynaptic after depolarization. The authors also map their learning rules to a T-maze context using a 2-D network and state that the network learns to do goal-directed path learning through reverse sequences. They examine how network connections organize following such learning. In principle this study is interesting as an implementation of a plasticity-driven approach to the emergence of forward and reverse replay, and provides a way to link it to goal planning.

The initial logic of the paper builds up nicely from Figure 1 through 5. One can see how to obtain reverse replay, there is evidence that this is reasonably robust, and one can see conditions where the replay will erase itself due to plasticity.

Figure 6 is a key figure, applying the learning rule to a 2-D network upon which the authors place a T maze. This is a key figure and unfortunately is very confusing.

1) The authors talk about early and late trials. I am going to assume that only trial 9 and 10 are late trials, but the authors must clarify this point.

2) There is a listing of positions A, B, C1, C2, D1, D2 in Panel A mapping to positions 0, 1, 2, 3, 4, 5 in panels C and D. It is strange to have to jump around with the naming within a single figure.

3) Worse, the mapping is different in odd trials and even trails because position 3 from panel C can either be mapped to D1 (panel A) or to B (panel A). Similarly, position B of panel A could be either position 1 or position 3 of Panels C and D. This makes no sense.

4) The authors make several statements about the reverse replay sequencesthat are hard to identify in the figure. They should individually highlightspecific reverse sequences that they want to talk about.

5) I do not see any case in the later trials where sequences travel to D2 except possibly in the first couple of spontaneous responses in trial 9 and one spontaneous trial in 10. Each of these occurs before the training run. Instead almost all the cases, e.g., in Trial 10, start from D2 and go to B. This is a perfectly reasonable reverse replay but is not presented as such in the text.

6) I do not see any case where backward sequences start from D1 and go to D2, unless the authors are conflating position 3 with D1, rather than B. If so then it is the 3 cases (2 in Trial 9 and 1 in Trial 10, which occur before the training run) which fit the bill. If so, those 3 cases look like forward sequences to me.

7) The text says that some of the reverse replay sequences from D1 propagate into D2 instead of the stem arm. I do not see any instances of this, except again if the authors have confused the identity of position 3.

8) The supplementary video looks interesting but lacks annotation to give clarity. Its value is considerably diminished as a result. Nevertheless, my impression on watching it is that my interpretation of Figure 6 is correct, and that the authors have confused position B and position D1.

9) The key paragraph three in subsection “Goal-directed path learning through reverse replay” is very anecdotal. For every statement of a certain kind of replay, the authors need to first, point to examples, and second, give statistics for how often such replays occur in a series of randomized runs.

It may well be that I am quite misunderstanding this figure, in which case the authors should explain it more clearly. Otherwise I think the figure and movie do not support the text.

Reviewer #2:

The manuscript "Recurrent network model for learning goal-directed sequences through reverse replay" proposes an intriguing mechanism for reverse replay of the sequential activation of place cells: combining spike-timing dependent plasticity with synaptic depression, the proposal envisions a wave packet of activity traveling through the network of neurons, such that neurons at the tail end of the packet still fire, but due to synaptic depression, no longer synaptically impinge on the neurons at the front of the packet. As a consequence, Hebbian plasticity strengthens front to back connections, hence enabling reverse replay upon reactivation. In a 2D model, the authors present a nice application of how such a network can produce sequences of place cell activations towards a goal on a path that the animal has never experienced.

The most critical assumption is not, in my opinion, the "rapid modulation of STDP" by synaptic depression, but rather the persistence of neural activity behind the immediate wave-front. Because of profound synaptic depletion, the fact is that there is no reverberant activity that would support the packet and cause neurons to continue to be active.

The trick appears to lie in a time constant of τexc=10 ms with which the excitatory input is convolved (Equation 3) Or, in the spiking network, an NMDA time constant of 150 ms (Equation 16), wherein the peak conductance for NMDA is slaved to the AMPA conductance.

The value of 10 ms for the time constant is, at the very least, debatable. Going back to classic papers (Koch, Rapp, Segev, 1996) or Treves (1993), the real excitatory synaptic time constant (as opposed to the membrane time constant of 10-20 ms) is extraordinarily short and on the order of 2 ms. With that kind of time constant, though, I believe the entire mechanism might collapse.

The second critique I would levy is that the model inhabits an intermediate realm: it is neither minimalist, nor veridically detailed.

In particular:

i) Equation 5-6 cover both facilitation and depression. As far as I can tell, facilitation is not at all necessary for the mechanism. Why is facilitation then included?

ii) Equation 12-13 describe the Izhikevich, 2003 model with the parameter set for the regular spiking cell (though the fact that it is the parameter set for RS is not explicitly mentioned). The only possible advantage of the Izhikevich model over an integrate-and-fire model might lie in the adaptation of the firing. But is this important in the model?

iii) Going from 1D to 2D in subsection “Goal-directed path learning through reverse replay”, the idea of theta modulation and theta sequences is sprung upon the reader, but it never became clear to me whether Equation 36 (for the theta-modulated current input) is really necessary or not.

The third critique reflects the color scheme. Throughout, inactivity is represented by black, which makes the figures hard to read in a printout or even on the screen. Please choose another color scheme that results in a white (or light-colored) background. Figure 6 is confusing, as it mixes letters on the W-shaped track (which, for some reason, is called a T-shaped track), but then the panels use numeric labels; the mapping is only explained in the last sentence of the caption. On some panels of Supplementary Figure 2, the tick-labels on the y-axes cannot be read.

Reviewer #3:

The paper describes a modified version of spike-timing dependent long-term plasticity (STDP) modulated by short-term synaptic plasticity (STP). The main advantage of this modulation is to be able to obtain an effectively asymmetric STDP rule starting from a symmetric one (symmetric STDP has been recently observed in hippocampus). The authors show for instance how an imposed sequential activation of neurons can modify synapses in a network, so that a network can spontaneously "replay" the sequence in the opposite order, as observed in place cells.

I think that the results nicely characterize the properties of the hypothesized plasticity rule and show a potential application in neural networks.

I have two major concerns:

1) The connection with dynamics of hippocampal place cell activity strongly focuses on reverse replays, but there might be other aspects to consider more carefully:

i) Forward replays: The modeling presented in the first part of the paper, where a reverse replay is elicited by the stimulation of place cell coding for the middle of the track, should be probably compared to the results of Davidson et al., 2009. In that paper, the rodents frequently stop away from the two ends of the track; this more closely resembles the scenario depicted in the manuscript. The results of the paper indicated that forward replays were as (or more) likely to occur compared to backward replays (similar to Diba and Buzsaki, 2007), and the propagation speed of forward and backward replays was comparable. How can one reconcile the results reported in the manuscript with these observations?

ii) Directionality of firing in linear tracks: It is generally observed that place cells code conjunctively for spatial location and direction of motion in 1D. This aspect of place field firing has not been discussed and it's not entirely clear to me how to interpret the authors’ results in light of this experimental observation.

iii) Replays in 2D: Pfeiffer and Foster, 2013 reported replays that generally did not correlate with the previous experience of the animal, rather there was a correlation with the immediate future navigational behavior of the rodent. In those experiments, the goal location was moved from session to session, and those sequences were observed within the first few trials. In a follow-up commentary (Pfeiffer, 2017), it is argued that "reverse replay does not facilitate learning in a familiar environment". It would be useful to see those results and claims more carefully discussed in the manuscript.

iv) Theta sequences: During running, fast sequential activity (forward direction) of place cells within individual cycles of the theta oscillation are observed. I guess that before replays, these sequences could help in building up the asymmetric connections that later generates reverse replays. But what happens to theta sequences after the synapses are modified? Would they be less likely to occur? In general, I found the few references to theta sequences in the manuscript to be confusing.

2) The plasticity rule is loosely based on previous work in visual cortical synapses (Froemke et al., 2006). As such there is no evidence that this rule quantitatively captures the dynamics of synapses in neo-cortex or hippocampus. It would be helpful to test the plasticity rules with firing patterns more closely resembling the activity of in vivo place cells (e.g., fields of ~1s durations, peak firing ~10Hz, phase precessing) and realistic learning rates.

[Editors' note: the authors’ plan for revisions was approved and the authors made a formal revised submission.]
