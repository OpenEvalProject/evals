# Peer review - Round 1

Editors:
- Lynne-Marie Postovit, Queens University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.95485.3.sa0](https://doi.org/10.7554/eLife.95485.3.sa0)

This important study represents a data processing pipeline to discover causal interactions from time-lapse imaging data and convincingly illustrates it on a challenging application for the analysis of tumor-on-chip ecosystem data. The authors describe the raw data they used (imaging data), go through a step-by-step description of how to extract the features they are interested in from the raw data, and how to perform the causal discovery process. This article tackles the problem of learning causal interactions from temporal data, which is applicable to many biological applications.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.95485.3.sa1](https://doi.org/10.7554/eLife.95485.3.sa1)

Summary:

This paper presents a data processing pipeline to discover causal interactions from time-lapse imaging data and convincingly illustrates it on a challenging application for the analysis of tumor-on-chip ecosystem data.

The core of the discovery module is the original tMIIC method of the authors, which is shown in supplementary material to compare favourably to two state-of-the-art methods on synthetic temporal data on a 15 nodes network.

Strengths:

This paper tackles the problem of learning causal interactions from temporal data which is an open problem in presence of latent variables.

The core of the method tMIIC of the authors is nicely presented in connection to Granger-Schreiber causality and to the novel graphical conditions used to infer latent variables and based on a theorem about transfer entropy.

tMIIC compares favourably to PC and PCMCI+ methods using different kernels on synthetic datasets generated from a network of 15 nodes.

A full application to tumor-on-chip cellular ecosystems data including cancer cells, immune cells, cancer-associated fibroblasts, endothelial cells and anti cancer drugs, with convincing inference results with respect to both known and novel effects between those components and their contact.

The code and dataset are available online for the reproducibility of the results.

Weaknesses:

The references to "state-of-the-art methods" concerning the inference of causal networks should be more precise by giving citations in the main text, and better discussed in general terms, both in the first section and in the section of presentation of CausalXtract. It is only in the legend of the figures of the supplementary material that we get information.

Of course, comparison on our own synthetic datasets can always be criticized but this is rather due to the absence of a common benchmark in this domain compared to other domains. I recommend the authors to explicitly propose their datasets made accessible in supplementary material as benchmark for the community.

Comments on revisions:

This is a very nice paper.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.95485.3.sa2](https://doi.org/10.7554/eLife.95485.3.sa2)

Summary:

The authors propose a methodology to perform causal (temporal) discovery. The approach appears to be robust and is tested in the different scenarios: one related to live-cell imaging data, and another one using synthetic (mathematically defined) time series data. They compare the performance of their findings against another well-known method by using metrics like F-score, precision and recall,

Strengths:

--Performance, robustness, the text is clear and concise, The authors provide the code to review.

Comments on revisions:

The authors have addressed my concerns properly providing the needed explanations.
