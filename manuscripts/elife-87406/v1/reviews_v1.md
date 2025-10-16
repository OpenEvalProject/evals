# Peer review - Round 1

Editors:
- Marisa Nicolás, Laboratório Nacional de Computação Científica Brazil

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.87406.3.sa0](https://doi.org/10.7554/eLife.87406.3.sa0)

This study presents Bactabolize, a valuable tool for the rapid genome-scale reconstruction of bacteria and the prediction of growth phenotypes. Using validated methodology, the tool relies on a reference pan-genome model to create strain-specific draft metabolic models, as demonstrated in this study using Klebsiella pneumoniae. While the evidence in this specific case is solid, validation across diverse bacterial species is yet to be confirmed.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87406.3.sa1](https://doi.org/10.7554/eLife.87406.3.sa1)

In this work, Vezina et al. present Bactabolize, a rapid reconstruction tool for the generation of strain-specific metabolic models. Similar to other reconstruction pipelines such as CarveMe, Bactabolize builds a strain-specific draft reconstruction and subsequently gap-fills it. The model can afterwards be used to predict growth on carbon sources. The authors constructed a pan-model of the Klebsiella pneumoniae species complex (KpSC) and used it as input for Bactabolize to construct a genome-sale reconstruction of K. pneumoniae KPPR1. They compared the generated reconstruction with a reconstruction built through CarveMe as well as a manually curated reconstruction for the same strain. They then compared predictions of carbon, nitrogen, phosphor, and sulfur sources and found that the Bactabolize reconstruction had the overall highest accuracy. Finally, they built draft reconstructions for 10 clinical isolates of K. pneumoniae and evaluated their predictive performance. Overall, this is a useful tool, the data is well-presented, and the paper is well-written.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87406.3.sa2](https://doi.org/10.7554/eLife.87406.3.sa2)

The authors present a pipeline for generating strain-specific genome-scale metabolic models for bacteria using Klebsiella spp. as the demonstrative data. This paper claims to provide a high-throughput tool for generating strain-specific models for bacteria. However, in reality, the tool requires a reference pan-genome-based complete model to generate the strain-specific model of the species of interest, which in this study is Klebsiella pneumoniae. This requirement renders the tool redundant for high-throughput purposes since the process of building or generating the pan-genome reference model is performed separately. Additionally, the quality of the newly built strain-specific model will depend on the reference model used. Therefore, this tool, on its own, can only work specifically with the available pan-genome model of reference, which in this case is only applicable to Klebsiella pneumoniae. Its effectiveness with other bacteria has not been proven. I would suggest that the authors either reframe the performance and results to be applicable only to Klebsiella or consider adding more reference pan-genome models for the study.
