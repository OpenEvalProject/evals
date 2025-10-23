# Peer review - Round 1

Editors:
- Manuel Zimmer, Research Institute of Molecular Pathology, Vienna Biocenter and University of Vienna Austria

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.59187.sa1](https://doi.org/10.7554/eLife.59187.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper is of great interest to system-biologists who aim to analyze large datasets of image-volume time series that contain objects to segment in continuously deforming life tissues. Wen et al. present a deep-learning method for mostly automatic 1) U-net based segmentation and 2) point-registration-based tracking of cells in tissues with ongoing deformations. The authors test their pipeline on various example systems: whole brain Ca2+-activity in partially immobilized and freely crawling C. elegans, beating zebrafish heart and a 3D culture of tumor tissue. This work presents significant improvements in tracking capabilities on various metrics including the possible number of tracked objects, robustness, and computing requirements.

Decision letter after peer review:

Thank you for submitting your article "3DeeCellTracker, a deep learning-based pipeline for segmenting and tracking cells in deforming organs" for consideration by eLife. Your article has been reviewed by two peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Ronald Calabrese as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

This paper presents a deep-learning method for mostly automatic 1) U-net based segmentation and 2) point-registration-based tracking of cells with some deformations. Their training data consists of a single volume of corrected annotated data. The authors test their pipeline on two example systems: 3 datasets of ~150 neurons each in partially immobilized C. elegans and ~100 cells in a beating zebrafish heart. Some datasets are from previous work [1,2] and some are newly acquired. Both of these previous works propose tracking pipelines, and this work claims improvements in tracking capabilities on various metrics including number of segmented neurons, percentage of correct identifications, and runtime. In addition, the authors degrade their datasets in various ways (adding noise, removing frames), and still retain good performance. However, both of these claims lack proper quantifications.

The general idea of using deep learning for segmentation, and for tracking, is timely. However, the manuscript feels at times anecdotal and it is not convincing that it is truly ready for the diverse applications it claims. The consensus among the reviewers is that the approach should be tested on more ground truth data-sets, which are available for worms and on repeated measurements from zebrafish heart. Moreover, it is unclear how well the approach would work from truly deforming tissues like unrestrained moving worms. Such datasets are available from the Leifer lab as well as from the Hillman lab, who is co-authoring this manuscript. Claims on the performance of their approach should be based on more solid quantifications.

Essential revisions:

Reviewer #1:

1) Motion in data

a) This pipeline would be a major breakthrough if tracking succeeded in the freely moving scenario across different species, as in previous custom-made trackers for C. elegans [3]. Indeed, this is the core challenge in video processing of calcium imaging data, as classical algorithms largely suffice for the no motion or slow-motion cases. To my understanding Nguyen et al., 2016, was from freely moving worms but the datasets used here seems all from an immobilized worm (worm #1-2). Please clarify. A better description of the used datasets should be provided instead of simply citing the original sources.

b) However, it is unclear how much of a contribution this pipeline is in this respect. While the zebrafish heart data are clearly moving and deforming (Figure 5—video 2), the motion is extremely stereotyped. The C. elegans videos however, do not appear to be moving (Figure 3—videos 1-2, Figure 4—videos 1-2). If this algorithm does not work with the motion present in freely moving animals, this should be clarified.

c) If it does, more explicit comparisons with the state of the art are required, e.g. [3].

d) Regardless of the exact claim, some quantification of tracking performance as a function of increased motion should be included. Although robustness tests are performed by removing intermediate volumes from the videos, due to the nature of the motion (cyclic in zebrafish and intermittent in C. elegans), it is not obvious if or in what way this increases the motion of the neurons

2) Feed-Forward Network (FFN) for initial tracking

a) This network is the sole deep-learning component of the second stage of the algorithm, finding correspondence between segmentations in different volumes. However, it is unclear what benefit this element brings, and the statement starting on "We believe that the high accuracy and robustness of our method is based on the introduction of FFN for tracking" seems unwarranted.

b) In particular: the FFN is trained on random affine transformations of segmented volumes (Materials and methods); thus, it is surprising that it would perform better than a direct affine alignment.

