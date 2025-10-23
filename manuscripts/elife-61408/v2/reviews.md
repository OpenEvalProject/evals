# Peer review - Round 1

Editors:
- Joseph G Gleeson, Howard Hughes Medical Institute, The Rockefeller University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.61408.sa1](https://doi.org/10.7554/eLife.61408.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The paper provides MagellanMapper, a suite of tools to provide quantitative measures of brain structure to accurately labeled 3D digital atlases across mouse neural development, and demonstrates that the resulting brain parcellations are superior to a naive agglomeration of the existing 2D labels. The novel computational methods transform slice annotations in the Allen Developing Mouse Brain Atlas into digital 3D reference atlases. The response to reviewer comments was complete and persuasive.

Decision letter after peer review:

Thank you for submitting your article "Constructing and Optimizing 3D Atlases From 2D Data With Application to the Developing Mouse Brain" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by Kate Wassum as the Senior Editor and Joseph Gleeson as Reviewing Editor. The following individual involved in review of your submission has agreed to reveal their identity: Harold Burgess (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require additional new data, as they do with your paper, we are asking that the manuscript be revised according to the guidelines below as much as possible, or for items that cannot be directly addressed due to COVID-19, either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data. Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

Despite the availability of a high resolution, expertly annotated digital adult mouse brain atlas (Allen CCFv3), accurately labeled 3D digital atlases across mouse neural development are lacking. The authors have filled that gap by developing novel computational methods that transform slice annotations in the Allen Developing Mouse Brain Atlas into digital 3D reference atlases. They demonstrate that the resulting brain parcellations are superior to a naive agglomeration of the existing 2D labels, and provide MagellanMapper, a suite of tools to aid quantitative measures of brain structure. Cellular level whole-brain quantitative analysis is rapidly becoming a reality in many species and this manuscript provides a foundational resource for mouse developmental studies. The methods are sophisticated, carefully applied and thoroughly evaluated. The manuscript reports a computational approach to transforming available 2D atlases of mouse brains into the 3D volumetric datasets. By optimizing the "smoothing" steps, a better quality of such 3D atlases is produced claimed. In addition, the authors applied their method to the imaging dataset of neonatal mouse brains obtained by lightsheet microscopy, as proof of its potential utilization in research.

1) The pipeline of the method involved the "mirroring" before the "smoothing" steps. Is it possible to perform the "smoothing" of one hemisphere and then "mirror" the smoothed 3D atlas onto the other hemisphere to check for the alignment? By doing so, the other hemisphere could serve as an internal control for the quality and accuracy of the 3D atlas.

2) The authors developed the “edge-aware procedure”, employed to extend existing labels to unannotated lateral regions of the brain, taking advantage of intensity gradations in underlying microscope images. Authors should manually annotate a small part of the lateral brain region to compare accuracy and compare computationally generated labels to the partial lateral labels in P28 brain.

3) For more delicate subregions (e.g., those in the hypothalamus) without clear anatomical boundaries, this “edge-aware” adjustment step may become ineffective. What could then be done for these subregions? Also, it is important to note that the anatomical edges required the manual annotation.

4) Annotations present in the ADMBA took advantage of co-aligned ISH data (and computational approaches using co-aligned gene expression data have been used for de novo brain parcellation). Intensity differences in the light-microscope images may not provide enough contrast or access this expression data for for accurate segmentation. Could there be instances where adjacent regions do not have intensity differences, and the edge-aware procedure actually reduces the accuracy of the manual annotation? What is the evidence that contrast is sufficient to demark the boundaries?

5) It does appear that despite the care to avoid losing thin structures, there is some loss, for example for the light-green structure in the forebrain in Figure 5E. Authors should indicate if all labels were preserved, and provide information on volume changes by label size.

6) The accuracy of non-rigid registration of light-sheet images to the references is assessed only using a DSC value for whole-brain overlaps. This does not assess the precision of registration within the brain. The authors should apply some other measure to assess quality of alignment within the brain (e.g. mark internal landmarks visible in the reference and original light-sheet images, and measure the post-registration distance between them).
