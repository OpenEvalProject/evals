# Peer review - Round 1

Editors:
- Peter Latham, University College London , United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.13824.014](https://doi.org/10.7554/eLife.13824.014)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your work entitled "Neural oscillations as a signature of efficient coding in the presence of synaptic delays" for consideration by eLife. Your article has been favorably evaluated by Timothy Behrens as the Senior editor and three reviewers, one of whom is a member of our Board of Reviewing Editors.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors have previously shown that a an optimal error correcting code requires a balanced excitatory (E) and inhibitory (I) network, where a spike occurs only to reduce the error between a network estimate and the true stimulus. In that previous work, feedback was instantaneous. Here the authors show that if feedback is delayed (as it must be in realistic networks), oscillations develop. However, excessive synchronous network oscillations degrades coding. The central result of the manuscript is that noise mitigates some of the deleterious aspects of network-wide oscillatory synchrony on neural coding.

Essential revisions:

1) Some features of the result will naturally depend on the readout time constant τ. The only place I see its value mentioned is in connection with Figure 2 (subsection "Simulation parameters", first paragraph). There it says that τ was 100 ms. Was this value also used in the later simulations? It seems rather a large value to want to associate with a membrane time constant, so I think it would be useful if the authors said something about how this filtering might be implemented biologically. And what would the results look like if τ had a value more like a typical membrane time constant?

2) How sensitive are the results to the parameters of the network? In particular, how do they scale with network size, and with the ratio of excitatory to inhibitory neurons? In particular, when the network is scaled up and the ratio of excitatory to inhibitory neurons is set to a more realistic value, like 4, what happens to the following:

A) Does the optimal noise (Figure 4c) stay at 15 mV? And does the ratio of the optimal RMS error to the Poisson RMS error stay the same?

B) Does the optimal failure probability stay at about 0.5? And does the ratio of the optimal RMS error to the Poisson RMS error (which should be shown in that figure) stay the same?

C) Do the oscillation frequencies stay in the 30-50 Hz range?

D) Do the oscillation frequencies depend most strongly on the delay, or on other network parameters?

3) In the text referring to Figure 3(e), it would be good to explain why the rate in the performance-matched case is so high.

4) The fact that failures improves network performance may be one of the most interesting results in the paper, as it implies that failures are a feature, not a bug. We suggest that the paper would have more impact on the community if you emphasized this point, although we will leave that up to you.
