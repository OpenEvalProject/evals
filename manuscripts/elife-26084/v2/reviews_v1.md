# Peer review - Round 1

Editors:
- Michael J Frank, Brown University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.26084.010](https://doi.org/10.7554/eLife.26084.010)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Learning multiple variable-speed sequences in striatum via cortical tutoring" for consideration by eLife. Your article has been favorably evaluated by Richard Ivry (Senior Editor) and two reviewers, one of whom, Michael Frank, is a member of our Board of Reviewing Editors. The following individual involved in review of your submission has agreed to reveal their identity: Mark D Humphries (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors propose a model for how the striatum can generate sequences of neuron activity, of variable duration, from non-sequential input, and how they can emerge from tutoring from cortex, and can progress at varying speeds. Their mechanism rests on some form of adaptation – here picked to be synaptic depression at MSN-MSN synapses, given this has existing experimental evidence. With adaptation as the mechanism, dilation of temporal sequences can occur solely through changing the level of input drive. Learning such sequences is proposed to occur via anti-Hebbian plasticity at MSN-MSN synapses. Finally, the authors show that their results generalise to a sparse, spiking network model. Thus, the model makes sense of biophysical data (synaptic depression), shows how it can explain experimental data on population dynamics, and makes clear, testable experimental predictions.

Essential revisions:

Both reviewers were quite enthusiastic about your contribution, but just wanted to see you address the following points.

1) We would like to know a bit more about the dependencies of the model's behaviour on its parameters, particularly for learning. These can take the form of further text, or small simulations – we will defer to your preference here. Specifically, the tutoring (Figure 4) requires that the input sequence is periodically repeated; presumably the time-scale of the period of the sequence has to be >> τy? What is the lower-limit here? In other words, how does the time-scale of interaction between neurons set by τy dictate the fastest period of the tutoring sequence? Presumably this is also a function of xin, just as for the switch time in the constant input case to the static network (Figure 1D).

2) Currently learning in the model is mediated by anti-Hebbian plasticity. The authors state in the Discussion that it still seems to be an open question as to whether this form of plasticity is appropriate for MSNs. Are there other learning rules that might also work for the model? Have the authors tried other learning rules? It might be nice to see more work or at least a discussion of potential alternative learning rules should the prediction of anti-Hebbian plasticity prove to be not well supported experimentally. This is not a criticism but rather something that is likely of interest to readers.
