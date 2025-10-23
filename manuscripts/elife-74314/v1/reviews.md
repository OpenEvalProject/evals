# Peer review - Round 1

Editors:
- Gordon J Berman, https://ror.org/03czfpz43 Emory University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74314.sa0](https://doi.org/10.7554/eLife.74314.sa0)

In this manuscript, the authors introduce a new piece of software, BehaviorDEPOT, that aims to serve as an open-source classifier in service of standard lab-based behavioral assays. The key arguments the authors make are that (1) the open-source code allows for freely available access, (2) the code doesn't require any coding knowledge to build new classifiers, (3) it is generalizable to other behaviors than freezing and other species (although this latter point is not shown), (4) that it uses posture-based tracking that allows for higher resolution than centroid-based methods, and (5) that it is possible to isolate features used in the classifiers. These aims are laudable, the software is indeed relatively easy to use, and it will likely be used widely in the community.


---

# Peer review - Round 1

Editors:
- Gordon J Berman, https://ror.org/03czfpz43 Emory University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74314.sa1](https://doi.org/10.7554/eLife.74314.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

The reviewers have opted to remain anonymous.

Reviewer #1 (Recommendations for the authors):

1) Line 24. The authors claim that part of the goal is to remove "human biases" using automated detection. I would push back on this a little. At the end of the day, humans are still choosing which behaviors to classify – there is no representation learning or other similar feature described here. Thus, the aim isn't to eliminate biases, it's really to make those biases more consistent (precision vs. accuracy).

2) Line 108. I'm not entirely sure what a "machine-learning quality camera" is. I would just call it a higher resolution and frame-rate camera.

Reviewer #2 (Recommendations for the authors):

I had the following notes about the paper:

No machine learning model is going to generalize well across all possible settings, and it is important for this paper to make clear from the onset what is required for the system to work. Two example points that come to mind are framerate and camera angle. Freezing is described as being detected across frames, which seems like it would be sensitive to changes in video framerate. Does the classifier need to be manually re-adjusted if a different video framerate is used? Also, are there lower bounds on the framerate or resolution of input videos that can be used? Regarding camera angle, all of the example videos shown in this paper are using a camera positioned directly above the animal. Will BehaviorDEPOT work if the mouse is filmed from the side, from below, or from an angle? While it's fine if a given classifier doesn't work in every condition, I do think the authors need to be more explicit in stating the scope of their system.

I like the idea behind the Data Exploration Module, however I was unsure where the explored metrics were coming from. Are these fully hard-coded, or can the user define their own metrics to look at? If metrics are hard-coded, it would be helpful for the authors to provide a complete list of metrics and their definitions within the manuscript (a few lists of example metrics are given, eg lines 84, 121, 146, and 155, but I don't know if these lists are complete.)

Different labs use different software for manual annotation. What annotation file formats are supported by BehaviorDEPOT's Inter-Rater Module? Can it be run on output of commonly used annotation software, like Noldus Observer?

The Methods section is nicely detailed with respect to experimental information, but it needs more information about the data analyses performed. Some examples:

– The "DeepLabCut Training and Model Availability" section of the Methods could use more detail, such as how many frames were trained for each camera, and precise error rates per body part for each video format used. Also despite the heading, there is no information about model availability in this section.

– What software was used for manual annotation of behavior?

– In Use Case 2 (Ca2+ imaging), were the computed ROC curves for imaged neurons generated using BehaviorDEPOT, or was this done post-hoc?

The claim that BehaviorDEPOT is "indistinguishable from a highly trained human" is made in reference to an ANOVA comparison of fraction time freezing according to BehaviorDEPOT vs manual annotations. While the authors can use this analysis to claim that BehaviorDEPOT is consistent with human annotations at the level of the entire trial, calling BehaviorDEPOT "indistinguishable from a human" is a much stronger claim, and needs to either be toned down or backed up by additional comparisons. For example, the authors would have to also address BehaviorDEPOT's frame-wise annotations, eg by showing that BehaviorDEPOT's precision, recall, F1 score, and specificity with respect to manual labels are comparable to that of another human.

Reviewer #3 (Recommendations for the authors):

There are several competing themes in this manuscript: is it meant to be an easy-to-use detector for simple behaviors once one has DLC data in hand? Or a simplified way to run a few types of popular behavioral experiments? Or a tool for exploring behavior data and performing statistical analyses? Overall a better demarcation of what the software does and doesn't do would be useful.

64: 'The Analysis Module processes pose tracking data from DLC or similar'.. does this mean the specific format, or that any keypoint data can be used? Would this easily generalize to 3D keypoint data or some other type of feature vector to be classified? The ability to take in different data types would add functionality and encourage users.

Different use cases are explored but they each appear to have different types of outputs and I could not find them in the GitHub. Code installation is easy but the guide could use a simpler demo.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "BehaviorDEPOT is a simple, flexible tool for automated behavioral classification based on markerless pose tracking" for further consideration by eLife. Your revised article has been evaluated by Laura Colgin (Senior Editor) and a Reviewing Editor.

The manuscript has been improved, but there are some remaining issues that need to be addressed. We ask you to respond to each of the comments below from the reviewers.

Reviewer #1:

I thank the authors for their effort in revising this manuscript- the additional detail makes the approach much easier to follow.

Thinking about the project as a whole, I think the authors' description of their freezing/VTE/etc detectors as "classifiers" is setting up false expectations in the reader, as evidenced by all the reviewers asking questions about the choice of algorithm and comparison to tools like SimBA, JAABA, MARS, B-SOiD, etc. The revised text is much clearer about how these detectors are created, and given this description, I think it may make more sense to refer to them as "heuristics", and not as "classifiers" or "algorithmic classifiers": BehaviorDEPOT is for creating human-crafted functions, whereas "algorithmic" and "classifiers" are terms used exclusively to refer to machine learning models that are fit to training data via optimization methods.

Overall, I think BehaviorDEPOT could be a useful tool. The "no coding experience required" claim is somewhat weakened by the fact that it requires users to first train a DeepLabCut model- this is definitely a task that requires a fair amount of coding experience. One could argue that once the pose model is trained, BehaviorDEPOT can be used by a non-coding user to create any number of behavior classifiers; the only shortcoming I see to that argument is that changes to the experimental setup that degrade pose estimator performance (lighting, frame rate, camera type, camera position, objects in the environment) may require periodic pose model retraining even after the initial setup process.

Other aspects of the authors' response to the review were more troubling, and would still need to be addressed. I outline these below.

1) I appreciate the authors' effort in comparing BehaviorDEPOT to JAABA, including processing all of their data with MoTr and Ctrax. I agree that providing more software tools to the rodent community is a respectable aim, and the authors are correct in noting that the additional data post-processing features of BehaviorDEPOT are not provided by JAABA. The authors' analysis satisfactorily addresses Reviewer 1's question about VTE detection.

