# Peer review - Round 1

Editors:
- Audrey Sederberg, https://ror.org/01zkghx44 Georgia Institute of Technology United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.99904.3.sa0](https://doi.org/10.7554/eLife.99904.3.sa0)

This study presents numerical results on a framework for understanding the dynamics of subthreshold waves in a network of electrical synapses modeled on the connectome data of the C elegans nematode. The strength of the evidence presented in favor of interference effects being a major component in subthreshold wave dynamics is inadequate and the approach is flawed. Substantial methodological issues are present, including altering the original network structure of the connectome without a clear justification and providing little motivation for the choice of numerical parameters values that were used.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.99904.3.sa1](https://doi.org/10.7554/eLife.99904.3.sa1)

Summary:

This work investigates numerically the propagation of subthreshold waves in a model neural network that is derived from the C. elegans connectome. Using a scattering formalism and tight-binding description of the network -- approximations which are commonplace in condensed matter physics -- this work attempts at showing the relevance of interference phenomena, such as wavenumber-dependent propagation, for the dynamics of subthreshold waves propagating in a network of electrical synapses.

Strengths:

The primary strength of the work is in trying to use theoretical tools from a far-away corner of fundamental physics to shed light on the properties of a real neural system.

Weaknesses:

The authors provide a good introduction and motivation for studying the propagation of subthreshold oscillations in the inferior olive nuclei. However, they chose to use the C elegans connectome for their study, and the implications of this work for C elegans neuroscience remain unclear by the end of the preprint. The authors should also give more evidence for the claim that their study may give a mechanism for synchronized rhythmic activity in the mammalian inferior olive nucleus, or refrain from making this conclusion. In the same vein, since the work emphasizes the dependence on the wavenumber for the propagation of subthreshold oscillations, they should make an attempt at estimating the wavenumber of subthreshold oscillations in C elegans if they were to exist and be observed. Next, the presence of two "mobility edges" in the transmission coefficient calculated in this work is unmistakably due to the discrete nature of the system, coming from the tight-binding approximation, and it is unclear to me if this approximation is justified in the current system. Similarly, it is possible that the wavenumber-dependent transmission observed depends strongly on the addition of a large number of virtual nodes (VNs) in the network, which the authors give little to no motivation for. As these nodes are not present in the C elegans connectome, the authors should explain the motivation for their inclusion in the model and should discuss their consequences on the transmission properties of the network. As it stands, I think the work would only have a very limited impact on the understanding of subthreshold oscillations in the rat or in C elegans. Indeed, the preprint falls short of relating its numerical results to any phenomena which could be observed in the lab.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.99904.3.sa2](https://doi.org/10.7554/eLife.99904.3.sa2)

This manuscript addresses an interesting and important question: the basic mechanisms underlying subthreshold intrinsic oscillations in the inferior olive. Instead of a direct investigation of the questions, the authors decide to study subthreshold oscillations in the C-elegans, where the connectivity pattern is known but does not exhibit sub-threshold oscillations. Furthermore, instead of the common description of gap-junction coupling by resistors, the authors decide to represent the system as a tight-binding Anderson Hamiltonian.

Weaknesses:

The authors study an architecture of the C-elegans instead of that of the inferior olive of mammals because the architecture of C-elegans is known.

No subthreshold oscillations were identified in the C-elegans.

Instead of representing electrical coupling via resistors that connect neurons, the authors use a quantum formalism and introduce the tight-binding Anderson Hamiltonian. Why?

Equally spaced two virtual nodes were added between cells connected by a gap junction. Why?

Comments on revised version:

Last time, I recommended that the authors should represent electrical coupling via resistors that connect neurons instead of via the quantum formalism. The authors have not tested this direction.
