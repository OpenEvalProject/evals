# Peer review - Round 1

Editors:
- Matthieu Louis, https://ror.org/02t274463 University of California, Santa Barbara United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.86585.sa0](https://doi.org/10.7554/eLife.86585.sa0)

This study describes a useful method to monitor the behavior of Drosophila larvae in a uniform environment over much longer time scales than was possible with previous methods. The authors provide a solid characterization of aspects of the method and show that the behavior of single larvae can be quantified over several hours. The experiments offer a proof-of-concept for a robotic device that will enable the investigation of behavior in long-term experiments in ways that were previously unimaginable.


---

# Peer review - Round 1

Editors:
- Matthieu Louis, https://ror.org/02t274463 University of California, Santa Barbara United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.86585.sa1](https://doi.org/10.7554/eLife.86585.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Continuous, long-term crawling behavior characterized by a robotic transport system" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and K VijayRaghavan as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The reviewers appreciate the qualities and future impact of the method you have developed to study the long-term behavior of Drosophila larvae. The observation of a bimodal distribution in the navigation index of single larvae highlights that mean behaviors measured over short observation times can mask diversity in the behaviors of individual animals. You provide strong evidence that your system will be useful to other laboratories interested in prolonged recording of larval activity. However, several weaknesses of the manuscript should be addressed prior to its publication. The revision does not require the collection of additional data. Generally, you should provide a more thorough description of where your method fits with respect to published work and how the method itself works. More specifically, we recommend that you implement the following changes:

– Improve the introduction to more accurately reflect previous work done to study behavior in worms and rodents over long durations.

– Provide additional information about the training process of the neural network used to track larvae. Please ensure that the method is reproducible and customizable by other labs.

– Discuss the implications of physical perturbations during the picking and transportation of an animal. These perturbations are likely to affect subsequent behavior, which might preclude the study of prolonged free-moving exploration. These limitations should be discussed in the manuscript.

– Comment on the ability of the tracker to maintain the identity of single larvae over prolonged periods of time.

Reviewer #1 (Recommendations for the authors):

Introduction:

43: More focus is needed for clarification. What is the problem you are trying to solve? It is very much larva-specific but that is not clear at all from the introduction. Both the aim of the work and the relative background in the literature can be defined in greater detail. High throughput analysis of behavior, in general, is possible and not prohibitive at all. Examples are the Drosophila activity monitors (commercial) and the ethoscope (open source). Both are able to record the activity of adult animals throughout their lifespan, in high throughput.

87: There is an issue here with how you define exploration. Picking an animal from the border of an arena to place it back in the center is not a way to prolong exploration. It's certainly a way to prolong crawling behaviour but not necessarily exploration. You are basically mimicking a conveyor belt here: it can certainly be useful but I don't think it has much to do with exploration. In fact, it would be important to think of this concept in ecological terms and ask: for how long will a larva crawl/explore its natural environment? Will a larva in an apple crawl continuously for 30 hours, as it does in this device?

315: I suppose you refer to melanogaster only, or do you mean all Drosophila species?

Figure 1: I don't think the concept exposed in E is so difficult to require illustrations. F is really difficult to understand and thus not informative. Perhaps replace it with a supplementary video of the picking process?

Figure 5: Not clear how to interpret this figure. What are the dashed and continuous lines? What does the P*** refer to? You refer to a "clear increase in navigation index" but this is not clear by looking at the figure.

Figure 6: I am afraid I do not understand the reasoning behind this experiment. This would really benefit from a clearer and more accessible explanation, in terms of aims and methods.

Reviewer #2 (Recommendations for the authors):

My only comment to the authors is that it would nice to see additional paths in the very long duration recordings. Are some larvae right-handed while others are predominantly left-handed?

Reviewer #3 (Recommendations for the authors):

– I don't think Figure 1A is cited in the text.

– Line 185: How long are the occlusions by the robot arm and how far does a typical larva move (perhaps as a fraction of body length) during the occlusions?

– Line 326: Is "navigational effectiveness" a standard term? If not, I wonder if a better term might be something like navigational cosine? The reason I ask is that if a larva has reached a desired temperature in a gradient then the "effective" thing to do might be to stop moving or move orthogonally to the gradient which would have a Navigational Effectiveness of 0.

– Line 343: include details of statistical test.

Suggestions for improvement:

– Include lines on the time series in Figure 4 to show the picking times.

– In general, the data in Figure 4 is tantalizing, but because it's based on a single observation we can't rule out the increase in speed later in the recording isn't due to chance or some environmental change in the room. The most interesting thing would be to include some more data, but if that's not possible, including some more discussion of possible causes (including those that don't have anything to do with larval biology) in the text might help.
