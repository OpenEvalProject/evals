# Peer review - Round 1

Editors:
- Dominique C Bergmann, Stanford University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.57613.sa1](https://doi.org/10.7554/eLife.57613.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

In this manuscript we are introduced to PlantSeg, an automated, versatile new image analysis pipeline with features that work especially well on plant tissues. PlantSeg uses machine learning (convolutional neural networks) to identify cellular boundaries and to segment complex tissues into their constituent cells. This pipeline performs well over a range of different tissues, is accessible to novice and expert users, and can be combined with other software to enable quantitative assessment of biological features.

Decision letter after peer review:

Thank you for submitting your article "Accurate and versatile 3D segmentation of plant tissues at cellular resolution" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Dominique C Bergmann as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Christian Hardtke as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Moritz Graeff (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

Summary:

PlantSeg, a tool described in Wolny et al.: "Accurate and versatile 3D segmentation of plant tissues at cellular resolution", harnesses recent advances in computer vision to perform volumetric segmentation of plant tissues. It describes an image analysis pipeline utilising machine learning for cellular segmentation of plant tissues, an essential but often time-consuming part of many recent studies in plant development. The authors provide an automated, versatile new pipeline that utilises convolutional neural networks to identify cellular boundaries before cell segmentation. This pipeline performs well over a range of different tissues, is accessible to novice and expert users, and will likely attract great interest within the plant (and animal) scientific community

Three reviewers concluded that this tool addressed a pressing need for the community, and in general, found the design, rationale, and performance good. There were several suggestions to improve these points as well as to improve the ease of installation and use. Below, we divide essential revisions into two categories: performance and usability, and these should be addressed in a revision and the response to reviewers.

Essential revisions:

Performance:

1) The authors compare nine different CNN designs, varying in the network architecture, loss function, and training protocol (including image augmentation and changes of layer orders within the training protocol). It is unclear how the tested designs were chosen out of the large number of possible design permutations. In particular, it is unclear why the authors do not include further design permutations using the design they consider the most robust (based on the Lbce + Ldice loss function) – only a single design uses this loss function, although it can reasonably be expected that other designs using this function might further improve CNN performance. Can the authors either include such networks, or explain why they chose not to, and furthermore lay out a clear rationale for choosing the networks presented here?

PlantSeg is accessible to non-experts, but its exact advantages over other user-friendly tools such as the U-Net ImageJ plug-in, CDeep3M, or ilastik could use further elaboration. Relative to these methods, what are PlantSeg's primary contributions-that it combines CNN-based predictions and more sophisticated post-processing methods for plant tissues?

2) In the sections assessing the performance of PlantSeg in different datasets, the authors do not specify which CNN they used for boundary detection, and which segmentation strategy they used. Did they preselect their strategy based on microscope type and voxel size, as recommended later on for other users? Or did they test multiple combinations and identified the best performing one? Considering it is not feasible to generate a ground truth for every dataset analysed, it is of great interest to the reader to understand the range in performance of the different CNN/segmentation combinations available in the PlantSeg pipeline. If the authors tested multiple combinations, they should report their results. If they used a single combination, they should explain how this was chosen.

3) In the subsection "Analysis of leaf growth and differentiation", the authors specify the mean number of segmentation errors to assess the quality of the PlantSeg pipeline compared to MorphoGraphX. It is not clear how the ground truth for these comparisons was generated, and also, why the authors deviate from their more detailed assessment of segmentation quality used before (subsections "Step 2: segmentation of tissues into cells using graph partitioning" and "Performance on external plant datasets").

4) It is unclear how PlantSeg perform on one of the most characteristic (and problematic) cell types-the highly lobed epidermal cells. Lobes have presented challenges to older watershed-based algorithms. The runs of PlantSeq on sepals, which contain these cells do not seem to have behaved well (likely due to the low quality of the input data) and the work on Cardamine leaves appears to be a combination of MorphoGraphX and PlantSeg. There are other published datasets that include lobed cells from Arabidopsis leaves and also maize leaves (where lobing is of a different nature) and these should be analyzed with PlantSeg alone to demonstrate its effectiveness at segmenting such cells.

Usability:

5) This is a Linux-based program, and this diminishes its usability especially for people who might want to use it at home on iOS/PC systems during the current pandemic. While we recognize that changing the structure to run on these systems is a big request and it is not an absolute requirement for this manuscript to be accepted, it is something that needs to be acknowledged. Writing early in the text (even in the Abstract) that this is Linux-based should cue in the reader about requirements.

6) To generate a tool that is both accurate and generalizable, you experimented with several design choices, including the network architecture, loss function, patch size, order of operations within a U-Net level, and partitioning strategy. The pre-trained networks are included in the software package and can be specified via the graphical user interface (GUI) or the command line. Here, non-experts would benefit from more guidance as to which pre-trained networks they should specify for which datasets. For example, beyond considerations such as microscope modality and voxel size, what are the guiding principles for which partitioning strategy should be selected? If this information is already available, please refer to its location in the main text.

7) Additionally, the GUI allows users to adjust a number of parameters. To expand the userbase, consider providing an appendix that (1) explains what these parameters mean and (2) outlines the circumstances under which they should be adjusted.

8) A valuable addition would be a table that lists how PlantSeg interfaces with other image analysis tools, specifically including software packages (in addition to MorphoGraphX) that can perform cell counting, cell tracking, and cell volume and shape measurements on the outputs of PlantSeg.

9) Finally, in the GitHub repository, the read-me document is helpful, but the folders and files are not named in an intuitive way for non-experts to navigate. Please rename and/or provide a short description so it is clear what each folder contains.
