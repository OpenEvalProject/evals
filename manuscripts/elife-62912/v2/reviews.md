# Peer review - Round 1

Editors:
- Srdjan Ostojic, Ecole Normale Superieure Paris France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.62912.sa1](https://doi.org/10.7554/eLife.62912.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The half-century research on synaptic plasticity has primarily focused on how neural activity gives rise to changes in synaptic connections, and how these changes underlie learning and memory. However, recent studies have shown that in fact, most of the synaptic changes are activity-independent. This result is surprising given the generally held belief that activity-dependent changes in connectivity underlie network functionality. This manuscript proposes a theoretical explanation of why this should be the case. Specifically, this work presents a mathematical analysis of the amount of synaptic plasticity required to maintain learned circuit function in presence of random synaptic changes. The central finding, supported by simulations, is that for an "optimal" learning algorithm that rectifies random changes in connectivity, task-related plasticity should generally be smaller than the magnitude of the fluctuations. All reviewers agreed that this is a very interesting theoretical perspective on an important biological problem.

Decision letter after peer review:

Thank you for submitting your article "Optimal synaptic dynamics for memory maintenance in the presence of noise" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Timothy Behrens as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Yonatan Loewenstein (Reviewer #2); Matthias H Hennig (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The half-century research on synaptic plasticity has primarily focused on how neural activity gives rise to changes in synaptic connections, and how these changes underlie learning and memory. However, recent studies have shown that in fact, most of the synaptic changes are activity-independent. This result is surprising given the generally held belief that activity-dependent changes in connectivity underlie network functionality. This manuscript proposes an explanation of why this should be the case.

Specifically, this work presents a mathematical analysis of the amount of synaptic plasticity required to maintain learned circuit function in presence of random synaptic changes. The central finding, supported by simulations, is that for an "optimal" learning algorithm that rectifies random changes in connectivity, task-related plasticity should generally be smaller than the magnitude of the fluctuations.

All reviewers agreed that this is a very interesting perspective on an important biological problem. However the reviewers have had difficulties fully understanding the specific claim, its derivation and potential implications. These issues are detailed in the Main Comments below, and need to be clarified. Additional suggestions are summarised in Other Comments.

Main comments:

1. How much does the main claim depend on the assumed learning algorithm? What is the family of learning algorithms that the authors refer to as "optimal" that have the property that directed changes are smaller in their magnitude than the noise-driven changes?

The reviewers' current understanding is the following, please clarify whether it is correct:

A) If the learning algorithm simply backtracks the noise, then the magnitude of learning-induced changes will be trivially equal that of the noise-induced changes. An optimal algorithm will not be worse than this trivial one.

B) If the learning algorithm (slowly) goes in the direction of the gradient of the objective function then (1) if the network is in a maximum of the objective function and changes are small then the magnitude of learning-induced changes will be equal to that of the noise-induced changes; (2) if the network is NOT in a maximum of the objective function then unless the noise is in the opposite direction to the gradient, the learning-induced path to the same level of performance would be shorter. Thus, the magnitude of learning-induced changes would be smaller that of that of the noise-induced changes

C) There exist (inefficient) learning algorithms such that the magnitude of the learning-induced changes are larger than the magnitude of the noise-induced ones. A learning algorithm that overshoots because of a too-large learning rate could be one of them, and it is trivial to construct other inefficient learning algorithms.

2. The reviewers have found the mathematical derivation in the main text difficult to follow, in part because it seems to use an unnecessarily complex set of mathematical notations and arguments. The reviewers suggest to focus on intuitive arguments in the main text, to make the arguments more transparent, and the paper more accessible to the broad neuroscience audience. Ultimately, this is up to authors to decide. In any case, the main arguments need to be clarified as laid out above.

3. The reviewers were not convinced by the role played by the numerical simulations. On one hand, it was not clear what the simulations added with respect to the analytical derivations. Is the purpose to check any specific approximation? On the other hand, the model does not seem to help link the derivations to the original biological question, as it is quite far removed from a biological setup. A minimal suggestion would be to use the model to illustrate more directly the geometric intuition behind the derivation, for instance by showing movements of weights along with some view of the gradient, contrasting optimal and sub-optimal.

