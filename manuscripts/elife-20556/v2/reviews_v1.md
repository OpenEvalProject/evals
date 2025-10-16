# Peer review - Round 1

Editors:
- Upinder S Bhalla, National Centre for Biological Sciences , India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.20556.019](https://doi.org/10.7554/eLife.20556.019)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: a previous version of this study was rejected after peer review, but the authors submitted for reconsideration. The first decision letter after peer review is shown below.]

Thank you for submitting your work entitled "Dendritic trafficking faces physiologically critical speed-precision tradeoffs" for consideration by eLife. Your article has been favorably evaluated by Naama Barkai (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors. Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

Here is a synthesis of the views of the reviewers, highlighting the main points.

1) All three reviewers appreciated the development of a general and simplecoarse-grained model of cargo localization, and the incorporation of severalaspects of experimentally observed trafficking.

2) There is a shared common concern about whether real neurons do experience the bottlenecks and very slow settling of cargo distributions that the model predicts. All three reviewers felt that the real settling time was likely tobe faster than the model predicts.

3) There were also shared concerns about the model assumptions, particularlywith respect to the mechanisms assumed for the system. The reviewers felt thatsome likely, and experimentally supported mechanisms were left out of theanalysis. Some of the mechanisms that the reviewers mentioned included cargo reloading, feedback, and having sufficiently large cargo traffic to feed transient local requirements for cargo. The reviewers felt that these mechanisms might eliminate the slow time-courses predicted by the current study.

4) The reviewers were hoping to see a more complete mapping to experimentswith stronger mechanistic predictions and closer ties to biologicalobservations.

Reviewer #1:

This study puts quantitative flesh on the bones of the sushi-belt model for transport in the dendrites and its interaction with local signals resulting in cargo offloading.

At the outset it is important to make the point that the sushi-belt model as originally proposed was a word-model, and the process of converting it to mathematical form is non-trivial and itself involves many mechanistic assumptions and insights. While I generally appreciate the motivation of the study, I have concerns about some of the assumptions and feel that some aspects of the model behavior and study conclusions may be artifacts of these assumptions. Specifically, I feel that the key conclusions about speed-specificity tradeoffs and the time-course for attaining desired distributions are overstated. Below I indicate how other model assumptions, or even factoring another term into the same model (point 6), may overcome the stated limitations in achieving target cargo distributions.

1) The first aspect of the model involves the microtubule-based transport.

Here the authors adapt and simplify a biased 1-D random-walk model by

Muller et al. They consider two variants: simple independent probabilities,and history-dependent probabilities. This first set of model conversion iswell-grounded in the literature and results in a familiar model form. Thistakes them to an analysis of cargo distribution as a function of transportrates, and they show that a variety of distributions can be achieved throughthis mechanism. If I understand correctly, the main novelty in this figureis the result that even with long runs the mass-action model fits thestochastic one reasonably well. It would be nice to have a panel of thisdependency, that is, a graph of fit vs. run length.

2) The next step of the modeling is to consider how the local rates oftransport might be modulated. The authors come up with a somewhat limitingmodel here, assuming only a single signal (Ca for convenience), and achieveforward/backward rate control by taking the signal levels in successive spatialcompartments. Here one could readily imagine that different localsignals might be a more versatile (and spatially more precise) way to achievecontrol of forward and backward rates of transport. Can the authors examinethis?

3) The electrical calculations in Figure 2E are poorly described. I assumethat the authors use the full Migliore 2012 model to obtain an electricalpotential distribution upon synaptic stimulation. It would have been usefulto have seen the electrical potential and its time-course. Over what timewas the 'average potential' taken? How did the potential map to the rates?

The authors refer to the methods section but there is insufficient informationthere.

4) The authors go through a few more elaborations in the model, before bringing in a 'detachment' scheme that finally takes their model to something more like the full sushi-belt model. In Figures 1–3 I am concerned that the analysis talks about density of cargo on the motors rather than free cargo in thedendrites. First, it would be valuable to make this distinction clearer tothe reader. Second, it would be valuable to discuss whether these predictionshave physiological observations to compare with. I do not have a sense forhow much cargo sits on the motors, and how much variability is observedin the distribution of motor-attached vs. detached forms.

5) When detachment is incorporated into the model, the authors find that onegets non-specific cargo delivery, as well as depletion of cargo attached tothe motors. I am concerned that these phenomena are more a reflection ofassumptions than physiology. Specifically, the unloading of cargo is anopen-loop, stimulus-driven process in the model. I wonder how many of thesefindings would hold if the unloading rate were driven not just by stimulus,but also by feedback based on amount of desired cargo that was alreadypresent. That is, a term dependent on ui*. Further, the degradation itselfcould also be driven by feedback. I suspect that the set point might bereached much faster with these elaborations.

6) Looking in more detail at the equations in the subsection “Incorporating detachment and degradation into the mass-action model”, I was trying to understand the effect of loading density of the cargo. Specifically,if ui is large and the desired ui* is small, surely the system shouldgive a very rapid convergence to the target ui*? In other words, if thereis a huge amount of cargo available and going past, then one can quicklyobtain what one needs in any location to a high degree of accuracy. Itseems to me that the loading term should also play a role in the analysis on

Figures 5 and 6. Thus the 'slow detachment' case could actually be fastin absolute time terms if one were to factor in lots of available cargo.

