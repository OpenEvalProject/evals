# Peer review - Round 1

Editors:
- Vitaly Ryu, Icahn School of Medicine at Mount Sinai United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.90502.3.sa0](https://doi.org/10.7554/eLife.90502.3.sa0)

This valuable study advances our understanding of spatial–temporal cell dynamics both in vivo and in vitro. The authors provide solid evidence for their innovative deep learning-based apoptosis detection system, ADeS, which utilizes the principle of activity recognition. This work will be of broad interest to cell biologists and neuroscientists.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.90502.3.sa1](https://doi.org/10.7554/eLife.90502.3.sa1)

Summary:

Pulfer et al., describes the development and testing of a transformer based deep learning architecture called ADeS, which the authors use to identify apoptotic events in cultured cells and live animals. The classifier is trained on large datasets and provides robust classification accuracies in test sets that are comparable to and even outperform existing deep learning architectures for apoptosis detection. Following this validation, the authors also design use cases for their technique both in vitro and in vivo, demonstrating the value of ADeS to the apoptosis research space.

Strengths:

ADeS is a powerful tool in the arsenal of cell biologists interested in the spatio-temporal co-ordinates of apoptotic events in vitro, since live cell imaging typically generates densely packed fields of view that are challenging to parse by manual inspection. The authors also integrate ADeS into the analysis of data generated using different types of fluorescent markers in a variety of cell types and imaging modalities, which increases its adaptability by a larger number of researchers. ADeS is an example of successful deployment of activity recognition (AR) in the automated bioimage analysis space, highlighting the potential benefits of AR to quantifying other intra- and intercellular processes observable using live cell imaging.

Weaknesses:

A major drawback was the lack of access to the ADeS platform for the reviewers; the authors state that the code is available in the code availability section, which is missing from the current version of the manuscript. This prevented an evaluation of the usability of ADeS as a resource for other researchers. The authors also emphasize the need for label-free apoptotic cell detection in both their abstract and their introduction but have not demonstrated the performance of ADeS in a true label-free environment where the cells do not express any fluorescent markers. While Pulfer et al., provides a wealth of information about the generation and validation of their DL classifier for in vitro movies, and the utility of ADeS is obvious in identifying apoptotic events among FOVs containing ~1700 cells, the evidence is not as strong for in vivo use cases. They mention the technical challenges involved in identifying apoptotic events in vivo, and use 3D rotation to generate a larger dataset from their original acquisitions. However, it is not clear how this strategy would provide a suitable training dataset for understanding the duration of apoptotic events in vivo since the temporal information remains the same. The authors also provide examples of in vivo acquisitions in their paper, where the cell density appears to be quite low, questioning the need for automated apoptotic detection in those situations. In the use cases for in vivo apoptotic detection using ADeS (Fig 8), it appears that the location of the apoptotic event itself was obvious and did not need ADeS, as in the case of laser ablation in the spleen and the sparse distribution of GFP labeled neutrophils in the lymph nodes. Finally, the authors also mention that video quality altered the sensitivity of ADeS in vivo (Fig 6L) but fail to provide an example of ADeS implementation on a video of poor quality, which would be useful for end users to assess whether to adopt ADeS for their own live cell movies.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.90502.3.sa2](https://doi.org/10.7554/eLife.90502.3.sa2)

Summary:

Pulfer A. et al. developed a deep learning-based apoptosis detection system named ADeS, which outperforms the currently available computational tools for in vitro automatic detection. Furthermore, ADeS can automatically identify apoptotic cells in vivo in intravital microscopy time-lapses, preventing manual labeling with potential biases. The authors trained and successfully evaluated ADeS in packed epithelial monolayers and T cells distributed in 3D collagen hydrogels. Moreover, in vivo, training and evaluation were performed on polymorphonucleated leukocytes in lymph nodes and spleen.

Strengths:

Pulfer A. et colleagues convincingly presented their results, thoroughly evaluated ADeS for potential toxicity assay, and compared its performance with available state-of-the-art tools.

Weaknesses:

The use of ADeS is still restricted to samples where cells are fluorescently labeled either in the cytoplasm or in the nucleus, which limits its use for in vitro toxicity assays that are performed on primary cells or organoids (e.g., iPSCs-derived systems) that are normally harder to transfect.

In conclusion, ADeS will be a useful tool to improve output quality and accelerate the evaluation of assays in several research areas with basic and applied aims.
