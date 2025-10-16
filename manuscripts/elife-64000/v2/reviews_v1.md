# Peer review - Round 1

Editors:
- David Lentink, Stanford University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64000.sa1](https://doi.org/10.7554/eLife.64000.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The paper by Walter and Couzin describes new open-source software to track individual animals, such as fish and insects, moving and interacting within groups in a quasi-two-dimensional plane. The method assumes controlled lighting conditions and a stationary camera, which facilitates ease of use and fast data analysis. The software is useful for animal behaviour, neurobiology and comparative biomechanics research. The authors report assessments of accuracy, run-time, and memory consumption, which illustrate this open-source solution is state-of-the-art. The invaluable utility of this open-source tool is enabled by how many standard and robust algorithms are combined in a single functional package. A particular strength of the present framework is the unusually large number of individuals that can be tracked simultaneously in real-time, enabling new virtual-reality manipulative studies of collective behaviour.

Decision letter after peer review:

Thank you for submitting your article "TRex, a fast multi-animal tracking system with markerless identification, and 2D estimation of posture and visual fields" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Christian Rutz as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Sergi Pujades (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this decision letter to help you prepare a revised submission. Please address the comments and suggestions to the best of your ability, mark all changes in the revised manuscript using a blue font, and provide a point-by-point response to the issues raised. This will significantly facilitate the Reviewing Editor's evaluation of your revision.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

The paper by Walter and Couzin describes new open-source software to track individual animals such as fish and insects moving and interacting within groups in a quasi-two-dimensional plane. The method assumes controlled lighting conditions and a stationary camera, which facilitates ease of use and fast data analysis. The software is useful for animal behaviour, neurobiology and comparative biomechanics research. The authors demonstrate this utility based on assessments of accuracy, runtime, and memory consumption, which illustrate this open-source solution is state-of-the-art. While the authors rightfully point out that their system is applicable to essentially any animal species, their tests were mainly on fish and insects, which have relatively limited deformations and appearance changes compared to many mammals and other organisms with dynamically morphing body shapes. The invaluable utility of this open-source tool is enabled by how many standard and robust algorithms are combined in a single functional package. A particular strength of the present framework is the unusually large number of individuals that can be tracked simultaneously in real-time, enabling new virtual-reality manipulative studies of collective behaviour.

Essential revisions:

Abstract: Please mention that background subtraction is the key default segmentation approach. Clarify that limb position of highly deformable bodies is not tracked.

To put the contribution of the software into perspective, it would be helpful to add in the conclusions the assumptions made on the shape of the animals (subsection “Posture Analysis”), and please provide examples of animals which do not fall into this category, to help the general eLife readership comprehend both the promise and limits of the new method.

Subsection “Realtime Tracking Option for Closed-Loop Experiments”: Please clarify what "very outdated " or "low-end" is in this context. Specs are given in the Results. This could be rephrased in the line of: "Problems of using a lower hardware as the recommended one (ref) lead to.… frame-rates, fragmented data and bad identity assignments." Please address.

"QR codes" are more correctly called "fiducial markers" (and mostly QR codes themselves are not used).

Subsection “Automatic Visual Identification Based on Machine Learning”: To our understanding, James Crall and Stacey Combes performed a thorough study documenting the effects of these fiducial markers ("QR codes") for tracking and quantifying bee behaviour. It would be useful to cite this work, because it shows such documentation can be done although it is not trivial.

The final training:

Is a validation set kept to avoid overfitting? The procedure to check on "uniqueness improvement" is not clearly described. This could be improved.

Figure 1B: The text in the figure seems to imply that Trex would do real-time online tracking, but isn't this the case for TGrabs only? Please double-check the implication of the text in this figure to make sure it is what you wish to communicate to the reader.

Figure 2: Exports: Does TRex export to.csv? It seems .npz only, correct? Also in the Introduction.
