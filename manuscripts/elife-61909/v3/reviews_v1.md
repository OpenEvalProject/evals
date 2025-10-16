# Peer review - Round 1

Editors:
- Gordon J Berman, Emory University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.61909.sa1](https://doi.org/10.7554/eLife.61909.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This submission introduces a new set of software tools for implementing real-time, marker-less pose tracking. The manuscript describes these tools, presents a series of benchmarks, and demonstrates their use in several experimental settings: including deploying low-latency closed-loop events triggered on an animal's pose. The first key development presented is a new python package – DeepLabCut-Live! – which optimizes pose inference to increase its speed, a key step for real-time application of DLC. The authors then present a new method for exporting trained DLC networks in a language-independent format and demonstrate how these can be used in three different environments to deploy experiments. Importantly, in addition to developing their own GUI, the authors have developed plugins for Bonsai and AutoPilot, two software packages already widely used by the systems neuroscience community to run experiments.

Decision letter after peer review:

Thank you for submitting your article "Real-time, low-latency closed-loop feedback using markerless posture tracking" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Gordon Berman as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Timothy Behrens as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Tiago Branco (Reviewer #2).

The reviewers have discussed the reviews with one another, were largely positive about the article, and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

This submission introduces a new set of software tools for implementing real-time, marker-less pose tracking. The manuscript describes these tools, presents a series of benchmarks and demonstrates their use in several experimental settings, which include deploying very low-latency closed-loop events triggered on pose detection. The software core is based on DeepLabCut (DLC), previously developed by the senior authors. The first key development presented is a new python package – DeepLabCut-Live! – which optimizes pose inference to increase its speed, a key step for real-time application of DLC. The authors then present a new method for exporting trained DLC networks in a language-independent format and demonstrate how these can be used in three different environments to deploy experiments. Importantly, in addition to developing their own GUI, the authors have developed plugins for Bonsai and AutoPilot, two software packages already widely used by the systems neuroscience community to run experiments.

All three reviewers agreed that this work is exciting, carefully done, and would be of interest to a wide community of researchers. The consensus was the this was a strong submission. There were, however, four points that the reviewers felt could be addressed to increase the scope and the influence of the work (enumerated below).

Essential revisions:

1) The fundamental trade-off in tracking isn't image size vs. speed, but rather accuracy vs. speed. Thus, the reviewers felt that providing a measure of how the real (i.e., not pixel space) accuracy of the tracking was affected by changing the image resolution would be very helpful to researchers wishing to design experiments that utilize this software.

2) The manuscript would also benefit from including additional details about the Kalman filtering approach used here (as well as, potentially, further discussion about how it might be improved in future work). For instance, while the use of Kalman Filters to achieve sub-zero latencies is very exciting, it is unclear how robust this approach is. This applies not only to the parameters of the filter itself, but also on the types of behavior that this approach can work with successfully. Presumably, this requires a high degree of stereotypy and reproducibility of the actions being tracked and the reviewers felt that some discussion on this point would be valuable.

3) A general question that the reviewers had was how the number of key (tracked) points affects the latency. For example, the “light detection task” using AutoPilot uses a single key-point, how would the additional of more key-points affect performance in this particular configuration? More fully understanding this relationship would be very helpful in guiding future experimental design using the system.

4) The DLG values appear to have been benchmarked using an existing video as opposed to a live camera feed. It is conceivable that a live camera feed would experience different kinds of hardware-based bottlenecks that are not present when streaming in a video (e.g., USB3 vs. ethernet vs. wireless). Although this point is partially addressed with the demonstration of real-time feedback based on posture later in the manuscript, a replication of the DLG benchmark with a live stream from a camera at 100 FPS would be helpful to demonstrate frame rates and latency given the hardware bottlenecks introduced by cameras. If this is impossible to do at the moment, however, at minimum, adding a discussion stating that this type of demonstration is currently missing and outlining these potential challenges would be important.

Again, though, the reviewers were very enthusiastic about this Tools and Resources submission, and the above points primarily point towards ways in which the authors could increase the manuscript's impact, rather than fundamental concerns about its validity or overall value to the community.
