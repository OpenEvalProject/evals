# Peer review - Round 1

Editors:
- Tatiana Pasternak, University of Rochester United States

Reviewers:
- Elizabeth A Buffalo

## Review text

DOI: [10.7554/eLife.47596.014](https://doi.org/10.7554/eLife.47596.014)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Population response magnitude variation in inferotemporal cortex predicts image memorability" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Timothy Behrens as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Elizabeth A. Buffalo (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The reviewers were impressed with several aspects of the work, including linking the strength of the overall population response in IT to memorability and the idea that coding schemes for memorability and identity may be orthogonal. However, they raised a number of issues that should be addressed, before the paper will be considered for publication in eLife. These are listed below.

Essential revisions:

1) Please provide the rationale for not utilizing the monkey behavioral data to directly link the strength and variability of responses to behavior. The question how the monkey IT was trained in classification needs to be clarified.

2) Please address the question of the role of learning and experience in making some images more memorable. A related question is whether IT population response depends on whether the stimuli are novel or familiar. This important question cannot be addressed with responses that are averaged across the two groups of stimuli, as it is currently the case.

3) Please clarify the approach used to create pseudopopulations since some of the data was likely to be collected for simultaneously recorded neurons and combined with the data collected on other days.

4) Please address the question whether model predictions can be used to modify images to increase their memorability.

5) Please discuss whether the face and body parts are the features with the highest positive correlation to memorability.

6) Please address the effect of categorization training on correlations between the model responses on image memorability and on the population response magnitude.

Reviewer #1:

In this paper, Jaegle and colleagues explore the connection between population responses in IT cortex and image memorability. Their hypothesis is that images that evoke a stronger population response will correlate positively with the likelihood of being able to remember that image. Using a combination of model predictions prom human experiments and their IT recordings, they obtain evidence supporting this hypothesis. Taken together, the authors suggest that prior attempts to reduce variability in population responses may have missed this potentially important connection.

The basic message in this paper is relatively clear, with the notion that overall response levels might both be variable and that this variability can be directly linked to behavior is intriguing. The paper is weakened considerably by the fact that the monkey behavioral data are not really used to draw these conclusions (Figure 2C does present a version of this, but it doesn't really form the basis for the core analyses). Indeed, the authors have a nicely designed behavioral paradigm, and we don't even see the effect of delay on the monkeys' performance. The main correlations are between the memorability predictions from the model designed to predict behavioral in human participants and evoked pseudopopulation response magnitudes. While the inability to clearly connect the behavioral data to the neural data in the same experiment is somewhat disappointing, the authors do point out that the relation may be explained by the development of representations that are more generally a results of having to classify objects, which could be preserved between species. This may be true, but exactly how the monkey's IT cortex has been trained in classification is not entirely clear.

A related question that the paper raises that is not directly addressed is how specific learning or training could alter their findings. It would seem that specialization of neural representations resulting from training could make certain images more memorable than others as a function of experiences. While it seems like the authors are assuming that they are sampling a large space where no subset of image would likely be more familiar or experienced than others, it might be worth at least discussing how experience might affect their results. Further, the authors clearly didn't target any particular cell populations, but they could have landed in a cluster of specialized cells (faces or other categories). It's not clear how their hypotheses would account for this?

Another point that I thought could have been briefly discussed is the relation of this work to the large literature of studies of memory formation, wherein activity at the time of encoding can affect subsequent recall. This work is clearly distinct from that, but that distinction could be made more clear.

I found the description of the creation of the pseudopopulations a bit difficult to follow (Materials and methods section), which leaves me somewhat concerned about the conclusions that are drawn from these. What happens when the sessions with 20 or so sites are used to make predictions, as these populations are real and simultaneously collected under identical conditions?

Do the authors have any approach for using their network predictions to help modify images to make them more or less memorable? This would be a powerful manipulation if it directly affected neural responses.

Reviewer #2:

In this manuscript, Jaegle et al. examine the hypothesis that variation in the magnitude of the population response of neurons in the monkey inferotemporal (IT) cortex is positively correlated with image memorability. The authors analyze a pseudo population of 707 IT units recorded as monkeys performed a recognition memory task with a large set of complex images, with each image presented once as novel and once as familiar. The data suggests that while image identity can be decoded through the population vector direction (as shown in DiCarlo et al., 2012), image memorability correlates with the response magnitude of the population, with higher magnitude population response reflecting greater image memorability. In addition, the authors probed CNN models trained to categorize objects and found that larger magnitude responses in higher layers of the network correlated with images that had high memorability. The question of how neural activity in IT contributes to recognition memory is not well understood, and the hypothesis that memorability and identity may be related to orthogonal population responses is novel and intriguing. The manuscript is well-written and should be of interest to a wide audience. I have just a few suggestions to improve clarity.

1) In constructing the population response, each neuron's response to a given image is averaged across the novel and familiar presentation. Because memorability is defined here as a bottom-up feature of the stimuli, it would be interesting to know whether there was a change in the IT population response for novel vs familiar presentations. If experience affected the response, then, presumably, the response to just the novel presentation would provide the strongest correlation with memorability.

2) The data in Khosla et al. suggests that memorability is strongly related to salience, in that stimuli with more consistent fixation locations across subjects had higher memorability. It would be helpful to discuss the extent to which memorability is thought to reflect something beyond image salience. That is, would it be expected that IT population response magnitude (and the monkey's recognition memory performance) would also be positively correlated with a measure of image salience?

3) Khosla et al. also suggest that CNN features with the highest positive correlation to memorability correspond to faces and body parts. It would be helpful to discuss whether this relationship to IT stimulus selectivity may underlie the relationship between IT population response magnitude and the memorability index.

4) The authors report a correlation between responses in higher layers of the CNN and image memorability after categorization training. It would be interesting to know what effect the categorization training had on population responses, i.e., did the training produce a separation in population magnitude across images that was more consistent early in training or was there a more complex relationship between training and population response magnitude?
