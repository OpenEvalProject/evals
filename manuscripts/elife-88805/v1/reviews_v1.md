# Peer review - Round 1

Editors:
- Upinder S Bhalla, National Centre for Biological Sciences India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.88805.3.sa0](https://doi.org/10.7554/eLife.88805.3.sa0)

The authors provide a valuable analysis of what neural circuit mechanisms enable varying the speed of retrieval of sequences, which is needed in situations such as reproducing motor patterns. Their use of heterogeneous plasticity rules to allow external currents to control speed of sequence recall is a novel alternative to other mechanisms proposed in the literature. They perform a convincing characterization of relevant properties of recall via simulations and theory, though a better mapping to biologically plausible mechanisms is left for future work.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88805.3.sa1](https://doi.org/10.7554/eLife.88805.3.sa1)

While there are many models for sequence retrieval, it has been difficult to find models that vary the speed of sequence retrieval dynamically via simple external inputs. While recent works have proposed some mechanisms, the authors here propose a different one based on heterogeneous plasticity rules. Temporally symmetric plasticity kernels (that do not distinguish between the order of pre and post spikes, but only their time difference) are expected to give rise to attractor states, asymmetric ones to sequence transitions. The authors incorporate a rate-based, discrete-time analog of these spike-based plasticity rules to learn the connections between neurons (leading to connections similar to Hopfield networks for attractors and sequences). They use either a parametric combination of symmetric and asymmetric learning rules for connections into each neuron, or separate subpopulations having only symmetric or asymmetric learning rules on incoming connections. They find that the latter is conducive to enabling external inputs to control the speed of sequence retrieval.

Comments on revised version:

The authors have addressed most of the points of the reviewers.

A major substantive point raised by both reviewers was on the biological plausibility of the learning.

The authors have added a section in the Discussion. This remains an open question, however the discussion suffices for the current paper.
