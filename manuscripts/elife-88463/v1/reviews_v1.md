# Peer review - Round 1

Editors:
- Hanna Salman, University of Pittsburgh United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.88463.4.sa0](https://doi.org/10.7554/eLife.88463.4.sa0)

This article provides a review and test of image-analysis methods for bacteria growing in the 'mother-machine' microfluidic device, introducing also a new graphical user interface for the computational analysis of mother-machine movies based on the 'Napari' environment. The tool allows users to segment cells based on two previously published methods (classical image transformation and thresholding as well as UNet-based analysis), with solid evidence for their robust performance based on comparison with other methods and use of datasets from other labs. While it was difficult to assess the user-friendliness of the new GUI, it appears to be valuable and promising for the field.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88463.4.sa1](https://doi.org/10.7554/eLife.88463.4.sa1)

The authors aim to develop an easy-to-use image analysis tool for the mother machine that is used for single-cell time-lapse imaging. Compared with related software, they tried to make this software more user-friendly for non-experts with a design of "What You Put Is What You Get". This software is implemented as a plugin of Napari, which is an emerging microscopy image analysis platform. The users can interactively adjust the parameters in the pipeline with good visualization and interaction interface.

Strengths:

- Updated platform with great 2D/3D visualization and annotation support.

- Integrated one-stop pipeline for mather machine image processing.

- Interactive user-friendly interface.

- The users can have a visualization of intermediate results and adjust the parameters.

Weaknesses:

- Based on the presentation of the manuscript, it is not clear that the goals are fully achieved.

- Although there is great potential, there is little evidence that this tool has been adopted by other labs.

- the diversity of datasets used in this study is limited.

- Some paragraphs in the Discussion section are like blogs with general recommendations. Although the suggestions look pretty useful, it is not the focus of this manuscript. It might be more appropriate to put it in the GitHub repo or a documentation page. The discussion should still focus on the software, such as features, software maintenance, software development roadmap, and community adoption.

A discussion of the likely impact of the work on the field, and the utility of the methods and data to the community.

- The impact of this work depends on the adoption of the software MM3. Napari is a promising platform with an expanding community. With good software user experience and long-term support, there is a good chance that this tool could be widely adopted in the mother machine image analysis community.

- The data analysis in this manuscript is used as a demo of MM3 features, rather than scientific research.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88463.4.sa2](https://doi.org/10.7554/eLife.88463.4.sa2)

The authors present an image-analysis pipeline for mother-machine data, i.e., for time-lapses of single bacterial cells growing for many generations in one-dimensional microfluidic channels. The pipeline is available as a plugin of the python-based image-analysis platform Napari. The tool comes with two different previously published methods to segment cells (classical image transformation and thresholding as well as UNet-based analysis), which compare qualitatively and quantitatively well with the results of widely accessible tools developed by others (BACNET, DelTA, Omnipose). The tool comes with a graphical user interface and example scripts, which should make it valuable for other mother-machine users, even if this has not been demonstrated yet.

The authors also add a practical overview of how to prepare and conduct mother-machine experiments, citing their previous work, referring to detailed instructions on their github page, and giving more advice on how to load cells using centrifugation.

Finally, the authors emphasize that machine-learning methods for image segmentation reproduce average quantities of training datasets, such as the length at birth or division. Therefore, differences in training can propagate to differences in measured average quantities. This result is not surprising but good to remember before interpreting absolute measurements of cell shape.