c) This comparison should be included, and if the FFN is better, some discussion motivating this surprising result should also be included.

3) Figure 2, part 2:

Panels A and B show FPFH and FNN performance (respectively) on a matching task, but neither appears to be the algorithm used in the actual pipeline, which is a combination of both. In addition, why is the matching shown between t=1 and t=10? I agree with the caption that this should be more challenging for the algorithm, but without the context of t=1 -> t=2 or further quantification, it is hard to understand the goal of these panels.

This figure could be significantly improved by adding quantifications due to robustness to motion as discussed above.

4) Figure 5:

Photobleaching is mentioned as causing difficulties with segmentation, but this is not quantified.

5) Related to usability: A key claim of this paper is that the authors' package is easy to use. Indeed, I applaud the use of github and freely available software like Tensorflow. This claim is generally supported by 1) the fact that the work runs on a desktop (favorably comparing to other trackers, e.g., which require a cluster [3]) and 2) the multiple example systems and optical systems tested on. However, there are several key concerns:

a) Basic automatic conda environment creation should be supported; see the.yaml files in e.g. DeepLabCut and the associated tutorial

https://github.com/DeepLabCut/DeepLabCut/blob/master/conda-environments/DLC-CPU.yaml

b) Why is Fiji a dependency? Although I personally love Fiji, simple rigid alignment can be performed in python and would remove a fragile dependency

c) What implementation of PR-GLS is being used? The original publication references a MATLAB implementation: https://github.com/jiayi-ma/PR-GLS. However, the authors are using entirely Python… did the authors rewrite the original algorithm? Or is there another implementation not associated with the paper? This should be clarified

Reviewer #2:

1) The work uses way too few sets of validation data. Altogether, it only used three sets of C. elegans wholebrain imaging data and a single set of zebrafish heart imaging data. Drawing general conclusions from this on the algorithm's performance (especially comparisons with other algorithms) is premature.

2) In the comparisons with other methods, while the intention was good, the results are anecdotal. Testing the algorithms is done on a very limiting set of data; whether these datasets represent the breadth of realistic problems that would be encountered for the variety of applications (e.g. neuroscience, or other physiological or developmental functional imaging, in C. elegans or zebrafish or other model systems) is hard to tell. Also quite importantly, it is difficult to say whether the optimal choice of parameters were used for the competing methods.

3) Noises added to the real data (as in Figure 6) aren't necessarily representative of the real data's properties/features. There should be characterizations of the variability in real data on size, intensity, shape, etc. Further, it does seem that the performance of the algorithm is sensitive to these noises, and thus it is not trivial to prove that the algorithm is robust to these noises. The manuscript did not convince me that the algorithm currently can indeed deal with real noises in real datasets.

4) "To solve the difficulty in preparing training data for FFN, we used artificial training data by simulating cell movements in deforming organs." Why is this good? How is the artificial data representing real organ deformation?

5) Results, comparing other datasets – the comparisons are very qualitative. Validation is vague, descriptive, rather than quantitative.

6) Several places of the manuscript are also anecdotal, e.g. Results (corrupt data, still get 53% correct). Even the in silico studies (e.g. noise or reduced sampling) aren't systematic.

7) 60-80% of zebrafish heart cells tracked – is it useful? Which ones are the missing cells? The qualitative conclusions seem to be fairly trivial.

The manuscript made a few assertions without backing up with data/results. For example, the problems identified are real (Results), but no specifics to back up, and no systematic characterizations are done, using real data, comparing the work with other approaches. Another example – "our method became robust to tracking errors in the initial matching".

References:

1) "Accurate Automatic Detection of Densely Distributed.… – PLoS." 6 Jun. 2016, https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004970. Accessed 26 Jun. 2020.

2) "Real-time volumetric microscopy of in vivo dynamics and large.…." 27 Sep. 2019, https://www.nature.com/articles/s41592-019-0579-4. Accessed 26 Jun. 2020.

3) "Automatically tracking neurons in a moving and.… – PLoS." 18 May. 2017, https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005517. Accessed 26 Jun. 2020.