Other comments:

4. The whole argument rests on an assumption that biological networks optimise a cost function, in particular during reconsolidation. How that assumption applies to the experimental setups detailed in the first part is unclear. At the very least, a clear statement and motivation of this assumption is needed.

5. One of the reviewers was not convinced (but happy to debate) cellular noise is such a major contributor to synaptic changes as stated in the introduction and in Table 1, as silencing neural activity pharmacologically will almost certainly affect synaptic function strongly. Strong synapses (big spines) tend to be more stable, and in any case it would be very difficult to know which of the observed modifications reported in the referenced papers have functional consequences. It would be very interesting to see what turnover (or weight dynamics) this model would predict under optimal and non-optimal conditions. In Figure 1 it is implied that weight changes continues unchanged in presence of noise (and optimal learning to maintain the objective), is this actually the case? What concrete experimental predictions the authors would (dare to) make?

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Optimal plasticity for memory maintenance in the presence of synaptic fluctuations" for further consideration by eLife. Your revised article has been evaluated by Timothy Behrens (Senior Editor) and a Reviewing Editor.

All reviewers have found that the manuscript has been very much improved and should be eventually published. The reviewers now fully understand the mathematical framework and the main mathematical result. During the consultation, it has however appeared that all reviewers feel that the main message of the manuscript, and in particular its implications for biology, need to be further clarified. Two main issues remain, which we suggest should be either addressed in the Results section or discussed in detail:

1. How much do the results rely on the assumption that synaptic changes are "strong"? To what extent is this assumption consistent with experiments? Is this theoretical framework really needed when infinitesimally small noise is immediately corrected by a learning signal, as often assumed (see below for more details)? Is the main result trivial when changes are small? Is the main contribution is to show that the result also holds far from this trivial regime, when noise and corrections are large?

2. what are the implications of the main mathematical result for interpreting measurable experimental quantities? The relation with experiments listed in the Discussion seems rather indirect (eg on lines 330-335 the interpretations of EM reconstructions in the authors' modelling framework seems unclear; it would be worth unpacking how the papers listed on lines 347-348 are consistent with the main result). Moreover, in many of the panels shown in Figures5-6, the dependence of the loss on the ratio between compensatory plasticity and synaptic fluctuations is rather flat; what does this imply for experimental data?

More details on the first point from one of the reviewers:

When studying learning in neuronal networks, the underlying assumption is always ("always" to the best of my knowledge) that learning-induced changes are gradual. For example, some form of activity-dependent plasticity has, on average, a negative projection on the gradient of the loss function of the current state. Small changes to synaptic efficacies are made and now the network is in a slightly different (improved) state. Activity-dependent plasticity in that new state has, again, a negative projection on the (new) gradient of the loss function at the new state, etc. If learning is sufficiently slow, we can average over the stochasticities in the learning process, organism's actions, rewards etc. and learning will improve performance.

In contrast to this approach, this paper suggests a very different learning process: activity-independent "noise" induces a LARGE change in the synaptic efficacies. This change is followed by a SINGLE LARGE compensatory learning-induced change. The question addressed in this manuscript is how large should this single optimal compensatory learning-induced change be relative to the single noise-induced change. The fact that the compensatory changes are not assumed to be small and that learning is done in a single step, rather than learning being gradual, allowing the local sampling of the loss function, complicates the mathematical analysis. While for analyzing infinitesimally-small changes we only need to consider the local gradient of the loss function, higher-order terms are required when considering single large changes.

What is the justification to this approach given that gradual learning is what we seem to observe in the experiments, specifically those cited in this manuscript? There is a lot of evidence of gradual changes in numbers of spines or synaptic efficacies, etc. If everything is gradual, why not "recompute" the gradient on the fly as is done in all previous models of learning?
