# Peer review - Round 1

Editors:
- Mark CW van Rossum, University of Nottingham United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.56212.sa1](https://doi.org/10.7554/eLife.56212.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

While traditional models of the development of the sensory cortices have relied on efficient coding principles and passive information processing, more recently active models have started to appear that minimize reconstruction error. In this paper Klimmasch et al., show that such model reproduce a number of experimental phenomena when applied to binocular vision.

Decision letter after peer review:

Thank you for submitting your article "The development of active binocular vision under normal and alternate rearing conditions" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Joshua Gold as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Laurent Perrinet (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This paper demonstrates that the Active Efficient Coding (AEC) model that Shi and Triesch have presented in several previous papers is also able to reproduce standard results regarding the effects of abnormal visual experience.

Essential revisions:

1. There seems to be quite a bit of overlap in this study and your recent PNAS paper ("Active efficient coding explains the development of binocular vision and its failure in amblyopia"). It is critical for you to provide a strong, detailed explanation of the key differences between the two studies and how the present work represents substantially new insights.

2. As we understand, the action perception loop is "closed" by enacting the differential change in eye movements to the simulator. It is therefore different from other strategies like Active Inference for which a feedback prediction signal may be sent from motor to sensory systems. This difference should be highlighted in the text. Also, we are surprised that the study uses a very elaborate simulation system but that you simply show a planar image of a natural image and not a three-dimensional scene. Do you observe vergence movements if you scan the image? Finally, concerning the experimental procedure it is specified line 100 that "The plane is positioned in front the agent at variable distances" but no detail is given until Figure 8B (or we missed something).

3. A simple mathematical treatment could likely predict some results you have found, for instance the property that the network detects the right vergence for RDS. As a binary white noise, one can predict the distribution of activated coefficients for different disparities, especially given the kind of fits you perform on the basis functions. Also some elements on the bibliography of modeling emergence of binocular disparity (e.g., doi: 10.1523/JNEUROSCI.1259-18.2018) are lacking. These points should be clarified, including possibly de-emphasizing the RDS results if their novelty and importance to the overall message cannot be better established.

4. Some details lack in the presentation of the model, in particular concerning sparse coding (lines 474-488 page 15). Indeed, you explain the sparse coding scheme, but not how you implement sparse Hebbian learning. Either more details (e.g., equations) or references to existing work are needed. Also, how do you control the equalization of the coefficients? The pooling procedure generates some form of histogram (marginalization over all positions) and it is lacking in figure 1 and the generality of this procedure should be illustrated, for instance by comparing it to other schemes using histograms of features to classify images.

5. A nice extension of this model would be to predict how one could recover disparity acuity after abnormal rearing such as strabismus. For instance, it has been shown that patching the weak eye could be more effective that the usual strategy of patching the dominant eye (see Zhou, J, Reynaud, A., Yao, Z., Liu, R., Feng, L., Zhou, Y. and Hess, R. F. (2018) Amblyopic suppression: passive attenuation, enhanced dichoptic masking by the fellow eye or reduced dichoptic masking by the amblyopic eye?. Investigative Ophthalmology and Visual Science, 59, 4190-4197. for instance). Could you predict such a methodology? Predict another one?
