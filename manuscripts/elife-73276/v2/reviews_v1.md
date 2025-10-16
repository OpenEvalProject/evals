# Peer review - Round 1

Editors:
- Markus Meister, https://ror.org/05dxps055 California Institute of Technology United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73276.sa0](https://doi.org/10.7554/eLife.73276.sa0)

The article introduces a geometrical interpretation for the dynamics and function of certain spiking networks, based on the earlier work of Machens and Deneve. Given that spiking networks are notoriously hard to understand, the approach could prove useful for many computational neuroscientists. Here, that visualization tool serves to assess how fragile the network is to perturbation of its parameters, such as neuronal death, or spurious noise in excitation and inhibition.


---

# Peer review - Round 1

Editors:
- Markus Meister, https://ror.org/05dxps055 California Institute of Technology United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73276.sa1](https://doi.org/10.7554/eLife.73276.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Robustness in spiking networks: a geometric perspective" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Markus Meister as Reviewing Editor and Reviewer #3, and the evaluation has been overseen by Michael Frank as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Brent Doiron (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Domain of applicability:

1. The authors analyze a very specific network, with carefully tuned feedback designed for a specific cost function (Equation 3). Do such tuned networks exist in Nature? The reader would benefit from knowing what the domain of applicability really is.

2. How would the framework generalize to settings other than an auto-encoder, e.g., for the dynamical systems approach in Boerlin et al.?

Consistency of the bounding box picture:

3. A central assumption of the framework is a coherence between the readout from the network and the dynamics and connectivity of the network. This allows the bounding box to follow the input vector around, so one can easily assess decoding errors. However, it seems that some of the perturbations break the assumptions that lead to the bounding box. For example, exciting a single neuron decreases its threshold and thereby shrinks the bounding box (Figure 3D). As the bounding box limits the error in the readout, this should mean that the error decreases. However, the opposite is the case (Figure 4A). Presumably the discrepancy arises from changing the threshold without changing the readout at the same time, so the bounding box loses its meaning. By contrast the loss of a neuron, or its inhibition, leaves the remaining network adjusted properly, so the bounding box retains its meaning. The authors should address this question, and whether the bounding box loses its meaning under some perturbations and not others.

4. A related question applies to delays. Where exactly are the delays? In the readout and then the network is optimised for that? Or is the network the optimal one assuming no delays and then delays are added in the recurrent connections and/or the readout? Clarifying that will make it easier for the reader to follow the argument.

5. In the section on perturbations of the reset potential: Is there again an asymmetry, e.g., do changes up or down in the optimal reset potential have very different consequences?

Robustness claims:

6. There are frequent comparisons between networks with few neurons and networks with many neurons. The idea that networks with more neurons are more robust seems kind of obvious. But the authors analyze a very specific network tuned for coordinated redundancy (Equation 3). How does that network compare to one with the same number of neurons but no coordinated redundancy? This would seem a more interesting comparison than varying the number of neurons.

7. Intuitively one might expect that the performance is fragile to changes in the recurrent coupling, since the decoding vector is tied to the feedforward and recurrent weights (Equation 10). Because of this the claimed robustness to perturbations in synaptic weight seems surprising. Is the 'synapse scaling factor' in Figure 6G,H the parameter \δ_{\Omega} in Equation 17? The way it is defined it is the maximal change, however most synapses are perturbed to a much smaller extent. Also, for \δ approaching 0.2 the performance only drops by 20% (Figure 6G). However, for such large \δ's the firing rates in the network seem unreasonably high (Figure 6H), suggesting it no longer performs efficiently. Overall it is hard to judge from the current presentation how robust the network is to synaptic perturbation. Perhaps the firing rates could be bounded, or the performance penalized for using very high rates?

Relation to plasticity:

8. Prior work (e.g. Bourdoukan 2012) proposed a Hebbian learning process that could tune up such a network automatically. If this plasticity is "always on" how would it respond to the various perturbations being considered? How might that contribute to robustness on a longer time scale? How does the size/shape of the bounding box depend on the parameters of the learning rule? Can one get looser and tighter boxes, as needed here for certain types of robustness?
