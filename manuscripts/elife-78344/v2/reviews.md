# Peer review - Round 1

Editors:
- Brice Bathellier, https://ror.org/02feahw73 CNRS France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78344.sa0](https://doi.org/10.7554/eLife.78344.sa0)

This article presents a novel realtime processing pipeline for miniscope imaging which enables accurate decoding of behavioral variables and generation of feedback commands within less than 50ms. The efficiency of this important tool for experiments requiring close-loop interaction with brain activity is demonstrated based on compelling measurements in two experimental contexts. This pipeline will be useful for a wide range of questions in system neuroscience.


---

# Peer review - Round 1

Editors:
- Brice Bathellier, https://ror.org/02feahw73 CNRS France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78344.sa1](https://doi.org/10.7554/eLife.78344.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "A hardware system for real-time decoding of in-vivo calcium imaging data" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Brice Bathellier as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Laura Colgin as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Provide a clear estimate of position accuracy that can be achieved with a space metric and not with a classifier accuracy with space bins whose size is unclear. Compare position estimates to what would be obtained from electrophysiology based on the literature.

2) Please provide a spatial distribution of speed, acceleration, arrests, and a description of the number of place cells and of the size of the place fields. Related to that, it is crucial to provide a plot of the accuracy of spatial decoding against spatial location to appreciate the performance of the system in real conditions, knowing that in linear tracks place fields are not homogeneously distributed.

3) Improve the description of the methodology and of imaging speed with respect to displacement speed according to referee 2's comments. It is particularly important to explain how much exploration time is needed to train the real-time classifier.

4) Provide an evaluation of the localisation information available in corrected motion artefacts in order to rule out that residual motion artefacts do not provide spatial information.

5) Repeat the experiment in a more complex environment, such as a 2D arena, in order to demonstrate the versatility of the method.

6) Provide a direct comparison of real performances based DeCalciOn to two previous online calcium imaging algorithms. The technical innovations of this work would be better highlighted by directly testing all three of these algorithms, ideally on similar datasets.

7) Provide a quantification of the spatial error (across different locations, and running speeds) made in a virtual experiment in which the goal is to emit a TTL signal at a specific location of the animal. The difference with point 7 is that this quantification includes not only classifier inaccuracies but also the time delay of the real time device in relation to the speed of the animal.

Reviewer #1 (Recommendations for the authors):

– Provide a clear estimate of position accuracy that can be achieved with a space metric and not with a classifier accuracy with space bins whose size is unclear.

– Provide measurements in 2D and estimates of both location and head direction. How does it compare with electrophysiology? Are the conclusions about the lack of importance of cell body identification still holding for these conditions?

Reviewer #2 (Recommendations for the authors):

– There is not enough information about the behavior. Please provide a spatial distribution of speed, acceleration, and arrests. Is there an influence on the decoding accuracy?

– There is not enough information about the place cells. How many place cells? What is the spatial information of the cells? What are the size of the place fields?

– Some details are lacking or are not explicitly described. For instance, I think the following information should be easier to obtain in the article. The 2.5m linear track is split into 13 regions, leading to regions of roughly 20cm. In linear tracks rats run with an average speed of 70cm.s-1, with maximum speed going up to 100cm.s-1. This means that running rats will stay between 280ms to 400ms in each zone. The video frames are down-sampled to 15 frames/s leading to 66ms between each frame. This implies that 4 to 6 frames will correspond to the same location.

– A clearer description of the methodology might help the reader:

Here is a short overview of the methodology:

Technological methodology:

Step 1: Correct for translational movement of brain tissue. Aa 128x128 pixel area with distinct anatomical features was selected within the 512x512 cropped subregion to serve as a motion stabilization window;

Step 2: ACTEV removes background fluorescence from the 512x512 image;

Step 3: ROI definition: The enhanced image then is filtered through a library of up to 1,024 binary pixel masks (each up to 25x25 in size) that define ROIs within fluorescence is summed to extract calcium traces;

Step 4: Decoding. Population vectors of extracted calcium trace values are stored in the DRAM, and then decoded by sending them as inputs to a linear classifier running on the MPSoC's ARM core.

Experimental methodology:

Step 1: collect an initial imaging dataset and store it on the host PC;

Step 2: pause for an intermission to identify cell contours if necessary (this is only required for contour-based decoding; see below) and train a linear classifier to decode behavior from the initial dataset;

Step 3: upload classifier weights from the host PC to the Ultra96;

Step 4: perform real-time decoding with the trained classifier.
