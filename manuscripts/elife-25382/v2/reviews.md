# Peer review - Round 1

Editors:
- Frances K Skinner, University Health Network , Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.25382.016](https://doi.org/10.7554/eLife.25382.016)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Ionic Mechanisms Underlying History-Dependence of Conduction Delay in an Unmyelinated Axon" for consideration by eLife. Your article has been favorably evaluated by Eve Marder (Senior Editor) and three reviewers, one of whom, Frances K Skinner (Reviewer #1), is a member of our Board of Reviewing Editors. The following individual involved in review of your submission has agreed to reveal their identity: Jeremy Niven (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this manuscript the authors examine action potential biophysics and use computational modelling to assess the history-dependence of conduction delay, as motivated by an unmyelinated invertebrate axon. The manuscript is well-written and well-organized with rationale, logic and motivation clearly presented. The reviewers felt that it should be of interest to neuroscientists from a variety of backgrounds, including those interested in the biophysics and those interested in neural coding and neuropathies. They use parameter screening and NEURON simulations to present findings that can explain the slow time scale via Ih and Na-K pump dynamics along with an empirical equation that can be obtained by a nonlinear combination of peak and threshold potentials.

Essential revisions:

While the manuscript itself was clear, some concerns regarding resting and reversal potentials were raised as well as the need for better explanations in some places. Specifically:

1) The authors mention that they have fixed the reversal potential of K+ in the axon model to -70 mV to prevent the occurrence of an after-hyperpolarisation. Have they checked whether this will affect any of their conclusions? We appreciate that they state that the after-hyperpolarisation is missing from axonal recordings of APs but this could be due to leaky recordings, or recordings being made in passive regions of an otherwise active axon (as occurs just prior to the output synapses in some arthropod neurons). It may be worth checking that the results are robust to a shift of the K+ reversal potential to something more conventional for an arthropod neuron such as -80 or -85 mV.

2) Near the beginning of the Results section the authors spend some time discussing whether the slow effects they observe could be reproduced by a K+ conductance rather than the Na+/K+ ATPase. I was a little concerned that this might appear to be a bit of a straw-man argument. The two will not be equivalent because of the time constants governing their dynamics, and because only in one case is the current accompanied by a conductance change. Surely, the choice of sufficiently long time constants would allow a voltage-gated conductance to replace the ATPase as long as the reversal potential was correct?

Could this be further examined as a novel mechanistic explanation to consider that the observation that the pump state is a more potent determinant of velocity than a similarly slow K conductance? Perhaps this could lead to an experimentally testable distinction of the two potential mechanisms. The present treatment in the manuscript is restricted to effects in line with the previous experimental work. This is not required for the present revision, but the authors may wish to consider this.

3) The origin of the resting and reversal potential/s in the model was a bit confusing. The K+ reversal potential is set to -70 mV and the Ih reversal potential presumably represents a mixed conductance of K+ and Na+ ions, but what happens to change this mixed conductance (and the reversal potential) in the presence of dopamine? Is the leak set to -65 mV to match the observed resting potential and, if so, is there experimental evidence to support such a depolarising leak in these neurons?

4) The sensitivity analysis description could be expanded to be more clear since it is a bit confusing as it stands given the earlier results/statements. For example, STS is mediated by Ipump, but they then show that gh has a strong effect, whereas the sensitivity analysis shows other parameters have important contributions. Similarly, FTS is not only affected by Ih but also by Ipump and much by EK and the sensitivity analysis shows only a comparatively weak effect of gh. Instead of the conclusions reached in the text, it looks like it is either a complex problem with many covariates, or the simple determinant has not been correctly identified. Presumably this is because one is looking at parameter sensitivity and not sensitivity to Ih itself, as stated toward the end of the section, but would perhaps be more helpful if this is stated more up front along with an expanded description to avoid confusion.

5) The authors are encouraged to expand their empirical equation discussion to have a wider appeal, perhaps in terms of a strategy. That is, if new currents were added/considered in the system and the consideration of time scale, how would one proceed?
