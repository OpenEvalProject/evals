# Peer review - Round 1

Editors:
- Daniel Y Takahashi, Federal University of Rio Grande do Norte Brazil

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.89892.3.sa0](https://doi.org/10.7554/eLife.89892.3.sa0)

This valuable study provides an experimental paradigm and state-of-the-art analysis method for studying the existence of call types and transition differences among Mongolian gerbil families in a naturalistic environment. The analyses are convincing, with a thorough treatment of the acoustic data and a demonstration of the robustness of the observed effect across days. The work will likely be of interest to the auditory neuroscience and neuroethology communities.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.89892.3.sa1](https://doi.org/10.7554/eLife.89892.3.sa1)

Summary:

This research offers an in-depth exploration and quantification of social vocalization within three families of Mongolian gerbils. In an enlarged, semi-natural environment, the study continuously monitored two parent gerbils and their four pups from P14 to P34. Through dimensionality reduction and clustering, a diverse range of gerbil call types was identified. Interestingly, distinct sets of vocalizations were used by different families in their daily interactions, with unique transition structures exhibited across these families. The primary results of this study are compelling, although some elements could benefit from clarification

Strengths:

Three elements of this study warrant emphasis. Firstly, it bridges the gap between laboratory and natural environments. This approach offers the opportunity to examine natural social behavior within a controlled setting (such as specified family composition, diet, and life stages), maintaining the social relevance of the behavior. Secondly, it seeks to understand short-timescale behaviors, like vocalizations, within the broader context of daily and life-stage timescales. Lastly, the use of unsupervised learning precludes the injection of human bias, such as pre-defined call categories, allowing the discovery of the diversity of vocal outputs.

Comments on the revised version:

(1) The authors have clarified the possible types of differences in the vocalizations of different families and discussed the potential contribution of the adult-pup difference.

(2) The authors have added the analysis in Figure 4 about the developmental changes in call types.

(3) The authors have analyzed the additional information in the 2-gram structure of the calls as evidence to apply the transition matrices to compare the families.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.89892.3.sa2](https://doi.org/10.7554/eLife.89892.3.sa2)

Peterson et al., perform a series of behavioral experiments to study the repertoire and variance of Mongolian gerbil vocalizations across social groups (families). A key strength of the study is the use of a behavioral paradigm which allows for long term audio recordings under naturalistic conditions. This new experimental set-up results in the identification of additional vocalization types, not previously described the literature. In combination with state-of-the-art methods for vocalization analysis, the authors demonstrate that the distribution of sound types and the transitions between these sound types across three gerbil families is different. This is a highly compelling finding which suggests that individual families may develop distinct vocal repertories. One potential limitation of the study lies in the cluster analysis used for identifying distinct vocalization types. The authors use a Gaussian Mixed Model (GMM) trained on variational auto Encoder derived latent representation of vocalizations to classify recorded sounds into clusters. Through the analysis the authors identify 70 distinct clusters and demonstrate a differential usage of these sound clusters across families. While the authors acknowledge the inherent challenges in cluster analysis and provide additional analyses (i.e. maximum mean discrepancy, MMD), additional analysis would increase the strength of the conclusions. In particular, analysis with different cluster sizes would be valuable. An additional limitation of the study is that due to the methodology that is used, the authors can not provide any information about the bioacoustic features that contribute to differences in sound types across families which limits interpretations about how the animals may perceive and react to these sounds in an ethologically relevant manner.

The conclusions of this paper are well supported by data.

• Can the authors comment on the potential biological significance of the 70 sound clusters? Does each cluster represent a single sound type? How many vocal clusters can be attributed to a single individual? Similarly, can the authors comment on the intra-individual and inter-individual variability of the sound types within and across families?

• As a main conclusion of the paper rests on the different distribution of sound clusters across families, it is important to validate the robustness of these differences across different cluster parameters. Specifically, the authors state that "we selected 70 clusters as the most parsimonious fit". Could the authors provide more details about how this was fit? Specifically, could the authors expand upon what is meant by "prior domain knowledge about the number of vocal types...". If the authors chose a range of cluster values (i.e. 10, 30, 50, 90) does the significance of the results still hold?

• While VAEs are powerful tools for analyzing complex datasets in this case they are restricted to analysis of spectrogram images. Have the authors identified any acoustic differences (i.e. in pitch, frequency, other sound components) across families?

Following a revision of the manuscript the authors have taken many of these points under consideration and as a result have significantly improved the manuscript. Critically, they have now provided additional quantification that differences across family repertories are robust against cluster selection size.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.89892.3.sa3](https://doi.org/10.7554/eLife.89892.3.sa3)

Summary:

In this study, Peterson et al. longitudinally record and document the vocal repertoires of three Mongolian gerbil families. Using unsupervised learning techniques, they map the variability across these groups, finding that while overall statistics of, e.g., vocal emission rates and bout lengths are similar, families differed markedly in their distributions of syllable types and the transitions between these types within bouts. In addition, the large and rich data are likely to be valuable to others in the field.

Strengths:

- Extensive data collection across multiple days in multiple family groups.

- Thoughtful application of modern analysis techniques for analyzing vocal repertoires.

- Careful examination of the statistical structure of vocal behavior, with indications that these gerbils, like naked mole rats, may differ in repertoire across families.

- Estimation of the stability of the effects across days.

Weaknesses:

- The work is largely descriptive, documenting behavior rather than testing a specific hypothesis.

- The number of families (N=3) is somewhat limited, though the authors have taken some care to examine the robustness of the findings.
