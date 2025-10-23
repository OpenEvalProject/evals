# Peer review - Round 1

Editors:
- Sjors HW Scheres, MRC Laboratory of Molecular Biology United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.98552.3.sa0](https://doi.org/10.7554/eLife.98552.3.sa0)

This work describes a new software platform for machine-learning-based segmentation of and particle-picking in cryo-electron tomograms. The program and its corresponding online database of trained models will allow experimentalists to conveniently test different models and share their results with others. The paper provides convincing evidence that the software will be valuable to the community.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.98552.3.sa1](https://doi.org/10.7554/eLife.98552.3.sa1)

This paper describes "Ais", a new software tool for machine-learning based segmentation and particle picking of electron tomograms. The software can visualise tomograms as slices and allows manual annotation for the training of a provided set of various types of neural networks. New networks can be added, provided they adhere to a python file with an (undescribed) format. Once networks have been trained on manually annotated tomograms, they can be used to segment new tomograms within the same software. The authors also set up an online repository to which users can upload their models, so they might be re-used by others with similar needs. By logically combining the results from different types of segmentations, they further improve the detection of distinct features. The authors demonstrate the usefulness of their software on various data sets. Thus, the software appears to be a valuable tool for the cryo-ET community that will lower the boundaries of using a variety of machine-learning methods to help interpret tomograms.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.98552.3.sa2](https://doi.org/10.7554/eLife.98552.3.sa2)

Summary:

Last et al. present Ais, a new deep learning based software package for segmentation of cryo electron tomography data sets. The distinguishing factor of this package is its orientation to the joint use of different models, rather than the implementation of a given approach: Notably, the software is supported by an online repository of segmentation models, open to contributions from the community.

The usefulness of handling different models in one single environment is showcased with a comparative study on how different models perform on a given data set; then with an explanation on how the results of several models can be manually merged by the interactive tools inside Ais.

The manuscripts presents two applications of Ais on real data sets; one oriented to showcase its particle picking capacities on a study previously completed by the authors; a second one refers to a complex segmentation problem on two different data sets (representing different geometries as bacterial cilia and mitochondria in a mouse neuron), both from public databases.

The software described in the paper is compactly documented in its website, additionally providing links to some youtube videos (less than an hour it toral) where the authors videocapture and comment major workflows.

In short, the manuscript describes a valuable resource for the community of tomography practitioners.

Strengths:

Public repository of segmentation models; easiness of working with several models and comparing/merging the results.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.98552.3.sa3](https://doi.org/10.7554/eLife.98552.3.sa3)

Summary:

In this manuscript, Last and colleagues describe Ais, an open-source software package for the semi-automated segmentation of cryo-electron tomography (cryo-ET) maps. Specifically, Ais provides a graphical user interface (GUI) for the manual segmentation and annotation of specific features of interest. These manual annotations are then used as input ground-truth data for training a convolutional neural network (CNN) model, which can then be used for automatic segmentation. Ais provides the option of several CNNs so that users can compare their performance on their structures of interest in order to determine the CNN that best suits their needs. Additionally, pretrained models can be uploaded and shared to an online database.

Algorithms are also provided to characterize "model interactions" which allows users to define heuristic rules on how the different segmentations interact. For instance, a membrane adjacent protein can have rules where it must colocalize a certain distance away from a membrane segmentation. Such rules can help reduce false positives; as in the case above, false negatives predicted away from membranes are eliminated.

The authors then show how Ais can be used for particle picking and subsequent subtomogram averaging and for segmentation of cellular tomograms for visual analysis. For subtomogram averaging, they used a previously published dataset and compared the averages of their automated picking with the published manual picking. Analysis of cellular tomogram segmentations were primarily visual.

Strengths:

CNN-based segmentation of cryo-ET data is a rapidly developing area of research, as it promises substantially faster results than manual segmentation as well as the possibility for higher accuracy. However, this field is still very much in the development and the overall performance of these approaches, even across different algorithms, still leaves much to be desired. In this context, I think Ais is an interesting packages, as it aims to provide both new and experienced users streamlined approaches for manual annotation, access to a number of CNNs, and methods to refine the outputs of CNN models against each other. I think this can be quite useful for users, particularly as these methods develop.
