# Peer review - Round 1

Editors:
- Jörn Diedrichsen, University of Western Ontario Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.48190.023](https://doi.org/10.7554/eLife.48190.023)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Independent representations of ipsilateral and contralateral arms in primary motor cortex" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Richard Ivry as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The paper provides an investigation into the neuronal responses in motor cortex during perturbations to the contralateral and ipsilateral arm. The main findings are that a) M1 represent the perturbations to both arms b) the responses to ipsilateral perturbations a slightly slower than those to contralateral perturbation (but see #2), and c) the population responses are orthogonal, allowing for independent encoding of both perturbations.

Essential revisions:

The reviewers highlighted 3 major areas of concerns that should be addressed:

1) The authors should provide more information about how recordings were combined across days. The Materials and methods state (subsection “Neural, EMG and kinematic recordings”) that neurons were recorded from 3 behavioral sessions spaced 2-3 months apart. Because the electrodes of chronically-implanted Utah arrays are not moved between sessions, there is always a concern that recordings from different days could be picking up an overlapping set of units. How many of the recorded neurons are shared across the recording days? How does this influence the statistical validity of the single neuron and population analyses presented in the paper (some of which are based on the assumption of statistical independence between units)?

2) The analysis of neural onset times is interesting and constitutes a novel major finding of the paper. However, the results could potentially be affected by the fact that contralateral perturbation responses tended to be larger than ipsilateral responses. If a neuron's response has the same time course in two conditions, but reaches a higher firing rate in one condition, then a set threshold for detecting the response time will yield an earlier for the higher firing rate condition. Does the earlier response time for contralateral movements still hold if controlling for the magnitude of firing rate changes? A subset analysis on neurons with matched response magnitudes (or a scatter plot of onset difference vs. response magnitude ratio) may be useful to address this concern.

3) The control analysis presented in Figure 8 should be clarified, revised or removed. One major concern was that the result presented in Figure 8B and C (larger spread of ipsilateral weights as compared to contralateral weights) may be statistical artifact related to the fact that the variances (or sums-of-squares) of the regressors (velocity of the contralateral and ipsilateral arm) are vastly different. The predicted variance of the regression coefficients is lawfully related to inverse of the variance of the regressor. More precisely in the context of multiple regression with design matrix X, the var(b) is proportional to inv(X'*X). Additionally, the ipsilateral movement is correlated to that on the contralateral arm, further increasing the variance of the weights.

Thus arguments of "higher sensitivity" or " context dependent selectivity" need to be carefully reinvestigated.

Overall, the reviewers also commented that the clarity of the writing needs to be improved.

Reviewer #1:

Overall, I found this paper to be well-written, with interesting and important implications for a major motor control mystery: how can motor cortex have neural responses during movements of the ipsilateral arm without evoking contralateral arm movements? The authors suggest that ipsilateral arm related activity resides within muscle null dimensions, thus enabling neural responses to cancel out at the level of downstream circuits, providing no net excitation. They use both single neuron analyses, neuron pair analyses, and state-space analyses to support their conclusion, providing strength and diversity of analyses. They further provide a very detailed analysis of neurons' responses to contralateral and ipsilateral arm perturbations, which helps to ground the paper and relate the conclusions to previous studies comparing contralateral and ipsilateral arm related responses in motor cortex. I have a few major suggestions, shared below, which I envision the authors should be able to fully address without major new experiments or analyses. If the authors address all of these concerns, I would be quite supportive of this paper's publication at eLife.

1) The authors should provide more information about how recordings were combined across days. The Materials and methods state (subsection “Neural, EMG and kinematic recordings”) that neurons were recorded from 3 behavioral sessions spaced 2-3 months apart. Because the electrodes of chronically-implanted Utah arrays are not moved between sessions, there is always a concern that recordings from different days could be picking up an overlapping set of units. Were any controls performed to ensure that no neurons were duplicated in the dataset?

2) The analysis of neural onset times could potentially be affected by the fact that contralateral perturbation responses tended to be larger than ipsilateral responses. If a neuron's response has the same time course in two conditions, but reaches a higher firing rate in one condition, then a set threshold for detecting the response time will yield an earlier for the higher firing rate condition. Does the earlier response time for contralateral movements still hold if controlling for the magnitude of firing rate changes?

Reviewer #2:

This manuscript describes a study of the activity in M1 in response to both ipsilateral and contralateral limb movements imposed by an exoskeleton. The title and Abstract are strongly focused on the second half of the study, the idea that the subspaces occupied by the activity driven by the two different arms are independent of one another. The types of methods they employ are being used in an increasing number of studies to investigate a wide range of properties of the networks of neurons that can be recorded by chronically implanted electrode arrays. The first (and lengthier) part of the study uses more traditional methods to analyze the basic properties of single neurons in response to perturbations of the two limbs. I edited the first part rather closely, until I got to the control section. I found the description to be unnecessarily hard to follow, but much more importantly, assuming I understood what they did, it raised major concerns in my mind, rather than alleviating any. Unless these can be adequately explained away, this strikes me as a tremendous amount of description and analysis of signals, the origin of which, is pretty unclear.

Comments related to my major concern:

“contralateral limb motion that was transferred through the body”. Meaning motion of the trunk with the arm stable, that causes shoulder rotation? Seems awfully unlikely. Doesn't the Kinarm constrain trunk motion?

“We addressed this by fitting the average neural activity when contralateral loads were applied to the average contralateral hand velocity in the perturbation epoch (data not shown).” I must not be following this, as I don't follow how this addresses the concern. You're trying to predict M1 from ipsilateral hand motion using a mapping derived from contra hand motion? I can't imagine that working well, or how it serves as a control. I gather the Kinarm was not being used to stabilize the non-moving limb?

“Contralateral and ipsilateral activity evoked a change in firing rate over a similar range for this neuron, but contralateral loads evoked larger hand speeds.” I find this to be really confusing. Activity doesn't "evoke" firing rate; that's how it's measured. Is that what you mean? Furthermore, is the (essentially zero) ipsilateral hand movement that which resulted from (was "evoked by") loads applied to the opposite limb? Unless I'm missing something pretty basic, this section is much more complicated than necessary. The opposite hand simply doesn't move. What more is there than that?

“We fit the evoked neural activity when ipsilateral loads were applied to the corresponding contralateral hand motion.” I confess I'm completely lost. What is meant by, "ipsilateral loads were applied to the corresponding contralateral hand motion." Does it mean mapping from the (tiny) non-moving hand speed to contralateral M1 activity?

“indicating the size of the ipsilateral weights were larger than the corresponding contralateral weights.” In fact, they differ by more than an order of magnitude, presumably because the non-perturbed ("contralateral") hand was moving so slowly. And yet the (tiny) hand movement accompanying loads on the opposite side of the body predicted contralateral M1 well? This causes major concerns about the validity of the entire study, if M1 activity is better predicted by the tiny contralateral hand movements than by the ipsilateral movements (albeit, that generalization was doomed from the outset). I wonder how well you can decode ipsilateral and contralateral limb movement from M1 activity when perturbations drive the ipsilateral arm? If they are of similar quality, or contra decoding is better, it would be a huge concern.
