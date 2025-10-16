# Peer review - Round 1

Editors:
- Tatjana Tchumatchenko, University Medical Center of the Johannes Gutenberg University Mainz Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.88777.3.sa0](https://doi.org/10.7554/eLife.88777.3.sa0)

The present study offers valuable insights into the emergence of oscillations in neural networks. It underscores the importance of achieving a delicate balance between excitatory and inhibitory links, and deals with the topological conditions for oscillations. The study provides solid evidence in simple networks based on formal mathematical theory and advanced simulations, but the wider implications to biological networks would require a more detailed investigation into delays and nonlinearities.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88777.3.sa1](https://doi.org/10.7554/eLife.88777.3.sa1)

Summary:

Authors study appearance of oscillations in motifs of linear threshold systems, coupled in specific topologies. They derive analytically conditions for appearance of oscillations, in the context of excitatory and inhibitory links. They also emphasize the higher importance of the topology, compared to the strength of the links, though it is not straightforward to apply this for brain networks where the weights can be distributed several orders of magnitude. Finally the results are confirmed with WC oscillators. The findings are to some extent confirmed with spiking neurons, though here results are less clear.

Overall, the results are sound from a theoretical perspective, but I still find hard to believe that they are of significant relevance for biological networks, or in particular for the oscillations of BG-thalamus-cortex loop in PD. I find motifs in general to be too simplistic for multiscale and generally large networks as it is the case in the brain. Moreover, the division on regions is more or less arbitrary by definition, and having such a strong dependence on odd/even number of inhibitory links is far from reality. Another limitation is the fact that the cortex is considered as a single node. Similarly, decomposing even such a coarse network in all possible (238 in this case) motifs doesn't seem of much relevance, when I'd assume that the emergence of pathological rhythms is more of an emergent phenomena.

Strengths:

From the point of nonlinear dynamics, the results are solid, and the intuition behind the proofs of the theorems is well explained.

Weaknesses:

As stated in the summary, I find the work to be too theoretical without a real application for the brain dynamics, where the networks are generally very large. The odd/even number rule is too strict, and talking about fixed and definite number of cycles in actual brain seems too simplistic. Moreover, the cortex is considered as a single node, and finally the impact of the delays is ignored even though they define the synchronizability of the brain network, and previous works on the amplitude reduction due to the time-delays in difference-coupled networks of oscillators is not mentioned.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88777.3.sa2](https://doi.org/10.7554/eLife.88777.3.sa2)

The authors present here a mathematical and computational study of the topological/graph theory requirements to obtain sustained oscillations in neural network models. A first approach mathematically demonstrates that, for a given network of interconnected neural populations (understood in the sense of dynamical systems) requires an odd number of inhibitory populations to sustain oscillations. The authors extend this result via numerical simulations of (i) a simplified set of Wilson-Cowan networks, (ii) a simplified circuit of the cortico-basal ganglia network, and (iii) a more complex, spike-based neural network of basal ganglia network, which provides insight on experimental findings regarding abnormal synchrony levels in Parkinson's Disease (PD).

The work elegantly and effectively combines a solid mathematical proof with careful numerical simulations at different levels of description, which is uncommon and provides additional layers of confidence to the study. Furthermore, the authors included detailed sections to provide intuition about the mathematical proof, which will be helpful for readers less inclined to the perusal of mathematical derivations. Its insightful and well-informed connection with a practical neuroscience problem, the presence of strong beta rhythms in PD, elevates the potential influence of the study and provides testable predictions.

In its updated form, the authors have solved the most pressing issues of the study, by acknowledging the limitations of their work regarding the effects of delays in oscillations, and addressing some of these effects in new simulations. Although some interesting simulations are still not presented in the revised version, they could constitute the focus of future work to complement the conclusions presented here. The absence of explanations for some of the figures and panels has been corrected, and the issues with grammar and lack of clarity have been improved. This important work is therefore now improved.
