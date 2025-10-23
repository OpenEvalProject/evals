# Peer review - Round 1

Editors:
- Chaogan Yan, Chinese Academy of Sciences China

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.94909.2.sa0](https://doi.org/10.7554/eLife.94909.2.sa0)

The study presents an important ecosystem designed to support literature mining in biomedical research, showcasing a methodological framework that includes tools like Pubget for article collection and labelbuddy for text annotation. The solid evidence presented for these tools suggests they could streamline the analysis and annotation of scientific literature, potentially benefiting research across a range of biomedical disciplines. While the primary focus is on neuroimaging literature, the applicability of these methods and tools might extend further, offering an advance in the practices of meta-research and literature mining.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.94909.2.sa1](https://doi.org/10.7554/eLife.94909.2.sa1)

Summary:

In this paper, the authors present new tools to collect and process information from the biomedical literature that could be typically used in a meta-analytic framework. The tools have been specifically developed for the neuroimaging literature. However, many of their functions could be used in other fields. The tools mainly enable to downloading of batches of paper from the literature, extracting relevant information along with meta-data, and annotating the data. The tools are implemented in an open ecosystem that can be used from the command line or Python.

Strengths:

The tools developed here are really valuable for the future of large-scale analyses of the biomedical literature. This is a very well-written paper. The presentation of the use of the tools through several examples corresponding to different scientific questions really helps the readers to foresee the potential application of these tools.

Weaknesses:

The tools are command-based and store outcomes locally. So users who prefer to work only with GUI and web-based apps may have some difficulties. Furthermore, the outcomes of the tools are constrained by inherent limitations in the scientific literature, in particular, here the fact that only a small portion of the publications have full text openly available.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.94909.2.sa2](https://doi.org/10.7554/eLife.94909.2.sa2)

Summary:

In this manuscript, the authors described the litmining ecosystem that can flexibly combine automatic and manual annotation for meta-research.

Strengths:

Software development is crucial for cumulative science and of great value to the community. However, such works are often greatly under-valued in the current publish-or-perish research culture. Thus, I applaud the authors' efforts devoted to this project. All the tools and repositories are public and can be accessed or installed without difficulty. The results reported in the manuscript are also compelling that the ecosystem is relatively mature.

Weaknesses:

First and foremost, the logic flow of the current manuscript is difficult to follow.

The second issue is the results from the litmining ecosystem were not validated and the efficiency of using litmining was not quantified. To validate the results, it would be better to directly compare the results of litmining with recognized ground truth in each of the examples. To prove the efficiency of the current ecosystem, it would be better to use quantitative indices for comparing the litmining and the other two approaches (in terms of time and/or other costs in a typical meta-research).

The third family of issues is about the functionality of the litmining ecosystem. As the authors mentioned, the ecosystem can be used for multiple purposes, however, the description here is not sufficient for researchers to incorporate the litmining ecosystem into their meta-research project. Imagine that a group of researchers are interested in using the litmining ecosystem to facilitate their meta-analyses, how should they incorporate litmining into their workflow? I have this question because, in a complete meta-analysis, researchers are required to (1) search in more than one database to ensure the completeness of their literature search; (2) screen the articles from the searched articles, which requires inspection of the abstract and the pdf; (3) search all possible pdf file of included articles instead of only relying on the open-access pdf files on PMC database. That said, if researchers are interested in using litmining in a meta-analysis that follows reporting standards such as PRISMA, the following functionalities are crucial:

(a) How to incorporate the literature search results from different databases;

(b) After downloading the meta-data of articles from databases, how to identify whose pdf files can be downloaded from PMC and whose pdf files need to be searched from other resources;

(c) Is it possible to also annotate pdf files that were not downloaded by pubget?

(d) How to maintain and update the meta-data and intermediate data for a meta-analysis by using litmining? For example, after searching in a database using a specific command and conducting their meta-analysis, researchers may need to update the search results and include items after a certain period.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.94909.2.sa3](https://doi.org/10.7554/eLife.94909.2.sa3)

Summary:

The authors aimed to develop an automated tool to easily collect, process, and annotate the biomedical literature for higher efficiency and better reproducibility.

Strengths:

Two charms coming with the efforts made by the team are Pubget (for efficient and reliable grabbing articles from PubMed) and labelbuddy (for annotating text). They make text-mining of the biomedical literature more accessible, effective, and reproducible for streamlined text-mining and meta-science projects. The data were collected and analyzed using solid and validated methodology and demonstrated a very promising direction for meta-science studies.

Weaknesses:

More developments are needed for different resources of literature and strengths of AI-powered functions.
