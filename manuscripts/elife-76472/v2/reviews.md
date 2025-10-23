# Peer review - Round 1

Editors:
- Hang Zhang, https://ror.org/02v51f717 Peking University China

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76472.sa0](https://doi.org/10.7554/eLife.76472.sa0)

This paper addresses the long-standing problem of color categorization and the forces that bring it about, which can be potentially interesting to researchers in cognition, visual neuroscience, society, and culture. In particular, the authors show that as a "model organism", a Convolutional Neural Network (CNN) trained with the human-labelled image dataset ImageNet for object recognition can represent color categories. The finding reveals important features of deep neural networks in color processing and can also guide future theoretical and empirical work in high-level color vision.


---

# Peer review - Round 1

Editors:
- Hang Zhang, https://ror.org/02v51f717 Peking University China

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76472.sa1](https://doi.org/10.7554/eLife.76472.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Color categories emerge in object learning" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Tirin Moore as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Bevil Conway (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Below is a list of revisions that we think are essential:

1) The authors need to experiment with other network architectures and different image datasets to show WHY and under WHAT circumstances color categorization may emerge or not emerge from a pre-trained network. Each of the three reviewers has offered some specific suggestions on how to do this. Please see their comments for details.

2) The authors need to show how their modeling results agree with existing psychophysical or physiological data of humans and animals. Otherwise, the biological relevance of the work might be limited. Please see Reviewer 3's comments for details.

3) Regarding the theoretical implications of their work, the authors are recommended to provide a more thorough discussion of the relationship of their findings with previous theories for color categorization and weaken claims such as "categories can emerge independent of language development". Please see Reviewers 1's and 3's comments.

Reviewer #2 (Recommendations for the authors):

Here are some of my suggestions:

They already apply k-means analysis on the image's pixels to show that there exist a few color clusters. But the clusters only match the revealed color category in other experiments partially. So they can also apply the similar k-means analysis of the units' responses in different layers of CNN to see how the color categorical information develops from layer to layer.

If the color categorical information emerges from the usefulness of object recognition, it might be interesting to see similar experiments with two other kinds of CNN as control:

1) Untrained CNN 2) CNN trained with images of which color information is not useful for object recognition. Recently, a few studies suggest that the untrained CNN can do face detection tasks (Baek et al., 2021) or do the enumeration task (Kim et al., 2021). Whether the color categorical perception can emerge from an untrained CNN will be very interesting. Also, if we really want to nail down the relationship between color categorical perception and object recognition, they might want to remove the relation between the color information and the object information. If a CNN is trained with these kinds of stimuli, can the similar color category emerge?

The paper lacks a direct comparison between the CNN and human subjects. The revealed color categories in CNN in the paper seem to be very reliable. Would these categories be similar to those observed in previous human behavior studies? If they were the same, that would strengthen the claim of the paper; if they were not, what are the possible reasons that would explain the difference?

Reviewer #3 (Recommendations for the authors):

The paper at this stage is a modeling paper without any human psychophysics. What we learned is behavior of a CNN. To my understanding, the only connection to humans is that the image dataset is labeled by humans. There are no comparisons to human psychophysics. To support the connection between the model results and human color categorization, especially the role of language and development in animal and human color categorization, the authors need to do more perceptual experiments or model previous empirical results from human vision. Otherwise, I suggest the authors remove some of these discussions and focus on the findings that color categorization might emerge through learning to classify objects. Perhaps, to strengthen the paper, an alternative model should be proposed (e.g. network trained NOT on a broad object dataset might NOT represent color categories) or results from an alternative CNN architecture other than ResNET.