However, I feel that the performance comparison between BehaviorDEPOT and JAABA in the text and in Figure 10 is inappropriate and misleading. The authors state that they were only able to train JAABA using either (a) the location of the animal's centroid or (b) fit ellipses produced by MoTr and Ctrax, which were of poor quality (as stated by the authors.) It is obvious that a classifier (JAABA) given just the (x,y) coordinate of a mouse's centroid or a poorly fit ellipse is going to be worse for freezing and VTE detection than a classifier (BehaviorDEPOT) given the full pose of the animal-but this undoubtedly because of the quality of the pose representation (MoTr or Ctrax vs DLC), not the quality of the classifier. Unless you can evaluate the two systems on equal footing, i.e. using the same pose representation, you should not present this comparison.

2) Similarly, the authors' response to Reviewer 1's question 3 is focused on the contrast between keypoint-based tracking to earlier classical computer vision methods, which is not what was asked (and is not relevant here, as neither BehaviorDEPOT nor JAABA is a pose estimation tool.) Rather, the key aspect of JAABA's success, as indicated by Reviewer 1, is its use of an optimized version of the GentleBoost algorithm, which takes in a large set of features and selects the small subset that is best suited to classification. I agree with Reviewer 1 that allowing a classifier to select the most informative features is a strong approach that is tough to beat. The authors do make the potentially valid point that classifiers using small sets of hand-crafted features may require less training data, although I don't think enough is shown for them to concretely state that BehaviorDEPOT is more efficient to set up than an appropriately regularized supervised classifier. (For example, how long does it take to annotate training data for a supervised classifier, vs how long did it take to create the new object-investigation detector from scratch?)

3) One last minor point on the subject of classifiers, I'd like to push back on the author's claim that supervised classification tools like SimBA and MARS are for detecting behaviors that are "difficult to see by eye"-this claim doesn't make any sense given that these tools require human annotations to train in the first place.

4) While supplementary Table 4 is helpful, it doesn't answer the question asked, which is "how good does my pose estimation need to be for the classifier to work well"- to do so, you would need to train pose models with different amounts of training data, to see how classifier performance depends on either training set size or mean DLC error, within a given dataset. This would help users figure out whether adding more DLC training data can be expected to improve the performance of the classifier.

5) In response to Reviewer 2's question about camera position, the authors present a new "jitter"-based freezing classifier. They write in the text "in videos recorded from the side, the velocity-based freezing classifier may be slightly affected by distortions in velocity calculations caused by the angle (e.g. when the mouse is moving towards/away from the camera). On the other hand, the 'jitter classifier' should work equally well with any viewing angle as long as tracked points remain generally unobscured." However, in the response to the reviewer, they write "We did not explicitly test our freezing classifier in videos recorded from the side or other angles, but there is no reason to think it wouldn't work since keypoints can be tracked from any angle." It is simply not reasonable to assume a method designed exclusively in one condition will work in another very different condition, let alone work "equally well." This claim is purely speculative and should be removed.

6) The authors also seem to misinterpret Reviewers 2 and 3 questions about annotation and pose data formats. For example, the authors write "BehaviorDEPOT can process pose tracking data in CSV and H5 file formats. Keypoint data collected by any software is fundamentally compatible with BehDEPOT". DeepLabCut data is saved in CSV or H5 formats, but there is additional file structure that must be known to be able to parse those files to extract the data (eg which variables to read, which columns are x vs y coordinates). A different pose estimation tool like SLEAP might still save pose data in an H5 format, but because it uses different file structure conventions, code written to unpack DLC pose data would return an error when run on SLEAP data. While any software is "fundamentally compatible" with BehaviorDEPOT, software other than DLC would require the creation of a conversion script to make sure keypoint data is in the expected format. (As the authors experienced with APT, this is easier said than done, as keypoint storage formats can change with the software version.) The authors should instead perhaps state whether they commit to providing support for new pose formats when requested by users.

Reviewer #2:

The authors have responded to the points from the initial review, including added descriptions of how the classifier works as well as a comparison to JAABA.

While testing the demo for ease of use, I found that it does not simply run as downloaded. For example, the demo functions use variables (like Tracked.raw from the csv file) which do not exist. I could fix this in the code myself but if targeted toward an audience with no coding experience, these examples should be simple to run.
