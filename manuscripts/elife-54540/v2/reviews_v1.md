# Peer review - Round 1

Editors:
- David Kleinfeld, University of California, San Diego United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.54540.sa1](https://doi.org/10.7554/eLife.54540.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

String-pulling by rodents is a canonical task in the assessment of spinal cord function in normal and neurologically compromised mice. The laboratories of Whishaw and Mohajerani demonstrate algorithms to automate the study of postural and hand kinematics in string-pulling behavior. This adds a new dimension to the routines available for high-throughput, high-volume studies of behavior.

Decision letter after peer review:

Thank you for submitting your article "A Matlab-based toolbox for characterizing behavior of rodents engaged in string-pulling" for consideration by eLife. Your article has been reviewed by two expert and respected peer reviewers, and the evaluation has been overseen by David Kleinfeld as Reviewing Editor and Kate Wassum as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and with the Reviewing Editor, and they find considerable merit in your Resources contribution, which addresses quantification of a behavioral paradigm of increasing importance and use in the spinal cord circuit community. However, the reviewers raise a number of strong and legitimate concerns that we ask be addressed. The Reviewing Editor has drafted this decision to help you prepare a revised submission.

Coordination of limb movement is a hallmark of spinal cord motor control. Rope pulling, which involves such coordination in addition to proper posture and grasping, is a critical task in the study of spinal circuits. This work describes a set of software tools for the automated characterization of this behavior, and thus provides a valuable tool for the behavioral characterization of spinal circuits and experimental modification of those circuits.

Essential revisions:

Some of these steps will require new data analysis.

Please clarify the specifics of your tracking accuracy. "The paper states that "our methods can provide group truth data for validating the results of neural network-based tagging of body parts." It is not clear how this conclusion is derived."

Please address the robust nature of your approach. "It is unclear how robust the segmentation is to variations in the video, such as camera angle relative to the mouse, illumination conditions, and color of the mice. For example, the paws of the white mice could not be reliably tracked, and the authors had to use markers to paint the paws. This suggest variations in the video could strongly affect the outcome."

Please simplify the statistics and justify all measures. "… while central-tendency results show large difference in speed between Black and White mice, it is unclear how spatial entropy, sharpness, Hausdorff fractal dimension, Higuichi fractal dimension, Fano Factor, and Entropy support this effect". Nor is the necessity of bringing these statistical measures made clear.

Please bring trial-averaged data. As string-pulling is a highly repetitive near rhythmic behavior, it would be useful to see the average cycle of the behavior to understand the stereotypical hand movements. Such response could be computed from the data of Figure 10 and 11 by warping each pull cycle to a common time base. Then "compare descriptive statistics to quantify differences in hand movement trajectories across White and Black mouse groups."

Please discuss the generality of your software. It would be useful to see if the software for string pulling could be adapted to "… analyze limb movements during pasta handling, thereby showing general applicability of the software."

Please discuss the support and maintenance. Further, the poor documentation must be improved and the associated GitHub must be organized

Please explicitly spell out the advantages of your approach over related methods. In this regard, address the black-box method of "DeepLabCut" and the "Janelia Animal Part Tracker".

Lastly, please make the toolbox available to be downloaded in Matlab 2019b (reviewers were unable to successfully download).

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "A Matlab-based toolbox for characterizing behavior of rodents engaged in string-pulling" for further consideration by eLife. Your revised article has been evaluated by Kate Wassum as the Senior Editor, and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

The reviewers would like you to please provide more discussion of the significance of these findings for an average audience. The data show how whole-body measurements could be used to reveal differences in motor kinematics between mouse strains. These analyses suggest that Swiss Webster Albino (white) mice exhibit faster movements that are more localized to the forelimb compared to black 6 mice. What is the significance of these differences? For example, the authors interpret these differences as the white mice using a "more primitive strategy" than the black mice. In addition, the white mice were considered to have "exaggerated compensatory adjustment" and "impaired individualized arm/hand movements". Please elaborate on how these conclusions were derived and what are the implications for future studies?

We also noted a number of typos and errors in figure references. Here are some examples:

– In the first paragraph of the subsection “Comparison with artificially intelligent machine learning based software”, Figure 2.11 is likely referring to Figure 12.

– At the end of the first paragraph of the subsection “Robustness and limitations of image segmentation and automatic detection of body parts”, the figure is incorrectly referenced. It is likely referring to Figure 15—figure supplement 1.

–The figure on Time Warping should be Figure 11—figure supplement 1, not Figure 15.
