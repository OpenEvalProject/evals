# Peer review - Round 1

Editors:
- Sandeep Krishna, National Centre for Biological Sciences­‐Tata Institute of Fundamental Research India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.92093.3.sa0](https://doi.org/10.7554/eLife.92093.3.sa0)

This useful manuscript explores conditions for epigenetic inheritance by studying the stability of simple network models to permanent and transient perturbations. A novel aspect of the study is that it unifies non-genetic inheritance phenomena across cell divisions of unicellular organisms and in the germline of multicellular organisms. However, the models studied are more a collection of vignettes of numerical studies than a systematic study, therefore the evidence presented remains incomplete. As a first step towards building a more systematic theoretical framework, this work will be of interest to colleagues in the field of epigenetic inheritance.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.92093.3.sa1](https://doi.org/10.7554/eLife.92093.3.sa1)

The author studies a family of models for heritable epigenetic information, with a focus on enumerating and classifying different possible architectures. The key aspects of the paper are:

- Enumerate all 'heritable' architectures for up-to 4 constituents.

- A study of whether permanent ("genetic") or transient ("epigenetic") perturbations lead to heritable changes

- Enumerated the connectivity of the "sequence space" formed by these heritable architectures

- Incorporating stochasticity, the authors explore stability to noise (transient perturbations)

- A connection is made with experimental results on C elegans.

The study is timely, as there is a renewed interest in the last decade in non-genetic, heritable heterogeneity (e.g., from single-cell transcriptomics). Consequently, there is a need for a theoretical understanding of the constraints on such systems. There are some excellent aspects of this study: for instance, the attention paid to how one architecture "mutates" into another. Unfortunately, the manuscript as a whole does not succeed in formalising nor addressing any particular open questions in the field. Aside from issues in presentation and modelling choices (detailed below), it would benefit greatly from a more systematic approach rather than the vignettes presented.

## Terminology

The author introduces a terminology for networks of interacting species in terms of "entities" and "sensors" -- the former being nodes of a graph, and the latter being those nodes that receive inputs from other nodes. In the language of directed graphs, "entities" would seem to correspond to vertices, and "sensors" those vertices with positive indegree and outdegree. Unfortunately, the added benefit of redefining accepted terminology from the study of graphs and networks is not clear.

## Model

The model seems to suddenly change from Figure 4 onwards. While the results presented here have at least some attempt at classification or statistical rigour (i.e. Fig 4 D), there are suddenly three values associated with each entity ("property step, active fraction, and number"). Furthermore, the system suddenly appears to be stochastic. The reader is left unsure what has happened, especially after having made the effort to deduce the model as it was in Figs 1 through 3. No respite is to be found in the SI, either, where this new stochastic model should have been described in sufficient detail to allow one to reproduce the simulation.

## Perturbations

Inspired especially by experimental manipulations such as RNAi or mutagenesis, the author studies whether such perturbations can lead to a heritable change in network output. While this is naturally the case for permanent changes (such as mutagenesis), the author gives convincing examples of cases in which transient perturbations lead to heritable changes. Presumably, this is due the the underlying multistability of many networks, in which a perturbation can pop the system from one attractor to another.

Unfortunately, there appears to be no attempt at a systematic study of outcomes, nor a classification of when a particular behaviour is to be expected. Instead, there is a long and difficult-to-read description of numerical results that appear to have been sampled at random (in terms of both the architecture and parameter regime chosen). The main result here appears to be that "genetic" (permanent) and "epigenetic" (transient) perturbations can differ from each other -- and that architectures that share a response to genetic perturbation need not behave the same under an epigenetic one. This is neither surprising (in which case even illustrative evidence would have sufficed) nor is it explored with statistical or combinatorial rigour (e.g. how easy is it to mistake one architecture for another? What fraction share a response to a particular perturbation?)

As an additional comment, many of the results here are presented as depending on the topology of the network. However, each network is specified by many kinetic constants, and there is no attempt to consider the robustness of results to changes in parameters.

## DNA analogy

At two points, the author makes a comparison between genetic information (i.e. DNA) and epigenetic information as determined by these heritable regulatory architectures. The two claims the author makes are that (i) heritable architectures are capable of transmitting "more heritable information" than genetic sequences, and (ii) that, unlike DNA, the connectivity (in the sense of mutations) between heritable architectures is sparse and uneven (i.e. some architectures are better connected than others).

In both cases, the claim is somewhat tenuous -- in essence, it seems an unfair comparison to consider the basic epigenetic unit to be an "entity" (e.g., an entire transcription factor gene product, or an organelle), while the basic genetic unit is taken to be a single base-pair. The situation is somewhat different if the relevant comparison was the typical size of a gene (e.g., 1 kb).
