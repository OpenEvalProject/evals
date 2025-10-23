# Peer review - Round 1

Editors:
- Tatyana O Sharpee, Salk Institute for Biological Studies United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.101506.3.sa0](https://doi.org/10.7554/eLife.101506.3.sa0)

This paper provides a useful systematic quantification of the relationship between electrophysiological response properties of single neurons with their position in the brain. The quality of the classification setup is high and the methodology is solid.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.101506.3.sa1](https://doi.org/10.7554/eLife.101506.3.sa1)

Summary:

The paper by Tolossa et al. presents classification studies that aim to predict the anatomical location of a neuron from the statistics of its in-vivo firing pattern. They study two types of statistics (ISI distribution, PSTH) and try to predict the location at different resolutions (region, subregion, cortical layer).

Strengths:

This paper provides a systematic quantification of the single-neuron firing vs location relationship.

The quality of the classification setup seems high.

The paper uncovers that, at the single neuron level, the firing pattern of a neuron carries some information on the neuron's anatomical location, although the predictive accuracy is not high enough to rely on this relationship in most cases.

Weaknesses:

As the authors mention in the Discussion, it is not clear whether the observed differences in firing is epiphenomenal. If the anatomical location information is useful to the neuron, to what extent can this be inferred from the vicinity of the synaptic site, based on the neurotransmitter and neuromodulator identities? Why would the neuron need to dynamically update its prediction of the anatomical location of its pre-synaptic partner based on activity when that location is static, and if that information is genetically encoded in synaptic proteins, etc (e.g., the type of the synaptic site)? Note that the neuron does not need to classify all possible locations to guess the location of its pre-synaptic partner because it may only receive input from a subset of locations. Ultimately, the inability to dissect whether the paper's findings point to a mechanism utilized by neurons or merely represent an epiphenomenon is the main weakness of the curious, though somewhat weak, observations described in this paper.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.101506.3.sa2](https://doi.org/10.7554/eLife.101506.3.sa2)

Summary:

In this manuscript, Tolossa et al. analyze Inter-spike intervals from various freely available datasets from the Allen Institute and from a dataset from Steinmetz et al.. They show that they can modestly decode between gross brain regions (Visual vs. Hippocampus vs. Thalamus), and modestly separate sub areas within brain regions (DG vs. CA1 or various visual brain areas). The core result is that a multi-layer perceptron trained on the ISI distributions can modestly classify different brain areas and perhaps in a reasonably compelling way generalize across animals. The result is interesting but the exact problem formulation still feels a tad murky to me because I am worried the null is a strawman and I'm unsure if anyone has ever argued for this null hypothesis ("the impact of anatomy on a neuron's activity is either nonexistent or unremarkable"). Given the patterns of inputs to different brain areas and the existence of different developmental origin and different cell types within these areas, I am unclear why this would be a good null hypothesis. Nevertheless, the machine learning is reasonable, and the authors demonstrate that a nonlinear population based classifier can pull out reasonable information about the brain area and layer.

Strengths:

The paper is reasonably well written, and the definitions are quite well done. For example, the authors clearly explained transductive vs. inductive inference in their decoders. E.g., transductive learning allows the decoder to learn features from each animal, whereas inductive inference focuses on withheld animals and prioritizes the learning of generalizable features. The authors walk the reader through various analyses starting as simply as PCA, then finally showing a MLP trained on ISI distributions and PSTHs performs modestly well in decoding brain area. The key is ISI distributions work well in inductive settings for generalizing from one mouse to the other.

Weaknesses:

As articulated in my overall summary, I still found the null hypothesis a tad underwhelming. I am not sure this is really a valid null hypothesis ("the impact of anatomy on a neuron's activity is either nonexistent or unremarkable"), although in the statistical sense it is fine. The authors took on board some of the advice from the first review and clarified the paper but there are portions that are unnecessarily verbose (e.g., "Beyond fundamental scientific insight, our findings may be of benefit in various practical applications, such as the continued development of brain-machine interfaces and neuroprosthetics"). Also, given that ISIs cannot separate between visual areas, why is the statement that these are conserved. I still find it somewhat underwhelming that the thalamus, hippocampus , and visual cortex have different ISI distributions. Multiple researchers have reported similar things in cortex perhaps without the focus on decoding area from these ISI distributions.

All in all, it is an interesting paper with the notion that ISI distributions can modestly predict brain area and layer. It could have some potential for a tool for neuropixels, although this needs to be developed further for this use case.
