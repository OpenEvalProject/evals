# Peer review - Round 1

Editors:
- Nikolaus Grigorieff, Janelia Research Campus, Howard Hughes Medical Institute United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.65894.sa1](https://doi.org/10.7554/eLife.65894.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

This manuscript describes the curation of a training dataset that will be an important resource for developers of new segmentation and deep-learning algorithms for electron microscopy data. The small size of the dataset makes it easy to use, and its broad range of image modalities ensures that the model will be applicable in many situations, making it very useful for the community.

Decision letter after peer review:

Thank you for submitting your article "CEM500K – A large-scale heterogeneous unlabeled cellular electron microscopy image dataset for deep learning" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Nikolaus Grigorieff as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Anna Akhmanova as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Stephan Saalfeld (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential Revisions:

1) This is an excellent manuscript. The authors establish a broadly usable dataset, and designed and conducted a strict and sound evaluation study. The paper is well written, easy to follow and overall well balanced in how it discusses technical details and the wider impact of this study. However, the work focuses on pixel classification on 2D images. This is not clear in the beginning and only discussed fairly late in the manuscript where 3D approaches are generally dismissed for no other reason than that they are not applicable to 2D images and more expensive. This dismissal is invalid and unnecessary. The authors should mention their focus on 2D images earlier in the manuscript, explain why this approach is taken, and what would have to be changed to include 3D data.

Reviewer #1 (Recommendations for the authors):

1) The authors should clarify that none of the benchmark data have been included in the CEM500K training set.

2) The authors should include a supplementary table for the cross-validation scores they obtained to validate their trained CEM500K-moco model.

3) Given the relatively small size of the CEM500K dataset, how much of a concern is overfitting?

4) Can the authors comment on the resolution of features that are likely relevant in their CEM500K-moco model? What are the prospects of using MoCoV2 to recognize higher-resolution features in cryo-EM images?

Reviewer #2 (Recommendations for the authors):

1) This work clearly targets pixel classification on 2D images, however the 2D focus is not clear in the beginning and only discussed late (Discussion) where 3D approaches are generally dismissed for no other reason than that they are not applicable to 2D images and more expensive. This dismissal is invalid and also unnecessary and should be removed. The 2D focus should become obvious in the Abstract and Introduction of the paper since the term "image" is used for nD data in the community.

2) Introduction, third paragraph: add paragraph.

3) The hashing algorithm used for identifying near duplicates (https://www.hackerfactor.com/blog/index.php?/archives/529-Kind-of-Like-That.html) may not be optimal but this probably doesn't do much harm as its main purpose is to remove nearby sections from 3D volumes.

4) Could CEMdedup be useful for tasks that contain empty resin or nuclei?

5) Conclusion: Pretraining dataset should include data relevant for the benchmark task. Does unrelated data necessarily make the benchmark performance better? How would CEM500K + Bloss pre-training perform for the mouse data?

6) CEM500K MoCoV2 training included 360° rotations, i.e. the increased rotation invariance compared to ImageNet is by design of the training, not necessarily the data.

7) Subsection “CEM500K models are largely impervious to meaningful image augmentations”: Why would models gain robustness to rare and random events such as artifacts? Weren't such images excluded from the dataset?

8) Subsection “CEM500K models learn biologically relevant features”: Could this also be just high contrast/high gradient regions which makes sense for the given training task? I.e. is the focus on objects of interest may be a trivial consequence of objects of interest being the only thing present/distinguishable in the image?

9) Subsection “Fully trained CEM500K models achieve state-of-the-art results on EM benchmarks”: The random initialization score for CREMI of 0.0 is surprising. Is this an indication that the training setup or this particular network architecture have other issues that are unrelated to the pre-training? Others have successfully trained synapse detection networks without pre-training.

10) Discussion, second paragraph: This is not correct for CREMI which is data from the large FAFB dataset, and also itself contains more data than necessary in the padded volumes available for download. I do not find it necessary to perform this experiment but it is ok to simply say that this hasn't been done without falsely asserting that it wasn't possible.

11) I do not understand this statement: "[…] moreover, the elimination of 3D context from volume EM datasets ensures that the shared data can only reasonably be used for DL." Is it necessary?

12) Materials and methods: The CREMI synaptic cleft evaluation metric is public including code to execute it. Ground truth for test data, however, is secret. Did you submit your results for evaluation? Like above, it is not necessary to do this but the statement "[…] the training and test datasets did not have an official evaluation metric, and the ground truth segmentations were not publicly available[…]" is not correct. May be replace with "The test data for the CREMI Synaptic Cleft benchmark is not publicly available and the challenge uses a different evaluation metric than IoU. Therefore[…]".

Thank you very much for this wonderful work. It's been a pleasure to read this manuscript.

Reviewer #3 (Recommendations for the authors):

– Would you please clarify the statement “a model's ability to generalize to unseen images”? I would like to see more clarification regarding this statement as it seems that it ignores the definition of transfer learning problems. Transfer learning techniques are applied where there exists lack of data. Therefore, providing datasets with large numbers of data does not seem to be a good solution for these problems though it is still a valuable dataset for many problems.

– In the first part of the paper, it is referred to "six publicly available dataset". I know that you name them in the later part of the paper but it is a question for the reader. It would be better to name them in these sections as well.

– It would be better if the minimum amount of outperformance is defined when it is presented "significantly outperformed randomly initialized".

– Is there any reference/proof for the following claim: "Although it is currently impossible to determine a priori what data will be useful for a model, we expect that this removal of significant redundancies in the image dataset is unlikely to result in the loss of meaningful information for DL model training."

– What would happen if you keep the duplicate images and use MoCoV2 algorithm?

– How about not applying the MoCoV2 algorithm and using other algorithms? Have you considered ablation studies in this regard?

– The following statements are unclear and I appreciate it if you clarify them more.

1) "These results emphasize the necessity of evaluating deep learning algorithms and pre-training datasets on multiple benchmarks before drawing conclusions about their quality."

2) “We expect that the superior robustness to variations in cellular EM data baked into CEM500K-moco should simplify the process of adjusting to new tasks.”
