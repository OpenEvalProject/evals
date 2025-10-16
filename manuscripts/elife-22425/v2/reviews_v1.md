# Peer review - Round 1

Editors:
- Mark CW van Rossum, University of Edinburgh United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.22425.017](https://doi.org/10.7554/eLife.22425.017)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "UP-DOWN cortical dynamics reflect state transitions in a bistable balanced network" for consideration by eLife. Your article has been favorably evaluated by Eve Marder (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors. The following individuals involved in review of your submission have agreed to reveal their identity: Benjamin Lindner (Reviewer #2); Brent Doiron (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This paper is devoted to further our understanding of up and down states in neural firing as observed in different brain states. Both novel experimental data and a simple yet novel computational rate model are presented allowing the authors to draw conclusions about the mechanism of up/down states and transitions between them.

The authors compare two possible mechanisms for the emergence of up/down states: (a) cellular adaptation that destabilizes each of the states on the time scale of seconds or (b) a true bistable situation, in which transitions between metastable states are triggered by external or internal fluctuations. Mechanism (a) seems to be at odds with their finding of little variation in the population rate when conditioned on the transition time. Also the high variability of the durations is more in line with a fluctuation-driven transition.

They then develop a simple computational model for the firing rates of excitatory and inhibitory subpopulations, which explain their experimental findings They predict a pronounced decline in the rate of the inhibitory neurons during the UP state and, by re-analyzing their data, can confirm this nontrivial prediction.

Overall, all reviewers thought this was a clearly written and solid study which, as it is an important contribution to basic cortical models, would interest a wider community, as the mechanism seems quite general.

Essential revisions:

One question is whether the conclusion would carry over directly to spiking networks. Did the authors search for the experimentally observed features also in a network of spiking neurons (one remark in the Discussion seems to indicate this)? Some of them have certainly great experience with these kinds of models and so it is not clear whether the features seen are difficult to achieve in a spiking-neuron model, or whether they are only typical for rate models. If the mechanisms illustrated are so basic that it would not be difficult to see them in a network of spiking neuron models, the authors could add one more figure illustrating this for the most salient features seen in their experimental data.

Figure 6 seems to be making the case that the up-down transitions seen in data are due to the fact that the cortex lives in the noise-induced transition state. However, in the model bifurcation diagram (Figure 5, panels A and B), we see that even the region where the up to down transition is adaptation induced rather than noise induced, it is still possible to get reasonable CVs for residence times in the up state (approx. 0.5). One would naively expect that as the transitions become more adaptation (rather than fluctuation) induced, the CV should shrink dramatically. However, that could be parameter dependent.

However since the CV can be high in the U to D adaptation regime it then begs the question: What would the analogue of Figure 6 panel A look like in that regime rather than the fully noise induced regime? Basically, Figure 6 currently provides some positive evidence for suggesting the U to D transitions should be noise induced, but no negative evidence that they shouldn't be adaptation induced.

In the Discussion the authors point out that Latham et al. developed a network model with adapting conductance-based point neuron models that displays transitions between a (practically silent) down state and a low-firing (0.2 Hz) up state, i.e. it achieves one goal of the simple rate model though in a more biophysically realistic setting. The authors point out that their own model is more 'parsimonious' and can reflect some of their own experimental findings. However, it was not clear to us whether the Latham-model would be able to show the same effects or not. The authors should add a statement on this point.