I do not see this factor in the analysis in the subsection “Conservative experimental estimates of trafficking parameters suggest that the tradeoff between speed and specificity is severe”.

Reviewer #2:

In this manuscript, the authors developed a theoretical model for transport of cargoes on microtubules. Analytical solutions of the model show that such transport can either be fast or precise but not both. (Precision in this case means similarity to target cargo concentration at the destination.) In particular, the authors considered two different transport schemes were considered: (1) specific transport, uniform detachment, and (2) uniform transport, specific detachment.

1) A consequence of the first transport scheme is that bottlenecks will occur with the same probability in the main dendrites and the subsequent branch dendrites, since the rate constants within the whole neuron are modeled by the same function. However, it is reasonable to ask if neurons in reality do exhibit bottlenecks in the main dendrite and the branch/daughter dendrites at the same frequency.

2) Perhaps there could be more detailed studies of transports using a combination of these two transport schemes (Figure 4E). For example, will an intermediate strategy improve speed and precision, i.e., can a scheme involving intermediate transport-specificity and intermediate detachment-specificity circumvent the problems of bottlenecks and cargo leakage? Perhaps a phase space plot that illustrates the effect of the combinations of schemes on accuracy and transport time may help to conveythe information better.

Reviewer #3:

The manuscript by Williams applies a "sushi-belt delivery model" to cargo transport In CA1 pyramidal neurons. The goal is to understand the tradeoff between speed versus precision during cargo transport along microtubules by motor proteins. The manuscript opens with a rather general discussion (mass-action model) of convection-diffusion in a channel that is coarse-grained at the level of adjacent boxes. This idea is extended to model pyramidal neurons where the steady state distribution of cargo is calculated w.r.t. a target profile. The authors then model a bottleneck situation by assuming low cargo transition rates (epsilon) into a compartment, and test how the system converges to steady state as a function of epsilon. The model is taken further by introducing detachment from microtubules (possibly followed by diffusion-recapture – details unclear), and looking at efficiency of transport under two possibilities – cargo is selectively transported to target or is uniformly distributed (combined with detachment).

The goal is laudable because it attempts to present a generalized and simple mathematically solvable coarse-grained description of cargo localization in a complex neuronal geometry. Most of the assumptions of the mathematical model appear valid, their rate constants seem to match the experimental velocities and they seem to have taken into consideration various scenarios during cellular transport. However, we feel that the paper starts off being rather general, and remains more-or-less so till the end. For example, Figures 4C-D show that the target cargo distributions are always achieved irrespective of the transport/detachment ratio. What is one expected to learn from this, and how might it be useful to plan future experiments? If the message is that many strategies can be employed to achieve target distributions, then this is a rather weak message unless this theme is developed further with specific examples and suggestions. Similarly, the observation (subsection “Convergence rate”, last paragraph) that transport will achieve steady state faster if bottlenecks are removed – why is this surprising? This part is followed up by a few poorly explained lines where the results (Figure 3F) seem interesting, but are obscured by unnecessary usage of complicated Latin words. On the same lines, in the places where it is mentioned, the connection to experiments is rather weak. Whether these assumptions hold true in a biological setting has not been tested for any neuronal cargoes. Live imaging to show that at least a few cargoes follow this model would have helped.

The authors talk about detachment and degradation of cargoes. But how does reloading of cargoes occur in instances when continuous supply is required?

The authors suggest using their model that accurate transport is slower, and faster rates of transport requires much greater complexity and is very sensitive to perturbations. This is hard to visualize in case of most neuronal functions where efficient robust and rapid signaling does occur during processes such as long term memory formation, signaling at the synapse etc. Again, there appears to be a disconnection between real biology and the model.

Taken together, we feel that this work would not have sufficient impact to warrant publication in eLife. This is in contrast to models of microtubule transport (e.g. Lipowsky group PNAS paper) which have made more specific mechanistic predictions that advanced the field and inspired new experiments. We suggest the authors also improve the writing of this manuscript in consultation with some experimental colleagues. Perhaps addition of some experiments as preliminary tests of models would also help.

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for submitting your article "Dendritic trafficking faces physiologically critical speed-precision tradeoffs" for consideration by eLife. Your article has been favorably evaluated by Naama Barkai (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors. The following individual involved in review of your submission has agreed to reveal their identity: Ambarish Kunwar (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The reviewers all felt that the paper was much improved from the earlier version. They made some small suggestions for minor improvements and clarifications, not requiring further review.

Summary:

In this study Williams et al. explore simulations of the 'sushi-belt' family of models, including local signals to unload cargo. They use deterministic methods after comparing with some preliminary stochastic calculations. They embed the model into a detailed neuronal morphology. The authors exercise the model on some not-so-obvious predictions such as speed and accuracy tradeoffs.

Essential revisions:

1) I'm surprised that the feedback and cargo recycling processes do not bring rapid settling to the system without large cargo excess. I think this is one of the key findings of the paper. I would suggest that the authors move some of the panels from Figure 5—figure supplement 2 into the main body of the paper, so as to better present this result.

2) The authors have based their entire simulation on a real life neuron (CA1 Pyramidal Cell) with a fixed number of compartments (742). It would be good if the authors throw some light on (i) how sensitive their simulations are to the number of compartments in the neuron, and (ii) how the compartment size is related to the cargo size.
