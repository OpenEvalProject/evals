# Peer review - Round 1

Editors:
- Josh W Shaevitz, Princeton University United States

Reviewers:
- Josh W Shaevitz, Princeton University United States
- Greg Stephens

## Review text

DOI: [10.7554/eLife.47994.sa1](https://doi.org/10.7554/eLife.47994.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "Fast and robust animal pose estimation" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Josh W Shaevitz as a guest Reviewing Editor, and the evaluation has been overseen by Ian Baldwin as the Senior Editor. The following individual involved in review of your submission has also agreed to reveal their identity: Greg Stephens.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This is a very well written resource article that covers the role of deep-learning in animal pose estimation, develops a new method with several improvements in accuracy and speed, and compares this method to existing methods in the literature. This is a timely paper and the improvements are likely to have a significant impact on users in this field. While this field is changing extremely rapidly, the reviewers believe that this paper will both move the technology further and also provide a readable review to the field for newcomers. However, the reviewers identified several issues that need to be addressed before publication, including text not well explained or a bit exaggerated, the effect of relatively small datasets, training routine differences that might affect the comparisons made, and a lack of explanation of the data acquisition.

Essential revisions:

1) Issues with the code:

a) In the script deepposekit/augment/__init__.py, the line 'from. import augmenters' needed to be substituted by 'from imgaug import augmenters'.

b) The module imgaug had to be installed.

c) We also found that comments in code were good at the beginning but less detailed later.

d) The example notebook "step5_predict.ipynb" could use some more instruction. In particular, what is missing is a section of code to analyze the full video.avi file, instead of just one batch of 5000 frames, which might be confusing for a beginner.

e) One suggestion for "step_4_train_model.ipynb". In the section "Define callbacks to enhance model training", the kwarg for the Logger object should be renamed "validation_batch_size" instead of "batch_size", since it is indeed using validation frames. If one labels a small number of annotated examples, then it is possible to get an error here, as the logger will try and use more validation frames than are actually available. The renaming of this variable might help any confusion.

2) Subsection “Animal pose estimation using deep learning”, fourth paragraph: I would recommend writing more text on the distinction between single and multi-animal pose estimation and tracking in the main text. This is a very important issue and I worry that the casual/uninitiated reader might be confused and not look at Appendix 4. For some systems, tracking is very difficult and it should be clear to readers that this method will be difficult to use out-of-the-box for those systems.

3) The Abstract and title do not specifically mention the key novelties of the manuscript and should be rewritten.

4) 'Further details of how these image datasets were acquired, preprocessed, and tracked before applying our pose estimation methods will be described elsewhere.' I think they need to be given here.

5) How do the presented methods differ depending on the amount of labelled data? In the subsection “Experiments and model comparisons”, the authors postulate that differences in methods depending on training routines are minimal. As you are proposing an improvement over these methods, you need to prove this. You should also add a discussion of how many frames one should annotate before starting. While this is an incremental process (using the network to initialize further annotations), how many frames should one label at first? Also, as a related point, how does the accuracy of the network depend on the number of annotations?

6) It is apparent that machine vision methods to track animal behavior on the scale of posture will continue to advance at a remarkable speed. The authors could add substantial and long-lasting value to their work by discussing some of the more general aspects of behavioral measurement. Some possibilities:

a) It was only a few years ago that most behavioral measurements focused on image centroids and it would be useful to expand on the usefulness of representing behavior through posture vs. centroid.

b) What behavioral conditions remain challenging for the current generation of pose estimation algorithms (including DeepPoseKit)? For example, it would seem that a densely-packed fish school or bee hive might require novel approaches for both individual identity, the 3D nature of the school and resulting occlusions. This is an important consideration for the comparison of techniques. For example LEAP was designed very directly for high-contrast, controlled laboratory environments and it is perhaps not surprising that LEAP fares worse under less ideal conditions.

c) Relatedly, when would we consider the "pose tracking" problem solved? For example, the number of body points is user- not organism-defined, when do we know that we have enough?

d) The DeepPoseKit algorithm leverages multiple spatial scales in the input image data and it would be useful to expand the discussion about why this is beneficial. For example, for the fly data, what explicitly are the multiple scales that one might want to learn from the images? Can you further discuss how exactly does multi-scale inference achieve the fast speed of LEAP without sacrificing accuracy

e) With deep learning algorithms especially, there is a danger of rare but very wrong label assignments. Since DeepPoseKit is designed for general use, including among those not experienced in such networks, it would be quite useful to emphasize post-processing analysis that can help minimize the effect of these errors.

7) The manuscript would benefit from a discussion of how long it takes to train the networks and especially interesting would be a benchmarking of the three algorithms: DeepPoseKit, LEAP and DeepLabCut.
